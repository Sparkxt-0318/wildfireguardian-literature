# moradi2026supported

## Citation
Moradi, S., Sauré, A., & Patrick, J. "A Relaxation-Based Decomposition Approach for Solving a
Supported-Evacuation Problem in Wildfires." arXiv:2608.05413 [math.OC]. 33 pages, 8 figures.
Telfer School of Management, University of Ottawa. DOI `10.48550/arXiv.2608.05413`
(arXiv-issued via DataCite; **not** a journal DOI). Only v1 exists.

## Publication status
`PREPRINT`. Not peer-reviewed. Submitted to an unnamed Elsevier journal per the title page; no
acceptance evidence retrieved, no journal-reference field on arXiv. **This does not reduce its force
as prior art** (NOVELTY_STANDARD §3.3) — a preprint occupies a claim exactly as thoroughly as a
journal paper.

**Priority date (resolved 2026-09-20, both readings verified):**
- arXiv abstract page submission history: "[v1] Wed, 5 Aug 2026 21:11:26 UTC (7,635 KB)"
- PDF title page footer: "Preprint submitted to Elsevier August 8, 2025"

The footer is the manuscript's compile-time stamp, corroborated by §6.5.1's use of "Google Maps
estimates from January 2025". So the manuscript is ~1 year older than its arXiv posting. **The
earliest demonstrable public priority date is 2026-08-05**; August 2025 is the authors' own
unverifiable title-page claim and may not be asserted by us as established.

## Problem
Supported evacuation in wildfires: moving people who *cannot evacuate independently* — hospital
patients, long-term-care residents, people with disabilities and limited mobility, people with no
vehicles, tourists — from temporary assembly areas inside the fire zone to hospitals and
special-needs medical shelters (SMSs), using a heterogeneous fleet (ambulances, buses, helicopters).

Joint decisions: (1) which shelters to open, (2) how many vehicles of each type to activate,
(3) pickup/delivery routes and schedules.

**Note the pickup node.** Residents are collected at *temporary assembly areas*, not at their homes:
"certain locations within the fire zone serve as temporary assembly areas housing or gathering
patients who are unable to evacuate by themselves" (§1). How residents reach an assembly area is
outside this model; the authors list dynamic arrival there as unexplored (§7).

## Method
Two-stage stochastic (TSS) mixed-integer program.
- **First stage:** SMS location (capacitated facility location) + fleet sizing per vehicle type.
- **Second stage, per scenario s:** multi-vehicle routing with **hard time windows**, split pickups,
  split deliveries, vehicle-specific loading (`c^v_l`) and unloading (`d^v_m`) dwell times,
  continuous-time operation with **no return-to-depot constraint**.
- Two model variants. **Model 1**: fixed per-scenario travel times; vehicles of a type are
  interchangeable; **no arc time windows**. **Model 2** (the one they call more realistic, and the
  one the case study is solved with): arcs carry *two* time windows — a **soft** window
  `STR^s_{ll'}` after which the arc is partially disrupted and travel time rises by y%, and a
  **hard** window `TWR^s_{ll'}` after which the arc "is reached by the fire and becomes completely
  unavailable." Under Model 2 vehicles can no longer be treated independently and benefit from
  cooperation.
- **Solution:** relaxation + Logic-Based Benders Decomposition; restricted master problem over
  first-stage variables, |S| scenario subproblems decomposed by vehicle, combinatorial Benders cuts
  driving a neighbourhood search, plus logic-based valid inequalities (minimum resource levels,
  shelter-activation rules).
- **Benchmarks:** three heuristic policies — Closest-First (CF), Shortest-Time-Window-First (STWF),
  Most-Crowded-First (MCF).

## Data
Roxborough Park, Colorado (WUI community, ~900 homes, population 9,057; the Gwynne et al. 2023
community wildfire evacuation drill involved 143 households). Three assembly areas (fire station,
intermediate school, primary school), three hospitals at 80 beds each, three candidate shelter sites.
Distances from Google Maps, January 2025 (Table 5). Demand ~900 people = 10% of population.
10,000 stochastic scenarios sampled and aggregated into 54 categories on four criteria: **fire origin
(south / north / west)**, average time-window length (long / short), population level, and
proportion of high-priority patients. Each category's parameters are the **average** over the
scenarios falling into it.

## Outputs
- Number of vehicles of each type to activate (case study: **6 ambulances, 16 buses, 0 helicopters**
  out of 10 / 20 / 2 available; small instance: 2 / 2 / 0 out of 4 / 4 / 2).
