# sun2025decisionfocusedsensing

## Citation
Sun, Q., G. Hults, and S. Xu, 2025: Decision-focused Sensing and Forecasting for
Adaptive and Rapid Flood Response: An Implicit Learning Approach. In *BuildSys
'25: Proceedings of the 12th ACM International Conference on Systems for
Energy-Efficient Buildings, Cities, and Transportation*, Golden, CO, USA,
19-21 November 2025, 117-127. DOI 10.1145/3736425.3770102

## Publication status
**Peer-reviewed conference paper** (ACM). Not a journal article. Full text
retrieved via alphaXiv; bibliographic record confirmed via Crossref API.
Evidence level **E3**.

## Problem
Traditional disaster pipelines place sensors to maximise *overall information
gain* and train forecast models to minimise *average forecasting error*, then
optimise response decisions downstream. Both upstream objectives are decision
task-agnostic.

## Method
End-to-end differentiable pipeline with four components: a contextual scoring
network; a differentiable sensor-selection module under a hard budget constraint
(discrete selection made learnable via Implicit Maximum Likelihood Estimation,
I-MLE); a spatio-temporal flood reconstruction/forecasting model; and a
differentiable decision layer with probabilistic decision heads approximating
constrained disaster-response tasks. Trained to minimise **downstream decision
regret**, not proxy prediction loss.

## Data
Real-world flood scenarios (specific datasets NEEDS_FULL_TEXT).

## Outputs
Outperforms baselines on **both** state prediction accuracy and decision quality;
final task metrics optimised directly are evacuation and relocation cost.

## Key equations
I-MLE gradient estimator over discrete sensor configurations; decision-regret
loss. NEEDS_FULL_TEXT for exact forms.

## Assumptions
Known downstream decision objective; hard sensor budget; differentiable
relaxation of the decision layer is faithful.

## Validation
Real flood scenarios, retrospective, against information-gain and average-error
baselines.

## Limitations
Flood depth field, not a fire front. No deadline in the mission sense — the
decision is evacuation/relocation cost, not whether a round trip closes in time.

## WildfireGuardian overlap
This paper occupies **almost exactly what WG-C-008 describes**, in floods:
select observations by their effect on the evacuation decision, explicitly
rejecting predictive-accuracy and information-gain criteria. It also states
WG-C-014's proposition as its motivation.

## WildfireGuardian difference
1. Hazard: flood depth (a slowly evolving scalar field) vs. fire arrival time (a
   propagating front with a strong directional structure relative to roads).
2. The decision objective is a *cost*, not a *feasibility deadline*; there is no
   responder ingress leg and no "mission closes / does not close" discontinuity.
3. Sensing here is *placement* of static in-situ sensors under a budget, not
   *tasking under a deadline* where an observation that arrives after the
   dispatch time has zero value.

## Novelty threat
**CRITICAL** to WG-C-008. It forecloses methodological novelty entirely and
forecloses "decision-directed sensing for hazard evacuation" as a general
application claim. What remains for WildfireGuardian is (a) the wildfire hazard
and (b) the *deadline* structure — an observation's value depends on whether it
arrives before the dispatch-by time.

## Quotes / page references
Abstract: "systems with the same sensing gain and average forecasting errors may
lead to distinct decisions".
Abstract: "Rather than minimizing proxy prediction loss, our method directly
optimizes final task performance metrics such as evacuation and relocation cost."

## Follow-up papers
- malings2016voisensor (the decision-dependent placement precursor)
- rossa2026actionbed
- shao2026beliefaware (the wildfire sensing analogue, but predictive-loss objective)
