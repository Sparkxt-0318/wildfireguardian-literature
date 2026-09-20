# beyki2026modular

## Citation
Beyki, S. M., Patricio, A. S., Gameiro Lopes, A., Santiago, A., & Laím, L. (2026). "A modular
agent-based framework for wildfire evacuation: Integrating fire spread, multimodal transport, and
dynamic routing." *Safety Science*, **199**, 107200. DOI: 10.1016/j.ssci.2026.107200.

**DOI verified** in Crossref, Unpaywall and Elsevier's own Article-Retrieval API. Not invented.

## Publication status
`PEER_REVIEWED`, journal article. **Open access, CC-BY 4.0** — confirmed from Elsevier's API
(`openaccessType: Full`, `openaccessUserLicense: creativecommons.org/licenses/by/4.0/`, sponsor
"Portugal institutions: Core Hybrid journals RAP 2025"). Online 2026-03-21; issue cover date July
2026. 43 references.

**FULL TEXT STILL NOT RETRIEVED.** Evidence level **E2**. Status `NEEDS_FULL_TEXT`.

A second, much more determined retrieval attempt was made on 2026-09-20 (Agent C) across 25
distinct access routes. It failed. The paper is genuinely CC-BY, but **ScienceDirect is its only
host and it denies this network at the IP level** (HTTP 403, Elsevier reference `CPE00001`),
including to a real headless Chromium. No repository copy exists anywhere (Unpaywall
`has_repository_copy: false`; OpenAIRE, CORE, BASE, Europe PMC, Coimbra "Estudo Geral" all
negative). Full log: `literature/reviews/fulltext-beyki2026.md` §0.

## Author correction (2026-09-20)
Four of the five authors are University of Coimbra (Mechanical Engineering: Beyki, Gameiro Lopes;
Civil Engineering: Santiago, Laím). **The second author, Anne S. Patricio, is at MaaSLab,
Limassol, Cyprus** — a mobility-as-a-service transport lab, not Coimbra. This explains the
multimodal-transport component and means a Coimbra-repository-only search was never sufficient.

## Problem
Wildfire evacuation in the WUI. The authors name four gaps in existing models: limited dynamic
rerouting when roads are compromised; insufficient representation of multimodal evacuation; weak
integration of high-resolution fire-spread data; and — the one that matters here — **"the lack of
inbound traffic and rescue operations."**

## Method
*(Abstract-level only. E2 may not support method-detail statements — `docs/EVIDENCE_LEVELS.md`.)*

Modular agent-based framework combining fire spread, pedestrian movement and vehicle traffic in one
model. Fire-driven road-segment closures dynamically update network availability during the run. A
custom waypoint-based routing algorithm enables adaptive rerouting for outbound **and inbound**
evacuation. Agent classes stated as explicitly represented: pedestrian movement, private vehicle,
**emergency extraction**, and vehicle–pedestrian interaction.

**Nothing is known about the algorithms themselves**: no objective function, no closure rule, no
information-gating on the router, no equations. See "What remains unread" below.

## Data
WUI case study in Portugal. Publicly available datasets throughout (stated design goal for
transferability).

## Outputs
As stated in the abstract: evacuation times; route availability under advancing fire; scenario /
"what-if" analyses. **No deadline or dispatch-time quantity appears anywhere in the retrievable
record.**

## Key equations
`NEEDS_FULL_TEXT`.

## Assumptions
`NEEDS_FULL_TEXT`.

## Validation
Validated against a real evacuation drill, "showing strong agreement in evacuation times." Stronger
empirical grounding than most of the assisted-evacuation optimisation literature.

## Limitations
`NEEDS_FULL_TEXT`. Standing observation: a validated *simulation* of inbound rescue is not the same
as an optimisation that solves for the latest feasible dispatch. Whether the framework is or can be
run backwards to produce a deadline is exactly the open question.

## Reference list — retrieved in full (43 items, Crossref, publisher-deposited)
This is the only body-adjacent evidence held at primary-source quality.

**Cites the trigger literature:** Cova (2002), Cova (2013), Dennison (2007, WUIVAC), Li (2019,
`li2018coupling`), Mitchell (2023, PERIL).
**Cites the simulation platforms:** Ronchi (2019, e-Sanctuary), Wahlqvist (2021, WUI-NITY),
Veeraswamy (2018), Siam (2022), Grajdura (2022), Gwynne (2019), Beloglazov (2016), Intini (2019),
Wolshon (2007).
**Cites the authors' own fire lineage:** Lopes (1995), Lopes (2002, FireStation), Ross (1988),
Rothermel (1972), Beyki (2023 / 2025 / 2025).

