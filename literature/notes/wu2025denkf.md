# wu2025denkf

## Citation
Wu, T., Zhang, Q., Zhu, J., Xu, L., & Zhang, Y. (2025). Forest Fire Spread Prediction and Assimilation Using the Deterministic Ensemble Kalman Filter. *Fire Technology*, 61(4), 2467-2492. https://doi.org/10.1007/s10694-024-01690-x

## Publication status
PEER_REVIEWED. Crossref-verified. Evidence level **E2** — abstract only.

## Problem
Forest fire spread predictions are corrupted by input-parameter and model error. Can a deterministic ensemble
Kalman filter (DEnKF) correct the predicted fire line better than the standard EnKF?

## Method
DEnKF-based dynamic correction, avoiding the perturbed-observations step of standard EnKF.
**"We used Observing System Simulation Experiments (OSSEs) to validate the effectiveness of the proposed method."**
Sensitivity to wind conditions and to DEnKF parameters was investigated. The authors state this is the first
application of DEnKF to forest fire spread.

## Data
Synthetic (OSSE-generated) fire spread scenarios.

## Outputs
DEnKF outperforms EnKF in correcting fire spread, particularly at fire-line inflection points. Integrated into a
"Forest Fire Spread Prediction and Assimilation" system offered as emergency-management guidance.

## Key equations
DEnKF analysis update; not retrieved.

## Assumptions
Identical-twin OSSE risk applies, as above.

## Validation
OSSE only; no real-fire assimilation reported in the abstract.

## Limitations
Synthetic truth; the "emergency management guidance" framing is asserted, not demonstrated against any decision.

## WildfireGuardian overlap
Confirms independently of zha2024distributed that OSSE is a standard, named validation methodology inside wildfire
spread prediction, in a mainstream fire journal, in 2025.

## WildfireGuardian difference
The OSSE is scored on fire-line position error. WildfireGuardian's OSSE would be scored on whether the responder
mission closed. Different loss function, different conclusion possible — that is exactly the WG-C-014 hypothesis.

## Novelty threat
**HIGH for WG-C-010.** WG-C-010 as currently worded ("We use an OSSE design to evaluate wildfire evacuation
decision quality") survives only because of the phrase *evacuation decision quality*. Dropping that phrase would
make the claim false. The registry entry should be narrowed accordingly.

## Quotes / page references
Abstract: "We used Observing System Simulation Experiments (OSSEs) to validate the effectiveness of the proposed
method in enhancing confidence in forest fire spread predictions."

## Follow-up papers
- zha2024distributed.
- Wu et al. (2024) *Fire Ecology*, FLC-GRU R-matrix estimation (OSSE-validated) — not yet filed.
