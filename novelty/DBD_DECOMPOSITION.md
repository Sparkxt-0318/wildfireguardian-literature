# DBD_DECOMPOSITION.md — the dispatch-by claim, split into seven scorable components

**Author:** Agent B — Prior-Art Adversary
**Date:** 2026-09-20
**Mandate:** `NOVELTY_STANDARD.md` §9 (decompose before scoring), §8 (four axes), §10
(full-text tier gates confidence).
**Stance:** adversarial. Each component was scored by looking for the paper that takes it,
not the paper that leaves it free.

> **Two papers are deliberately not scored here.** `beyki2026modular` and
> `moradi2026supported` were being read in full by other agents while this document was
> written. Every score below is computed **with those two excluded**. Both are CRITICAL
> threats; when their full-text reads land, components 1, 2, 4 and 5 must be re-scored
> against them. **No score in this file may be quoted as a whole-corpus verdict until that
> is done.**

> **Standing rule for this file.** "No occupying prior art was identified in the searched
> corpus" is the only permitted way to record an empty result. It is not a novelty finding
> (`NOVELTY_STANDARD.md` §3.2). Nowhere in this file does zero occupants mean novel.

---

## 0. Headline table

| ID | Component | Score | Closest occupant (Beyki/Moradi excluded) |
|---|---|---|---|
| WG-DBD-1 | Complete assisted mission = responder ingress + service + egress | **OCCUPIED** | `zhao2020roundtrip`; `bish2011planning`; `shahparvari2017robust`; `alexander2026nursing`; `xu2022multiparking`; `chang2024stochastic`; `flores2023goal` |
| WG-DBD-2 | Fire-relative feasible dispatch times are computed | **OCCUPIED** | `mitchell2023peril` / `cova2005trigger` (computed, egress subject); `shahparvari2017robust` / `abbasi2015vehicle` (responder subject, windows as inputs) |
| WG-DBD-3 | Latest feasible dispatch instant reported as an operational quantity | **OCCUPIED** | `kamphuis2025departure` (peer-reviewed, exact quantity); `fluschnik2026decaying` (preprint, fire-motivated evacuation) |
| WG-DBD-4 | Non-monotone feasible dispatch windows as a **SET**, not one deadline | **OCCUPIED (as representation; robotics)** | `phillips2011sipp`; `kemisetti2026stochsipp` |
| WG-DBD-5 | Hazard evaluated over the **whole traversal**, not only at arc entry | **OCCUPIED (as method; robotics + graph algorithms)** | `kemisetti2026stochsipp`; `phillips2011sipp`; `fluschnik2026decaying`; in wildfire, `ma2025damaged` (NEEDS_FULL_TEXT) |
| WG-DBD-6 | Feasibility conditioned on information available at decision time, not oracle future | **OCCUPIED** | `rambha2021staged`; `kemisetti2026stochsipp`; `kamphuis2025departure` (online variant); `larsen2011cedar` |
| WG-DBD-7 | Dispatch-by maps applied to Korean rural wildfire geometry | **WEAKENED** | `kim2011evacmap`; `kwak2021evacroute`; `kwon2025koreaevac`; `mois2025evacuationstages` (GOVERNMENT_REPORT) |

**The finding that should change the program's plan:** WG-DBD-4 and WG-DBD-5 — the two
components the brief expected to be the most technically distinctive — are the two that
adjacent fields occupy most cleanly, and have occupied since **2011**. They are robotics and
graph-algorithms method, not fire science, which is exactly why they survived nine previous
category reviews unexamined.

---

## WG-DBD-1 — Complete assisted mission contains responder ingress + service + egress

**Score: OCCUPIED.**

**Occupants.** `zhao2020roundtrip` owns the phrase and the structure: depot → pickup point →
shelter and back, with capacity, demand and time-window constraints. `bish2011planning` is
the canonical carless-population formulation and already carries a per-location,
risk-determined last-pickup time. `shahparvari2017robust` (and the Abbasi/Shahparvari
2015–2019 lineage) sends capacitated vehicles in to collect late bushfire evacuees and out to
shelters under hard time windows. `alexander2026nursing` adds load-dependent **service**
times as a modelled component. `xu2022multiparking` adds mobility-class to vehicle-class
matching. `chang2024stochastic` does it for ambulances on a vulnerable road network.
`flores2023goal` does it with health-priority classes on a wildfire case.

