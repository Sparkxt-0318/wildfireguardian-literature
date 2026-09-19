# 04 — Forecast-Value Literature (Category 4)

**Agent:** A/B — Search Researcher + Prior-Art Adversary
**Date:** 2026-09-19
**Scope:** forecast value, cost-loss / decision-analytic frameworks, relative
economic value, forecast skill vs decision value, evacuation-order timing under
forecast uncertainty (hurricane, flood, severe weather, volcano, wildfire),
act-now-vs-wait / optimal stopping, forecast latency and timeliness, decision
thresholds, false-alarm/hit-rate trade-offs.
**Claims under attack:** WG-C-002, WG-C-006, WG-C-012, WG-C-014.
**Search log:** `docs/search-logs/agent-forecast-voi.md`.

> Reading instruction for anyone defending this project: this review is written
> to *lose* arguments, not to win them. Everything below that is marked generic
> prior art must be conceded immediately and cheerfully in a judge exchange. The
> only defensible ground is what is left after the concessions.

---

## 1. The canonical frameworks and who owns them

There are three distinct, mature bodies of theory here. None of them is ours.

### 1.1 The cost-loss / decision-analytic framework — **Murphy owns it**

| Work | What it established |
|---|---|
| `murphy1977costloss` (MWR 105(7):803-816) | The expense expressions and the *relative value* measure for climatological / categorical / probabilistic / perfect forecasts in the two-action, two-event cost-loss situation. |
| `murphy1987accuracyvalue` (WAF 2(3):243-251) | **Accuracy and value are not monotonically related** in the cost-loss situation. |
| `chen1987qualityvalue` (MWR 115(8):1534-1541) | The same non-monotonicity generalised to the N-action cost-loss situation. |
| `murphy1994assessing` (Met. Apps 1(1):69-73) | Survey: the machinery was already mature in 1994. |

The 1987 pair is the single most important finding of this review. **The
proposition underlying WG-C-014 is 39 years old.**

### 1.2 Relative Economic Value (REV) for ensembles — **Richardson / Zhu own it**

`richardson2000relative` (QJRMS 126(563):649-667) and `zhu2002economic`
(BAMS 83(1):73-83) made REV the standard operational instrument: value plotted
as a function of the cost-loss ratio C/L, with climatology as the reference and
the optimal probability threshold chosen per C/L. The *region of C/L where the
forecast has positive value* is already a forecast-value boundary. Recent work
(`stephenson2025extremeloss`, `olivetti2026compounding`,
`shanker2024` — see search log) extends REV to loss variance, compounding
extremes and declining user trust.

### 1.3 Sequential / dynamic decision under improving forecasts — **Regnier owns it**

`regnier2006dynamic` (WAF 21(5):764-780) reframed preparation as a sequence of
decisions in which the decision maker anticipates *future* forecasts whose
accuracy improves as lead time declines. `regnier2008public` (Mgmt Sci
54(1):16-28) turned this into a location-specific statement about the
false-alarm rate forced by a required miss probability. `georgakakos2025evacuationtiming`
(Nat. Hazards 121(16):18849-18878) carried the same structure into 2025 with an
explicit evacuation-completion-time term.

---

## 2. Hazard-by-hazard state of the art

### Hurricane
The most decision-theoretically developed hazard. Regnier (2006, 2008) gives
both the dynamic act-now-vs-wait model and the achievable
(miss-probability, false-alarm-rate) frontier per location, driven by a Markov
track model and a fixed clearance time. Nothing in this literature models a
responder round trip; clearance time is exogenous.

### Flood
`verkade2011estimating` (HESS 15:3751-3765) established REV for deterministic vs
probabilistic flood forecasts across lead times. The humanitarian
forecast-based-action community then made *timing* explicit:
`bischiniotis2019tradeoffs` (IJDRR 40:101252) solves for the **optimal lead time
to trigger action as a function of forecast quality and the operational
characteristics of the action**, and shows two-stage (long-lead low-certainty +
short-lead high-certainty) designs dominate. `lopez2020bridging`
(Weather Clim. Extremes 27:100167) selects the joint
(magnitude, probability threshold, lead time) that should trigger action.

