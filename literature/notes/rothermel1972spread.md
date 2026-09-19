# rothermel1972spread

## Citation
Rothermel, R. C. (1972). *A mathematical model for predicting fire spread in wildland fuels.* Research Paper INT-RP-115. Ogden, UT: U.S. Department of Agriculture, Forest Service, Intermountain Forest and Range Experiment Station. 40 p. https://doi.org/10.2737/INT-RP-115

## Publication status
**GOVERNMENT_REPORT** (USDA Forest Service Research Paper). **Not a peer-reviewed journal article.**
This must be stated correctly in any related-work section; describing Rothermel 1972 as a peer-reviewed paper is a
factual error a judge can catch. Verified from the USDA FS TreeSearch record (32533).

## Problem
Predict the steady-state rate of spread and intensity of a surface fire in wildland fuels from measurable fuel,
moisture, wind and slope properties.

## Method
Quasi-empirical energy-balance formulation. Laboratory fuel beds of uniform particles were burned across a wide
range of bulk densities; three fuel sizes were used (0.026-inch square-cut excelsior, 1.5-inch sticks, 1.75-inch
sticks). Coefficients were fitted to these beds and then generalised to hypothetical "fuel models".

## Data
Laboratory fuel-bed burns; no wildfire observations.

## Outputs
Steady-state surface rate of spread and reaction intensity; the basis of the U.S. National Fire Danger Rating
System and, downstream, of BEHAVE, FARSITE, FlamMap, ELMFIRE and the surface component of WRF-SFIRE.

## Key equations
The spread-rate equation (propagating flux / heat sink form) with wind and slope coefficients. Full symbol-by-
symbol exposition is in andrews2018rothermel (RMRS-GTR-371), which is the document to cite for the equations.

## Assumptions
These are the assumptions WildfireGuardian inherits by transitivity through every simulator listed above:
1. **Steady state.** The fire is spreading at equilibrium. Acceleration, and the surge behaviour that kills people,
   is outside the model.
2. **Continuous, homogeneous, contiguous surface fuel bed.** Real landscapes are patchy.
3. **Surface fire only.** Crown fire and spotting are bolted on by later models, not by this one.
4. **Fitted on uniform laboratory fuel arrays**, not on field or wildfire data.
5. **Wind is a single effective value**, not a turbulent, terrain-channelled field.

## Validation
Demonstration against hypothetical fuel models in the report itself. Subsequent independent evaluation is
overwhelmingly negative on non-US and live fuels (see weise2016chaparral, zhang2023karst, cruz2013uncertainty).

## Limitations
The model is 1972 laboratory physics extrapolated worldwide for five decades. Its failure modes on live fuels
(weise2016chaparral) and on East Asian fuel complexes (zhang2023karst and the Pinus koraiensis recalibration
series) are documented and large.

## WildfireGuardian overlap
Every forecast WildfireGuardian consumes traces back to this equation. The steady-state and homogeneous-fuel
assumptions propagate into our arrival-time fields and therefore into our dispatch deadlines.

## WildfireGuardian difference
We do not modify or extend this model. Saying so plainly is part of PROJECT_CONTEXT's "what WildfireGuardian is
NOT".

## Novelty threat
**BACKGROUND.**

## Quotes / page references
TreeSearch record 32533 bibliographic entry: "Res. Pap. INT-RP-115. Ogden, UT ... 40 p."

## Follow-up papers
- andrews2018rothermel (RMRS-GTR-371) — the equation reference.
- finney1998farsite (RMRS-RP-4) — the two-dimensional growth engine built on it.
- cruz2013uncertainty, weise2016chaparral — how wrong it is in practice.
