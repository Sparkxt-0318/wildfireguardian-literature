# NOVELTY_STANDARD.md

The standard of proof this repository applies before any claim may be called
novel. It is deliberately hard to satisfy.

---

## §1. Novelty is a property of a *claim*, not of a *project*

"WildfireGuardian is novel" is not a checkable statement. Only sentences in
`docs/CLAIM_REGISTRY.md` are checkable. Every novelty discussion must resolve
to a claim ID.

---

## §2. The four novelty types, ranked by strength

| Type | Definition | Strength | Typical fate |
|---|---|---|---|
| **N1 — Problem novelty** | The decision question itself has not been posed | Strongest | Rare; usually someone posed it in another hazard |
| **N2 — Quantity novelty** | The output quantity has not been computed before | Strong | Our best realistic target (e.g. inbound-inclusive dispatch deadline) |
| **N3 — Methodological novelty** | The method is new *as a method* | Strong but expensive | We are unlikely to beat the OR/ML literature at its own game |
| **N4 — Application novelty** | Known method, new domain/region/dataset | **Weak alone** | Acceptable only when bundled with N2, or with a *demonstrated* domain-specific failure of the known method |

A claim resting solely on N4 is filed as `WEAKENED` by default, not
`SUPPORTED_CANDIDATE`.

---

## §3. Forbidden novelty arguments

These do not count and will be rejected in review:

1. **Conjunction novelty** — "no one combines all of A, B, C, D." Any
   sufficiently long conjunction is unique. If the combination is the claim,
   you must state *why the combination changes the answer* — what conclusion
   does joint treatment produce that the parts cannot?
2. **Search-failure novelty** — "we searched and found nothing." A null search
   yields `UNKNOWN`, never support. Only a *documented protocol* search
   (`docs/SEARCH_PROTOCOL.md`) that included adjacent fields, synonyms,
   preprints, and non-English literature can support a claim, and even then it
   yields `SUPPORTED_CANDIDATE`, never certainty.
3. **Prestige novelty** — "no *top-venue* paper does this." Irrelevant. A 2019
   regional workshop paper occupies a claim exactly as thoroughly as a Nature
   paper.
4. **Implementation novelty** — "our code does it differently." Not a research
   claim.
5. **Scale novelty without consequence** — "we run more scenarios." Only counts
   if the extra scale changes a conclusion.

---

## §4. Geographic / national novelty (the Korea question)

"First in Korea" is N4 and is **not sufficient**. It becomes admissible only if
at least one of these is demonstrated, not asserted:

- (a) A Korean-specific condition (fuel structure, terrain slope distribution,
  road geometry, population age structure) **changes the answer** relative to
  published settings — and we show the change, not just the difference in
  inputs.
- (b) The published method **fails** on Korean data in a way we document.
- (c) No comparable analysis exists *anywhere* for the quantity, and Korea is
  merely where we did it — in which case the novelty is N2, and Korea is
  incidental and should be described as such.

Writing "first Korean X" without (a), (b), or (c) is a judge-bait sentence.
See `fair/JUDGE_QUESTIONS.md` Q7.

---

## §5. Burden of proof

| To move a claim to | You must provide |
|---|---|
| `REJECTED` | One verified prior work that does it, with the specific section/result cited |
| `OCCUPIED` | Same as REJECTED (OCCUPIED = the space is taken; REJECTED = our sentence is false) |
| `WEAKENED` | A prior work covering a strict subset, plus the narrowed claim text |
| `SUPPORTED_CANDIDATE` | A completed protocol search per `SEARCH_PROTOCOL.md` across ≥4 wording variants, ≥2 adjacent fields, ≥1 preprint server, ≥1 non-English pass, with the query log committed |
| `NEEDS_FULL_TEXT` | A named paper whose abstract is insufficient to decide |
| `UNKNOWN` | Nothing — this is the default |

**Asymmetry is intentional.** One paper can kill a claim. No number of searches
can prove one.

---

## §6. Difference statements must be operational

Unacceptable: "We consider uncertainty, they do not."

