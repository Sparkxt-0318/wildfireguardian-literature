# SEARCH_GAPS_BLOCKING_CLAIMS.md — which unclosed gaps can actually change a score

**Author:** Agent B — Prior-Art Adversary
**Date:** 2026-09-20
**Rule applied:** a gap is worth closing only if closing it could change the score of a
component or claim that is still alive. Gaps that can only confirm an existing `OCCUPIED`
are worthless, because `NOVELTY_STANDARD.md` §5's asymmetry means occupancy needs one paper
and is already established.

**What is still alive after `DBD_DECOMPOSITION.md`:** WG-C-003, narrowed to an empirical /
operational-artifact claim (WG-DBD-3's residue, WG-DBD-4's residue, WG-DBD-7's time-valued
map), plus the Korean empirical items Q1 and Q5 in `KOREAN_EMPIRICAL_AUDIT.md`. Nothing else
in the registry is a candidate contribution, so no gap that touches only WG-C-001, -004, -005,
-011, -013 or -014 is worth a minute.

---

## 1. Priority table

| Gap | Claims/components it could change | Can it be closed? | Priority |
|---|---|---|---|
| **G1. Planning-conference sweep (ICAPS, SoCS, AAMAS, IJCAI) + Canadian Traveller Problem literature** | WG-DBD-4 residue (mission-completion departure **set**), WG-DBD-5 residue, WG-DBD-6 residue — i.e. everything WG-C-003 now rests on | **Yes.** OpenAlex and alphaXiv both index these; `kemisetti2026stochsipp` names CTP as its ancestor and gives a citation ladder | **P1 — highest** |
| **G2. Japanese-language sweep (要配慮者 / 避難行動要支援者 / 避難限界時間 / 消防 出動時間)** | WG-DBD-1, -2, -3 empirical axes; WG-DBD-7 by analogy; WG-C-005 | **Probably.** J-STAGE and CiNii are fetchable in principle; not attempted this session | **P1** |
| **G3. Korean RISS / DBpia / NDSL / agency report series** | WG-DBD-7; `KOREAN_EMPIRICAL_AUDIT` Q3 (the file's weakest "not found") | **Partly.** DBpia returned 503 twice across two agents; RISS untried; KCI keyword search is undrivable but KCI *article pages* work | **P2** |
| **G4. Air-traffic-management "reverse time-restricted shortest path" line (Sherali & Hill 2009, *TR-C* 17(6):631–641) and its citers** | WG-DBD-3 — could show the latest-departure quantity is older and more general than `kamphuis2025departure` | **Yes**, via Crossref/OpenAlex citation chase; ScienceDirect returns 403 so the abstract must come from another index | **P2** |
| **G5. Hamilton–Jacobi / backward-reachable-set literature** | WG-DBD-4 residue — a backward reachable tube *is* a set of feasible start times under a moving hazard | **Yes**, but the queries used here returned nothing and the field's vocabulary must be learned first | **P3** |
| **G6. Greek / Portuguese / Spanish category-3 pass** | WG-DBD-1, -5 empirical axes (Mati, Pedrógão Grande civil-protection literatures) | **Yes**, but expected yield is more evacuation *simulations*, which do not report deadlines | **P3** |
| **G7. Category 5 VOI / hard-deadline sensor scheduling (`OPEN_QUESTIONS` B2)** | WG-C-008 only | Yes | **P4 — see §3** |
| **G8. Truck-driving-ban / temporary-road-closure routing** | WG-DBD-5 occupancy only | Yes | **P4 — see §3** |
| **G9. Category 6 fire-spread-model non-English pass; category 10 non-English pass** | nothing alive | Yes | **P4 — see §3** |

---

## 2. Why the top three are the top three

**G1 is P1 because it is aimed at the residue, not the occupancy.** WG-DBD-4 and WG-DBD-5 are
already occupied as method; more searching cannot make that worse. What *can* change is the one
sentence WG-C-003 has left — that nobody reports the **set of departure instants at which a
two-leg mission with a dwell still closes**. Multi-agent-pathfinding and contingent-planning
venues are exactly where a "latest safe start" or "departure-feasibility set" result would be
published without ever using the words wildfire, evacuation or dispatch. This session reached
that literature only through whatever OpenAlex and alphaXiv surfaced; no proceedings were swept.
If G1 finds the residue occupied, **WG-C-003 has nothing left and the program must move to the
empirical/artifact axes or change question.**

**G2 is P1 because the setting argument dies without it.** Japan has an ageing rural population,
steep terrain, a large statutory framework for 避難行動要支援者 (residents requiring evacuation
assistance) and a fire-service literature that measures 出動時間. A Japanese paper computing an
assisted-evacuation departure deadline would occupy WG-DBD-3's residue *and* remove the "Korean
ageing-rural setting is where this has to be done" argument in one move. The repository has never
run a Japanese pass; `docs/SEARCH_PROTOCOL.md` §1 requires a non-English pass for
`SUPPORTED_CANDIDATE`, and Korean alone is a thin reading of that requirement when the nearest
comparable society is next door.

**G3 is P2, not P1, because this session partly closed it.** KoreaScience keyword search, KCI and
ScienceON record pages and a systematic OpenAlex `language:ko` sweep all worked (see
`docs/search-logs/agent-dbd-korea.md`). What remains — RISS, DBpia, NDSL, agency report series —
is a real gap, but it now bears mainly on `KOREAN_EMPIRICAL_AUDIT` Q3, which is an empirical-axis
question about a claim whose *concept* axis is already occupied elsewhere. It cannot resurrect a
dead claim; it can only invalidate an empirical one.

---

## 3. Gaps NOT worth closing, and why

- **G7 — deeper VOI / hard-deadline sensor scheduling.** WG-C-008 is `WEAKENED` with three
  independent occupants (`malings2016voisensor`, `sun2025decisionfocusedsensing`,
  `shao2026beliefaware`) and survives only bundled with WG-C-003. Closing G7 can move it from
  WEAKENED to OCCUPIED — a change with no consequence, because nothing is claimed on it alone.
  Skip unless WG-C-003 survives G1, at which point the bundle becomes worth defending.
- **G8 — truck-driving-ban routing.** This would almost certainly show that "you may not be *on*
  the arc while it is closed" predates SIPP by decades. WG-DBD-5 is already OCCUPIED; a second
  and older occupant changes no score. Useful for an introduction, not for a verdict.
- **G9 — non-English passes for categories 6 and 10.** Fire-spread models and simulation-study
  methodology support no live claim. WG-C-010 is WEAKENED and WG-C-014 is WEAKENED with 1987
  occupants; neither can be rescued or further harmed by a language pass.
- **More searching on WG-DBD-4 / WG-DBD-5 occupancy as such.** Occupied is occupied. Additional
  confirmations are `NOVELTY_STANDARD.md` §3.2 in reverse: they feel like work and change nothing.
- **Anything aimed at WG-C-001, -004, -011, -013.** REJECTED or OCCUPIED. Closed.

---

## 4. Full-text gaps that block harder than any search gap

These are not search failures — the papers are identified — and under `NOVELTY_STANDARD.md` §10
they cap confidence regardless of how much more searching is done.

| Item | Blocks | Why it outranks searching |
|---|---|---|
| `beyki2026modular` full text | WG-DBD-1, -2, -5; WG-C-003 | Names the inbound-rescue gap and closes it; if it reports safe-time-remaining per waypoint, WG-C-003 is OCCUPIED |
| `moradi2026supported` full text / journal version | WG-DBD-1, -2, -4, -5 | Per-arc hard fire windows already; a per-time-step feasibility indicator would occupy the **set** |
| `kamyabniya2022thesis` (uO Research / ProQuest) | WG-DBD-4 | `OPEN_QUESTIONS` A2 predicts a time-step feasibility indicator, which *is* the dispatch-feasible set |
| `ma2025damaged` full text | WG-DBD-5 wildfire application | Decides whether traversal-interval hazard is occupied inside wildfire or only by analogy |
| `tang2025transit` abstract/full text | WG-DBD-1, -3 | Structurally our trip, not indexed as wildfire |
| `kamphuis2025departure` journal full text | WG-DBD-3, -4 | Whether the online variant reports a feasible departure **set** after each update |

**Recommended order of work:** `beyki2026modular` → G1 → `kamyabniya2022thesis` → G2 →
`ma2025damaged` → G3/G4. Everything else waits.