**Evidence.** Corpus records with `matrix.inbound_responder`, `matrix.pickup` and
`matrix.egress` all true or partial: seventeen records, listed above less the two excluded.

**What is NOT occupied by these.** None of them reports a dispatch instant, and in all of them
the hazard enters as an exogenous window or risk score rather than as a modelled arrival-time
field. That is a statement about components 2, 3 and 5, not about component 1.

**Axes** (`NOVELTY_STANDARD.md` §8): concept OCCUPIED · method OCCUPIED · empirical OCCUPIED ·
operational_artifact OCCUPIED.

**Coverage.** Search: category 2/3 reviews at tier S2 (37 logged queries, 5 sources) plus this
agent's corpus re-read. Full text: all seven occupants at `ABSTRACT_VERIFIED` or below except
where the category-2 review states otherwise; **no occupant read at `METHODS_VERIFIED`**.
Unsearched: TRB Annual Meeting proceedings, INFORMS conference papers, national civil-defence
technical series. Language: English only for this component. Date cutoff: 2026-09-20.
**Confidence: HIGH** that it is occupied (occupancy needs one paper, and there are seven).

---

## WG-DBD-2 — Fire-relative feasible dispatch times are computed

**Score: OCCUPIED**, with a subject split that must be stated whenever it is cited.

**Occupants, split by who is dispatched.**

*Subject = household / community (the quantity is computed from a fire model).*
`cova2005trigger` computes a level set of modelled fire travel time equal to an evacuation
time — a fire-relative latest-action locus, by construction. `mitchell2023peril` states it as
arithmetic: trigger = fire-spread time − evacuation time, plus a safety factor.
`li2015household` computes it **per household** and ranks households by remaining lead time.
`kalogeropoulos2025dire` computes "the latest wildfire location with a low risk of a dire
evacuation" with both fire and evacuation time probabilistic.

*Subject = dispatched vehicle (the window is fire-derived but supplied, not computed).*
`shahparvari2017robust` and `abbasi2015vehicle` take hard time windows and route-disruption
risk **derived from bushfire propagation scenarios**; per `literature/reviews/02` the window
"is always an input whose variation is studied, never an output."

**Reading.** The *computation* of a fire-relative latest-action time is twenty-one years old;
what the responder lineage does is consume such times rather than produce them. This is a
narrower residue than the claim register currently implies, and it is not a residue that can
carry a contribution by itself.

**Axes.** concept OCCUPIED · method OCCUPIED · empirical WEAKENED (no published fire-relative
window computed *for a responder mission* outside the two excluded papers) · artifact WEAKENED.

**Coverage.** Search: category 1 at S1→S2 (backward refs of `cova2005trigger` never traversed,
publisher 403); category 2 at S2. Full text: `mitchell2023peril`, `cova2005trigger`,
`li2015household` at `ABSTRACT_VERIFIED`; the Shahparvari lineage partly `TITLE_ONLY`
(`shahparvari2017possibilistic`, `shahparvari2019fleet` both flagged NEEDS_FULL_TEXT).
Unsearched: Australian AFAC/Bushfire CRC technical reports; Greek, Portuguese and Spanish
national literatures. Date cutoff: 2026-09-20. **Confidence: HIGH** on occupancy for the
egress subject; **MODERATE** on the responder subject, because the two most dangerous papers
are excluded here and two lineage members are title-only.

---

## WG-DBD-3 — Latest feasible dispatch instant reported as an operational quantity

**Score: OCCUPIED.** This is the component the program believed was its one open column.
It is not open outside wildfire, and it is not open in the graph-algorithms treatment of
wildfire evacuation.

**Occupant 1 — peer-reviewed, exact quantity, probability-indexed.**
`kamphuis2025departure` — Kamphuis, Levering & Mandjes, *Computers & Operations Research*
183:107148 (2025), preprint arXiv:2208.14516. Verbatim from the abstract:

