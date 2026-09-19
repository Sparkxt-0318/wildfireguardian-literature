# Search Log — Agent A/B (Categories 2 & 9: Assisted Evacuation, Vulnerable Populations)

**Agent role:** Search Researcher + Prior-Art Adversary
**Domain:** Cat 2 (supported/assisted wildfire evacuation), Cat 9 (vulnerable populations)
**Target claims to falsify:** WG-C-003, WG-C-005, WG-C-011
**Search dates:** 2026-09-19
**Tools used:** Consensus (Semantic Scholar/PubMed/Scopus/arXiv), WebSearch, WebFetch (ScienceDirect, Springer, arXiv, OpenAlex, Crossref, Google Scholar), alphaXiv/arXiv

---

## Log format
`| # | Date | Source | Query | Usable hits |`

---

## Round 1 — Core Category 2 sweep

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 1 | 2026-09-19 | Consensus | `assisted evacuation of non-ambulatory residents wildfire vehicle routing deadline` | 10 returned; **HIGH VALUE**: Beyki 2026 (inbound rescue + fire spread), Moradi 2026 (supported evacuation wildfire, stochastic, time windows), Shahparvari 2017a/b (bushfire VRP late evacuees), Alexander 2026 (NH-Evac-VRP), Abbasi 2015, Xu 2022 (heterogeneous fleet, low-mobility individuals), Grajdura 2022, Raei 2026, Zhao 2021 |
| 2 | 2026-09-19 | WebSearch | `latest dispatch time responder evacuation vulnerable resident wildfire round trip deadline` | 0 academic hits — only public-facing preparedness guidance (Ready.gov, CAL FIRE, Oregon OEM). Notable: the phrase "latest dispatch time" returns no research literature. |
| 3 | 2026-09-19 | WebSearch | `bus-based evacuation routing fire spread time windows inbound leg deadline optimization` | Goerigk/Bish bus-evacuation lineage; Zhang round-trip bus evacuation model (TR-A 2020); Valparaiso fire bus routing (CEC 2017); Beyki 2026 again |
| 4 | 2026-09-19 | WebFetch (ScienceDirect) | Beyki 2026 full text `S0925753526000913` | **HTTP 403** — paywalled. Metadata obtained via Crossref instead. NEEDS_FULL_TEXT. |
| 5 | 2026-09-19 | WebSearch | `Moradi "supported evacuation" wildfire Logic-Based Benders Decomposition Roxborough Park vulnerable` | **arXiv 2608.05413** located (Moradi, Sauré, Patrick). Full text retrieved via alphaXiv. CRITICAL. |
| 6 | 2026-09-19 | alphaXiv get_paper_content | `arxiv.org/abs/2608.05413` | Full preprint text (2,910 lines) retrieved and read. |
| 7 | 2026-09-19 | Crossref API | bibliographic query: Beyki modular agent-based wildfire evacuation | DOI 10.1016/j.ssci.2026.107200, Safety Science 199:107200 (2026) confirmed |
| 8 | 2026-09-19 | WebSearch | `Flores supported evacuation vulnerable populations Saddleridge fire goal programming pick-up points` | Flores/Ortuño/Tirado 2023 Safety Science 164:106117; Flores et al. 2020 Mathematics 8(4):648 |
| 9 | 2026-09-19 | WebSearch | `"latest safe departure time" OR "latest dispatch time" emergency vehicle hazard evacuation optimization` | **ZERO academic hits.** Only public preparedness guidance and NFPA response-time standards. Strong negative signal for the exact output quantity of WG-C-003. |
| 10 | 2026-09-19 | WebSearch | `Kamyabniya supported evacuation wildfire temporary shelter location vehicle routing two-stage stochastic` | Kamyabniya (2022) confirmed only as a citation inside Moradi et al.; primary record not retrieved → RECALL/CITED_ONLY |
| 11 | 2026-09-19 | WebSearch | `first responder ingress wildfire trigger buffer rescue vehicle travel time fire arrival constraint` | Li/Cova/Dennison trigger-coupling (egress only); Greater Khingan fire-truck scheduling (suppression, not evacuation); no dispatch-deadline work |
| 12 | 2026-09-19 | Crossref API (batch) | 6 bibliographic queries (Flores x2, Shahparvari x2, Xu, Zhang round-trip bus) | All DOIs verified. Additional find: Shahparvari et al. Omega 72:96-117 (2017) possibilistic scheduling |
| 13 | 2026-09-19 | alphaXiv discover_papers | assisted evacuation / wildfire / dispatch deadline / vulnerable / inbound leg (difficulty 9, recency) | 8 results. New leads: arXiv 2410.14500 (time-expanded networks + wildfire info), 2608.04225 (adaptive robust evacuation planning), 2603.29055 (Lahaina macroscopic traffic) |
| 14 | 2026-09-19 | WebSearch | `2026 wildfire evacuation "cannot self-evacuate" transport disadvantage carless households operational definition` | UCLA ITS 2025 LA Fires transit-rider studies; Natural Hazards Center "Transit Agencies and Wildfire Evacuation". Cat-9 evidence base. |

