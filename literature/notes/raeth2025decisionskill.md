# raeth2025decisionskill

## Citation
Raeth, K., and N. Ludwig, 2026: Forecast skill is not decision skill: evidence
from weather-dependent decision tasks. arXiv:2512.14779v2 [cs.LG], 4 September
2026. DOI 10.48550/arXiv.2512.14779

## Publication status
**PREPRINT** (arXiv). Not peer-reviewed. Full text retrieved via alphaXiv.
Evidence level **E3**.

## Problem
Standard forecast verification evaluates at the *forecast* level (forecast vs.
observation). Decision makers care about the *decision* level. Do forecast-level
rankings survive the transfer?

## Method
Applies the **decision calibration** framework (Zhao et al.). A decision task is
a cost function c(a, y) over actions and outcomes; the decision maker applies the
Bayes rule delta_c(F_x) = argmin_a E_{Y~F_x}[c(a,Y)]. Evaluation uses both the
observed cost c(delta_c(F_x), y_obs) and the *cost gap* between expected and
observed costs. Cost-induced scoring rules connect this back to proper scoring
rules: every bounded cost function c induces a proper scoring rule
S_c(F_x, y) = c(delta_c(F_x), y).

## Data
State-of-the-art probabilistic ML weather prediction models vs. a classical NWP
ensemble, evaluated on decision tasks motivated by frost protection, heat
protection and wind-power dispatch.

## Outputs
Model performance at the forecast level **does not reliably translate** to
downstream decision performance; some performance differences only appear at the
decision level; and even among *similar* decision tasks, model rankings change.

## Key equations
- Bayes decision rule: delta_c(F_x) := argmin_{a in A} E_{Y~F_x}[c(a,Y)]
- Observed cost: C_obs = E_{X,Y}[c(delta_c(F_X), Y)]
- Cost-induced proper scoring rule: S_c(F_x, y) = c(delta_c(F_x), y)

## Assumptions
Normative: assumes optimal (Bayes) decision-making and that the decision maker
trusts the forecast. Cost functions are bounded and known.

## Validation
Retrospective evaluation on operational forecast archives. No live decision trial.

## Limitations
Decision tasks have scalar outcome variables and small action spaces. No spatial
hazard field, no routing, no deadline. Preprint.

## WildfireGuardian overlap
This is the strongest current statement of **WG-C-014's general proposition**,
and it also pre-empts a large part of **WG-C-006**: the paper's whole point is
that you must evaluate at the decision level, with a decision-specific cost
function, rather than trusting aggregate skill metrics.

## WildfireGuardian difference
The paper explicitly recovers Relative Economic Value as the special case of
"binary threshold decisions with a cost-loss cost function". WildfireGuardian's
decision is neither: it is a *feasibility* decision on a routed round trip whose
cost function is discontinuous (mission closes / does not close) and whose
predictor output is a spatial arrival-time field scored by overlap, not a scalar
predictive distribution. The mechanism by which IoU decouples from decision
quality — error *location* relative to the access route — has no analogue here.

## Novelty threat
**CRITICAL** to WG-C-014 in general form; **HIGH** to WG-C-006. After this paper,
"we show accuracy metrics don't track decision quality" is not a contribution;
only "here is the wildfire-geometric mechanism by which IoU misleads about
evacuation-mission feasibility, quantified" is.

## Quotes / page references
Abstract: "model performance at the forecast level does not reliably translate to
performance in downstream decision-making" (abstract, p.1).
Related work: "recovering REV as the special case of binary threshold decisions
with a cost-loss cost function" (Sec. 1, Related work).

## Follow-up papers
- mandi2024dfl, liu2026dflfail (the OR/ML lineage of the same proposition)
- murphy1987accuracyvalue, chen1987qualityvalue (the 1987 originals)
- berlinghieri2024pm25 (the same move in a wildfire-smoke setting)
