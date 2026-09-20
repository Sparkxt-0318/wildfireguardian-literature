# NOVELTY_THREATS.md

**Last updated:** 2026-09-19 · **Corpus:** 165 verified records
(132 peer-reviewed · 21 preprints · 10 government reports · 2 software docs)

Threat levels rank **conceptual overlap**, never venue prestige. A 2026 arXiv
preprint and a NIST report outrank a famous journal paper here whenever they
sit closer to what we want to claim.

Counts: **CRITICAL 11 · HIGH 42 · MODERATE 36 · LOW 12 · BACKGROUND 64**

---

## 1. Closest prior art — top 10

Ranked by conceptual overlap with the two live research questions.

| Rank | Paper | Similarity | What it already does | What it does not do | Threat |
|---|---|---|---|---|---|
| 1 | `moradi2026supported` — Moradi, Sauré & Patrick, arXiv:2608.05413 (**PREPRINT**) | Very high on RQ2 | Two-stage stochastic **supported evacuation in wildfires**: shelter location + fleet sizing + split pickup/delivery routing. Vehicles start at a base, drive **in**, dwell at an assembly area, deliver out. **Hard time window on every arc, defined as the time after which the route "is reached by the fire."** | Fire is never simulated: windows are sampled `Uniform(400,850)` min with a categorical fire-origin label. Output is a routing plan and fleet size (6 ambulances, 16 buses), never a departure time. No forecast, skill, or latency. | **CRITICAL** |
| 2 | `beyki2026modular` — Beyki et al., *Safety Science* 199:107200 | Very high on RQ2 | Names "the lack of inbound traffic and rescue operations" as the field's gap **and closes it**: high-resolution fire model drives live road-segment closure, explicit **emergency extraction** agents, adaptive rerouting on **inbound** legs, validated against a Portuguese drill. | Reports simulated evacuation/extraction outcomes, not a latest-dispatch quantity — **pending full text, which could change this row.** | **CRITICAL** |
| 3 | `kalogeropoulos2026ensemble` — Kalogeropoulos & Rein, *Fire Safety Journal* 165:104912 | Total on WG-C-004 | Trigger boundaries from a **multi-model ensemble** of flame-spread models (Farsite, Prometheus/WISE, ELMFIRE, Google EPD, EPD-ConvLSTM), Fort McMurray. Finds triggers extend beyond practical detection distances. | Egress triggers for self-evacuating communities. No responder, no pickup, no dispatch time. | **CRITICAL** |
| 4 | `regnier2008public` — Regnier, *Management Science* 54(1):16–28 | High on RQ1 | Derives the **forecast-quality boundary for evacuation ordering**: a 10% miss probability requires ≥76% false alarms. This is WG-C-002's object, in hurricanes, since 2008. | Hurricanes; single evacuate/don't decision; no tuned spatial-trigger comparator; no wildfire. | **HIGH** |
| 5 | `ardid2026forecastvalue` — Ardid et al., *IJWF* 35(4):WF25221 | High on RQ1 | **Skill → potential economic value in wildfire**, sub-hourly, Australian regions, against the Fire Behaviour Index. | Fire-danger forecasting, not evacuation mission feasibility; comparator is an index, not a tuned trigger. | **HIGH** |
| 6 | `murphy1987accuracyvalue` — Murphy & Ehrendorfer, *Weather and Forecasting* 2(3):243–251 | Total on WG-C-014's proposition | Establishes that forecast **accuracy is not monotone with value** in the cost-loss situation. **1987.** | Scalar cost-loss; no spatial field; no IoU; no routing. | **HIGH** |
| 7 | `li2018coupling` — Li, Cova & Dennison, *Fire Technology* 55(2):617–642 | High on WG-C-006 | Replaces expert judgement with traffic simulation, derives a clearance-time CDF, emits **percentile-indexed trigger buffers** (160 min at 95%; 292 min at doubled demand). This *is* the tuned comparator we proposed to introduce. | Egress only; no responder; buffer is a distance, not a dispatch time. | **CRITICAL** |
| 8 | `mois2026aievacroute` — KFS/MOIS programme announcement (**GOVERNMENT REPORT, not peer-reviewed**) | High on WG-C-007 and RQ2's framing | Announced 2026-09: AI wildfire/smoke spread prediction that outputs resident evacuation routes **and 진화 인력·장비의 투입 경로 — ingress routes for suppression personnel and equipment.** | Under development, not deployed; outputs routes, not a dispatch-by deadline; serves suppression crews, not assisted-evacuation vehicles. Primary MOIS release not retrieved. | **HIGH** |
| 9 | `sun2025decisionfocusedsensing` — Sun, Hults & Xu, BuildSys '25 | High on WG-C-008 | Decision-focused **sensor selection and forecaster training on evacuation decision regret**, floods, peer-reviewed. | Floods; no deadline conditioning; no wildfire. | **CRITICAL** |
| 10 | `yu2020disruption` — Yu et al., *Nature Sustainability* | High on RQ2's premise | **Inbound responder feasibility under a modelled hazard**, targeting care homes and sheltered accommodation, at national scale. | Floods; accessibility disruption statistics, not a per-mission dispatch deadline. | **HIGH** |

