# lu2026lahaina

## Citation
Lu, A.; Tan, H. K.; Xue, A.; Koniges, A.; Bertozzi, A. L. (2026). "Macroscopic Traffic
Flow Network Modeling For Wildfire Evacuation: A Game-Theoretic Junction Optimization
Approach with Application to Lahaina Fire." arXiv:2603.29055. Submitted 2026-03-30.
DOI: UNVERIFIED.

## Publication status
**PREPRINT** (arXiv). Not peer-reviewed. Open access.
Evidence level E2 — arXiv abstract page fetched directly; full text not read.
Per NOVELTY_STANDARD §3.3, preprint status does not reduce its force as prior art.

## Problem
The 2023 Lahaina fire killed ~102 people on a peninsula served by a single two-lane
highway. Exit-lane capacity, not behaviour, was the binding constraint. How much does
adding or reversing lanes actually buy, and can responders be let in at the same time?

## Method
Evacuation modelled as a system of hyperbolic scalar conservation laws on a directed graph,
with **game-theoretic junction conditions** that maximise total network flux, an
evacuation-calibrated piecewise linear–quadratic flux function, and a loss-driven
optimisation that tunes traffic distribution toward priority corridors. Analytical results
on a toy network plus numerical simulation of the real Lahaina road network.

## Data
Lahaina, Maui road network; 2023 Lahaina fire as the motivating event.

## Outputs
- A **phase transition in exit-lane capacity**: extra lanes improve throughput linearly up
  to a computable critical threshold, past which no route optimisation helps.
- For Lahaina: reversing one southbound lane captures nearly all achievable improvement.
- **A fourth lane can be reserved for emergency vehicles with negligible impact on civilian
  clearance time.**

## Key equations
Conservation-law system with junction flux-maximisation conditions; the critical-threshold
expression is the headline analytical result. NEEDS_FULL_TEXT for the exact forms.

## Assumptions
Macroscopic (continuum) traffic; no individual vehicles; fire enters as a constraint on the
network topology/priority rather than as a simulated spreading front (NEEDS_FULL_TEXT to
confirm).

## Validation
Real network geometry, retrospective event; not a calibration against observed flows.

## Limitations
No fire-spread model coupling verified. No pickup, no dwell, no per-vehicle mission. The
emergency-vehicle result is a *capacity reservation*, not a routed or timed response.

## WildfireGuardian overlap
Directly relevant to **WG-C-003**: it is the clearest published statement that inbound
emergency-vehicle access can be *priced against* outbound evacuee throughput, and that the
price can be near zero if you reserve capacity. If a reviewer asks "doesn't responder
ingress just trade off against evacuation?", this paper is the answer — and it is not ours.

## WildfireGuardian difference
Lu et al. answer a **network design** question (how many lanes, which direction, reserve
one for responders). WG-C-003 answers a **timing** question about a specific mission
(when must this unit leave so that in + pickup + out all complete before fire arrival).
One allocates capacity; the other computes a deadline. They are complementary, not
competing — but WG-C-003 can no longer claim to be first to notice that responders must
move against the evacuation flow.

## Novelty threat
**level: HIGH** — WG-C-003 (occupies "responder ingress modelled alongside outbound
evacuation at the network level"; does not occupy the dispatch deadline).

## Quotes / page references
Abstract: "a fourth lane can be reserved for emergency vehicles with negligible impact on
civilian clearance time." (arXiv:2603.29055 abstract)
Abstract: "Additional lanes improve throughput linearly until a computable critical
threshold." (arXiv:2603.29055 abstract)

## Follow-up papers
UNKNOWN — too recent.
