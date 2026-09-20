# RQ1_DECOMPOSITION.md — Component-Level Scoring of the Forecast-Value Question

**Agent:** C + B (Verification / Citation Auditor + Prior-Art Adversary)
**Date:** 2026-09-20
**Governing standards:** `docs/NOVELTY_STANDARD.md`, `docs/SEARCH_PROTOCOL.md`,
`docs/EVIDENCE_LEVELS.md`
**Companion deliverables:** `literature/reviews/fulltext-ardid2026.md`,
`docs/search-logs/agent-rq1-decomposition.md`
**Corpus searched:** 165 records in `literature/metadata/` as of 2026-09-20,
plus the targeted external queries logged in the search log.

---

## 0. Scope, and what is deliberately excluded

RQ1 as written in `docs/CURRENT_THESIS.md` is a conjunction. Under
`NOVELTY_STANDARD.md` §3.1 a conjunction is **not** a novelty argument. This
file therefore refuses to score "RQ1" as a unit and scores seven separable
components plus one cross-cutting combination claim.

**Treated as OCCUPIED background and not re-litigated anywhere below:**

> *Forecast accuracy is not the same as decision quality.*
> `murphy1987accuracyvalue` (Murphy & Ehrendorfer 1987, WAF 2(3):243-251) and
> `chen1987qualityvalue` (Chen, Ehrendorfer & Murphy 1987, MWR 115(8):1534-1541).
> Thirty-nine years old. Restated in 2024-2026 by `mandi2024dfl`, `liu2026dflfail`,
> `raeth2025decisionskill`, `elmachtoub2022smartpredict`. **Concede it
> immediately and in full.** Any WildfireGuardian sentence that sounds like this
> proposition is a restatement, not a finding.

**Scoring vocabulary used here**

| Score | Meaning | Burden met |
|---|---|---|
| `OCCUPIED` | A named prior work does this thing | One verified work, E3 minimum (EVIDENCE_LEVELS rule 1) |
| `WEAKENED` | Prior work covers a strict subset, an adjacent domain, or the same move with a different outcome variable | Named work + the narrowed statement of what is left |
| `PLAUSIBLE` | No occupant found **and** the search behind that null reached SEARCH_PROTOCOL tier S2 | Documented protocol search; still only `SUPPORTED_CANDIDATE`-grade, never certainty |
| `UNKNOWN` | Default. No occupant found but the search was S0/S1, or a named blind spot remains | Nothing |

**The asymmetry is the point.** One paper can occupy a component. No number of
null searches can vacate one.

---

## 1. Summary table

| ID | Component | Score | Occupying / nearest work |
|---|---|---|---|
| WG-FV-1 | Controlled forecast-error dimensions varied | `WEAKENED` | `jewson2026evacuation`; `sezer2026infodesign` |
| WG-FV-2 | Forecast latency varied as an experimental factor | `WEAKENED` | `zha2024distributed`; `chang2026multiscale` |
| WG-FV-3 | Comparison against a strong **tuned trigger/buffer** policy | `PLAUSIBLE` | none; nearest `ardid2026forecastvalue` (tuned *index threshold*) |
| WG-FV-4 | Break-even set/frontier in **error x latency** space | `UNKNOWN` | 1-D forms occupied (`jewson2026evacuation`, `richardson2000relative`, `bouttier2024optimal`); joint form has no identified occupant |
| WG-FV-5 | **Decision loss** rather than forecast score defines the frontier | `OCCUPIED` | `richardson2000relative`; `murphy1977costloss`; `bouttier2024optimal`; `jewson2026evacuation` |
| WG-FV-6 | Independent hidden truth / OSSE evaluation | `OCCUPIED` | `arnold1986osse`; `zeng2020osse`; in wildfire `wu2025denkf`, `zha2024distributed` |
| WG-FV-7 | Evaluated on Korean landscapes / anchored Korean conditions | `UNKNOWN` | none found, but KCI/RISS/DBpia sweep is **not done** |
| WG-COMB-1 | Information availability vs assisted-evacuation option expiry, evaluated directly | `UNKNOWN` | no occupant identified; nearest `jewson2026evacuation`, `georgakakos2025evacuationtiming`, `moradi2026supported` |

**Three of eight are occupied or weakened by named papers. One is plausible.
Four are unknown, and "unknown" is not a synonym for "ours".**

---

## WG-FV-1 — Controlled wildfire forecast-error dimensions are varied

*Error injected along named axes, not merely evaluated as-is.*

