# Full-Text Read — Ardid et al. (2026)

**Agent:** C + B (Verification / Citation Auditor + Prior-Art Adversary)
**Date:** 2026-09-20
**Target:** `ardid2026forecastvalue`
**Search log:** `docs/search-logs/agent-rq1-decomposition.md`
**Companion deliverable:** `novelty/RQ1_DECOMPOSITION.md`

---

## 0. Citation and access

Ardid, A., A. Power, A. Valencia, H. G. Pearce, S. Gross, D. Dempsey and
M. M. Boer, 2026: *From forecast skill to economic value: sub-hourly wildfire
potential forecasting across Australian regions.* International Journal of
Wildland Fire **35**(4), WF25221. DOI 10.1071/WF25221.

- **Access route:** DOI → 302 → ConnectSci (CSIRO Publishing) article page,
  retrieved as rendered HTML. **Open Access, CC BY-NC-ND 4.0** (stated on the
  article page; OpenAlex records `oa_status: hybrid`, `license: cc-by-nc-nd`,
  `version: publishedVersion`).
- **Evidence level attained: E3** (full text read, relevant sections; verbatim
  quotes located).
- **Why not E4.** Every reading of the body came through one rendering
  (WebFetch of the ConnectSci HTML). Independent second renderings were
  attempted and **failed**: `curl` to ConnectSci → HTTP 403 (Cloudflare);
  University of Canterbury repository record `hdl.handle.net/10092/109982` →
  HTTP 403 to both `curl` and WebFetch; `publish.csiro.au/WF/WF25221` → 301
  back to the same ConnectSci host; OpenAlex reports
  `any_repository_has_fulltext: false` and no repository PDF URL. Per
  `docs/EVIDENCE_LEVELS.md` rule 3, **no number extracted below may be quoted
  as a WildfireGuardian figure until a second rendering confirms it.**

### Anti-fabrication controls actually run

The project has previously had a summarising fetch invent statistics. Controls
applied here, and their results:

1. **Negative-control term sweep.** Asked for PRESENT/ABSENT on eleven terms.
   Returned ABSENT for ten (`latency`, `lead time`, `delay`, `timeliness`,
   `evacuation`, `trigger boundary`, `buffer`, `OSSE`, `synthetic`, `perturb`)
   and PRESENT with a plausible in-context quote for one (`noise`). An
   extractor that fabricates does not return ten ABSENTs.
2. **False-premise trap.** Asked it to quote "the sentence describing the
   authors' Korean case study" and "the sentence stating the latest-safe
   dispatch time for rescue vehicles." Both returned **ABSENT** with the
   correct correction (three Australian regions). It declined the bait.
3. **Repeated-table cross-check.** Table 1 was requested twice in separately
   worded calls. The FBI rows agreed exactly both times (thresholds
   19.53 / 12.97 / 24.99; PEV 0.23 / 0.407 / 0.239).

These controls raise confidence that the body text was genuinely read. They do
**not** substitute for an independent rendering, which is why the level is E3.

---

## 1. Extraction against the brief

### 1.1 What decision is modelled, and whose decision is it?

A **precautionary deployment / suppression-preparedness decision by a fire
management agency**, in the two-action cost-loss form.

> "Let *C* = A$50,000 (cost of a precautionary deployment) and *L* = A$10
> million (loss from an uncontrolled fire)." (Methods, *Cost–loss for forecast
> utility*)

The forecast target is **fire occurrence**, not fire arrival at a place:

> "A binary classification target was assigned to each 30-min timestamp, where
> label = 1 indicated that a fire occurred within a future look-ahead window
> (2, 5 or 10 days)" (Methods, *Feature engineering and forecast target*)

**"Sub-hourly" refers to the input/update cadence, not the forecast lead:**

> "Each forecast cycle ingests 30-min AWS observations – temperature, relative
> humidity, wind speed and other variables" (Methods)

