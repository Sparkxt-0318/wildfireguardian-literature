# Category 3 — Wildfire + Traffic

**Author:** Agent A/B (Search Researcher + Prior-Art Adversary)
**Date:** 2026-09-19
**Stance:** adversarial. The purpose of §4 of this review is to kill WG-C-003.
**Evidence caveat:** most items are **E2 (abstract retrieved)**. ScienceDirect, Springer
and Wiley returned HTTP 403 to this agent, so the two most dangerous papers
(`beyki2026modular`, `tang2025transit`) were assessed without full text. Both are flagged
`NEEDS_FULL_TEXT` and the verdict in §4 is explicitly provisional on them.

---

## 1. The four sub-literatures

Category 3 is not one field. It is four, and they barely cite each other.

**(a) Coupled fire–traffic simulation platforms.**
`wahlqvist2021wuinity` (WUI-NITY: FARSITE + pedestrian + LWR traffic + PERIL),
`siam2022interdisciplinary` (agent-based, multimodal, behaviourally grounded),
`ronchi2023verification` (the 24-test verification protocol these platforms are judged by),
`beyki2026modular` (modular agent-based, Portugal). Output: clearance times, exposure
counts, what-if scenarios.

**(b) Trigger-setting via traffic.**
`li2018coupling` is the whole sub-literature: run the traffic model many times, get a
clearance-time CDF, emit percentile-indexed trigger buffers. This is the bridge between
Categories 1 and 3 and it is the strongest single piece of prior art against WG-C-006.

**(c) Degraded / damaged networks.**
`ma2025damaged` (fire-induced closures during the run, entrapment risk),
`beyki2026modular` (fire-driven road-segment closures updating availability dynamically),
`kim2024directional` (which fire approach directions leave a community with no usable
exit), `dennison2007wuivac` (the 2007 ancestor: buffers predicting closure of **all**
evacuation routes).

**(d) Network control and capacity.**
`lu2026lahaina` (conservation laws on a graph, game-theoretic junctions, contraflow, and a
lane reserved for emergency vehicles), `janfeshanaraghi2025silverado` (empirical traffic
performance indicators from the 2020 Silverado fire), `chang2026marin` (differential access
to safe egress across a population), `gwynne2023roxborough` (the community drill dataset
everyone benchmarks against).

---

## 2. What Category 3 has settled

1. **Coupled fire + pedestrian + traffic simulation is standard practice**, has a named
   reference platform (WUI-NITY), and has a **published verification protocol**. Building
   another coupled simulator is not a contribution.
2. **The network degrades under the fire you predicted.** Fire-induced link closure,
   dynamic rerouting, and entrapment-as-an-outcome are all implemented
   (`ma2025damaged`, `beyki2026modular`).
3. **Exit capacity, not behaviour, is often the binding constraint**, and the return to
   adding capacity has a computable threshold (`lu2026lahaina`).
4. **Multimodal evacuation (pedestrian, private vehicle, transit) is modelled**
   (`siam2022interdisciplinary`, `beyki2026modular`, `tang2025transit`).
5. **Real evacuation data exists to calibrate against**: the Roxborough Park drills
   (`gwynne2023roxborough`), Silverado 2020 (`janfeshanaraghi2025silverado`), and the
   Portuguese drill used by `beyki2026modular`. "We had no data" is no longer an excuse,
   and a simulation-only result will be judged against these.
6. **Equity of egress access is an established analysis** (`chang2026marin`).

---

## 3. What Category 3 has NOT done

1. No paper found reports a **dispatch-by deadline** as its output quantity.
2. No paper found derives **responder time windows from a fire-spread model's arrival
   times** and inverts them to solve for a departure instant.
3. No paper found sweeps **forecast skill / lead time / latency** as the independent
   variable of a traffic-coupled evacuation decision.
4. No paper found in a **Korean** road/terrain setting for evacuation timing. (One Korean
   wildfire paper surfaced — Park, Yun & Baek, *Fire* 9(4):150, 2026, on Natech fuel-
   infrastructure exposure at the Korean WUI — but it is exposure mapping, not evacuation.)

---

## 4. **Inbound responder vs outbound evacuee** — state of the art

