# ma2025damaged

## Citation
Ma, F.; Lee, J. Y. (2025). "Analyzing wildfire evacuation dynamics with agent-based
modeling in damaged road networks." *Safety Science* 187: 106835.
DOI 10.1016/j.ssci.2025.106835
Earlier preprint: SSRN, DOI 10.2139/ssrn.4871791 (2024), same authors and title.

## Publication status
PEER_REVIEWED (journal article). OA UNKNOWN.
Evidence level E2/E3 — Crossref metadata verified for both the journal article and its
SSRN precursor; **abstract not retrieved in full**. Description below is from a web-search
summary of the publisher page and must be confirmed. `NEEDS_FULL_TEXT`.

## Problem
Most wildfire evacuation models run on an intact road network. Real wildfire evacuations
run on a network that the fire is actively destroying.

## Method
(Per publisher-page summary, E3.) A framework integrating wildfire simulation with road
network vulnerability assessment and agent-based modelling, with microscopic traffic
simulation on a dynamically degrading network.

## Data
NOT VERIFIED.

## Outputs
(Per summary, E3.) Effect of fire-induced road closures on community evacuation time, and
on the risk of agents being trapped inside the fire zone.

## Key equations
NOT VERIFIED.

## Assumptions
NOT VERIFIED beyond "fire closes roads during the run."

## Validation
NOT VERIFIED.

## Limitations
NOT VERIFIED. From the framing: outbound evacuees only; no responder ingress.

## WildfireGuardian overlap
Supplies the mechanism WG-C-003 depends on — **a link becomes impassable at a
fire-model-derived arrival time, and the agent on it may be trapped** — but applies it only
to outbound self-evacuees. It is also second prior art for the rejected WG-C-001.

## WildfireGuardian difference
Ma & Lee report the *consequence* of network damage (longer clearance, more entrapment).
WG-C-003 uses the same mechanism as a *feasibility constraint* on a responder's inbound
leg and inverts it to solve for a departure time. The quantity differs: simulated outcome
distribution vs. latest-safe-dispatch instant.

## Novelty threat
**level: HIGH** for WG-C-001 and WG-C-009; **MODERATE** for WG-C-003 (mechanism occupied,
direction and quantity not).

## Quotes / page references
None. No verbatim abstract text was retrieved; nothing here may be quoted as the authors'
own words.

## Follow-up papers
beyki2026modular (same dynamic-closure mechanism, extended to inbound).
