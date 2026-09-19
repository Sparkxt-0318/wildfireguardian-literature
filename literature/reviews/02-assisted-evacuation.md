# 02 — Supported / Assisted Wildfire Evacuation

**Category 2.** Agent A/B (Search Researcher + Prior-Art Adversary).
**Compiled:** 2026-09-19.
**Claims under adversarial test:** WG-C-003, WG-C-005, WG-C-011.
**Search log:** `docs/search-logs/agent-assisted-vulnerable.md`.

> **Reading instruction.** This review was written to *kill* WG-C-003, not to protect it.
> Where it concludes that a claim survives, that conclusion is `UNKNOWN`-grade at best
> (NOVELTY_STANDARD §3.2): no number of failed searches supports a claim.

---

## 1. Summary verdict up front

| Claim | Status entering | **Status after this review** | Killed by |
|---|---|---|---|
| WG-C-003 | UNKNOWN | **WEAKENED** (narrowed; see §5) | Moradi et al. 2026 (formulation) + Beyki et al. 2026 (inbound leg under modelled fire) + Yu et al. 2020 (inbound leg under hazard) |
| WG-C-005 | UNKNOWN | **OCCUPIED** | Moradi 2026; Flores 2023; Shahparvari lineage 2015–2019; Alexander 2026 |
| WG-C-011 | UNKNOWN | **OCCUPIED** | Moradi 2026 (fleet sizing); Shahparvari 2019 (required vehicle count); Xu 2022 (mobility-class/vehicle-class matching); Alexander 2026 |

---

## 2. Taxonomy of assisted-evacuation formulations

Six distinguishable formulation families were found. They are ordered by how close each gets to
the WildfireGuardian quantity.

### F1 — Bus-based / transit-based evacuation of carless populations
*Bish (2011); Zhao et al. (2020); Tang et al. (2025) [recorded by the transit/forecast agent].*

Capacitated buses shuttle repeatedly between a depot, pickup points where transit-dependent people
wait, and a shelter. Objective is total waiting time / exposure / evacuee time cost. **Hazard enters
only as an exogenous risk score or a given last-pickup time.** Bish's location-specific
risk-determined last-pickup deadline is the earliest instance found of *a time bound on a leg of an
assisted-evacuation mission*, and it predates WildfireGuardian by fifteen years.

### F2 — Bushfire "late evacuee" VRP with time windows
*Abbasi et al. (2015); Shahparvari et al. (2016, 2017 Omega, 2017 TR-A, 2019 TR-D).*

The wildfire-native lineage. Rescue vehicles collect residents who did not self-evacuate and deliver
them to shelters, under **hard time windows** and **road-disruption risk derived from bushfire
propagation scenarios**. Later variants add robust and possibilistic uncertainty over evacuee
population, travel time and window length. Outputs: required vehicle count, safest routes, schedules,
and a feasibility verdict. **The time window is always an input whose variation is studied, never an
output.**

### F3 — Supported evacuation with health-priority goal programming
*Flores et al. (2020, 2023).*

Introduces the term "supported evacuation" and the pick-up-point / safe-area–unsafe-area network.
Evacuees are classified by health condition and arrive dynamically at pickup points. Lexicographic
or goal-programming objectives trade off number evacuated, time, cost and unmet supply.
**No hazard-progression constraint on any leg.**

### F4 — Two-stage stochastic facility location + routing with fire-derived arc windows
*Moradi, Sauré & Patrick (2026) [PREPRINT]; Kamyabniya (2022) [citation-only lead].*

**The state of the art and the most dangerous family for WildfireGuardian.** First stage: shelter
location and fleet sizing. Second stage: split-pickup/split-delivery routing with vehicle-specific
loading dwell, no return-to-depot requirement, and **two time windows per arc** — a soft window
(partial disruption, +y% travel time) and a **hard window after which the fire reaches the arc and it
becomes unavailable**. Solved by Logic-Based Benders Decomposition. This family enforces fire-arrival
feasibility on **every leg, inbound included**, for exactly WildfireGuardian's population.

