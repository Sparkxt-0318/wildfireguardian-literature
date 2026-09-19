# morris2019simulation

## Citation
Morris, T. P., White, I. R., & Crowther, M. J. (2019). Using simulation studies to
evaluate statistical methods. *Statistics in Medicine*, 38(11), 2074–2102.
DOI: 10.1002/sim.8086

## Publication status
Published, peer-reviewed, open access. Metadata verified via Crossref API. A preprint
exists at arXiv:1712.03198.

## Problem
Simulation studies are widely used and poorly reported: aims are vague, the
data-generating mechanism is under-specified, the number of repetitions is unjustified,
and Monte Carlo uncertainty is not reported — so readers cannot tell whether a reported
difference between methods is real or simulation noise.

## Method
Proposes the **ADEMP** structure for planning and reporting:
- **A**ims
- **D**ata-generating mechanisms
- **E**stimands / other targets
- **M**ethods (the procedures being compared)
- **P**erformance measures

and supplies formulae for common performance measures (bias, empirical SE, coverage,
power) together with their **Monte Carlo standard errors (MCSE)**, plus formulae for
choosing the number of repetitions n_sim from a target MCSE.

## Data
Illustrative simulated examples.

## Outputs
- The ADEMP checklist.
- MCSE formulae per performance measure.
- Repetition-count planning: n_sim chosen so MCSE is small relative to the difference the
  study is meant to detect.
- Guidance on presenting results (including plots over the simulation grid rather than
  tables of significance stars).

## Key equations
For a performance measure estimated as a mean over n_sim repetitions, MCSE = SD across
repetitions / sqrt(n_sim); for coverage p̂, MCSE = sqrt(p̂(1−p̂)/n_sim). **Verify against
the paper's numbered equations before typesetting.**

## Assumptions
Repetitions are independent draws from the data-generating mechanism. *This assumption is
where our design is exposed* — see below.

## Validation
Not applicable (methodological).

## Limitations
- Written for statistical-method evaluation where the data-generating mechanism is a
  probability model the analyst fully controls. Our generator is a fire simulator over a
  small set of real events, so the "independent draws" premise is not automatic.
- Says little about clustered/nested simulation designs.

## WildfireGuardian overlap
Our whole experimental apparatus is a simulation study: we compare a forecast-aware policy
against a tuned trigger policy over a scenario grid. ADEMP maps onto us directly — the
data-generating mechanism is the fire-scenario generator, the estimand is the
latest-safe-dispatch time or the decision regret, and the performance measures are regret,
mission-completion rate, and calibration.

## WildfireGuardian difference
**Requirement imposed on us:**
1. Report the experiment as ADEMP, with the scenario generator specified precisely enough
   to be re-implemented.
2. Attach a Monte Carlo standard error to every headline number, and justify the number of
   scenarios from a target MCSE rather than from compute budget.
3. **Reconcile MCSE with the event-level unit of analysis.** MCSE computed over
   non-independent scenarios understates uncertainty. Our MCSE must be computed over
   *events* (or via the event-level cluster bootstrap), which will make it much larger and
   may show that our current scenario count is buying precision we cannot claim. This is
   the arithmetic most likely to change a headline number in the program.

## Novelty threat
BACKGROUND.

## Quotes / page references
Full text not retrieved; no verbatim quotation recorded. The ADEMP acronym and the MCSE
emphasis are taken from the verified title/abstract and from Siepe et al. (2024), which
builds directly on it.

## Follow-up papers
- Siepe, Bartoš, Morris, Boulesteix, Heck & Pawel (2024), *Psychological Methods*,
  DOI 10.1037/met0000695 — ADEMP-PreReg preregistration template. Recorded.
- Williams et al. (2024), *Methods in Ecology and Evolution* 15(11):1926–1939 — reporting
  items; finds only 17% of surveyed articles report Monte Carlo uncertainty. Recorded.