> "The focus of this paper lies on determining their optimal departure time: **the latest time
> of departure for which a chosen on-time arrival probability can be guaranteed.**"

A latest departure instant, indexed by a completion probability, computed on a stochastic
time-dependent road network, reported as *the* output. The differences from WildfireGuardian
are mission structure and hazard model, not the quantity: one-way trip, no second leg, no
service dwell, a Markovian incident process on link speeds rather than a spreading fire.

**Occupant 2 — preprint, and in our own hazard family.**
`fluschnik2026decaying` — "Smooth Routing in Decaying Trees", arXiv:2603.23504 [cs.DS].
Verbatim: "Motivated by evacuation scenarios arising in extreme events such as flooding or
forest fires… **We provide an integer linear program (ILP) to compute the latest possible time
to evacuate.**" Edges "become impassable at some point in time". Outbound paths only; decay
times exogenous; no responder; a single latest time rather than a set.

**Wildfire-internal near-occupant.** `kalogeropoulos2025dire` reports the latest *fire
location* with low risk of a dire evacuation, and an evacuation safety factor in [0,1] — the
same decision content in spatial units.

**What remains after this.** Not "we compute a latest time and others compute routes." What
remains is narrower and must be said in these words or not at all: *a latest departure instant
for a **two-leg mission with a dwell**, whose feasibility is governed by a **modelled fire
arrival-time field with quantified forecast error**, reported for a named resident.* Every
italicised element is doing work; drop one and an occupant above swallows the sentence.

**Axes.** concept OCCUPIED · method OCCUPIED · empirical PLAUSIBLE (no published latest-dispatch
instant for a wildfire assisted-evacuation round trip was identified in the searched corpus) ·
operational_artifact PLAUSIBLE.

**Coverage.** Search: this agent ran OpenAlex title/abstract and full-text passes, arXiv via
alphaXiv, Crossref and WebSearch on "latest departure time", "latest dispatch time", "departure
time advice", "time-restricted shortest path", "latest possible time to evacuate". Consensus
was unavailable (monthly quota exhausted) and Semantic Scholar returned HTTP 429 — **two
databases the protocol expects were not queried for this component.** Full text:
`kamphuis2025departure` `ABSTRACT_VERIFIED` (journal text not retrieved, published abstract not
compared with the preprint); `fluschnik2026decaying` `ABSTRACT_VERIFIED` and carrying an
unresolved arXiv-identifier/date discrepancy. Unsearched: Transportation Science, TR-B and
EJOR full runs; air-traffic-management literature beyond one hit (Sherali & Hill 2009,
"Reverse time-restricted shortest paths", *TR-C* 17(6):631–641, abstract **not** retrieved —
title alone suggests a latest-departure formulation and it is an open lead). Language: English
only. Date cutoff: 2026-09-20. **Confidence: HIGH** on occupancy of the quantity; **MODERATE**
on the exact residue wording, because the ATM lead is unread.

---

## WG-DBD-4 — Non-monotone feasible dispatch windows represented as a SET

**Score: OCCUPIED as a representation, in robotics, since 2011.** This is the component the
brief expected to be most distinctive, and it is the one with the cleanest occupant.

**Occupant.** `phillips2011sipp` — Phillips & Likhachev, ICRA 2011, pp. 5628–5635. Read at
`METHODS_VERIFIED` from the author-hosted PDF. Verbatim:

> "We define a safe interval as a contiguous period of time for a configuration, during which
> there is no collision and it is in collision one timestep prior and one timestep after the
> period."

> "Each spatial configuration … has a timeline …, which is just an ordered list of intervals,
> **alternating between safe and collision**."

An alternating timeline is a non-monotone feasible set by construction: blocked, then free,
then blocked again is the ordinary case in SIPP, not a special case. The number of safe
intervals at a configuration is bounded by the number of obstacle trajectories through it.