### F5 — Care-facility / patient evacuation VRP and staged evacuation
*Alexander et al. (2026) [conference]; Rambha et al. (2021); Kim/Kutanoglu/Hasenbein line [lead].*

Two sub-branches. The **routing** branch (Alexander) names the NH-Evac-VRP with multi-trip shuttling,
split pickups, load-dependent service times and an operational 300 s compute budget — this is the
pickup-dwell term as an established modelled component. The **timing** branch (Rambha) decides
*whether and in what order* to evacuate hospital patients as a hurricane forecast evolves, and reports
the value of recourse over new forecast information. Rambha et al. are the closest published work to
WildfireGuardian's *conceptual frame* found anywhere.

### F6 — Coupled fire-spread agent-based simulation with inbound rescue
*Beyki et al. (2026).*

A high-resolution fire model drives road-segment closures in real time inside an ABM that represents
pedestrians, private vehicles and **emergency extraction**, with waypoint-based adaptive rerouting for
**both outbound and inbound** legs. Validated against a real WUI evacuation drill in Portugal.
This is the only work found that couples a *modelled, progressing fire* to an *inbound responder leg*.

### Adjacent family — responder ingress under hazard, mission ends at arrival
*Yu et al. (2020), Nature Sustainability.*

Not an evacuation model: it models whether ambulance and fire-and-rescue units can still **reach**
care homes, sheltered accommodation and schools when the road network floods, measured against a
mandatory response-time standard. No pickup, no egress, no round trip — but it is published,
top-venue, national-scale proof that the inbound leg is hazard-dependent for exactly our sites.

---

## 3. Comparison table

Legend: `Y` yes · `N` no · `P` partial · `?` unverified / needs full text.

