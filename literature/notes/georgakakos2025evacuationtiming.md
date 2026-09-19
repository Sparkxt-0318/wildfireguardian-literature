# georgakakos2025evacuationtiming

## Citation
Georgakakos, K. P., 2025: Determinants of evacuation timing in response to
probabilistic forecasts. *Natural Hazards*, **121**(16), 18849-18878.
DOI 10.1007/s11069-025-07540-5

## Publication status
Peer-reviewed journal (Springer). Bibliographic record verified via Crossref API
(Crossref carries no abstract for this record). Abstract obtained from the RePEc/
IDEAS record and search summary; publisher full text paywalled. Evidence level
**E2**. Flagged `NEEDS_FULL_TEXT`.

## Problem
When should an agency issue an evacuation statement for a local or regional
life-threatening hazard whose probability of occurrence is forecast in real time?

## Method
Adaptive stochastic decision methodology embedded in Monte Carlo simulation
experiments that explicitly carry parametric uncertainty. At each decision time
the target is binary: issue now, or delay to a later time.

## Data
Simulated (Monte Carlo) scenarios with parametric uncertainty; hazard-generic.
This is effectively an **OSSE-style** design.

## Outputs
Determinants of the issue-time, given:
(a) the forecast sequence of event probability as a function of lead time plus a
measure of forecast uncertainty;
(b) a probabilistic model of the evolving public response as a function of lead time;
(c) the uncertain probability threshold below which the public will not respond;
(d) the estimate of the **time interval of evacuation completion**.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Forecast probability evolves stochastically with lead time; public response is a
probabilistic function of lead time; evacuation completion time is an estimated
interval.

## Validation
Simulation-only. No real event reconstruction reported in the retrieved abstract.

## Limitations
The completion time is an exogenous scalar/interval, not derived from a network,
a vehicle, or a hazard-arrival constraint per leg. No spatial hazard field.

## WildfireGuardian overlap
This is the closest published relative of **RQ1 as a decision structure**: act
now vs. wait, under a forecast whose quality is indexed by lead time, with a
completion-time feasibility term. It also anticipates WG-C-010 (an OSSE for
evacuation-decision quality) in a hazard-generic form.

## WildfireGuardian difference
- Completion time here is an *input estimate*; in WildfireGuardian the
  completion time is the *computed quantity*, derived from ingress + pickup +
  egress against a modelled fire-arrival field.
- No comparator policy at all: the paper characterises determinants, it does not
  benchmark a forecast-aware policy against a tuned positional trigger.
- Hazard-generic, not wildfire; no fuel, terrain or road geometry.

## Novelty threat
**HIGH** to WG-C-002 and WG-C-012; **MODERATE** to WG-C-010. The "evacuation
timing under a probabilistic forecast with a completion-time constraint" framing
is occupied as of 2025.

## Quotes / page references
No verbatim quotes from the publisher text (paywalled). The four determinants
(a)-(d) above are paraphrased from the RePEc abstract record (E2).

## Follow-up papers
- Georgakakos, K., "Incorporating Forecast and Public Response Uncertainty in
  Agency Timing Decisions for Evacuation Statements", EGUsphere Plinius
  conference abstract, DOI 10.5194/egusphere-plinius19-85 (2026, posted content,
  NOT peer-reviewed journal) — same programme, later.
- regnier2008public
