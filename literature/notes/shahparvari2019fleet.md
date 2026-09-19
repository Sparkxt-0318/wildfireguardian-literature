# shahparvari2019fleet

## Citation
Shahparvari, S., Abbasi, B., Chhetri, P., & Abareshi, A. (2019). "Fleet routing and scheduling in
bushfire emergency evacuation: A regional case study of the Black Saturday bushfires in Australia."
*Transportation Research Part D: Transport and Environment*, 67, 703–722.
DOI: 10.1016/j.trd.2016.11.015.

Note: Crossref gives the issue year as 2019 (vol. 67, pp. 703–722); Semantic Scholar lists 2017 for
the online-first record. **Year discrepancy is real — cite the Crossref issue year and be ready to
explain it.**

## Publication status
`PEER_REVIEWED`, journal article, CLOSED access. Full abstract retrieved via Semantic Scholar;
body NOT retrieved. Evidence level **E2**.

## Problem
Emergency-service response to a **short-notice** bushfire evacuation of **late evacuees** — people
still in the fire-affected area who did not or could not leave, and who must now be collected by
rescue vehicles and taken to shelters.

## Method
Vehicle Routing Problem (VRP) model with time windows and road-disruption risk. Determines
simultaneously: the number of rescue vehicles required, the safest routes, and the vehicle
schedules. A heuristic solution method handles the operational interdependencies.

## Data
Parameters derived from the 2009 Black Saturday bushfires, Victoria, Australia. Case instance:
1,100 late evacuees, four shelters, seven rescue vehicles.

## Outputs
- Required number of vehicles.
- Safest (low-risk) routes and schedules for late evacuees.
- Feasibility result: all 1,100 late evacuees can be evacuated via low-risk routes within the
  available resources.
- Sensitivity: evacuation can be compromised when the hard time-window constraints are changed.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Shelters are pre-established. Fire-impacted route availability is **not explicitly modelled**;
instead reliability scores are assigned to routes (this characterisation is taken from the
literature review in Moradi et al. 2026, §2, which reviews this paper directly). Time windows are
inputs.

## Validation
Retrospective parameterisation on a real, catastrophic fire; no forward validation.

## Limitations
The fire is present as scenario parameterisation and route-risk scores, not as a progression model.
The time window is the input whose variation is studied, never the output that is computed.

## WildfireGuardian overlap
This is the founding paper of the **bushfire assisted-evacuation VRP lineage** and it establishes,
in wildfire, that:
- "late evacuees" (functionally, residents who did not self-evacuate) are collected by rescue
  vehicles and delivered to shelters;
- this is modelled as a routing-and-scheduling problem with **time windows and fire-related route
  disruption risk**;
- the number of vehicles required is a computed output (WG-C-011 territory);
- and the answer is **sensitive to the hard time window**, which the authors explicitly
  sensitivity-analyse.

That last point is the closest any pre-2026 wildfire paper comes to WG-C-003: it asks
"what happens as the window tightens?" — but the window remains exogenous.

## WildfireGuardian difference
- The time window is *varied as a what-if input*; it is never *derived* from a modelled fire, and
  the paper does not report a critical window value at which feasibility is lost as its headline
  quantity.
- No inbound-leg fire-arrival constraint (route risk is a static reliability score, not an
  arrival-time field).
- No forecast, no uncertainty in the fire's future position, no latency.
- Output is a plan and a feasibility verdict; WildfireGuardian's output is a time.

## Novelty threat
**level: HIGH**
- **WG-C-005** → `OCCUPIED`. Assisted wildfire evacuation of people who did not self-evacuate was
  modelled in this lineage a decade before WildfireGuardian.
- **WG-C-011** → `OCCUPIED`. "computes the required number of vehicles" is resource allocation, and
  the resource-disruption sensitivity in the companion paper (shahparvari2016enhancing) goes further.
- **WG-C-003** → threatens the framing but not the quantity.

## Quotes / page references
From the retrieved abstract:
- "identifies the safest routes and schedules for late evacuees under various time windows and road
  disruption risk" (Abstract).
- "the feasibility of evacuating 1100 late evacuees via low risk routes within the available
  resources of four shelters and seven rescue vehicles" (Abstract).
- "could be potentially affected when the hard constraints such as the time-window are changed"
  (Abstract).

## Follow-up papers
- Abbasi, Shahparvari & Chhetri (2015), IEEE IEEM — earliest version of the model.
- Shahparvari, Chhetri, Abbasi & Abareshi (2016), *TR-E* 93:148–176 — multi-objective version with
  resource-disruption sensitivity.
- Shahparvari, Abbasi & Chhetri (2017), *Omega* 72:96–117 — possibilistic (fuzzy) uncertainty.
  **Abstract not retrieved — NEEDS_FULL_TEXT.**
- Shahparvari & Abbasi (2017), *TR-A* 104:32–49 — robust stochastic version with uncertain
  population, time windows, and bushfire propagation.
- Moradi, Sauré & Patrick (2026) — positions itself explicitly against this lineage.
