# hall2023geostationary

## Citation
Hall, J. V., Schroeder, W., Rishmawi, K., Wooster, M., Schmidt, C. C., Huang, C., Csiszar, I., & Giglio, L. (2023). Geostationary active fire products validation: GOES-17 ABI, GOES-16 ABI, and Himawari AHI. *International Journal of Remote Sensing*, 44(10), 3174-3193. https://doi.org/10.1080/01431161.2023.2217983

## Publication status
PEER_REVIEWED, Open Access (CC-BY, Taylor & Francis). Crossref-verified; **full text extracted locally** from the
NOAA Institutional Repository copy (item 53332), so the numbers below are **E1** (read in the source text).

## Problem
How accurate are the operational geostationary active fire products — NOAA's Fire Detection and Characterization
(FDC) and the LSA-SAF FRP-PIXEL product — when compared against a higher-resolution reference?

## Method
Comparison against Landsat active fire detections acquired simultaneously (within ±5 minutes of the geostationary
observation), across two seasons: 1 Jan-31 Mar 2020 and 1 Jul-30 Sep 2020. Detection rate expressed as a function
of fire fractional area, assuming each Landsat OLI reference fire pixel corresponds to 900 m² of active fire, so
that products with different pixel sizes can be compared.

## Data
GOES-16 ABI, GOES-17 ABI, Himawari AHI, MSG SEVIRI; Landsat-8 OLI reference detections.

## Outputs
- **False alarm rates for high-confidence pixels: 4-7% (FDC), 2-6% (FRP-PIXEL)**, depending on season and disk.
- FDC false alarms fell from **48% (summer 2018) to 4% (summer 2020)** after algorithm changes — the older
  literature's numbers are obsolete.
- Complementary behaviour: FRP-PIXEL has fewer false alarms but a lower detection rate; FDC detects more fire
  pixels at a much higher false alarm rate.
- **Cadence, stated in Section 2.1:** ABI FDC every 10 minutes full disk, every 5 minutes CONUS/PACUS, and every
  30-60 seconds for the mesoscale sector; full disk was 15 minutes before April 2019. MSG FRP-PIXEL every 15
  minutes. FDC product resolution 2 km.
- **Geolocation:** ABI fire pixel locations are not terrain-corrected.

## Key equations
Detection-rate-vs-fire-fractional-area curves; no closed-form equations needed.

## Assumptions
- Landsat OLI detections are reference truth.
- The 900 m² filled-pixel assumption is acknowledged by the authors as usually wrong, and is used only to
  normalise across pixel sizes.

## Validation
This is the validation paper.

## Limitations
No Korean or GK2A coverage — GK2A is absent from this assessment. Korean numbers must come from sung2025geostationary.

## WildfireGuardian overlap
Fixes two of the three columns of the Category 7 observation table (cadence and detection reliability) with
peer-reviewed numbers, and supplies a terrain-specific caveat that matters enormously for Korea.

## WildfireGuardian difference
None; consumed as input constraint.

## Novelty threat
**BACKGROUND.**

## Quotes / page references
Abstract: "low false alarm rates, ranging between 4%-7% (FDC) and 2%-6% (FRP-PIXEL)".
Abstract: "48% false alarms in summer 2018 compared to 4% in summer 2020 for high confidence pixels".
Section 2.1: "Fire pixel locations are not terrain-corrected" and the resulting positioning error "can be on the
order of several kilometres depending on terrain elevation and view zenith angle."

## Follow-up papers
- sung2025geostationary (the Korean geostationary analogue).
- paugam2026mtgfci (turning geostationary cadence into rate-of-spread).
- Hall et al. (2019), the earlier validation the 48%→4% comparison refers to — not yet retrieved.
