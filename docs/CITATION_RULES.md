# CITATION_RULES.md

## Required fields

Every bibliography entry records, where obtainable:

```
title, authors, year, venue, volume, issue, pages/article number,
DOI, URL, publication_status, open_access_status, date_verified
```

Unobtainable fields are written as the literal string `UNVERIFIED`.
**A blank is not acceptable and a guess is a fabrication.**

---

## Verification standard

1. **Never trust metadata from a single secondary source.** Aggregators copy
   each other; an error in one propagates everywhere. Corroborate against the
   publisher page, Crossref/DataCite, or the arXiv/repository record.
2. `verified_via` lists the sources actually consulted. Two aggregators that
   both derive from the same upstream record count as **one** source.
3. `date_verified` is the date of the last actual check, not the date the
   record was created.

---

## Publication status — never blur these

| Status | Meaning | How it must be described |
|---|---|---|
| `PEER_REVIEWED` | Journal article or reviewed conference paper | Name the venue and its type |
| `PREPRINT` | arXiv, EarthArXiv, SSRN, Research Square, etc. | **Must** be labeled a preprint everywhere it appears |
| `GOVERNMENT_REPORT` | NIFoS, KFS, MOIS, USFS GTR, agency technical report | **Never** called a peer-reviewed paper |
| `THESIS` | MSc/PhD dissertation | Labeled as a thesis with institution |
| `SOFTWARE_DOC` | Model user guide / technical documentation | Labeled as documentation |
| `UNVERIFIED` | Status not established | Cannot be cited in a paper until resolved |

Specific traps in our domain:
- **Rothermel (1972)** and many FARSITE/FlamMap documents are USDA Forest
  Service research papers / general technical reports — `GOVERNMENT_REPORT`,
  not journal articles. They are foundational and authoritative; that is not
  the same as peer-reviewed, and a judge may know the difference.
- **Conference papers** (TRB, ISCRAM, ICCV-style) are not journal articles.
  Say "conference paper."
- **Korean agency documents** (산림청, 국립산림과학원) are government reports.
  Korean *journal* articles (e.g. 한국산림과학회지) are peer-reviewed — record
  the language, and do not conflate the two categories.

---

## Priority dating

Novelty is about **public priority**, not about peer review. When a preprint
precedes the journal version, the **preprint date is the priority date** for
novelty purposes, while the journal version is what we cite. Record both.

---

## Quoting

- Short quotes only (≤25 words), with page/section location.
- Never paste long passages of copyrighted text into notes.
- Paraphrase in our own words and mark the evidence level.
- Quoting a Korean source: give the original and a translation, and mark the
  translation as ours.

---

## BibTeX conventions (`bibliography/wildfireguardian.bib`)

- Key = `paper_id` (see `AGENTS.md` §6).
- Correct entry types: `@article`, `@inproceedings`, `@techreport`,
  `@phdthesis`, `@misc` (with `note = {Preprint}`) — never `@article` for a
  preprint or a report.
- Include `doi` only when verified. An unverified DOI field is omitted, never
  guessed.
- Every entry carries `note = {verified: YYYY-MM-DD; status: ...}`.