**Occupant 2, with uncertainty.** `kemisetti2026stochsipp` (arXiv:2608.00792, PREPRINT)
attaches a **set of valid times** `D_z` to every roadmap vertex *and edge*, with per-interval
Bernoulli safety probabilities, and notes that edges too long to fit are dropped "so every edge
has at least one valid departure time."

**Therefore the following sentences are now forbidden:** "representing dispatch feasibility as
a set of intervals rather than a single deadline is new"; "no one has noticed that feasibility
under a moving hazard can be non-monotone in departure time." Both are false against ICRA 2011.

**What is still not occupied.** SIPP and StochSIPP compute **earliest arrival**, never a latest
departure, and their intervals are per-configuration occupancy windows, not *mission-completion*
windows for a round trip. No retrieved work reports, as a decision product, the set of departure
instants at which a two-leg assisted-evacuation mission still closes. That is a real distinction
and it is also a thin one: it is a use of an existing representation, i.e. N4-with-N2-flavour,
not N3.

**Axes.** concept WEAKENED · **method OCCUPIED** · empirical PLAUSIBLE · operational_artifact
PLAUSIBLE.

**Coverage.** Search: dedicated per the brief. Vocabulary variants run — "safe interval path
planning", "SIPP", "forbidden intervals shortest path", "time-dependent shortest path", "non-FIFO
arc", "latest departure time network", "departure time reachability deadline", "moving firefighter
problem", "escaping spreading fire graph", "backward reachable set latest start", "reach-avoid
moving obstacle". Sources: OpenAlex (title/abstract and full-text indexes), alphaXiv/arXiv,
Crossref, WebSearch. Adjacent fields covered: robotics/MAPF, graph algorithms/temporal graphs,
time-dependent routing/OR. Full text: SIPP `METHODS_VERIFIED`; StochSIPP `METHODS_VERIFIED` for
its problem-setup section. **Not searched:** ICAPS/SoCS/AAMAS proceedings systematically (only
what OpenAlex and alphaXiv surfaced); Hamilton–Jacobi reachability literature returned nothing on
the queries used and was **not** pursued properly — a backward reachable tube is the same object
in continuous state space and this is an open lead. Language: English only. Date cutoff:
2026-09-20. **Confidence: HIGH** that the representation is occupied; **MODERATE** that no one has
reported a mission-completion departure *set*, because the systematic planning-conference sweep
was not done.

---

## WG-DBD-5 — Full traversal-interval hazard, not a check at arc entry

**Score: OCCUPIED as a method, in robotics and graph algorithms.**

**Occupant 1 — the definition, stated as a definition.** `kemisetti2026stochsipp`, verbatim:

> "A vertex safety event at time t states whether the robot may occupy q at t; **an edge safety
> event at departure time t states whether the complete execution of e over [t, t + W(e)) is
> collision-free.** The event for a wait self-loop therefore covers the complete unit-time
> occupancy, not only its endpoints."

That last clause is WG-DBD-5 written out, including the failure mode it guards against.

**Occupant 2.** `phillips2011sipp`: successors are generated "with the earliest possible arrival
time that does not have any collisions **along the motion**".

**Occupant 3, in our hazard family.** `fluschnik2026decaying`: paths must clear edges before
those connections "become impassable", i.e. the constraint binds over the traversal.

**Nearest wildfire occupant.** `ma2025damaged` couples wildfire simulation to road-network
vulnerability so that fire-induced closures degrade the network *during* the run and agents on a
link "may be trapped". Its record is explicitly `NEEDS_FULL_TEXT` (E2/E3, publisher-page summary
only). If its full text checks fire arrival against the *interval* an agent occupies a link, then
WG-DBD-5 is occupied inside wildfire too and not merely by analogy. **This is now a priority read.**

**Axes.** concept WEAKENED · **method OCCUPIED** · empirical PLAUSIBLE (for a responder's inbound
leg under a modelled wildfire, outside the two excluded papers) · operational_artifact UNKNOWN.

