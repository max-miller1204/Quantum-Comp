#!/usr/bin/env python3
"""Rebuild Poppler/Tesseract extraction artifacts for course source files."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".gif", ".webp"}
PDF_EXTENSIONS = {".pdf"}
MANAGED_DIRS = (
    "info",
    "text",
    "rendered-pages",
    "ocr/pages",
    "ocr/combined",
    "ocr/logs",
    "image-ocr",
    "full-text",
)


@dataclass(frozen=True)
class PdfArtifact:
    source: Path
    rel: str
    safe_name: str
    pages: int
    embedded_text_path: Path
    embedded_lines: int
    rendered_pages: list[Path]
    ocr_page_texts: list[Path]
    ocr_combined_path: Path
    ocr_lines: int
    full_text_path: Path
    full_text_lines: int


@dataclass(frozen=True)
class ImageArtifact:
    source: Path
    rel: str
    safe_name: str
    ocr_text_path: Path
    ocr_lines: int


def run_command(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=False)


def require_tool(name: str) -> str:
    found = shutil.which(name)
    if not found:
        raise RuntimeError(f"Required tool not found on PATH: {name}")
    return found


def safe_file_name(relative_path: str) -> str:
    return relative_path.replace(os.sep, "__").replace("/", "__")


def natural_key(path: Path) -> list[object]:
    parts: list[object] = []
    for part in re.split(r"(\d+)", path.name):
        parts.append(int(part) if part.isdigit() else part)
    return parts


def count_lines(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        return sum(1 for _ in handle)


def count_meaningful_lines(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        return sum(1 for line in handle if line.replace("\f", "").strip())


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def discover_files(root: Path) -> tuple[list[Path], list[Path]]:
    pdfs: list[Path] = []
    images: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            rel_parts = path.relative_to(root).parts
        except ValueError:
            continue
        if rel_parts and rel_parts[0] in {".git", "output"}:
            continue
        ext = path.suffix.lower()
        if ext in PDF_EXTENSIONS:
            pdfs.append(path)
        elif ext in IMAGE_EXTENSIONS:
            images.append(path)
    return sorted(pdfs), sorted(images)


def parse_page_count(info_text: str) -> int:
    for line in info_text.splitlines():
        if line.startswith("Pages:"):
            try:
                return int(line.split(":", 1)[1].strip())
            except ValueError:
                break
    return 0


def render_pdf(pdf: Path, out_dir: Path) -> list[Path]:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = out_dir / "page"
    result = run_command(["pdftoppm", "-png", "-scale-to", "2200", str(pdf), str(prefix)])
    if result.returncode != 0:
        raise RuntimeError(f"pdftoppm failed for {pdf}:\n{result.stderr}")
    return sorted(out_dir.glob("page-*.png"), key=natural_key)


def ocr_image(image: Path, out_base: Path, log_path: Path) -> Path:
    out_base.parent.mkdir(parents=True, exist_ok=True)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    result = run_command(["tesseract", str(image), str(out_base), "-l", "eng", "--dpi", "220"])
    log_text = ""
    if result.stdout:
        log_text += result.stdout
    if result.stderr:
        log_text += result.stderr
    write_text(log_path, log_text)
    if result.returncode != 0:
        raise RuntimeError(f"tesseract failed for {image}:\n{log_text}")
    return out_base.with_suffix(".txt")


def extract_pdf(root: Path, output: Path, pdf: Path) -> PdfArtifact:
    rel = pdf.relative_to(root).as_posix()
    safe_name = safe_file_name(rel)

    info_path = output / "info" / f"{safe_name}.info.txt"
    info_result = run_command(["pdfinfo", str(pdf)])
    if info_result.returncode != 0:
        raise RuntimeError(f"pdfinfo failed for {pdf}:\n{info_result.stderr}")
    write_text(info_path, info_result.stdout)
    pages = parse_page_count(info_result.stdout)

    embedded_text_path = output / "text" / f"{safe_name}.txt"
    text_result = run_command(["pdftotext", "-layout", str(pdf), str(embedded_text_path)])
    if text_result.returncode != 0:
        raise RuntimeError(f"pdftotext failed for {pdf}:\n{text_result.stderr}")
    embedded_lines = count_meaningful_lines(embedded_text_path)

    rendered_dir = output / "rendered-pages" / safe_name
    rendered_pages = render_pdf(pdf, rendered_dir)

    ocr_page_dir = output / "ocr" / "pages" / safe_name
    if ocr_page_dir.exists():
        shutil.rmtree(ocr_page_dir)
    ocr_page_dir.mkdir(parents=True, exist_ok=True)
    ocr_page_texts: list[Path] = []
    for page_image in rendered_pages:
        page_stem = page_image.stem
        out_base = ocr_page_dir / page_stem
        log_path = output / "ocr" / "logs" / f"{safe_name}--{page_stem}.log"
        ocr_page_texts.append(ocr_image(page_image, out_base, log_path))

    ocr_combined_path = output / "ocr" / "combined" / f"{safe_name}.ocr.txt"
    ocr_chunks: list[str] = []
    for index, page_text in enumerate(ocr_page_texts, start=1):
        body = read_text(page_text).strip()
        ocr_chunks.append(f"--- OCR page {index}: {rel} ---\n{body}\n")
    write_text(ocr_combined_path, "\n".join(ocr_chunks).rstrip() + "\n")
    ocr_lines = count_lines(ocr_combined_path)

    full_text_path = output / "full-text" / f"{safe_name}.full.txt"
    embedded_text = read_text(embedded_text_path).strip()
    ocr_text = read_text(ocr_combined_path).strip()
    full_text = (
        f"# {rel}\n\n"
        f"Pages: {pages}\n"
        f"Embedded text lines: {embedded_lines}\n"
        f"Tesseract OCR lines: {ocr_lines}\n\n"
        "## Poppler embedded text (`pdftotext -layout`)\n\n"
        f"{embedded_text if embedded_text else '[No embedded text extracted by Poppler.]'}\n\n"
        "## Tesseract OCR from Poppler-rendered pages\n\n"
        f"{ocr_text if ocr_text else '[No OCR text extracted by Tesseract.]'}\n"
    )
    write_text(full_text_path, full_text)
    full_text_lines = count_lines(full_text_path)

    return PdfArtifact(
        source=pdf,
        rel=rel,
        safe_name=safe_name,
        pages=pages,
        embedded_text_path=embedded_text_path,
        embedded_lines=embedded_lines,
        rendered_pages=rendered_pages,
        ocr_page_texts=ocr_page_texts,
        ocr_combined_path=ocr_combined_path,
        ocr_lines=ocr_lines,
        full_text_path=full_text_path,
        full_text_lines=full_text_lines,
    )


def extract_image(root: Path, output: Path, image: Path) -> ImageArtifact:
    rel = image.relative_to(root).as_posix()
    safe_name = safe_file_name(rel)
    out_base = output / "image-ocr" / Path(safe_name).with_suffix("")
    log_path = output / "image-ocr" / "logs" / f"{safe_name}.log"
    ocr_text_path = ocr_image(image, out_base, log_path)
    return ImageArtifact(
        source=image,
        rel=rel,
        safe_name=safe_name,
        ocr_text_path=ocr_text_path,
        ocr_lines=count_lines(ocr_text_path),
    )


def clean_managed_dirs(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    for rel in MANAGED_DIRS:
        target = output / rel
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)


def write_manifests(
    root: Path,
    output: Path,
    pdf_artifacts: list[PdfArtifact],
    image_artifacts: list[ImageArtifact],
) -> None:
    total_pages = sum(pdf.pages for pdf in pdf_artifacts)
    total_embedded_lines = sum(pdf.embedded_lines for pdf in pdf_artifacts)
    total_ocr_lines = sum(pdf.ocr_lines for pdf in pdf_artifacts)
    total_full_lines = sum(pdf.full_text_lines for pdf in pdf_artifacts)
    rendered_pages = [page for pdf in pdf_artifacts for page in pdf.rendered_pages]
    ocr_page_texts = [page for pdf in pdf_artifacts for page in pdf.ocr_page_texts]
    image_only = [pdf.rel for pdf in pdf_artifacts if pdf.embedded_lines == 0]

    write_text(output / "pdf-list.txt", "\n".join(pdf.rel for pdf in pdf_artifacts) + "\n")
    write_text(output / "source-image-list.txt", "\n".join(img.rel for img in image_artifacts) + ("\n" if image_artifacts else ""))
    write_text(output / "page-counts.tsv", "\n".join(f"{pdf.rel}\t{pdf.pages}" for pdf in pdf_artifacts) + "\n")
    write_text(
        output / "text-line-counts.txt",
        "\n".join(f"{pdf.embedded_lines:8d} {pdf.embedded_text_path.relative_to(root).as_posix()}" for pdf in sorted(pdf_artifacts, key=lambda item: item.embedded_lines)) + "\n",
    )
    write_text(output / "image-only-pdfs.txt", "\n".join(image_only) + ("\n" if image_only else ""))
    write_text(output / "rendered-page-list.txt", "\n".join(page.relative_to(root).as_posix() for page in rendered_pages) + "\n")
    write_text(output / "ocr" / "ocr-page-list.txt", "\n".join(page.relative_to(root).as_posix() for page in ocr_page_texts) + "\n")
    write_text(output / "ocr" / "ocr-combined-list.txt", "\n".join(pdf.ocr_combined_path.relative_to(root).as_posix() for pdf in pdf_artifacts) + "\n")
    write_text(
        output / "ocr" / "ocr-line-counts.txt",
        "\n".join(f"{pdf.ocr_lines:8d} {pdf.ocr_combined_path.relative_to(root).as_posix()}" for pdf in sorted(pdf_artifacts, key=lambda item: item.ocr_lines)) + "\n",
    )
    write_text(output / "full-text-list.txt", "\n".join(pdf.full_text_path.relative_to(root).as_posix() for pdf in pdf_artifacts) + "\n")
    write_text(
        output / "full-text-line-counts.txt",
        "\n".join(f"{pdf.full_text_lines:8d} {pdf.full_text_path.relative_to(root).as_posix()}" for pdf in sorted(pdf_artifacts, key=lambda item: item.full_text_lines)) + "\n",
    )
    write_text(
        output / "image-ocr-list.txt",
        "\n".join(img.ocr_text_path.relative_to(root).as_posix() for img in image_artifacts) + ("\n" if image_artifacts else ""),
    )

    corpus_chunks: list[str] = []
    for pdf in pdf_artifacts:
        corpus_chunks.append(read_text(pdf.full_text_path).rstrip())
    if image_artifacts:
        corpus_chunks.append("# Standalone source image OCR")
        for image in image_artifacts:
            corpus_chunks.append(f"## {image.rel}\n\n{read_text(image.ocr_text_path).strip()}")
    write_text(output / "all-extracted-text.txt", "\n\n\n".join(corpus_chunks).rstrip() + "\n")

    tesseract_version = run_command(["tesseract", "--version"]).stdout.splitlines()[0]
    pdfinfo_version = (run_command(["pdfinfo", "-v"]).stderr or run_command(["pdfinfo", "-v"]).stdout).splitlines()[0]
    pdftotext_version = (run_command(["pdftotext", "-v"]).stderr or run_command(["pdftotext", "-v"]).stdout).splitlines()[0]
    pdftoppm_version = (run_command(["pdftoppm", "-v"]).stderr or run_command(["pdftoppm", "-v"]).stdout).splitlines()[0]

    summary = f"""# Poppler/Tesseract Extraction Audit

