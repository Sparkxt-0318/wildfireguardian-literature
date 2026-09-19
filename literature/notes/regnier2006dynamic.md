# regnier2006dynamic

## Citation
Regnier, E., and P. A. Harr, 2006: A Dynamic Decision Model Applied to Hurricane
Landfall. *Weather and Forecasting*, **21**(5), 764-780. DOI 10.1175/WAF958.1

## Publication status
Peer-reviewed journal (AMS). Bibliographic record verified via Crossref API.
Abstract obtained as a search-engine paraphrase, not read from the publisher
page (AMS returned 403). Evidence level **E2**.

## Problem
Hurricane preparation is usually framed as a *static* cost-loss decision on the
current strike probability. That framing ignores that the decision maker will
receive better forecasts later, and that preparation is irreversible.

## Method
Reframes preparation as a sequence of interrelated decisions in which the
decision maker explicitly anticipates and plans for future forecasts whose
accuracy improves as lead time declines. A discrete Markov model of hurricane
travel, derived from historical tracks, supplies the forecast-evolution process.

## Data
Historical Atlantic tropical cyclone tracks (per abstract paraphrase).

## Outputs
The additional value extractable from *existing* forecasts by anticipating
updates, rather than committing on the instantaneous strike probability.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Markovian storm motion; irreversible preparation cost; a decision maker who
optimises expected cost; forecast accuracy is a known decreasing function of
lead time.

## Validation
Historical-track-driven simulation. No real deployment.

## Limitations
Single protective action with a scalar cost. No transport network, no mission
that must physically complete, no inbound leg.

## WildfireGuardian overlap
Owns **"act now vs. wait for a better forecast"** as a formal decision problem
in which *forecast quality is indexed by lead time*. This is a large part of what
WG-C-002 and WG-C-012 describe.

## WildfireGuardian difference
Regnier & Harr's waiting cost is the loss of preparation *time* against a scalar
clearance requirement. WildfireGuardian's waiting cost is the loss of
*mission feasibility*: a responder round trip (base -> resident -> pickup ->
destination) whose every leg must remain traversable ahead of a modelled fire
front. The decision variable is a dispatch time for a specific vehicle, not a
binary prepare/don't-prepare.

## Novelty threat
**HIGH** to WG-C-012 and WG-C-002 in their general form. "We treat the value of
waiting for a better forecast" is not claimable.

## Quotes / page references
No verbatim quotes (full text not retrieved).

## Follow-up papers
- regnier2008public (the location-specific false-alarm/lead-time boundary)
- georgakakos2025evacuationtiming (same structure, 2025, with a completion-time term)
- bischiniotis2019tradeoffs (the flood/humanitarian version)
