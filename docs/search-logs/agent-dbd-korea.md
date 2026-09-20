# Search log — Agent B (Prior-Art Adversary): dispatch-by decomposition + Korean empirical audit

**Agent:** B — Prior-Art Adversary
**Date of all queries:** 2026-09-20 (single session)
**Outputs:** `novelty/DBD_DECOMPOSITION.md`, `novelty/KOREAN_EMPIRICAL_AUDIT.md`,
`novelty/SEARCH_GAPS_BLOCKING_CLAIMS.md`
**Mandate:** narrow and targeted. Corpus padding was explicitly forbidden; five records were
added and at least four candidates were examined and deliberately **not** recorded (§4).

---

## 1. Corpus-first pass (no external queries)

| Action | Result |
|---|---|
| Read `bibliography/literature.csv` (165 records): id, year, category, threat, title | full list reviewed |
| Printed `one_line_difference` for all 53 records in categories 1, 2, 3, 9 | source of the WG-DBD-1/2 occupancy findings |
| Aggregated `matrix.*` flags across all 165 `literature/metadata/*.yaml` | 17 records with inbound_responder/pickup/dispatch_by_deadline true-or-partial; `dispatch_by_deadline` is `no`/`false` in 109 records, `partial` in 2, `UNKNOWN` in 3 |
| Read `literature/reviews/01-trigger-modeling.md`, `02-assisted-evacuation.md`, `08-korea-specific.md` | WG-DBD-2 subject split; F1–F6 taxonomy; Korean baseline |

**Conclusion of the corpus pass:** WG-DBD-1 and WG-DBD-2 needed no external search — they were
already occupied inside the repository. External search was spent on WG-DBD-3, -4, -5, -6 and
on Korea.

---

## 2. Adjacent-field queries (WG-DBD-3/4/5/6)

Sources: **OpenAlex API** (`title_and_abstract.search` and full-text `search`), **alphaXiv
discover_papers + get_paper_content**, **Crossref API**, **WebSearch**, **WebFetch** on
publisher/preprint pages, author-hosted PDF.

