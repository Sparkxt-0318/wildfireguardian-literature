# dennison2007wuivac

## Citation
Dennison, P. E.; Cova, T. J.; Moritz, M. A. (2007). "WUIVAC: a wildland-urban interface
evacuation trigger model applied in strategic wildfire scenarios." *Natural Hazards*
41(1): 181–199. DOI 10.1007/s11069-006-9032-y
(Note: the Crossref record spells the third author "Mortiz"; recorded here as seen.)

## Publication status
PEER_REVIEWED (journal article). OA status UNKNOWN. Evidence level E2 (abstract only).

## Problem
Trigger buffers computed for one fire event are tactical. Can the same machinery produce
a *strategic*, pre-season planning product?

## Method
WUIVAC. Eight years of wind measurements are used to identify worst-case (strongest)
winds in each of 16 directions. Surface-fire rate of spread gives trigger buffers for the
communities and, separately, for three evacuation routes. Multiple buffers are unioned
into "fire planning areas."

## Data
Julian and Whispering Pines, California, USA. Eight years of wind observations (station
NOT verified).

## Outputs
- Per-direction worst-case trigger buffers
- Fire planning areas (union of buffers)
- Buffers predicting **closure of all evacuation routes**

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
- Worst-case wind per direction is the right conservative envelope (a margin, not a
  probability).
- Route closure is a geometric consequence of the fire reaching the route.
- Egress only.

## Validation
Strategic demonstration; no event validation.

## Limitations
"Worst case in 16 directions" is an envelope, not a distribution: it cannot say how
*likely* a given boundary is. No traffic, no responders, no household resolution.

## WildfireGuardian overlap
Two overlaps matter. (1) It is second prior art for WG-C-001. (2) Its **route-closure
buffers** are the earliest thing in the lineage that reasons about a road becoming
unusable because of fire arrival — the mechanism WG-C-003 needs for the inbound leg.

## WildfireGuardian difference
Dennison et al. ask "when will the fire close the way out?" WG-C-003 asks "when must a
responder already be moving *in*, so that the whole in-pickup-out trip still closes?"
Route closure here bounds an escape; in WG-C-003 it bounds an approach as well.

## Novelty threat
**level: HIGH** — reinforces the rejection of WG-C-001; partially anticipates the
route-closure component of WG-C-003 but not the round trip or the dispatch time.

## Quotes / page references
Abstract: "trigger buffers that predict the closure of all evacuation routes were
explored." (abstract, Consensus record)

## Follow-up papers
larsen2011cedar, li2018coupling, kim2024directional, ma2025damaged.
