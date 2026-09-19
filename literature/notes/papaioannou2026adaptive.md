# papaioannou2026adaptive

## Citation
Papaioannou, S., Kolios, P., Panayiotou, C. G., & Polycarpou, M. M. (2026). *Adaptive Monitoring of Stochastic Fire Front Processes via Information-seeking Predictive Control.* arXiv:2601.11231 (submitted 16 January 2026; revised 21 February 2026).

## Publication status
**PREPRINT** (arXiv). No DOI. Abstract page read; full text not retrieved (**E2**).

## Problem
A mobile agent (drone) monitors a wildfire front. Its trajectory determines where measurements are taken and
therefore how accurately fire propagation can be estimated. Where should it fly?

## Method
Formulated as a stochastic optimal control problem integrating sensing, estimation and control. A Bayesian
estimator is derived for nonlinear elliptical-growth fire front models and recast as a finite-horizon Markov
decision process with information-seeking control, solved by a lower-confidence-bound adaptive search algorithm
with asymptotic convergence to the optimal policy. The trajectory is planned over a rolling finite horizon.

## Data
Simulation; stochastic nonlinear elliptical-growth fire front models. No real fire.

## Outputs
An adaptive drone trajectory policy that reduces uncertainty in the estimated fire evolution.

## Key equations
Bayesian estimator for the elliptical-growth front plus a finite-horizon MDP with an information-seeking reward;
exact forms not retrieved. NEEDS_FULL_TEXT.

## Assumptions
- Elliptical fire growth (the Alexander/Anderson ellipse family), i.e. a homogeneous local spread regime.
- A single mobile agent; sensing is the only control.

## Validation
Simulation only.

## Limitations
No real fire data. No human, no community, no responder.

## WildfireGuardian overlap
This is **the closest wildfire-specific prior art to WG-C-008**. It is a full closed loop: fire model →
uncertainty → where to look next → better fire model.

## WildfireGuardian difference
The objective. Papaioannou et al. minimise *estimation uncertainty about the fire front*. WildfireGuardian's
proposed objective is the expected change in a *protective-action decision* — which observation most changes
whether we dispatch now or wait. These coincide only if decision value is monotone in front-position uncertainty,
which is precisely what WG-C-014 suspects is false. The claim therefore survives only if we demonstrate a case
where information-seeking control and decision-seeking control choose different flight paths, and the
decision-seeking one produces a better outcome against the same fire.

## Novelty threat
**HIGH for WG-C-008.** The *method* (information-driven active sensing) is occupied, both generically
(veiga2023activesensing, already filed) and now wildfire-specifically. WG-C-008 must be rewritten as a
**decision-consequence objective** claim, not an active-sensing claim, and even then it must be demonstrated, not
asserted.

## Quotes / page references
Abstract: formulates the task as "a stochastic optimal control problem that integrates sensing, estimation, and
control"; control is "information-seeking predictive control".

## Follow-up papers
- veiga2023activesensing (field survey; already filed by another agent).
- sun2025decisionfocusedsensing (already filed; the decision-focused objective, in flood not fire — the two
  together substantially box in WG-C-008).
- bailonruiz2022uavfleet, roysingh2025constellation.
