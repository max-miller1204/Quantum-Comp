# Poppler/Tesseract Extraction Audit

Generated from source PDFs/images in this repository. Files under `output/` are treated as generated artifacts and are not re-ingested as source images.

## Tools

- `pdftotext version 26.04.0` for embedded text.
- `pdfinfo version 26.04.0` for PDF metadata.
- `pdftoppm version 26.04.0` with `-png -scale-to 2200` for page rendering.
- `tesseract 5.5.2` for OCR on every rendered PDF page.

## Summary

- PDFs processed: 33
- PDF pages rendered with Poppler: 215
- PDF page OCR files generated with Tesseract: 215
- Total PDF page count from metadata: 215
- Standalone source images processed: 0
- Embedded Poppler text lines: 4971
- PDF OCR text lines: 8195
- Full combined PDF text lines: 15381
- Full corpus path: `output/pdf/poppler-extraction/all-extracted-text.txt`

## Image-Only PDFs

These PDFs had zero embedded text from `pdftotext -layout`; their OCR sections are the primary extracted text:

- `Lectures/quantum-algorithms(I).pdf`
- `Lectures/quantum-algorithms(II).pdf`
- `Past-Exams/Test1.pdf`
- `Past-Exams/Test2.pdf`
- `Past-Exams/Test3.pdf`
- `Past-Exams/Test4.pdf`

## Output Layout

- `text/`: Poppler embedded text per PDF.
- `rendered-pages/`: Poppler PNG render for every PDF page.
- `ocr/pages/`: Tesseract OCR per rendered page.
- `ocr/combined/`: Combined Tesseract OCR per PDF.
- `full-text/`: Per-PDF files containing both Poppler text and Tesseract OCR.
- `all-extracted-text.txt`: Combined corpus across all PDFs and source images.
