# liu2026dflfail

## Citation
Liu, M., 2026: Decision-Focused Learning: When and Why Traditional Prediction
Models Fail. arXiv:2606.21773, submitted 19 June 2026.
DOI 10.48550/arXiv.2606.21773

## Publication status
**PREPRINT** (arXiv), presented as a tutorial. Not peer-reviewed. Abstract page
retrieved via WebFetch. Evidence level **E2**.

## Problem
The predict-then-optimize paradigm assumes better predictions give better
decisions. They do not, in general.

## Method
Tutorial review of decision-focused learning (DFL), focused on stochastic linear
programming as the downstream problem.

## Data
N/A (review).

## Outputs
Two specific conclusions that bear on WildfireGuardian:
(i) data-collection strategies driven purely by *predictive uncertainty* are not
suited to decision-focused settings;
(ii) distributional distance measures such as the Wasserstein distance must be
rethought for decision-focused settings.

## Key equations
N/A at abstract level.

## Assumptions
Stochastic linear programming downstream; known decision objective.

## Validation
N/A (review).

## Limitations
Linear-programming downstream problems; no hazard, no spatial field, no deadline.
Preprint.

## WildfireGuardian overlap
Pre-empts **both** WG-C-014 ("improved predictive accuracy does not, in general,
translate into improved decision quality") **and** the motivating argument for
WG-C-008 (uncertainty-driven data collection is the wrong criterion), in one
2026 document.

## WildfireGuardian difference
The failure mechanisms studied are those of linear programs (degenerate vertices,
parameter-to-solution discontinuities). WildfireGuardian's would be geometric:
a burned-area overlap error whose *location* relative to the access route
determines whether the dispatch deadline moves at all. That mechanism is not in
this literature.

## Novelty threat
**HIGH** to WG-C-014 and WG-C-008.

## Quotes / page references
Abstract: "improved predictive accuracy does not, in general, translate into
improved decision quality".
Abstract: "data collection strategies driven purely by predictive uncertainty"
are among the tools "not directly suited to decision-focused settings".

## Follow-up papers
- mandi2024dfl (the benchmark survey)
- raeth2025decisionskill (weather instantiation)
- sun2025decisionfocusedsensing (flood instantiation)
