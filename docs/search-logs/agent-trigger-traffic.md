# Search Log — Agent A/B (Trigger Modeling + Wildfire Traffic)

**Agent:** A/B — Search Researcher + Prior-Art Adversary
**Domain:** Category 1 (wildfire evacuation trigger modeling), Category 3 (wildfire + traffic)
**Target claims:** WG-C-001, WG-C-003, WG-C-004, WG-C-006, WG-C-014
**All searches run:** 2026-09-19

"Usable hits" = records that were recorded in `literature/metadata/` or followed up.

---

## 1. Discovery queries

| # | Query (verbatim) | Source | Date | Usable hits |
|---|---|---|---|---|
| Q01 | `wildfire evacuation trigger buffer modeling fire spread WUIVAC` | Consensus (mcp__consensus__search) | 2026-09-19 | 10 of 10 — the entire Cova/Dennison/Li/PERIL lineage in one call, **plus** `beyki2026modular` |
| Q02 | `probabilistic wildfire evacuation trigger boundary ensemble uncertainty` | Consensus | 2026-09-19 | 0 — **rate-limit error**, query never executed |
| Q03 | `k-PERIL wildfire evacuation trigger boundary Mitsopoulos Imperial College` | WebSearch | 2026-09-19 | 4 — Zenodo k-PERIL record, FSJ stochastic-boundaries paper, PERIL Safety Science paper, Ronchi verification. **Established that "Mitsopoulos" is not an author in this lineage** (correct names: Mitchell, Kalogeropoulos, Rein) |
| Q04 | `Beyki wildfire evacuation agent-based inbound rescue operations multimodal Safety Science 2026` | WebSearch | 2026-09-19 | 3 — Beyki 2026 pii, Chang 2026 Marin County, Siam 2022 |
| Q05 | `emergency vehicle ingress against outbound evacuation traffic wildfire simulation contraflow responder` | WebSearch | 2026-09-19 | 2 — `lu2026lahaina` (arXiv 2603.29055), Zhao & Wong Berkeley traffic sim |
| Q06 | `"latest dispatch time" OR "dispatch deadline" emergency responder wildfire evacuation assistance vulnerable residents model` | WebSearch | 2026-09-19 | **0 research hits** — returned only fire-department public guidance pages. Notable null result for WG-C-003 |
| Q07 | `wildfire evacuation vehicle routing problem time windows assisted evacuation nursing home mobility impaired pickup` | WebSearch | 2026-09-19 | 4 — **`moradi2026supported` (arXiv 2608.05413)**, `flores2023goal`, a GECCO nursing-home evacuation VRP, Shahparvari-adjacent review |
| Q08 | `wildfire evacuation trigger boundary 2026 machine learning ensemble forecast uncertainty new paper` | WebSearch | 2026-09-19 | 3 — arXiv 2605.03148 (boundary-aware UQ), arXiv 2603.22331 (conformal risk control for evacuation mapping), EGUsphere diffusion surrogate. **Leads only; not recorded** |
| Q09 | `dynamic traffic assignment wildfire evacuation road closure fire arrival time network degradation simulation` | WebSearch | 2026-09-19 | 3 — `ma2025damaged`, `lu2026lahaina`, `beyki2026modular` |
| Q10 | `"emergency responder" access ingress during evacuation counterflow simulation "response vehicles" delay wildfire hurricane modeling` | WebSearch | 2026-09-19 | 1 — reinforced `lu2026lahaina` emergency-lane result; no new dispatch-deadline work |
| Q11 | `"latest safe departure" OR "latest departure time" OR "last safe moment" evacuation fire arrival time computation model` | WebSearch | 2026-09-19 | 1 useful — `chang2026marin`; the rest are **building-fire** RSET work, a different literature |
| Q12 | `wildfire spread prediction accuracy IoU Jaccard versus decision quality evacuation downstream decision relevance metric` | WebSearch | 2026-09-19 | 1 lead — arXiv 2603.22331 states that existing work "evaluates exclusively on accuracy-based metrics (F1, IoU, AUROC)". **Supports WG-C-014 remaining open; not recorded (out of my category)** |
| Q13 | `wildfire evacuation model "rescue" vehicles entering fire zone while residents evacuate simulation 2025` | WebSearch | 2026-09-19 | 0 new — confirmed 2025 work is staged-evacuation / behaviour focused, not responder ingress |
| Q14 | `Beyki Santiago Laim wildfire evacuation model Portugal estudogeral repository emergency extraction inbound` | WebSearch | 2026-09-19 | 1 — located the EvacuarFloresta project (2021–2025), whose stated objectives include "determining support vehicle routes" |
| Q15 | `산불 대피 교통 시뮬레이션 대피 시점 연구 Korea wildfire evacuation traffic simulation trigger` (**non-English pass**) | WebSearch | 2026-09-19 | 1 lead — a Korean-language GIS resident evacuation-route paper (semanticscholar PDF cd9a/...). **RECALL/lead only, not verified, not recorded.** No Korean trigger-timing work located |
| Q16 | `arxiv 2026 preprint wildfire evacuation "trigger" deadline optimization responder rescue dispatch timing` (**preprint sweep**) | WebSearch | 2026-09-19 | 0 new killers — surfaced wildfire *suppression* optimisation (arXiv 2605.04510) and UAV response, not evacuation dispatch deadlines |
| Q17 | keywords `["wildfire evacuation","trigger boundary","emergency responder","dispatch","vehicle routing","fire spread forecast"]`, difficulty 9, prioritize=recency | alphaXiv `discover_papers` | 2026-09-19 | 2 of 10 — re-surfaced `moradi2026supported` and `lu2026lahaina` as the top two hits, which is corroborating evidence that these are the closest preprints |
| Q18 | `emergency responder inbound travel against outbound evacuation traffic flow modeling` | Consensus | 2026-09-19 | **0 — monthly search quota exhausted (30/30).** Query never executed |

