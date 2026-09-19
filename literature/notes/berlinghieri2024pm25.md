# berlinghieri2024pm25

## Citation
Berlinghieri, R., D. R. Burt, P. Giani, A. Fiore, and T. Broderick:
Are Hourly PM2.5 Forecasts Sufficiently Accurate to Plan Your Day? Individual
Decision Making in the Face of Increasing Wildfire Smoke. arXiv:2409.05866.
DOI 10.48550/arXiv.2409.05866

## Publication status
**PREPRINT** (arXiv). Peer-review status not verified. Full text retrieved via
alphaXiv. Evidence level **E3**.

## Problem
Are operational air-quality forecasts good enough to support the concrete
decisions individuals actually make during wildfire-smoke episodes?

## Method
Evaluates six operational PM2.5 forecasts (HRRR-Smoke, GEOS-CF, CAMS, NAQFC,
Microsoft Aurora, HAQES) plus a **persistence baseline** (Ainslie et al.'s
recommendation: assume air quality stays constant for 24 h, anchored on an
AirNow monitor reading at 11 UTC). Two decision tasks:
1. *Whether* to go outside on a day that may exceed 35 ug/m3 — scored by a
   confusion matrix, precision and recall.
2. *When* to go outside for one hour — scored by a new metric, **Mean Excess
   Exposure (MEE)**: the PM2.5 actually experienced at the forecast-argmin hour
   minus the true daily minimum.

## Data
2023 US fire season; 5,031 urban-area-days across 30 census-division urban
areas; AirNow monitors as ground truth.

## Outputs
Task 1: of 219 high-PM2.5 days, only GEOS-CF, CAMS and HAQES had higher recall
than persistence (persistence: precision 0.908, recall 0.315). GEOS-CF's higher
recall came with 1,892 false positives. Conclusion: no forecast performed
substantially better than persistence for the go/no-go decision, in either the
Eastern or Western region.
Task 2: most forecasts beat persistence substantially on MEE, especially on
smoke days (GEOS-CF 10.84, CAMS 10.48, NAQFC 10.82 vs. persistence 19.27).

## Key equations
DEE(d,s) = PM2.5_{d,s}(argmin_h hat{PM2.5}_{d,s}(h)) - min_h PM2.5_{d,s}(h);
MEE = mean of DEE over a day set T.

## Assumptions
A rational individual acting on the forecast; a fixed 35 ug/m3 threshold;
monitor readings as truth.

## Validation
Real operational forecasts against real monitors. Strong empirical validation.

## Limitations
Individual exposure decisions, not evacuation. No spatial fire model. Preprint.

## WildfireGuardian overlap
Two overlaps that matter:
1. **WG-C-006**: it is an existing, wildfire-domain example of evaluating
   forecasts against a *decision task* using a *non-trivial baseline* (persistence)
   rather than a strawman. The "beat a strong simple baseline" evaluation
   standard is therefore not ours to claim as novel.
2. **WG-C-014**: the *same forecast set* ranks differently on the two decision
   tasks, and the San Francisco case shows a forecast that is better by
   conventional metrics failing the decision while persistence succeeds.

## WildfireGuardian difference
Persistence is a *forecast* baseline, not a *policy* baseline. WildfireGuardian's
comparator is a positional trigger/buffer whose parameter is optimised over the
scenario distribution — a different and stronger object. And the decision is a
routed mission with a deadline, not an hour-selection.

## Novelty threat
**HIGH** to WG-C-006 and WG-C-014; **MODERATE** to WG-C-002.

## Quotes / page references
"no forecast performance substantially better than the persistence baseline for
the task of deciding whether to go outside" (Appendix A.4, regional results).
"the persistence baseline captured elevated PM2.5 levels" (Sec. 5.1, San
Francisco case).

## Follow-up papers
- raeth2026decisionskill
- ardid2026forecastvalue
