# moradi2026supported

## Citation
Moradi, S., Sauré, A., & Patrick, J. "A Relaxation-Based Decomposition Approach for Solving a
Supported-Evacuation Problem in Wildfires." arXiv:2608.05413. Telfer School of Management,
University of Ottawa. Title page states "Preprint submitted to Elsevier August 8, 2025";
arXiv posting date 2026-08-05. DOI: UNVERIFIED.

## Publication status
`PREPRINT`. Not peer-reviewed. Submitted to an Elsevier journal per the title page; no acceptance
evidence retrieved. **This does not reduce its force as prior art** (NOVELTY_STANDARD §3.3) —
a preprint occupies a claim exactly as thoroughly as a journal paper.

## Problem
Supported evacuation in wildfires: moving people who *cannot evacuate independently* — hospital
patients, long-term-care residents, people with disabilities and limited mobility, people with no
vehicles, tourists — from temporary assembly areas inside the fire zone to hospitals and
special-needs medical shelters (SMSs), using a heterogeneous fleet (ambulances, buses, helicopters).

Joint decisions: (1) which shelters to open, (2) how many vehicles of each type to activate,
(3) pickup/delivery routes and schedules.

## Method
Two-stage stochastic (TSS) mixed-integer program.
- **First stage:** SMS location (capacitated facility location) + fleet sizing per vehicle type.
- **Second stage, per scenario s:** multi-vehicle routing with **hard time windows**, split pickups,
  split deliveries, vehicle-specific loading (`c_vY`) and unloading (`d_vR`) dwell times,
  continuous-time operation with **no return-to-depot constraint**.
- Two model variants. **Model 1**: fixed per-scenario travel times; vehicles of a type are
  interchangeable. **Model 2** (the one they call more realistic): arcs carry *two* time windows —
  a **soft** window after which the arc is partially disrupted and travel time rises by y%, and a
  **hard** window after which the arc "is reached by the fire and becomes completely unavailable."
  Under Model 2 vehicles can no longer be treated independently and benefit from cooperation.
- **Solution:** relaxation + Logic-Based Benders Decomposition; restricted master problem over
  first-stage variables, |S| scenario subproblems decomposed by vehicle, combinatorial Benders cuts
  driving a neighbourhood search, plus logic-based valid inequalities (minimum resource levels,
  shelter-activation rules).
- **Benchmarks:** three heuristic policies — Closest-First (CF), Shortest-Time-Window-First (STWF),
  Most-Crowded-First (MCF).

## Data
Roxborough Park, Colorado (WUI community, population ~9,057; the Gwynne et al. 2023 community
wildfire evacuation drill involved 143 households). Assembly areas, hospitals and candidate shelter
sites placed on the Roxborough Park map. 10,000 stochastic scenarios sampled and aggregated into
54 categories on four criteria: **fire origin (south / north / west)**, average time-window length
(long / short), population level, and proportion of high-priority patients.

## Outputs
- Number of vehicles of each type to activate (case study solution: **6 ambulances, 16 buses,
  0 helicopters**).
- Which shelters to open (S8 and S9 of three candidates).
- Routes, split pickups and split deliveries per scenario.
- Number of evacuees moved within the time windows; ~10% improvement over the benchmark heuristics.
- **No dispatch time, departure deadline, or latest-feasible-departure quantity is reported anywhere.**

## Key equations
Not reproduced here (see §4 of the preprint). Structurally relevant constraints:
- Constraint (28): forbids travelling to nodes whose time windows are closed.
- Constraints (50)–(55): Model 2 replacements of (26)–(30), adding the arc-origin-indexed arrival
  variable `AT_ll'^s_{v,k}` and the partial-disruption indicator so that partial and complete arc
  disruptions can be tracked per trip.
- Constraints (52)–(53): forbid travelling to nodes, **and using routes**, whose time windows have closed.

## Assumptions
- Roads have unlimited capacity; congestion appears only as a percentage travel-time surcharge on
  "partially disrupted" arcs.
- **Time windows are exogenous stochastic parameters, not outputs of a fire-spread model.** In the
  numerical experiments assembly-area windows and route windows are both drawn from
  Uniform(400, 850) minutes. Fire origin enters as a three-level categorical scenario label.
- The number of patients at each assembly area is known at the start and does not change (the
  authors flag dynamic arrival as an open problem).
- Each vehicle starts at a specific medical facility under each scenario (binary parameter).

## Validation
Numerical experiments on generated instances plus the Roxborough Park case parameterisation.
No validation against a real supported evacuation. Benchmarking is against the authors' own three
heuristics, not against an external published method.

