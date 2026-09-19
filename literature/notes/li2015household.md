# li2015household

## Citation
Li, D.; Cova, T. J.; Dennison, P. E. (2015). "A household-level approach to staging
wildfire evacuation warnings using trigger modeling." *Computers, Environment and Urban
Systems* 54: 56–67. DOI 10.1016/j.compenvurbsys.2015.05.008

## Publication status
PEER_REVIEWED (journal article). OA UNKNOWN. Evidence level E2 (abstract only).

## Problem
Trigger buffers had been computed for communities and for firefighters but not for
individual households, so warnings could not be staged.

## Method
Three steps: (1) compute a trigger buffer for **each household**; (2) model fire spread
until every household's buffer is crossed; (3) **rank households by available (lead)
time** to produce a staged warning schedule.

## Data
Julian, California, USA (the standard WUIVAC test bed).

## Outputs
A per-household lead time and a staged warning ordering derived from it.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Deterministic fire spread; evacuation time per household exogenous; every household
self-evacuates.

## Validation
Method demonstration; no drill or event validation.

## Limitations
No traffic interaction between staged groups (an ordering that is safe in isolation may
congest). No probabilistic treatment. No modelling of *who* moves a household that cannot
move itself.

## WildfireGuardian overlap
This occupies two things WildfireGuardian might have wanted: **household-resolution
triggers**, and **prioritising people by remaining lead time**. Any WildfireGuardian
statement of the form "we compute triggers per household and order residents by urgency"
is prior art from 2015.

## WildfireGuardian difference
Li et al. rank households by their own egress lead time and assume each household then
leaves. WG-C-003's subject is the *responder*: the ordering constraint is fleet
feasibility (one vehicle, three legs, fire on every leg), not the resident's own clock.
The quantity is a dispatch time, not a warning rank.

## Novelty threat
**level: HIGH** — occupies the household-trigger and lead-time-ranking framings; supports
the rejection of WG-C-001. Does not reach WG-C-003.

## Quotes / page references
Abstract: "ranking households by their available (or lead) time, which enables emergency
managers to develop a staged evacuation warning plan." (abstract, Consensus record)

## Follow-up papers
li2018coupling, tang2025transit.