This is the section WG-C-003 lives or dies in. Four bodies of work touch it. They are
ordered by how close they get.

### 4.1 The closest thing to simultaneity: `beyki2026modular` (2026, *Safety Science*) — **CRITICAL**
Beyki, Patricio, Lopes, Santiago & Laím name the gap in their own abstract and then close
part of it. Their stated gaps in prior work include **"the lack of inbound traffic and
rescue operations,"** and their framework **"supports dynamic routing responsive to
advancing fires, enables both outbound self-evacuation and inbound rescue operations."**
Agent classes explicitly include **emergency extraction**. Fire-driven road-segment
closures update network availability during the run, and the model was validated against a
real evacuation drill in Portugal.

**What this occupies:** the *simultaneity itself*. As of 2026 it is published that inbound
rescue vehicles and outbound evacuees can be simulated together on a fire-degraded network.
WildfireGuardian **cannot claim to be first to model inbound responder movement against
outbound evacuation flow.** That sentence is now false and must be struck.

**What it does not occupy (pending full text):** the abstract reports *evacuation times
validated against a drill*. It reports no deadline, no latest-dispatch quantity, and no
inversion of fire-arrival constraints into a departure time. `NEEDS_FULL_TEXT` — this is
the single most important full text to obtain.

### 4.2 The closest thing to the formulation: `moradi2026supported` (2026, arXiv preprint) — **CRITICAL**
Moradi, Sauré & Patrick cast supported evacuation of people who cannot self-evacuate as a
two-stage stochastic **facility location + multi-vehicle PDPTW**. Vehicles start at medical
facilities *outside* the fire zone, travel **into** the zone to assembly areas, perform
split pickups with vehicle-specific dwell times, and deliver to shelters/hospitals. Their
second model gives **every arc two time windows**: a soft one after which the route is
partially disrupted and travel time rises, and a **hard one after which the route is
reached by the fire and becomes unavailable**.

So the inbound leg **is** fire-constrained, in print, for exactly our population, on the
same Roxborough Park data the trigger lineage uses.

**Two things save WG-C-003 from being dead here, and only two:**
- **Where the windows come from.** In their experiments the time windows are drawn from
  `Uniform(400, 850)` minutes, and "fire origin" is a three-valued categorical scenario
  label (south / north / west). The windows are a *stochastic abstraction of* a fire, not
  the arrival-time field of a modelled fire. WG-C-003's `future_fire` is `yes`; theirs is
  at best `partial`.
- **What is reported.** The outputs are shelter-activation decisions, fleet size, routes and
  evacuation counts within windows, benchmarked against Closest-First,
  Shortest-Time-Window-First and Most-Crowded-First heuristics. **No latest-dispatch time is
  reported as a quantity.** The clock appears as a constraint, never as the answer.

This is a thin margin. If the referee version of this paper (it is "submitted to Elsevier")
adds fire-model-derived windows or reports a latest-departure analysis, WG-C-003 is gone.

### 4.3 The network-capacity treatment: `lu2026lahaina` (2026, arXiv preprint) — **HIGH**
Lu, Tan, Xue, Koniges & Bertozzi show, on the real Lahaina network, that **"a fourth lane
can be reserved for emergency vehicles with negligible impact on civilian clearance time."**
This prices responder ingress against outbound throughput at the network level and answers,
in the negative, the obvious objection "doesn't letting responders in cost evacuees time?"
It computes no mission and no deadline.

### 4.4 The transit-pickup branch: `tang2025transit` (2025, *TR-C*) — **HIGH, UNRESOLVED**
Transit evacuation of carless/transit-dependent populations is structurally the same trip:
depot → into the threatened area → pickup → out, with a scarce fleet allocated by
reinforcement learning. **Its abstract could not be retrieved** (OpenAlex budget exhausted,
publisher 403). This is the paper most likely to move WG-C-003 unnoticed, because it is not
indexed as wildfire work. `NEEDS_FULL_TEXT`.

