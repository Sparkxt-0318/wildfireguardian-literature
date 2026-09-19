# kalogeropoulos2025dire

## Citation
Kalogeropoulos, N.; Mitchell, H.; Kuligowski, E.; Ronchi, E.; Rein, G. (2025).
"Quantifying dire evacuations in case of wildfire using trigger boundaries and case study
of the 2018 Mati wildfire in Greece." *Safety Science* 181: 106691.
DOI 10.1016/j.ssci.2024.106691 (Crossref issue date 2025-01.)

## Publication status
PEER_REVIEWED (journal article). OPEN ACCESS (hybrid). Evidence level E2 — full abstract
via OpenAlex.

## Problem
"Dire evacuation" was used informally in the literature with no quantitative definition.

## Method
Treats **both wildfire spread and evacuation time as probabilistic variables** and defines
an **evacuation safety factor** ranging from 1 (no risk of a dire evacuation) to 0 (100%
risk). A trigger boundary is then "the latest wildfire location with a low risk of a dire
evacuation."

## Data
2018 Mati wildfire, Greece (104 fatalities), used as a forensic case.

## Outputs
- A scalar safety factor per community/time
- The finding that Mati's safety factor was already well below 1 at the moment of
  detection, i.e. the evacuation was doomed from first detection

## Key equations
The safety factor's definition. NEEDS_FULL_TEXT.

## Assumptions
Both distributions are available and independent enough to combine; egress only.

## Validation
Forensic reconstruction of a real fatal event.

## Limitations
Single case. No traffic network. No responder. The safety factor is about the *community*,
not about any individual resident or vehicle.

## WildfireGuardian overlap
This is the closest published relative to WildfireGuardian's *output type*: a scalar,
probabilistic, decision-relevant statement of "will this protective action complete in
time?" It also occupies "latest X with acceptable failure probability," which is the
shape of WG-C-003's sentence.

## WildfireGuardian difference
Their latest-X is a **fire location** for community egress. WG-C-003's latest-X is a
**clock time for a responder to depart**, feasible only if base→resident, pickup dwell and
resident→destination all close under fire arrival. Kalogeropoulos et al. have one leg;
WG-C-003 has three, one of which runs toward the fire.
Also: their probability comes from historic variability, not from a forecast whose skill is
swept — which is where WG-C-002 still has room.

## Novelty threat
**level: CRITICAL** for WG-C-004; **HIGH** for WG-C-002 (occupies the "probability of
protective-action failure" output, though not the forecast-skill boundary).

## Quotes / page references
Abstract: "an evacuation safety factor to assess the likelihood of a dire evacuation."
(abstract via OpenAlex)
Abstract: "Trigger boundaries thus define the latest wildfire location with a low risk of a
dire evacuation." (abstract via OpenAlex)

## Follow-up papers
kalogeropoulos2026ensemble.