| Paper | Hazard | Who is assisted | Vehicle / fleet model | Hazard progression modelled? | Inbound leg modelled? | Output = route / schedule / deadline? | Time windows from hazard? |
|---|---|---|---|---|---|---|---|
| **Moradi et al. 2026** (PREPRINT) | Wildfire | Hospital patients, LTC residents, disabled, **people with no vehicles**, tourists | Heterogeneous (ambulance/bus/helicopter), fleet **size** is a decision, split pickup + split delivery, no return-to-depot | **P** — fire origin is a categorical scenario label; windows sampled Uniform(400,850) min; **no spread model run** | **Y** — arc hard window = "route ... is reached by the fire", binds on facility→assembly-area legs | **Route + schedule + fleet size + shelter set.** No deadline | **P** — asserted to come from fire origin/wind/vegetation, but operationally exogenous |
| **Beyki et al. 2026** | Wildfire | Residents requiring **emergency extraction** | Private vehicle + pedestrian + rescue agents; fleet size not a decision | **Y** — high-resolution fire model drives live road-segment closure | **Y** — explicit inbound rescue with adaptive rerouting | **Evacuation times + scenario analysis.** No deadline | **P/?** — route availability is fire-driven; whether a per-waypoint "safe time remaining" is reported needs full text |
| **Alexander et al. 2026** (conf.) | UXO exclusion zone; storm surge | Mobility-impaired nursing-home residents | Heterogeneous, multi-trip, split pickup, **load-dependent service time** | **N** — static hazard extent | **Y** — open-ended multi-trip shuttling | **Schedule.** Objective = waiting time + makespan | **N** — minute-level deadlines exogenous |
| **Rambha et al. 2021** | Hurricane (flood/wind/traffic forecasts) | Hospital patients | Transport assumed available; sequencing is the decision | **Y** — evolving predictions in a scenario tree with recourse | **P** | **Adaptive ordering policy over forecast stages.** Nearest thing to a timing output found | **N** — risk enters through the scenario tree, not as arc windows |
| **Shahparvari et al. 2019** | Bushfire | "Late evacuees" | Rescue vehicles; **required count is an output**; 4 shelters / 7 vehicles | **P** — propagation scenarios + route reliability scores | **Y** | **Routes + schedules + vehicle count + feasibility verdict** | **N** — windows are inputs, varied as what-ifs |
| **Shahparvari & Abbasi 2017** | Bushfire | Late evacuees | Robust stochastic fleet | **P** — bushfire propagation is an uncertain parameter | **Y** | Routes + schedules | **N** — windows are an uncertainty *distribution* |
| **Shahparvari et al. 2016** | Bushfire | Late evacuees | Multi-objective, resource-disruption sensitivity | **P** | **Y** | Tactical plan + feasibility under resource loss | **N** |
| **Abbasi et al. 2015** (conf.) | Bushfire | Late evacuees | VRP fleet | **P** — "fire propagation scenarios" | **Y** | Vehicles + schedules + routes | **N** |
| **Flores et al. 2023** | Wildfire (Saddleridge 2019) | Vulnerable people at pick-up points, health-priority classed | Heterogeneous, dynamic arrivals | **N** — static unsafe-area designation | **Y** | **Goal-programming plan**; time is an objective, not a bound | **N** |
| **Flores et al. 2020** | Earthquake/tsunami (Palu) | Vulnerable people, health-classed | Heterogeneous | **N** | **Y** | Lexicographic plan | **N** |
| **Xu et al. 2022** | Generic emergency | **Low-mobility individuals (e.g. elderly)** vs high-mobility | Heterogeneous incl. wheelchair-equipped vehicles + volunteers; **mobility-class↔vehicle-class matching constraints**; multi-parking-lot, split pickup | **N** | **Y** — origin ≠ destination by construction | Routes | **N** |
| **Bish 2011** | Generic regional | Transit-dependent / carless | Capacitated multi-trip buses | **N** | **Y** | Routes; objective = total exposure/waiting | **P** — **location-specific last-pickup time set by "risk considerations"**, exogenous |
| **Zhao et al. 2020** | Generic emergency | Evacuees at pickup points | **Round-trip** buses, unfixed routes, capacity + demand + time windows | **N** | **Y** | Schedule + routing; objective = total evacuee time cost | **N** |
| **Dubois et al. 2022** | Flash flood | Victims | Rescue-team vehicles, capacitated | **N** | **Y** | Routes **under given per-victim deadlines** | **N** — deadlines are exogenous constraints |
| **Chang (K.-H.) et al. 2024** | Earthquake MCI | Casualties at collection points | Ambulances, stochastic road vulnerability | **P** | **Y** | Dispatch + routing; objective = expected survivors | **N** |
| **Yu et al. 2020** | Flood | Care homes, sheltered accommodation, schools (**reached**, not moved) | All ambulance + fire-and-rescue stations in England | **Y** — flood extent/severity degrades network | **Y — this is the paper's subject** | **Coverage / compliance fraction vs a mandatory response-time standard** | **N** — standard is regulatory, not hazard-derived |
| **Borgwardt et al. 2024** (PREPRINT) | Wildfire | Nobody (population max-flow) | None | **Y** — plan built on a predicted fire, updated on revised fire info | **N** | Flow plan / routes | **P** — hazard shapefile constrains the time-expanded network |
| **WildfireGuardian (proposed)** | Wildfire, **modelled future fire** | Residents who cannot self-evacuate (**transport-access predicate**) | One responder unit; base→resident→pickup→destination | **Y (intended)** — ensemble / forecast with skill, lead time, latency | **Y** | **A latest fire-relative dispatch time, with sensitivity to forecast error, ingress congestion and pickup dwell** | **Y (intended)** — derived from the modelled fire |

---

## 4. 2025–2026 subsection

The field moved sharply into WildfireGuardian's territory in the last eighteen months. Every paper
below post-dates the point at which WG-C-003 was drafted.