**Coverage.** Same sweep as WG-DBD-4. Additional wildfire-specific queries: road-segment burn-over
during traversal; fire-arrival feasibility on links; "RESCUE" (Tammali et al., ICDCN 2026,
10.1145/3772290.3772301 — an edge-fire-risk function from rate-of-spread for evacuee routing;
examined and **deliberately not recorded**, because it occupies no component here). Full text:
StochSIPP and SIPP at `METHODS_VERIFIED`; `fluschnik2026decaying` and `ma2025damaged` at
`ABSTRACT_VERIFIED` or below. Unsearched: the truck-driver-routing literature on driving bans,
where "you may not be *on* the arc during the ban" is standard and almost certainly predates all
of the above; ICAPS/SoCS systematically. Language: English only. Date cutoff: 2026-09-20.
**Confidence: HIGH** on method occupancy; **LOW-to-MODERATE** on the claim that wildfire
application is open, because the closest wildfire paper is unread and two more are excluded.

---

## WG-DBD-6 — Feasibility conditioned on information available at decision time

**Score: OCCUPIED.**

**Occupants.** `rambha2021staged` decides whether and in what order to move hospital patients *as
a hurricane forecast evolves*, over a scenario tree, and reports the value of recourse on new
forecast information — non-anticipativity is the formulation's spine. `kemisetti2026stochsipp` is
an explicitly *contingent* planner: statuses are "revealed locally during execution" and the
policy "anticipates future local observations". `kamphuis2025departure`'s online variant exists
precisely because "the conditions in the road network … may change between the time of request and
the advised time of departure", and revises advice while the traveller is still at the origin.
`larsen2011cedar` makes trigger buffers from the forecast winds actually available at the time.
More broadly, two-stage stochastic programming with recourse *is* this component, and the
supported-evacuation lineage is built on it.

**What is not occupied.** No retrieved work contrasts a decision-time-information dispatch policy
against an **oracle** dispatch policy in wildfire, and reports the gap as the result. That
contrast — the regret of not knowing the fire's future — is a legitimate open residue, but it is a
*measurement*, not a formulation, and it sits on top of WG-C-002/WG-C-012, both already WEAKENED.

**Axes.** concept OCCUPIED · method OCCUPIED · empirical PLAUSIBLE · operational_artifact UNKNOWN.

**Coverage.** Search: inherited from categories 2 and 4 at tier S2, plus this agent's robotics and
OR passes. Full text: `rambha2021staged` `ABSTRACT_VERIFIED`. Unsearched: the online/competitive-
analysis literature on the Canadian Traveller Problem, which `kemisetti2026stochsipp` names as its
generalised ancestor and which is the natural home of "how much worse is a non-clairvoyant
policy" — **this is an unclosed adjacent field, and it is the field most likely to already contain
the oracle-gap result.** Language: English only. Date cutoff: 2026-09-20. **Confidence: HIGH** on
occupancy; **LOW** on the residue, because the CTP literature was identified and not searched.

---

## WG-DBD-7 — Dispatch-by maps applied to Korean rural wildfire geometry

**Score: WEAKENED.** Full reasoning and the five empirical sub-questions are in
`novelty/KOREAN_EMPIRICAL_AUDIT.md`; the summary is here.

**What is occupied in Korea.**
- **The wildfire evacuation map as a Korean product, at village scale, motivated by vulnerable
  residents, driven by modelled spread — since 2011.** `kim2011evacmap` (김명훈, 이병두, 김응식,
  「산불대피지도 작성 알고리즘에 관한 연구」, 한국화재소방학회 학술대회 논문집 2011.11a, 289–293,
  **conference proceedings, not a journal article**). Its own abstract says the work exists because
  「대부분의 대피 대상자들이 재해 약자들로 구성되어있어」 *[translation]* "most of those to be
  evacuated consist of disaster-vulnerable people". It emits routes, not times.
- Route-level Korean wildfire evacuation planning: `kwak2021evacroute` (2021).
- Rural Korean county wildfire evacuation system design: `kwon2025koreaevac` (2025).
- **A fire-relative act-by rule, operational and nationwide:** `mois2025evacuationstages`
  (GOVERNMENT_REPORT, in force since April 2025) partitions space by predicted fire-line arrival
  into ≤5 h and ≤8 h zones, with vulnerable residents moved on the 8 h boundary. That is already a
  fire-relative act-by *map* over Korean geometry, at zone resolution, with a differential for
  people who move slowly.

