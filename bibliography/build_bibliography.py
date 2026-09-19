#!/usr/bin/env python3
"""Generate bibliography/literature.csv, bibliography/wildfireguardian.bib and
novelty/NOVELTY_MATRIX.md from the per-paper records in literature/metadata/.

The metadata files are the single source of truth. Nothing is typed twice, so
a citation cannot drift between the CSV, the BibTeX and the matrix.

Entry types follow docs/CITATION_RULES.md: a preprint is never @article, a
government report is never @article, and an unverified DOI is omitted rather
than guessed.

Usage:  python3 bibliography/build_bibliography.py
"""
import csv
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
META = ROOT / "literature" / "metadata"
CSV_OUT = ROOT / "bibliography" / "literature.csv"
BIB_OUT = ROOT / "bibliography" / "wildfireguardian.bib"
MATRIX_OUT = ROOT / "novelty" / "NOVELTY_MATRIX.md"

MATRIX_COLS = [
    ("future_fire", "future fire"),
    ("traffic", "traffic"),
    ("household_trigger", "household trigger"),
    ("probabilistic_trigger", "prob. trigger"),
    ("multiple_fire_models", "multi fire models"),
    ("assisted_evacuation", "assisted evac"),
    ("inbound_responder", "inbound responder"),
    ("pickup", "pickup"),
    ("egress", "egress"),
    ("dispatch_by_deadline", "dispatch-by deadline"),
    ("forecast_latency", "forecast latency"),
    ("forecast_skill_boundary", "skill boundary"),
    ("decision_value", "decision value"),
    ("scarce_resources", "scarce resources"),
    ("voi", "VOI"),
    ("active_sensing", "active sensing"),
    ("korean_setting", "Korean setting"),
    ("real_validation", "real validation"),
    ("osse", "OSSE"),
]

CSV_COLS = ["paper_id", "title", "authors", "year", "venue", "venue_type",
            "volume", "issue", "pages", "doi", "url", "publication_status",
            "open_access_status", "date_verified", "category", "threat_level",
            "threatens_claims", "one_line_difference"]

THREAT_ORDER = {"CRITICAL": 0, "HIGH": 1, "MODERATE": 2, "LOW": 3, "BACKGROUND": 4}
SCALAR = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")


