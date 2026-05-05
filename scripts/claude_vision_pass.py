#!/usr/bin/env python3
"""Run Claude vision over rendered PDF pages and write markdown transcriptions.

Reads PNGs from `output/pdf/poppler-extraction/rendered-pages/<safe>/page-N.png`,
sends each page to Claude with a transcription system prompt, and writes
markdown to `output/pdf/claude-vision/pages/<safe>/page-N.md`.
Per-PDF combined files go to `output/pdf/claude-vision/full/<safe>.md`,
and a corpus file is written to `output/pdf/claude-vision/all-extracted-text.md`.

Resumes by skipping pages whose output file already exists. Use --force to redo.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import anthropic


SYSTEM_PROMPT = """You are transcribing a single page of a university-level Quantum Computing course.
Source pages may be: (a) typed/LaTeX problem statements, (b) handwritten lecture notes
on a tablet, (c) scanned handwritten exam answers, or any mixture.

Output requirements:
- Faithfully transcribe ALL legible content on the page into well-formed Markdown.
- Render math in LaTeX. Inline math: $...$. Display math: $$...$$.
  Use \\ket{...}, \\bra{...}, \\braket{...|...}, \\langle, \\rangle for Dirac notation.
- Preserve structure: numbered problems (1., 2., (a), (b)...), bullet points, headings.
- For diagrams, circuits, plots, or matrices that you can describe accurately,
  write a short bracketed description like `[Bloch sphere with |0> at top, |+> on +x axis]`
  or transcribe the matrix in LaTeX. Don't invent details you can't actually see.
- For illegible handwriting, write `[illegible]` rather than guessing. Partial guesses
  may be marked `[illegible: maybe "..."]`.
- Do NOT add commentary, summaries, headers like "Transcription:", or anything
  not present on the page. Output the page contents only.