So the product is a **30-minute-cadence forecast of whether a fire will occur
somewhere in the region within the next 2–10 days.** There is no resident, no
household, no responder and no place-specific arrival time anywhere in the
decision.

Asked directly whether the paper addresses evacuation, resident protective
action, emergency dispatch or human safety, the extraction returned **ABSENT**:
the paper "focuses on forecast skill and economic value for fire management
resource allocation."

### 1.2 Comparator/baseline — and is it tuned?

The comparator is the **Fire Behaviour Index (FBI)**, the operational Australian
fire-danger index:

> "The 2022 Australian Fire Danger Rating System (AFDRS) replaced the FFDI with
> the fuel-specific Fire Behaviour Index (FBI)" … "While the Bureau of
> Meteorology (BoM) now computes the FBI hourly on a ~1.5 km grid … only a
> single daily rating is released publicly."

**The baseline IS tuned, on the same data, to the same objective.** This
corrects the repository's previous record.

> "The optimal classification threshold for each model is selected
> retrospectively to maximise PEV, reflecting how an operator might calibrate
> decision rules based on historical performance." (Methods)

and the FBI is recomputed by the authors rather than taken as published:

> "all FBI values in this study were recalculated directly from observed AWS
> data"

Table 1 reports a distinct optimal FBI threshold per region — 19.53 (Sunshine
Coast), 12.97 (Brisbane), 24.99 (Hobart) — i.e. a **per-region retrospectively
optimised decision threshold on the baseline**.

> **Correction to the repository.** `literature/metadata/ardid2026forecastvalue.yaml`
> and `literature/notes/ardid2026forecastvalue.md` previously recorded
> "comparator tuned? **not stated**" and "the retrieved record does not indicate
> it was re-tuned." That was an E2 inference and it is **wrong at E3**. Ardid et
> al. tune the FBI threshold retrospectively to maximise the same PEV objective
> the ML model is scored on. This is a *stronger* baseline than the repository
> credited, and it removes any suggestion that Ardid et al. benchmarked against
> an untuned index.
>
> What it is **not** is a *positional* comparator. The tuned object is a scalar
> threshold on a danger index. It is not a spatial trigger boundary or buffer
> distance, and there is no scenario distribution of fire progression over which
> a buffer parameter could be optimised. The distinction that survives is
> "tuned index threshold" vs "tuned positional trigger", **not** "untuned vs
> tuned".

### 1.3 Break-even or usability frontier?

**No.** Asked directly, the extraction returned ABSENT and gave the reason: the
study fixes a single cost-loss pair rather than sweeping it.

- No break-even skill threshold is reported.
- PEV is **not** plotted against the cost-loss ratio C/L, and no region of C/L
  with PEV > 0 is delimited. C and L are fixed at A$50,000 and A$10 million
  throughout the main text.
- The only nod to the C/L dependence is a stability check, not a frontier:
  > "Sensitivity tests (Supplementary Text S2) show that although absolute PEV
  > values depend on these assumptions, the relative performance ranking of
  > models remains stable"

So the paper reports **a value comparison at one point of the cost-loss space**,
not a usability boundary in any space. This is the single most important
finding of the read: the Richardson/Zhu apparatus is used to produce **two PEV
numbers per region**, not a value region.

### 1.4 Forecast latency — treated at all?

**No.** `latency`, `delay` and `timeliness` are all ABSENT from the body, and a
direct question about observation-to-product delay, update cadence or real-time
operation returned ABSENT.

The paper's temporal argument is about **release cadence of the public product**
("only a single daily rating is released publicly"), which motivates a
sub-hourly product. That is an argument about *how often information is
published*. It is never converted into a decision-value quantity, never varied,
and never distinguished from forecast lead.

Note also that **`lead time` itself is ABSENT** as a phrase. The temporal
structure is a 2/5/10-day look-ahead window on the label, examined as three
label definitions — not as a lead-time axis along which value is traced.

