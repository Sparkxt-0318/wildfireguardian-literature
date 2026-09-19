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