| Paper | Date | Why it matters |
|---|---|---|
| **Moradi, Sauré & Patrick**, arXiv 2608.05413 | Preprint submitted to Elsevier **Aug 2025**; arXiv **Aug 2026** | The one that does the most damage. First two-stage stochastic supported-evacuation model for **wildfires** integrating capacitated facility location with multi-vehicle routing under hard time windows, including **arc windows defined by the fire reaching the route**. Occupies WG-C-005 and WG-C-011 outright and the constraint structure of WG-C-003. |
| **Beyki, Patricio, Lopes, Santiago & Laím**, *Safety Science* 199:107200 | **2026** | Names "the lack of inbound traffic and rescue operations" as the gap in prior work and then fills it, with a coupled high-resolution fire model and drill validation. If any 2025–2026 paper contains a latest-extraction-time result, this is the one — **full text must be obtained.** |
| **Alexander, Tannenbaum & Noennig**, GECCO '26, pp. 1029–1037 | **2026** | Defines and benchmarks the NH-Evac-VRP for mobility-impaired care-home residents, with load-dependent service times and an operational compute budget. Releases a public benchmark. |
| **Chang, Comfort, Soga, Li & Wang**, *Risk Analysis* | **2026** | Tri-coupled fire + communications + traffic; shows notification latency produces nonlinear congestion and unequal access to safe egress. Relevant to WG-C-012 and to WG-C-007 (a Korea-affiliated group already publishing here). |
| **Matsuo, Kietzman, Hays & Song**, *IJERPH* 22(11):1680 | **Nov 2025** | PRISMA-ScR scoping review of transportation barriers for vulnerable populations. The evidence base for WG-C-005's premise; see review 09. |
| **Tang, Wang & Delle Monache**, *TR-C* 180:105342 | **2025** | Equitable transit evacuation via RL. Recorded by another agent; overlaps Category 2/9 — check its output type before WG-C-011 is re-argued. |
| Preprint sweep (arXiv/alphaXiv) | 2025–2026 | arXiv 2502.07787 (shared autonomous vehicles for **rural vulnerable populations** — closest demographic match to the Korean setting, `NEEDS_FULL_TEXT`); arXiv 2410.14500 (time-expanded networks with integrated wildfire information); arXiv 2608.04225 (adaptive robust evacuation planning); arXiv 2603.29055 (Lahaina macroscopic traffic); arXiv 2412.05777 (equitable transit evacuation RL); arXiv 2402.06639 (Kincade social vulnerabilities). |

**Trend statement.** Between 2015 and 2023 the assisted-wildfire-evacuation literature was a VRP
literature with exogenous time windows. In 2025–2026 two things happened independently: the
optimisation side (Moradi) pushed the hazard into the **arc constraints**, and the simulation side
(Beyki) pushed the **inbound responder** into a fire-coupled model. WildfireGuardian's assumed gap
was closing while the claim was being drafted. Any re-audit after 90 days (NOVELTY_STANDARD §7)
should assume it has closed further.

---

## 5. Is the dispatch-by deadline occupied?

**This is the section WG-C-003 lives or dies in.**

### 5.1 What was searched

Across the log in `docs/search-logs/agent-assisted-vulnerable.md`: 20+ distinct queries, ≥15 wording
variants, five sources (Consensus / Semantic Scholar–PubMed–Scopus–arXiv; WebSearch; Crossref;
Semantic Scholar API; alphaXiv/arXiv), one non-English (Korean) pass, and a dedicated preprint sweep.

Wording variants attempted for the quantity itself:
`latest dispatch time` · `latest safe departure time` · `last feasible dispatch` ·
`latest possible departure` · `dispatch-by deadline` · `latest departure time` (time-dependent
network formulation) · `time-to-dispatch` · `latest time to begin evacuation` ·
`round trip ... deadline` · `deadline for emergency vehicle collecting a resident` ·
`responder ingress ... fire arrival constraint`.

Adjacent-field passes: hurricane transit and patient evacuation OR; flood rescue VRP; earthquake MCI
ambulance dispatch; wildland-firefighter escape-route and entrapment-trigger literature; dial-a-ride
and PDPTW; nursing-home hurricane evacuation decision timing; time-dependent shortest path
("latest departure" as a classical OR quantity).

### 5.2 What was found

**Five distinct things that are *not* the quantity, and matter anyway:**

