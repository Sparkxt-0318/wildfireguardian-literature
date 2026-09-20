# Full-text extraction — `moradi2026supported`

**Agent:** C — Verification Auditor
**Date:** 2026-09-20
**Target:** Moradi, S., Sauré, A., & Patrick, J. "A Relaxation-Based Decomposition Approach for
Solving a Supported-Evacuation Problem in Wildfires." arXiv:2608.05413 [math.OC]. **PREPRINT.**
**Scope:** full-text read, not a search. No new papers added to the corpus.

---

## 0. Retrieval and evidence level

| Field | Value |
|---|---|
| `fulltext_status` | **`METHODS_VERIFIED`** — complete body, all 7 sections, all constraint blocks (1)–(61), Tables 1–7, reference list; equations and parameters located by number. Not `RESULTS_VERIFIED`: nothing was reproduced or independently corroborated |
| `evidence_level` | **E4** — the ceiling `docs/EVIDENCE_LEVELS.md` sets for `METHODS_VERIFIED` |
| `access_route` | alphaXiv MCP `get_paper_content(fullText=true)` on `arxiv.org/abs/2608.05413` (97,958 chars), cross-checked against alphaXiv `answer_pdf_queries` page-ranked extraction (pages 1, 6, 7, 9, 10, 16, 18, 19, 20, 23, 24, 25, 27) and against the arXiv abstract page via WebFetch |
| HTML renderings | **Not available.** `arxiv.org/html/2608.05413v1` → HTTP 404. `ar5iv.labs.arxiv.org/html/2608.05413` → 200 but redirects to the abstract page (no LaTeX source HTML published). |

### Cross-check caveat (read this before citing any number)

The instruction was to prefer HTML over PDF and cross-check numerics against a second *rendering*.
**No second rendering exists** — arXiv published no HTML for this submission. What was actually
done is two **independent extraction passes over the same PDF** by two different alphaXiv
endpoints (linearized full text vs. page-ranked extraction). The two passes agreed **character for
character** on every load-bearing item below:

- `Uniform(400, 850)` for both assembly-area and route time windows (Table 6)
- `6 ambulances, 16 buses, and 0 helicopters` (§6.5.2)
- Table 7 evacuation times `158 / 242 / 646`, `157 / 243 / 574`, `142 / 211 / 482`, `143 / 217 / 509`, `144 / 220 / 500`
- Table 2 small-instance time windows `{838, 846, 745} {678, 600, 798} {741, 827, 711}`
- The text of constraints (26), (27), (28), (50), (51), (52), (53) and their prose glosses
- Table 3 itinerary, first cell `Arrival Time [min] = 0`

Agreement across two extractors of one PDF is **not** corroboration by a second source
(`docs/EVIDENCE_LEVELS.md` §Rules 4). Numbers here are E4 for *what the PDF says*; they are not E5.

### Metadata as retrieved

- arXiv abstract page (WebFetch **and** ar5iv redirect, two retrievals): `[Submitted on 5 Aug 2026]`,
  submission history `[v1] Wed, 5 Aug 2026 21:11:26 UTC (7,635 KB)`. **Only v1 exists**
  (`arxiv.org/abs/2608.05413v2` → HTTP 404).
- Comments field: `33 pages, 8 figures`. Subject: `Optimization and Control (math.OC)`.
- DOI: `https://doi.org/10.48550/arXiv.2608.05413`, labelled on the page
  "arXiv-issued DOI via DataCite". This is the arXiv deposit DOI, **not** a journal DOI.
  No journal-reference field is populated.
- Affiliation (PDF p.1): Telfer School of Management, University of Ottawa.
- Funding (§Acknowledgments): NSERC RGPIN-2018-05225, RGPIN-2020-04301; NRC 18122020.

---

## 1. Priority date — resolved

Both readings the task asked about are correct; they disagree by almost exactly one year.

| Source | Exact text |
|---|---|
| arXiv abstract page, submission history | "[v1] Wed, 5 Aug 2026 21:11:26 UTC (7,635 KB)" |
| PDF title page, footer of p.1 | "Preprint submitted to Elsevier August 8, 2025" |