Generated from source PDFs/images in this repository. Files under `output/` are treated as generated artifacts and are not re-ingested as source images.

## Tools

- `{pdftotext_version}` for embedded text.
- `{pdfinfo_version}` for PDF metadata.
- `{pdftoppm_version}` with `-png -scale-to 2200` for page rendering.
- `{tesseract_version}` for OCR on every rendered PDF page.

## Summary

- PDFs processed: {len(pdf_artifacts)}
- PDF pages rendered with Poppler: {len(rendered_pages)}
- PDF page OCR files generated with Tesseract: {len(ocr_page_texts)}
- Total PDF page count from metadata: {total_pages}
- Standalone source images processed: {len(image_artifacts)}
- Embedded Poppler text lines: {total_embedded_lines}
- PDF OCR text lines: {total_ocr_lines}
- Full combined PDF text lines: {total_full_lines}
- Full corpus path: `output/pdf/poppler-extraction/all-extracted-text.txt`

## Image-Only PDFs

These PDFs had zero embedded text from `pdftotext -layout`; their OCR sections are the primary extracted text:

{chr(10).join(f"- `{item}`" for item in image_only) if image_only else "- None"}

## Output Layout

- `text/`: Poppler embedded text per PDF.
- `rendered-pages/`: Poppler PNG render for every PDF page.
- `ocr/pages/`: Tesseract OCR per rendered page.
- `ocr/combined/`: Combined Tesseract OCR per PDF.
- `full-text/`: Per-PDF files containing both Poppler text and Tesseract OCR.
- `all-extracted-text.txt`: Combined corpus across all PDFs and source images.
"""
    write_text(output / "README.md", summary)

    audit_rows = [
        "source\tpages\tembedded_lines\tocr_lines\tfull_text_lines\trendered_pages\tocr_pages",
        *(
            f"{pdf.rel}\t{pdf.pages}\t{pdf.embedded_lines}\t{pdf.ocr_lines}\t{pdf.full_text_lines}\t{len(pdf.rendered_pages)}\t{len(pdf.ocr_page_texts)}"
            for pdf in pdf_artifacts
        ),
    ]
    write_text(output / "audit.tsv", "\n".join(audit_rows) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=Path("output/pdf/poppler-extraction"))
    args = parser.parse_args()

    root = args.root.resolve()
    output = (root / args.output).resolve() if not args.output.is_absolute() else args.output.resolve()

    for tool in ("pdfinfo", "pdftotext", "pdftoppm", "tesseract"):
        require_tool(tool)

    pdfs, images = discover_files(root)
    clean_managed_dirs(output)

    pdf_artifacts: list[PdfArtifact] = []
    for index, pdf in enumerate(pdfs, start=1):
        rel = pdf.relative_to(root).as_posix()
        print(f"[{index}/{len(pdfs)}] PDF {rel}", flush=True)
        pdf_artifacts.append(extract_pdf(root, output, pdf))

    image_artifacts: list[ImageArtifact] = []
    for index, image in enumerate(images, start=1):
        rel = image.relative_to(root).as_posix()
        print(f"[{index}/{len(images)}] image {rel}", flush=True)
        image_artifacts.append(extract_image(root, output, image))

    write_manifests(root, output, pdf_artifacts, image_artifacts)

    total_rendered = sum(len(pdf.rendered_pages) for pdf in pdf_artifacts)
    print(f"Processed {len(pdf_artifacts)} PDFs, rendered/OCR'd {total_rendered} pages, processed {len(image_artifacts)} standalone images.")
    print(f"Wrote {output.relative_to(root).as_posix()}/all-extracted-text.txt")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