| # | Query | Source | Usable hits |
|---|---|---|---|
| 1 | safe interval path planning dynamic obstacles | OpenAlex | **`phillips2011sipp`** (ICRA 2011) + 9 SIPP descendants |
| 2 | safe interval path planning | OpenAlex t+a | SIPP kinodynamic (AAAI-23), prioritized SIPP, **SIPP applied to a pickup-and-delivery variant** (Yakovlev et al. 2020, 10.5220/0009888905210528) |
| 3 | moving firefighter problem | OpenAlex t+a | The Moving Firefighter Problem (*Mathematics* 11(1):179); Exact Solutions… on Trees (*Networks* 88(1):42–58, 2026) — examined, **not recorded** (§4) |
| 4 | forbidden intervals shortest path | OpenAlex t+a | 0 |
| 5 | latest departure time network | OpenAlex t+a | reliable-path and earliest-arrival/latest-departure parking papers; no hazard |
| 6 | reach-avoid moving obstacle latest | OpenAlex t+a | 0 usable |
| 7 | latest departure time time-dependent shortest path | OpenAlex full-text | 0 |
| 8 | path planning moving hazard spreading fire robot | OpenAlex full-text | **Wang, Zlatanova & van Oosterom (2017), "Path Planning for First Responders in the Presence of Moving Obstacles With Uncertain Boundaries", *IEEE T-ITS* 18(8):2163–2173** — examined, not recorded (§4) |
| 9 | evacuation routing dynamic obstacles time-expanded network fire spread | OpenAlex full-text | indoor-evacuation noise only |
| 10 | latest dispatch time emergency response deadline | OpenAlex t+a | 0 |
| 11 | departure time reachability deadline time-dependent network | OpenAlex t+a | 0 |
| 12 | shortest path time-dependent arc availability time windows | OpenAlex t+a | 0 |
| 13 | evacuation route fire arrival time road segment traversal feasibility | OpenAlex t+a | 0 |
| 14 | non-FIFO time-dependent shortest path waiting | OpenAlex t+a | Study on Non-FIFO Arc in Time-Dependent Networks (2007) — background |
| 15 | "latest departure time" OR "latest dispatch time" evacuation "fire spread" deadline computed responder | WebSearch | 0 academic |
| 16 | time-dependent shortest path "forbidden intervals" edge unavailable during traversal algorithm | WebSearch | **Sherali & Hill (2009), "Reverse time-restricted shortest paths: Application to air traffic management", *TR-C* 17(6):631–641** (abstract NOT retrieved — open lead); Shortest Paths Avoiding Forbidden Subpaths; route planning with temporary driving bans |
| 17 | reverse time-restricted shortest paths air traffic | OpenAlex t+a | Sherali & Hill record confirmed (DOI 10.1016/j.trc.2009.04.015); **OpenAlex holds no abstract**; ScienceDirect 403 |
| 18 | escaping spreading fire graph agent / backward reachable set latest start time hazard / Hamilton-Jacobi reachability wildfire | OpenAlex t+a | 0 — the HJ-reachability vocabulary was not found and the field was not properly pursued (gap G5) |
| 19 | firefighter escape route travel rate wildland | OpenAlex t+a | Campbell et al. Escape Route Index (*Fire* 2(3):40) and firefighter travel-rate papers — one-way egress capacity, not recorded |
| 20 | alphaXiv discover: "safe interval path planning", "latest departure time", "dynamic obstacles", "time-dependent shortest path", "moving hazard", "deadline" | alphaXiv (arXiv) | **`kemisetti2026stochsipp`** (2608.00792); **`fluschnik2026decaying`** (2603.23504); **`kamphuis2025departure`** preprint (2208.14516); Optimal Path Planning in Hostile Environments (2603.18958); MT-VRP-O (2603.21880); Beer Path Problems in Temporal Graphs (2507.08685) |
| 21 | wildfire evacuation road segment burned over during traversal | WebSearch | **RESCUE (Tammali et al., ICDCN '26, 10.1145/3772290.3772301)** — examined, not recorded (§4) |
| 22 | optimal departure time advice road networks stochastic disruptions | OpenAlex t+a | **journal version: *Computers & Operations Research* 183:107148 (2025), DOI 10.1016/j.cor.2025.107148** |

**Full-text retrievals performed**
- `phillips2011sipp`: PDF from `cs.cmu.edu/~maxim/files/sipp_icra11.pdf`, text extracted with
  pypdf; Section III and Fig. 5 read; three passages quoted verbatim in the note.
- `kemisetti2026stochsipp`: full text via alphaXiv `get_paper_content`; problem-setup section
  read; edge-safety-event definition quoted verbatim.
- `fluschnik2026decaying`, `kamphuis2025departure`: abstracts reproduced verbatim from arXiv abs
  pages (the latter requested twice, second time with an explicit verbatim instruction).

---

## 3. Korean queries

Korean search terms are recorded in Korean, as run.

| # | Query | Source | Route status | Usable hits |
|---|---|---|---|---|
| K1 | 산불 대피 소요시간 산정 연구 취약계층 대피 시간 논문 | WebSearch | ok | KCI/ScienceON/DBpia record URLs; no evacuation-time study |
| K2 | 산불 대피 | koreascience.kr search.page | **ok (WebFetch)** | 9 titles incl. "A Study of Evacuation Map Designing Algorithm in Forest Fire" (2011) |
| K3 | 대피 소요시간 | koreascience.kr | **ok** | 37 results — all building/tunnel/flood/aircraft egress; **no wildfire** |
| K4 | 소방 출동 시간 | koreascience.kr | **ok** | 29 results — urban fire/EMS mobilization time, golden time, dispatch-delay factors; **no wildfire** |
| K5 | 산불 취약계층 | koreascience.kr | **ok** | **0 results** |
| K6 | 산불 확산 예측 | koreascience.kr | **ok** | 33 results, 1998–2025; **none** on prediction latency or evacuation decision timing |
| K7 | 산불 골든타임 | koreascience.kr | **HTTP 400** on this query only (K2–K6 on the same endpoint succeeded) | — |
| K8 | 산불대피지도 | koreascience.kr | **ok** | English title, romanised authors and article ID `CFKO201129149561372` for `kim2011evacmap` |
| K9 | `language:ko` + `title_and_abstract.search:산불`, full cursor sweep | OpenAlex API | **ok** | **all 406 Korean-language 산불 records** retrieved and grepped for 대피/피난/출동/골든/취약/고령/주민/예측 지연 → **one wildfire-evacuation item: `kim2011evacmap`**; everything else is 취약성 (susceptibility) mapping |
| K10 | `language:ko` + `title.search:대피` | OpenAlex API | ok | 93 records; **all building/tunnel/subway fire egress**; no wildfire, no dispatch |
| K11 | site:koreascience.kr OR site:kci.go.kr 산불 대피 시간 고령자 대피 한계시간 연구 | WebSearch | ok | surfaced the 2011 gap statement that led to K8/K9 |
| K12 | 산불 확산 예측 기반 주민 대피 유도 알고리즘 개발 논문 한국 | WebSearch | ok | DQN spread model (한국정보통신학회논문지 2025); `kwak2021evacroute`; `gu2016spreadalgorithm` |
| K13 | "산불" "대피" 인근 마을 재난약자 대피 유도 알고리즘 확산 | WebSearch | ok | ScienceON report `TRKO201800042755` (= `nifos2018evacsystem`) |
| K14 | "산불대피지도 작성 알고리즘에 관한 연구" 한국화재소방학회 2011 | WebSearch | ok | NIFoS report `TRKO201600011244` 「산불지도 작성 알고리즘 개발 및 제작기법 연구」, PI 이병두, 2015 |
| K15 | KCI article page `artiId=ART002789577` | kci.go.kr | **ok (WebFetch)** | `kwak2021evacroute` full record incl. DOI 10.9798/KOSHAM.2021.21.6.63 and Korean abstract |
| K16 | ScienceON report `cn=TRKO201800042755` | scienceon.kisti.re.kr | **ok (WebFetch)** | confirms `nifos2018evacsystem` computes evacuation **range**, not time |
| K17 | ScienceON report `cn=TRKO201600011244` | scienceon.kisti.re.kr | **ok (WebFetch)** | 2015 NIFoS wildfire-map report; abstract does **not** mention 대피지도; no time computed |
| K18 | KCI keyword search `poArtiSearList.kci?poSearchBean.searchQuery=산불 대피` | kci.go.kr | **FAILED — query ignored** | returned an unfiltered listing of 2,432,564 records |
| K19 | DBpia article `nodeId=NODE12543144` | dbpia.co.kr | **FAILED — HTTP 503** | — |
| K20 | ScienceON site search `search/total/Total.do?queryText=산불 대피 시간` | scienceon.kisti.re.kr | **FAILED — HTTP 404** (wrong endpoint) | — |

---

## 4. Examined and deliberately NOT recorded (anti-padding)

| Item | Why not recorded |
|---|---|
| The Moving Firefighter Problem (*Mathematics* 11(1):179, 2022) and Exact Solutions… on Trees (*Networks* 88(1):42–58, 2026) | Responders travel while fire spreads — but the output is a defence strategy minimising burnt vertices; no egress leg, no departure instant, no feasible-window set, and movement is a metric τ rather than a hazard-constrained traversal. Occupies no WG-DBD component. |
| Wang, Zlatanova & van Oosterom (2017), *IEEE T-ITS* 18(8):2163–2173 | First responders routed through moving obstacles with uncertain boundaries — but a modified A* producing a route, no deadline, no round trip, no set. Strong background, not an occupant. |
| RESCUE (Tammali et al., ICDCN '26, 10.1145/3772290.3772301, pp. 168–172) | Evacuee routing with an edge-fire-risk function from rate-of-spread; duplicates `ma2025damaged`'s mechanism without adding a component. 5-page short paper. |
| Campbell et al., Escape Route Index (*Fire* 2(3):40) and wildland-firefighter travel-rate papers | One-way firefighter egress capacity; `fryer2013entrapment` already holds this position in the corpus. |
| Yakovlev et al. (2020), SIPP applied to a pickup-and-delivery variant | Would be a genuine WG-DBD-1 + -4 + -5 combination, but it is multi-agent task allocation on real robots with no hazard and no deadline; **flagged as a follow-up read**, not recorded. |

---

## 5. Access-failure table (feeds `SEARCH_GAPS_BLOCKING_CLAIMS.md`)

| Route | Method | Result | Workaround found? |
|---|---|---|---|
| Consensus (`mcp__consensus__search`) | MCP | **Monthly quota exhausted (30/30)**, resets 1 Oct | No — OpenAlex used instead |
| Semantic Scholar Graph API | curl | **HTTP 429** on every call | No |
| arXiv API (`export.arxiv.org`) | curl | empty response through the agent proxy | Yes — WebFetch on `arxiv.org/abs/...` and alphaXiv `get_paper_content` |
| `koreascience.kr` | curl | **proxy 502 on CONNECT** | **Yes — WebFetch works**; this reverses the previous agents' assumption |
| `scienceon.kisti.re.kr` | curl | connection failed | **Yes — WebFetch works on record pages (`cn=…`)**; the site-search endpoint is still unknown (404) |
| `kci.go.kr` article pages | WebFetch | **ok** | n/a |
| `kci.go.kr` keyword search | WebFetch | **query parameter ignored; unfiltered corpus returned** | No — correct parameter name still unknown |
| `dbpia.co.kr` | WebFetch | **HTTP 503** (third failure across three agents) | No |
| RISS, NDSL | — | **not attempted this session** | — |
| ScienceDirect (`sciencedirect.com`) | WebFetch | **HTTP 403** | No — OpenAlex/Crossref metadata only |
| ACM DL (`dl.acm.org`) | WebFetch | **HTTP 403** | Yes — OpenAlex carried the abstract |
| MDPI (`www.mdpi.com`) | — | not attempted; previously 403 | OpenAlex/Crossref |

---

## 6. Registry edits still OWED (not made by this agent)

The task brief restricted this agent to the files listed in §"Outputs" above and forbade edits
to shared files, because other agents were editing them concurrently. `AGENTS.md` §5 therefore
remains **unsatisfied** for the five new records, and this is recorded here rather than
silently skipped. Whoever holds the shared files must add, for
`phillips2011sipp`, `kemisetti2026stochsipp`, `fluschnik2026decaying`, `kamphuis2025departure`
and `kim2011evacmap`:

- [ ] `bibliography/literature.csv` — one row each
- [ ] `bibliography/doi_registry.csv` — DOI + verification state (three are `UNVERIFIED`:
      StochSIPP, Decaying Trees, `kim2011evacmap`)
- [ ] `bibliography/wildfireguardian.bib` — `@inproceedings` for `phillips2011sipp` and
      `kim2011evacmap`, `@misc`/`@unpublished` for the two preprints, `@article` for
      `kamphuis2025departure`
- [ ] `novelty/NOVELTY_MATRIX.md` — one row each
- [ ] `novelty/NOVELTY_THREATS.md` — all five are HIGH or MODERATE; §2's WG-C-003 table row
      "Latest dispatch time reported as the output" can no longer read "no occupying prior art
      identified" without the qualifier "in wildfire, for a round trip"
- [ ] `docs/CLAIM_REGISTRY.md` — WG-C-003 `SUPPORTED_CANDIDATE` → `WEAKENED`, per
      `DBD_DECOMPOSITION.md` §1
- [ ] `docs/SEARCH_PROTOCOL.md` — category 8 tier note: the Korean-language pass is no longer
      "blocked"; KoreaScience, KCI article pages, ScienceON record pages and an OpenAlex
      `language:ko` sweep all succeeded. DBpia/RISS remain unsearched, so the category moves to
      **S1→S2 (partial)**, not S2.