Runners-up that matter: `kalogeropoulos2025dire` (*Safety Science* 181:106691) defines a trigger as "the latest wildfire location with a low risk of a dire evacuation" and emits an evacuation safety factor ∈[0,1] — structurally the same *kind* of output RQ2 wants, for egress. `rambha2021staged` (*TR-E* 151:102321) is a forecast-value result for non-self-evacuating people in all but name. `tang2025transit` (*TR-C* 180:105342) is transit evacuation of carless populations by RL — **the paper most likely to move RQ2 unnoticed, because it is not indexed as wildfire work.** `averill2007emergencyresponse` (NIST IR 7425, **government report**) put responders in counterflow against evacuating occupants in 2007.

---

## 2. Threats by claim

### WG-C-003 — dispatch-by deadline (the program's best claim)
Four of its five components are occupied:

| Component | Occupied by | Status |
|---|---|---|
| Non-self-evacuating residents modelled | `moradi2026supported`, `flores2023goal`, `shahparvari2017robust` | **Occupied** |
| Inbound responder simulated with outbound evacuation | `beyki2026modular`, `averill2007emergencyresponse` | **Occupied — this sentence must be struck from our claim** |
| Pickup dwell + delivery in one routed mission | `moradi2026supported`, `flores2023goal` | **Occupied** |
| Fire-arrival feasibility on the **inbound** leg | `moradi2026supported` (in form) | **Occupied in form** |
| **Latest dispatch time reported as the output, from a modelled future fire, as a function of forecast error** | *no occupying prior art identified in the searched corpus* | **Open, pending full-text comparison** |

### WG-C-004 — probabilistic/ensemble triggers
Three independent occupants: `kalogeropoulos2023kperil`, `kalogeropoulos2026ensemble`, `li2018coupling`. **Unclaimable.**

### WG-C-002 / WG-C-012 — forecast value and latency
Concept owned (`regnier2006dynamic`, `regnier2008public`), wildfire application owned (`ardid2026forecastvalue`), lead-time-as-variable owned (`bischiniotis2019tradeoffs`, `lopez2020bridging`), threshold tuning owned (`bouttier2024optimal`).

### WG-C-014 — accuracy ≠ decision quality
Owned since **1987** (`murphy1987accuracyvalue`, `chen1987qualityvalue`), restated by `mandi2024dfl`, `liu2026dflfail`, `raeth2025decisionskill`, and shown on wildfire tasks by `xu2026wildfirefm`.

### WG-C-008 — decision-directed sensing
Method owned (`malings2016voisensor`, `rossa2026actionbed`), hazard-evacuation application owned (`sun2025decisionfocusedsensing`), wildfire sensing owned (`shao2026beliefaware`, `papaioannou2026adaptive`, `roysingh2025constellation`).

### WG-C-007 — Korean setting
`kwon2025koreaevac`, `chang2026multiscale`, `kwak2021evacroute`, `nifos2018evacsystem`, plus the operational `mois2025evacuationstages` (5 h / 8 h rule, **with vulnerable groups directed to evacuate in advance**) and `mois2026aievacroute`.

---

## 3. Sentences that are now forbidden

Each is false against a verified record. Saying any of them at the fair is an
immediate, deserved loss of credibility.

- "First to model future wildfire spread for evacuation routing." → `cova2005trigger` (2005).
- "First to use probabilistic or ensemble fire predictions for triggers." → `kalogeropoulos2023kperil`, `kalogeropoulos2026ensemble`.
- "No one models responders moving inbound against evacuees." → `beyki2026modular`, `averill2007emergencyresponse`.
- "No one models evacuation of people who cannot self-evacuate." → `moradi2026supported`, `flores2023goal`, `shahparvari2017robust`.
- "Nobody has done forecast value for wildfire." → `ardid2026forecastvalue`.
- "We are the first to note that prediction accuracy ≠ decision quality." → `murphy1987accuracyvalue` (1987).
- "First Korean wildfire evacuation study." → `kwak2021evacroute`, `kwon2025koreaevac`, `nifos2018evacsystem`.
- "Korea has no wildfire evacuation timing rule." → `mois2025evacuationstages` (5 h / 8 h, operational since April 2025).
- "Korea ignores people who cannot self-evacuate." → `mois2025evacuationstages` directs 고령자 등 to evacuate in advance.
- "No one routes responders inbound in Korea." → `mois2026aievacroute`.
- "PERIL/k-PERIL is the Mitsopoulos lineage." → **Not a person on these papers.** PERIL is Mitchell, Gwynne, Ronchi, Kalogeropoulos & Rein; k-PERIL is Kalogeropoulos, Mitchell, Ronchi, Gwynne & Rein.

---

## 4. Watch list — threats not yet resolved

Ranked by how much damage they do if the full text says what we fear.

1. **`beyki2026modular`** — if its full text reports a latest-extraction or
   safe-time-remaining quantity per waypoint, **WG-C-003 moves to OCCUPIED**
   and RQ2 must be abandoned or re-scoped. *Highest priority read in the repo.*
2. **`moradi2026supported` journal version** — if peer review adds
   spread-model-derived time windows, the last structural difference closes.
3. **`tang2025transit`** — abstract never retrieved. Transit evacuation of
   carless populations is structurally our trip and is not indexed as wildfire.
4. **Kamyabniya (2022)** — a citation-only lead inside Moradi §2, described as
   two-stage stochastic supported evacuation with shelter location and routing.
   Unidentified. Could be another CRITICAL.
5. **`murphy1987accuracyvalue` / `chen1987qualityvalue`** — known at E1/E2 only,
   and they are the load-bearing killers of WG-C-014.
6. **Korean KCI/RISS/DBpia keyword sweep could not be completed** (server-side
   search undrivable, DBpia 503). This is the largest remaining blind spot for
   a missed Korean claim-killer.