### 1.5 Is forecast error manipulated in controlled dimensions?

**No — forecasts are evaluated as-is against observed records.**

> "all FBI values in this study were recalculated directly from observed AWS
> data"

and validation is

> "on the full, naturally imbalanced held-out records without any re-balancing
> at evaluation."

Nothing is perturbed, degraded or injected. `perturb` and `synthetic` are both
ABSENT. Error enters only as whatever error the trained models happen to have
on held-out data.

### 1.6 Is decision loss the evaluation metric, or a forecast score?

**Both, in sequence — and the decision-loss step is a scalar, not a frontier.**

- Forecast-side metrics: TPR, FPR, ROC curves, PR curves, AUC.
- Decision-side: Potential Economic Value, in the standard Richardson/Zhu form.
  As extracted:
  `E_p = C×(FPR×D) + L×((1−TPR)×T)`; `E_no-f = L×T`; `E_pe-f = 0`;
  `PEV = (E_no-f − E_p)/(E_no-f − E_pe-f)`.
  (Recorded as extracted; the `E_pe-f = 0` term should be re-checked against an
  independent rendering before it is ever reproduced.)

So the paper does close the loop from skill to value — that is its stated
contribution and the title says so. What it does **not** do is let the decision
loss *define a boundary*. The loss is evaluated once per model per region.

### 1.7 Any OSSE / hidden-truth design?

**No.** `OSSE` and `synthetic` are ABSENT. Ground truth is real:

> "Using almost 50 years of sub-hourly weather observations and 126 documented
> fires across the three regions, we train Random-Forest classifiers"
> … "Fire ignitions were identified from official incident reports"

This is a retrospective real-data study. Its truth is observed, not hidden.

### 1.8 Assisted evacuation? Mission feasibility? Korean or non-Australian application?

- **Assisted evacuation:** ABSENT. No responder, no vehicle, no pickup.
- **Mission feasibility:** ABSENT. The payoff is a scalar expense, not a
  feasibility indicator on a routed trip.
- **Korean or non-Australian application:** ABSENT. Three Australian regions
  only (Sunshine Coast, Brisbane fringe, Hobart). Note the author affiliations
  span New Zealand (Canterbury, FENZ, Scion) and Australia (Covey Associates,
  Western Sydney), but the *application* is Australian. A transfer-learning /
  generalisation subsection exists ("Cross-validation and transfer learning";
  "Model generalisation and data sufficiency") and the learning-curve result is
  offered as evidence of feasibility "for data-limited regions" — which is the
  paper's own claim on the ground a Korean application would otherwise occupy.
  It is a *feasibility* claim about ML fire-potential forecasting in data-poor
  regions, not a Korean result.

### 1.9 Headline results (E3 — NOT yet citable as numbers)

> "The ML model improved forecast skill over the FBI by 10–30%, with the ML
> system doubling potential savings" (Abstract; the extraction reports the same
> phrasing in the Conclusion.)

Table 1 as extracted (**E3, pending an independent rendering — do not cite**):

| Region | Model | Optimal threshold | TPR | FPR | PEV | Net savings (A$ M) |
|---|---|---|---|---|---|---|
| Sunshine Coast | FBI | 19.53 | 0.38 | 0.08 | 0.23 | 34.5 |
| Sunshine Coast | ML tailored | 0.6 | 0.796 | 0.077 | 0.651 | 97.7 |
| Sunshine Coast | ML generalised | 0.58 | 0.682 | 0.135 | 0.392 | 39.3 |
| Brisbane | FBI | 12.97 | 0.611 | 0.109 | 0.407 | 61.1 |
| Brisbane | ML tailored | 0.57 | 0.718 | 0.158 | 0.421 | 63.2 |
| Brisbane | ML generalised | 0.52 | 0.568 | 0.137 | 0.379 | 38.1 |
| Hobart | FBI | 24.99 | 0.429 | 0.101 | 0.239 | 35.9 |
| Hobart | ML tailored | 0.84 | 0.755 | 0.135 | 0.502 | 75.4 |
| Hobart | ML generalised | 0.71 | 0.654 | 0.129 | 0.384 | 35.3 |

