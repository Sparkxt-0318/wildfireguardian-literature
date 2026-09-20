# AGENTS.md — Rules for Any Agent Modifying This Repository

This file is binding on every agent (model or human) that edits this repository.

---

## 1. Mandatory reading before ANY modification

You **must** read all six of these before changing a single file:

1. `docs/PROJECT_CONTEXT.md`
2. `docs/CURRENT_THESIS.md`
3. `docs/CLAIM_REGISTRY.md`
4. `docs/NOVELTY_STANDARD.md`
5. `docs/SEARCH_PROTOCOL.md`
6. `novelty/NOVELTY_THREATS.md`

Do not skip this because a task "looks small." Editing a claim status without
knowing the novelty standard, or adding a paper without knowing the existing
threats, corrupts the audit trail.

---

## 2. The adversarial stance is not optional

Your job is to **disprove** WildfireGuardian's novelty.

- Search for the paper that kills the claim, not the paper that flatters it.
- If you find a prior work that does what we want to claim, file it immediately
  at its true threat level and downgrade the claim in the same commit.
- Never write "no one has combined all of these." That is not a novelty
  argument (see `docs/NOVELTY_STANDARD.md` §3).
- Never mark a claim `SUPPORTED_CANDIDATE` because one search returned nothing.
  Absence of evidence in a single query is `UNKNOWN`, not support.

---

## 3. Never fabricate

- **No invented DOIs.** If you did not see the DOI in a retrieved record, write
  `UNVERIFIED`.
- **No invented papers.** Every entry must trace to a retrieved source.
- **No invented page numbers, volumes, or author lists.**
- If you are recalling a paper from training memory rather than from a tool
  result, mark it `RECALL_UNVERIFIED` and file it under
  `docs/SEARCH_PROTOCOL.md` follow-ups. Recall is a search lead, not a citation.
- Do not attribute a claim to a paper unless you have seen text supporting it.
  If you only saw the abstract, say so: evidence level `E2` (see
  `docs/EVIDENCE_LEVELS.md`).

---

## 4. Role separation

| Agent | Role | Hard limit |
|---|---|---|
| **A — Search Researcher** | Systematic search; backward and forward citation chains; wording variants; adjacent fields; preprints; 2025–2026 sweep | **May not decide final novelty alone** |
| **B — Prior-Art Adversary** | For each claim, find the publication that already does it | Must attempt falsification of every claim, not just easy ones |
| **C — Verification / Citation Auditor** | Verify title, authors, year, venue, DOI, publication status, and whether attributed claims are actually supported | **Never trust a single secondary source** |
| **D — Synthesis Researcher** | Novelty matrix, closest-prior-art ranking, exact differences, surviving/weakened/abandoned claims | **Runs only after A–C finish** |

---

## 5. Required edits when you add a paper

Adding a paper is not done until all of these are updated:

- [ ] `literature/notes/<paper_id>.md` (full note template, if key paper)
- [ ] `literature/metadata/<paper_id>.yaml` (structured metadata)
- [ ] `bibliography/literature.csv` (one row)
- [ ] `bibliography/doi_registry.csv` (DOI + verification state)
- [ ] `bibliography/wildfireguardian.bib` (BibTeX, correct entry type)
- [ ] `novelty/NOVELTY_MATRIX.md` (one row, all columns filled or `-`)
- [ ] `novelty/NOVELTY_THREATS.md` (if threat level is MODERATE or above)
- [ ] `docs/claims.yaml` (if it affects any claim's status), then run
      `python3 bibliography/build_claims.py` — `docs/CLAIM_REGISTRY.md` is
      **generated** and must never be hand-edited
- [ ] `docs/SEARCH_PROTOCOL.md` (log the query that found it)

---

## 6. Paper IDs

Format: `<firstauthorlastname><year><keyword>`, lowercase, no punctuation.

Examples: `cova2005trigger`, `dennison2007wuivac`, `mitsopoulos2025peril`.

Collisions get a trailing letter: `cova2005triggera`, `cova2005triggerb`.

---

## 7. Commit discipline

- One coherent unit of literature work per commit.
- Commit message states what the evidence changed, not just what file moved.
  Good: `Downgrade WG-C-003 to WEAKENED: k-PERIL already emits ensemble trigger boundaries`
  Bad: `update docs`
- Never rewrite history on a shared branch.

---

## 8. Copyright

- Short quotes only, with page or section reference.
- Never paste long passages of copyrighted text into notes.
- `literature/papers/` holds local PDFs and is **gitignored** — never commit PDFs.

---

## 8a. Counts are derived, never typed

Claim counts appear in several documents. They are generated from
`docs/claims.yaml` into `<!-- CLAIM-COUNTS:BEGIN/END -->` regions by
`bibliography/build_claims.py`. **Never type a claim count by hand.** A
hand-maintained summary once reported five figures that summed to 15 for 14
claims, and it survived review because nobody adds up a sentence.

`python3 bibliography/build_claims.py --check` exits non-zero if any generated
file is stale. Run it before committing.

---

## 8b. Novelty is scored on four axes, never collapsed

Every claim carries `novelty_axes`: `concept`, `method`, `empirical`,
`operational_artifact`, each one of `OCCUPIED` / `WEAKENED` / `PLAUSIBLE` /
`UNKNOWN`.

Do not collapse them into a single verdict. A dispatch-by algorithm may be
methodologically occupied while a Korean dispatch-by atlas remains empirically
open — one status cannot express that, and collapsing it has previously made
the picture look worse (and in other places better) than the evidence supports.

---

## 8c. How to word a null search result

Forbidden: "0 occupants out of 165 papers, therefore novel."

Required: "**No occupying prior art was identified in the searched corpus.**"

Every surviving claim must additionally report: search coverage · full-text
coverage · unsearched databases · language limitations · publication-date
cutoff · confidence. A claim whose closest threat is only `TITLE_ONLY` or
`ABSTRACT_VERIFIED` cannot be held at high confidence.

---

## 9. When you do not know

Write `UNKNOWN` or `NEEDS_FULL_TEXT` and add it to
`novelty/OPEN_QUESTIONS.md`. An honest gap is worth more than a confident
guess, and a guess in this repository will eventually be read aloud to a judge.
