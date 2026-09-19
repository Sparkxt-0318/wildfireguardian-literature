# larsen2011cedar

## Citation
Larsen, J. C.; Dennison, P. E.; Cova, T. J.; Jones, C. (2011). "Evaluating dynamic
wildfire evacuation trigger buffers using the 2003 Cedar Fire." *Applied Geography*
31(1): 12–19. DOI 10.1016/j.apgeog.2010.05.003

## Publication status
PEER_REVIEWED (journal article). OA UNKNOWN. Evidence level E2 (abstract only).

## Problem
Trigger buffers had never been checked against a real fire front. Also: static buffers
built on climatological wind ignore the forecast that is actually available.

## Method
WUIVAC buffers are regenerated hourly using **forecast winds**, producing *dynamic*
trigger buffers. Hourly buffer positions are compared to the hourly observed leading edge
of the 2003 Cedar Fire for a test community.

## Data
2003 Cedar Fire, southern California; hourly forecast wind fields; hourly observed fire
front positions.

## Outputs
Spatial and temporal discrepancy between modelled buffer and actual front: the modelled
buffers exceeded the actual fire front by up to 126 m (1-h buffer) and 1400 m (3-h
buffer), i.e. the buffers were conservative.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Forecast wind is usable as an input; forecast *error* is not separately characterised.

## Validation
This is the validation paper of the classical lineage — retrospective comparison against
an observed fire, and the conclusion that WUIVAC "would have likely been successful."

## Limitations
One fire, one community. Error is reported as a distance discrepancy, not as a decision
consequence. No statement of how much forecast skill was needed.

## WildfireGuardian overlap
Direct pressure on **WG-C-002 and WG-C-012**: this is forecast-driven protective-action
timing, published in 2011. It also gives the honest baseline that WildfireGuardian's
"tuned trigger comparator" (WG-C-006) must be at least as good as.

## WildfireGuardian difference
Larsen et al. report *spatial* buffer error (metres) for one event. WG-C-002 proposes a
boundary in forecast-quality space (skill x lead time x latency) at which forecast-aware
action beats a tuned positional trigger — a different axis entirely, and evaluated over a
scenario distribution rather than one fire. Larsen et al. never vary forecast quality.

## Novelty threat
**level: HIGH** for WG-C-001; **MODERATE** for WG-C-002/WG-C-012 (it uses forecasts but
does not treat forecast quality as the independent variable).

## Quotes / page references
Abstract: "The novel use of forecast winds yielded dynamic trigger buffers that varied
with changes in wind speed and direction." (abstract, Consensus record)

## Follow-up papers
kalogeropoulos2023kperil, kalogeropoulos2026ensemble.