## Round 2 — Formulation-level adversarial sweep (OR / non-wildfire hazards)

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 15 | 2026-09-19 | alphaXiv get_paper_content | `arxiv.org/abs/2410.14500` (Borgwardt et al., time-expanded networks + wildfire info) | Full text retrieved. Keyword scan for `latest / deadline / depart / dispatch / inbound / pickup / round-trip / arrival time` → **no matches in body**. Self-evacuation max-flow only. Threat LOW. |
| 16 | 2026-09-19 | WebSearch | `"latest departure time" time-dependent network hazard evacuation quickest path deadline computation` | Classical OR: "latest departure" exists as a time-dependent shortest-path quantity under FIFO (Bast et al. route-planning survey). **No application to hazard-constrained rescue dispatch.** |
| 17 | 2026-09-19 | WebSearch | `dial-a-ride problem emergency evacuation mobility impaired deadline hazard progression 2025` | IJERPH 2025 scoping review (10.3390/ijerph22111680); Scientia Iranica disability evacuation optimisation; Applied Intelligence 2022 disability compatibility constraints; UCLA ITS 2025 LA-fires transit riders; arXiv 2205.05324 DARP branch-cut-price |
| 18 | 2026-09-19 | WebSearch | `nursing home hurricane evacuation decision timing model latest time to begin evacuation` | **HURREVAC** (operational tool: evacuation start time as a *range*, = hazard onset minus clearance time) — closest operational analogue to a dispatch-by deadline, but a government tool, not research. NSF PAR 10537248 (flood prediction + stochastic optimisation for hospital/NH evacuation). |
| 19 | 2026-09-19 | WebSearch | `no-notice evacuation transit-dependent populations pickup point bus dispatch time optimization hazard` | Bish (2011) OR Spectrum; Heydar 2016 J. Adv. Transportation; pedestrian–bus pickup location planning; Zhao 2020 round-trip bus model |
| 20 | 2026-09-19 | WebFetch | `par.nsf.gov/servlets/purl/10537248` | PDF downloaded (2.1 MB) but **text extraction failed** (no working PDF toolchain). Identified instead via search as the Kim / Toplu-Tutay / Kutanoglu / Hasenbein line. NEEDS_FULL_TEXT. |
| 21 | 2026-09-19 | WebSearch | `physics-based flood prediction stochastic optimization hospital nursing home evacuation coordination hurricane vehicle scheduling` | **Kim, Toplu-Tutay, Kutanoglu & Hasenbein** (SSRN 4704899); **Rambha et al. 2021** TR-E 151:102321 staged hospital evacuation — both HIGH threat, recorded |
| 22 | 2026-09-19 | WebFetch | `pmc.ncbi.nlm.nih.gov/articles/PMC12652914/` (Matsuo et al. 2025 full text) | Population definition, five barrier criteria, and evidence-base characterisation extracted. **Confirms no operational definition of "cannot self-evacuate" and no baseline registry/census instrument.** |
| 23 | 2026-09-19 | WebSearch | `"Evacuation and Transportation Barriers Among Vulnerable Populations..." scoping review 2025` | DOI 10.3390/ijerph22111680 confirmed; also surfaced U Alberta "Equitable Public Transit Evacuation Planning: A Systematic Review" and arXiv 2412.05777 |
| 24 | 2026-09-19 | Consensus | `latest feasible dispatch time emergency responder round trip hazard arrival deadline rescue mission feasibility` | 10 results. **Yu et al. 2020 Nature Sustainability** (inbound responder under flood, vulnerable sites) — HIGH; Dubois 2022 VRP under deadlines (flood); Chang 2024 JORS ambulance MCI; Shiri 2020/2024 online SAR routing; Jagtenberg 2017 / Usanov 2019 dispatch policy. **No paper outputs a latest-dispatch time.** *(Consensus monthly quota exhausted after this query.)* |