**Absent from all 43:** any vehicle-routing, pickup-and-delivery, PDPTW, fleet-sizing,
dispatch-optimisation or scheduling reference (no Shahparvari, no Moradi, no Kamyabniya); any
forecast-value / ensemble / uncertainty reference; any title containing "deadline", "time window",
"dispatch" or "departure time".

**Weight:** inferential only. A paper reporting a dispatch deadline would be expected to situate
itself against the routing-and-scheduling literature, and does not. But absence of a citation is
not absence of a mechanism, and arguing from it is the shape `NOVELTY_STANDARD.md` §3.2 forbids.
**It may not be used to move any claim.** It is a prior on what the full text will say.

## ⚠ Retracted from this note: the "safe time remaining" quote
The previous version of this note carried a tentatively-attributed mechanism — "determining safe
time remaining for evacuation routes based on fire arrival time for each waypoint on the route,
where the safe time remaining is the least of the fire arrival times."

**I tried to trace it to a primary source and could not.** It is not in the publisher-deposited
abstract or highlights, and not in any retrievable record (Crossref, Unpaywall, OpenAlex, Semantic
Scholar, Elsevier `coredata`). A fresh WebSearch reproduced the same description — but that is a
second helping of the same class of source, not a second source.

**Status: `RECALL_UNVERIFIED` / unsourced. Do not cite, quote, or describe as something the paper
says.** Logged for follow-up per `AGENTS.md` §3.

It is still the most valuable thing to check first on the next retrieval, because if true:
- it would be a fire-relative feasibility **margin per route** (bears on WG-DBD-2);
- it would be a `min`-over-waypoints rule, i.e. a **single scalar deadline per route** — the
  monotone single-deadline structure WG-DBD-4 is defined *against*, so it would **strengthen** that
  differentiation, not occupy it;
- it would **not** be a dispatch instant for an inbound responder (WG-DBD-3 untouched).

## WildfireGuardian overlap
Still the only work found that couples a modelled, progressing fire to an explicit inbound
responder leg:
- fire-spread model coupled to network availability, updating during the run;
- inbound rescue operations and emergency extraction as first-class agent behaviours;
- adaptive rerouting for inbound legs when roads are compromised by fire;
- drill validation in a real WUI community.

Where `moradi2026supported` owns the *optimisation formulation* of the assisted round trip with
fire-arrival windows, Beyki et al. own the *simulation of the inbound leg against a modelled fire*.

## WildfireGuardian difference
**Every item below remains unverified against the body and must not be spoken to a judge as fact.**

- **Direction of the computation.** Beyki et al. appear to simulate forward: given a dispatch, what
  happens? WildfireGuardian proposes to solve backward: given that the mission must close, how late
  may dispatch be? A simulator that answers "did this rescue succeed" does not by itself report the
  latest departure time; that needs a search or root-find over dispatch time.
- **Decision subject.** Their reported outputs are community-level evacuation times and operational
  consistency; ours is a per-resident, per-responder time-to-dispatch.
- **Uncertainty.** No ensemble, forecast error, skill or latency treatment appears anywhere in the
  retrievable record — and none of the 43 references is a forecast-uncertainty paper.

## Novelty threat
**level: CRITICAL** — unchanged, and explicitly *not* downgraded for being unread. Threat level
measures overlap; evidence level measures our knowledge. A CRITICAL threat known only at E2 is,
per `docs/EVIDENCE_LEVELS.md`, the most urgent item in the repository.

- **WG-C-003** → threatens the inbound-leg component directly. Stays `SUPPORTED_CANDIDATE`; this
  audit produced no evidence permitting a move in either direction.
- **WG-C-005** → contributes to `OCCUPIED`.
- Also relevant to WG-C-001 (already `REJECTED`).

---

## Full-text verification 2026-09-20

**Agent C — Verification Auditor. Outcome: RETRIEVAL FAILED.**

