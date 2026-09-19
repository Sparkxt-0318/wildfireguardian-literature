# yu2019twin

## Citation
Yu, L., Fennel, K., Wang, B., Laurent, A., Thompson, K. R., & Shay, L. K. (2019).
Evaluation of nonidentical versus identical twin approaches for observation impact
assessments: an ensemble-Kalman-filter-based ocean assimilation application for the Gulf
of Mexico. *Ocean Science*, 15(6), 1801–1814. DOI: 10.5194/os-15-1801-2019

## Publication status
Published, peer-reviewed, gold open access (Copernicus). A discussion-stage preprint
exists at DOI 10.5194/os-2019-85 under the title "fraternal versus identical twin" —
**cite the journal version, not the preprint; the titles differ.**

## Problem
Twin experiments are the standard way to assess the impact of new observations. If the
"truth" run and the forecast run come from the same model (identical twin), the impact
assessment may be biased. The bias was known in atmospheric NWP but had not been directly
quantified for ocean DA.

## Method
Direct side-by-side comparison of identical-twin and nonidentical-twin OSSE designs in one
Gulf of Mexico EnKF assimilation system. Same observations, same filter; only the
truth/forecast model relationship differs.

## Data
Synthetic observations (SSH, SST, temperature/salinity profiles) sampled from the nature
run; real observing-network geometry.

## Outputs
Impact estimates (mean absolute difference reduction) under both designs:

| Metric | Identical twin (I1) | Nonidentical twin (N1) |
|---|---|---|
| Temperature MAD reduction | 45% | 29% |
| Velocity MAD reduction | 46% | 25% |
| Subsurface circulation (400 m) | ~67% | ~45% |

Direction of the bias: identical twins **overestimate** the value of the cheap surface
observations (SSH, SST) and **underestimate** the value of profile observations.

## Key equations
None required for our use. The relevant construct is the error-growth rate of the forecast
run relative to the nature run, which the authors show can look "reasonable" in both
designs while impacts are still biased.

## Assumptions
That the nonidentical-twin result is the better proxy for real-world observation impact.

## Validation
Internal: error growth rates were checked in both frameworks and found comparable — this
is the important negative result, because a plausible error-growth rate does **not**
certify the design.

## Limitations
- Ocean EnKF, one domain, one filter. Generalisation to fire/decision settings is by
  analogy, not by demonstration.
- The nonidentical twin is itself only an approximation of reality.

## WildfireGuardian overlap
Our OSSE (WG-C-010) generates the "true" fire and the forecast fire. If both come from the
same spread model with only perturbed inputs, we are running an identical twin, and by
this paper's result our estimated value of forecast-aware action is biased upward — which
is precisely the direction that would flatter WG-C-002.

## WildfireGuardian difference
**Requirement imposed on us:** (1) never report an identical-twin impact number as the
result; (2) if we run one, report it explicitly as an upper bound alongside a
non-identical result; (3) do not treat a plausible forecast-error growth rate as evidence
that the design is sound — this paper shows that check passes even when the impact is
biased.

## Novelty threat
BACKGROUND, but load-bearing: this is the citation that makes our OSSE design defensible,
and the citation a hostile reviewer would use against an identical-twin design.

## Quotes / page references
- "the identical twin produces a biased skill assessment, overestimating the improvement
  from assimilating sea surface height and sea surface temperature observations"
  (Abstract).
- Identical twin: "same model implementation but with perturbed initial, forcing or
  boundary conditions"; fraternal twin: "same model type ... but with sufficiently
  different configurations" (Introduction).
- "Such biases can lead to ... a misguided distribution of observing system investments"
  (Abstract).

## Follow-up papers
Cites Arnold & Dey (1986), Atlas (1997), Hoffman & Atlas (2016) as the atmospheric sources
of the identical-twin bias claim — all three recorded, all three **NEEDS_FULL_TEXT**
(cited here secondhand). Related: Halliwell et al. (2014); Privé et al. (2023).
