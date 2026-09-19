# JUDGE_QUESTIONS.md

Hard questions and evidence-based answers. Every answer concedes the occupied
ground **first** — conceding early removes most of the attack surface and buys
credibility for the one thing we do claim.

Format: a 30-second spoken answer, then the evidence, then the follow-up the
judge will actually ask next.

**Drill rule:** if you cannot give the 30-second answer without reading it, you
do not know it yet.

---

## Q1. "Isn't this just Cova trigger modelling?"

**30s.** No, but it's built on it, and Cova owns more of this than people
think. Cova (2005) computes a *boundary on the ground*: cross this line and the
community should leave. That lineage — WUIVAC, PERIL, k-PERIL — has been
refined for twenty-one years and now includes ensemble-based probabilistic
boundaries. All of it answers "when must the people in the house leave?" We ask
a different question: "when must a vehicle leave the station, to get to someone
who cannot leave on their own, and get back out?" That's a departure time for a
responder, not a distance for a resident.

**Evidence.** `cova2005trigger` (Transactions in GIS 9(4):603–617);
`kalogeropoulos2026ensemble`; `NOVELTY_MATRIX.md` column `dispatch-by deadline`
is the only one with zero occupants.

**Follow-up: "Isn't the deadline just the boundary read backwards?"**
For a self-evacuating household, largely yes. For a round trip it isn't, because
the inbound leg is constrained by a fire that is moving toward the vehicle while
the outbound leg is constrained by one that has moved further. Those two
constraints bind at different times, and a single boundary does not encode both.

---

## Q2. "Isn't assisted evacuation already solved?"

**30s.** The modelling of it, largely yes — and we say so. Moradi et al. (2026)
solve supported evacuation in wildfires with hard fire-arrival time windows on
every arc; Shahparvari's bushfire work goes back to 2015; Beyki et al. (2026)
simulate inbound rescue on a fire-degraded network. We do not claim to have
invented assisted-evacuation modelling. What none of them report is the
*deadline* — they all report a plan: routes, fleet sizes, shelter locations.
The time windows are inputs to their models; the departure time is our output.

**Evidence.** `moradi2026supported` (arXiv 2608.05413, **preprint**);
`shahparvari2019fleet`; `beyki2026modular`; `flores2023goal`.
`ABANDONED_CLAIMS.md` lists WG-C-005 and WG-C-011 as OCCUPIED.

**Follow-up: "So what does the deadline give a commander that a plan doesn't?"**
This is the question that decides whether the project has a contribution, and
we have to answer it with a demonstrated case, not an argument. If we cannot
show a situation where the deadline and the plan imply different actions, the
claim should be narrowed to the sensitivity result. That is written down in
`SURVIVING_CLAIMS.md` as the condition on S1.

---

## Q3. "Why not just use a fixed buffer?"

**30s.** That's the right challenge, and it's our baseline rather than our
strawman. Li, Cova & Dennison derive buffers indexed by clearance percentile
from traffic simulation — 160 minutes at the 95th percentile in their case. We
tune that buffer on the same scenarios our forecast-aware policy sees, and then
ask what the forecast adds. If a tuned buffer wins, that's our result and we
report it.

**Evidence.** `li2018coupling`; `FAILURE_MODES.md` §1 names weak baselines as
the program's highest-probability failure; `CURRENT_THESIS.md` falsifier #3.

**Follow-up: "And has the tuned buffer won?"**
Answer honestly with whatever the current experiment says. If not yet run, say
so. Never answer this with a projection.

---

## Q4. "Why use simulations?"

**30s.** Because the counterfactual doesn't exist in data: nobody records what
would have happened if a crew had left thirty minutes later. And because the
validation data for WUI evacuation models don't exist either — Ronchi et al.
(2023) say so explicitly, which is why they build a *verification* standard
instead. So we verify against that standard, and we state our results as
conditional on the simulation.

**Evidence.** `ronchi2023verification` (Natural Hazards 117(2):1493–1519);
`FAILURE_MODES.md` §8.

**Follow-up: "Then why should I believe the numbers?"**
You shouldn't believe the magnitudes. We claim orderings and boundaries, not
magnitudes, because the OSSE has no calibration anchor. That limitation is
written in `OPEN_QUESTIONS.md` M1.

---

## Q5. "How do you know your fire model is right?"

**30s.** It isn't, and we can quantify how wrong. Cruz & Alexander found only
3% of rate-of-spread predictions were accurate across 1,278 observations, with
mean percent errors of 20–310%, and proposed ±35% as *reasonable* performance.
Three operational fire-growth models agree with observed extent at IoU ≈
0.17–0.20 at default parameterisation. So we treat the fire model as a source
of error to propagate, not a source of truth.

**Evidence.** `cruz2013uncertainty` (Environmental Modelling & Software
47:16–28); `bennett2026wise` (IJWF 35(8), F1 0.259 / IoU 0.194 over 19,848
fire-days); ELMFIRE documentation (**software documentation**, Jaccard 0.178;
FARSITE 0.176 on the same pipeline).

**Follow-up: "If the fire model is that bad, is the deadline meaningful?"**
That is exactly why the deadline is reported as a function of forecast error
rather than as a single number. A point estimate from a model with IoU 0.19
would be indefensible; a boundary in error-space is not.