def read_meta(path):
    """Flat key: value plus one nested 'matrix:' block. Handles YAML folded
    scalars ('>' and '|') by joining their indented continuation lines."""
    data, cur_block, folding_key, folded = {}, None, None, []
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        stripped = line.strip()
        indented = line[:1] in (" ", "\t")

        if folding_key is not None:
            if indented and stripped:
                folded.append(stripped)
                continue
            data[folding_key] = " ".join(folded)
            folding_key, folded = None, []

        if not stripped or stripped.startswith("#"):
            continue

        if indented:
            if cur_block:
                m = SCALAR.match(stripped)
                if m:
                    val = m.group(2).split("#")[0].strip().strip('"').strip("'")
                    data.setdefault(cur_block, {})[m.group(1)] = val
            continue

        m = SCALAR.match(line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val in (">", "|", ">-", "|-"):
            folding_key, folded, cur_block = key, [], None
        elif val == "":
            cur_block = key
            data.setdefault(key, {})
        else:
            cur_block = None
            data[key] = val.strip('"').strip("'")
    if folding_key is not None:
        data[folding_key] = " ".join(folded)
    return data


def clean(v):
    return re.sub(r"\s+", " ", str(v or "")).strip()


def split_items(v):
    """Split a list-ish field into items.

    Metadata uses two conventions: bracketed lists ('[A, B]') and
    semicolon-separated name lists ('Malings, Carl; Pozzi, Matteo'). Splitting
    the second on commas would tear 'Last, First' in half, so a semicolon, when
    present, is the only separator.
    """
    s = clean(v).strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    quoted = re.findall(r'"([^"]+)"', s)
    if quoted:
        return [q.strip() for q in quoted if q.strip()]
    sep = ";" if ";" in s else ","
    return [p.strip().strip('"').strip("'") for p in s.split(sep) if p.strip()]


def listy(v):
    return "; ".join(split_items(v))


def bib_type(meta):
    status = clean(meta.get("publication_status")).upper()
    vtype = clean(meta.get("venue_type")).lower()
    if status == "PREPRINT" or vtype == "preprint":
        return "misc"
    if status in ("GOVERNMENT_REPORT", "SOFTWARE_DOC") or vtype in ("report", "software_doc"):
        return "techreport"
    if status == "THESIS" or vtype == "thesis":
        return "phdthesis"
    if vtype == "conference":
        return "inproceedings"
    if vtype == "book_chapter":
        return "incollection"
    return "article"


def bib_escape(s):
    return clean(s).replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")


def bib_entry(meta):
    pid = clean(meta.get("paper_id"))
    etype = bib_type(meta)
    authors = split_items(meta.get("authors"))
    fields = [("title", "{" + bib_escape(meta.get("title")) + "}")]
    if authors:
        fields.append(("author", "{" + " and ".join(bib_escape(a) for a in authors) + "}"))
    year = clean(meta.get("year"))
    if year and year.upper() != "UNVERIFIED":
        fields.append(("year", "{" + year + "}"))

    venue = bib_escape(meta.get("venue"))
    if venue and venue.upper() != "UNVERIFIED":
        key = {"article": "journal", "inproceedings": "booktitle",
               "incollection": "booktitle", "techreport": "institution",
               "phdthesis": "school", "misc": "howpublished"}[etype]
        fields.append((key, "{" + venue + "}"))

    for src, dst in (("volume", "volume"), ("issue", "number"), ("pages", "pages")):
        v = clean(meta.get(src))
        if v and v.upper() != "UNVERIFIED":
            fields.append((dst, "{" + v + "}"))

    doi = clean(meta.get("doi"))
    if doi and doi.upper() != "UNVERIFIED":              # never guess a DOI
        fields.append(("doi", "{" + doi + "}"))
    url = clean(meta.get("url"))
    if url and url.upper() != "UNVERIFIED":
        fields.append(("url", "{" + url + "}"))

    status = clean(meta.get("publication_status")) or "UNVERIFIED"
    note = f"verified: {clean(meta.get('date_verified')) or 'UNVERIFIED'}; status: {status}"
    if status.upper() == "PREPRINT":
        note = "Preprint -- not peer reviewed. " + note
    elif status.upper() == "GOVERNMENT_REPORT":
        note = "Government/agency report -- not peer reviewed. " + note
    fields.append(("note", "{" + bib_escape(note) + "}"))

    body = ",\n  ".join(f"{k} = {v}" for k, v in fields)
    return f"@{etype}{{{pid},\n  {body}\n}}\n"


def main():
    files = sorted(META.glob("*.yaml"))
    if not files:
        print("no metadata files found", file=sys.stderr)
        return 1
    records = [read_meta(p) for p in files]
    records = [r for r in records if r.get("paper_id")]
    records.sort(key=lambda r: (THREAT_ORDER.get(clean(r.get("threat_level")).upper(), 5),
                                clean(r.get("paper_id"))))

    with CSV_OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(CSV_COLS)
        for r in records:
            w.writerow([listy(r.get(c)) if c in ("authors", "category", "threatens_claims")
                        else clean(r.get(c)) for c in CSV_COLS])

    BIB_OUT.write_text(
        "% WildfireGuardian bibliography -- GENERATED, do not edit by hand.\n"
        "% Source of truth: literature/metadata/*.yaml\n"
        "% Regenerate: python3 bibliography/build_bibliography.py\n"
        "% Every entry carries its verification date and publication status.\n"
        "% Preprints are @misc, agency reports are @techreport -- never @article.\n\n"
        + "\n".join(bib_entry(r) for r in records), encoding="utf-8")

    def cell(v):
        v = clean(v).lower()
        if v in ("yes", "true", "y"):
            return "Y"
        if v in ("partial", "part"):
            return "~"
        if v in ("no", "false", "n", "", "-"):
            return "."
        return "?"

    head = "| Paper | Threat | " + " | ".join(lbl for _, lbl in MATRIX_COLS) + " |"
    sep = "|---|---|" + "---|" * len(MATRIX_COLS)
    rows = []
    for r in records:
        mx = r.get("matrix") or {}
        rows.append("| `" + clean(r.get("paper_id")) + "` | "
                    + clean(r.get("threat_level")) + " | "
                    + " | ".join(cell(mx.get(k)) for k, _ in MATRIX_COLS) + " |")

    MATRIX_OUT.parent.mkdir(parents=True, exist_ok=True)
    MATRIX_OUT.write_text(f"""# NOVELTY_MATRIX.md

**GENERATED** from `literature/metadata/*.yaml` by
`bibliography/build_bibliography.py`. Do not edit by hand — edit the metadata.

Rows are papers, sorted by threat level (conceptual overlap, never venue
prestige). Columns are the capability dimensions WildfireGuardian might claim.

Legend: `Y` = does it · `~` = partially / indirectly · `.` = does not · `?` = unrecorded

**How to read this for novelty.** A column that is dense with `Y` is a column
we cannot claim. A column that is empty is *not* thereby ours — it may simply
mean nobody indexes their work that way, or that we have not searched the field
that uses different vocabulary. Per `docs/NOVELTY_STANDARD.md` §3.2, an empty
column supports `UNKNOWN`, never novelty. The matrix shows where to *look*; it
does not by itself establish anything.

**Conjunction warning.** Reading across a row to find that no single paper has
`Y` everywhere is the forbidden argument (`NOVELTY_STANDARD.md` §3.1). The
useful reading is column-wise and pairwise, not row-wise.

{head}
{sep}
""" + "\n".join(rows) + f"""

---

## Column occupancy

| Column | Y | ~ | . | Reading |
|---|---|---|---|---|
""" + "\n".join(
        "| {} | {} | {} | {} | {} |".format(
            lbl,
            sum(1 for r in records if cell((r.get("matrix") or {}).get(k)) == "Y"),
            sum(1 for r in records if cell((r.get("matrix") or {}).get(k)) == "~"),
            sum(1 for r in records if cell((r.get("matrix") or {}).get(k)) == "."),
            "heavily occupied" if sum(1 for r in records if cell((r.get("matrix") or {}).get(k)) == "Y") >= 5
            else ("occupied" if sum(1 for r in records if cell((r.get("matrix") or {}).get(k)) == "Y") >= 2
                  else "sparse -- investigate whether this is genuinely open or merely unsearched"))
        for k, lbl in MATRIX_COLS)
        + f"\n\n*{len(records)} papers recorded.*\n", encoding="utf-8")

    print(f"wrote {CSV_OUT.name} ({len(records)} rows), {BIB_OUT.name}, {MATRIX_OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
