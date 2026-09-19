#!/usr/bin/env python3
"""Verify that every paper_id cited in prose actually exists in
literature/metadata/. A novelty document that cites a record we do not hold is
indistinguishable, to a reader, from a fabricated citation.

Scans docs/, novelty/, fair/ and literature/reviews/ for backtick-quoted
identifiers shaped like a paper_id and reports any that have no metadata file.

Exit code is non-zero if any dangling reference is found.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
KNOWN = {p.stem for p in (ROOT / "literature" / "metadata").glob("*.yaml")}
# Search logs deliberately record unverified leads and superseded ids, so they
# are excluded: a dangling id there is history, not a broken citation.
SCAN = ["novelty", "fair", "literature/reviews", "literature/notes"]
SCAN += ["docs"]
SKIP_DIRS = {"search-logs"}
# a paper_id is lastname + 4-digit year + keyword, all lowercase alphanumeric
CAND = re.compile(r"`([a-z][a-z0-9]*(?:19|20)\d{2}[a-z0-9]+)`")

def main():
    dangling = {}
    for rel in SCAN:
        for f in sorted((ROOT / rel).rglob("*.md")):
            if any(part in SKIP_DIRS for part in f.parts):
                continue
            for m in CAND.finditer(f.read_text(encoding="utf-8")):
                pid = m.group(1)
                if pid not in KNOWN:
                    dangling.setdefault(pid, set()).add(str(f.relative_to(ROOT)))
    print(f"{len(KNOWN)} metadata records known")
    if not dangling:
        print("no dangling paper_id references")
        return 0
    print(f"\n{len(dangling)} DANGLING paper_id reference(s):")
    for pid, where in sorted(dangling.items()):
        print(f"  {pid}")
        for w in sorted(where):
            print(f"      cited in {w}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
