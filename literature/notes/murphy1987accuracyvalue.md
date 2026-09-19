# murphy1987accuracyvalue

## Citation
Murphy, A. H., and M. Ehrendorfer, 1987: On the Relationship between the Accuracy
and Value of Forecasts in the Cost-Loss Ratio Situation. *Weather and Forecasting*,
**2**(3), 243-251. DOI 10.1175/1520-0434(1987)002<0243:OTRBTA>2.0.CO;2

## Publication status
Peer-reviewed journal (AMS). Bibliographic record verified via Crossref API,
2026-09-19. **Abstract and full text NOT retrieved** — evidence level E1
(bibliographic only). See `novelty/OPEN_QUESTIONS.md`.

## Problem
Whether increases in forecast accuracy necessarily increase forecast value to a
decision maker operating in the cost-loss ratio situation.

## Method
Analytical treatment of the two-action/two-event cost-loss decision model with
accuracy characterised by the joint distribution of forecasts and observations.
(Method described from title and from the way the paper is cited in the later
forecast-value literature — NEEDS_FULL_TEXT to state the derivation.)

## Data
UNKNOWN — NEEDS_FULL_TEXT.

## Outputs
Conditions under which accuracy and value are, and are not, monotonically
related. NEEDS_FULL_TEXT for the exact conditions.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Cost-loss payoff structure; a decision maker who acts optimally given the
forecast; binary event. (Standard for this literature; NEEDS_FULL_TEXT.)

## Validation
Analytical, plus (per the companion literature) illustrative forecast sets.
NEEDS_FULL_TEXT.

## Limitations
No spatial hazard field. No mission-feasibility decision. Scalar accuracy
measures only — nothing about spatial overlap metrics.

## WildfireGuardian overlap
This is the canonical statement of the proposition underlying **WG-C-014**:
predictive accuracy is not monotone with decision quality. The proposition is
1987 prior art in general form.

## WildfireGuardian difference
WildfireGuardian's version is specific: the accuracy metric is a *spatial*
overlap statistic (IoU/Jaccard between predicted and actual burned area) and the
decision quality is *mission feasibility* (does the responder round trip close).
Murphy & Ehrendorfer studied scalar accuracy of a binary forecast against a
scalar cost-loss payoff. Those are different objects with different failure
mechanisms — theirs is payoff-asymmetry driven, ours would be geometry driven
(a perimeter error in the direction of the access road matters; the same area of
error elsewhere does not).

## Novelty threat
**HIGH** to WG-C-014. The general claim is occupied. Only the wildfire-spatial
instantiation and the specific mechanism can survive, and only if we state the
mechanism, not the slogan.

## Quotes / page references
No quotes — full text not retrieved. Title is itself the load-bearing evidence:
"On the Relationship between the Accuracy and Value of Forecasts".

## Follow-up papers
- chen1987qualityvalue (generalised N-action version, same year)
- richardson2000relative, zhu2002economic (REV as the operational form)
- raeth2025decisionskill, mandi2024dfl (the ML-era restatement)
