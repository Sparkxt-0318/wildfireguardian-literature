#!/usr/bin/env python3
"""Extract real text from a PDF, locally, with page markers.

This exists because of FAILURE_MODES section 10: a summarising fetch of a
binary PDF once returned fluent, specific statistics that contradicted the
paper's actual abstract. Correct citation, fabricated numbers -- the hardest
error to detect downstream.

The fix is not "be careful with PDFs", it is to never let a language model
paraphrase a PDF it cannot read. Extract the text deterministically, then read
the text. Page markers make page-numbered evidence possible, which
EVIDENCE_LEVELS E4 requires.

Usage:
    python3 bibliography/extract_pdf_text.py paper.pdf
    python3 bibliography/extract_pdf_text.py paper.pdf --out paper.txt
    python3 bibliography/extract_pdf_text.py paper.pdf --grep "dispatch|deadline|latest"

--grep prints only matching lines with their page number, which is the usual
way this is used: asking whether a paper ever says "dispatch time" is a
question about presence, and presence is exactly what an abstract cannot tell
you.
"""
import argparse
import pathlib
import re
import sys


def extract_pages(path):
    """Yield (page_number, text). pdfminer first; pypdf as a fallback."""
    try:
        from pdfminer.high_level import extract_text
        from pdfminer.pdfpage import PDFPage
        with open(path, "rb") as fh:
            n = sum(1 for _ in PDFPage.get_pages(fh))
        for i in range(n):
            yield i + 1, extract_text(str(path), page_numbers=[i]) or ""
        return
    except Exception as e:
        print(f"[pdfminer failed: {type(e).__name__}: {e}] trying pypdf",
              file=sys.stderr)
    import pypdf
    reader = pypdf.PdfReader(str(path))
    for i, page in enumerate(reader.pages):
        yield i + 1, page.extract_text() or ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--out")
    ap.add_argument("--grep", help="regex; print only matching lines, with page numbers")
    ap.add_argument("--context", type=int, default=0, help="lines of context around --grep hits")
    args = ap.parse_args()

    path = pathlib.Path(args.pdf)
    if not path.exists():
        print(f"no such file: {path}", file=sys.stderr)
        return 2

    pages = list(extract_pages(path))
    total = sum(len(t) for _, t in pages)
    print(f"# {path.name}: {len(pages)} pages, {total} characters extracted",
          file=sys.stderr)
    if total < 200 * len(pages):
        print("# WARNING: very little text per page. This may be a scanned PDF "
              "(needs OCR) or a form. Do NOT summarise it from a fetch -- say "
              "you could not read it.", file=sys.stderr)

    if args.grep:
        rx = re.compile(args.grep, re.I)
        hits = 0
        for pno, text in pages:
            lines = text.splitlines()
            for i, line in enumerate(lines):
                if rx.search(line):
                    hits += 1
                    lo = max(0, i - args.context)
                    hi = min(len(lines), i + args.context + 1)
                    for j in range(lo, hi):
                        mark = ">" if j == i else " "
                        print(f"p{pno:>3} {mark} {lines[j].strip()}")
                    if args.context:
                        print("    ---")
        print(f"# {hits} matching line(s)", file=sys.stderr)
        # Absence is a finding: report it explicitly rather than silently.
        if hits == 0:
            print(f"# NO MATCH for /{args.grep}/ in {len(pages)} extracted pages. "
                  "That is evidence of absence ONLY if extraction succeeded -- "
                  "check the character count above.", file=sys.stderr)
        return 0

    out = "\n".join(f"\n===== page {pno} =====\n{text}" for pno, text in pages)
    if args.out:
        pathlib.Path(args.out).write_text(out, encoding="utf-8")
        print(f"# wrote {args.out}", file=sys.stderr)
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
