# elmfire2025validation

## Citation
ELMFIRE Developers (2025). *ELMFIRE documentation: Validation* (version 2025.0212). https://elmfire.io/validation.html

## Publication status
**SOFTWARE_DOC.** Not peer-reviewed. This matters: it is the model's own self-assessment, published by its
developers. Cite it as documentation, never as an independent evaluation.

## Problem
How closely do ELMFIRE's simulated fire perimeters match observed historic fire perimeters, and how does that
compare with FARSITE?

## Method
Two validation tracks are documented:
1. **CONUS automated validation** — a large-scale historic wildfire dataset run through an automated pipeline
   ("Wildfire AV"), with per-fire overlap statistics aggregated. Fire count not stated on the page.
2. **Canada, Dogrib Fire (RWF085, 2001)** — a single-event comparison against Prometheus, focused on the
   16 October growth spurt (13:00-19:42 local).

## Data
Historic CONUS wildfire perimeters; the 2001 Dogrib Fire.

## Outputs
CONUS automated validation, mean values:

| Model | Jaccard | Sorensen | Cohen's kappa |
|---|---|---|---|
| ELMFIRE | 0.178 | 0.278 | 0.241 |
| FARSITE | 0.176 | 0.274 | 0.249 |

Dogrib: ELMFIRE predicted a significantly smaller fire than both Prometheus and the observed extent. With terrain
effects disabled, ELMFIRE and Prometheus were near-identical apart from flank spread — the divergence is
attributed to how each model derives directional spread rates from a point source, not to a deeper defect.

## Key equations
None given on the page (standard set-overlap coefficients).

## Assumptions
- Observed historic perimeters are truth.
- Default/automated parameterisation, i.e. no per-fire hand tuning.

## Validation
Self-validation by the model's developers.

## Limitations
- No sample size, no confidence intervals, no fuel-type breakdown on the page.
- Not peer-reviewed; numbers may change between documentation versions. Record the version (2025.0212).

## WildfireGuardian overlap
This is the cheapest and most striking single statement of operational spread-model error: **two of the most
widely used fire growth models agree with reality at a mean Jaccard index below 0.18.** Combined with
bennett2026wise (IoU 0.194 for W.I.S.E.), three independent operational models land in the same 0.17-0.20 range.
That convergence is the number WildfireGuardian should quote.

## WildfireGuardian difference
None — we consume this, we do not compete with it.

## Novelty threat
**BACKGROUND.**

## Quotes / page references
Validation page, CONUS section: "ELMFIRE seems to have a more balanced output with regards to over- or
underestimation of total fire area compared to Farsite".
Dogrib section: with terrain disabled the two models were "near identical (barring differences in flank fire)".

## Follow-up papers
- lautenberger2013elmfire (the model's primary citation).
- bennett2026wise (independent, peer-reviewed, much larger sample, same order of magnitude).
