# yu2020disruption

## Citation
Yu, D., Yin, J., Wilby, R. L., Lane, S. N., Aerts, J. C. J. H., Lin, N., Liu, M., Yuan, H.,
Chen, J., Prudhomme, C., Guan, M., Baruch, A., Johnson, C. W. D., Tang, X., Yu, L., & Xu, S.
(2020). "Disruption of emergency response to vulnerable populations during floods."
*Nature Sustainability*. DOI: 10.1038/s41893-020-0516-7. Volume/issue/pages: UNVERIFIED.

## Publication status
`PEER_REVIEWED`, journal article, open access (BRONZE).
Abstract retrieved via Consensus record; full text NOT retrieved. Evidence level **E2**.

## Problem
Emergency responders must reach urgent cases within mandatory response times regardless of weather.
Flooding of the transport network adds minutes between dispatch and arrival. The paper asks how
much of the national emergency-response coverage is lost when the road network floods, and which
vulnerable sites become unreachable.

## Method
Explicit spatial modelling of the coverage of **all** Ambulance Service and Fire and Rescue Service
stations in England under flooding of varying severity, evaluated against mandatory
(compliant) response times. Hotspots of vulnerability are then identified — the paper names
**care homes, sheltered accommodation, nurseries and schools** specifically.

## Data
All ambulance and fire-and-rescue station locations in England; national road network; flood
scenarios of varying magnitude.

## Outputs
- Reduction in national-level compliance with mandatory response times as a function of flood
  magnitude, with much larger reductions in some urban agglomerations.
- Identification of "stranded sites" — vulnerable locations that fall outside compliant coverage.
- A policy finding: the sensitivity is underpinned by ambulance-service centralisation and
  fire-and-rescue decentralisation.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Hazard (flood depth/extent) is prescribed per scenario; travel time on flooded links is degraded.
Response standard is exogenous and fixed (a regulatory target, not a derived feasibility bound).

## Validation
Real national infrastructure data for England; scenario-based, not event-validated.

## Limitations
The modelled mission **ends at arrival**. There is no loading, no return leg, no destination
capacity, and therefore no round trip.

## WildfireGuardian overlap
This is the best published treatment found of **the inbound leg under a modelled hazard, aimed at
exactly WildfireGuardian's vulnerable sites**. It establishes, at national scale and in a top-tier
venue, that:
- hazard progression materially changes responder ingress travel time;
- that degradation concentrates on vulnerable sites (care homes, sheltered accommodation);
- and that responder *reachability* is therefore a hazard-dependent quantity, not a fixed one.

That is the empirical premise WG-C-003 rests on, already published.

## WildfireGuardian difference
- **Hazard.** Flood, not wildfire. Flood inundation is largely static within an event; a wildfire
  front moves, so the binding constraint is an *arrival-time* field rather than a depth field.
  (This is a genuine structural difference, not a cosmetic one — but it is a difference of hazard
  physics, which WildfireGuardian explicitly does **not** claim to contribute, per PROJECT_CONTEXT.)
- **Mission.** Yu et al. measure arrival against an externally imposed regulatory standard
  (e.g. an 8-minute ambulance target). WildfireGuardian derives the bound from *mission feasibility*:
  ingress + pickup dwell + egress must all complete before fire arrival on each leg. Yu et al.
  never model pickup or egress.
- **Output.** Coverage/compliance fraction vs. a latest-dispatch time.
- **Decision.** Yu et al.'s decision is strategic (where to site stations, how to write contingency
  plans). WildfireGuardian's is tactical and per-incident (when to send this vehicle).

## Novelty threat
**level: HIGH**
- **WG-C-003** → `WEAKENED`. The "nobody models the inbound leg under a hazard" half of the
  argument is false: Yu et al. did it at national scale in *Nature Sustainability*. What remains is
  the round-trip closure and the deadline, which Yu et al. do not address.
- Also a **useful** citation: it is strong, independent, top-venue evidence that the inbound leg is
  a real and consequential constraint — which is exactly what a judge will ask WildfireGuardian to
  justify.

## Quotes / page references
From the retrieved abstract:
- "flooding of transport networks can add critical minutes to travel times between dispatch and
  arrival" (Abstract).
- "hotspots of vulnerability (such as care homes, sheltered accommodation, nurseries and schools)"
  (Abstract).
- "Natural disasters can obstruct first responders when and where they are needed most."
  (Editor's summary line).

## Follow-up papers
- Johnson, S., Wilby, R., Yu, D., & Matthews, T. (2022), EGU abstract
  (doi:10.5194/egusphere-egu22-5214) — global analysis of emergency service provision to vulnerable
  populations under flooding and climate change. Conference abstract only.
- Forward citation search on this paper for any **wildfire** analogue is an open task —
  see `novelty/OPEN_QUESTIONS.md`.