**Score: `WEAKENED`**

**Occupying work (adjacent hazards):**

- `jewson2026evacuation` — Jewson, S. (2026), *Frontiers in Communication*
  11:1762033, DOI 10.3389/fcomm.2026.1762033. Varies a **named**
  forecast-uncertainty dimension — the standard deviation of the change in
  forecast probability between successive issuances — and reports where the
  recommended action flips. Abstract (E4, two independent sources): "We give an
  example in which low standard deviations imply evacuation as the best option,
  while higher standard deviations imply waiting for the next forecast as the
  best option." Tropical cyclone; idealized; no landscape.
- `sezer2026infodesign` — Sezer, F. (2026), arXiv:2606.30320, **PREPRINT**.
  Experiment 2 sweeps public-signal precision and plots expected social cost
  against it, finding a **sign reversal**: "Under a single common signal (K = 1)
  cost rises with precision and the optimum is the vague corner" (Fig. 6
  caption, E3). The swept quantity is a designed signal's precision, not
  forecast error.

**Evidence that it is not occupied in wildfire:**

- `ardid2026forecastvalue` — read at **E3** on 2026-09-20. Forecasts are
  evaluated as-is: "all FBI values in this study were recalculated directly from
  observed AWS data", evaluation "on the full, naturally imbalanced held-out
  records without any re-balancing at evaluation". The words `perturb` and
  `synthetic` are **ABSENT** from the body. See
  `literature/reviews/fulltext-ardid2026.md` §1.5.
- `allaire2020ensemble` propagates *input* uncertainty through hundreds of Monte
  Carlo wildfire simulations and scores the resulting burn-probability maps with
  proper scores. That is forecast-side scoring of propagated uncertainty, not
  injection of error along named axes to test a decision.
- `berlinghieri2024pm25` evaluates six operational smoke forecasts as-is on two
  decision tasks against persistence. No error manipulation.
- Corpus-wide grep for `perturb` / `sensitivity analys` / `injected` /
  `degrad` across all 71 notes returned only: DA machinery (`wu2025denkf`,
  `zha2024distributed`), OSSE twin-design methodology (`yu2019twin`,
  `sargent2013verification`), and `hurlbert1984pseudoreplication`'s warning
  about wind perturbations as pseudoreplication. **No wildfire paper injects
  forecast error along named axes and measures a protective-action outcome.**

**What survives, stated narrowly.** Not "we vary forecast error" — that move is
published in two hazards in 2026. What is unoccupied is varying error in a
**spatial fire arrival-time field along axes that have a geometric relationship
to the access route** (review 04 §4.2, O5). If the axes turn out to be scalar
skill parameters, this component collapses into Jewson.

- **Search coverage:** existing Category 4 log (S2: 37 queries, 5+ sources,
  Korean pass, preprint sweep) plus 3 targeted queries today + 2 alphaXiv
  discovery rounds. Tier for this component: **S2**.
- **Full-text coverage:** `ardid2026forecastvalue` E3; `jewson2026evacuation`
  abstract E4 / body E3; `sezer2026infodesign` E3; `allaire2020ensemble` E2.
- **Unsearched databases:** Scopus, Web of Science, Engineering Village, KCI,
  RISS, DBpia. **Consensus quota exhausted (30/30, resets 1 October)** — no
  peer-reviewed-corpus query could be run today.
- **Language limitations:** one Korean-language web query today (null); no
  Chinese, Japanese, Spanish, Portuguese or Greek pass.
- **Publication-date cutoff:** 2026-09-20.
- **Confidence:** Moderate-high that no wildfire occupant exists; high that the
  generic move is occupied.

---

## WG-FV-2 — Forecast latency is varied as an experimental factor

**Score: `WEAKENED`**

**Occupying work — and it is inside wildfire, which is the uncomfortable part:**

- `zha2024distributed` — Zha, Wang, Ji & Zhu (2024), *Int. J. Wildland Fire*
  33(7), DOI 10.1071/wf23165. The repository's own one-line difference:
  "Runs OSSEs to generate asynchronous fire-front observations, **treats
  observation staleness (latency) as the central problem**, and concludes that
  observation resources should be concentrated where spread rates are highest."
  Latency is the experimental variable. The **outcome is prediction error**, not
  a protective-action consequence. `forecast_latency: yes`, `osse: yes`,
  `decision_value: no`.