### Severe weather / precipitation
`bouttier2024optimal` (NHESS 24(8):2793-2816) computes user-specific *optimal*
decision thresholds and reports an explicit usability boundary in
(intensity, spatial scale). Tornado-warning work (Simmons & Sutter, as relayed —
`RECALL_UNVERIFIED`, see search log) reports a **non-monotone** lead-time effect:
lead times up to ~15 min reduce fatalities, longer ones do not.

### Volcano
A 2026 *Nature Communications* paper on the socio-economic value of data-driven
eruption forecasts balancing false alarms against catastrophic loss appeared in
search; **not verified, listed as a search lead only** (see search log).

### Wildfire — the decisive section
Until 2026 the honest answer was "the forecast-value machinery has not been
applied to wildfire". That is **no longer true**:

- `ardid2026forecastvalue` (Int. J. Wildland Fire 35(4):WF25221, 2026) runs the
  full pipeline: ML sub-hourly fire-potential forecasts, TPR/FPR discrimination,
  and **Potential Economic Value** against the Fire Behaviour Index. Headline:
  ~10-30% skill gain, ~2x potential savings.
- `berlinghieri2024pm25` (arXiv, PREPRINT) evaluates six operational wildfire-smoke
  forecasts on two explicit *decision* tasks against a **persistence baseline**,
  finding no forecast substantially beats persistence for the go/no-go decision
  while most beat it for the when-to-go decision.
- `simon2022wildfirevoi`, `hope2024wildfiresat`, `frisvold2024demandinfo` cover
  the wildfire *information-economics* side (see review 05).

What is still absent in wildfire: any paper that evaluates a forecast-aware
**protective-action / evacuation-timing** policy against a **tuned positional
trigger or buffer** and reports the skill boundary.

---

## 3. Comparison table

| Paper | Hazard | Decision modelled | Comparator used | Comparator tuned? | Skill boundary reported? | Latency treated? |
|---|---|---|---|---|---|---|
| `murphy1977costloss` | generic | protect / don't protect | climatology, categorical, perfect | n/a (analytic) | yes — value region in C/L | no |
| `murphy1987accuracyvalue` | generic | protect / don't protect | n/a | n/a | accuracy-value relation | no |
| `chen1987qualityvalue` | generic | N-action protection | n/a | n/a | quality-value relation | no |
| `richardson2000relative` | weather (generic) | binary protective action | climatology; control fcst | threshold optimised per C/L | yes (REV>0 region, by lead time) | no (lead time only) |
| `zhu2002economic` | weather (generic) | binary protective action | higher-res control forecast | threshold optimised per C/L | yes | no |
| `regnier2006dynamic` | hurricane | prepare now vs wait | static cost-loss framing | no | partial | lead time, not latency |
| `regnier2008public` | hurricane | order evacuation now vs wait | none (frontier characterised) | n/a | **yes** (miss-prob vs false-alarm frontier) | lead time |
| `verkade2011estimating` | flood | issue flood warning | no-warning / perfect | no | yes (REV by lead time) | lead time |
| `bischiniotis2019tradeoffs` | flood | trigger early action, when | no-action; 1-stage vs 2-stage | **yes** (optimal lead time solved) | yes | **lead time as decision variable** |
| `lopez2020bridging` | flood | trigger humanitarian action | climatology / act-always | **yes** (threshold selected by value) | yes (3-axis trigger region) | lead time |
| `bouttier2024optimal` | precipitation | issue categorical warning | deterministic control | **yes** (p_opt by ETS/F2) | **yes** (usable intensity/scale limit) | forecast range 9-36 h |
| `georgakakos2025evacuationtiming` | generic life-threat | issue evacuation statement now vs delay | none | no | partial | lead time + completion interval |
| `stephenson2025extremeloss` | generic | warn / don't warn | no-action | analytic optimum | yes (VaR vs expected-loss optima differ) | no |
| `olivetti2026compounding` | multi-hazard urban | protect / don't protect | competing forecast systems | varying C/L | yes (rank flips by C/L) | no |
| `ardid2026forecastvalue` | **wildfire** | fire-potential warning / preparedness | Fire Behaviour Index | **not stated** | no explicit boundary | no (sub-hourly cadence only) |
| `berlinghieri2024pm25` | **wildfire smoke** | go outside? when to go outside? | **persistence** | baseline is strong, not tuned | partial (task-dependent) | no |
| `raeth2026decisionskill` | weather (generic) | frost/heat protection, wind dispatch | competing forecast models | thresholds varied | partial | no |
| `masiwal2026decisionoriented` | monsoon | when to disseminate onset forecast | climatology | no | yes (skill horizon ~3 weeks) | operational runnability, not quantified |