- Which shelters to open (S8 and S9 of three candidates).
- Routes, split pickups and split deliveries per scenario; per-stop arrival times (Table 3).
- "Evacuation time for given % of the population [min]" at 50 / 70 / 100% (Table 7) — a
  **completion** time measured forward from a fixed t = 0.
- ~10% improvement over the benchmark heuristics.
- **No dispatch time, departure deadline, or latest-feasible-departure quantity is reported
  anywhere.** The words `latest`, `deadline` and `dispatch time` do not occur in the body.

## Key equations
- **(26)** `AT^{v,k=0}_{ls} = 0` and **(50)** `AT^{ll'_s}_{(v,k=0)} = 0` — arrival times start at
  zero. **Dispatch is fixed by constraint, not chosen.**
- **(28)** `AT^{vk}_{ls} ≤ (TW^s_l − c^v_l) · [visited]` — forbids travelling to nodes whose time
  windows are closed.
- **(29)/(30)**, Model 2 **(54)/(55)** — arrival-time recursion: previous arrival + loading dwell +
  unloading dwell + travel time (inflated by y% if the soft window has passed), big-M switched on
  the routing binary.
- **(52)/(53)** — Model 2 replacements of (28): forbid travelling to nodes, **and using routes**,
  whose time windows have closed. (53) bounds the arrival time at the arc's **origin**, i.e. at
  arc entry.
- **(56)/(57)** — set the partial-disruption indicator when arrival at the arc's origin exceeds
  `STR^s_{ll'}`.
- **(59)/(60)/(61)** — heuristic estimators for trips per vehicle, vehicles per type, and best
  shelter combination.

## Assumptions
- Roads have unlimited capacity; congestion appears only as a flat exogenous percentage travel-time
  surcharge on "partially disrupted" arcs. No self-evacuating traffic is modelled at all.
