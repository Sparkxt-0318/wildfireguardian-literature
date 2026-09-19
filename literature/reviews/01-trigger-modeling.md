# Category 1 — Wildfire Evacuation Trigger Modeling

**Author:** Agent A/B (Search Researcher + Prior-Art Adversary)
**Date:** 2026-09-19
**Stance:** adversarial. This review exists to find the paper that kills our claims.
**Evidence caveat:** unless stated otherwise, papers here were assessed at **evidence
level E2 (abstract retrieved)**. Full texts were not obtainable for most Elsevier and
Springer items (HTTP 403 from the publisher to this agent). Every "NEEDS_FULL_TEXT" below
is a real gap, not a formality.

---

## 1. Lineage & timeline

The trigger literature is not a diffuse field. It is essentially **two research groups and
one hand-off**, plus a recent operations-research branch that arrived from outside.

### Branch A — Utah (Cova / Dennison), 2005–2019: the invention

| Year | Paper | What it added |
|---|---|---|
| 2005 | `cova2005trigger` | **The trigger buffer itself.** A level set of modelled fire travel time equal to an estimated evacuation time, computed in GIS. Calabasas Fire case. |
| 2007 | `dennison2007wuivac` | **WUIVAC** and the *strategic* use: 8 years of winds, worst case in 16 directions, fire planning areas, and buffers predicting **closure of all evacuation routes**. |
| 2011 | `larsen2011cedar` | **Forecast winds** make buffers dynamic; first **retrospective validation** against a real front (2003 Cedar Fire). Buffers were conservative by 126 m (1 h) to 1400 m (3 h). |
| 2011 | `cova2011shelter` | The protective action becomes a **choice** (evacuate vs shelter-in-place), not a given. |
| 2013 | `fryer2013entrapment` | Subject changes from residents to **firefighters**; evacuation *mode* (foot / engine / dozer) varied; triggers for entrapment avoidance. |
| 2015 | `li2015household` | **Household-level** triggers; households **ranked by lead time** for staged warnings. |
| 2017 | `li2017reversegeocoding` | Buffers rendered as nameable landmarks a dispatcher can say aloud. |
| 2019 | `li2018coupling` | **Traffic simulation replaces expert judgement** for evacuation time; Monte-Carlo over runs gives a clearance-time CDF and **probability-indexed trigger buffers**. |

### Branch B — Imperial College HAZELAB + Lund (Rein / Ronchi / Gwynne), 2022–2026: the probabilistic re-founding

| Year | Paper | What it added |
|---|---|---|
| 2021 | `wahlqvist2021wuinity` | **WUI-NITY**: FARSITE + pedestrian + LWR traffic in one platform, with PERIL embedded as the trigger sub-model. |
| 2022 | `kalogeropoulos2022kperil` | First announcement of **k-PERIL** (conference **book chapter**, not a journal article). |
| 2023 | `mitchell2023peril` | **PERIL**: triggers as fire-spread time minus evacuation time, with explicit **safety factors**. Swinley Forest (UK) and Roxborough Park (USA). |
| 2023 | `kalogeropoulos2023kperil` | **k-PERIL**: *stochastic* trigger boundaries from historic wind/weather/vegetation variability; **uncertainty rosettes**. Open-source (Zenodo). |
| 2023 | `ronchi2023verification` | A **24-test verification protocol** for coupled fire/pedestrian/traffic/trigger models. |
| 2025 | `kalogeropoulos2025dire` | Fire spread **and** evacuation time both probabilistic; the **evacuation safety factor** in [0,1]; "trigger boundaries define the latest wildfire location with a low risk of a dire evacuation." Mati 2018, forensic. |
| 2026 | `kalogeropoulos2026ensemble` | **Multi-model ensemble** triggers (Farsite, Prometheus/WISE, ELMFIRE, Google EPD, EPD-ConvLSTM). Fort McMurray. Boundaries differ by model; and Fort McMurray's triggers "extend beyond practical detection distances." |

### Nomenclature correction (important for the defence)
The task brief referred to a "**Mitsopoulos**" PERIL lineage. That name does **not** appear
on any PERIL or k-PERIL record retrieved. The correct authorship is
**Harry Mitchell** (PERIL) and **Nikolaos Kalogeropoulos** (k-PERIL), with Guillermo Rein,
Enrico Ronchi and Steve Gwynne. Saying "Mitsopoulos" in a fair defence would be an
immediate credibility loss. `RECALL_UNVERIFIED`: no author named Mitsopoulos was located in
this literature.

---

## 2. What a "trigger" *is* across the literature

Four incompatible senses are all called "trigger." Conflating them is the commonest error.