---

## 4. What is generic prior art vs what remains open for wildfire

### 4.1 Concepts we may **NOT** claim (generic prior art)

1. **Forecast value as a decision-analytic quantity.** Murphy 1977. Closed.
2. **Relative / potential economic value curves over cost-loss ratio.**
   Richardson 2000, Zhu 2002. Closed.
3. **Accuracy (or quality) is not monotone with value/decision quality.**
   Murphy & Ehrendorfer 1987; Chen, Ehrendorfer & Murphy 1987; restated by
   `mandi2024dfl`, `liu2026dflfail`, `raeth2026decisionskill`. **Closed.**
4. **Act now vs wait for a better forecast, with forecast quality indexed by
   lead time.** Regnier & Harr 2006. Closed.
5. **A boundary in forecast-quality space separating "act on the forecast" from
   "don't".** Regnier 2008 (miss-prob vs false-alarm frontier); Bouttier &
   Marchal 2024 (usability limit); Richardson 2000 (REV>0 region). **Closed —
   including for evacuation ordering.**
6. **Lead time as an optimisation variable jointly with skill and action
   duration.** Bischiniotis et al. 2019; Lopez et al. 2020. **Closed.**
7. **Tuning the decision threshold before reporting value.** Standard since
   Richardson 2000; explicit in Bouttier & Marchal 2024. Closed.
8. **Evaluating forecasts against a decision task rather than a skill score.**
   Raeth & Ludwig 2026; Berlinghieri et al.; Masiwal et al. 2026. Closed.
9. **Applying the cost-loss/PEV pipeline to wildfire.** Ardid et al. 2026.
   **Closed as of 2026.**
10. **Using a strong non-forecast baseline (persistence/climatology) in a
    wildfire decision evaluation.** Berlinghieri et al. Closed.

### 4.2 What genuinely remains open for wildfire

These are narrow. That is the correct size for a surviving claim.

- **O1 — The tuned-positional-trigger comparator.** Every forecast-value paper
  above compares against climatology, no-action, persistence, or a competing
  forecast system. *None* compares against a **spatial trigger boundary or
  buffer whose distance/lead-time parameter has been optimised over the same
  scenario distribution.* That comparator class exists only in wildfire (Cova,
  Dennison, PERIL/k-PERIL — review 01/03) and has never been used as the
  benchmark in a forecast-value study. This is the load-bearing survivor.
- **O2 — Skill boundary against that comparator.** Consequently, no boundary in
  (skill x lead time x latency) space has been reported *relative to a tuned
  positional trigger* in any hazard.
- **O3 — Forecast *latency* proper.** The literature optimises **lead time**
  (how far ahead the forecast looks). It does not treat **latency** (the delay
  between observation and forecast availability) as an independent axis that
  shortens the usable decision window at fixed skill. The satellite-wildfire
  literature quantifies latency operationally (VIIRS ultra-real-time ~50 s;
  end-to-end alarm latency <17 min in one Swedish validation — see search log)
  but does **not** feed it into a decision-value calculation. This is a real gap.
- **O4 — Mission-feasibility as the payoff.** All payoffs above are scalar
  costs. None is a *feasibility indicator* on a routed round trip with
  hazard-arrival constraints per leg. A discontinuous mission-closes/doesn't-close
  payoff has different value geometry from a cost-loss payoff.
- **O5 — The spatial mechanism of accuracy-value decoupling.** Nobody has shown
  *why* a spatial overlap metric (IoU/Jaccard on burned area) decouples from
  evacuation decision quality — i.e. that error **location relative to the access
  route** matters and equal-area error elsewhere does not.

---

## 5. Verdicts

### WG-C-002 — "forecast-quality boundary (skill x lead time x latency) at which forecast-aware wildfire protective action outperforms a tuned trigger/buffer policy"

**Verdict: `WEAKENED`.** Not occupied, but badly exposed.

