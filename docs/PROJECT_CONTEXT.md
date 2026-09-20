# PROJECT_CONTEXT.md

## What WildfireGuardian is

WildfireGuardian is a research program about **wildfire protective-action
timing under forecast uncertainty**, with a specific focus on residents who
**cannot self-evacuate**.

It is a simulation-and-analysis program, not a deployed system. Its outputs are
decision-relevant quantities (deadlines, thresholds, skill boundaries) and the
experimental evidence that those quantities are computed correctly and matter.

## What WildfireGuardian is NOT

Stating this precisely matters, because most novelty failures come from
claiming a neighbouring field's territory.

- It is **not** a new fire-spread physics model. It consumes spread models.
- It is **not** a new remote-sensing detection algorithm.
- It is **not** a production dispatch or CAD system for a fire service.
- It is **not** a traffic-simulation engine.
- It is **not** a claim about lives saved. It is a claim about decision timing
  under stated assumptions.

## What this literature repository is for

This repository exists to make the program **falsifiable against prior art**
before the program invests further. Concretely it supports:

1. Korea Code Fair novelty defense (spoken, under hostile questioning);
2. paper introductions and related-work sections;
3. research-direction decisions (what to drop, what to pursue);
4. claim auditing (nothing is asserted that the literature already owns);
5. citation verification (nothing is cited that we have not verified);
6. physical literature binder preparation;
7. continuous monitoring for new papers that threaten or strengthen the work.

## Primary research questions (current)

**RQ1 — Forecast-value boundary.**
How accurate and timely must a wildfire forecast be before forecast-aware
protective action outperforms a strong, *tuned* trigger/buffer policy?

The comparator matters more than the method. A forecast-aware policy beating a
naive fixed buffer is not a result. Beating a well-tuned baseline is.

**RQ2 — Assisted-evacuation dispatch deadline.**
For residents who cannot self-evacuate, what is the latest fire-relative
dispatch time at which a responder can complete the *full* mission:

```
responder base -> resident -> pickup -> safe destination
```

The full round trip, including inbound ingress against the fire and against
outbound traffic, is the unit of analysis. A one-way egress deadline is a
different (and much better-studied) quantity.

## Longer-term directions

These are **not yet claims**. They are directions whose prior art must be
mapped before we invest:

- scarce assisted-evacuation resource allocation (who gets the one vehicle);
- value of information (VOI) for fire observation;
- deadline-aware sensing / decision-directed observation;
- robust protectability (which locations are protectable under model error);
- intervention ranking;
- video / camera-based fire-state observation;
- richer Korean fuel and biological modeling.

## Setting

Korea is the intended application setting. The characteristics below are
listed with their evidence status, because an unsourced setting description is
how an unsupported claim enters a paper by the back door:

| Characteristic | Evidence status |
|---|---|
| Steep terrain amplifies spread | **Sourced** — upslope spread 4.68x downslope at 30 degrees (`an2008slope`) |
| Ridge channelling | **Sourced** — ridge enrichment 2.3 vs 1.5 proximity-only over 118 Korean fires (`choi2026ridgeline`) |
| Gust-driven spread | **Sourced** — +1 m/s peak wind ~ +8.5 ha over 905 fires 1980-2024 (`park2025drivers`) |
| Dense *Pinus densiflora* fuels | **Sourced** — canopy bulk density 1.6x higher in unmanaged stands (`lee2021crownfuel`) |
| Observation latency over Korea | **Sourced** — GK2A mean detection delay 12.9 min; the sub-minute direct-readout tier does not cover Korea (`sung2025geostationary`) |
| Ageing rural population | **Partially sourced** — older adults showed the lowest movement intensity under identical warning content (`an2026donghae`); national demographic structure not yet cited here |
| **Narrow mountain road networks** | **UNSOURCED — do not assert.** No verified Korean road-geometry evidence exists in the corpus (`novelty/OPEN_QUESTIONS.md` C4) |
| Centralized disaster management (KFS, NIFoS, MOIS) | **Sourced** — operational 5 h / 8 h evacuation staging (`mois2025evacuationstages`) |

The road-geometry row is the one that matters most to RQ2, since a dispatch
deadline depends on travel times over that network, and it is precisely the row
we cannot yet support.
Korean specificity is a *possible* axis of novelty, but it is a weak one on its
own — see `docs/NOVELTY_STANDARD.md` §4 on geographic novelty.

## Standing constraints on how we may argue

- Comparator strength is part of the claim. Weak baselines invalidate results.
- Self-generated uncertainty (our model producing both truth and forecast) is
  an OSSE, and must be labeled as one — see `docs/FAILURE_MODES.md` §2.
- Simulated results are evidence about the simulation first, and about the
  world only under stated transfer assumptions.
- We do not medicalize residents. "Cannot self-evacuate" is a mobility and
  transport-access condition, evidenced from transport-disadvantage and
  evacuation-assistance literature, not a diagnosis.
