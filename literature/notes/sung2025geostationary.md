# sung2025geostationary

## Citation
Sung, Taejun; Lee, Garyung; Kim, Doeun; Kim, Woohyeok; Yang, Seyoung; Im, Jungho (2025).
"Real-Time Wildfire Monitoring via Geostationary Satellite and Artificial Intelligence:
Insights from the March 2025 South Korea Wildfires." *Korean Journal of Remote Sensing*
(한국원격탐사학회지) 41(3): 565–580. DOI 10.7780/kjrs.2025.41.3.6. Diamond OA (CC-BY-NC).

Author-name discrepancy logged: the journal page renders author 5 as "Seyoung Yang",
OpenAlex as "Shiren Yang". The journal page is taken as authoritative.

## Publication status
**PEER_REVIEWED.** Korean-domiciled journal; article **language: English**.

## Problem
How quickly are Korean wildfires actually detected from space, and does a geostationary +
AI pipeline close the latency gap left by polar-orbiting sensors?

## Method
Comparison of five fire-detection products over the March 2025 South Korea wildfires,
including a LightGBM-based detector on GK-2A AMI, against reference fire records; detection
delay measured per event.

## Data
GK-2A AMI (LGBM and FF products), Himawari AHI WLF, MODIS AF, VIIRS AF; March 2025 Korean
wildfire events.

## Outputs
Mean detection delay:
| Product | Mean delay |
|---|---|
| AMI LGBM | **12.9 min** |
| AHI WLF | 16.3 min |
| AMI FF | 18.2 min |
| MODIS AF | 210.1 min |
| VIIRS AF | 318.1 min |

For the Uiseong fire specifically (reported at **99,289 ha**, "the largest in the country's
history"): geostationary detection in **22–36 min**, polar-orbiting in **93–196 min**.
Geostationary platforms captured a rapid eastward spread that polar-orbiting sensors missed
during evening hours.

## Key equations
Detection delay = detection timestamp − reference ignition/report timestamp (exact reference
definition NEEDS_FULL_TEXT). ML detector is LightGBM on AMI channels.

## Assumptions
Reference fire records give a trustworthy ignition time; per-event delays are comparable
across sensors despite differing overpass geometry.

## Validation
Real events, March 2025; detection products scored against official records.

## Limitations
Detection latency only — not forecast latency, and not forecast skill. The paper does not
convert any of these minutes into a decision consequence.

## WildfireGuardian overlap
Directly supplies the **latency term** in WG-C-012. A Korean evacuation rule that grants a
5-hour lead time is, in practice, operating on information that is already 13–320 minutes
old depending on the sensor — a 5-hour budget shrinks to ~4.7 h at best and ~2.7 h at worst
before anything else happens. That arithmetic is exactly WG-C-012's claim, in Korean
numbers, and it is *not* made in this paper.

## WildfireGuardian difference
Sung et al. measure latency; WildfireGuardian prices it. "How late is the observation" and
"at what latency does the observation stop being worth acting on" are different quantities
with different units.

## Novelty threat
**MODERATE for WG-C-012 (as an input, not an occupation); LOW for WG-C-007.** The paper
does not establish any decision-value boundary, so WG-C-012 survives — but the program must
cite these numbers rather than generate its own, or it will look like it ignored the Korean
measurement that already exists.

## Quotes / page references
> "geostationary satellite products enabled relatively rapid detection, with average delays
> between 12 and 18 minutes" (abstract/results).
> Uiseong described as "the largest in the country's history" at "99,289 hectares."
Page range 565–580; exact page for each quotation NEEDS_FULL_TEXT.

## Follow-up papers
- Any work converting Korean detection latency into evacuation decision value — none found.
- `mois2025evacuationstages` (the 5 h / 8 h budget these latencies consume).
