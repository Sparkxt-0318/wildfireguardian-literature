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

## 2026-09-20 — Phase 2: full-text resolution

**Outcome: the dispatch-by method is occupied.** Decomposition plus an
adjacent-field sweep found what five rounds of fire-vocabulary searching
missed. Kamphuis et al. have reported the latest guaranteed departure time
since 2022; SIPP has represented non-monotone feasible sets since 2011. Six of
seven dispatch-by components are occupied and no claim remains at
`SUPPORTED_CANDIDATE`. Thesis B adopted: empirical and artifact contribution,
method novelty explicitly disclaimed.

**Corrections to our own record.** The headline counts summed to 15 for 14
claims. We had asserted that wildfire forecast-value work uses untuned
baselines; Ardid tunes its comparator. A "safe time remaining" mechanism
attributed to Beyki was retracted as untraceable. An OCCUPIED component rested
on an E2 citation, against Rule 1. Two paper_ids in our own prose named papers
that did not exist.

**Tooling built:** `build_claims.py` (counts derived, never typed),
`check_fulltext_tiers.py` (confidence gated on what was actually read),
`extract_pdf_text.py` (deterministic PDF text, closing the fabricated-statistics
failure mode). Fixed a parser bug that silently dropped author lists from 33
BibTeX entries.

**New failure modes recorded:** self-citation contamination (a search returned
this project's own repository and the engine paraphrased its README as prior
art); verifying a fact at E2 and then asserting its opposite.
