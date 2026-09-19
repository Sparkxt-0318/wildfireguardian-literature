# roysingh2025constellation

## Citation
Roy-Singh, S., Ravindra, V., Levinson, R., Moghaddam, M., Mandel, J., Kochanski, A., Farguell Caus, A., Nelson, K., Alkaee Taleghan, S., Kannan, A., & Melebari, A. (2025). *Optimal Planning and Machine Learning for Responsive Tracking and Enhanced Forecasting of Wildfires using a Spacecraft Constellation.* arXiv:2508.06687.

## Publication status
**PREPRINT** (arXiv). No DOI retrieved. Full text read via alphaXiv.

## Problem
How should a satellite constellation be tasked so that wildfire products reach firefighters "within latency
appropriate for time-critical applications"?

## Method
A Mixed Integer Program schedules joint observation collection and downlink across all satellites in NASA's
CYGNSS constellation (passive GNSS-R receivers, which see through cloud and smoke). ML-derived fire predictions
supply the target priorities that drive the planner objective. Retrieved soil moisture and burn predictions feed
USGS fire danger maps and the WRFx / WRF-SFIRE coupled forecasting system via fire arrival time.

## Data
CYGNSS observations; case studies on the Texas Smokehouse Creek fire, LA and CONUS fire dates.

## Outputs
- Planner collects **98-100% of available observation opportunities / science rewards**; 100% of active-fire
  targets and roughly 80-90% of pre-fire targets covered.
- **Expected observation-to-downlink latency < 24 h**; **end-to-end workflow latency 6-30 h**, against a current
  delivery time of "multiple days".
- CYGNSS inclusion boosts ML burn-prediction accuracy by 13%; high-resolution data adds another 15% recall.
- Solver: relaxed gap tolerance 1e-2 reached nearly the same reward in ~30 min as 1e-4 runs that timed out at 3 h.

## Key equations
Objective (their Eq. 1): a weighted sum of rewards for observed active-fire and pre-fire targets, with **active-fire
targets favoured by a factor of 10**, each target's reward counted only once even if imaged by several satellites.
Constraints tie target coverage to at least one covering image.

## Assumptions
- Target "reward" is a prioritisation value derived from fire danger / active-fire prediction.
- Storage and downlink buffers are the binding resources.

## Validation
Case studies; planner performance measured against available reward, not against any field outcome.

## Limitations
- The reward is a **proxy for scientific/monitoring value**. Nothing in the objective represents a consequence for
  a person, a community or a responder.
- 6-30 h end-to-end latency is far slower than an evacuation decision cycle. This is useful honesty for our
  latency table: the state of the art in *tasked* spaceborne fire observation is hours to a day, not minutes.

## WildfireGuardian overlap
The strongest existing instance of **decision-directed observation in wildfire** — observations are chosen, not
merely received — and it explicitly treats **latency as a designed quantity**, which touches WG-C-012.

## WildfireGuardian difference
Operational and precise: Roy-Singh et al. maximise a hand-weighted science reward (active fire x10). WildfireGuardian
would maximise the expected improvement in a protective-action decision — e.g. the probability that the
latest-safe-dispatch time is estimated correctly. Their weight of 10 is a modelling choice; ours would be derived
from a loss function over mission feasibility. If we cannot show those two produce different observation plans, the
distinction is rhetorical and WG-C-008 should be downgraded.

## Novelty threat
**HIGH for WG-C-008** (observation tasking for wildfire with an explicit objective already exists and is
NASA-scale) and **MODERATE for WG-C-012** (latency is budgeted, though not traded against decision value).

## Quotes / page references
Abstract: workflow has "an expected latency of 6-30h, improving on the current delivery time of multiple days".
Section on the MIP: the objective "is a weighted sum of the rewards for the active and pre-fire targets observed
which favors active fire targets by a factor of 10."
Results: "we expect observation-to-downlink latency to be <24h."

## Follow-up papers
- braydwood2026quantum (same problem, quantum solver).
- papaioannou2026adaptive (airborne, closed-loop, information-theoretic).
- mandel2014wrfsfire (the assimilation target).