Reasoning. The *concept* of a forecast-quality boundary for protective action is
fully occupied (Regnier 2008 for evacuation ordering; Bouttier & Marchal 2024 for
warning thresholds; Richardson 2000 for REV regions). The *wildfire application*
of forecast-value theory is occupied as of Ardid et al. 2026. What is not
occupied is the conjunction of (a) evacuation/protective-action timing as the
decision, (b) **a tuned positional-trigger comparator**, and (c) a boundary
reported jointly over skill, lead time and latency, in wildfire.

Per `NOVELTY_STANDARD` §3.1, a conjunction is not a novelty argument by itself.
The claim survives only if we can state **why the tuned-trigger comparator
changes the answer** — i.e. show that a tuned buffer is a materially harder
baseline than climatology/persistence, and that the boundary moves when you swap
comparators. If it does not move, WG-C-002 is a negative result and should be
reported as one (CURRENT_THESIS "what would falsify" item 3).

**Required claim rewrite (proposed):** drop "we identify the forecast-quality
boundary" (occupied) in favour of "we report how the forecast-quality boundary
for wildfire protective action *moves* when the comparator is strengthened from
a fixed buffer to a buffer tuned on the same scenario distribution."

**Threat papers:** `regnier2008public`, `ardid2026forecastvalue`,
`bouttier2024optimal`, `lopez2020bridging`, `georgakakos2025evacuationtiming`.

### WG-C-006 — "tuned trigger/buffer comparator as evaluation standard"

**Verdict: `WEAKENED` (as a novelty claim); retain as methodological hygiene.**

Comparator tuning is standard practice in the forecast-value literature
(Richardson 2000, Bouttier & Marchal 2024) and decision-level evaluation against
strong baselines already exists in the wildfire domain (`berlinghieri2024pm25`
uses persistence; `ardid2026forecastvalue` uses FBI). The *specific* comparator —
a positional trigger boundary with an optimised parameter — is not used anywhere
as a forecast-value benchmark, and that is the only part worth stating. It is
N3-weak and must never be presented as a contribution on its own; its function is
defensive, exactly as the registry says.

### WG-C-012 — "forecast latency, not only skill, as a first-class decision variable"

**Verdict: `WEAKENED`, and the claim text must be repaired or it is `OCCUPIED`.**

As currently written, "timing of the forecast as a decision variable" is
occupied by `bischiniotis2019tradeoffs` (optimal trigger lead time as a function
of forecast quality *and action duration*) and `lopez2020bridging` (lead time as
one of three trigger axes), with `regnier2006dynamic` as the ancestor. Those
papers already own "a skilful forecast that arrives too late has no value."

What they do **not** own is latency in the strict sense: *observation-to-product
delay at fixed lead time and fixed skill*. That quantity is measured in the
wildfire remote-sensing literature but never converted into decision value. If
WG-C-012 is restated as

> "we treat observation-to-product latency as an axis distinct from lead time and
> skill, and show it shifts the wildfire dispatch-by deadline independently of
> skill"

then it is `UNKNOWN` leaning defensible. If it is left as "timeliness matters",
it is `OCCUPIED`. **Recommend rewriting the claim text in the registry.**

### WG-C-014 — "spatial fire-prediction accuracy (IoU) is not monotonically related to evacuation decision quality"

**Verdict: `WEAKENED`, close to `OCCUPIED` in general form.** See review 05 §4
for the decision-focused-learning side. The general proposition is owned by
Murphy & Ehrendorfer (1987) and restated in 2024-2026 by Mandi et al., Liu, and
Raeth & Ludwig. The wildfire-spatial-metric version is not yet published, and
`xu2026wildfirefm` — the closest wildfire-metric paper — only shows metric-to-metric
instability, not metric-to-decision decoupling. Claimable **only** with the
mechanism stated (error location relative to egress/ingress routes), never as
the bare slogan.

---

## 6. Papers needing full text

`murphy1987accuracyvalue` (E1 — bibliographic only), `chen1987qualityvalue` (E1),
`regnier2006dynamic` (E2), `regnier2008public` (E2),
`bischiniotis2019tradeoffs` (E2, publisher 403), `georgakakos2025evacuationtiming`
(E2, paywalled), `ardid2026forecastvalue` (E2), `lopez2020bridging` (E2),
`veiga2023activesensing` (E1). Logged in the search log; should be mirrored to
`novelty/OPEN_QUESTIONS.md` by the synthesis agent.