**Resolution.** The footer is the manuscript's own compile-time stamp and is corroborated by
internal evidence: §6.5.1 uses "Google Maps estimates from **January 2025**". So the manuscript
was prepared and submitted to an Elsevier journal around **August 2025**, and posted to arXiv
**one year later, 2026-08-05**.

**What we may assert:** the earliest *demonstrable public* priority date is **2026-08-05**.
Anything earlier is the authors' own unverifiable claim on their own title page. We may not treat
August 2025 as established priority, and we may not treat 2026-08-05 as proof the work is new —
it is a year-old manuscript. Neither date changes its force as prior art.

**No evidence of acceptance or publication was retrieved.** No journal-reference on arXiv; the
Elsevier target journal is not named anywhere in the document.

---

## 2. Q-M1 — What carries a time window? (the crux)

Answered separately for each of the five, as instructed.

### (a) Residents — **NO** (not individually); **YES** at their gathering point

Residents themselves carry **no** time window. What carries a window is the *assembly area* node
they wait at. From §3:

> "Depending on the origin of the fire, wind direction, and vegetation density, each assembly area
> [l] is subject to a time window of [TW^s_l] after which it cannot be visited." (§3, Problem Definition)

Table 1 parameter gloss: "Time window for the evacuation at assembly area [l]."

Residents are a *count* at that node, not entities with attributes: Table 1, "Number of patients at
assembly area [l] from level [n] under scenario [s]". They have a priority level (1 high / 2 low)
and nothing temporal.

Also material: the assembly area is **not a residence**. §1:

> "certain locations within the fire zone serve as temporary assembly areas housing or gathering
> patients who are unable to evacuate by themselves" (§1)

