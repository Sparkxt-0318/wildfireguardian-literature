# CURRENT_THESIS.md

**Last revised:** 2026-09-19
**Status:** Live. Revised only with a `docs/DECISIONS.md` entry.

---

## Thesis statement (one paragraph)

Wildfire protective-action decisions are currently made against *fire position*
(a trigger boundary crossed, a buffer breached). WildfireGuardian asks whether
decisions should instead be made against *mission feasibility under forecast
uncertainty* — and, critically, at what forecast quality that shift stops being
a theoretical improvement and starts beating a well-tuned positional trigger.
The sharpest instance of this is the assisted-evacuation round trip, where the
decision-relevant quantity is not "when must this person leave" but "when must
a responder *depart* so the whole mission still closes."

---

## RQ1 — Forecast-value boundary

> How accurate and timely must a wildfire forecast be before forecast-aware
> protective action outperforms a strong tuned trigger/buffer policy?

**Decision variable:** act now vs. wait, given a forecast of fire arrival.

**Comparator (non-negotiable):** a *tuned* trigger/buffer policy — the buffer
distance or trigger-boundary lead time optimized over the same scenario
distribution the forecast-aware policy sees. Beating an untuned buffer is not a
result and will be treated as a failed experiment.

**Output:** a boundary in forecast-quality space — (skill, lead time, latency)
— separating the region where forecast-aware action wins from where it does
not.

**Why this could be novel:** forecast *value* frameworks are mature outside
wildfire (hurricanes, floods, severe weather — see
`literature/reviews/04-forecast-value.md`). The open question is whether the
wildfire-specific instantiation, with a tuned positional-trigger comparator and
an explicit skill boundary, has already been done. **This is a prior-art
question, not a methods question.**

**Known risk to this RQ:** if the boundary is trivially "forecast-aware always
wins when skill > 0", the result is uninteresting. The interesting result is a
non-trivial boundary where latency and lead time trade against skill.

---

## RQ2 — Assisted-evacuation dispatch deadline

> For residents who cannot self-evacuate, what is the latest fire-relative
> dispatch time at which a responder can complete the full mission:
> responder base -> resident -> pickup -> safe destination?

**Decision variable:** dispatch time of a responder unit.

**Unit of analysis:** the **complete round trip**, decomposed as

```
t_ingress  (base -> resident, inbound, against outbound traffic and toward fire)
t_pickup   (loading / assistance dwell time)
t_egress   (resident -> safe destination, outbound)
```

subject to fire arrival constraints on *every leg*, not just the last.

**Output:** a latest-safe-dispatch time, fire-relative, and its sensitivity to
forecast error, ingress congestion, and pickup dwell.

**Why this could be novel:** the trigger literature computes *egress* deadlines
for self-evacuating households. The rescue/fleet-routing literature computes
*routes*. The open question is whether anyone computes the **inbound-inclusive
dispatch-by deadline as the decision quantity** under a *modeled future fire*.

**Known risk to this RQ:** pickup-and-delivery / vehicle-routing formulations
with time windows are extremely mature. If a prior work casts assisted wildfire
evacuation as a PDPTW with fire-derived time windows, the *formulation* is
occupied and only the deadline-as-output framing may survive. This must be
searched hard — see `novelty/NOVELTY_THREATS.md`.

---

## What would falsify the thesis

Stated in advance so we cannot move the goalposts later:

1. A paper computing a responder-inclusive (inbound + pickup + outbound)
   wildfire evacuation deadline under a modeled future fire. → RQ2 largely
   occupied.
2. A paper establishing a forecast-skill boundary for wildfire protective
   action against a tuned trigger comparator. → RQ1 largely occupied.
3. A demonstration that tuned fixed buffers are within noise of any
   forecast-aware policy across realistic forecast quality. → both RQs become
   negative results (still publishable, but not the claimed contribution).
4. Evidence that assisted-evacuation dispatch is in practice constrained by
   resource availability and communication, not by travel-time feasibility. →
   the deadline is the wrong decision variable.

---

## Current confidence

| Element | Confidence | Basis |
|---|---|---|
| RQ2 is the stronger question | Moderate | Reasoning from the trigger literature's egress-only framing; **must be tested against prior art** |
| RQ1 forecast-value framing is generic prior art | High | Forecast-value theory is mature; only the wildfire instantiation can be novel |
| Korean setting alone is sufficient novelty | **Low — treat as false** | See `docs/NOVELTY_STANDARD.md` §4 |

All three rows are provisional until `novelty/CURRENT_NOVELTY_VERDICT.md` is
populated from adversarial search.
