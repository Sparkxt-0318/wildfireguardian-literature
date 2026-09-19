# rossa2026actionbed

## Citation
Rossa, T., A. Phillips, and T. Rainforth, 2026: Action-BED: Task-Driven Bayesian
Experimental Design with Singly Intractable Objectives. arXiv:2606.23662,
submitted 22 June 2026. DOI 10.48550/arXiv.2606.23662

## Publication status
**PREPRINT** (arXiv). Not peer-reviewed. Abstract page retrieved via WebFetch;
full text not read. Evidence level **E2**.

## Problem
Classical Bayesian experimental design maximises expected information gain
(prior-to-posterior uncertainty reduction). This gives doubly intractable
objectives and is hard to customise to a downstream task.

## Method
Following first-principles decision theory, reformulates BED as minimising an
**expected future loss (EFL)** on downstream actions. Shows all such EFLs can be
rearranged into *singly* intractable objectives, jointly optimisable over a
design policy and a downstream action policy via stochastic gradients. Needs only
the ability to sample from the joint model and evaluate the downstream loss — no
explicit posterior or marginal-likelihood estimation.

## Data
Domain-agnostic; benchmark problems NEEDS_FULL_TEXT.

## Outputs
ACTION-BED: a general method for learning task-driven data-gathering policies.

## Key equations
Design objective = expected future loss of downstream Bayes-optimal actions
(exact form NEEDS_FULL_TEXT).

## Assumptions
Known downstream loss; simulable joint model over parameters and data.

## Validation
Benchmarks, NEEDS_FULL_TEXT.

## Limitations
No hazard domain, no deadline, no spatial field. Preprint.

## WildfireGuardian overlap
Directly instantiates the general idea behind **WG-C-008**: select observations
by their effect on the downstream decision rather than by information gain, as a
*general method*, in 2026, from the group that wrote the canonical BED review.

## WildfireGuardian difference
None at the methodological level — which is the point. WildfireGuardian would be
a *user* of Action-BED-style reasoning, not an inventor of it.

## Novelty threat
**CRITICAL** to WG-C-008 as an N3 (methodological) claim.

## Quotes / page references
Abstract: "BED can alternatively be formulated in terms of an expected future
loss (EFL) on downstream actions, providing a simple and naturally task-driven
framework."

## Follow-up papers
- rainforth2024modernbed
- Huang, D. et al., "Amortized Bayesian Experimental Design for Decision-Making",
  NeurIPS 2024 / arXiv:2411.02064 (bibliographic seen via search listing; full
  author list NOT verified — verify before citing)
- "Goal-driven Bayesian Optimal Experimental Design for Robust Decision-Making
  Under Model Uncertainty", arXiv:2605.26093 (authors NOT verified — search lead)