| Field | Value |
|---|---|
| `fulltext_status` | **`ABSTRACT_VERIFIED`** |
| `evidence_level` | **E2** (content) / E4-equivalent (bibliographic metadata only) |
| `access_route` | Publisher-deposited metadata via Crossref, Unpaywall, OpenAlex and Elsevier Article-Retrieval API (`coredata` view, no key). **Body: no route succeeded.** |
| Blocking cause | Elsevier IP-level denial (`CPE00001`) on ScienceDirect *and* SSRN; `web.archive.org` blocked by this session's egress policy and not routed around |
| Routes attempted | 25, itemised in `literature/reviews/fulltext-beyki2026.md` §0 |

**No page or section numbers appear below, because no paginated text was ever read.** Any
page-numbered citation to this paper appearing anywhere in the repository would be fabricated.

### Q-B1 … Q-B6

The permitted vocabulary was YES / NO / NOT_ADDRESSED_IN_TEXT. **None of the three is available**:
"NOT_ADDRESSED_IN_TEXT" is itself an assertion about the text. `AGENTS.md` §9 requires `UNKNOWN`
here.

| ID | Question | Answer | Basis |
|---|---|---|---|
| **Q-B1** | Latest feasible start time for an inbound responder's complete extraction mission? | **`NOT_DETERMINED — NO FULL TEXT`** | Not among the abstract's listed outputs; no scheduling refs in 43. Neither is textual evidence about the body. |
| **Q-B2** | `base → resident → pickup → destination` as ONE fire-relative mission? | **`NOT_DETERMINED — NO FULL TEXT`** | Abstract asserts inbound rescue and an "emergency extraction" agent class exist; whether one mission is chained end-to-end with a dwell is a method detail E2 cannot support. |
| **Q-B3** | Dispatch-feasible set/window or equivalent? | **`NOT_DETERMINED — NO FULL TEXT`** | Nothing at E2. The retracted "safe time remaining" lead would bear on this if ever verified. |
| **Q-B4** | Hazard over the full traversal interval, or only at edge-decision times? | **`NOT_DETERMINED — NO FULL TEXT`** | "Fire-driven road-segment closures dynamically update network availability" establishes the *network* is time-varying; it does **not** establish whether an agent already on an edge is re-checked mid-traversal. That distinction is the question. |
| **Q-B5** | Non-monotone feasibility / reopening? | **`NOT_DETERMINED — NO FULL TEXT`** | No indication either way; "closures" cannot be read as evidence of irreversibility. |
| **Q-B6** | Is "latest extraction time" an explicit output, or implicit in the machinery? | **`NOT_DETERMINED — NO FULL TEXT`** | Abstract's outputs are evacuation times, drill agreement, scenario analysis — suggestive of "not explicit", but not a reading of the body. |

### Requested passages — availability

Available at abstract level for 5 of 12 topics; **7 are empty, and they are the decision-relevant
ones.**

| Topic | Verbatim fragment (abstract / highlights) |
|---|---|
| inbound emergency responders | "enables both outbound self-evacuation and **inbound rescue operations**" |
| emergency extraction | "Pedestrian movement, private vehicle, **emergency extraction**, and vehicle–pedestrian interactions are explicitly represented" |
| responder routing | "custom waypoint-based routing algorithm enables adaptive rerouting for outbound and **inbound** evacuation" |
| dynamic rerouting | "limited **dynamic rerouting** when roads are compromised" (gap); "adaptive rerouting" (highlight) |
| fire-driven road closure | "**Fire-driven road-segment closures** dynamically update network availability during the evacuation" |
| pickup | **none** |
| egress | **none** beyond "outbound self-evacuation" |
| departure time | **none** |
| dispatch time | **none** |
| latest feasible extraction | **none** |
| deadlines | **none** |
| time windows | **none** |

### WG-DBD-1 … WG-DBD-7 scoring

Scored independently. **`docs/EVIDENCE_LEVELS.md` Rule 1 forbids `OCCUPIED` on E2 evidence**, so at
this evidence level no component can legitimately be scored OCCUPIED by this paper.