Acceptable: "Cova et al. (2005) compute a trigger boundary from a single
deterministic FARSITE run with fixed weather; the boundary is a level set of
fire arrival time. We compute the latest dispatch time such that a
responder round trip closes under *P* of an ensemble's arrival-time
distribution. The outputs have different units (distance/level-set vs.
time-to-dispatch) and different decision subjects (household egress vs.
responder dispatch)."

The test: could a reader reproduce the distinction without asking us what we
meant? See `fair/ONE_SENTENCE_DIFFERENCES.md`.

---

## §7. Continuous falsification

A `SUPPORTED_CANDIDATE` claim is not settled. Each claim carries
`last_reviewed`. Any claim older than 90 days is automatically re-opened to
`UNKNOWN` at the next audit unless re-searched. New 2025–2026 preprints are the
most likely killers and are swept separately.

---

## §8. Four axes, scored separately

A claim's novelty is scored on four axes, never collapsed into one verdict:

| Axis | Question | Field |
|---|---|---|
| **CONCEPT_NOVELTY** | Has anyone posed this question or defined this quantity? | `concept` |
| **METHOD_NOVELTY** | Is the way we compute it new *as a method*? | `method` |
| **EMPIRICAL_NOVELTY** | Is the *result* — the numbers, for this setting — new? | `empirical` |
| **OPERATIONAL_ARTIFACT_NOVELTY** | Is the produced artifact (an atlas, a map, a benchmark, a dataset) new and usable? | `operational_artifact` |

Each takes one of `OCCUPIED` · `WEAKENED` · `PLAUSIBLE` · `UNKNOWN`.

**Why this matters.** A single status forces a false choice. A dispatch-by
algorithm may be methodologically occupied while a Korean dispatch-by atlas
remains empirically open; collapsing those into "WEAKENED" hides a real
contribution, and collapsing them into "PLAUSIBLE" claims one we do not have.

The axes are stored in `docs/claims.yaml` under `novelty_axes` and rendered
into the registry. **An empirical or artifact contribution is a legitimate
scientific contribution.** A program with `method: OCCUPIED` and
`empirical: PLAUSIBLE` is not a failed program — it is an empirical paper.

---

## §9. Decomposition before scoring

Do not score a compound claim. Split it into components that can be occupied
independently, and score each on its own evidence.

"We compute the latest dispatch time for an assisted evacuation" is not one
claim; it is at least seven (`novelty/DBD_DECOMPOSITION.md`). A paper that
models a responder round trip does not thereby report a latest dispatch instant,
and a paper that reports a single deadline does not thereby represent a
non-monotone feasible *set*.

Scoring the compound is how conjunction novelty (§3.1) creeps back in wearing a
different hat: the compound always looks open because no single paper does all
of it. Score the parts; state which parts are ours.

---

## §10. Full-text tier gates confidence

Every threatening paper carries `fulltext_status`, one of:

```
TITLE_ONLY < ABSTRACT_VERIFIED < FULL_TEXT_READ < METHODS_VERIFIED < RESULTS_VERIFIED
```

**A claim may not be held at high confidence when its closest threat has been
read only at `TITLE_ONLY` or `ABSTRACT_VERIFIED`.** Concluding that a paper
does *not* compute our quantity, on the strength of its abstract, is not a
finding — abstracts omit most of what a paper does, and the omission is exactly
where an occupant hides.

`bibliography/check_fulltext_tiers.py` reports each claim's ceiling and, with
`--strict`, fails while any `CRITICAL` paper is below `FULL_TEXT_READ`.

---

## §11. Required reporting for every surviving claim

A claim may not be listed as surviving unless it reports all six:

```
search coverage            which tiers/queries actually ran
full-text coverage         tier of the closest threats
unsearched databases       named, not gestured at
language limitations       which literatures were not read
publication-date cutoff    when the sweep stopped
confidence                 bounded by §10
```

"No occupying prior art was identified in the searched corpus" is the required
wording for a null result. Never "0 occupants, therefore novel" — a null search
establishes `UNKNOWN` (§3.2), and only full-text comparison against the closest
work can support more.
