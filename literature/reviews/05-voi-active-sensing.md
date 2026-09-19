# 05 — Value of Information and Active Sensing (Category 5)

**Agent:** A/B — Search Researcher + Prior-Art Adversary
**Date:** 2026-09-19
**Scope:** value of information (VOI) in environmental/disaster decisions,
Bayesian experimental design, optimal sensor placement, decision-directed
sensing, observation targeting / adaptive observation in meteorology,
informative path planning, sensor tasking under deadlines, expected value of
sample information, decision-focused learning (predict-then-optimize / SPO).
**Claims under attack:** WG-C-008 primarily; WG-C-014 via §4.
**Search log:** `docs/search-logs/agent-forecast-voi.md`.

---

## 1. The canonical frameworks and who owns them

### 1.1 Value of information / pre-posterior analysis
Classical decision analysis (EVPI / EVSI). In the environmental and
infrastructure setting the operative modern references are
`malings2016voisensor` (Reliab. Eng. Syst. Saf. 154:219-233) and
`malings2018voispatiotemporal` (ibid. 172:45-57). The 2016 paper's headline
finding is the one that matters here: **sensor placements depend on the
decision-making problem to be addressed, as encoded in a problem-specific loss
function.** The 2018 companion adds *when* to sense (scheduling) over a
management horizon. A third companion (Malings & Pozzi, 2019, submodularity —
DOI `UNVERIFIED`, search lead only) shows VOI is **not submodular**, so greedy
sensor selection carries no near-optimality guarantee: a practical warning for
any WildfireGuardian implementation.

### 1.2 Bayesian experimental design — **Rainforth's group owns the modern form**
`rainforth2024modernbed` (Statistical Science 39(1)) is the canonical review of
expected-information-gain design. `rossa2026actionbed` (arXiv 2026) then moves
BED off information gain entirely: design is reformulated as minimising the
**expected future loss on downstream actions**, i.e. task-driven /
decision-directed design as a general method. Related 2024-2026 work in the same
direction (author lists **not verified** — search leads only): "Amortized
Bayesian Experimental Design for Decision-Making" (NeurIPS 2024 /
arXiv:2411.02064) with its Decision Utility Gain; and "Goal-driven Bayesian
Optimal Experimental Design..." (arXiv:2605.26093), whose stated finding is that
reducing parameter uncertainty does not necessarily improve downstream decisions.

### 1.3 Adaptive / targeted observation in meteorology — **Palmer et al. own it**
`palmer1998singular` (JAS 55(4):633-653) established targeting observations by
sensitivity, and — importantly for us — that **the correct metric depends on the
purpose of the observations**. The ETKF/CNOP targeting lineage follows.

### 1.4 Active sensing in decision-theoretic planning
`veiga2023activesensing` (ACM Comput. Surv. 55(13s):1-22) surveys the whole
field: information gathering embedded in POMDP planning, myopic vs non-myopic,
reward functions capturing uncertainty reduction. This is a settled field with
its own taxonomy.

### 1.5 Wildfire-specific information economics
- `simon2022wildfirevoi` (Front. Environ. Sci. 10:804958) — a **conceptual** VOI
  framework for wildfire management effort (fuel treatment / suppression /
  rehabilitation). Verified by full-text read: it does **not** address sensor
  selection, observation timing, or decision-directed sensing.
- `hope2024wildfiresat` (PLOS ONE 19(5):e0302699) — cost-benefit analysis of a
  whole wildfire monitoring satellite mission.
- `frisvold2024demandinfo` (Atmosphere 15(11):1364) — empirical demand-side study
  of who uses fire information and when.
- `shao2026beliefaware` (arXiv 2026, PREPRINT) — **wildfire active sensing**:
  non-myopic scheduling of sensing/representation/transmission under a
  sparse-window downlink, evaluated in a physics-calibrated synthetic
  environment. Objective is **predictive** loss on an H-step hazard map.

---

## 2. The paper that does the most damage

`sun2025decisionfocusedsensing` — Sun, Hults & Xu, ACM BuildSys '25, DOI
10.1145/3736425.3770102 — is a peer-reviewed conference paper that:

