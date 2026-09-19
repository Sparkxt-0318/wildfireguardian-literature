# alexander2026nursing

## Citation
Alexander, N., Tannenbaum, M., & Noennig, J. (2026). "Operational Decision Support for Evacuating
Nursing Home Residents: A Hamburg Benchmark and Metaheuristic Comparison Under a 5-Minute Time
Budget." In *Proceedings of the Genetic and Evolutionary Computation Conference* (GECCO '26),
pp. 1029–1037. DOI: 10.1145/3795095.3805113.

## Publication status
`PEER_REVIEWED` **conference** paper (GECCO). Not a journal article — this matters for how it is
described, not for how thoroughly it occupies a claim (NOVELTY_STANDARD §3.3). Open access
(HYBRID). Full abstract retrieved; body NOT retrieved.

## Problem
Evacuating **mobility-impaired nursing home residents** during urban emergencies, where the task is
routing and scheduling a heterogeneous vehicle fleet under minute-level deadlines, and where a
usable answer must be produced fast enough to be operational.

## Method
Defines the **Nursing Home Evacuation Vehicle Routing Problem (NH-Evac-VRP)** with:
open-ended multi-trip shuttling, split pickups, **load-dependent service times**, and shelter
capacities. A hard **300 s single-thread** compute budget is part of the problem definition.
Compares a constructive dispatcher baseline against a Genetic Algorithm, a Memetic Algorithm, and
Adaptive Large Neighborhood Search. Objective: demand-weighted average waiting time and makespan,
with a shelter-overfill penalty.

## Data
Releases the **Hamburg-NH-Evac benchmark**: two expert-specified real scenarios —
(i) unexploded-ordnance exclusion-zone evacuation in Altona-Altstadt (479 evacuees, one shelter),
(ii) storm-surge evacuation in Wilhelmsburg (510 evacuees, three shelters) — plus a synthetic stress
test (1,348 evacuees, five shelters). Real facility data and asymmetric road-network travel times.

## Outputs
Schedules and routes; comparative metaheuristic performance (no method dominates: ALNS best makespan
in two configurations, MA best in three, beating ALNS by 27 min in the synthetic mass-transit case);
a web-based decision support system for scenario configuration, optimisation, and schedule
visualisation.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Travel times are asymmetric but static — the hazard does not progress across the road network during
the run. Deadlines are minute-level and externally specified.

## Validation
Real facility data and expert-specified scenarios; no real evacuation.

## Limitations
No hazard progression. The two real hazards (an ordnance exclusion zone and a storm surge) are both
effectively static in extent during the operation, so the formulation never needed a moving front.

## WildfireGuardian overlap
- **Load-dependent service times** is the pickup-dwell term (`t_pickup`) that CURRENT_THESIS RQ2
  lists as one of three legs. It is already a modelled, named component of an established VRP
  variant.
- **Open-ended multi-trip shuttling** — vehicles do not return to a depot between trips — matches
  Moradi et al.'s no-return-to-depot feature and further erodes any claim to novelty in the
  round-trip structure.
- Mobility-impaired residents of care facilities as the served population.
- An explicit **operational compute budget** — a rigour dimension WildfireGuardian has not claimed
  and should consider, because a deadline computed in 20 minutes is useless at a 15-minute deadline.

## WildfireGuardian difference
- No fire. No hazard progression on any leg. The deadlines are exogenous.
- The objective is throughput (waiting time, makespan), not a feasibility boundary.
- No forecast and no uncertainty.

## Novelty threat
**level: HIGH**
- **WG-C-005** → contributes to `OCCUPIED`; a 2026 peer-reviewed paper naming and benchmarking a
  dedicated VRP variant for non-ambulatory care-facility residents.
- **WG-C-011** → `OCCUPIED`; five scenario-fleet configurations compared is scarce-resource
  allocation, and the paper shows the allocation regime changes which algorithm wins.
- **WG-C-003** → weak direct threat, strong indirect: the pickup-dwell and multi-trip components are
  standard, so WG-C-003's novelty cannot rest on "we model the pickup dwell."

## Quotes / page references
From the retrieved abstract:
- "Evacuating mobility-impaired nursing home residents during urban emergencies requires routing and
  scheduling heterogeneous vehicles under minute-level deadlines." (Abstract).
- "with open-ended multi-trip shuttling, split pickups, load-dependent service times, and shelter
  capacities" (Abstract).
- "solutions must be produced within a hard 300 s single-thread budget" (Abstract).

## Follow-up papers
- Moradi, Sauré & Patrick (2026) — the wildfire counterpart with hazard-derived arc windows.
- Xu, Wang, Chen & Lin (2022), *IEEE Access* 10:36073–36090 — heterogeneous fleet matched to
  individual mobility class.
- Bish (2011), *OR Spectrum* 33(3):629–654 — bus-based evacuation with risk-determined
  location-specific last-pickup times.
