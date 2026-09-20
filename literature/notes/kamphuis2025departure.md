# kamphuis2025departure

## Citation
Kamphuis, R.; Levering, N.; Mandjes, M. (2025). "Optimal departure-time advice in road
networks with stochastic disruptions." *Computers & Operations Research* 183: 107148.
DOI 10.1016/j.cor.2025.107148.
Preprint: arXiv:2208.14516 [math.OC], submitted 30 Aug 2022, title spelled
"Optimal departure time advice in road networks with stochastic disruptions".

## Publication status
PEER_REVIEWED journal article (the arXiv item is the preprint of the same work).
Evidence level **E2 / `ABSTRACT_VERIFIED`**. The abstract below was reproduced verbatim
from the arXiv abs page on 2026-09-20. **The journal full text was not retrieved**, and the
published abstract was not compared against the preprint abstract. Everything below the
abstract is inference from the abstract and is marked as such.

## Problem
A traveller wants to arrive on time at a destination over a road network whose link travel
times are both time-dependent (recurrent patterns) and random (non-recurrent disruptions),
while not spending an excessive travel-time budget.

## The quantity (verbatim)
> "The focus of this paper lies on determining their optimal departure time: the latest time
> of departure for which a chosen on-time arrival probability can be guaranteed."

That sentence is WG-DBD-3's output quantity, probability-indexed, named as the paper's
focus — in an OR journal, on a road network.

## Method
(From the abstract, E2.) A Markovian background process tracks events affecting driveable
speeds on links, giving a per-link travel-time distribution conditional on the process state
at departure. A "computationally efficient algorithm" composes these link distributions into
the optimal departure time for a given path or origin–destination pair. An **online** variant
issues departure-time updates while the traveller is still at the origin, because network
conditions may change between request and advised departure.

## Data
Numerical experiments on "an existing road network -- the Dutch highway network". Instance
sizes, horizons and disruption parameters NOT VERIFIED.

## Outputs
A departure time (and, online, a revised departure time). No route is the headline output;
the path or OD pair is an input.

## Key equations
NOT VERIFIED — full text not retrieved.

## Assumptions
NOT VERIFIED beyond: Markovian background process; on-time arrival probability chosen by the
user; link travel-time distributions conditionally evaluable.

## Validation
Numerical experiments only, per the abstract. No field trial claimed.

## WildfireGuardian overlap
**This is the strongest published occupation of the "latest feasible departure instant as the
reported operational quantity" component (WG-DBD-3) found by this agent**, and its online
variant occupies WG-DBD-6 in form: the advice is conditioned on the state observable at the
time of advice, not on oracle future knowledge.

What it does **not** do, stated operationally:
- The mission is a **single one-way trip**. There is no second leg, so no round trip can fail
  because the *return* becomes infeasible after the outbound leg succeeds.
- The uncertainty is a **Markovian incident process on link speeds**, not a spreading hazard
  with a spatial arrival-time field. Disruptions raise travel time; they do not make a link
  permanently impassable at a modelled fire-arrival time, and they do not threaten the
  traveller.
- There is **no service/dwell term** and no person collected.
- Feasibility is monotone in the relevant sense: the paper reports *the* latest departure
  time, a scalar, not a set of disjoint feasible windows (WG-DBD-4 is untouched).

## Consequence for the registry (recommended, not applied)
WG-C-003's difference statement may no longer be "we compute a latest departure time and
others compute routes." It must become a statement about the **mission structure and the
hazard model**, because the latest-departure-time *quantity* is occupied.

## Open
`NEEDS_FULL_TEXT`: does the paper's online variant compute the set of departure times that
remain feasible after each update, or only the single current best? If the former, it also
touches WG-DBD-4.