So the residents have already reached a gathering point by unmodelled means. The door-to-door
leg does not exist in this model, and the authors flag its dynamics as an open problem (§7:
"it is possible that people arrive at the assembly areas at different times. This dynamic arrival
... is an unexplored topic").

### (b) Facilities (hospitals / shelters) — **NO**

Hospitals and shelters carry **capacity** constraints only, per priority level and per scenario
(Table 1: "Capacity of hospital or shelter [m] for accepting patients from severity level [n]";
constraints (5)–(6)). They carry **no** time window and are never closed by fire — they are
defined as being outside the fire zone (§3: "Outside the fire zone, there are |M| medical
facilities"). A vehicle may deliver to a hospital at any time. Constraint (52) applies the node
window only over the assembly-area index, not over medical facilities.

### (c) Arcs / routes — **YES, in Model 2 only, and there are two of them**

This is the paper's sharpest feature and the reason it is a CRITICAL threat. §5.4:

> "We assume each route has two time windows. The first is a soft time window, [STR^s_{ll'}], after
> which the route between l to l' becomes partially disrupted under scenario s, increasing the route
> travel time by y%." (§5.4)

> "The second is a hard time window, [TWR^s_{ll'}], after which the route connecting l to l' is
> reached by the fire and becomes completely unavailable." (§5.4)

Model 1 has **no** arc windows — only fixed per-scenario travel times. The arc window is the
Model-2 extension, and it is the one the case study is solved with (§6.5.2: "Solving Model 2,
which is the more realistic formulation").

### (d) Vehicles — **NO**

Vehicles carry capacity, speed, activation cost, travelling unit cost, an initial location
(binary parameter `IL^s_{vm}`, constraints (7)–(8)), a per-location loading time and a per-facility
unloading time, and a maximum number of stops `MAX_k` (20 in the experiments). **No shift length,
no availability window, no release time, no return-by time.** §7 is explicit that the trip need not
close back at base:

> "they do not have to return to their original dispatch location after each trip" (§7)

### (e) Complete missions — **NO**

There is **no** mission-level, trip-level, or horizon-level time window anywhere in the
formulation. Nothing constrains when a round trip must finish. The only global temporal pressure is
a soft one: an objective penalty term. Table 1: "[ξ] A penalty term to minimize the arrival times,"
entering objective (1) as `+ ξ Σ_v Σ_k Σ_l AT^{vk}_{ls}`, and described in §4 as "penalties for
delaying the evacuation beyond the acceptable time limits."

**Summary for Q-M1.** Windows attach to **nodes (assembly areas only) and to arcs (Model 2 only)**.
They do not attach to residents, facilities, vehicles, or missions.

---

## 3. Q-M2 — `base/staging -> resident -> pickup/service -> shelter/destination`? **YES**

Every link of the chain is present and explicitly timed.

| Leg | Where in the model |
|---|---|
| **base / staging** | §3: "Each evacuation vehicle [v] is initially stationed at a specific medical facility [m] under scenario [s]". Constraints (7)–(8) pin stop k=0 to that facility. Table 3 confirms operationally: bus 5's stop 1 is `H5`, a hospital. |
| **→ resident** | Travel to an assembly area node; arrival-time recursion (29)/(30), Model 2 (54)/(55). |
| **pickup / service** | Explicit dwell. §3: "extra time of [c^v_l] and [d^v_m] may be required for loading patients at assembly area [l] or unloading them at medical facility [m]". Loading time enters the recursion (29) and (54) via the pickup indicator. |
| **→ shelter / destination** | Delivery to a hospital (both priorities) or shelter (low priority only, constraint (4)), with unloading dwell `d^v_m`. |

The chain repeats: vehicles chain trips without returning to base (§7), Table 3 shows 18 stops
`H5 → A2 → A1 → S6 → A3 → S6 → …`.

**Note the direction of the constraint.** The *inbound* leg is fire-constrained in Model 2 —
constraint (53) applies to every arc `(l, l')` regardless of whether `l'` is an assembly area
(inbound) or a medical facility (outbound). CURRENT_THESIS RQ2's phrase "fire arrival constraints
on *every leg*, not just the last" is a literal description of Model 2's constraint set.

---

## 4. Q-M3 — Is dispatch time a decision variable? **NO — it is fixed at zero by constraint**

This is the single most important finding in this review.

Model 1, constraint (26):

> `AT^{v,k=0}_{ls} = 0   ∀ v, l, s`   (26)

Model 2, constraint (50):

> `AT^{ll'_s}_{(v,k=0)} = 0   ∀ s, v, l, l'`   (50)

Authors' own gloss, identical in both places:

> "Constraints (26) and (27) impose that arrival times start at 0 and are set to zero for unvisited
> nodes." (§4, after (27))

> "Constraints (50) and (51) state that arrival times start at 0 and are set to 0 for unvisited
> nodes." (§5.4, after (51))

Corroborated operationally by Table 3, whose first column reads `Stop 1 | H5 | Arrival Time [min] 0`.

The only time-valued decision variable in the entire model is Table 1's
`AT` — "(2nd-stage) Time of vehicle [v]'s [k]-th stop at location [l] under scenario [s]" — which is
an **arrival** time at a stop, constrained from below by the travel-time recursion (29)/(30)/(54)/(55)
and from above by the window constraints (28)/(52)/(53). There is no release-time variable, no
departure-from-base variable, no delay variable, no waiting variable.

**Consequence.** Every vehicle departs at t = 0. The model chooses *where* vehicles go and *how many*
to activate. It never chooses *when* to start. "When to start" is not a question this paper asks.

---

## 5. Q-M4 — *Could* the formulation yield a latest feasible dispatch time?
**YES — by parametric re-solving. Label: `MATHEMATICALLY_IMPLICIT`.**

The quantity is obtainable, but not by reading any variable. Two routes, neither taken by the authors:

1. **Uniform shift of the time origin.** All windows `TW^s_l`, `STR^s_{ll'}`, `TWR^s_{ll'}` are absolute
   times on an axis whose origin is fixed at 0 by (26)/(50). Re-solve with every window replaced by
   `TW − δ` and bisect on δ for the largest δ under which the objective still evacuates everyone.
   That δ is a latest-dispatch offset. It requires one full re-solve per bisection step, each of
   which the paper reports costs minutes to an hour (Table 4: 121 s – 3,776 s by Benders;
   24 h by direct solver).
2. **Relaxing (26)/(50) into a variable.** Replace the equality with `AT^{v,k=0} = τ_v ≥ 0` and
   maximize `Σ τ_v`. This is a *different model* — the authors neither write it nor mention it.

Both routes need `feasible` to be defined, which the paper does not do: its objective *permits*
leaving patients behind at a penalty (`np_n`, "Penalty of leaving a patient with severity [n] behind"),
so "infeasible" is never reached — the plan degrades continuously instead of failing. Any
latest-dispatch extraction would first have to impose a full-evacuation requirement that the paper
deliberately avoids.

---

## 6. Q-M5 — Is a latest dispatch time explicitly studied as an output? **NO**

Searched the full text for `dispatch`, `depart`, `departure`, `latest`, `deadline`, `start time`,
`time zero`, `sensitivity`. Results:

- `dispatch` occurs **twice**, both irrelevant: §7 "they do not have to return to their original
  dispatch location after each trip", and Table 1's `IL` gloss. Never as a time.
- `departure` occurs **once**, in a reference title (Transportation Research Part D, on evacuee
  departure timing — a *cited* paper, not this paper's content).
- `latest`, `deadline`, `dispatch time`: **zero occurrences.**

**Every reported output is a plan or a completion time, never a start time:**

| Reported output | Location |
|---|---|
| Fleet size — "6 ambulances, 16 buses, and 0 helicopters" | §6.5.2 |
| Fleet size, small instance — "two ambulances, two buses, and zero helicopters" | §6.3 |
| Shelters opened — S8 and S9 (case study); S6 (small instance) | §6.5.2, §6.3 |
| Per-vehicle itinerary with arrival times 0…250 min | Table 3 |
| Objective value and solve time by configuration | Table 4 |
| Drop-off counts by facility across categories | Table 7, Figure 7 |
| **"Evacuation time for given % of the population [min]"** — 50% / 70% / 100% | **Table 7** |
| "full evacuation can be done within the time windows resulting in almost 10% improvement" | §6.5.2 |

Table 7's last block is the closest thing in the paper to our quantity, and it is the **wrong end
of the mission**: it is a *completion* time measured forward from a fixed t=0 (e.g. category 1:
50% in 158 min, 70% in 242 min, 100% in 646 min). It answers "how long does this take", not
"how late may we begin".

**Sensitivity analyses that exist** (§6.5.2, Figures 3, 5, 7; Table 7): over shelter-combination
count, fire origin (N vs S), total population, high-priority proportion, and average time-window
length. **No sensitivity over dispatch or start time**, because there is no such quantity.

**Verdict on Q-M4/Q-M5 jointly: `MATHEMATICALLY_IMPLICIT`, decisively not
`EXPLICITLY_STUDIED_CONTRIBUTION`.**

---

## 7. Q-M6 — Shared evolving fire field for ingress and egress? **NO on both counts**

Two separate findings; do not conflate them.

**(a) There is no evolving fire field at all.** The fire never appears as a state. It appears only as
three families of scalar closure-time *parameters* — `TW^s_l` (node), `STR^s_{ll'}` (arc soft),
`TWR^s_{ll'}` (arc hard) — drawn **independently** from `Uniform(400, 850)` (Table 6). No fire-spread
model, no rate of spread, no wind field, no fuel, no ignition-to-arrival computation, no ensemble,
no forecast, no forecast error, no latency. §3's causal claim —

> "Depending on the origin of the fire, wind direction, and vegetation density, each assembly area
> [l] is subject to a time window" (§3)

— is **asserted and never operationalised**. Table 6 samples "Fire origin `Random(south, west, north)`"
as a *separate, independent* draw from the window draws. Nothing in the generation procedure makes
the window of a southern node depend on the fire originating in the south. The only place the
dependence surfaces is post-hoc narrative interpretation of the aggregated categories (§6.5.2:
"In category 32 … the fire originates in the south, allowing more time to evacuate northern assembly
areas"), which reads a causal story onto categories whose parameters were drawn independently.
This is a **real, defensible, citable weakness**.

**(b) There is no evacuee egress stream to share a field with.** The only movers in the model are
the evacuation vehicles. Self-evacuating residents do not exist in the formulation; the drill they
cite involved self-evacuation ("The evacuation relied on the residents use of their own vehicles",
§6.5.1) but that traffic is not modelled. Roads have unlimited capacity (§3: "Roads have unlimited
capacity but their availability can be affected by the fire"); congestion enters only as a flat
exogenous `y%` travel-time surcharge on partially disrupted arcs. There is no counterflow, no
inbound-vs-outbound interaction, no shared road demand.

**What *is* shared:** within Model 2, a vehicle's inbound leg (facility → assembly area) and its
loaded outbound leg (assembly area → facility) are subject to the **same arc parameter set**
`TWR^s_{ll'}` / `STR^s_{ll'}`. So ingress and egress face one common hazard *parameterisation*. That
is a genuine structural overlap with RQ2 and must be conceded. It is not a shared *field*.

---

## 8. Q-M7 — Finite fleets and resources? **YES, with explicit numbers**

Table 1: "[Λ2] Maximum number of vehicles of type [ambulance, bus, helicopter] that we have."
Constraint (37): `Σ_{m∈M2} y_m ≤ MAX_shelters`.

**Case study (Roxborough Park), §6.5.1 — availability:**

| Type | Count available | Capacity | Avg. speed |
|---|---|---|---|
| Ambulance | **10** | 1 patient | 60 km/h |
| Bus | **20** | 10 patients | 50 km/h |
| Helicopter | **2** | 2 patients | 200 km/h |

**Case study — activated (§6.5.2):** 6 ambulances, 16 buses, 0 helicopters; 2 of 3 candidate
shelters opened (S8, S9). Hospitals: 3, each 80 beds (UCHealth Highlands Ranch, Sky Ridge Medical
Center, AdventHealth Castle Rock). Demand: ~900 people (10% of Roxborough Park's 9,057), of whom
~5% high-priority (`Bin(p1 = 0.05)`, Table 6).

**Small instance (Table 2):** 4 ambulances (cap 1), 4 buses (cap 6), 2 helicopters (cap 2);
activated 2 / 2 / 0. Max 20 stops per vehicle throughout.

Only ambulances may carry priority-1 patients (constraints (31)–(32)); shelters may not receive
priority-1 patients (constraint (4)); facility capacity is enforced per priority level per scenario
(constraints (5)–(6)).

---

## 9. Q-M8 — A feasible dispatch *set*, or one optimization per scenario? **One optimization**

There is no dispatch set, and no set of any timing quantity.

Structure: 10,000 scenarios sampled from Table 6, collapsed to **54 aggregated "categories"**
(2 window-length × 3 fire-origin × 3 population × 3 priority-mix), each category's parameters being
the **average** of the scenarios in it, with probability = its share of 10,000 (§6.5.1). The
two-stage stochastic program is then solved **once** over those 54 categories: a restricted master
problem in the first-stage binaries plus |S| scenario subproblems. Output: one first-stage plan
(fleet + shelters) plus one routing schedule per category.

Averaging 10,000 scenarios into 54 category means is itself worth noting: it destroys the tails of
the window distribution, which is precisely where a latest-dispatch quantity would live.

---

## 10. WG-DBD component scoring

Scored independently against **this paper only**, with the evidence that decides each.

### WG-DBD-1 — Complete assisted mission = responder ingress + service + egress
**`OCCUPIED`**

Base is a medical facility (§3, constraints (7)–(8), Table 3 stop 1 = H5); ingress to the assembly
area; explicit loading dwell `c^v_l` (§3); egress to hospital or shelter with unloading dwell
`d^v_m`; all three legs timed by the arrival recursion (29)/(30), and in Model 2 all three subject
to arc hard windows via (53). This component is taken. The sentence "nobody models the assisted
evacuation round trip as one timed mission" is now **forbidden**.

*Caveat recorded for honesty, not as a defence:* the pickup node is a temporary **assembly area**,
not a residence (§1). The door-to-door leg is outside this model and the authors list dynamic
arrival at assembly areas as unexplored (§7). This narrows the component slightly; it does not
un-occupy it.

### WG-DBD-2 — Fire-relative feasible dispatch times computed
**`NOT_OCCUPIED`**

Dispatch is a constant, not a computed quantity: `AT^{v,k=0} = 0` (26)/(50). Nothing in the paper
computes any time *at which to begin*, fire-relative or otherwise. The windows are fire-relative in
*name* — "after which the route … is reached by the fire" (§5.4) — but they are sampled from
`Uniform(400, 850)` and applied to arrival, not to departure.

### WG-DBD-3 — Latest feasible dispatch instant reported as an operational quantity
**`NOT_OCCUPIED`**

Zero occurrences of `latest`, `deadline`, or `dispatch time` in the body. The only reported
temporal results are forward completion times (Table 7) and per-stop arrival times (Table 3).
See §6 above. This is the component WG-C-003's survival depends on, and it is **open**.

### WG-DBD-4 — Non-monotone feasible dispatch windows as a SET
**`NOT_OCCUPIED`**

Each node and each arc gets exactly **one** closure instant, after which it is permanently
unavailable — "after which it cannot be visited" (§3), "becomes completely unavailable" (§5.4).
Strictly monotone: nothing ever reopens, and there is no second interval. The soft window
`STR^s_{ll'}` does not create an interval either — it is a one-way step that raises travel time by
`y%` from that instant on (constraints (56)–(57)). No set-valued feasibility object exists anywhere.

### WG-DBD-5 — Full traversal-interval hazard evaluated (vs hazard checked only at arc entry)
**`NOT_OCCUPIED` — and the paper is demonstrably arc-entry-only**

Constraint (53) reads `Σ_{l''} AT^{l''l_s}_{vk} ≤ TWR^s_{ll'} + M(1 − x^{ll'_s}_{vk})`. The bounded
quantity is the arrival time **at l**, the *origin* of arc `(l, l')` — i.e. the moment the vehicle
*enters* the arc. Nothing constrains the arrival at `l'`, nor the state of the arc during traversal.
The soft-disruption trigger (56) is built the same way, and the authors state the logic in words:

> "If the arrival time of vehicle [v] at location [l] in its [k]th stop is greater than [STR^s_{ll'}],
> then a binary variable … must be equal to 1" (§5.4, before (56))

**Operational consequence:** a vehicle that enters an arc one minute before the fire reaches it
completes the traversal unharmed, however long the arc takes — up to 38.6 km in the case-study
distance matrix (Table 5, A1→H5), ~39 min at the 60 km/h ambulance speed. The hazard is a gate at
the entrance, not a field along the path. This is a clean, citable difference for WildfireGuardian.

### WG-DBD-6 — Feasibility conditioned on decision-time information rather than oracle knowledge
**`NOT_OCCUPIED`** (with a first-stage nuance recorded)

This is a two-stage stochastic program. The **first stage** (fleet size `z_v`, shelter activation
`y_m`) is genuinely non-anticipative — chosen before the scenario is revealed, which is real
decision-time conditioning for the *resource* decision. But **mission feasibility is second-stage**,
and every second-stage variable is indexed by `s` and optimized knowing that scenario's realized
`TW^s_l`, `STR^s_{ll'}` and `TWR^s_{ll'}` — i.e. knowing exactly when the fire reaches every node and
every arc. Routing feasibility therefore uses **oracle future knowledge** of fire arrival. There is
no filtration, no rolling horizon, no re-planning on observation, no forecast, and no information
constraint on the routing.

Recorded explicitly so the nuance cannot be said to have been hidden: the *resource* decision is
non-anticipative; the *feasibility* decision is not.

### WG-DBD-7 — Korean rural wildfire geometry
**`NOT_OCCUPIED`**

Roxborough Park, Colorado, USA — a WUI community of ~900 homes, ~9,057 people, on Google Maps
distances from January 2025 (§6.5.1, Table 5). Canada/USA/Australia framing throughout (§1).
Korea does not appear in the paper.

---

## 11. Verdict

**`MATHEMATICALLY_IMPLICIT`.** The latest feasible dispatch time is obtainable from this
formulation by parametric re-solving over a shifted time origin. It is never extracted, never
reported, never plotted, never varied, and never named. The paper contains no variable, no
constraint, no table row, no figure axis and no sentence about when to depart. Dispatch is an
*assumption* in this model (t = 0), not a result.

A constraint that bounds arrival times is not a reported latest dispatch time, and this paper
contains only the former.

**Does it kill the dispatch-by-deadline claim? — ONLY PARTLY.**

It takes **WG-DBD-1** outright and must be conceded without qualification. It leaves
**WG-DBD-2, -3, -4, -5, -6, -7** standing — six of seven. The surviving contribution is narrower
than "we model the assisted-evacuation round trip" (false) but is not empty: it is *the latest
dispatch instant as the reported output, as a set rather than a scalar, from a modelled future fire,
with hazard evaluated over the whole traversal interval, under decision-time information.*

Each of those five qualifiers must now be defended against other papers — `beyki2026modular` first
(`novelty/NOVELTY_THREATS.md` §4 item 1). This review settles Moradi only.

---

## 12. Kamyabniya (2022) — identified

Cited in §2: "Closely related to our study are the works by Shahparvari et al. …, Shahparvari &
Abbasi (2017) and Kamyabniya Kamyabniya (2022)." (The doubled surname is a citation-macro error in
the original.) The reference list entry, **verbatim**:

> Kamyabniya, A. (2022). Integrated and Coordinated Relief Logistics Planning Under Uncertainty for
> Relief Logistics Operations. University of Ottawa.

**It is a University of Ottawa doctoral thesis**, not a journal article — which is why it could not
be found by article search. Same institution as Moradi/Sauré/Patrick; Sauré and Patrick are
co-authors on Kamyabniya et al. (2024). Almost certainly Sauré/Patrick supervised it, i.e. Moradi
is a successor thesis in the same group.

What Moradi et al. attribute to it (§2):

> "Kamyabniya, on the other hand, proposed a mixed-integer programming model for supported
> evacuation, jointly optimizing temporary shelter locations and vehicle routing. His model,
> formulated as a time-step-based two-stage stochastic problem, was ultimately solved using
> meta-heuristic techniques." (§2)

**Status: `E1` — this is a reference-list record only.** We have not seen the thesis. The
description above is Moradi et al.'s characterisation, not ours, and per `AGENTS.md` §3 we may not
attribute a claim to it. It stays on the watch list; the note is "time-step-based" — a discretised
time axis, which is the structure most likely to contain a per-time-step feasibility indicator, and
therefore the closest thing to a dispatch *set* in this lineage. **Agent A should retrieve it from
uO Research (University of Ottawa's institutional repository).**

Second, distinct Kamyabniya record in the same reference list, not to be confused with it:

> Kamyabniya, A., Sauré, A., Salman, F. S., Bénichou, N., & Patrick, J. (2024). Optimization models
> for disaster response operations: A literature review. OR Spectrum, 46, 737–783.

---

## 13. Items for `novelty/OPEN_QUESTIONS.md` (not written by this agent)

1. Kamyabniya (2022), uOttawa thesis — unretrieved, E1, plausibly a CRITICAL threat via its
   time-step formulation. Retrieve from uO Research.
2. Flores et al. (2023), *Safety Science* 164:106117 — the prior supported-evacuation wildfire
   model Moradi et al. position against (§2). Still unretrieved.
3. Journal version of Moradi et al. — submitted to an unnamed Elsevier journal ~Aug 2025, still
   arXiv-only at 2026-08-05 with no v2. If peer review adds spread-model-derived windows or a
   departure-time variable, WG-DBD-2 and -3 close. **Re-check periodically.**
4. Gwynne et al. (2023), *Fire Technology* 59(2):879–901 — the Roxborough Park drill dataset.
