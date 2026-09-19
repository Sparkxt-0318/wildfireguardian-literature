# bouttier2024optimal

## Citation
Bouttier, F., and H. Marchal, 2024: Probabilistic short-range forecasts of
high-precipitation events: optimal decision thresholds and predictability limits.
*Natural Hazards and Earth System Sciences*, **24**(8), 2793-2816.
DOI 10.5194/nhess-24-2793-2024

## Publication status
Peer-reviewed journal (Copernicus, open access). Article page retrieved and read
via WebFetch. Evidence level **E2/E3**.

## Problem
How should ensemble precipitation predictions be converted into categorical
warnings, and where are the limits of usable skill?

## Method
User-oriented verification. Two hypothetical user types with different
miss/false-alarm preferences. Optimal probability decision thresholds p_opt
obtained by maximising the Equitable Threat Score or the F2 score. Skill examined
across spatial scales, precipitation intensities and forecast ranges 9-36 h.
Comparator: the deterministic AROME control forecast.

## Data
AROME ensemble precipitation forecasts (France).

## Outputs
- Explicit tuned thresholds, e.g. "the optimal forecast strategy for user L is to
  set the decision threshold to p_opt(ETS) = 0.3".
- A **usability boundary**: "the highest usable precipitation intensities have
  return periods of a few years only, with resolution limited to several tens of
  kilometres"; skill deteriorates sharply below 20 km for intense precipitation.
- Ensembles objectively outperform the deterministic control.
- Scores nearly independent of forecast range from 9 to 36 h (~10% degradation).

## Key equations
ETS, F2, threshold optimisation. See paper.

## Assumptions
Two stylised user types; categorical warning as the decision.

## Validation
Retrospective verification against observations.

## Limitations
The decision is "issue a categorical warning", not a protective-action mission.
The comparator is a competing forecast, not a non-forecast policy.

## WildfireGuardian overlap
This paper does, for precipitation, two of the three things WG-C-002 promises:
it **tunes** the decision threshold per user, and it reports a **boundary**
beyond which the forecast is not usable. It also directly contradicts the naive
assumption that skill degrades fast with lead time in the short range.

## WildfireGuardian difference
The tuned object is a *probability threshold*, not a *spatial buffer distance or
trigger lead time*. WildfireGuardian's comparator class (positional triggers) does
not exist in precipitation warning. And the boundary here is in
(intensity, spatial scale) space, not in (skill, lead time, latency) space.

## Novelty threat
**HIGH** to WG-C-002 and WG-C-006 as general claims: "we tune the decision
threshold and report the skill boundary" is standard practice.

## Quotes / page references
"the optimal forecast strategy for user L is to set the decision threshold to
p_opt(ETS)=0.3" (retrieved from article page; section not page-verified).
"the highest usable precipitation intensities have return periods of a few years
only" (conclusions).

## Follow-up papers
- richardson2000relative
- lopez2020bridging
