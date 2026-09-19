# shao2026beliefaware

## Citation
Shao, X., K. Yamakawa, and W. S. Cheah, 2026: Belief-Aware Scheduling for
Predictive Wildfire Hazard Mapping under Sparse-Window Telemetry.
arXiv:2606.06917. DOI 10.48550/arXiv.2606.06917

## Publication status
**PREPRINT** (arXiv; formatted as an IEEE submission). Not peer-reviewed as
retrieved. Full text obtained via alphaXiv. Evidence level **E3**.

## Problem
An edge node monitoring a wildfire observes more than a duty-cycle-limited or
windowed downlink (e.g. LoRaWAN, intermittent LEO) can carry. What should be
sensed, represented and transmitted so the receiver can predict the H-step-ahead
hazard map?

## Method
Formalised as a partially observed sequential allocation problem with three
coupled per-region action axes (sensing, representation, transmission). The
structured belief is derived from the H-step forward operator's input
requirements; a scheduler anticipates future transmission opportunities
(non-myopic). Compared against a FAIR activity-paced reference and uniform
pacing. Lightweight (~40k parameter) cross-region attention encoder vs. a deeper
Transformer.

## Data
Physics-calibrated **synthetic** environment (chosen because window period P,
per-window capacity C, predictive horizon H and fuel composition are not
separable in real-landscape data). Worked scenario: 4-hour daylight shift over a
16 km x 16 km incident, 16x16 grid of 1 km cells, 25 actionable regions.

## Outputs
(1) The gap between non-myopic activity-paced scheduling and uniform pacing is
unimodal in window-period sparsity, peaking at intermediate spacing.
(2) Ablating the structured belief, the dominant component flips between temporal
staleness (default landscape) and static-risk prior (structured landscape); the
per-cell intensity belief is redundant in both.
(3) The lightweight encoder beats the FAIR reference by ~28% / ~11%.

## Key equations
POMDP-style sequential allocation; NEEDS_FULL_TEXT for the exact objective.

## Assumptions
Known forward hazard operator; bandwidth/duty-cycle model; synthetic landscape
statistics transfer.

## Validation
Synthetic OSSE-style environment only. Explicitly justified, but no real fire.

## Limitations
The scheduler's objective is **mean predictive loss on the hazard map**. There is
no evacuation decision, no deadline, no protective action. Preprint.

## WildfireGuardian overlap
Occupies "wildfire active sensing / observation scheduling under a communication
budget with a non-myopic scheduler". Any WildfireGuardian claim phrased as
"first to schedule wildfire observations adaptively" is dead.

## WildfireGuardian difference
The decisive difference is the objective: Shao et al. optimise a *predictive*
loss (hazard-map accuracy). WG-C-008 proposes to optimise the *decision* — which
observation most changes the dispatch-by deadline. Given raeth2026decisionskill,
mandi2024dfl and sun2025decisionfocusedsensing, these are demonstrably not the
same objective, which is exactly why the gap is worth occupying.

## Novelty threat
**HIGH** to WG-C-008 as an application claim ("wildfire sensing scheduling"),
but it does *not* occupy the decision-directed version.

## Quotes / page references
Abstract: "the operative design problem is not which neural architecture to use
but how to derive a structured belief sufficient for the receiver's prediction
task".
Index terms include "active sensing, partially observable Markov decision
process ... predictive hazard mapping, wildfire monitoring".

## Follow-up papers
- sun2025decisionfocusedsensing
- veiga2023activesensing