## Round 3 — 2025–2026 sweep and preprint sweep

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 25 | 2026-09-19 | WebSearch | `2026 wildfire assisted evacuation optimization vulnerable residents fire spread simulation coupled routing preprint arXiv` | Chang 2026 Risk Analysis (PMC13507379, PMID 42642826); arXiv 2502.07787 (SAV rural vulnerable); arXiv 2601.01052 (Palisades/Eaton Facebook data) |
| 26 | 2026-09-19 | WebSearch | `"trigger point" OR "trigger boundary" assisted evacuation special needs population wildfire WUIVAC PERIL responder` | WUIVAC, PERIL, Cedar Fire dynamic buffers, Fryer/Dennison/Cova firefighter entrapment triggers. **All egress-only; explicit note that results "do not contain specific information about special needs populations or assisted evacuation protocols."** |
| 27 | 2026-09-19 | WebSearch | `evacuation "pickup and delivery problem with time windows" wildfire fire arrival time derived time windows` | Moradi 2026 again; Flores 2023; secondary mention of "safe time remaining ... least of the fire arrival times" per waypoint (attributed to Beyki 2026, unconfirmed) |
| 28 | 2026-09-19 | WebSearch | `Chang 2026 Risk Analysis multiscale wildfire evacuation differential access safe egress Marin County` | Authors + Korea University affiliation of first author; tri-coupled fire/communications/traffic framework |
| 29 | 2026-09-19 | alphaXiv discover_papers | transit evacuation / carless / transport-disadvantaged / equity / elderly / disability / SAV / rural (difficulty 7, recency) | 10 results. New: arXiv 2502.07787, 2412.05777, 2402.17593, 2103.15156, 2604.22737, 2008.11169, 2609.03301 |
| 30 | 2026-09-19 | WebSearch | `wildfire evacuation systematic review research gaps assisted evacuation vulnerable "research gap" dispatch timing 2025 2026` | Zehra & Wong (2024) TP&T 47(8):1364-1398 — **its declared gaps must be read in full**; MDPI Applied Sciences 13:9587 evacuation-simulation gaps overview |

