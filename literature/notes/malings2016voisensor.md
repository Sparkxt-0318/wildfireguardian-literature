# malings2016voisensor

## Citation
Malings, C., and M. Pozzi, 2016: Value of information for spatially distributed
systems: Application to sensor placement. *Reliability Engineering & System
Safety*, **154**, 219-233. DOI 10.1016/j.ress.2016.05.010

## Publication status
Peer-reviewed journal (Elsevier). Bibliographic record verified via Crossref API.
Abstract obtained via Consensus. Full text not read. Evidence level **E2**.

## Problem
How should sensors be placed in a spatially distributed system so as to maximise
the *decision-relevant* benefit of the information they yield?

## Method
Value-of-information (VOI) analysis restricted to Gaussian random field and
binary state models. Several loss functions are considered; computational
techniques are given for evaluating VOI under each; placements are then optimised
by VOI. Information propagation between locations is exploited.

## Data
Two example applications in infrastructure management (specifics NEEDS_FULL_TEXT).

## Outputs
Two results stated in the abstract:
(1) sensor placements **depend on the decision-making problem to be addressed**,
as encoded in a problem-specific loss function;
(2) the complexity of VOI computation is governed by that loss function's
characteristics.

## Key equations
Pre-posterior decision analysis / VOI. NEEDS_FULL_TEXT.

## Assumptions
Gaussian random field state; binary component states; known intervention actions
and costs.

## Validation
Numerical examples, not field deployment.

## Limitations
Static infrastructure; no propagating hazard; no deadline. The companion 2019
paper (Malings & Pozzi, *Reliab. Eng. Syst. Saf.*) shows VOI is **not
submodular**, so greedy placement can be sub-optimal — an important practical
caveat for any WildfireGuardian implementation.

## WildfireGuardian overlap
Result (1) is the core methodological content of **WG-C-008**: what to observe
should be chosen by the downstream decision's loss, not by generic uncertainty
reduction. That was published in 2016.

## WildfireGuardian difference
No time-critical structure. Malings & Pozzi choose *where* to put sensors for a
management decision made at leisure. WildfireGuardian would choose *what to
observe next* when the value of any observation collapses to zero once the
dispatch deadline passes. That deadline-conditioned collapse is the only part of
WG-C-008 not already covered here.

## Novelty threat
**CRITICAL** to WG-C-008 as a methodological claim. WG-C-008 cannot be N3.

## Quotes / page references
Relayed from the publisher abstract (E2, not page-verified): "sensor placements
depend on the decision-making problem to be addressed, as encoded in a
problem-specific loss function".

## Follow-up papers
- malings2018voispatiotemporal (adds scheduling / when to sense)
- Malings & Pozzi, "Submodularity issues in value-of-information-based sensor
  placement", *Reliability Engineering & System Safety*, 2019 (DOI UNVERIFIED —
  abstract seen via Consensus; verify before citing)
- sun2025decisionfocusedsensing