1. **Hard arc time windows defined by fire arrival, binding on the inbound leg.**
   *Moradi et al. (2026), Model 2.* "the route connecting l to l' is reached by the fire and becomes
   completely unavailable." This is fire-arrival feasibility on every leg of a
   base→pickup→destination trip for residents who cannot self-evacuate. **The constraint structure
   WG-C-003 assumed was unclaimed is claimed.**

2. **Inbound rescue against a modelled, progressing fire.**
   *Beyki et al. (2026).* Fire-driven live road closure + explicit emergency-extraction agents +
   inbound adaptive rerouting, drill-validated.

3. **Inbound responder feasibility under a modelled hazard, aimed at vulnerable sites.**
   *Yu et al. (2020), Nature Sustainability.* National-scale, peer-reviewed, top venue. The mission
   ends at arrival — but "does the hazard make the inbound leg infeasible for care homes?" is answered.

4. **A location-specific, risk-determined deadline on an assisted-evacuation leg.**
   *Bish (2011).* On the *pickup* instant, exogenous. Fifteen years old.

5. **A timing decision for non-self-evacuating people under an evolving hazard forecast, with the
   value of adapting to new information as the reported result.**
   *Rambha et al. (2021).* Hurricane, hospital patients, scenario tree with recourse.

**What was NOT found, anywhere:**

- No paper reports **a latest departure/dispatch time as its output quantity** for a vehicle sent to
  collect a person who cannot self-evacuate.
- No paper enforces feasibility on **all three legs (ingress + pickup dwell + egress)** against a
  **modelled future fire** and reports the resulting **scalar time bound**.
- No paper reports the **sensitivity of such a deadline to forecast error, forecast lead time, or
  forecast latency**.
- The literal phrases "latest dispatch time" and "latest safe departure time" return **zero academic
  results** in the emergency-vehicle context — only public preparedness guidance and NFPA
  response-time standards.

### 5.3 **VERDICT**

> **WG-C-003 is `WEAKENED`, not `OCCUPIED` — and the surviving margin is narrow enough that it must
> be stated as a quantity claim, never as a problem claim.**

**What is occupied (and must be conceded on first contact with a judge):**
- The problem of assisted wildfire evacuation of non-self-evacuating residents — Moradi 2026,
  Flores 2023, Shahparvari 2015–2019. *(WG-C-005)*
- The base→resident→pickup→destination round-trip structure, with split pickup, pickup dwell, and no
  return-to-depot — Moradi 2026, Alexander 2026, Zhao 2020.
- **Fire-arrival hard constraints on the inbound leg** — Moradi 2026 (as a constraint),
  Beyki 2026 (as a simulated mechanism), Yu 2020 (as an empirical result for a different hazard).
- Scarce-fleet allocation among assisted evacuees — Moradi 2026, Shahparvari 2019, Xu 2022. *(WG-C-011)*
- Protective-action timing for non-self-evacuating people under an evolving hazard forecast —
  Rambha 2021.

**What survives, precisely:**
> No retrieved work computes and reports, as its output, *the latest fire-relative instant at which a
> responder may depart its base such that ingress, pickup dwell and egress all complete ahead of the
> modelled fire arrival on their respective legs* — nor the sensitivity of that instant to forecast
> skill, lead time and latency.

**Honesty warning, recorded in advance.** This surviving margin is close to the conjunction novelty
that NOVELTY_STANDARD §3.1 forbids. It is admissible **only** if WildfireGuardian can state *what
conclusion the deadline supports that a routing plan cannot*. The defensible version of that
argument is: a routing plan answers "is there a feasible plan given a departure time," which requires
the departure time as an input, whereas an incident commander at minute zero does not have one — the
deadline is the quantity that converts a feasibility check into a decision. **If WildfireGuardian
cannot demonstrate a case where the deadline and the plan give different operational answers, WG-C-003
should be abandoned in favour of a narrower N2 claim about the sensitivity surface.**

