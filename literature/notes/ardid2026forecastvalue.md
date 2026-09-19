# ardid2026forecastvalue

## Citation
Ardid, A., A. Power, A. Valencia, H. G. Pearce, S. Gross, D. Dempsey, and
M. M. Boer, 2026: From forecast skill to economic value: sub-hourly wildfire
potential forecasting across Australian regions. *International Journal of
Wildland Fire*, **35**(4), WF25221. DOI 10.1071/WF25221

## Publication status
Peer-reviewed journal (CSIRO / ConnectSci). Metadata and abstract retrieved from
the FRAMES catalog record and the ConnectSci listing. Full text not read.
Evidence level **E2**. Flagged `NEEDS_FULL_TEXT`.

## Problem
Operational fire forecasts rely on daily indices that miss rapid sub-daily
weather shifts; and forecast skill improvements are not routinely translated
into economic terms.

## Method
Machine-learning classifiers trained on sub-hourly Automatic Weather Station
data from three Australian regions (Sunshine Coast, Brisbane, Hobart),
benchmarked against the Fire Behaviour Index (FBI). Discrimination assessed by
true-positive / false-positive rates; value assessed by **Potential Economic
Value (PEV)**, i.e. the Richardson/Zhu cost-loss apparatus. Learning-curve tests
included.

## Data
Sub-hourly AWS observations, three Australian regions.

## Outputs
ML improves forecast skill over FBI by 10-30%; the ML system roughly doubles
potential savings relative to FBI under the cost-loss framework.

## Key equations
PEV / cost-loss (standard form). NEEDS_FULL_TEXT for the exact specification.

## Assumptions
Binary fire-potential event; a cost-loss user characterised by C/L; FBI as the
operational reference.

## Validation
Real weather-station data, retrospective. Not a decision trial.

## Limitations
No reported skill *threshold* or boundary at which forecast-based action starts
to beat the reference. FBI is an operational index, and the retrieved record
does not indicate it was re-tuned to the same scenario distribution.

## WildfireGuardian overlap
This is **the wildfire instantiation of the forecast-skill-to-economic-value
pipeline**. It is the single most direct answer to "has anyone done cost-loss
forecast value in wildfire?" — yes, in 2026, in IJWF.

## WildfireGuardian difference
Operationally distinct on three axes:
1. **Decision modelled**: fire-potential warning / preparedness posture, not
   protective-action timing for residents or responder dispatch.
2. **Comparator**: FBI, an operational danger index. WildfireGuardian's stated
   comparator is a *trigger/buffer policy whose buffer distance or lead time is
   optimised over the same scenario distribution the forecast-aware policy sees*.
   Those are not the same comparator and not the same standard of rigour.
3. **Output**: a value ratio, not a boundary in (skill, lead time, latency) space.

## Novelty threat
**HIGH** to WG-C-002. It does not kill WG-C-002, but it forecloses the sentence
"no one has applied forecast-value theory to wildfire". WG-C-002 must be stated
as a boundary against a tuned positional-trigger comparator or it is redundant.

## Quotes / page references
Relayed from the FRAMES/ConnectSci record (E2): "the ML system doubling
potential savings relative to the FBI".

## Follow-up papers
- richardson2000relative, zhu2002economic (the PEV machinery used here)
- Sub-hourly fire potential ML precursor: *Sub-hourly forecasting of fire
  potential using machine learning on time series of surface weather variables*,
  International Journal of Wildland Fire, DOI 10.1071/WF24113 (authors/year
  NOT verified — search lead only).
