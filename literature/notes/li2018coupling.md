# li2018coupling

## Citation
Li, D.; Cova, T. J.; Dennison, P. E. (2019). "Setting Wildfire Evacuation Triggers by
Coupling Fire and Traffic Simulation Models: A Spatiotemporal GIS Approach."
*Fire Technology* 55(2): 617–642. DOI 10.1007/s10694-018-0771-6
(Online first 2018-09-06; issue year 2019.)

## Publication status
PEER_REVIEWED (journal article). OA UNKNOWN. Evidence level E2 (abstract only).

## Problem
Every prior trigger model took *evacuation time* as an expert-judgement input. That input
is the single largest lever on buffer size and it was never modelled.

## Method
Three steps inside a spatiotemporal GIS: (1) estimate total community evacuation
(clearance) time with a **traffic simulation**; (2) run the simulation repeatedly to
obtain a **cumulative probability distribution** over clearance times and generate
**probability-indexed trigger buffers**; (3) evaluate the buffers by co-simulating fire
perimeters and evacuation traffic to see how the two interact spatially.

## Data
Julian, California, USA. Two travel-demand scenarios (baseline and doubled demand).

## Outputs
Buffers labelled by the probability that the evacuation completes before fire arrival.
Reported: 160 min to guarantee 95% of residents reach safety in one scenario; 292 min when
travel demand is doubled.

## Key equations
NEEDS_FULL_TEXT (the mapping from the clearance-time CDF to the buffer level set is the
equation that matters for us).

## Assumptions
- Demand and departure timing are scenario inputs.
- All evacuees are self-evacuating drivers.
- Fire spread deterministic; the probability is over *evacuation time*, not over fire.

## Validation
Scenario comparison rather than event validation.

## Limitations
The probability is one-sided: the fire is a single deterministic realisation, only traffic
is stochastic. No responders. No inbound movement.

## WildfireGuardian overlap
Serious. This is the closest published object to "a probabilistic, traffic-aware,
percentile-indexed trigger." It is prior art for **WG-C-004** from the traffic side, and
it is the natural strong comparator that **WG-C-006** demands — a *tuned* buffer whose
lead time is derived from a simulated clearance-time distribution rather than guessed.

## WildfireGuardian difference
Li et al. randomise the evacuation and fix the fire; WildfireGuardian proposes to
randomise the fire (ensemble/forecast) as well, and to evaluate a *responder round trip*
rather than aggregate community clearance. Their percentile is over clearance time and is
reported as a distance; WG-C-003's output is a time-to-dispatch.

## Novelty threat
**level: CRITICAL** for WG-C-004 and WG-C-006; HIGH for WG-C-001.
Practical consequence: WG-C-006 must be stated as "we adopt the Li et al. (2019) style of
simulation-derived, percentile-indexed buffer *as our baseline*," never as our invention.

## Quotes / page references
Abstract: "derives the cumulative probabilities for distinct evacuation times ... and
generates corresponding probability-based trigger buffers." (abstract, Consensus record)

## Follow-up papers
mitchell2023peril, kalogeropoulos2023kperil, wahlqvist2021wuinity.
