# COMPLETED.md

## 2026-09-19
- Repository initialised; directory structure created.
- `README.md`, `AGENTS.md` written; mandatory reading order established.
- `docs/` durable context written: PROJECT_CONTEXT, CURRENT_THESIS,
  CLAIM_REGISTRY (14 claims), NOVELTY_STANDARD, SEARCH_PROTOCOL,
  INCLUSION_CRITERIA, EXCLUSION_CRITERIA, EVIDENCE_LEVELS, CITATION_RULES,
  DECISIONS (D-001…D-005), FAILURE_MODES, GLOSSARY.
- Adversarial search launched across ten literature categories.

## 2026-09-19 — Phase 1: adversarial prior-art sweep

**Corpus.** 165 verified records (132 peer-reviewed, 21 preprints, 10
government reports, 2 software docs), 67 paper notes, 10 thematic reviews,
7 query logs. Search tiers S1–S2; no category reached S3.

**Verdict.** Of 14 claims: 1 REJECTED, 4 OCCUPIED, 8 WEAKENED, 1
SUPPORTED_CANDIDATE, 1 UNKNOWN. Of 19 novelty-matrix columns, 18 occupied.

**Tooling built.**
- `bibliography/build_bibliography.py` — metadata is the single source of truth
  for CSV, BibTeX and the novelty matrix.
- `bibliography/verify_dois.py` — Crossref + DataCite resolution with
  title/year agreement checking; fails the build on any unresolved DOI.
- `bibliography/check_references.py` — fails the build on any paper_id cited in
  prose with no metadata record.

**Integrity defects found and fixed.** One metadata file silently absent from
every artifact (YAML parse error); two papers double-recorded under different
ids; three author-list placeholders, two of which had produced paper_ids naming
the wrong first author; four online-first vs issue-year errors; 55 records with
non-standard publication_status vocabulary; two paper_ids I wrote from memory
that did not exist.

**Corrections to the project brief.** The PERIL/k-PERIL lineage is Mitchell and
Kalogeropoulos et al., not "Mitsopoulos" — no such author appears on any
retrieved record.