---

## 2. Citation-chain traversals

| # | Traversal | Source | Date | Usable hits |
|---|---|---|---|---|
| C01 | **Forward** citations of k-PERIL (`10.1016/j.firesaf.2023.103854`) | Semantic Scholar graph API | 2026-09-19 | 13 citing papers; **4 recorded**. This call found **`kalogeropoulos2026ensemble`** — the WG-C-004 killer |
| C02 | **Forward** citations of PERIL (`10.1016/j.ssci.2022.105914`) | Semantic Scholar graph API | 2026-09-19 | 23 citing papers; **4 recorded**, incl. `tang2025transit`, `kim2024directional`, `gwynne2023roxborough` |
| C03 | **Forward** citations of `li2018coupling` (`10.1007/s10694-018-0771-6`) | Semantic Scholar graph API | 2026-09-19 | 0 — API returned an empty list; **traversal incomplete, must be retried** |
| C04 | **Backward** — literature review of `moradi2026supported` read in full (alphaXiv full-text retrieval of arXiv:2608.05413) | alphaXiv `get_paper_content` + grep | 2026-09-19 | 6 — `flores2020supported`, `flores2023goal`, `shahparvari2017robust`, `shahparvari2019fleet`, Kamyabniya 2022, `cova2011shelter` |
| C05 | **Backward** — references of `cova2005trigger` | — | 2026-09-19 | **NOT PERFORMED.** Full text unobtainable (publisher 403). Recorded as an open gap |

---

## 3. Metadata verification calls (Crossref / Unpaywall / OpenAlex / Semantic Scholar)

- **Crossref REST API** (`api.crossref.org`) — used for every recorded paper. Both
  `query.bibliographic` searches (~14 calls) and single-DOI lookups (28 DOIs in one sweep,
  plus retries). This was the primary verification channel: it supplied exact title,
  full author given names, container title, volume, issue, pages, article number, issued
  date and work type. **Two failures:** `10.1016/j.trd.2016.11.015` (`shahparvari2019fleet`)
  would not resolve on single-DOI lookup, so only family names and a truncated title were
  verified for it — flagged in its YAML.
- **Unpaywall** (`api.unpaywall.org`) — OA status for `10.1016/j.firesaf.2023.103854`,
  `10.1016/j.ssci.2022.105914`, `10.1016/j.firesaf.2026.104912`, `10.1016/j.ssci.2026.107200`.
  All four `is_oa = true`; the three 2023–2026 Elsevier ones are `hybrid`.