1. **Geometric trigger (Cova 2005 →).** A polygon. Decision rule: fire crosses edge →
   act. Unit: distance. Encodes time only implicitly.
2. **Landmark trigger (Li 2017).** The polygon snapped to a nameable feature (ridge, road,
   river) so it can be communicated over radio. Unit: a place name.
3. **Safety-factor trigger (Mitchell 2023).** The geometric trigger inflated by a
   deterministic margin. Unit: distance, with an engineering margin.
4. **Probabilistic trigger (Li 2019; k-PERIL 2023; Kalogeropoulos 2025, 2026).** A family
   of boundaries indexed by the probability that the protective action completes. Unit:
   distance conditioned on a probability — or, in Kalogeropoulos 2025, collapsed to a
   **scalar safety factor in [0,1]**.

**The protective action is almost always the same across all four: one-way household
egress by private car.** The two exceptions are `fryer2013entrapment` (firefighter egress
to a safety zone, still one-way) and `dennison2007wuivac` (route closure, still about
getting out).

---

## 3. Comparison table

`det` = deterministic, `prob` = probabilistic. "—" = not addressed. "?" = NEEDS_FULL_TEXT.

| Paper | Trigger definition | Protective action | Det / prob | Traffic? | Household? | Mobility-specific? | Forecast uncertainty? |
|---|---|---|---|---|---|---|---|
| `cova2005trigger` (2005) | Level set of fire travel time = given evacuation time | Community egress | det | no | no | no | no |
| `dennison2007wuivac` (2007) | Same, per worst-case wind in 16 directions; + route-closure buffers | Community egress; route viability | det (worst-case envelope) | no | no | no | no (climatology) |
| `larsen2011cedar` (2011) | Hourly buffer from **forecast** wind | Community egress | det, forecast-driven | no | no | no | **uses** forecast; does not quantify its error |
| `cova2011shelter` (2011) | n/a — a decision model over actions | Evacuate **vs** shelter-in-place | det + decision analysis | no | no | no | no |
| `fryer2013entrapment` (2013) | Buffer sized to firefighter escape time | **Firefighter** egress to safety zone | det, 80 input combinations | no | no | **mode**-specific (foot/engine/dozer) | no |
| `li2015household` (2015) | One buffer **per household**; households ranked by lead time | Staged household egress | det | no | **yes** | no | no |
| `li2017reversegeocoding` (2017) | Buffer snapped to named landmark | Community egress | det | no | no | no | no |
| `li2018coupling` (2019) | Buffer from the **CDF of simulated clearance time** | Community egress | **prob (over traffic)** | **yes** | no | no | no |
| `wahlqvist2021wuinity` (2021) | PERIL buffer inside a 3-layer platform | Community egress | det | **yes** (LWR) | partial | partial (pedestrian layer) | no |
| `mitchell2023peril` (2023) | Fire time − evacuation time, + safety factor | Community egress | det + margin | via WUI-NITY | no | no | no |
| `kalogeropoulos2023kperil` (2023) | Boundary distribution from historic wind/weather/fuel sampling | Community egress | **prob (climatological)** | no | no | no | **no — historic variability, not forecast error** |
| `ronchi2023verification` (2023) | n/a — verification tests for the above | all layers | n/a | yes | yes | yes | n/a |
| `kalogeropoulos2025dire` (2025) | Latest fire location with low risk of a "dire" evacuation; **safety factor ∈ [0,1]** | Community egress | **prob (fire AND evacuation)** | implicit in evac time | no | no | no |
| `kalogeropoulos2026ensemble` (2026) | Boundary from a **multi-model ensemble** of spread models | Community egress | **prob (over models)** | no | no | no | **model** uncertainty, not forecast skill |

**No row in this table has a responder inbound leg, a pickup dwell, or a dispatch time.**

---

## 4. What the lineage has definitively settled

State these as settled in any paper introduction. Do not re-derive them and do not claim
them.

1. **Coupling a modelled future fire to a protective-action decision is twenty-one years
   old.** (`cova2005trigger`) → WG-C-001 is REJECTED and the sentence is *false*, not merely
   unoriginal.
2. **Forecast-driven, time-varying triggers exist and have been validated retrospectively
   against a real fire front.** (`larsen2011cedar`, 2011.)
3. **Household-resolution triggers and lead-time ranking exist.** (`li2015household`, 2015.)
4. **Trigger buffers derived from a simulated clearance-time distribution, indexed by
   completion probability, exist.** (`li2018coupling`, 2019.)
5. **Stochastic trigger boundaries with a spatial uncertainty product exist, are
   peer-reviewed, and are open source.** (`kalogeropoulos2023kperil`, 2023.)
6. **Multi-model-ensemble trigger boundaries exist, including ML emulators alongside
   physical simulators.** (`kalogeropoulos2026ensemble`, 2026.)
