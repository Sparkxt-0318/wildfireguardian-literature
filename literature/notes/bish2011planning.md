# bish2011planning

## Citation
Bish, D. R. (2011). "Planning for a bus-based evacuation." *OR Spectrum*, 33(3), 629–654.
DOI: 10.1007/s00291-011-0256-1.

## Publication status
`PEER_REVIEWED`, journal article, CLOSED access. Bibliographic record verified via Crossref.
Content below is from the summary returned by WebSearch of the publisher page and the description
in the bus-evacuation review literature. Evidence level **E2**. `NEEDS_FULL_TEXT`.

## Problem
Regional evacuation of **transit-dependent / transit-captive populations** — people without access
to a private vehicle — using a capacity-constrained bus fleet that must make multiple trips.

## Method
Bus evacuation problem: capacity-constrained buses routed multiple times to transport all evacuees
from pickup locations to a depot/shelter. Formulated to minimise **total waiting time at pickup
locations** — interpreted by Bish as total **exposure** — subject to the requirement that
**the last pickup at each location occurs by a location-specific time determined by risk
considerations.**

## Data
Not a case study paper; formulation and computational analysis.

## Outputs
Bus routes and trip sequences; total exposure/waiting time.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
The location-specific last-pickup time is **given**, derived from unspecified "risk considerations"
external to the model. No hazard progression model produces it.

## Validation
Computational only.

## Limitations
Static risk; no hazard front; no responder ingress feasibility against a hazard.

## WildfireGuardian overlap
Structurally this is the canonical ancestor of everything in Category 2: buses depart a depot,
travel **inbound** to pickup locations where carless people wait, load them, and deliver them to a
shelter, repeatedly. WildfireGuardian's mission decomposition is this loop.

The single most relevant feature: Bish imposes a **location-specific deadline on the last pickup,
set by risk**. That is a per-location time bound on a leg of an assisted-evacuation mission, in
print since 2011. WG-C-003 cannot claim novelty for "a time bound on an assisted-evacuation leg."

## WildfireGuardian difference
- Bish's deadline is on the **pickup instant**, not on **dispatch**, and it is exogenous, not
  derived. The distinction WildfireGuardian must be able to state crisply:
  a last-pickup time answers "when must this person be aboard"; a latest-dispatch time answers
  "when must the vehicle leave base so that being aboard by then, *and getting out afterwards*, is
  still possible." The second requires an inbound travel model and an egress feasibility check that
  Bish does not have.
- No hazard progression. No fire. No forecast.

## Novelty threat
**level: BACKGROUND** (but load-bearing background)
- **WG-C-005** → contributes to `OCCUPIED`; carless/transit-captive populations as the served
  group is 2011-vintage.
- **WG-C-003** → no direct threat, but it caps the claim: the existence of a risk-derived
  location deadline in assisted evacuation is 15 years old.

## Quotes / page references
No verbatim quotes recorded; the article body was not retrieved. The phrase
"the last pickup occurs at a location-specific time determined by risk considerations" is a
paraphrase from a secondary summary and must be verified before it is quoted.

## Follow-up papers
- Zhao, Ji, Xu, Qian, Ren & Shan (2020), *TR-A* 137:285–300 — round-trip bus evacuation with
  simultaneous scheduling and routing.
- Goerigk & Grün — robust bus evacuation with delayed scenario information (**lead only;
  bibliographic record NOT verified — RECALL/secondary**).
- Bus routing for the Great Fire of Valparaíso, IEEE CEC 2017 (**lead only; record not verified**).