- **OpenAlex** (`api.openalex.org`) — **abstract** retrieval (inverted index reconstructed)
  for `kalogeropoulos2026ensemble`, `beyki2026modular`, `kalogeropoulos2023kperil`,
  `kalogeropoulos2025dire`. **Then the shared-IP daily budget was exhausted (HTTP 429)**,
  which is why `tang2025transit`, `ma2025damaged` and `kim2024directional` have no verified
  abstract. Retry on a later day or with an API key.
- **Semantic Scholar graph API** — citation traversals (above) and abstract attempts.
  Abstracts returned `null` for all four Elsevier DOIs tried. One HTTP 429 early on.
- **FRAMES catalog** (`frames.gov/catalog/66666`) — supplied the PERIL abstract when
  ScienceDirect refused.
- **Zenodo** (`zenodo.org/records/10277917`) — k-PERIL software record, DOI
  10.5281/zenodo.10277917, dated 2023-12-06.
- **arXiv abstract pages** — `2603.29055`, `2608.05413`, fetched directly.

---

## 4. Access failures (these are real gaps, not formalities)

| Resource | Failure | Consequence |
|---|---|---|
| ScienceDirect (all Elsevier full texts) | HTTP 403 to WebFetch **and** to curl with a browser UA, including for CC-BY open-access articles | `beyki2026modular`, `tang2025transit`, `ma2025damaged`, `li2018coupling`, `mitchell2023peril`, `kalogeropoulos2*` all assessed at E2 or worse |
| OpenAlex | HTTP 429, shared-IP daily budget exhausted | No abstracts for `tang2025transit`, `kim2024directional`, `ma2025damaged` |
| Consensus MCP | Monthly quota (30) exhausted after 1 successful call | Only one Consensus query ran; it was productive, but the planned probabilistic-trigger and inbound-responder queries never executed |
| Crossref single-DOI `10.1016/j.trd.2016.11.015` | Malformed/empty response on repeated attempts | `shahparvari2019fleet` given names UNVERIFIED |

---

## 5. Protocol compliance for this agent's domain

| NOVELTY_STANDARD §5 requirement for `SUPPORTED_CANDIDATE` | Status |
|---|---|
| ≥4 wording variants | **Met** — 16 distinct discovery queries executed (Q01, Q03–Q17) |
| ≥2 adjacent fields | **Met** — building-fire responder counterflow (`averill2007emergencyresponse`); transit/paratransit evacuation (`tang2025transit`); humanitarian-logistics OR (`flores2020supported`); macroscopic traffic flow / conservation laws (`lu2026lahaina`) |
| ≥1 preprint server | **Met** — arXiv (2 recorded preprints), SSRN (precursor of `ma2025damaged`), alphaXiv discovery |
| ≥1 non-English pass | **Partially met** — one Korean-language pass (Q15) returned a lead that was **not verified and not recorded**. No Greek, Portuguese or Spanish pass was run despite three relevant national literatures (Mati, EvacuarFloresta, Flores et al.) |
| Query log committed | **This file** |

**Conclusion on protocol:** the non-English pass is incomplete and the `li2018coupling`
forward chain (C03) and the `cova2005trigger` backward chain (C05) were not completed.
Per NOVELTY_STANDARD §5, **no claim in this agent's domain may be moved to
`SUPPORTED_CANDIDATE` on the strength of this log alone.**

---

## 6. Cross-agent collisions observed (for the verification agent)

While this agent was writing, other agents wrote to the same directories. Two conflicts
must be reconciled by Agent C:

1. **Duplicate paper_id for one paper.** `10.1111/risa.70338` (Chang et al., Marin County)
   is filed twice: `chang2026marin.yaml` (this agent) and `chang2026multiscale.yaml`
   (another agent). One must be retired.
2. **Metadata overwritten.** `beyki2026modular.yaml` and `moradi2026supported.yaml` were
   written by another agent at ~18:18–18:19 and then rewritten by this agent's generator at
   ~18:20. The *notes* (`literature/notes/beyki2026modular.md`,
   `moradi2026supported.md`) are the other agent's and were **left intact** — they are
   independent, substantively agree with this agent's reading, and in the Moradi case were
   produced from the same full text. The YAML/note pairs should be checked for consistency.