Observe, adversarially, that on Brisbane the tuned FBI (PEV 0.407) is within a
few per cent of the ML model (0.421), and the ML *generalised* model loses to
the tuned FBI in Brisbane and Hobart. **A tuned baseline is close to a good
forecast in 1 of 3 regions.** That is a live warning for WildfireGuardian's own
"what would falsify the thesis" item 3.

---

## 2. Required side-by-side table

WildfireGuardian column is filled from `docs/CURRENT_THESIS.md` (RQ1 statement,
comparator paragraph, output paragraph, and the RQ2 assisted-evacuation
framing). **Nothing in that column is built. Every cell is PROPOSED.**

| Feature | Ardid et al. 2026 | WildfireGuardian proposed experiment |
|---|---|---|
| **Forecast-error manipulation** | **No.** Forecasts evaluated as-is on held-out records; "all FBI values … recalculated directly from observed AWS data"; `perturb`/`synthetic` absent. Error is whatever the trained model has. | **PROPOSED.** Forecast quality treated as a controlled experimental axis — CURRENT_THESIS RQ1 output is "a boundary in forecast-quality space — (skill, lead time, latency)", which requires skill to be set, not observed. No axis definition exists yet. |
| **Latency manipulation** | **No.** `latency`, `delay`, `timeliness` absent from the body. Product *release cadence* motivates the work but is never a variable and never valued. | **PROPOSED.** Latency as an axis *distinct from lead time* (observation-to-product delay shortening the usable window at fixed skill). Currently claim text only; see review 04 §4.2 O3 and WG-C-012. |
| **Strong trigger baseline** | **Partly — a tuned index threshold, not a positional trigger.** FBI threshold "selected retrospectively to maximise PEV" per region (19.53 / 12.97 / 24.99). Genuinely tuned, same objective, same data. But it is a scalar danger-index cut-off; no buffer distance, no trigger boundary, no scenario distribution of fire progression. | **PROPOSED.** "A *tuned* trigger/buffer policy — the buffer distance or trigger-boundary lead time optimized over the same scenario distribution the forecast-aware policy sees" (CURRENT_THESIS, RQ1, marked non-negotiable). Not implemented. |
| **Decision loss** | **Yes, as a point estimate.** PEV in the Richardson/Zhu form at fixed C = A$50,000, L = A$10 M; reported as two numbers per region plus a stability check in Supplementary S2. | **PROPOSED.** Decision loss as the object that *defines the boundary*, not as a summary statistic — and, for RQ2, a discontinuous mission-closes/does-not-close payoff rather than a scalar expense (review 04 §4.2 O4). Not implemented. |
| **Break-even frontier** | **No.** No skill threshold, no C/L sweep, no PEV>0 region, no usability limit. Single cost-loss point. | **PROPOSED.** The stated RQ1 deliverable: a boundary "separating the region where forecast-aware action wins from where it does not". Not implemented; the thesis itself flags the risk that the boundary is trivial. |
| **OSSE hidden truth** | **No.** Real ignitions from official incident reports; ~50 years of AWS observations; 126 documented fires. Truth is observed. | **PROPOSED.** Hidden-truth evaluation is implied by manipulating forecast error against a known answer, and is the subject of WG-C-010; `zeng2020osse` records "extension of OSSEs to societal impacts" as an open community recommendation. Not implemented. |
| **Assisted evacuation** | **No.** No responder, no pickup, no vehicle, no resident. Decision is agency pre-positioning. | **PROPOSED.** The whole of RQ2 — responder base → resident → pickup → safe destination, with fire-arrival constraints on every leg, output = latest-safe dispatch time. Not implemented. |
| **Korean application** | **No.** Sunshine Coast, Brisbane fringe, Hobart. Australia only. (Transfer-learning / data-limited-region feasibility is claimed, which pre-empts part of the "new region" argument.) | **PROPOSED.** Korean landscapes. Explicitly rated **"Low — treat as false"** as standalone novelty in CURRENT_THESIS's confidence table, and N4-weak under NOVELTY_STANDARD §4 unless (a), (b) or (c) is *demonstrated*. Not implemented. |