**What is not occupied.** No Korean **dispatch-by** quantity — nothing addressed to a responder's
departure — and nothing at household or village resolution with an uncertainty treatment, was
identified in the searched corpus.

**Consequence.** Under `NOVELTY_STANDARD.md` §4 this cannot be carried as geography. It is
admissible only as §4(c) — Korea is where an N2 quantity was computed — or via a §4(b) documented
failure of an imported method on Korean data. The registry's existing WEAKENED status for
WG-C-007 is correct and this component does not improve it.

**Axes.** concept OCCUPIED · method OCCUPIED · **empirical PLAUSIBLE** · **operational_artifact
PLAUSIBLE** (a household-resolution Korean dispatch-by atlas is a distinct artifact from anything
retrieved).

**Coverage.** See the access-failure table in `docs/search-logs/agent-dbd-korea.md`. Korean-language
routes that **worked**: KoreaScience keyword search and article pages, KCI article pages by
`artiId`, ScienceON report pages by `cn`, and an OpenAlex `language:ko` sweep of all 406 Korean
records matching 산불. Routes that **failed**: DBpia (HTTP 503, again), KCI server-side keyword
search (the query parameter is ignored and the unfiltered 2.4 M-record corpus is returned),
ScienceON site search endpoint (404), RISS (not reached), koreascience.kr over `curl` (proxy 502 —
it works through WebFetch). Full text: `kim2011evacmap` `ABSTRACT_VERIFIED` only. Date cutoff:
2026-09-20. **Confidence: MODERATE.** The OpenAlex Korean sweep is the first systematic
Korean-language pass in this repository, but OpenAlex indexes Korean conference proceedings
unevenly and RISS/DBpia remain unsearched.

---

## 1. What this decomposition does to WG-C-003

The claim register records WG-C-003 as `SUPPORTED_CANDIDATE` on the strength of one open column:
"latest dispatch time reported as the output, from a modelled future fire, as a function of
forecast error."

Against this decomposition, **that column is not open as stated**. `kamphuis2025departure`
publishes the latest-departure-instant-under-probability quantity, `fluschnik2026decaying`
publishes a latest-possible-evacuation-time for a fire-motivated decaying graph, and
`phillips2011sipp`/`kemisetti2026stochsipp` publish the interval-set representation and the
traversal-interval hazard test. What survives is the **conjunction**, and
`NOVELTY_STANDARD.md` §3.1 forbids claiming a conjunction unless we say what the joint treatment
changes.

**Recommended registry action (for whoever holds `docs/CLAIM_REGISTRY.md` — not applied by this
agent):** move WG-C-003 from `SUPPORTED_CANDIDATE` to `WEAKENED`, with `method: OCCUPIED` and
`empirical: PLAUSIBLE` under §8, and rewrite the claim as an empirical/artifact claim:

> For a named non-self-evacuating resident under a modelled Korean wildfire with quantified
> forecast error, we report the set of responder departure instants at which the full
> ingress–dwell–egress mission still closes, and we show a case where that set and a routing
> plan give different operational answers.

The §3.1 answer this claim owes — what does joint treatment change? — is the sentence after
"and we show". If that demonstration fails, the claim has nothing left.

---

## 2. Re-scoring triggers

Re-open this file when any of these lands:
1. `beyki2026modular` full text (components 1, 2, 5).
2. `moradi2026supported` full text or journal version (components 1, 2, 4, 5).
3. `ma2025damaged` full text (component 5, wildfire application).
4. `kamyabniya2022thesis` (component 4 — `OPEN_QUESTIONS.md` A2 already predicts a time-step
   feasibility indicator, i.e. a dispatch-feasible set).
5. Sherali & Hill (2009) *TR-C* 17(6):631–641 abstract (component 3).
6. Any ICAPS/SoCS/AAMAS or Canadian-Traveller-Problem sweep (components 4, 5, 6).