### 4.5 The older OR lineage (context, and it is long)
`shahparvari2017robust` (2017) already did last-mile, short-notice bushfire evacuation of
late/vulnerable evacuees by capacitated vehicles under **hard time windows** with route
disruption, on Black Saturday data. `flores2020supported` (2020) named and formalised
"supported evacuation." `flores2023goal` (2023) built the dynamic pick-up-point /
safe-area network with health-priority classes on the 2019 Saddleridge fire.
**Assisted wildfire evacuation as a routing problem with deadline-like windows has been
solved repeatedly since 2017.** WG-C-005 is a framing, not a contribution.

### 4.6 The cross-hazard precedent
`averill2007emergencyresponse` (NIST IR 7425, 2007 — a **government report**, not
peer-reviewed) modelled first responders ascending a stairwell against descending occupants
in building evacuation. Responder counterflow as a modelled penalty is nearly twenty years
old in the building-fire domain. Any claim of conceptual novelty for "responders move
against the flow" is indefensible.

---

### 4.7 Verdict: does Category 3 kill WG-C-003?

**Partially occupied. Not dead. The surviving claim is much narrower than written.**

Decomposing WG-C-003 into its five components:

| Component | Status | Occupant |
|---|---|---|
| Residents who cannot self-evacuate are modelled | **OCCUPIED** | `flores2020supported`, `shahparvari2017robust`, `moradi2026supported` |
| Inbound responder movement simulated with outbound evacuation | **OCCUPIED (2026)** | `beyki2026modular`; capacity form in `lu2026lahaina`; cross-hazard in `averill2007emergencyresponse` |
| Pickup dwell + delivery in one routed mission | **OCCUPIED** | `moradi2026supported` (split pickup, vehicle-specific load/unload times), `flores2023goal` |
| Fire-arrival feasibility enforced on the **inbound** leg | **OCCUPIED in form, OPEN in source** | `moradi2026supported` has a hard arc window "after which the route is reached by the fire" — but drawn from `Uniform(400,850)`, not from a spread model |
| **Latest fire-relative dispatch time reported as the output quantity** | **OPEN** | nothing found |

**Therefore:**
- The sentence "we are first to model inbound responder movement against outbound
  evacuation" is **FALSE as of 2026** and must be deleted.
- The sentence "we formulate assisted wildfire evacuation with fire-derived time windows"
  is **OCCUPIED in formulation** by `moradi2026supported`.
- The sentence that survives is only:
  > *We compute the latest fire-relative **dispatch time** at which a responder round trip
  > (base → resident → pickup → safe destination) remains feasible, with fire-arrival
  > constraints on every leg derived from a **modelled future fire** rather than from
  > assumed time windows, and we report that time — not a route — as the decision quantity.*
- That surviving claim is **N2 (quantity) narrowed by the conditioning clause**. It is
  defensible only if we can say precisely how a spread-model-derived arrival field differs
  in its *conclusions* from a `Uniform(400,850)` window — i.e. NOVELTY_STANDARD §3.1
  applies: the combination must change the answer, and we must show it.

**Recommended status:** WG-C-003 → **WEAKENED**, with the narrowed text above, contingent on
the full texts of `beyki2026modular` and `tang2025transit`. It should NOT be set to
SUPPORTED_CANDIDATE, and it should NOT be left at UNKNOWN.

---

## 5. What Category 3 means for the other claims

- **WG-C-001** — REJECTED, reinforced by `wahlqvist2021wuinity`, `ma2025damaged`,
  `beyki2026modular`.
- **WG-C-005** — treat as **OCCUPIED**: `flores2020supported` (2020) onward. Use it as
  framing and cite it; do not claim it.
- **WG-C-006** — **WEAKENED**: `li2018coupling` already supplies a simulation-derived,
  percentile-indexed (i.e. tuned) trigger comparator, and `ronchi2023verification` already
  supplies the verification standard. Our contribution is compliance, not invention.
- **WG-C-011** — expect **OCCUPIED**: fleet sizing and scarce-vehicle allocation are
  first-stage decisions in `moradi2026supported` and the control problem in
  `tang2025transit`.
- **WG-C-014** — **still open in Category 3**; nothing here relates a spatial prediction
  score (IoU/Jaccard) to decision quality. The nearest pressure is Category 1's
  `kalogeropoulos2026ensemble`, which shows different spread models yield different
  boundaries.