---

## 3. Verdict: does Ardid occupy RQ1?

**No. It occupies RQ1's premise, not RQ1.**

What it forecloses, permanently and cheerfully conceded:

1. "Nobody has applied cost-loss / potential-economic-value machinery to
   wildfire." **False since 2026.** Ardid et al. did it, in IJWF, with the
   standard Richardson/Zhu apparatus.
2. "Wildfire forecast evaluations use untuned operational baselines."
   **False.** The FBI threshold is retrospectively optimised to the same PEV
   objective, per region. The repository recorded the opposite at E2 and must
   correct it.
3. "Forecast skill improvements in wildfire have not been translated into
   money." **False.** That is literally this paper's title.

What it leaves untouched, all of it verified ABSENT at E3:

- The decision is **agency pre-positioning against regional fire occurrence in
  2–10 days**, not protective action for people against fire arrival at a place.
- **No boundary of any kind** is reported — no skill threshold, no C/L region,
  no usability limit. One cost-loss point, two PEV numbers per region.
- **Error is never manipulated**; **latency is never mentioned**; **truth is
  never hidden**.
- The tuned object is a **scalar index threshold**, not a **positional trigger
  or buffer**.

So the correct adversarial sentence for a judge is:

> Ardid et al. (2026) closed the question "can wildfire forecast skill be
> converted into economic value?" — yes, by about a factor of two against a
> retrospectively tuned Fire Behaviour Index threshold, at one cost-loss point,
> for agency pre-positioning against 2–10 day fire occurrence in three
> Australian regions. They did not ask at what forecast quality that conversion
> stops paying, they did not vary forecast error or latency to find out, and
> the decision they priced is not a protective action.

WG-C-002 therefore stays `WEAKENED` and does **not** move to `OCCUPIED`. But
the required claim rewrite proposed in review 04 §5 must be tightened further:
the contrast is no longer "tuned vs untuned comparator" (Ardid tunes), it is
**"tuned index threshold vs tuned positional trigger, and point estimate vs
boundary."** Anyone defending the project on the "their baseline wasn't tuned"
line will be corrected in public by anyone who has read the Methods.

---

## 4. Corrections required elsewhere (not made by this agent)

Flagged, not edited — this agent's write scope was restricted.

1. `literature/metadata/ardid2026forecastvalue.yaml` — the `one_line_difference`
   asserts the FBI "is an operational index, not a buffer/trigger policy tuned
   on the same scenario distribution." The second half is right; the phrasing
   implies the FBI was not tuned, which is wrong. Needs rewording.
   (`fulltext_status`, `evidence_level`, `access_route` **were** added by this
   agent, as instructed.)
2. `literature/notes/ardid2026forecastvalue.md` — "Limitations" and
   "WildfireGuardian difference §2" both need the tuning correction; "Full text
   not read. Evidence level E2. Flagged NEEDS_FULL_TEXT" is now stale.
3. `literature/reviews/04-forecast-value.md` §3 comparison table — the
   `ardid2026forecastvalue` row reads "Comparator tuned? **not stated**". It is
   now stated: **yes, threshold optimised to maximise PEV.** Also §4.1 item 7
   ("tuning the decision threshold before reporting value … Closed") should
   cite Ardid as the wildfire instance.
4. `novelty/NOVELTY_THREATS.md` — threat level HIGH remains correct; the
   *reason* changes (stronger baseline than recorded, but still no boundary).
