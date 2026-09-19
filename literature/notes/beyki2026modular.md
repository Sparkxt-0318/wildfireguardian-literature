# beyki2026modular

## Citation
Beyki, S. M., Patricio, A. S., Lopes, A. G., Santiago, A., & Laím, L. (2026). "A modular
agent-based framework for wildfire evacuation: Integrating fire spread, multimodal transport, and
dynamic routing." *Safety Science*, 199, 107200. DOI: 10.1016/j.ssci.2026.107200.

## Publication status
`PEER_REVIEWED`, journal article. Open access (Unpaywall/Semantic Scholar report HYBRID, CC-BY).
**Full text NOT retrieved** — ScienceDirect returned HTTP 403 to this agent. All content below is
from the structured abstract and publisher highlights. Evidence level **E2**. `NEEDS_FULL_TEXT`.

## Problem
Wildfire evacuation in the WUI, where the authors name four gaps in existing models:
limited dynamic rerouting when roads are compromised; insufficient representation of multimodal
evacuation; weak integration of high-resolution fire-spread data; and — the one that matters here —
**"the lack of inbound traffic and rescue operations."**

## Method
Modular agent-based framework combining, in one model: fire spread (a high-resolution wildfire
model), pedestrian movement, and vehicle traffic. Fire-driven road-segment closures dynamically
update network availability during the evacuation run. A custom **waypoint-based routing algorithm
enables adaptive rerouting for outbound *and inbound* evacuation**. Agent classes explicitly
represented: pedestrian movement, private vehicle, **emergency extraction**, and
vehicle–pedestrian interaction.

A secondary search result (WebSearch, not the paper itself) described a mechanism of "determining
safe time remaining for evacuation routes based on fire arrival time for each waypoint on the route,
where the safe time remaining is the least of the fire arrival times." This is attributed here only
tentatively and must be confirmed against the full text before being cited.

## Data
WUI case study in Portugal. Publicly available datasets throughout (a stated design goal for
transferability).

## Outputs
Evacuation times; route availability under advancing fire; scenario / "what-if" analyses for
evacuation planning. **No deadline or dispatch-time quantity is reported in the abstract.**

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
NEEDS_FULL_TEXT. Known: modular design, publicly available datasets, high-resolution fire spread
coupled to route availability.

## Validation
Validated against a real evacuation drill, "showing strong agreement in evacuation times."
This is stronger empirical grounding than most of the assisted-evacuation optimisation literature.

## Limitations
Not retrievable from the abstract. Note that a validated *simulation* of inbound rescue is not the
same as an optimisation that solves for the latest feasible dispatch; whether the framework can
be run backwards to produce a deadline is exactly the open question.

## WildfireGuardian overlap
**This is the only work found that couples a modelled, progressing fire to an explicit inbound
responder leg.** Specifically:
- Fire spread model coupled to network availability, updating during the run (WildfireGuardian's
  "modelled future fire" on the network).
- Inbound rescue operations and emergency extraction as first-class agent behaviours
  (WildfireGuardian's `t_ingress`).
- Adaptive rerouting for inbound legs when roads are compromised by fire (fire-arrival feasibility
  on the inbound leg).
- Drill validation in a real WUI community.

Where Moradi et al. (2026) own the *optimisation formulation* of the assisted round trip with
fire-arrival windows, Beyki et al. own the *simulation of the inbound leg against a modelled fire*.
Between the two of them, most of what WG-C-003 assumed was unclaimed territory is claimed.

## WildfireGuardian difference
- **Direction of the computation.** Beyki et al. simulate forward: given a dispatch, what happens?
  WildfireGuardian proposes to solve backward: given that the mission must close, how late may
  dispatch be? A simulator that can answer "did this rescue succeed" does not by itself report the
  latest departure time; that requires a search or root-find over dispatch time, which the abstract
  does not describe.
- **Decision subject.** Beyki et al.'s reported outputs are community-level evacuation times and
  operational consistency. WildfireGuardian's reported output is a per-resident, per-responder
  time-to-dispatch.
- **Uncertainty.** No ensemble, forecast error, skill, or latency treatment appears in the abstract.

**This difference must be verified against the full text before it is spoken to a judge.** If the
paper reports a latest-feasible-extraction time anywhere, WG-C-003 moves to `OCCUPIED`.

## Novelty threat
**level: CRITICAL** (provisionally; CRITICAL on the strength of the inbound-rescue + coupled-fire
combination, pending full text)
- **WG-C-003** → threatens the inbound-leg component directly. Currently `WEAKENED` rather than
  `OCCUPIED` only because no deadline output is evidenced.
- **WG-C-005** → contributes to `OCCUPIED`.
- Also relevant to WG-C-001 (already REJECTED).

## Quotes / page references
From the publisher's structured abstract and highlights (not the article body):
- "the lack of inbound traffic and rescue operations" (Abstract, gap statement).
- "A custom waypoint-based routing algorithm enables adaptive rerouting for outbound and inbound
  evacuation." (Highlights).
- "Pedestrian movement, private vehicle, emergency extraction, and vehicle–pedestrian interactions
  are explicitly represented." (Highlights).
- "enables both outbound self-evacuation and inbound rescue operations" (Abstract).

## Follow-up papers
- Siam et al. (2022), *Transportation Research Part D* 103:103147 — interdisciplinary agent-based
  multimodal wildfire evacuation model (critical decisions and life safety).
- Wahlqvist et al., WUI-NITY platform, *Safety Science* (2021).
- "Analyzing wildfire evacuation dynamics with agent-based modeling in damaged road networks,"
  *Safety Science* (2025), S0925753525000608 — **RETRIEVE**, damaged-network rerouting.
- Grajdura et al. (2022) — Camp Fire ABM with reduced vehicle access.
