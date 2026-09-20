# phillips2011sipp

## Citation
Phillips, M.; Likhachev, M. (2011). "SIPP: Safe interval path planning for dynamic
environments." *2011 IEEE International Conference on Robotics and Automation (ICRA)*,
pp. 5628–5635. DOI 10.1109/ICRA.2011.5980306.

## Publication status
PEER_REVIEWED conference paper (ICRA). Evidence level **E4 / `METHODS_VERIFIED`** — the
author-hosted PDF was retrieved on 2026-09-20 and Section III (ALGORITHM) and Fig. 5
(`getSuccessors`) were read directly. Quotations below are verbatim from that PDF.

## Problem
Plan a collision-free path for a robot among dynamic obstacles whose future trajectories are
given, without paying the cost of adding a full time dimension to the search space.

## The two definitions that matter here (verbatim)
> "We define a safe interval as a contiguous period of time for a configuration, during which
> there is no collision and it is in collision one timestep prior and one timestep after the
> period."

> "Each spatial configuration ... has a timeline ..., which is just an ordered list of
> intervals, alternating between safe and collision."

> "Then for each of the time intervals in this new configuration, we generate a successor with
> the earliest possible arrival time that does not have any collisions along the motion."

## Method
A* over states `(configuration, safe interval)` rather than `(configuration, timestep)`. The
number of safe intervals at a configuration "is at most the number of dynamic obstacles whose
trajectories intersect in that configuration", so the search space collapses relative to a
time-expanded graph. Successor generation uses "wait and move" actions: wait the minimal time
so that the move lands in the target safe interval as early as possible.

## Data
Simulation with up to 200 dynamic obstacles; comparison against HCA*; real trials on the PR2.

## Outputs
A time-parameterised path minimising arrival time. **Earliest** arrival, never a latest
departure.

## WildfireGuardian overlap
Two WildfireGuardian components exist here as 2011 robotics method, in a hazard-free setting:

- **WG-DBD-4 (feasible windows as a SET, possibly non-monotone).** The "timeline ... alternating
  between safe and collision" *is* the representation. A configuration blocked, then free, then
  blocked again is the normal case, not an exception. Any claim that representing feasibility as
  a set rather than a single deadline is novel *as a representation* is false.
- **WG-DBD-5 (hazard over the whole traversal).** "no collisions along the motion" is an
  explicit traversal-interval check, not an entry check.

What it does not do: no hazard model (obstacle trajectories are given), no mission with legs,
no service time, no dispatch decision, no latest-departure quantity, no uncertainty over the
obstacle prediction (see `kemisetti2026stochsipp` for that), and nothing fire-related.

## The honest reading
WG-DBD-4 and WG-DBD-5 are **method-occupied in robotics**. What is not occupied by SIPP is
their *use*: nobody in this lineage asks when a vehicle must be sent so that a two-leg mission
with a dwell still closes under a modelled wildfire. WildfireGuardian should cite SIPP as the
representation it adopts, and must not present the representation as its own.
