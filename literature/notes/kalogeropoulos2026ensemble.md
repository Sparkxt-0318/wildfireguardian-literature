# kalogeropoulos2026ensemble

## Citation
Kalogeropoulos, N.; Rein, G. (2026). "Defining probabilistic evacuation triggers for
wildfires using an ensemble of flame spread models: The Fort McMurray case study."
*Fire Safety Journal* 165: 104912. DOI 10.1016/j.firesaf.2026.104912

## Publication status
PEER_REVIEWED (journal article), issue dated 2026-11. OPEN ACCESS (hybrid).
Evidence level E2 — full abstract retrieved from OpenAlex; full text not read.

## Problem
A trigger boundary computed from one fire-spread model inherits that model's biases. Which
boundary should a planner believe?

## Method
Build evacuation trigger boundaries from a **multi-model ensemble of flame-spread models
with different computational approaches**, at landscape scale. The ensemble members named
in the abstract are **Farsite, Prometheus/WISE, ELMFIRE, Google EPD and EPD-ConvLSTM**
(i.e. physical/semi-empirical simulators *and* machine-learned emulators together).

## Data
The 2016 Fort McMurray wildfire, Alberta, Canada.

## Outputs
- Ensemble-derived probabilistic trigger boundaries
- A demonstration that individual models produce *different* boundaries, attributed to
  differences in fuel representation, fire dynamics and rate-of-spread prediction
- A negative operational finding: Fort McMurray's triggers "extend beyond practical
  detection distances under rapid fire spread conditions" — i.e. the trigger would have to
  fire before the fire could be detected

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Ensemble spread is treated as a usable proxy for predictive uncertainty. Egress only.

## Validation
Retrospective case study of a real dire evacuation.

## Limitations
Multi-model spread is not calibrated probability. No traffic, no responders, no dispatch.

## WildfireGuardian overlap
Three claims are hit at once:
- **WG-C-004** (probabilistic / multi-model-ensemble triggers) — fully occupied.
- **WG-C-014** — the paper already demonstrates that *which* spread model you use changes
  the decision object, which is the qualitative half of "spatial accuracy is not
  decision quality."
- **WG-C-009** — "which boundaries are robust across models" is close to robust
  protectability.
Its detection-distance finding also anticipates part of **WG-C-012**: a trigger that fires
before detection is possible is a *latency* failure, stated in print.

## WildfireGuardian difference
Kalogeropoulos & Rein show *that* models disagree and propagate that disagreement into a
boundary. WG-C-014's surviving form must be sharper and quantitative: a demonstrated
**non-monotonic** relationship between a spatial accuracy score (IoU/Jaccard) and a
decision-quality score, which this paper does not report. WG-C-012's surviving form must
treat latency as a swept variable, not a single observation about one town.

## Novelty threat
**level: CRITICAL** for WG-C-004; **HIGH** for WG-C-014 and WG-C-009; MODERATE for WG-C-012.
This is the single most dangerous 2026 paper in Category 1 and must be read in full
before any of those claims is stated aloud.

## Quotes / page references
Abstract: "By using an ensemble the resulting evacuation trigger boundaries are more robust
and comprehensive than those derived from any single model." (abstract via OpenAlex)
Abstract: "Fort McMurray's triggers extend beyond practical detection distances under
rapid fire spread conditions." (abstract via OpenAlex)

## Follow-up papers
NEEDS_FULL_TEXT — reference list not retrieved.