| ID | Component | Score | Evidence |
|---|---|---|---|
| **WG-DBD-1** | Complete assisted mission: ingress + service + egress | **`PARTIALLY_OCCUPIED`** (provisional, E2) | Ingress and an extraction agent class are asserted by the authors' own deposited abstract/highlights — topic-level statements E2 does support. **The `service` (pickup/loading dwell) element is wholly unevidenced**, and nothing shows ingress/service/egress are chained into one accounted mission rather than three separate behaviours. |
| **WG-DBD-2** | Fire-relative feasible dispatch times computed | **`NOT_DETERMINED`** | Nothing at E2. The retracted lead would, if verified, push toward PARTIALLY_OCCUPIED — for *routes*, not *dispatch instants*. |
| **WG-DBD-3** | Latest feasible dispatch instant reported as an operational quantity | **`NOT_DETERMINED`** | The decisive question; unanswered. Weak negative indicators only (not in stated outputs; no scheduling refs). Neither is admissible to score it. |
| **WG-DBD-4** | Non-monotone feasible dispatch windows as a **set**, not a single deadline | **`NOT_DETERMINED`** | No evidence either way. **Recorded explicitly: WG-DBD-1 being partially occupied does not touch this.** A framework that simulates an inbound leg need not represent feasibility as anything, let alone a non-singleton set. If the "safe time remaining" lead is ever confirmed, its `min` structure is one scalar per route and counts **against** occupancy here. |
| **WG-DBD-5** | Full traversal-interval hazard evaluated | **`NOT_DETERMINED`** | Time-varying *network* state is evidenced; hazard integration across an agent's traversal is not, and is exactly Q-B4. |
| **WG-DBD-6** | Feasibility conditioned on information available at decision time, not oracle future fire | **`NOT_DETERMINED`** | Unreadable at E2. Flagged as first-order for the next attempt: a coupled simulator can trivially hand the router the true future fire, and whether the authors gate that is unaddressed in every retrievable record. |
| **WG-DBD-7** | Dispatch-by maps on Korean rural wildfire geometry | **`NOT_OCCUPIED` — confirmed** | E2 suffices: this is a topic-level fact, not a method detail. Abstract: "tested in a **case study in Portugal**." Four authors Portuguese-institution, one Cypriot. Korea appears nowhere. |

### Does this paper kill the dispatch-by-deadline claim?

**Cannot determine — without the article body, which Elsevier does not serve to this network.**

WG-C-003 stays `SUPPORTED_CANDIDATE`; this audit produced nothing that licenses moving it.
`beyki2026modular` stays CRITICAL, stays `NEEDS_FULL_TEXT`, and stays watch-list item #1.

### What remains unread
The entire body: all sections, figures, tables, equations, limitations and conclusions; all
pagination; the **"emergency extraction" agent logic** (most decision-relevant object in the paper);
whether a **pickup/loading dwell** exists at all; the **waypoint routing algorithm's** objective,
inputs and information-gating; whether any **"safe time remaining"** quantity exists; the
**road-closure rule** and whether a closed segment can **reopen**; whether hazard is checked on
**edge entry** or across **traversal**; the Portuguese site, the drill, and every reported number.

### Next actions, cheapest first
1. **Re-check `evacuarfloresta.enb.pt`.** The authors' project site open-posts their own publisher
   PDFs but has not been updated since 2025-07-28. Cheapest route to E3/E4; no institutional
   access needed.
2. **Email the corresponding author** (Beyki, corresponding). The article is **CC-BY**: he may send
   it and we may hold it. For a paper this decision-critical, one email outranks further scraping.
3. **Retrieve via any institutional network.** The block is on this IP range, not on the reader.
4. **Watch for a Coimbra "Estudo Geral" deposit** (currently `has_repository_copy: false`).

## Follow-up papers
- Siam et al. (2022), *Transportation Research Part D* 103:103147 — cited by this paper.
- Wahlqvist et al., WUI-NITY platform, *Safety Science* (2021) — cited by this paper.
- "Analyzing wildfire evacuation dynamics with agent-based modeling in damaged road networks,"
  *Safety Science* (2025), S0925753525000608 — **RETRIEVE**, damaged-network rerouting.
- Grajdura et al. (2022) — Camp Fire ABM with reduced vehicle access; cited by this paper.
- **New lead (not added to corpus):** "Dynamic command and risk-adaptive decisions in wildfire
  evacuation: simulation-based analysis of a real WUI fire incident in Catalonia, Spain" (2026,
  SSRN preprint, two DOIs: 10.2139/ssrn.7196351 and 10.2139/ssrn.7244752) — **cites this paper**;
  "dynamic command and risk-adaptive decisions" is close to RQ2's framing. SSRN is Elsevier and is
  blocked from this network. Flag for Agent A.
