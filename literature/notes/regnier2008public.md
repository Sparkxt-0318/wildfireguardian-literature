# regnier2008public

## Citation
Regnier, E., 2008: Public Evacuation Decisions and Hurricane Track Uncertainty.
*Management Science*, **54**(1), 16-28. DOI 10.1287/mnsc.1070.0764

## Publication status
Peer-reviewed journal (INFORMS). Bibliographic record verified via Crossref API.
Abstract obtained via publisher listing and search summaries; full text not read.
Evidence level **E2**.

## Problem
Officials who can order evacuations must trade risk to life against costly false
alarms, using imperfect track forecasts, and must decide *when* to order.

## Method
Markov model of storm motion fitted to historic Atlantic tracks, used to quantify
the time profile of track uncertainty for specific target locations (New Orleans,
Miami, Norfolk, Montauk). Combined with a required-lead-time constraint for
completing evacuation and a tolerance on the probability of failing to evacuate
before a strike.

## Data
Historical Atlantic hurricane tracks; four target locations.

## Outputs
Per-location statements of the form: an official requiring no more than a 10%
probability of failing to evacuate before a striking hurricane must accept that
at least ~76% (and at some locations >90%) of evacuations will be false alarms.
Also: whether to act now or wait for an updated forecast differs by location at
the same instantaneous strike probability.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Fixed clearance time per location; strike probability from a Markov track model;
a single ordering decision; risk tolerance expressed as a miss-probability cap.

## Validation
Retrospective/statistical against historical tracks. Not an operational trial.

## Limitations
Aggregate clearance time is exogenous. No road network, no vehicle, no responder.
Hazard is a track, not a spreading area.

## WildfireGuardian overlap
This paper *already reports a forecast-quality boundary for evacuation ordering*:
given a required miss probability and the uncertainty-vs-lead-time curve, it
derives the unavoidable false-alarm rate. That is structurally the object WG-C-002
proposes to produce, in a different hazard.

## WildfireGuardian difference
(a) Hazard: hurricane track uncertainty vs. spreading fire-arrival-time field.
(b) Comparator: Regnier compares against *no* alternative policy; she characterises
the achievable operating points. WildfireGuardian proposes to compare a
forecast-aware policy against a *tuned positional trigger/buffer* — a comparator
Regnier does not have because hurricanes have no trigger-boundary literature.
(c) Decision subject: aggregate public evacuation vs. a single responder dispatch
with an inbound leg and a pickup dwell.

## Novelty threat
**HIGH** to WG-C-002 as a general claim. Reduces WG-C-002 from N2 towards N4
unless the tuned-trigger comparator and the mission-feasibility objective are
made load-bearing.

## Quotes / page references
No verbatim quotes (full text not retrieved). The "10% miss -> >=76% false alarms"
figure is from the publisher abstract as relayed by search; treat as E2.

## Follow-up papers
- regnier2006dynamic (the dynamic-programming precursor)
- georgakakos2025evacuationtiming
- lopez2020bridging
