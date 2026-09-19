# kwak2021evacroute

## Citation
곽재환 (Kwak, Jae-Hwan); 김남균 (Kim, Namgyun); 김만일 (Kim, Man-Il) (2021).
「도시산불 대응을 위한 GIS 기반 주민최적대피경로설정 알고리즘 개발」 /
"Development of Evacuation Route Planning Algorithm for Responding to Urban Forest Fires."
『한국방재학회논문집』 *Journal of the Korean Society of Hazard Mitigation* 21(6): 63–70.
DOI 10.9798/KOSHAM.2021.21.6.63.

## Publication status
**PEER_REVIEWED.** Korean-language journal article (Korean title with an official English
title supplied by the journal). Evidence level **E2** — KCI record and abstract only.

## Problem
When an urban-adjacent wildfire threatens, which route should a resident take to a shelter?

## Method
GIS-based route-planning algorithm. Candidate paths from each origin point to shelters are
generated within wildfire spread zones and ranked; applied to a hypothetical scenario
(가상 시나리오).

## Data
Korean GIS road/shelter layers; a hypothetical urban-wildfire scenario. Specific study area
NEEDS_FULL_TEXT.

## Outputs
Up to **fifteen** evacuation routes per origin point to the shelter, offering decision
makers a diverse option set rather than a single prescribed path.

## Key equations
Not available from the record. NEEDS_FULL_TEXT — in particular whether route cost is
distance, travel time, or fire-exposure weighted.

## Assumptions
Shelters are known and available; the spread zone is static during the evacuation; every
resident can traverse the route unaided.

## Validation
None against a real event — the application is a hypothetical scenario.

## Limitations
- No departure time and no arrival-time constraint: the algorithm says *where to go*, never
  *when to go* or *whether the route is still open when you get there*.
- Spread zone appears to be a fixed region, not a time-varying front.
- No traffic, no capacity, no vulnerable-resident case, no responder.

## WildfireGuardian overlap
Occupies "Korean wildfire evacuation routing in GIS." Together with `kwon2025koreaevac`
(shelter siting) it means Korea already has a peer-reviewed wildfire evacuation *spatial*
literature.

## WildfireGuardian difference
Route-set enumeration under a static hazard zone versus a latest-safe dispatch time under a
time-varying, uncertain fire arrival field. Different output type entirely (paths vs a
scalar time), and Kwak et al. never impose a fire-arrival feasibility constraint on any leg.

## Novelty threat
**MODERATE for WG-C-007** — it forbids "first Korean wildfire evacuation routing work."
**NONE for WG-C-003.**

## Quotes / page references
> "Up to fifteen evacuation routes were determined for each start point" (abstract, as
> rendered in the KCI record).
Page range 63–70; per-quotation page NEEDS_FULL_TEXT.

## Follow-up papers
- `kwon2025koreaevac` — the shelter-location/backup-linkage successor.
- `gu2016spreadalgorithm` — the spread-prediction side of the same Korean problem.