- If the page is essentially blank, output a single line: `[blank page]`.
"""


@dataclass(frozen=True)
class PageJob:
    pdf_safe: str
    page_num: int
    png_path: Path
    out_path: Path


def natural_key(name: str) -> list[object]:
    return [int(p) if p.isdigit() else p for p in re.split(r"(\d+)", name)]


def discover_jobs(rendered_root: Path, out_pages_root: Path, force: bool) -> list[PageJob]:
    jobs: list[PageJob] = []
    for pdf_dir in sorted(rendered_root.iterdir(), key=lambda p: p.name):
        if not pdf_dir.is_dir():
            continue
        safe = pdf_dir.name
        pngs = sorted(pdf_dir.glob("page-*.png"), key=lambda p: natural_key(p.name))
        for png in pngs:
            m = re.match(r"page-(\d+)\.png", png.name)
            if not m:
                continue
            page_num = int(m.group(1))
            out_path = out_pages_root / safe / f"page-{page_num}.md"
            if out_path.exists() and not force:
                continue
            jobs.append(PageJob(safe, page_num, png, out_path))
    return jobs


async def transcribe_page(
    client: anthropic.AsyncAnthropic,
    model: str,
    job: PageJob,
    semaphore: asyncio.Semaphore,
    progress: dict,
) -> tuple[PageJob, str | None, str | None]:
    """Returns (job, text, error_message). text is None on failure."""
    async with semaphore:
        max_attempts = 8
        for attempt in range(max_attempts):
            try:
                image_bytes = job.png_path.read_bytes()
                image_b64 = base64.standard_b64encode(image_bytes).decode("ascii")

                async with client.messages.stream(
                    model=model,
                    max_tokens=8192,
                    system=[
                        {
                            "type": "text",
                            "text": SYSTEM_PROMPT,
                            "cache_control": {"type": "ephemeral"},
                        }
                    ],
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "image",
                                    "source": {
                                        "type": "base64",
                                        "media_type": "image/png",
                                        "data": image_b64,
                                    },
                                },
                                {
                                    "type": "text",
                                    "text": (
                                        f"Transcribe page {job.page_num} of "
                                        f"`{job.pdf_safe}`."
                                    ),
                                },
                            ],
                        }
                    ],
                ) as stream:
                    final = await stream.get_final_message()

                text_parts = [b.text for b in final.content if b.type == "text"]
                text = "\n".join(text_parts).strip()

                progress["done"] += 1
                progress["cache_read"] += final.usage.cache_read_input_tokens or 0
                progress["cache_create"] += final.usage.cache_creation_input_tokens or 0
                progress["input_tokens"] += final.usage.input_tokens
                progress["output_tokens"] += final.usage.output_tokens
                done = progress["done"]
                total = progress["total"]
                print(
                    f"[{done}/{total}] {job.pdf_safe} page {job.page_num} "
                    f"(in={final.usage.input_tokens}, out={final.usage.output_tokens}, "
                    f"cache_read={final.usage.cache_read_input_tokens or 0})",
                    flush=True,
                )
                return (job, text, None)

            except (anthropic.RateLimitError, anthropic.APIStatusError) as e:
                status = getattr(e, "status_code", None)
                if isinstance(e, anthropic.APIStatusError) and status is not None and status < 500 and status != 429:
                    return (job, None, f"{type(e).__name__}: {e}")
                wait = min(2 ** attempt + (attempt * 0.5), 60.0)
                print(
                    f"  retry {attempt + 1}/{max_attempts} for {job.pdf_safe} page {job.page_num} after {wait:.1f}s ({type(e).__name__})",
                    file=sys.stderr,
                    flush=True,
                )
                await asyncio.sleep(wait)
            except anthropic.APIConnectionError as e:
                wait = min(2 ** attempt, 60.0)
                print(
                    f"  connection retry {attempt + 1}/{max_attempts} for {job.pdf_safe} page {job.page_num}: {e}",
                    file=sys.stderr,
                    flush=True,
                )
                await asyncio.sleep(wait)

        return (job, None, "max retries exceeded")


def write_page(job: PageJob, text: str) -> None:
    job.out_path.parent.mkdir(parents=True, exist_ok=True)
    job.out_path.write_text(text + "\n", encoding="utf-8")


def assemble_per_pdf(out_pages_root: Path, out_full_root: Path, rendered_root: Path) -> list[Path]:
    full_paths: list[Path] = []
    for pdf_dir in sorted(rendered_root.iterdir(), key=lambda p: p.name):
        if not pdf_dir.is_dir():
            continue
        safe = pdf_dir.name
        page_files = sorted(
            (out_pages_root / safe).glob("page-*.md"),
            key=lambda p: natural_key(p.name),
        )
        if not page_files:
            continue
        chunks = [f"# {safe}\n"]
        for pf in page_files:
            m = re.match(r"page-(\d+)\.md", pf.name)
            if not m:
                continue
            page_num = int(m.group(1))
            body = pf.read_text(encoding="utf-8").rstrip()
            chunks.append(f"\n## Page {page_num}\n\n{body}\n")
        out_path = out_full_root / f"{safe}.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("".join(chunks), encoding="utf-8")
        full_paths.append(out_path)
    return full_paths


def assemble_corpus(full_paths: list[Path], corpus_path: Path) -> None:
    corpus_path.parent.mkdir(parents=True, exist_ok=True)
    parts = [p.read_text(encoding="utf-8").rstrip() for p in full_paths]
    corpus_path.write_text("\n\n\n".join(parts) + "\n", encoding="utf-8")


async def amain() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--rendered",
        type=Path,
        default=Path("output/pdf/poppler-extraction/rendered-pages"),
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("output/pdf/claude-vision"),
    )
    parser.add_argument("--model", default="claude-opus-4-7")
    parser.add_argument("--concurrency", type=int, default=6)
    parser.add_argument("--force", action="store_true", help="re-run pages with existing outputs")
    parser.add_argument("--limit", type=int, default=0, help="cap number of pages (0 = all)")
    args = parser.parse_args()

    root = args.root.resolve()
    rendered_root = (root / args.rendered).resolve()
    out_root = (root / args.out).resolve()
    out_pages_root = out_root / "pages"
    out_full_root = out_root / "full"
    corpus_path = out_root / "all-extracted-text.md"

    if not rendered_root.exists():
        print(f"error: rendered-pages directory not found: {rendered_root}", file=sys.stderr)
        return 1
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print(
            "error: ANTHROPIC_API_KEY not set. Export it before running:\n"
            "  export ANTHROPIC_API_KEY=sk-ant-...",
            file=sys.stderr,
        )
        return 1

    jobs = discover_jobs(rendered_root, out_pages_root, args.force)
    if args.limit > 0:
        jobs = jobs[: args.limit]
    if not jobs:
        print("nothing to do (all pages already have outputs; pass --force to redo).")
    else:
        print(
            f"transcribing {len(jobs)} pages with {args.model} "
            f"(concurrency={args.concurrency})...",
            flush=True,
        )

        progress = {
            "done": 0,
            "total": len(jobs),
            "cache_read": 0,
            "cache_create": 0,
            "input_tokens": 0,
            "output_tokens": 0,
        }

        client = anthropic.AsyncAnthropic()
        semaphore = asyncio.Semaphore(args.concurrency)
        start = time.monotonic()

        tasks = [
            asyncio.create_task(
                transcribe_page(client, args.model, job, semaphore, progress)
            )
            for job in jobs
        ]

        failures: list[tuple[PageJob, str]] = []
        for coro in asyncio.as_completed(tasks):
            job, text, err = await coro
            if err is not None or text is None:
                failures.append((job, err or "unknown error"))
                continue
            write_page(job, text)

        elapsed = time.monotonic() - start
        print(
            f"\ntranscribed {progress['done']}/{progress['total']} pages in {elapsed:.1f}s",
            flush=True,
        )
        print(
            f"tokens: input={progress['input_tokens']:,}, output={progress['output_tokens']:,}, "
            f"cache_read={progress['cache_read']:,}, cache_create={progress['cache_create']:,}",
            flush=True,
        )
        if failures:
            print(f"\n{len(failures)} failures:", file=sys.stderr)
            for job, err in failures:
                print(f"  {job.pdf_safe} page {job.page_num}: {err}", file=sys.stderr)

    full_paths = assemble_per_pdf(out_pages_root, out_full_root, rendered_root)
    if full_paths:
        assemble_corpus(full_paths, corpus_path)
        print(f"\nwrote {len(full_paths)} per-PDF files to {out_full_root}")
        print(f"wrote corpus: {corpus_path}")

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(amain()))