7. **The output can legitimately be a scalar probability of protective-action failure.**
   (`kalogeropoulos2025dire`, 2025 — the "evacuation safety factor.")
8. **The community has a published verification protocol** for models of exactly this kind.
   (`ronchi2023verification`, 2023.) Not using it is now a defect.
9. **Trigger boundaries can be operationally impossible.** Fort McMurray's triggers
   "extend beyond practical detection distances under rapid fire spread conditions"
   (`kalogeropoulos2026ensemble`). This is a *published* latency failure.

---

## 5. What the lineage has NOT done

Each item is stated as the specific gap, with the nearest occupant named so we cannot
later pretend the gap is larger than it is.

1. **No inbound leg.** Every trigger in this literature bounds a one-way movement *away*
   from the fire. Nothing here computes feasibility for a vehicle travelling *toward* the
   fire. Nearest: `dennison2007wuivac` route-closure buffers (a road becoming unusable),
   and `fryer2013entrapment` (a responder subject, but still egressing).
2. **No round trip, no pickup dwell.** No paper in Category 1 chains ingress + dwell +
   egress into a single feasibility constraint.
3. **No dispatch time as the output.** The outputs are polygons, landmark names, or a
   scalar risk. None is a clock time at which a unit must depart.
4. **No forecast-error model — only variability.** This is the sharpest surviving
   distinction and it must be stated carefully. k-PERIL samples **historic** wind/weather/
   fuel variability; the 2026 paper samples **model** disagreement; `larsen2011cedar`
   *consumes* a forecast without characterising its error. **Nobody sweeps forecast skill,
   lead time and latency as independent variables and reports a decision-value boundary.**
   That is where WG-C-002/WG-C-012 still live.
5. **No tuned comparator study.** `li2018coupling` produces a well-founded buffer, but no
   paper in this lineage *optimises* a buffer over a scenario distribution and then asks
   whether anything beats it. WG-C-006 therefore describes an evaluation practice that is
   absent — but absence of a practice is weak novelty (N3), not a contribution.
6. **No mobility-restricted subject.** Category 1 assumes every protected person can drive
   away. `fryer2013entrapment` varies *mode* but for able responders. The non-self-
   evacuating resident does not appear in this literature at all — that person appears only
   in the Category 3 / operations-research branch (see `03-wildfire-traffic.md` §4).
7. **No Korean setting located** in the trigger lineage. That is N4 and weak on its own
   (NOVELTY_STANDARD §4) and should only be used under §4(a) or §4(c).

---

## 6. Direct implications for WG-C-003 and WG-C-002

### WG-C-003 (inbound-inclusive dispatch deadline)
**Category 1 does not kill it.** No trigger paper computes a responder round-trip deadline.
But Category 1 does constrain how we may phrase it:

- We may **not** say "we are the first to model future fire spread for evacuation timing."
  (`cova2005trigger`.)
- We may **not** say "we are the first to compute triggers probabilistically."
  (`kalogeropoulos2023kperil`.)
- We may **not** say "we are the first to compute a *latest safe* protective-action
  moment under uncertainty." (`kalogeropoulos2025dire` says exactly that for egress.)
- The only sentence Category 1 leaves standing is the narrow one:
  *the latest fire-relative **dispatch** time for a **responder round trip** with fire-
  arrival feasibility enforced on the **inbound** leg.*
  The threat to that sentence comes from Category 3, not from here.

### WG-C-002 (forecast-skill boundary vs a tuned trigger)
**Category 1 weakens but does not occupy it.** The machinery to *make* a probabilistic
trigger is fully published. What is missing is the *evaluation axis*: nobody varies forecast
quality and reports where forecast-aware action starts to beat a tuned positional trigger.

Two dangers, both real:
- `li2018coupling` already supplies the **tuned comparator** we planned to introduce. Our
  comparator claim (WG-C-006) must be framed as *adopting* their percentile-indexed,
  simulation-derived buffer, not inventing it.
- `kalogeropoulos2026ensemble`'s detection-distance finding is a published instance of the
  latency argument behind WG-C-012. It is one observation about one town, not a swept
  boundary — but a hostile judge who has read it will ask why ours is different, and
  "we sweep latency; they reported one case" must be demonstrable, not asserted.

**Recommended status changes** (for the synthesis agent, not applied here):
WG-C-004 → **OCCUPIED** (`kalogeropoulos2023kperil`, `kalogeropoulos2026ensemble`,
`li2018coupling`). WG-C-006 → **WEAKENED** (`li2018coupling`, `ronchi2023verification`).
WG-C-001 → stays REJECTED, closest prior art now named: `cova2005trigger`.
