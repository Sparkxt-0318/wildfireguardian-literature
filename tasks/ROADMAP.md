# ROADMAP.md

## Phase 0 — Durable context (COMPLETE)
Scaffold, protocols, claim registry, novelty standard, failure modes.

## Phase 1 — Adversarial prior-art sweep (IN PROGRESS)
Ten literature categories searched adversarially; per-paper notes; metadata;
first novelty matrix; first threat register; first verdict.

**Exit criteria:** 50+ relevant works recorded, 20+ detailed notes, novelty
matrix populated, `novelty/CURRENT_NOVELTY_VERDICT.md` written without
softening.

## Phase 2 — Full-text resolution
Resolve every `NEEDS_FULL_TEXT` item, prioritised by threat level. Any
`CRITICAL` threat known only at evidence level E2 is the top of the queue —
it may end the project and we have not read it.

**Exit criteria:** no CRITICAL or HIGH threat below evidence level E3.

## Phase 3 — Claim narrowing
Rewrite every `WEAKENED` claim into a form the prior art does not cover, or
abandon it. Each rewrite gets a `docs/DECISIONS.md` entry.

**Exit criteria:** every claim is `SUPPORTED_CANDIDATE`, `REJECTED`, or
explicitly abandoned. No claim left at `UNKNOWN`.

## Phase 4 — Fair binder
Tier 1 annotation sheets, judge-question drill, one-sentence differences,
printed binder assembly.

**Exit criteria:** every Tier 1 paper has a one-page sheet; every judge
question has a 30-second answer that survives a hostile follow-up.

## Phase 5 — Continuous monitoring
Standing sweep for 2026+ work that threatens or strengthens the program;
90-day claim re-validation per `NOVELTY_STANDARD.md` §7.

---

## Standing backlog

- Forward-citation sweep on every anchor paper, repeated quarterly.
- Korean-language sweep repeated after each major Korean fire season.
- Preprint servers swept monthly (arXiv, EarthArXiv, SSRN, Research Square).
- DOI resolution check across `bibliography/doi_registry.csv`.
- Adversarial re-rating: a second agent re-rates threat levels assigned by the
  agent that found the paper.
