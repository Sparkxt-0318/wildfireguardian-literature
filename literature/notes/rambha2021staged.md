# rambha2021staged

## Citation
Rambha, T., Nozick, L. K., Davidson, R., Yi, W., & Yang, K. (2021). "A stochastic optimization
model for staged hospital evacuation during hurricanes." *Transportation Research Part E: Logistics
and Transportation Review*, 151, 102321. DOI: 10.1016/j.tre.2021.102321.

## Publication status
`PEER_REVIEWED`, journal article, CLOSED access. Abstract retrieved in full via Semantic Scholar;
body NOT retrieved. Evidence level **E2**. `NEEDS_FULL_TEXT`.

## Problem
Whether and when to evacuate a hospital before a hurricane. The paper frames this as the hard case:
a hospital is itself a refuge, moving patients degrades care, and hurricane track and intensity are
uncertain — so most emergency response plans contain no clear evacuate-or-shelter guideline.

## Method
Stochastic optimization with **recourse** over the evolving storm. The formulation takes in
successively revised flood, wind, and roadway-traffic predictions and determines the **order in
which patients should be evacuated over time**, trading off cost against risk. The headline
methodological point is that a recourse formulation which adapts to new forecast information
outperforms one that commits up front.

## Data
North Carolina; Hurricane Isabel; a "holistic case study" fusing data and model outputs from
multiple sources (storm, flood, wind, traffic).

## Outputs
An adaptive, forecast-stage-indexed evacuation ordering policy for patients, with a cost–risk
trade-off; demonstration of the value of recourse.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Forecast evolution is representable as a scenario tree. Transport capacity is available when
called for (the paper's decision is sequencing, not vehicle ingress feasibility).

## Validation
Retrospective case study on a real storm, not a controlled comparison against a tuned baseline.

## Limitations
The inbound leg is not the object of study — the binding physical constraint modelled is flooding
and wind at the facility and on the roadway, not whether a specific vehicle can still reach a
specific facility and get back out.

## WildfireGuardian overlap
This is the closest published work to WildfireGuardian's **conceptual frame**, and it is closer on
the frame than anything found in the wildfire literature:
- Non-self-evacuating people (hospital patients).
- A decision about **timing under forecast uncertainty**, not about routes.
- Explicit use of *evolving* hazard predictions, with the value of adapting to new information as a
  reported result. That is a forecast-value argument in all but name.
- The decision is "act now or wait," exactly WildfireGuardian's RQ1 decision variable.

If a judge asks "hasn't someone already done protective-action timing under forecast uncertainty for
people who cannot evacuate themselves?", **this is the paper they mean**, and the answer must be
"yes, for hospital patients and hurricanes, by Rambha et al. (2021)."

## WildfireGuardian difference
- **Output shape.** Rambha et al. produce a *policy* over a scenario tree — an ordering that adapts
  as the storm evolves. WildfireGuardian proposes a *scalar deadline* per mission, fire-relative,
  with a reported sensitivity surface. A policy and a deadline are not the same object and support
  different operational uses.
- **The comparator.** Rambha et al. compare recourse against a non-adaptive formulation. That is
  *not* the tuned positional-trigger comparator that CURRENT_THESIS RQ1 makes non-negotiable. This
  is a real remaining difference for WG-C-002/WG-C-006 — but it is a difference in evaluation
  rigour, and NOVELTY_STANDARD §2 classes that as N3-weak.
- **The mission.** No responder ingress, no pickup dwell, no round trip. The vehicle's own
  feasibility against the hazard is not modelled.
- **Hazard.** Hurricane, with 30–72 h lead times. Wildfire dispatch deadlines are minutes-to-hours
  quantities; the latency term WildfireGuardian cares about (WG-C-012) is negligible at hurricane
  lead times and potentially decisive at wildfire lead times. **This is WildfireGuardian's best
  substantive argument for why the wildfire instantiation is not a transposition.**

## Novelty threat
**level: HIGH**
- **WG-C-003** → `WEAKENED`. The "timing decision for people who cannot self-evacuate, under an
  evolving hazard forecast" territory is occupied in the hurricane/health-facility domain.
- **WG-C-005** → contributes to `OCCUPIED`.
- **WG-C-011** → contributes to `OCCUPIED` (patient sequencing under scarce transport is
  allocation).
- Cross-category warning for **WG-C-002 / WG-C-012**: this paper demonstrates forecast value for a
  protective-action decision. Category 4 (forecast value) should treat it as in-scope.

## Quotes / page references
From the retrieved abstract:
- "the decision of whether or not to evacuate hospitals in these emergencies" (Abstract).
- "Most emergency response plans do not have clear guidelines for evacuating or sheltering-in-place."
  (Abstract).
- "determines the order in which patients should be evacuated over time based on the evolution of
  the storm by trading off cost and risk" (Abstract).
- "the advantages of using a recourse formulation that adapts to new information" (Abstract).

## Follow-up papers
- Kim, K. Y., Toplu-Tutay, G., Kutanoglu, E., & Hasenbein, J. J. — "A Stochastic Optimization Model
  for Patient Evacuation from Health Care Facilities During Hurricanes" (SSRN abstract 4704899);
  and the associated "Integrated Flood Prediction and Stochastic Optimization" line of work
  (seminar records at UT Knoxville and U Houston). **This couples a physics-based flood prediction
  model to multi-facility hospital/nursing-home evacuation logistics, including staging-area
  location and EMS vehicle positioning — RETRIEVE AND ASSESS. Potentially HIGH or CRITICAL.**
- HURREVAC — operational tool that computes an evacuation start-time *range* by subtracting
  clearance time from earliest-reasonable and most-likely hazard-onset times. This is the closest
  **operational practice** analogue to a dispatch-by deadline and must be documented; it is a
  government/operational tool, not peer-reviewed research.
