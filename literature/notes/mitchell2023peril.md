# mitchell2023peril

## Citation
Mitchell, H.; Gwynne, S.; Ronchi, E.; Kalogeropoulos, N.; Rein, G. (2023). "Integrating
wildfire spread and evacuation times to design safe triggers: Application to two rural
communities using PERIL model." *Safety Science* 157: 105914.
DOI 10.1016/j.ssci.2022.105914

## Publication status
PEER_REVIEWED (journal article). OPEN ACCESS (Unpaywall is_oa = true, publisher PDF).
Evidence level E2 — abstract obtained via the FRAMES catalog record; full text not read.

## Problem
Operational evacuation triggers in rural WUI communities are set by convention, without
safety margins and without reference to fire-spread dynamics or evacuation duration.

## Method
PERIL (Population Evacuation tRigger aLgorithm): couples a wildfire spread model (FARSITE)
with evacuation time estimates to generate trigger perimeters around a community, with
explicit **safety factors** applied to absorb uncertainty.

## Data
Two real communities with existing evacuation data: Swinley Forest (UK) and Roxborough
Park, Colorado (USA).

## Outputs
Trigger perimeters, with safety-factor-inflated variants.

## Key equations
NEEDS_FULL_TEXT. The safety factor's definition and where it is applied (to time, to
distance, or to rate of spread) is the detail we need.

## Assumptions
Deterministic FARSITE run per scenario; margin handled by a multiplier rather than a
distribution; egress only.

## Validation
Applied to two communities chosen because evacuation data already existed; this is
application rather than skill validation.

## Limitations
A safety factor is a margin, not a probability — it cannot say how likely the trigger is
to fail. No traffic layer of its own (WUI-NITY supplies that in the sibling work).
No responders.

## WildfireGuardian overlap
Re-establishes, in the fire-safety-engineering tradition, that a trigger is the product of
*fire spread time* and *evacuation time* with an uncertainty margin. This is the direct
intellectual ancestor of everything WildfireGuardian wants to compute.

## WildfireGuardian difference
PERIL's uncertainty is a deterministic margin on a community egress boundary. WG-C-003's
quantity is a dispatch time whose feasibility is enforced leg-by-leg on a round trip, and
WG-C-002's uncertainty is a forecast-quality parameter that is *varied*, not a fixed
multiplier.

## Novelty threat
**level: HIGH** for WG-C-001; **HIGH** for WG-C-004 as the precursor that makes k-PERIL's
probabilistic version obvious.

## Quotes / page references
FRAMES catalog abstract: PERIL "can be applied to inform safer strategies for to protect
rural communities threatened by wildfires." (abstract as reproduced on frames.gov/catalog/66666)

## Follow-up papers
kalogeropoulos2022kperil, kalogeropoulos2023kperil, kalogeropoulos2025dire,
kalogeropoulos2026ensemble, ronchi2023verification, wahlqvist2021wuinity.
