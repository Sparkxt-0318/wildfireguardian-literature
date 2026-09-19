# bennett2026wise

## Citation
Bennett, L., Jain, P., Moore, B., & Boisvert, J. (2026). Assessment of fire spread predictions from the Wildfire Intelligence and Simulation Engine (W.I.S.E.) using a large set of satellite-derived wildfire perimeters. *International Journal of Wildland Fire*, 35(8), WF26072. https://doi.org/10.1071/WF26072

## Publication status
PEER_REVIEWED. Verified from the publisher's article page (abstract plus scenario results).

## Problem
Fire spread models are rarely evaluated at scale because real spread data is scarce. How well does Canada's
operational fire growth engine actually predict daily fire perimeters?

## Method
Ran W.I.S.E. (the Prometheus successor, built on the Canadian FBP system) to produce daily spread predictions,
and compared them to the Canadian Fire Spread Dataset (CFSDS) of satellite-derived daily perimeters. Three
scenarios: (1) default model parameters; (2) burn duration optimised in hindsight; (3) burn duration and wind
direction both optimised in hindsight.

## Data
**19,848 individual fire-days across 2,210 wildfires**, historical inputs.

## Outputs
Metrics: normalized area difference, precision, recall, F1, Intersection-over-Union, Hausdorff distance.

| Scenario | F1 | Precision | Recall | IoU | Hausdorff | Norm. area diff. |
|---|---|---|---|---|---|---|
| 1 — default parameters | 0.259 | 0.200 | 0.856 | 0.194 | 2828 m | 0.544 |
| 2 — optimised burn duration | 0.498 | 0.451 | 0.637 | 0.284 | 918 m | -0.109 |
| 3 — optimised duration + wind direction | 0.539 | 0.475 | 0.701 | 0.309 | 891 m | -0.061 |

## Key equations
Standard confusion-matrix and set-overlap definitions; not reproduced here.

## Assumptions
- Satellite-derived daily perimeters (CFSDS) are treated as ground truth.
- Scenarios 2 and 3 use **hindsight-optimised** parameters, i.e. information unavailable at forecast time.

## Validation
This is the validation study. Its scale (19,848 fire-days) makes it the strongest available statement about
operational fire growth model skill on real fires.

## Limitations
- Daily timestep; says nothing about sub-daily arrival timing, which is the timescale of an evacuation decision.
- Canadian boreal fuels via the FBP system; transfer to Korean *Pinus densiflora* on steep slopes is unestablished.

## WildfireGuardian overlap
Directly supplies the "how wrong are these models" number for the OSSE design. Default-parameter precision 0.200
with recall 0.856 means the model massively over-predicts burned area — it burns far more than reality. That
asymmetry, not a symmetric error, is what our injected forecast error should look like.

## WildfireGuardian difference
Bennett et al. measure perimeter agreement. They do not ask, and explicitly cannot answer, whether a model with
IoU 0.194 produces a worse *evacuation decision* than one with IoU 0.309. That question is WG-C-014.

## Novelty threat
**BACKGROUND**, and simultaneously the strongest supporting evidence for WG-C-014's premise: it demonstrates that
the field's evaluation currency is spatial overlap, full stop.

## Quotes / page references
Abstract: "Using default model parameters, fire spread predictions achieve an average F1 score of 0.259."
Abstract: "scenario 2 optimizes burn duration, reaching an average F1 score of 0.498."

## Follow-up papers
- elmfire2025validation (comparable CONUS numbers for ELMFIRE and FARSITE).
- Forward citations of WF26072 not yet chased. **Open task.**
