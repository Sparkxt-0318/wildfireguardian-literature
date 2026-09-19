# WildfireGuardian Literature, Prior-Art & Novelty-Defense Repository

This repository is the **authoritative literature, prior-art, citation, and
novelty-defense record** for the WildfireGuardian research program.

It does **not** contain wildfire simulation code, routing algorithms, rescue
solvers, or any production decision system. Nothing here runs. Everything here
is evidence, argument, and audit trail.

## The one question this repository answers

> **What has already been done, what is genuinely still open, and exactly which
> WildfireGuardian claims survive the existing literature?**

## The fundamental rule

**Do not try to prove WildfireGuardian is novel. Try to disprove it.**

The literature process here is adversarial. If a prior work already does
something we want to claim, that claim is marked `OCCUPIED` or `WEAKENED` and
the paper is filed as a threat — visibly, permanently, and without softening.
A strong negative novelty result is a successful outcome of this repository,
not a failure. Threatening papers are never hidden, buried in a footnote, or
described in weaker terms than they deserve.

## Repository map

| Path | Purpose |
|---|---|
| `AGENTS.md` | Mandatory reading order and rules for any agent (human or model) modifying this repo |
| `docs/` | Durable context: project scope, thesis, claim registry, novelty standard, protocols |
| `literature/` | Per-paper notes (`notes/`), extracted metadata (`metadata/`), thematic reviews (`reviews/`), local PDFs (`papers/`, gitignored) |
| `novelty/` | Novelty matrix, threat register, surviving/abandoned claims, current verdict |
| `bibliography/` | `wildfireguardian.bib`, `literature.csv`, `doi_registry.csv` |
| `fair/` | Korea Code Fair binder prep, judge questions, one-sentence differences |
| `tasks/` | Roadmap, current work, completed work |

## Start here

1. `docs/PROJECT_CONTEXT.md` — what WildfireGuardian is and is not
2. `docs/CURRENT_THESIS.md` — the two live research questions
3. `docs/CLAIM_REGISTRY.md` — every claim and its current status
4. `novelty/CURRENT_NOVELTY_VERDICT.md` — **the headline answer**
5. `novelty/NOVELTY_THREATS.md` — what could sink us
6. `fair/JUDGE_QUESTIONS.md` — the hard questions and our answers

## Status conventions

Claims use exactly these statuses:

```
SUPPORTED_CANDIDATE   Survived adversarial search so far; still falsifiable
WEAKENED              Prior art covers part of it; the claim must be narrowed
OCCUPIED              A prior work substantially does this already
REJECTED              The claim is false as stated; do not make it
UNKNOWN               Not yet adversarially searched
NEEDS_FULL_TEXT       Verdict blocked on reading the actual paper
```

Threat levels are ranked by **conceptual overlap**, never by venue prestige:

```
CRITICAL  HIGH  MODERATE  LOW  BACKGROUND
```

---

## Current state — 2026-09-19

**Corpus:** 165 verified records · 132 peer-reviewed · 21 preprints ·
10 government reports · 2 software docs · 67 paper notes · 10 thematic reviews

**Verdict:** of 14 registered claims — **1 REJECTED · 4 OCCUPIED · 8 WEAKENED ·
1 SUPPORTED_CANDIDATE · 1 UNKNOWN.** Of 19 novelty-matrix columns, 18 are
occupied. The single empty column, *dispatch-by deadline*, is the program's
entire surviving contribution.

Read `novelty/CURRENT_NOVELTY_VERDICT.md` before anything else.

**Search tier:** S1–S2. No category reached S3; categories 5 (VOI/sensing) and
8 (Korea) did not reach S2. Under `docs/NOVELTY_STANDARD.md` §5 this caps every
positive finding at `SUPPORTED_CANDIDATE`, and **no Korean claim may be
described as searched** until the KCI/RISS/DBpia sweep is completed.

**Verdict expires 2026-12-18.**

## Tooling

Three scripts keep the citations honest. All three should exit clean before any
commit that touches literature:

```bash
python3 bibliography/build_bibliography.py    # metadata -> CSV, BibTeX, matrix
python3 bibliography/verify_dois.py           # Crossref + DataCite resolution
python3 bibliography/check_references.py      # no cited paper_id without a record
```

`literature/metadata/*.yaml` is the single source of truth; the CSV, BibTeX and
novelty matrix are generated, so a citation cannot drift between them. The DOI
auditor compares the registry's title and year against what the registrar
returns — it has already caught four dating errors and two paper_ids written
from memory that named the wrong first author.

## Verification discipline

Every bibliography entry records `publication_status` and `date_verified`.

- Preprints are labeled `PREPRINT`. Always.
- Conference papers are never described as journal publications.
- Government and agency technical reports are never described as peer-reviewed.
- **No invented DOIs. No invented papers.** A field that could not be verified
  is written as `UNVERIFIED`, never guessed.

See `docs/CITATION_RULES.md` and `docs/EVIDENCE_LEVELS.md`.
