# cruz2013uncertainty

## Citation
Cruz, M. G., & Alexander, M. E. (2013). Uncertainty associated with model predictions of surface and crown fire rates of spread. *Environmental Modelling & Software*, 47, 16-28. https://doi.org/10.1016/j.envsoft.2013.04.004

## Publication status
PEER_REVIEWED. Crossref-verified (DOI, volume, pages, authors). Abstract text verified independently via the FRAMES catalog record 16277.

## Problem
How accurate are operational wildland fire rate-of-spread (ROS) models when evaluated against independent
observations, and what error magnitude should count as "adequate" for operational use?

## Method
Meta-analysis. The authors compiled published evaluation datasets in which model-predicted ROS was compared
with observed ROS, and computed error statistics across them. Evidence level here is **E2**: the abstract was
read in full via two independent sources; the full text was not retrieved.

## Data
49 fire spread model evaluation datasets, 1278 observations, seven fuel type groups.

## Outputs
- Only **3% of predictions were exact**.
- **Mean percent error ranged 20% to 310%**, described as homogeneous across fuel type groups.
- **Over half of the evaluation datasets had mean errors between 51% and 75%.**
- The authors propose that a **±35% error interval** represents reasonable model performance for ROS.
- Empirically-based models built from solid field observations extrapolated beyond their original datasets better
  than expected.

A widely reported additional figure — under-prediction bias present in 75% of the 49 datasets — appeared in a
search-engine summary but was **not** visible in the abstract text retrieved, and is marked NEEDS_FULL_TEXT.

## Key equations
Not retrieved (error statistics are standard MAPE/mean percent error definitions). NEEDS_FULL_TEXT.

## Assumptions
- That published evaluation datasets are representative of operational conditions (a selection-bias risk the
  authors themselves flag as a limit on inference).
- That "observed ROS" in field datasets is itself accurate enough to serve as truth.

## Validation
This paper *is* the validation synthesis. It is the most-cited single source for the claim that operational fire
spread prediction carries tens-of-percent to multiple-hundred-percent ROS error.

## Limitations
- Errors are reported for **rate of spread**, a scalar, not for fire arrival time at a specific location, which is
  what a trigger boundary or a dispatch deadline actually needs. Converting ROS error into arrival-time error at a
  given distance is an extra step WildfireGuardian must make explicitly and defend.
- No lead-time dependence: the paper does not report how error grows with forecast horizon. **This is a real gap
  for WG-C-012 and we should not pretend otherwise.**

## WildfireGuardian overlap
This is the evidence base for the forecast-skill axis of RQ1. Any skill range we simulate must contain the
published error magnitudes, or we are testing a fantasy forecast.

## WildfireGuardian difference
Cruz & Alexander quantify how wrong the forecast is. WildfireGuardian asks what that wrongness costs a
decision-maker who must dispatch a responder by a deadline. The output units differ: percent ROS error versus
minutes of dispatch slack.

## Novelty threat
**BACKGROUND.** Threatens nothing. It is a constraint on what we may assume, and the strongest single citation
for "we do not get to assume a good forecast."

## Quotes / page references
Abstract (via FRAMES record 16277): "Mean percent error ranged from 20 to 310%".
Abstract: a "±35% error interval" would represent "reasonable model performance".

## Follow-up papers
- Cruz & Alexander (2013), *The Forestry Chronicle* 89(3) — "Limitations on the accuracy of model predictions of
  wildland fire behaviour: A state-of-the-knowledge overview". Publisher returned HTTP 403; NEEDS_FULL_TEXT.
- Cruz & Alexander (2010), *IJWF* 19(4):377-398, DOI 10.1071/wf08132 — crown fire potential critique.
- bennett2026wise — the modern large-sample spatial analogue of this error synthesis.
