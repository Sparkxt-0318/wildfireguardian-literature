# kwon2025koreaevac

*(Metadata for this item was already committed by another agent as
`literature/metadata/kwon2025koreaevac.yaml`; this note is the Category-8 reading of it and
records an independent re-verification.)*

## Citation
Kwon, Kyubin; Kim, Yejin; Han, Jinil (2025). "An Integrated Optimization for Resilient
Wildfire Evacuation System Design: A Case Study of a Rural County in Korea." *Systems*
13(12): 1125. DOI 10.3390/systems13121125. Gold OA (CC-BY).

**Verification note (Agent C role):** metadata re-verified independently via the OpenAlex
API on 2026-09-19; authors, venue, volume, issue, article number, year, DOI and OA status
all agree with the existing Crossref-sourced record. No discrepancy found.

## Publication status
**PEER_REVIEWED.** Language: English. Evidence level **E2** — abstract only (MDPI blocks
WebFetch with HTTP 403).

## Problem
Where should a rural Korean county place wildfire shelters, and how should villages be
linked to them so the system still works when roads are blocked or fire cuts a link?

## Method
Mixed-integer programming. A **dual-stage** structure: simultaneously choose primary and
secondary shelter locations and establish main *and backup* evacuation linkages, so
accessibility survives disruption. Wildfire risk indices derived from topographic and
environmental data enter the objective/constraints to give risk-aware, balanced allocation.

## Data
Uiryeong County (의령군), South Korea — a rural county. Topographic and environmental layers
for the risk index; road network and settlement/shelter candidates.

## Outputs
Shelter locations (primary + secondary) and main/backup village→shelter assignments;
reported as improving evacuation efficiency and reliability across disruption scenarios.

## Key equations
MIP formulation; exact objective NEEDS_FULL_TEXT.

## Assumptions
- Wildfire risk is a **static index** from terrain and environment, not a propagating front.
- Disruption is represented as scenario-wise link failure, not as timed fire arrival.
- Everyone assigned to a shelter can get there.

## Validation
Scenario-based computational study on a real county; no real evacuation is reproduced.

## Limitations
- **No time axis.** There is no fire arrival time, no departure time, no deadline.
- No vulnerable or non-self-evacuating residents as a distinct class.
- No responder, no inbound leg, no round trip.
- Strategic (plan-before-the-season), not tactical (decide-during-the-fire).

## WildfireGuardian overlap
This is the strongest *peer-reviewed* Korean wildfire evacuation-planning paper found, and
it is a rural Korean county — the same setting WildfireGuardian claims. It is the paper a
judge will cite if WG-C-007 is overclaimed.

## WildfireGuardian difference
Operational, in NOVELTY_STANDARD §6 terms: Kwon et al. solve a **static facility-location
and assignment** problem whose output is a network plan (which shelter, which backup link),
using a **time-independent** terrain-derived risk index. WildfireGuardian solves a
**timing** problem whose output is a fire-relative dispatch clock, with fire-arrival
feasibility enforced leg-by-leg on a responder round trip drawn from an ensemble of
arrival-time fields. Different objects (facilities vs a departure time), different hazard
representation (static index vs time-varying arrival distribution), different decision
moment (pre-season planning vs during-incident dispatch).

## Novelty threat
**HIGH for WG-C-007** — a "Korean rural-county wildfire evacuation system design" already
exists in a peer-reviewed venue, so geography alone is dead as a novelty axis.
**LOW for WG-C-003** — it computes no deadline and no responder trip.
**Relevant to WG-C-011** (it does allocate a scarce resource — shelter capacity — though
not vehicles or crews).

## Quotes / page references
> "simultaneously determines the locations of primary and secondary shelters and establishes
> both main and backup evacuation linkages" (abstract).
Article number 1125; per-quotation page NEEDS_FULL_TEXT.

## Follow-up papers
- Anything citing it that adds a time dimension — nothing found as of 2026-09-19.
- `kwak2021evacroute`, `mois2025evacuationstages`.
