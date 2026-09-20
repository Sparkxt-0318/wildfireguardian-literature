# fluschnik2026decaying

## Citation
Fluschnik, T.; Pucic, A.; Renken, M. (2026). "Smooth Routing in Decaying Trees."
arXiv:2603.23504 [cs.DS]. **PREPRINT.**

## Publication status
PREPRINT. Not peer reviewed. Evidence level **E2 / `ABSTRACT_VERIFIED`**: the abstract was
reproduced verbatim from the arXiv abs page on 2026-09-20; the body was not read.

**Identifier caveat.** The abs page displays "[Submitted on 6 Feb 2026]", which does not match
the `2603` (March 2026) identifier prefix. Recorded as displayed, not reconciled. Resolve
before the record is cited anywhere.

## Abstract (verbatim)
> "Motivated by evacuation scenarios arising in extreme events such as flooding or forest
> fires, we study the problem of smoothly scheduling a set of paths in graphs where connections
> become impassable at some point in time. A schedule is smooth if no two paths meet on an edge
> and the number of paths simultaneously located at a vertex does not exceed its given capacity.
> We study the computational complexity of the problem when the underlying graph is a tree, in
> particular a star or a path. We prove that already in these settings, the problem is NP-hard
> even with further restrictions on the capacities or on the time when all connections ceased.
> We provide an integer linear program (ILP) to compute the latest possible time to evacuate.
> Using the ILP and its relaxation, we solve sets of artificial (where each underlying graph
> forms either a path or star) and semi-artificial instances (where the graphs are obtained from
> German cities along rivers), study the runtimes, and compare the results of the ILP with those
> of its relaxation."

## Outputs
"the latest possible time to evacuate", computed by an ILP.

## WildfireGuardian overlap
Occupies **WG-DBD-3** — the latest feasible start instant reported as *the* computed output —
in a graph-algorithms venue, for an evacuation problem explicitly motivated by forest fires,
with edges that "become impassable at some point in time" (**WG-DBD-5** in form: a path must
clear an edge before it ceases, which is a traversal constraint, not an entry test).

What it does not do:
- Paths are **outbound**; there is no inbound leg, no pickup, no dwell, no round trip.
- The times at which connections cease are **exogenous inputs**, not derived from a fire-spread
  model, and carry no uncertainty and no forecast.
- The output is a **single latest time**, not a set of feasible windows (WG-DBD-4 untouched).
- Congestion appears only as edge-exclusivity and vertex capacity, not as traffic.

## Why it matters anyway
It removes "computing a latest possible time rather than a route is itself the new move" from
WildfireGuardian's available sentences, in the same hazard family (forest fire evacuation), from
a field the program was not searching.

## Open
`NEEDS_FULL_TEXT`: whether the ILP's feasibility region is reported per origin (a per-village
latest time) or only globally. A per-origin report would also bear on WG-DBD-7's "map" framing.
