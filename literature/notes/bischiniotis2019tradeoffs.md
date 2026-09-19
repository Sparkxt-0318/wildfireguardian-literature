# bischiniotis2019tradeoffs

## Citation
Bischiniotis, K., B. van den Hurk, E. Coughlan de Perez, T. Veldkamp,
G. G. Nobre, and J. Aerts, 2019: Assessing time, cost and quality trade-offs in
forecast-based action for floods. *International Journal of Disaster Risk
Reduction*, **40**, 101252. DOI 10.1016/j.ijdrr.2019.101252

## Publication status
Peer-reviewed journal (Elsevier). Bibliographic record verified via Crossref API.
Full text blocked (ScienceDirect 403; IIASA repository copy behind a bot wall).
Abstract/findings from publisher listing and the Zurich Climate Resilience
Alliance record. Evidence level **E2**. Flagged `NEEDS_FULL_TEXT`.

## Problem
Forecast skill decreases with lead time, but early actions need time to be
effective. When should an early-warning-early-action system pull the trigger?

## Method
Assessment of early warning / early action systems (EWEAS) in one-stage and
two-stage configurations, with potential-economic-value style accounting over
forecast quality, action cost and action effectiveness.

## Data
Flood case study (region and dataset NEEDS_FULL_TEXT).

## Outputs
The **optimal lead time to trigger action** as a function of forecast quality,
local geographic conditions, and the operational characteristics of the actions.
Finding that low-certainty long-lead forecasts become valuable when paired with
short-lead high-quality ones in a two-stage action design.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Forecast skill monotonically degrades with lead time; action effectiveness is a
function of the time available to execute it; costs are additive.

## Validation
Retrospective flood case study. NEEDS_FULL_TEXT for the verification design.

## Limitations
Actions are generic preparedness measures with an execution duration, not a
routed mission on a network. "Timeliness" here means forecast *lead time*, not
observation-to-product *latency*.

## WildfireGuardian overlap
Directly overlaps **WG-C-012**. It treats the timing dimension of the forecast as
a first-class decision variable, jointly with skill, and solves for the trigger
lead time. It also anticipates the WildfireGuardian intuition that the action's
own duration sets what lead time is usable.

## WildfireGuardian difference
Two operational distinctions survive:
1. **Latency vs. lead time.** Bischiniotis et al. optimise the *lead time at
   which to act*. WildfireGuardian's WG-C-012 as written concerns *latency* —
   the delay between observation and forecast availability — which shortens the
   usable decision window independently of skill. This distinction must be
   written into the claim or WG-C-012 collapses into this paper.
2. **Action duration is a routed round trip** with fire-arrival feasibility on
   every leg, not a scalar execution time.

## Novelty threat
**HIGH** to WG-C-012. The "lead time as a decision variable jointly with skill"
formulation is occupied in floods. WG-C-012 must be re-scoped to latency
specifically, or downgraded.

## Quotes / page references
Short quote relayed from the publisher/alliance record (E2, not page-verified):
"an inherent trade-off between timeliness and accuracy exists".

## Follow-up papers
- lopez2020bridging (same group; magnitude x probability x lead-time trigger selection)
- macleod2021anticipatory
- regnier2006dynamic (the hurricane analogue)