## Limitations
Stated by the authors: static patient counts at assembly areas; dynamic arrival unexplored.
Identified here: the fire is never simulated — the coupling from fire behaviour to time windows is
asserted ("Depending on the origin of the fire, wind direction, and vegetation density, each
assembly area Y is subject to a time window") rather than computed; no fire-spread model, no
ensemble, no forecast error, no forecast latency.

## WildfireGuardian overlap
This is the **single most dangerous paper found for WildfireGuardian**, and it overlaps on
four axes at once:
1. **Population.** Exactly WildfireGuardian's population: residents who cannot self-evacuate,
   and — importantly — defined non-medically as well ("people with no vehicles"), which is the
   definition PROJECT_CONTEXT requires us to use.
2. **The full round trip.** Vehicles are stationed at medical facilities (= base), travel to
   assembly areas (= resident), incur an explicit loading dwell time (= pickup), and deliver to a
   hospital or shelter (= safe destination). WildfireGuardian's `base -> resident -> pickup ->
   safe destination` decomposition is already the object of study.
3. **Fire-arrival feasibility on the inbound leg.** Model 2's *hard arc time window* is defined as
   the time after which the fire reaches that arc. That constraint binds on the inbound leg
   (facility → assembly area) exactly as it binds on the outbound leg. CURRENT_THESIS RQ2's
   sentence "subject to fire arrival constraints on *every leg*, not just the last" describes
   Model 2's constraint set.
4. **Scarce resources.** First-stage fleet sizing plus shelter activation is scarce-resource
   allocation for assisted evacuation.

## WildfireGuardian difference
Operational, per NOVELTY_STANDARD §6:
- **Unit of the output.** Moradi et al. output a *plan* — a fleet size (integer count), a shelter
  set, and a routing schedule — evaluated by the number of evacuees moved within given windows.
  WildfireGuardian proposes to output a *time*: the latest fire-relative instant `t*` at which
  dispatch may begin such that the round trip still closes. These have different units (vehicles,
  routes vs. minutes-before-fire-arrival) and answer different questions ("what plan?" vs. "how
  late may we start?").
- **Where the time window comes from.** Moradi et al.'s window is an input sampled from
  Uniform(400, 850) min with a categorical fire-origin label. WildfireGuardian proposes to *derive*
  the binding times from a modelled future fire and to report the deadline's sensitivity to
  forecast error, ingress congestion, and pickup dwell. Moradi et al. run no sensitivity analysis
  on forecast quality because there is no forecast.
- **What varies.** Moradi et al. vary population, priority mix, window length, and fire origin.
  WildfireGuardian varies *forecast skill, lead time, and latency*.

This difference is real but **narrow**. It is a difference in reported quantity and in the
provenance of the time windows, not in problem structure. WG-C-003 cannot be defended as
"nobody has modelled the assisted-evacuation round trip against fire arrival" — Moradi et al. have.

## Novelty threat
**level: CRITICAL**
- **WG-C-005** → `OCCUPIED`. "We model assisted/supported evacuation of residents who cannot
  self-evacuate" is this paper's title-level contribution, in wildfire, with Colorado WUI data.
- **WG-C-011** → `OCCUPIED`. First-stage fleet sizing and shelter activation under cost is scarce
  assisted-evacuation resource allocation, benchmarked against three priority heuristics.
- **WG-C-003** → `WEAKENED`, not occupied. The constraint structure (fire-arrival hard windows on
  every arc of a base→pickup→destination trip for non-self-evacuating residents) is occupied.
  What survives is only: the deadline as the reported output, and its derivation from a modelled
  future fire rather than from sampled parameters.

## Quotes / page references
- "the route connecting l to l' is reached by the fire and becomes completely unavailable"
  (§ Model 2, description of the hard arc time window).
- "supported-evacuation, which involves assisting individuals unable to evacuate independently such
  as hospital patients, long-term care residents, and people with disabilities" (Abstract).
- "individuals with disabilities and limited mobility, seniors residing in long-term care facilities
  and retirement homes, people with no vehicles, and tourists" (§1 Introduction).
- "Time windows for assembly areas [min] Uniform(400, 850)" (§6, parameter table).
- "they do not have to return to their original dispatch location after each trip" (§7 Conclusion).

## Follow-up papers
- Flores et al. (2023), Safety Science 164:106117 — the prior supported-evacuation wildfire model
  that Moradi et al. position against. **RETRIEVE.**
- Kamyabniya (2022) — cited by Moradi et al. as a time-step-based two-stage stochastic supported
  evacuation model with joint shelter location and routing. **Primary record NOT retrieved; this is
  a citation-only lead.** Could be a thesis. **RETRIEVE — potentially another CRITICAL paper.**
- Gwynne et al. (2023), Roxborough Park community wildfire evacuation drill (data + model
  benchmarking) — the underlying drill dataset.
- Cova et al. (2011) — evacuate vs. shelter-in-place optimisation, cited by Moradi et al.
- Zhou & Erdogan (2019) — wildfire resource allocation under spread scenarios.