- `chang2026multiscale` — Chang, Comfort, Soga, Li & Wang (2026), *Risk
  Analysis*, DOI 10.1111/risa.70338. Cognition/communication delay distributions
  are a first-class modelled variable and "cognitive delays produc[e] nonlinear
  congestion" (Abstract, E2); the outcome is **who escapes**. That is a
  decision-relevant outcome. The delay is **alert** latency (order → household),
  not observation-to-product latency.

**Adjacent-field occupation of the same move.** NWP data-cut-off / observing-
system experiments routinely vary data latency as a factor — e.g. a study of
low-latency satellite sounder observations for local severe storms in regional
NWP, which compares "different data cut-off windows to evaluate the impact of
data latency" (surfaced by web search 2026-09-20, **not retrieved, metadata
UNVERIFIED — search lead only**, logged in the search log). Outcome there is a
forecast quality score, not decision loss.

**Evidence of non-occupation in the strict sense:**

- `ardid2026forecastvalue` (E3): `latency`, `delay`, `timeliness` and even
  `lead time` are **ABSENT** from the body. Its temporal argument is about the
  public *release cadence* of the FBI ("only a single daily rating is released
  publicly"), never converted to value, never varied.
- `sung2025geostationary` measures Korean wildfire observation latency
  operationally and "never converts latency into decision value".
- `nasafirms2026latency`, `roysingh2025constellation`, `paugam2026mtgfci`,
  `hall2023geostationary` quantify or budget latency; none feeds it into a
  decision-value calculation.
- `bischiniotis2019tradeoffs` and `lopez2020bridging` optimise **lead time**,
  which review 04 §5 already conceded is a different quantity and is occupied.

**What survives, stated narrowly.** Not "latency matters" (occupied, twice in
wildfire). What is unoccupied is **observation-to-product latency varied at
fixed skill and fixed lead time, scored by decision loss** — i.e. the
conjunction of `zha2024distributed`'s independent variable with
`chang2026multiscale`'s outcome variable. Per §3.1 that conjunction is not by
itself a novelty argument; the project must say why joint treatment changes the
answer.

- **Search coverage:** existing Category 4 + 7 logs, plus 3 targeted queries
  today. Tier: **S1→S2** for this component (no citation chase on
  `zha2024distributed` or `chang2026multiscale`).
- **Full-text coverage:** `zha2024distributed` E2 (abstract via Consensus;
  **full text never read** — this is a gap, because the claim that its outcome
  is purely prediction error rests on the abstract); `chang2026multiscale` E2;
  `ardid2026forecastvalue` E3.
- **Unsearched databases:** Scopus, WoS, IEEE Xplore, KCI/RISS/DBpia; Consensus
  unavailable (quota).
- **Language limitations:** no Chinese-language pass, which matters — both
  `zha2024distributed` and `wu2025denkf` come from Chinese fire-safety groups
  whose adjacent work may be in Chinese.
- **Publication-date cutoff:** 2026-09-20.
- **Confidence:** Moderate. **Lowered** by the fact that the two closest papers
  are known only at E2. `zha2024distributed` must be read in full before this
  score is trusted — if its OSSE scores anything downstream of prediction error,
  this component moves to `OCCUPIED`.

---

## WG-FV-3 — Forecast-aware protective action compared against a strong **tuned** trigger/buffer policy

**Score: `PLAUSIBLE`**

*The only component scored above `UNKNOWN` on a null, and it is scored that way
only because Category 4 reached tier S2 with a committed query log
(`docs/SEARCH_PROTOCOL.md` §6). It supports `SUPPORTED_CANDIDATE` at most, never
certainty.*

**No occupying prior art was identified in the searched corpus.**

**Nearest works, and why each falls short:**

- `ardid2026forecastvalue` — **the baseline IS tuned**, which corrects the
  repository's prior E2 record. "The optimal classification threshold for each
  model is selected retrospectively to maximise PEV" (Methods, E3), with
  per-region optimal FBI thresholds. But the tuned object is a **scalar
  danger-index cut-off**, not a spatial trigger boundary or buffer distance, and
  there is no scenario distribution of fire progression over which a buffer
  parameter could be optimised. The surviving distinction is **"tuned index
  threshold vs tuned positional trigger"**, *not* "untuned vs tuned". Anyone
  defending the project on the old line will be publicly corrected.
- `berlinghieri2024pm25` uses **persistence** — a strong baseline, but not tuned
  and not positional.
- `richardson2000relative`, `zhu2002economic`, `bouttier2024optimal` tune the
  *decision threshold* of the forecast system itself. That is threshold tuning,
  not a rival policy family.
- The tuned-positional-trigger comparator class exists only in wildfire
  (`cova2005trigger`, `dennison2007wuivac`, `larsen2011cedar`,
  `kalogeropoulos2023kperil`, `mitchell2023peril`, `ramirez2019stochastic`) and
  has **never been used as the benchmark in a forecast-value study**.
  `mois2025evacuationstages` shows the Korean operational analogue: two
  administratively fixed lead times (5 h general, 8 h vulnerable) — a fixed,
  untuned trigger, which is exactly the weak baseline CURRENT_THESIS forbids
  beating.

**Standing caveat.** `docs/NOVELTY_STANDARD.md` §5 and review 04 §5 both hold:
this comparator is **N3-weak and defensive**, never a contribution on its own.
If swapping comparator from a fixed buffer to a tuned buffer does not move the
boundary, WG-C-002 is a negative result and must be reported as one
(CURRENT_THESIS "what would falsify" item 3).

- **Search coverage:** existing Category 4 log at **S2** (37 queries, 5 sources,
  Korean pass, preprint sweep, backward/forward chase on the forecast-value
  anchors), plus 2 targeted queries today explicitly hunting a tuned-buffer
  benchmark. Tier: **S2**.
- **Full-text coverage:** `ardid2026forecastvalue` E3; `berlinghieri2024pm25`
  E2; `bouttier2024optimal` E2; the trigger-lineage papers are Category 1's
  responsibility and are read at mixed E1-E3 there.
- **Unsearched databases:** Scopus, WoS, Engineering Village, TRID
  (transportation — relevant, since trigger/buffer work publishes there),
  KCI/RISS/DBpia. Consensus unavailable (quota).
- **Language limitations:** no Greek, Portuguese or Spanish pass, and
  `docs/SEARCH_PROTOCOL.md` already records that gap for Category 3, where the
  trigger/traffic literature lives.
- **Publication-date cutoff:** 2026-09-20.
- **Confidence:** Moderate. This is the load-bearing survivor of review 04
  (O1) and it has now survived a second, hostile pass. It has **not** survived a
  PRISMA-style S3 sweep, and TRID in particular is unsearched.

---

## WG-FV-4 — A break-even set/frontier in **error x latency** space is estimated

**Score: `UNKNOWN`**

**No occupying prior art was identified in the searched corpus** for the joint
two-axis form.

**But every one-dimensional version is occupied, and one two-dimensional
version in a different pair of axes is occupied:**

- `richardson2000relative`, `zhu2002economic` — the region of cost-loss ratio
  where REV > 0 is a break-even set in C/L, by lead time.
- `regnier2008public` — an achievable (miss-probability, false-alarm-rate)
  frontier per location for hurricane evacuation ordering.
- `bouttier2024optimal` — an explicit **two-dimensional** usability boundary in
  (intensity, spatial scale).
- `jewson2026evacuation` — a break-even in a forecast-uncertainty dimension: the
  standard deviation of probability change at which "evacuate" flips to "wait".
- `lopez2020bridging` — a three-axis trigger region (magnitude, probability
  threshold, lead time). Note: **lead time, not latency.**

**Why this is `UNKNOWN` and not `PLAUSIBLE`.** Two reasons, both binding.
(1) The searches specifically aimed at an error x latency frontier were run
today at tier **S1** only — 2 web queries and 2 alphaXiv rounds, with Consensus
unavailable. A null at S1 confers nothing (`SEARCH_PROTOCOL` §1).
(2) Even if the null held at S2, the component as written is a **conjunction**
of WG-FV-1 and WG-FV-2, and `NOVELTY_STANDARD` §3.1 forbids conjunction novelty
outright. To be claimable at all, the project must state *what conclusion joint
error-latency treatment produces that the two separate axes cannot* — for
example, a trade-off region in which extra skill cannot buy back lost latency.
Absent that sentence, this component is not a claim, it is a longer list.

- **Search coverage:** S1 today; the underlying Category 4 corpus is S2 but was
  not built around this two-axis question.
- **Full-text coverage:** `bouttier2024optimal` E2, `regnier2008public` E2,
  `richardson2000relative` E2, `jewson2026evacuation` E3. **None of the four
  frontier papers is read at E3+ except Jewson** — so statements about the
  *shape* of their frontiers are weakly evidenced.
- **Unsearched databases:** Scopus, WoS, Consensus (quota), KCI/RISS/DBpia.
- **Language limitations:** English-only for this component.
- **Publication-date cutoff:** 2026-09-20.
- **Confidence:** Low. This is the component most likely to be quietly occupied
  by something the search has not phrased correctly yet.

---

## WG-FV-5 — **Decision loss**, rather than a forecast score, defines the frontier

**Score: `OCCUPIED`**

**Occupying works:**

- `murphy1977costloss` — Murphy (1977), *MWR* 105(7):803-816. The expense
  expressions and the relative-value measure. The frontier is defined by
  expected expense, i.e. decision loss.
- `richardson2000relative` — Richardson (2000), *QJRMS* 126(563):649-667. The
  REV > 0 region over C/L is a **loss-defined** usability region, with the
  probability threshold optimised per C/L. This is the cleanest occupant.
- `zhu2002economic` — Zhu et al. (2002), *BAMS* 83(1):73-83. Same, operational.
- `bouttier2024optimal` — user-specific optimal decision thresholds and a
  usability boundary defined by user cost, not by a verification score.
- `jewson2026evacuation` — the evacuate/wait flip is located by comparing
  expected losses, not by any skill score.
- `sezer2026infodesign` — expected social cost is the y-axis of the
  precision sweep (PREPRINT).
- `sun2025decisionfocusedsensing` — sensors placed and the forecast model
  trained end-to-end to minimise downstream **decision regret**, "explicitly
  rejecting information-gain placement and average-error training" (flood).
- In wildfire specifically: `ardid2026forecastvalue` computes PEV — decision
  loss — for wildfire, in 2026. It just does not use it to draw a frontier.

**This component is closed.** `NOVELTY_STANDARD` §3 forbids restating it. The
only defensible WildfireGuardian sentence in this area is about the *shape* of
the loss — a discontinuous mission-closes/does-not-close payoff on a routed
round trip has different value geometry from a scalar cost-loss payoff (review
04 §4.2, O4) — and that belongs to RQ2, not RQ1.

- **Search coverage:** S2 (Category 4 log, 25 logged queries in section A alone).
- **Full-text coverage:** `murphy1977costloss` E1-E2, `richardson2000relative`
  E2, `jewson2026evacuation` E3/E4, `ardid2026forecastvalue` E3. **Note:** an
  `OCCUPIED` verdict requires E3 minimum per EVIDENCE_LEVELS rule 1. That bar is
  met by `jewson2026evacuation` and `ardid2026forecastvalue`; it is **not** met
  by Murphy 1977 or Richardson 2000, which remain at E2 and should be read.
- **Unsearched databases:** irrelevant to the verdict — the component is
  occupied and further search cannot vacate it.
- **Language limitations:** irrelevant for the same reason.
- **Publication-date cutoff:** n/a (occupancy established 1977).
- **Confidence:** Very high.

---

## WG-FV-6 — Experiment uses independent hidden truth / OSSE evaluation

**Score: `OCCUPIED`**

**Occupying works:**

- `arnold1986osse` — Arnold & Dey (1986), *BAMS* 67(6):687-695. The foundational
  OSSE methodology statement, including the identical-twin problem.
- `atlas1997observations` — Atlas (1997), *JMSJ* 75(1B):111-130. OSSE validation
  requirements.
- `halliwell2014fraternal` — Halliwell et al. (2014), *JTECH* 31(1):105-130.
  Fraternal-twin design criteria.
- `zeng2020osse` — Zeng et al. (2020), *BAMS* 101(8):E1427-E1438. Review of OSSE
  use in the US.
- **In wildfire:** `wu2025denkf` — "Uses Observing System Simulation Experiments
  **by name** to validate a deterministic EnKF for fire-front correction, so OSSE
  is already a normal, named method inside wildfire spread prediction."
  `zha2024distributed` likewise.
- **In evacuation decision-making:** `georgakakos2025evacuationtiming` —
  Monte Carlo simulation experiments carrying parametric uncertainty, recorded
  in the corpus as "effectively an **OSSE-style** design", with `osse: yes`.

**The one narrower thing that is not occupied,** and the project should say only
this: `zeng2020osse` itself lists "extension of OSSEs to **societal impacts**"
as an outstanding community recommendation as of 2020. A *decision-level* OSSE
in wildfire — hidden fire truth, scored by protective-action loss rather than
forecast accuracy — has no identified occupant. But that is a statement about
WG-FV-6 **combined with** WG-FV-5 and the wildfire domain, i.e. a conjunction
again (§3.1). Standalone, "we use an OSSE" is a 1986 method.

Also binding: `arnold1986osse`, `yu2019twin` and `kaipio2007inversecrime`
impose a *requirement*, not an opportunity — the truth model must not be the
forecast model, or the design is an identical twin / inverse crime and the
results are worthless.

- **Search coverage:** Category 10 log at **S2** (53 queries over 8 rounds), plus
  1 targeted query today. Tier: **S2**.
- **Full-text coverage:** `arnold1986osse` E1 (NEEDS_FULL_TEXT),
  `atlas1997observations` E1 (cited secondhand via Yu et al. 2019),
  `kaipio2007inversecrime` E2 (abstract elided by publisher), `zeng2020osse` E2,
  `wu2025denkf` E2, `georgakakos2025evacuationtiming` E2 (paywalled).
  **EVIDENCE_LEVELS rule 1 requires E3 to declare occupancy and not one of these
  is at E3.** The `OCCUPIED` verdict here rests on the uncontroversial fact that
  OSSE is a named, forty-year-old method; formally, the citation-level burden is
  **not** discharged and at least one of these must be read in full.
- **Unsearched databases:** Consensus (quota), Scopus, WoS, AMS journals direct.
- **Language limitations:** English-only.
- **Publication-date cutoff:** 2026-09-20.
- **Confidence:** Very high on the verdict; **low on the citation hygiene**.

---

## WG-FV-7 — Result evaluated on Korean landscapes or operationally anchored Korean conditions

**Score: `UNKNOWN`**

**No occupying prior art was identified in the searched corpus.** The corpus
holds 23 Korean-setting records (`an2008slope`, `an2026donghae`, `choi2025gee`,
`choi2026ridgeline`, `gu2016spreadalgorithm`, `han2026dangerrating`,
`heo2026vulnerability`, `kang2020hfri`, `kfs2025majorfires`, `kfs2026statistics`,
`kwak2021evacroute`, `kwon2025koreaevac`, `lee2021crownfuel`, `lee2026occurrence`,
`lim2022fueldanger`, `lim2025fwi`, `mois2025evacuationstages`,
`mois2026aievacroute`, `nifos2018evacsystem`, `nifos2026kfdrs`, `park2025drivers`,
`sung2025geostationary`), and **not one of them computes a forecast-value or
decision-quality quantity.** They are occurrence prediction, danger rating, fuel
and crown-fire characterisation, shelter-location planning, route optimisation,
observed evacuation behaviour, observation latency measurement, and agency
statistics.

Nearest approaches:
- `sung2025geostationary` — Korean wildfire observation latency measured
  (geostationary vs polar-orbiting), "never converts latency into decision
  value". This is the correct *input* to a Korean instantiation and must be
  cited rather than re-derived.
- `mois2025evacuationstages` — the Korean operational trigger, two fixed lead
  times (5 h / 8 h), which is the untuned baseline, not an evaluation.
- `chang2026multiscale` — a Korea-affiliated first author already publishing
  wildfire-evacuation modelling in *Risk Analysis*, on a **US** case. The
  sentence "first Korean researcher to do wildfire evacuation modelling" is
  therefore **false** and must not be written.

**Why `UNKNOWN` and not `PLAUSIBLE`.** `docs/SEARCH_PROTOCOL.md` §6 records
Category 8 as **"S1 (blocked)"** — 49 queries, but "**KCI/RISS/DBpia keyword
sweep could not be completed** (server-side search undrivable, DBpia 503)" and
states the consequence explicitly: "**no Korean claim may be described as
searched** until the KCI/RISS/DBpia sweep is completed." Today's single
Korean-language web query (logged) returned only agency action guidelines, a
news item on the 2025 forecast-system shortfall, and blog material — no academic
study. That does not lift the block.

**And even if it were vacated:** `NOVELTY_STANDARD` §4 makes "first in Korea"
**N4 and insufficient** unless (a) a Korean-specific condition *changes the
answer* and the change is shown, (b) the published method *fails* on Korean
data and the failure is documented, or (c) the quantity has no comparable
analysis anywhere, in which case the novelty is N2 and Korea is incidental.
`docs/CURRENT_THESIS.md` already self-rates "Korean setting alone is sufficient
novelty" as **"Low — treat as false"**. This component can therefore never be
promoted on its own, whatever the search returns.

- **Search coverage:** Category 8 at **S1 (blocked)**; Category 4's Korean pass
  (query 4.23, null) plus 1 Korean-language query today. Tier: **S1**.
- **Full-text coverage:** `sung2025geostationary` E2-E3 (Category 7's record);
  most Korean records E1-E2.
- **Unsearched databases:** **KCI, RISS, DBpia, ScienceON, NDSL** — the entire
  Korean academic indexing infrastructure. Also Scopus/WoS.
- **Language limitations:** the Korean-language pass is web-search only; the
  Korean *journal* literature is unsearched. This is the largest blind spot in
  the repository and it sits directly under this component.
- **Publication-date cutoff:** 2026-09-20.
- **Confidence:** **Low, and deliberately so.** Any Korean claim written before
  the KCI/RISS/DBpia sweep is a judge-bait sentence.

---

## WG-COMB-1 — The relationship between information availability / forecast quality and **assisted-evacuation option expiry** is evaluated directly

*Plain statement of the question: is useful wildfire forecast or observation
information available **before** an assisted-evacuation option expires?*

**Score: `UNKNOWN`**

**No occupying prior art was identified in the searched corpus.**

**Nearest works, and the exact gap in each:**

| Work | Has | Lacks |
|---|---|---|
| `jewson2026evacuation` | Information *arrival timing* vs. an act-now decision, solved by loss; "evacuate now or wait for the next forecast" | Self-evacuation only; no assisted option; nothing expires except the chance to act early; no latency |
| `georgakakos2025evacuationtiming` | Issue-now-vs-delay under a probability sequence, **with an evacuation-completion-time interval** | Completion time is an **exogenous input estimate**, not a computed expiry; hazard-generic; no responder |
| `sezer2026infodesign` | Information precision vs decision loss, with routes that "flood at a surge deadline" (PREPRINT) | Self-evacuating zones; no assisted evacuation; no information *availability* question |
| `moradi2026supported` | Supported evacuation of hospital/long-term-care residents, inbound responder, pickup, egress (PREPRINT) | No forecast-quality axis at all; "runs no sensitivity analysis" over forecast error |
| `shahparvari2017robust` | Assisted evacuation of late evacuees under **hard time windows** | Time windows are exogenous; no fire-spread-derived deadline; no information axis |
| `beyki2026modular` | Inbound rescue traffic simultaneous with outbound self-evacuation | Output is simulated evacuation time; no forecast-quality axis |
| `alexander2026nursing` | Shuttling mobility-impaired residents | No hazard progression constrains any leg; no deadline computed |
| `bish2011planning` | Last pickup required by a location-specific risk-determined time | Exogenous deadline, not hazard-derived; no information axis |
| `sung2025geostationary` | Korean observation latency, quantified | No decision, no deadline |
| `chang2026multiscale` | Alert latency determines *who gets out* | Self-evacuating households; no responder; no deadline computed |

Nobody in the corpus joins the two halves. The assisted-evacuation literature
takes deadlines as given and never asks whether the information needed to hit
them exists in time. The forecast-value literature asks what information is
worth having and never applies it to a rescue mission that can expire.

**Adjacent-hazard pass (required by the brief).** Flood, hurricane, tsunami and
landslide were searched. Hurricane came closest twice: `jewson2026evacuation`
and `regnier2008public` both put information timing against an evacuation
decision, and the hurricane **nursing-home / hospital** literature discusses
warning time as a determinant of evacuate-vs-shelter (e.g. the US national
criteria document for nursing-home evacuation decision-making, and
GAO-06-443R — **practitioner and audit documents, not research evaluations,
metadata UNVERIFIED, logged as leads only**). That literature reasons about
warning time qualitatively; it does not evaluate information availability
against option expiry. Landslide early warning
(arXiv:2605.17419, *"to provide sufficient evacuation time"* — **search lead,
UNVERIFIED**) frames the same intuition without evaluating it. **No occupant
found in any adjacent hazard.**

**Why `UNKNOWN`, explicitly.** Three binding reasons:

1. The search behind this null is **S1**: 8 targeted web queries, 2 alphaXiv
   discovery rounds, 1 Korean-language query, and a corpus scan. Consensus — the
   peer-reviewed corpus — was **unavailable all day (quota 30/30, resets 1
   October)**. Scopus, WoS, TRID and the entire Korean indexing infrastructure
   are unsearched. Under `SEARCH_PROTOCOL` §1, an S1 null supports nothing.
2. `NOVELTY_STANDARD` §3.2 is explicit: a null search yields `UNKNOWN`, never
   support. This component **must not** be described as novel on the strength of
   this file.
3. Even at S2, the component as phrased is a **conjunction** (assisted
   evacuation + information availability + expiry). Under §3.1 it needs the
   missing sentence: *what does joint treatment conclude that the parts cannot?*
   The candidate answer — that a mission-feasibility payoff is discontinuous, so
   information has value only in the narrow window where it can flip
   feasibility, which is a different value geometry from a scalar cost-loss
   payoff — is **asserted, not demonstrated**, and demonstrating it is the
   experiment, not the prior-art finding.

- **Search coverage:** **S1.** Queries logged in
  `docs/search-logs/agent-rq1-decomposition.md` §C.
- **Full-text coverage:** `jewson2026evacuation` E3/E4; `sezer2026infodesign`
  E3; `moradi2026supported` E3 (read by a prior agent via alphaXiv);
  `georgakakos2025evacuationtiming` E2 (paywalled — and this is the most
  important one to obtain); `shahparvari2017robust`, `beyki2026modular`,
  `bish2011planning` at Category 2/3's levels.
- **Unsearched databases:** Consensus (quota), Scopus, Web of Science, TRID,
  IEEE Xplore, ScienceDirect direct, KCI/RISS/DBpia.
- **Language limitations:** one Korean query; no Chinese, Japanese, Spanish,
  Portuguese, Greek or Italian pass, despite Greek, Portuguese and Australian
  groups owning much of the assisted-evacuation and trigger literature.
- **Publication-date cutoff:** 2026-09-20.
- **Confidence:** **Low.** This is the project's most distinctive question and
  it has the **weakest** search behind it. It should be promoted to a full S2
  protocol search — including Consensus after 1 October and the Korean
  databases — before anyone says the word "novel" about it out loud.

---

## 2. Consequences for the claim registry

Recorded here, **not applied** — this agent's write scope was restricted to the
files listed in its brief. The following are owed:

1. **WG-C-002** stays `WEAKENED`. But the *reason* changes: the defensible
   contrast is no longer "their comparator is untuned" — `ardid2026forecastvalue`
   tunes its FBI threshold to maximise PEV (E3). The contrast is **tuned index
   threshold vs tuned positional trigger, and point estimate vs frontier.**
2. **WG-C-012** — `zha2024distributed` and `chang2026multiscale` are both closer
   than review 04 credited. The claim needs re-reading against them, and
   `zha2024distributed` needs full text.
3. **Two new papers are filed** — `jewson2026evacuation` and
   `sezer2026infodesign` — with metadata and notes only. Per **AGENTS.md §5**
   they also require rows in `bibliography/literature.csv`,
   `bibliography/doi_registry.csv`, `bibliography/wildfireguardian.bib`,
   `novelty/NOVELTY_MATRIX.md`, and (for `jewson2026evacuation`, threat HIGH)
   `novelty/NOVELTY_THREATS.md`. **Those edits are outstanding.** Ready-to-paste
   rows are in `docs/search-logs/agent-rq1-decomposition.md` §E so the next
   agent can apply them without re-deriving anything.
4. **Corrections owed** in `literature/notes/ardid2026forecastvalue.md`,
   `literature/metadata/ardid2026forecastvalue.yaml` (`one_line_difference`),
   and `literature/reviews/04-forecast-value.md` §3 table and §4.1 item 7 — all
   itemised in `literature/reviews/fulltext-ardid2026.md` §4.

## 3. Open questions this file generates

For `novelty/OPEN_QUESTIONS.md`:

- Read `zha2024distributed` in full. Does its OSSE score anything downstream of
  prediction error? If yes, WG-FV-2 becomes `OCCUPIED`.
- Read `georgakakos2025evacuationtiming` in full. Its evacuation-completion
  interval is the single closest published object to an expiring evacuation
  option.
- Backward and forward citation chase on `jewson2026evacuation` — a 2026 paper
  posing the RQ1 decision structure in its purest form, with citations not yet
  traversed.
- Obtain Ardid et al.'s **Supplementary Text S2**. It contains the cost-loss
  sensitivity tests. If S2 contains a C/L sweep, WG-FV-4's one-dimensional form
  is occupied *in wildfire* and the RQ1 framing needs revision.
- Complete the KCI / RISS / DBpia sweep. Until then WG-FV-7 cannot move and no
  Korean claim may be described as searched.
- Re-run WG-COMB-1 on Consensus after 1 October 2026.
