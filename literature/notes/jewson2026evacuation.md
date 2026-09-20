# jewson2026evacuation

## Citation
Jewson, S., 2026: An extreme weather evacuation cost-lost model and the
implications for early warning weather forecasting systems. *Frontiers in
Communication*, **11**, 1762033. DOI 10.3389/fcomm.2026.1762033. Published
2026-04-10, CC BY 4.0.

> The spelling "cost-**lost**" is the published title, in both Crossref and on
> the publisher page. Do not silently normalise it.

## Publication status
Peer-reviewed journal article, open access. Bibliographic record verified
independently via the Crossref REST API and the Frontiers article page; the
abstract text is identical from both. Abstract-level statements are **E4**;
body statements are **E3** (single rendering of the publisher full text).

## Problem
The classic cost-loss model answers "evacuate or stay". Jewson argues the
operationally sharper question is different:

> "A more subtle but perhaps more relevant question that also arises in many
> evacuation situations is whether to evacuate now or wait for the next
> forecast." (Abstract)

And then asks what forecast information a decision maker would need in order to
answer it.

## Method
A new idealized cost-loss model with **two sequential forecasts** rather than
one — in the worked example, forecasts issued on successive days before a
tropical cyclone landfall. The decision at the first forecast is act-now vs.
wait-for-the-update. The model is solved analytically and then illustrated by a
parameter sweep.

## Data
None. Explicitly idealized:

> "Idealized models of this type are not intended to be used as actual decision
> making algorithms in real situations. However, they can help us understand the
> logic of the decision-making process." (Abstract)

## Outputs
Two results, one negative and one positive, and the negative one is the more
interesting:

1. **Negative.** "uncertainty around the probability of extreme weather does not
   make any difference to decisions" (Abstract). Second-order uncertainty about
   *today's* probability is decision-irrelevant.
2. **Positive.** "information about how the probability might change between
   forecasts does make a difference" (Abstract). The decision-relevant quantity
   is the **distribution of the change in forecast probability between updates**.
3. **The frontier.** Sweeping the standard deviation of that change produces a
   switch: "For low standard deviations the model recommends evacuation, while
   for high standard deviations the model recommends waiting." (worked example,
   E3). Worked-example parameters recorded at E3, **not citable as numbers**:
   C = 5, L2 = 45, L1 = 100, giving p_crit = 0.09, with p2 and the standard
   deviation of p1 varied.
4. **Recommendation to forecasters.** "Forecasters may wish to consider
   providing information about forecast changes in some experimental way, either
   as standard deviations of possible changes in probability, or in some other
   format." (E3)

## Key equations
Cost-loss with a two-stage structure; threshold form reported as the standard
`C < pL` condition with the probabilities weighted by the forecast-change
dynamics. Exact equations NEEDS_FULL_TEXT at E4.

## Assumptions
Two forecast issuances at known times; loss differs between evacuating early
(L2) and being caught (L1); the change in forecast probability between issuances
is a random variable with a specified standard deviation.

## Validation
None — idealized model, no case study, no observations.

## WildfireGuardian overlap
This is the **most exposed single paper for RQ1's experimental design**, more so
than `ardid2026forecastvalue`, and it was not in the corpus before 2026-09-20.

- **WG-FV-1 (controlled forecast-error dimensions).** Jewson varies a *named*
  forecast-uncertainty dimension deliberately and reports how the decision
  changes. That is exactly the experimental move WildfireGuardian proposes, in a
  different hazard, in a one-dimensional and analytically tractable form. The
  move "sweep a forecast-quality axis, find where the recommendation flips" is
  therefore published.
- **WG-FV-4/WG-FV-5.** The flip point is a **break-even defined by decision
  loss**, not by a forecast score. One-dimensional, but real.
- **WG-C-012 (latency).** Uncomfortable. The whole paper is about the value of
  *waiting for information that has not arrived yet*, which is the economic
  substance of "a forecast that arrives later is worth less". It is framed as
  forecast update timing, not observation-to-product latency, but a hostile
  reader will ask why that distinction matters and the project must be able to
  answer operationally.
- **WG-C-014.** Reinforces Murphy/Ehrendorfer: a forecast attribute that
  improves the forecast's own description of its uncertainty (second-order
  uncertainty on p) is shown to be **decision-irrelevant**, while a different
  attribute is decision-relevant. Accuracy-value decoupling, demonstrated
  constructively, in 2026.

## WildfireGuardian difference
Stated operationally, per NOVELTY_STANDARD §6:

1. **The axis swept is different.** Jewson sweeps the standard deviation of the
   *change in a scalar probability between two forecast issuances*. RQ1 proposes
   to sweep spatial/temporal error in a **fire arrival-time field** and
   **observation-to-product latency**, which are two axes, not one, and which
   interact with a *place* (where the error lands relative to the route).
2. **There is no comparator policy.** Jewson compares act-now against
   wait-for-update within one decision model. RQ1's non-negotiable comparator is
   a *tuned positional trigger/buffer* — a different family of policy, not a
   different timing of the same policy.
3. **The payoff is a scalar loss.** RQ2's payoff is a mission-feasibility
   indicator on a routed round trip with hazard-arrival constraints per leg.
4. **No landscape, no hazard field, no responder, no assisted evacuation, no
   Korea.** The terms "wildfire", "latency", "assisted" and "vulnerable" are all
   absent from the paper.

## Novelty threat
**HIGH** to WG-C-002 and WG-C-012; **MODERATE** to WG-C-014.

It does not occupy RQ1, because RQ1 is defined by the tuned-positional-trigger
comparator and by the two-axis (error x latency) boundary. It **does** occupy
the generic move "sweep a forecast-quality parameter until the recommended
action flips, using decision loss as the criterion" — which means that move can
never be presented as a WildfireGuardian contribution. The contribution has to
be what the sweep is over and what it is benchmarked against.

## Quotes / page references
All quotes above are attributed to Abstract (E4, two independent sources) or to
the worked example / results (E3, single rendering). No page numbers: the
article is paginated by article number 1762033 only.

## Follow-up papers
- `murphy1977costloss`, `richardson2000relative` — the machinery Jewson extends.
- `regnier2006dynamic` — the direct ancestor of "act now vs wait for a better
  forecast"; Jewson should be read as the 2026 idealized restatement.
- `georgakakos2025evacuationtiming` — the Monte Carlo cousin, with a public
  response model and an evacuation completion interval.
- Backward/forward citation chase of this paper is **NOT DONE** and is the
  highest-value next search for Category 4.
