# allaire2020ensemble

## Citation
Allaire, F., Filippi, J.-B., & Mallet, V. (2020). Generation and evaluation of an ensemble of wildland fire simulations. *International Journal of Wildland Fire*, 29(2), 160-173. https://doi.org/10.1071/wf19073

## Publication status
PEER_REVIEWED. Crossref-verified. Evidence level **E2** — abstract only.

## Problem
Fire simulation inputs (weather forecast, fuel parameterisation, fire characteristics) are uncertain. How should
that uncertainty be propagated, summarised, and *scored*?

## Method
Probability distributions are assigned to the inputs; uncertainty is propagated by running hundreds of Monte Carlo
simulations. The ensemble is summarised as a burn probability map. Probabilistic scores standard in meteorological
verification are defined and applied, together with a set of desired ensemble properties.

## Data
Seven fires in Corsica, mid-2017 to early 2018.

## Outputs
Burn probability maps with proper probabilistic scores. Performance reported as "fair in some of the cases", with
accuracy and reliability both identified as needing improvement. The authors state ensemble generation takes a
reasonable amount of time and **could be used operationally given sufficient computational resources**, and that
the scores are also suitable as a calibration objective.

## Key equations
Standard probabilistic verification scores (Brier-family / reliability decomposition); specific forms not retrieved.

## Assumptions
- Input distributions are specifiable.
- Observed burned surface is truth for scoring.

## Validation
Seven real fires — genuinely validated against reality, unusually for this literature.

## Limitations
Single-model ensemble (input uncertainty only). Does not span structural model error, which
kalogeropoulos2026ensemble shows is large.

## WildfireGuardian overlap
This is the paper that imports forecast-verification discipline into wildfire. It matters for WG-C-002 and
WG-C-006 because it establishes that *scoring the forecast properly* is already normal practice in wildfire.

## WildfireGuardian difference
Allaire et al. score the forecast. WildfireGuardian scores the decision the forecast supports, against a tuned
positional-trigger comparator. Proper scores are forecast-side; our comparator is decision-side. The distinction
survives, but it means our contribution cannot be "we score probabilistically".

## Novelty threat
**MODERATE for WG-C-004.** Single-model probabilistic burn maps exist and are scored; combined with
ramirez2019stochastic (probabilistic trigger buffers) and kalogeropoulos2026ensemble (multi-model ensemble
triggers), the probabilistic/ensemble trigger space is fully occupied.

## Quotes / page references
Abstract: "The ensemble generation can be accomplished in a reasonable amount of time and could be used in an
operational context provided that sufficient computational resources are available."
Abstract: "We obtain fair performance in some of the cases but accuracy and reliability of the forecasts can be
improved."

## Follow-up papers
- allaire2021emulation (same group; emulation to make the ensemble affordable).
- kalogeropoulos2026ensemble (multi-model rather than multi-input).