- **Time windows are exogenous stochastic parameters, not outputs of a fire-spread model.** In the
  case study, assembly-area windows and route windows are both drawn from **Uniform(400, 850)
  minutes** (Table 6), and **fire origin is drawn independently** as
  `Random(south, west, north)`. The causal sentence in §3 ("Depending on the origin of the fire,
  wind direction, and vegetation density…") is asserted, never operationalised: nothing in the
  sampling makes a southern node's window depend on a southern ignition.
- Medical facilities lie outside the fire zone and carry **no** time window — only capacity.
- The number of patients at each assembly area is known at the start and does not change (the
  authors flag dynamic arrival as an open problem).
- Each vehicle starts at a specific medical facility under each scenario (binary parameter `IL^s_{vm}`).
- Maximum 20 stops per vehicle.

## Validation
Numerical experiments on four generated configurations plus the Roxborough Park case
parameterisation. No validation against a real supported evacuation. Benchmarking is against the
authors' own three heuristics, not against an external published method. Optimality gaps are large
(11%–47% for the direct solver at 24 h); the authors attribute them to weak lower bounds.

## Limitations
Stated by the authors: static patient counts at assembly areas; dynamic arrival unexplored.
Identified here: the fire is never simulated — the coupling from fire behaviour to time windows is
asserted rather than computed; no fire-spread model, no ensemble, no forecast, no forecast error,
no forecast latency; hazard is gated at arc entry only; averaging 10,000 scenarios into 54 category
means destroys the distribution tails where a timing deadline would live.

---

## Full-text verification 2026-09-20

**Agent C — Verification Auditor.** `fulltext_status: FULL_TEXT_READ`. `evidence_level: E4`.
Access route: alphaXiv MCP `get_paper_content(fullText=true)`, cross-checked against alphaXiv
`answer_pdf_queries` page extraction and the arXiv abstract page.
**Caveat:** `arxiv.org/html/2608.05413v1` returns 404 and ar5iv serves no LaTeX HTML, so no second
*rendering* exists — the cross-check is two independent extraction passes over the same PDF, which
agreed exactly. Numbers are E4 for what the PDF says; they are **not E5**.
Detailed extraction with locations: `literature/reviews/fulltext-moradi2026.md`.

### Q-M1 — What carries a time window? (the crux)

| Entity | Window? | Evidence |
|---|---|---|
| **Residents** | **NO** individually; the *assembly area* they wait at carries one | §3: "each assembly area [l] is subject to a time window of [TW^s_l] after which it cannot be visited". Residents are a count with a priority level, no temporal attribute |
| **Facilities** | **NO** | Hospitals/shelters carry capacity per priority level only (Table 1; constraints (5)–(6)); they sit "Outside the fire zone" (§3) and are never closed |
| **Arcs / routes** | **YES — Model 2 only, and two of them** | §5.4: soft `STR^s_{ll'}` ("becomes partially disrupted… increasing the route travel time by y%") and hard `TWR^s_{ll'}` ("the route connecting l to l' is reached by the fire and becomes completely unavailable") |
| **Vehicles** | **NO** | Capacity, speed, costs, initial location, dwell times, max 20 stops. No shift, no release time, no return-by time. §7: "they do not have to return to their original dispatch location after each trip" |
| **Complete missions** | **NO** | No trip-level or horizon-level window anywhere. Only a soft objective penalty `ξ` — Table 1: "A penalty term to minimize the arrival times" |

Windows attach to **nodes (assembly areas) and arcs (Model 2)**. Nothing else.

### Q-M2 — `base -> resident -> pickup -> destination`? **YES**
Base = the medical facility a vehicle is stationed at (§3; constraints (7)–(8); Table 3 stop 1 = H5).
Ingress to an assembly area; explicit loading dwell `c^v_l` and unloading dwell `d^v_m` (§3);
delivery to hospital or shelter. In Model 2 constraint (53) applies to **every** arc regardless of
direction, so the inbound leg is fire-constrained exactly as the outbound leg is. Caveat: the
pickup node is an assembly area, not a residence.

### Q-M3 — Is dispatch time a decision variable? **NO — fixed at zero by constraint**
Constraint **(26)** (Model 1) and **(50)** (Model 2) force `AT^{v,k=0} = 0` for every vehicle.
Authors' gloss: "Constraints (26) and (27) impose that arrival times start at 0" (§4);
"Constraints (50) and (51) state that arrival times start at 0" (§5.4). Table 3 confirms:
stop 1, arrival time 0. The only time-valued variable is `AT` — "Time of vehicle [v]'s [k]-th stop
at location [l] under scenario [s]" (Table 1) — an **arrival** time. No release, departure, delay
or waiting variable exists. **Every vehicle departs at t = 0.**

### Q-M4 — Could the latest feasible dispatch time be obtained? **YES — by parametric re-solving**
Windows are absolute times on an axis whose origin (26)/(50) pins at 0. Shifting every window to
`TW − δ` and bisecting on δ would yield a latest-dispatch offset, at one full re-solve per step
(121 s–3,776 s by Benders, 24 h direct — Table 4). Alternatively (26)/(50) could be relaxed into a
variable `τ_v` — but that is a different model the authors neither write nor mention. Either route
first needs "feasible" defined, which the paper avoids: leaving patients behind is *penalised*
(`np_n`), never infeasible, so the plan degrades continuously instead of failing.
**Label: `MATHEMATICALLY_IMPLICIT`.**

### Q-M5 — Is that latest time explicitly studied as an output? **NO**
`latest`, `deadline`, `dispatch time`: zero occurrences in the body. `dispatch` occurs twice, both
meaning a *location*. Every reported output is a plan (fleet, shelters, routes) or a **completion**
time: Table 7's "Evacuation time for given % of the population [min]" (50% / 70% / 100%), which is
the wrong end of the mission. Sensitivity analyses cover shelter count, fire origin, population,
priority mix and window length — never dispatch or start time.
**Label: NOT `EXPLICITLY_STUDIED_CONTRIBUTION`.**

### Q-M6 — Shared evolving fire field for ingress and egress? **NO, twice over**
(a) There is **no fire field**. The fire appears only as scalar closure-time parameters
`TW^s_l`, `STR^s_{ll'}`, `TWR^s_{ll'}`, all drawn from `Uniform(400, 850)` (Table 6), with fire origin
drawn **independently**. No spread model, no wind, no fuel, no ensemble, no forecast, no latency.
(b) There is **no evacuee egress stream**: the only movers are the evacuation vehicles;
self-evacuating traffic is absent and roads have unlimited capacity (§3).
**What must be conceded:** within Model 2 a vehicle's inbound and loaded outbound legs are subject
to the *same arc parameter set*. One common hazard parameterisation — not a shared field.

### Q-M7 — Finite fleets and resources? **YES**
Case study availability: **10 ambulances** (cap 1, 60 km/h), **20 buses** (cap 10, 50 km/h),
**2 helicopters** (cap 2, 200 km/h); 3 candidate shelters; 3 hospitals at 80 beds.
Activated: **6 / 16 / 0**, shelters S8 and S9. Small instance: 4 / 4 / 2 available, 2 / 2 / 0
activated. Only ambulances carry priority-1 patients (constraints (31)–(32)); shelters take
low-priority only (constraint (4)).

### Q-M8 — A feasible dispatch set, or one optimization per scenario? **One optimization**
10,000 sampled scenarios collapsed to 54 aggregated categories by *averaging*, solved once as a
two-stage program (RMP + |S| subproblems). One first-stage plan, one routing schedule per category.
No set-valued output of any kind, timing or otherwise.

### WG-DBD component scoring — this paper only

| Component | Score | Deciding evidence |
|---|---|---|
| **WG-DBD-1** Complete assisted mission = ingress + service + egress | **OCCUPIED** | Base at a medical facility (§3, (7)–(8)); loading dwell `c^v_l`; delivery with unloading dwell; all legs timed by (29)/(30)/(54)/(55) and gated by (53). Caveat: pickup node is an assembly area, not a residence |
| **WG-DBD-2** Fire-relative feasible dispatch times computed | **NOT_OCCUPIED** | Dispatch is the constant 0, by (26)/(50). Nothing computes a time at which to begin |
| **WG-DBD-3** Latest feasible dispatch instant reported as an operational quantity | **NOT_OCCUPIED** | Word absent from the paper; only forward completion times (Table 7) and per-stop arrival times (Table 3) |
| **WG-DBD-4** Non-monotone feasible dispatch windows as a SET | **NOT_OCCUPIED** | One closure instant per node and per arc, permanent — "after which it cannot be visited" (§3), "becomes completely unavailable" (§5.4). Strictly monotone; the soft window is a one-way step, not an interval |
| **WG-DBD-5** Full traversal-interval hazard evaluated | **NOT_OCCUPIED** | (53) bounds arrival at the arc's **origin**; (56) triggers on arrival at the origin. Nothing checks arc state at exit or during traversal — a vehicle entering one minute before closure traverses safely, up to 38.6 km (Table 5) |
| **WG-DBD-6** Feasibility conditioned on decision-time information, not oracle knowledge | **NOT_OCCUPIED** | Second-stage routing is optimized knowing the realized `TW^s`, `STR^s`, `TWR^s` — oracle knowledge of fire arrival. *Nuance recorded:* the first-stage fleet/shelter decision **is** non-anticipative, but mission feasibility is second-stage |
| **WG-DBD-7** Korean rural wildfire geometry | **NOT_OCCUPIED** | Roxborough Park, Colorado; Canada/USA/Australia framing. Korea absent |

### Verdict

**`MATHEMATICALLY_IMPLICIT`, not `EXPLICITLY_STUDIED_CONTRIBUTION`.** The latest feasible dispatch
time is obtainable from this formulation by parametric re-solving. It is never extracted, reported,
plotted, varied or named. Dispatch is an *assumption* here (t = 0), not a result.

**Does this paper kill the dispatch-by-deadline claim? — ONLY PARTLY.** It takes **WG-DBD-1**
outright. It leaves WG-DBD-2 through -7 standing. What survives is narrower than "we model the
assisted-evacuation round trip" — that sentence is now forbidden — but not empty.

---

## WildfireGuardian overlap
Still the **single most dangerous paper found for WildfireGuardian**. It overlaps on four axes:
1. **Population.** Exactly WildfireGuardian's population, and defined non-medically as well
   ("people with no vehicles"), which is the definition PROJECT_CONTEXT requires us to use.
2. **The full round trip.** Base → assembly area → explicit loading dwell → hospital/shelter.
   WildfireGuardian's `base -> resident -> pickup -> safe destination` decomposition is already the
   object of study. **Confirmed at E4.**
3. **Fire-arrival feasibility on the inbound leg.** Model 2's hard arc window binds on the inbound
   leg exactly as on the outbound leg. RQ2's "fire arrival constraints on *every leg*, not just the
   last" describes Model 2's constraint set. **Confirmed at E4 — but see WG-DBD-5: the gate is at
   arc entry only.**
4. **Scarce resources.** First-stage fleet sizing plus shelter activation, with explicit availability
   bounds (10 / 20 / 2).

## WildfireGuardian difference
Operational, per NOVELTY_STANDARD §6. Full-text reading **strengthened** this list from three items
to five; each is now anchored to a specific constraint or table.
- **Dispatch is a constant here, not a decision.** (26)/(50) pin `AT^{v,k=0} = 0`. WildfireGuardian
  makes it the decision variable and the reported output.
- **Unit of the output.** Moradi et al. output a plan (fleet count, shelter set, schedule) and a
  *completion* time (Table 7). WildfireGuardian outputs a *latest start* time. Different units,
  opposite ends of the mission.
- **Provenance of the binding times.** `Uniform(400, 850)` minutes with an independently drawn
  categorical fire-origin label (Table 6) vs. derivation from a modelled future fire with reported
  sensitivity to forecast error. Moradi et al. run no forecast sensitivity because there is no forecast.
- **Hazard gating.** Arc entry only, per (53)/(56), vs. the full traversal interval.
- **Information structure.** Second-stage routing sees the realized fire-arrival times (oracle) vs.
  feasibility conditioned on what is knowable at decision time.

## Novelty threat
**level: CRITICAL** (unchanged after full text).
- **WG-C-005** → `OCCUPIED`. Title-level contribution, in wildfire, with Colorado WUI data. E4.
- **WG-C-011** → `OCCUPIED`. First-stage fleet sizing and shelter activation under cost,
  benchmarked against three heuristics. E4.
- **WG-C-003** → `WEAKENED`, not occupied — **confirmed at E4, which is the level
  `docs/EVIDENCE_LEVELS.md` §Rule 1 requires before a status may be settled.** The constraint
  structure is occupied. What survives is the deadline as the reported output, as a set rather than
  a scalar, from a modelled future fire, gated over the whole traversal, under decision-time
  information.

## Quotes / page references
- "the route connecting l to l' is reached by the fire and becomes completely unavailable" (§5.4).
- "supported-evacuation, which involves assisting individuals unable to evacuate independently such
  as hospital patients, long-term care residents, and people with disabilities" (Abstract).
- "individuals with disabilities and limited mobility, seniors residing in long-term care facilities
  and retirement homes, people with no vehicles, and tourists" (§1).
- "each assembly area [l] is subject to a time window of [TW^s_l] after which it cannot be visited" (§3).
- "Constraints (26) and (27) impose that arrival times start at 0 and are set to zero for unvisited
  nodes" (§4, after eq. 27).
- "Constraints (52) and (53), respectively, forbid traveling to nodes and using routes whose time
  windows are closed" (§5.4, after eq. 53).
- "Time windows for assembly areas [min] Uniform(400, 850)" and "Time windows for routes [min]
  Uniform(400, 850)" and "Fire origin Random(south,west, north)" (Table 6, §6.5.1).
- "Solving Model 2, which is the more realistic formulation, provided a solution with 6 ambulances,
  16 buses, and 0 helicopters" (§6.5.2).
- "Evacuation time for given % of the population [min]" (Table 7 row label, §6.5.2).
- "they do not have to return to their original dispatch location after each trip" (§7).
- "Preprint submitted to Elsevier August 8, 2025" (PDF title page footer, p.1).

## Follow-up papers
- **Kamyabniya (2022) — IDENTIFIED 2026-09-20.** Reference list, verbatim: "Kamyabniya, A. (2022).
  Integrated and Coordinated Relief Logistics Planning Under Uncertainty for Relief Logistics
  Operations. University of Ottawa." **It is a University of Ottawa doctoral thesis**, which is why
  article search never found it. Same institution; Sauré and Patrick co-author Kamyabniya et al.
  (2024), so this is almost certainly a predecessor thesis in the same group. Moradi et al. §2
  describe it as "a mixed-integer programming model for supported evacuation, jointly optimizing
  temporary shelter locations and vehicle routing … formulated as a time-step-based two-stage
  stochastic problem". **Status `E1` — reference-list record only; that description is theirs, not
  ours, and may not be attributed.** Still a potential CRITICAL: a time-step formulation is the
  structure most likely to contain a per-step feasibility indicator, i.e. the closest thing in this
  lineage to a dispatch *set*. **RETRIEVE from uO Research.**
- Kamyabniya, A., Sauré, A., Salman, F. S., Bénichou, N., & Patrick, J. (2024). "Optimization models
  for disaster response operations: A literature review." *OR Spectrum*, 46, 737–783. A distinct
  record — do not confuse with the thesis.
- Flores et al. (2023), *Safety Science* 164:106117 — the prior supported-evacuation wildfire model
  Moradi et al. position against. **RETRIEVE.**
- Gwynne et al. (2023), *Fire Technology* 59(2):879–901 — Roxborough Park drill dataset.
- Cova et al. (2011) — evacuate vs. shelter-in-place optimisation, cited by Moradi et al.
- Zhou & Erdogan (2019) — wildfire resource allocation under spread scenarios.
- Gan et al. (2016) — optimization + traffic simulation for "optimal evacuation timing and routes",
  Victoria, Australia. Cited in §2. Timing-related; **not yet in our corpus — flag for Agent A.**
