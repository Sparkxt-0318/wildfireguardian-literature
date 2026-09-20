# EVIDENCE_LEVELS.md

How strongly a source supports a statement we make. Every claim attribution in
`literature/notes/` carries an evidence level.

---

## Levels

| Level | Basis | May be used to |
|---|---|---|
| **E0** | Recall / unverified | Nothing. Search lead only. Never cited. |
| **E1** | Metadata only (title + venue seen) | Establish existence; log in registry |
| **E2** | Abstract read | Characterize topic; flag as prior art candidate; **may not** support a statement about method details or results |
| **E3** | Full text read, relevant sections | Support statements about method, assumptions, results |
| **E4** | Full text + verified numbers/equations located at a specific page/section | Support quantitative claims and direct quotes |
| **E5** | Reproduced or independently corroborated by a second source | Support a load-bearing claim in a paper or fair defense |

---

## Rules

1. **A claim status change to `REJECTED` or `OCCUPIED` requires E3 minimum.**
   Killing a claim on an abstract alone is as sloppy as supporting one on an
   abstract alone. If you only have E2, the status is `NEEDS_FULL_TEXT`.
2. **Tier 1 binder papers (`fair/MUST_PRINT.md`) must reach E3, ideally E4.**
   You will be asked about these out loud, by someone who may have read them.
3. Any quantitative number we cite (a rate-of-spread error, a latency, an
   evacuation response time) requires **E4**. No number enters our work at E2.
4. Metadata must be corroborated by ≥2 independent sources before reaching
   `date_verified` (see `docs/CITATION_RULES.md`). A publisher page plus
   Crossref counts; two aggregators copying the same upstream record does not.

---

## Evidence level vs threat level

They are orthogonal and are frequently confused:

- **Evidence level** = how well *we* know the paper.
- **Threat level** = how much the paper *overlaps* our claims.

A `CRITICAL` threat known only at `E2` is the most urgent item in the
repository: it may kill the project and we have not read it. Such items go
straight to `novelty/OPEN_QUESTIONS.md` and `fair/MUST_PRINT.md` Tier 1.

---

## Relationship to `fulltext_status`

Two scales now exist and they must not drift apart. They measure different
things and both are needed:

- **Evidence level (E0–E5)** is about *a statement*: how well supported is this
  particular assertion we are making about the paper?
- **`fulltext_status`** is about *the paper record*: how much of this paper has
  anyone actually read?

Mapping (the tier is the ceiling on the evidence level any statement about that
paper can carry):

| `fulltext_status` | Ceiling on evidence level | What may be asserted |
|---|---|---|
| `TITLE_ONLY` | E1 | Existence and topic only |
| `ABSTRACT_VERIFIED` | E2 | Topic and headline claim. **Not** method details, and **not** the absence of a feature |
| `FULL_TEXT_READ` | E3 | Method, assumptions, reported results |
| `METHODS_VERIFIED` | E4 | Equations, parameters, located quantitative values |
| `RESULTS_VERIFIED` | E5 | Results corroborated or reproduced |

**The asymmetry that matters.** Asserting a paper *does* something is often
safe at E2 — the abstract says so. Asserting a paper does **not** do something
requires `FULL_TEXT_READ` at minimum, because absence is not reported in
abstracts. Almost every novelty argument in this repository is an absence
argument, which is why `NOVELTY_STANDARD.md` §10 gates confidence on the tier
rather than on the number of searches.

Run `python3 bibliography/check_fulltext_tiers.py` to see each claim's current
ceiling.
