# halliwell2014fraternal

## Citation
Halliwell, G. R., Srinivasan, A., Kourafalou, V., Yang, H., Willey, D., Le Hénaff, M., &
Atlas, R. (2014). Rigorous Evaluation of a Fraternal Twin Ocean OSSE System for the Open
Gulf of Mexico. *Journal of Atmospheric and Oceanic Technology*, 31(1), 105–130.
DOI: 10.1175/JTECH-D-13-00011.1

## Publication status
Published, peer-reviewed (AMS). Metadata verified via Crossref; abstract retrieved via
Consensus. Full text not retrieved — evidence level E2.

## Problem
OSSE-derived observation-impact estimates are only useful if the OSSE system itself is
known not to over- or under-state impact. Atmospheric OSSE practice had developed design
criteria and validation procedures; ocean OSSEs had not applied them.

## Method
Builds and then *validates* a fraternal-twin OSSE. Three components:
1. a **nature run** (NR) stipulated as truth;
2. a **forecast model** — the same model type as the NR but differently configured — plus
   a data assimilation system;
3. software to **simulate observations** from the NR and add realistic errors.

Validation strategy: run real Observing System Experiments (OSEs) with real observations,
then run OSSEs that are identical except that synthetic observations are assimilated, and
require the OSE–OSSE impact pairs to match.

## Data
Gulf of Mexico ocean model output (nature run) and real ocean observing networks for the
OSE side.

## Outputs
A validated OSSE system, plus — the reusable contribution — an explicit list of design
requirements: NR realism against climatology and variability; forecast-model error growth
matched to the growth of errors between real state-of-the-art models and the real ocean;
realistic simulated observation errors; OSE–OSSE agreement as the acceptance test.

## Key equations
None extracted (full text not retrieved).

## Assumptions
That agreement between OSE and OSSE impact for *existing* observing systems licenses
belief in the OSSE's impact estimate for a *hypothetical* one.

## Validation
This is the paper's whole point: OSSE validation by OSE benchmarking, which removed the
need for post hoc calibration of impact magnitudes.

## Limitations
- Ocean domain; fraternal (same model type), not nonidentical.
- Requires a real OSE to exist. **We have no real OSE for wildfire evacuation decisions.**

## WildfireGuardian overlap
This is the design template for WG-C-010. Our nature run is a fire scenario generator; our
"forecast model" is the spread model the decision policy consumes; our "observations" are
whatever fire-state information the policy receives.

## WildfireGuardian difference
**Requirement imposed on us — and a hard constraint:** the acceptance test used here
(OSE–OSSE agreement) is unavailable to us, because there is no real observing-system
experiment for wildfire evacuation decision quality to benchmark against. Therefore we
must either (a) find a weaker but real anchor — e.g. reproduce a documented fire's
observed arrival timing with the forecast model and report its error — or (b) state
plainly that our OSSE is **uncalibrated** and that impact magnitudes are not to be read as
real-world magnitudes, only orderings. Option (b) is honest and is what
PROJECT_CONTEXT's transfer-assumption rule already demands. Claiming a calibrated OSSE
without an anchor would be the single most attackable sentence in the program.

## Novelty threat
BACKGROUND.

## Quotes / page references
- "These procedures are necessary to determine a priori that the OSSE system does not
  overestimate or underestimate observing system impacts" (Abstract).
- The forecast model is configured so that "errors ... grow at the same rate as errors
  that develop between state-of-the-art ocean models and the true ocean" (Abstract).

## Follow-up papers
Errico et al. (2013) QJRMS 139(674):1162–1178; Hoffman & Atlas (2016) BAMS 97(9):1601–1616;
Yu et al. (2019) Ocean Science 15(6):1801–1814; Privé et al. (2023) Tellus A 75(1):309–333.
All recorded.
