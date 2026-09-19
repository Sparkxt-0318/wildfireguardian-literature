# cova2005trigger

## Citation
Cova, T. J.; Dennison, P. E.; Kim, T. H.; Moritz, M. A. (2005). "Setting Wildfire
Evacuation Trigger Points Using Fire Spread Modeling and GIS." *Transactions in GIS*
9(4): 603–617. DOI 10.1111/j.1467-9671.2005.00237.x

## Publication status
PEER_REVIEWED (journal article). Open-access status UNKNOWN.
Evidence level E2 — abstract retrieved via Consensus; metadata verified via Crossref API.
Full text NOT retrieved.

## Problem
An incident commander must decide *who* evacuates, *when*, and under what order type,
while a fire is advancing. The paper asks how to convert a fire-spread model into a
spatial object a commander can act on.

## Method
Minimum-travel-time fire spread over a raster of wind, topography and fuel. Given an
estimated evacuation time supplied by the decision maker, the method computes the set of
landscape points from which the fire would take exactly that long to reach the community.
That level set is the **trigger buffer**. Implemented in GIS.

## Data
Corral Canyon section of the 1996 Calabasas Fire, Malibu, California, USA. Wind,
topography and fuel layers (specific products NOT verified — NEEDS_FULL_TEXT).

## Outputs
A single closed polygon (trigger buffer) per community per weather assumption. The
decision rule is binary: fire crosses the edge → recommend evacuation.

## Key equations
NEEDS_FULL_TEXT. From the abstract the construction is a level set of modelled fire
travel time equal to the estimated evacuation time; the specific minimum-travel-time
formulation was not retrieved.

## Assumptions
- Evacuation time is an exogenous input from a decision maker, not modelled.
- A single deterministic weather/fuel state.
- The protected subject is a community, treated as a point/area, not as households.
- The protective action is one-way egress.

## Validation
Case-study demonstration only; no retrospective skill assessment in this paper. (That
arrives with larsen2011cedar.)

## Limitations
No traffic. No uncertainty quantification. No responders. Evacuation time is an
unexamined scalar. The buffer is as good as the single weather scenario chosen.

## WildfireGuardian overlap
This is the paper that invented "model the future fire in order to time a protective
action." It is the direct and sufficient reason **WG-C-001 is REJECTED** and must never
be spoken.

## WildfireGuardian difference
Cova et al. compute a *distance/level-set* object whose decision subject is a community
performing one-way egress, with evacuation time given. WG-C-003 computes a *time*
(latest fire-relative dispatch instant) whose decision subject is a responder unit
performing a three-leg round trip, with the trip time endogenous and fire-feasibility
enforced on the inbound leg. Different units, different subject, different constraint set.

## Novelty threat
**level: CRITICAL** — kills WG-C-001 outright. Background/foundational for WG-C-003.

## Quotes / page references
Abstract: "a trigger buffer can be computed for a community whereby an evacuation is
recommended if a fire crosses the edge of the buffer." (abstract, Consensus record)

## Follow-up papers
dennison2007wuivac, larsen2011cedar, fryer2013entrapment, li2015household, li2018coupling,
mitchell2023peril.