---

## Q6. "Are you predicting lives saved?"

**30s.** No. We predict whether a mission is feasible under stated assumptions.
We do not model injury, mortality, or whether a resident would comply. Claiming
lives saved would require causal evidence we don't have and can't get from a
simulation.

**Evidence.** `PROJECT_CONTEXT.md` ("What WildfireGuardian is NOT");
`FAILURE_MODES.md` §7 on vulnerability overreach.

---

## Q7. "Why does Korea need this if MOIS already has AI evacuation routing?"

**30s.** This is the sharpest question and we raise it ourselves. Korea is
ahead of where most people assume. Since April 2025 MOIS and KFS have run a
three-stage system keyed to modelled fire-line arrival — order at 5 hours,
prepare at 8 hours — and it *already* directs older residents to evacuate in
advance. In September 2026 KFS announced an AI system that outputs resident
evacuation routes *and* ingress routes for suppression crews. So we do not claim
Korea lacks this. What neither produces is a dispatch-by time for a vehicle
collecting a specific resident, and the 5-hour threshold has no published
derivation, so we cannot tell whether it is tuned or administrative.

**Evidence.** `mois2025evacuationstages`, `mois2026aievacroute` (both
**government documents, not peer-reviewed**; the primary MOIS release for the
2026 programme was not retrieved — say so if pressed); `kwon2025koreaevac`
(peer-reviewed Korean wildfire evacuation optimization). `OPEN_QUESTIONS.md` B4.

**Follow-up: "So is any of this novel in Korea?"**
No — and we don't claim it is. Korean novelty fails our own standard
(`NOVELTY_STANDARD.md` §4). Korea is where we work, not why the work matters.

---

## Q8. "Isn't your uncertainty model self-generated?"

**30s.** It would be if we used one model for both truth and forecast — that's
inverse crime, and it inflates results. We use a non-identical-twin design.
Yu et al. (2019) measured the difference: identical-twin OSSEs reported 45%
error reduction where non-identical reported 29%. Their sharpest finding is
that error-growth rates looked fine in *both* designs while the impacts were
biased — so the obvious sanity check doesn't certify the design.

**Evidence.** `yu2019twin` (Ocean Science 15(6):1801–1814);
`kaipio2007inversecrime`; `halliwell2014fraternal`; `FAILURE_MODES.md` §2.

**Follow-up: "Where does your injected error come from, then?"**
It must have the *structure* of real model error — biased, spatially
correlated, regime-dependent — derived from truth-forecast discrepancy, not
white noise. And we should publish the identical-vs-non-identical gap so the
optimism is measured rather than asserted.

---

## Q9. "How do you avoid hindsight?"

**30s.** Every quantity the policy consumes carries an availability timestamp,
and it may only be used if it was available at the decision time. That rules out
the final perimeter, the observed wind shift, and the known duration of the
event. It also means our forecast carries real observation latency — over Korea
the fastest fire detection tier doesn't exist, because sub-minute direct-readout
satellite coverage is US and Canada only.

**Evidence.** `FAILURE_MODES.md` §4; `sung2025geostationary` (GK2A 2 km,
2-minute cadence over the peninsula, mean detection delay 12.9 minutes, recall
0.329); `nasafirms2026latency`.

---

## Q10. "Why doesn't a good IoU mean a good evacuation decision?"

**30s.** Because where the error is matters more than how much there is. A
forecast can be spatially excellent overall and still be wrong on the one road
segment the vehicle needs. We should be careful here though: the general point
that accuracy isn't value is not ours — Murphy and Ehrendorfer established it
in 1987. What we'd be adding is the geometric version: error *located on the
ingress or egress route* is what breaks the decision, and aggregate overlap
metrics can't see that.

**Evidence.** `murphy1987accuracyvalue` (Weather and Forecasting 2(3):243–251);
`chen1987qualityvalue`; `raeth2025decisionskill` (**preprint**);
`dayan2026conformal` (AUROC 0.969 yet standard thresholds captured only 7–72%
of actual spread).

**Follow-up: "Have you shown the non-monotonicity, or assumed it?"**
If we have only assumed it, say so. `CLAIM_REGISTRY.md` marks WG-C-014
WEAKENED, and notes the two 1987 papers are still at evidence level E1/E2 — we
have not yet read the papers that own this proposition.

---

## Questions we are not ready for

Prepared honesty is better than improvised confidence:

- **"Is travel time actually what constrains dispatch, or is it tasking and
  communication?"** We don't know. The vulnerable-populations literature points
  toward communication. `OPEN_QUESTIONS.md` A4. The honest answer declares the
  regime as an assumption.
- **"How many independent fire events is your result based on?"** Say the
  number. If it's under ten, the boundary may not be separable from noise, and
  the event-level Monte Carlo standard error must be reported before the
  boundary is shown.
- **"Did you search the Korean databases?"** Not completely. KCI's search
  wasn't drivable and DBpia returned errors. That's the largest blind spot and
  it's in our own setting.
- **"What's your citation for narrow Korean mountain roads?"** We don't have
  one. Do not assert it.
