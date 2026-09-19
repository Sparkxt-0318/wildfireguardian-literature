# INCLUSION_CRITERIA.md

A work is included in this repository if it satisfies **at least one** of the
following, and is verifiable per `docs/CITATION_RULES.md`.

## I1 — Direct prior art
It addresses any decision quantity WildfireGuardian claims: evacuation trigger,
protective-action timing, evacuation deadline, dispatch timing, assisted
evacuation, forecast value for protective action.
*Include even if the hazard is not wildfire.* Hurricane and flood work occupies
our formulations just as effectively.

## I2 — Methodological dependency
We rely on its method, assumption, or finding — fire spread models, observation
characteristics, statistical methods, OSSE design. Threat level is typically
`BACKGROUND`, but the dependency must be documented because it is what a judge
will probe when asking "how do you know your fire model is right?"

## I3 — Adjacent-field occupancy
It occupies a formulation we might otherwise claim as novel — PDPTW, VRP with
time windows, informative path planning, Bayesian experimental design,
decision-focused learning. These are the most commonly missed threats, because
they are indexed under vocabulary the fire community does not use.

## I4 — Empirical grounding
It supplies real-world numbers we need: evacuation response curves, rates of
spread, observation latency, road network characteristics, demographic
composition of at-risk populations.

## I5 — Setting evidence
It documents the Korean (or comparable) setting: fuels, terrain, road geometry,
population structure, institutional arrangements, event chronologies.

## I6 — Evaluation-standard evidence
It establishes how work of this kind must be evaluated, or documents a common
evaluation failure (weak baselines, pseudoreplication, inverse crime).

---

## Recency
No date cutoff. Foundational work from the 1970s–2000s is as relevant as 2026
preprints. **However**, 2025–2026 work receives a dedicated sweep because it is
the most likely source of an unnoticed claim-killer.

## Language
Korean and English are first-class. Other languages are included where the work
is directly relevant; record the language in metadata. Do not exclude a paper
because reading it is inconvenient — mark it `NEEDS_FULL_TEXT`.

## Publication status
Preprints, theses, and government reports are included, and labeled as such.
Their evidence weight differs (`docs/EVIDENCE_LEVELS.md`) but **their
novelty-occupying power does not**: a 2025 arXiv preprint that computes our
quantity occupies it. Priority is priority.