**What would move WG-C-003 to `OCCUPIED` (falsifiers, stated in advance):**
1. Beyki et al. (2026) full text reporting a latest-extraction or latest-dispatch time. *(most likely)*
2. Kamyabniya (2022) — the citation-only lead in Moradi et al. §2 — containing a dispatch-time output.
3. The Kim / Toplu-Tutay / Kutanoglu / Hasenbein integrated flood-prediction + patient-evacuation line
   reporting a latest-start time for facility evacuation.
4. Any follow-up to Moradi et al. that inverts the model to solve for the binding departure time.

---

## 6. Where the literature is thin (genuine gaps, stated without claiming them)

- **No wildfire paper runs a fire-spread model to produce the time windows it then optimises against.**
  Moradi asserts the link and samples the windows; Beyki simulates the fire but does not optimise.
  Nobody closes the loop.
- **No assisted-evacuation paper treats forecast latency.** Chang et al. (2026) treat *alert* latency
  for self-evacuees; nothing treats the delay between observation and the dispatcher's decision.
- **No tuned comparator.** Every optimisation paper benchmarks against its own heuristics
  (Moradi's CF/STWF/MCF) or against another metaheuristic (Alexander), never against a tuned
  positional-trigger policy. WG-C-006's rigour point is real — but it is N3-weak on its own.
- **Korea.** No peer-reviewed Korean assisted-evacuation modelling was retrieved. The Korean-language
  pass returned policy and news material only — MOIS's 2025 rapid-wildfire resident-evacuation policy
  revision, and a Yeongyang County scheme converting scheduled buses and taxis into evacuation
  vehicles for elderly and carless mountain-village residents. **That scheme is a real-world instance
  of WildfireGuardian's exact problem and should be treated as motivating evidence, not as literature.**

---

## 7. Papers needing full text before any claim is defended

| Paper | Why |
|---|---|
| **Beyki et al. 2026** (ScienceDirect 403; OA CC-BY, so obtainable) | Could move WG-C-003 to OCCUPIED single-handedly |
| **Kamyabniya (2022)** | Citation-only lead in Moradi §2; described as time-step two-stage stochastic supported evacuation with shelter location + routing |
| **Flores et al. 2023** | Abstract not retrieved from any source; current record is second-hand via Moradi §2 |
| **Kim, Toplu-Tutay, Kutanoglu & Hasenbein** (SSRN 4704899 + related) | Physics-based flood prediction coupled to multi-facility patient-evacuation logistics incl. EMS vehicle positioning |
| **Shahparvari et al. 2017 (Omega)** | No abstract retrieved from any source |
| **Zehra & Wong 2024 systematic review** | Its declared research gaps must be read before WildfireGuardian declares one |
| **arXiv 2502.07787** (SAV, rural, vulnerable) | Abstract mentions optimising routes *and timing*; author list not retrieved |
| **Ebrahimnejad, Villeneuve & Tavakkoli-Moghaddam (2021)**, *Scientia Iranica* | Disability evacuation optimisation; no abstract retrieved |

---

## 8. Recommended claim edits

1. **WG-C-005 → `OCCUPIED`.** Remove it as a contribution. It is a scope statement. Cite Moradi 2026
   and Flores 2023 when stating scope.
2. **WG-C-011 → `OCCUPIED`.** Fleet sizing (Moradi), required-vehicle count (Shahparvari),
   mobility-class↔vehicle-class matching (Xu) and priority allocation (Flores) between them cover it.
   If any allocation claim is retained it must be about *allocating by deadline slack*, which is a
   consequence of WG-C-003, not an independent claim.
3. **WG-C-003 → `WEAKENED`**, with the claim text narrowed to the quantity as stated in §5.3, and
   with `closest_prior_art: [moradi2026supported, beyki2026modular, yu2020disruption, rambha2021staged]`.
4. **Add a new one-sentence difference** to `fair/ONE_SENTENCE_DIFFERENCES.md`:
   *"Moradi et al. (2026) forbid a vehicle from using an arc after the fire reaches it and report the
   resulting routing plan and fleet size; we invert the same feasibility condition over departure time
   and report the latest instant at which the plan exists at all."*