- criticises exactly the practice WG-C-008 criticises ("fixed, decision
  task-agnostic strategies to decide where to put in-situ sensors (e.g. maximize
  overall information gain) and train flood forecasting models (e.g. minimize
  average forecasting errors)");
- states WG-C-014's proposition as its motivation ("systems with the same
  sensing gain and average forecasting errors may lead to distinct decisions");
- builds an end-to-end differentiable pipeline that selects sensors **and**
  trains the forecaster to minimise **downstream evacuation/relocation decision
  regret**;
- validates on real flood scenarios.

In other words: decision-directed sensing for hazard evacuation already exists,
peer-reviewed, one hazard over.

---

## 3. Comparison table

| Paper | Domain | Sensing decision | Objective driving sensing | Deadline / time-criticality | Decision modelled | Threat |
|---|---|---|---|---|---|---|
| `palmer1998singular` | synoptic met. | where to observe | forecast-error sensitivity (metric = purpose-dependent) | no | none (forecast quality) | HIGH (field ownership) |
| `malings2016voisensor` | infrastructure | where to place sensors | **problem-specific decision loss (VOI)** | no | maintenance/intervention | **CRITICAL** |
| `malings2018voispatiotemporal` | infrastructure | where + when to sense | VOI over management horizon | ageing horizon, not a deadline | lifecycle management | HIGH |
| `veiga2023activesensing` | planning (generic) | information-gathering actions | POMDP reward incl. uncertainty reduction | task-dependent | generic | HIGH (field ownership) |
| `rainforth2024modernbed` | statistics | experiment design | expected information gain | no | none | HIGH (field ownership) |
| `rossa2026actionbed` | statistics | experiment design | **expected future loss of downstream actions** | no | generic downstream task | **CRITICAL** |
| `sun2025decisionfocusedsensing` | flood | sensor placement + forecaster training | **evacuation/relocation decision regret** | "rapid response", no hard deadline | evacuation / relocation | **CRITICAL** |
| `shao2026beliefaware` | **wildfire** | sensing/representation/transmission scheduling | **predictive** loss on hazard map | bandwidth windows, not a decision deadline | none | HIGH (application) |
| `simon2022wildfirevoi` | **wildfire** | none (conceptual) | management cost minimisation | no | fuel/suppression/rehab effort | MODERATE |
| `hope2024wildfiresat` | **wildfire** | mission-level (build satellite?) | programme cost-benefit | no | agency investment | MODERATE |
| `frisvold2024demandinfo` | **wildfire** | none | descriptive demand | no | none | LOW |
| `mandi2024dfl` | OR/ML | (data collection discussed) | decision regret | no | LP/MILP downstream | CRITICAL (for WG-C-014) |
| `liu2026dflfail` | OR/ML | **critiques uncertainty-driven data collection** | decision regret | no | stochastic LP | HIGH |

---

## 4. Decision-focused learning and what it does to WG-C-014

Decision-focused learning (DFL) is the ML/OR restatement of Murphy &
Ehrendorfer (1987), and it is a danger zone exactly as the task brief warned.

- `mandi2024dfl` (JAIR 80:1623-1701) is the reference survey, with an 11-method /
  7-problem benchmark. Its premise is that training to predictive accuracy is not
  training to decision quality.
- `liu2026dflfail` (arXiv 2026) states it baldly: "improved predictive accuracy
  does not, in general, translate into improved decision quality" — and,
  separately, that **data-collection strategies driven purely by predictive
  uncertainty are not suited to decision-focused settings**. That one sentence
  pre-empts the *motivation* for both WG-C-014 and WG-C-008.
- `raeth2025decisionskill` (arXiv 2026) supplies the weather-domain empirical
  demonstration, including that model rankings change between *similar* decision
  tasks (review 04 §1.1).
- Portfolio-domain instances (`arXiv:2601.04062`, `arXiv:2605.01176` — author
  lists not verified, search leads) make the same point in finance.

**Implication for WG-C-014.** The general claim is dead. Three things survive,
and only if demonstrated rather than asserted:

1. **The metric is spatial, not scalar.** DFL works with scalar or vector
   parameter predictions feeding an optimisation. Nobody in this literature
   studies a *spatial overlap* metric (IoU / Jaccard / Dice on a burned-area
   mask). `xu2026wildfirefm` is the nearest wildfire work and it only shows
   metric-to-metric instability under different evaluation contracts, not
   metric-to-decision decoupling.
2. **The mechanism is geometric.** The interesting, publishable statement is not
   "IoU is not decision quality" but "an IoU-equal perturbation of the predicted
   perimeter changes the dispatch-by deadline by X minutes when it lies across
   the ingress route and by ~0 minutes elsewhere." That is a measurable,
   falsifiable, wildfire-specific statement.
3. **The payoff is a feasibility discontinuity**, not a smooth cost. DFL's
   failure modes are LP-geometric; a mission-closes/doesn't-close payoff has a
   different structure.

Anything short of (1)+(2)+(3) is a restatement of 1987.

---

## 5. What is generic prior art vs what remains open for wildfire

### 5.1 Concepts we may **NOT** claim

1. **Value of information as a criterion for choosing observations.** Classical;
   Malings & Pozzi 2016/2018 in the spatial-systems form. Closed.
2. **"What to observe should depend on the downstream decision, not on generic
   uncertainty reduction."** Malings & Pozzi 2016 (explicit); Palmer et al. 1998
   (metric depends on purpose); Rossa, Phillips & Rainforth 2026 (as a general
   BED method). **Closed. WG-C-008 cannot be N3.**
3. **Decision-directed sensing for hazard evacuation.** Sun, Hults & Xu 2025, in
   floods, peer-reviewed. **Closed as a general application claim.**
4. **Joint sensing + forecasting optimised end-to-end on decision regret.**
   Sun et al. 2025. Closed.
5. **Active sensing / informative path planning for wildfire monitoring.**
   Shao et al. 2026 (scheduling under telemetry constraints); plus the UAV
   informative-path-planning literature (PyroTrack, Julian & Kochenderfer-type
   distributed surveillance, fleet monitoring — see search log). Closed.
6. **Value-of-information analysis in wildfire management.** Simon, Crowley &
   Franco 2022 (conceptual); Hope et al. 2024 (mission cost-benefit). Closed.
7. **Non-submodularity caveats for greedy VOI sensor selection.** Malings &
   Pozzi 2019. Closed (and must be respected, not rediscovered).

### 5.2 What genuinely remains open for wildfire

- **O6 — Deadline-conditioned observation value.** No paper found treats the
  value of an observation as *collapsing to zero once a decision deadline has
  passed*. Malings & Pozzi schedule over a management horizon; Sun et al. respond
  "rapidly" but with no hard deadline; Shao et al. schedule against bandwidth
  windows, not decision deadlines. **An observation's value gated by the
  dispatch-by time is the sharpest open corner of WG-C-008.**
- **O7 — Decision-directed sensing with a *wildfire* hazard and a *mission
  feasibility* objective.** Shao et al. have wildfire + sensing but a predictive
  objective. Sun et al. have decision-focused sensing but floods and a cost
  objective. The intersection is empty — but it is an intersection, and
  `NOVELTY_STANDARD` §3.1 forbids claiming conjunctions without saying why the
  conjunction changes the answer. The answer it must change: *which* observation
  is worth taking should flip between the predictive-loss ranking and the
  deadline-value ranking. If it does not flip, there is no claim.
- **O8 — VOI under a propagating front.** The VOI literature's spatial models are
  Gaussian random fields over static domains. A fire-arrival-time field is
  strongly anisotropic and advancing; whether standard VOI approximations remain
  usable is unexamined.

---

## 6. Verdict on WG-C-008

> Claim: "We select wildfire observations by their effect on the evacuation
> decision (decision-directed / deadline-aware sensing) rather than by
> predictive accuracy."

**Verdict: `WEAKENED`. The registry's open question is answered: this is
application novelty (N4), not methodological novelty (N3) — and even the
application novelty is partial.**

Breakdown:

| Component of the claim | Status | Killing paper |
|---|---|---|
| Decision-directed sensing as a *method* | `OCCUPIED` | `malings2016voisensor`, `rossa2026actionbed` |
| "rather than by predictive accuracy" as a *motivation* | `OCCUPIED` | `liu2026dflfail`, `mandi2024dfl` |
| Decision-directed sensing for *hazard evacuation* | `OCCUPIED` | `sun2025decisionfocusedsensing` |
| Active/adaptive sensing in *wildfire* | `OCCUPIED` | `shao2026beliefaware` |
| VOI in *wildfire management* | `OCCUPIED` | `simon2022wildfirevoi`, `hope2024wildfiresat` |
| **Deadline-aware** observation value (value -> 0 after the dispatch deadline) | `UNKNOWN` — no prior art found | — |
| Decision-directed wildfire sensing with a *mission-feasibility* objective | `UNKNOWN` | — |

Per `NOVELTY_STANDARD` §2, an N4 claim is filed `WEAKENED` by default. WG-C-008
is admissible only bundled with WG-C-003's quantity (the inbound-inclusive
dispatch deadline), because the deadline is the only thing that makes the sensing
problem different from Sun et al.'s. Standing alone it is not a contribution.

**Recommended claim rewrite:** "We rank candidate wildfire observations by how
much they move the responder dispatch-by deadline, and show this ranking differs
from both information-gain and predictive-accuracy rankings."

**Note for the search protocol:** the two `UNKNOWN` rows above rest on a null
search and therefore carry no credit (`NOVELTY_STANDARD` §3.2). They must be
re-run against the sensor-scheduling / POMDP-with-deadline and
early-classification literatures, which this pass touched only shallowly
(see search log, unresolved items U2 and U3).

---

## 7. Papers needing full text

`malings2016voisensor` (E2), `malings2018voispatiotemporal` (E2),
`veiga2023activesensing` (E1, ACM 403), `rainforth2024modernbed` (E2),
`rossa2026actionbed` (E2, abstract only), `sun2025decisionfocusedsensing`
(E3 but experimental datasets unread), `hope2024wildfiresat` (E1/E2),
Malings & Pozzi 2019 submodularity paper (DOI `UNVERIFIED`).