## Round 4 — Non-English (Korean) pass and adjacent-field pass

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 31 | 2026-09-19 | WebSearch (ko) | `산불 대피 거동불편자 구조 차량 배차 시간 최적화 고령자 농촌` | **No peer-reviewed Korean research.** Returned: MOIS 2025 rapid-wildfire resident-evacuation system revision; **Yeongyang County (영양군) bus/taxi disaster evacuation network** for elderly and carless mountain-village residents — motivating evidence, not literature; KFS/NIFoS/provincial public action guidelines |
| 32 | 2026-09-19 | WebSearch | `wildland firefighter escape route travel time safe separation distance Campbell Dennison entrapment trigger` | Escape Route Index (10.3390/fire2030040); firefighter travel rates by slope (Fire 3(3):52); GeoLCES; Fryer/Dennison/Cova entrapment triggers. **All firefighter EGRESS; no responder ingress-to-collect-a-resident deadline.** |
| 33 | 2026-09-19 | WebSearch | `"special needs registry" evacuation assistance wildfire effectiveness carless registry enrollment evidence` | Florida statutory county registries (pickup time + location given to enrolees); documented limitations (no guarantee of assistance, privacy suppression of enrolment, inaccessible shelters). Practice, not research. |
| 34 | 2026-09-19 | WebSearch | `Shahparvari late evacuees bushfire "time window" derived fire propagation ... shelter vehicle capacity` | Full Shahparvari lineage mapped: TR-E 93:148-176 (2016); Omega 72:96-117 (2017); TR-A 104:32-49 (2017); TR-D 67:703-722 (2019); AJIS multi-objective. **Confirms time windows are inputs throughout.** |
| 35 | 2026-09-19 | WebSearch | `"latest possible departure" OR "last feasible dispatch" rescue vehicle wildfire deadline feasibility round trip base resident shelter` | **ZERO academic hits.** Greater Khingan fire-truck scheduling (suppression) only. |

## Round 5 — Metadata verification

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 36 | 2026-09-19 | Crossref API (batch) | 11 bibliographic queries: Shahparvari TR-E; Bish OR Spectrum; Zehra & Wong; Grajdura; Ebrahimnejad; Alexander GECCO; Zhao round-trip bus; Dubois; Rambha; Beyki; Flores | All DOIs, volumes, pages, author lists verified. One 429 rate-limit encountered and retried with backoff. |
| 37 | 2026-09-19 | Semantic Scholar API | DOI lookups x10 for abstracts and OA status | Full abstracts obtained for Rambha 2021, Alexander 2026, Matsuo 2025, Shahparvari 2016, Shahparvari 2019, Flores 2020, Chang 2026. **Abstracts NOT available for**: Shahparvari 2017 Omega, Flores 2023, Shahparvari 2017 TR-A, Beyki 2026 (all flagged NEEDS_FULL_TEXT). |

---

## Negative results worth recording

These are **negative results**, which under NOVELTY_STANDARD §3.2 yield `UNKNOWN`, never support.
They are logged so the next auditor does not repeat them.

1. The literal phrases **"latest dispatch time"** and **"latest safe departure time"** return **no
   academic literature** in the emergency-vehicle / evacuation context across multiple engines —
   only public preparedness guidance and NFPA response-time standards.
2. No retrieved paper reports a **dispatch-by deadline** as its output quantity for an
   assisted-evacuation mission under any hazard.
3. The wildfire **trigger-boundary** literature (WUIVAC, PERIL, Cedar Fire buffers, firefighter
   entrapment triggers) contains **no** treatment of special-needs or assisted evacuation; one search
   engine surfaced this absence explicitly.
4. No peer-reviewed **Korean** assisted-evacuation research was retrieved in a Korean-language pass.
5. No **validated instrument** for identifying in advance who cannot self-evacuate is reported in the
   2025 PRISMA-ScR scoping review that would have found one.

## Failures and access barriers (recorded honestly)

- **ScienceDirect HTTP 403** on Beyki et al. 2026 (`S0925753526000913`) despite CC-BY hybrid OA.
- **PDF text extraction unavailable** in this environment (no `pdftotext`; `pypdf` import fails on a
  broken `cryptography` rust binding) — blocked reading of the NSF PAR patient-evacuation PDF.
- **Consensus monthly quota exhausted** after 3 queries; remaining coverage carried by WebSearch,
  Crossref, Semantic Scholar and alphaXiv.
- **Crossref 429** once; resolved with backoff and a UA header.
