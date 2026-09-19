# Search Log — Agent A/C (Category 8: Korea-specific wildfire research)

**Agent role:** Search Researcher + Verification Auditor
**Domain:** Cat 8 — Korean wildfire research, Korean AND English language
**Target claim to decide:** WG-C-007 (Korean-setting wildfire evacuation-timing analysis),
with secondary bearing on WG-C-003, WG-C-005, WG-C-012, WG-C-014.
**Judge question addressed:** Q7 (geographic novelty / "first in Korea").
**Search date:** 2026-09-19
**Tools used:** Consensus (Semantic Scholar/Scopus/PubMed/arXiv), WebSearch (Korean + English),
WebFetch (KCI, ScienceON/KISTI, DBpia, j-kosham.or.kr, kjrs.org, mois.go.kr, forest.go.kr,
center.forest.go.kr, book.nifos.go.kr, index.go.kr, OpenAlex API, Crossref API, MDPI via DOI).

**Note on tool limits:** MDPI (`www.mdpi.com`) returns HTTP 403 to WebFetch and DBpia returns
HTTP 503; MDPI metadata was therefore verified through the OpenAlex and Crossref APIs
(`api.openalex.org/works/doi:...`), which return publisher-deposited records. Consensus quota
was nearly exhausted (3 searches remaining at end of session) — the Korean-language sweep was
carried mainly by WebSearch + KCI/ScienceON record fetches.

---

## Log format
`| # | Date | Source | Query (verbatim; Korean queries recorded in Korean) | Usable hits |`

---

## Round 1 — Broad bilingual opening sweep

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 1 | 2026-09-19 | Consensus | `Korea wildfire evacuation timing model rural residents` | 10 returned; **HIGH VALUE**: An et al. 2026 (2022 Donghae, disaster-vulnerable evacuation behaviour from mobile floating-population data), Kwon et al. 2025 (`Systems`, Uiryeong County MIP evacuation-system design). Rest non-Korean (Zhao 2021, Mitchell 2022 PERIL, Kuligowski 2020/2022, Vaiciulyte 2021, Grajdura 2021, Li 2022, Molan 2022). |
| 2 | 2026-09-19 | Consensus | `Korean forest fire spread model Rothermel fuel model Pinus densiflora` | **RATE LIMITED — no results returned.** Re-run deferred; coverage obtained instead via queries 9, 16, 17. |
| 3 | 2026-09-19 | WebSearch | `산불 대피 시간 모델 주민 대피 연구 논문` | **HIGH VALUE**: KCI record 도시산불 대응을 위한 GIS 기반 주민최적대피경로설정 알고리즘 개발; ScienceON 재난 재해 지역의 산불 확산경로와 이동속도 예측 알고리즘; MOIS press release 「정부, 초고속 산불 대비 주민대피 체계 개선키로」; edaily 「최대 순간풍속으로 산불 예측…주민대피 3단계 구분」. |

## Round 2 — Record verification for Round 1 Korean hits

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 4 | 2026-09-19 | WebFetch (KCI) | `ciSereArtiView.kci?...artiId=ART002789577` | Full record verified: 곽재환·김남균·김만일 (2021), 한국방재학회논문집 21(6):63–70, DOI 10.9798/KOSHAM.2021.21.6.63. → `kwak2021evacroute` |
| 5 | 2026-09-19 | WebFetch (ScienceON) | `selectPORSrchArticle.do?cn=JAKO201626360540384` | Full record verified: 구남경·이강환 (2016), 한국정보통신학회논문지 20(8):1581–1586, DOI 10.6109/jkiice.2016.20.8.1581. → `gu2016spreadalgorithm` |
| 6 | 2026-09-19 | WebFetch (MOIS) | `mois.go.kr ... nttId=117125` | **CRITICAL**: MOIS press release 2025-04-16. General residents evacuate ~5 h before predicted fire arrival; disaster-vulnerable residents ~8 h before. → `mois2025evacuationstages` |

## Round 3 — MOIS / agency operational systems (the WG-C-007 crux, judge Q7)

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 7 | 2026-09-19 | WebSearch | `행정안전부 산불 주민대피 5시간 전 재난약자 8시간 전 대피 기준 2025` | Confirms the 위험구역 (≤5 h) / 잠재적 위험구역 (≤8 h) zoning and the 3-stage 주민대피 system across korea.kr, kyongbuk.co.kr, nate/news. Corroborated by ≥3 independent outlets + the MOIS release itself. |
| 8 | 2026-09-19 | WebSearch | `행정안전부 인공지능 AI 산불 대피 경로 안내 시스템 개발` | **CRITICAL**: 2026-09-15 government announcement of an AI wildfire/smoke spread monitoring-and-prediction service that outputs resident evacuation routes AND suppression crew/equipment ingress routes. Covered by aitimes.kr, newspim, koit.co.kr, dailian, public25, anjunj, kodominnews. → `mois2026aievacroute` |
| 9 | 2026-09-19 | WebFetch (edaily) | `newsId=02981526642136776` | Verified: Ready / Set / Go three-stage system; max instantaneous wind speed 27.6 m/s and 8.2 km/h spread in the March 2025 Gyeongbuk fires; quote 「화선 도달거리가 5시간 이내로 예상된 지역은 '위험구역'으로, 8시간 이내인 경우는 '잠재적 위험구역'으로 설정」. No AI component in the 2025 evacuation rule. |
| 10 | 2026-09-19 | WebFetch (aitimes.kr) | `articleView.html?idxno=41932` | Verified quote: 「과거 산불 피해지역의 확산 자료에 기상·지형·연료 정보를 결합해 산불의 확산 방향과 속도를 분석한다. 연기 확산 경로까지 반영해 주민 대피경로와 진화 인력·장비의 투입 경로를 제시」. Status: 개발 중 (under development). |
| 11 | 2026-09-19 | WebFetch (newspim) | `view/20260915000178` | Independent corroboration of #10; explicitly "not yet deployed operationally"; no completion date given. |
| 12 | 2026-09-19 | WebSearch | `행정안전부 보도자료 2026 공공부문 AI 서비스 지원사업 산불 확산 예측 대피경로 4대 과제` | Fifth/sixth independent corroboration; names the KFS system 「AI 기반 산불·연무 확산 감시·예측」 and lists the four AI tasks. **Official MOIS press-release page itself not retrieved** — see Open questions. |

## Round 4 — Korean fuel, terrain and spread modelling (NOVELTY_STANDARD §4(a) evidence)

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 13 | 2026-09-19 | WebSearch | `국립산림과학원 산불확산예측시스템 연료모델 임상도 소나무 Rothermel 논문` | NIFoS 「AI 기반 산불확산예측시스템 사용자가이드」 catalogue entry (book.nifos.go.kr — HTTP 503 on fetch); KFS 「산불 제대로 알기」 booklet; KOSHAM/한국산림과학회지 leads. |
| 14 | 2026-09-19 | WebSearch | `"산불확산예측" 모델 검증 한국 연료모델 지표화 확산속도 한국산림과학회지` | 산불확산예측모델의 개발 (DBpia NODE09436466 — HTTP 503); 경사에 따른 산불의 확산속도 (ScienceON JAKO200833338361788); 산림 내 연료 특성 분석을 통한 산불 위험도 예측 (j-kosham). |
| 15 | 2026-09-19 | WebFetch (ScienceON) | `cn=JAKO200833338361788` | Verified: 안상현·신영철 (2008) 경사에 따른 산불의 확산속도 / *Spread Speed of Forest Fire based on Slope*, 한국방재학회논문집 8(4):75–79. Upslope spread 4.68× downslope at 30°. DOI not shown → UNVERIFIED. → `an2008slope` |
| 16 | 2026-09-19 | WebSearch | `임상도 기반 산불 연료모델 구축 소나무림 연료량 국립산림과학원 연구` | KCI 수관연료 수직분포모델 (Pinus densiflora, Gyeongbuk); DBpia 솎아베기에 따른 산불연료량과 수관화 위험도 변화 (고성 소나무림); j-kosham fuel-characteristics paper. |
| 17 | 2026-09-19 | WebFetch (KCI) | `artiId=ART002703652` | Verified: 이선주·권춘근·김성용 (2021), 한국농림기상학회지 23(1):46–54. Canopy bulk density ~1.6× higher in unmanaged *P. densiflora* stands. DOI not shown → UNVERIFIED. → `lee2021crownfuel` |
| 18 | 2026-09-19 | WebFetch (j-kosham) | `view.php?number=10401` | Verified: Lim & Chae (2022), *J. Korean Soc. Hazard Mitig.* 22(6):125–132, DOI 10.9798/KOSHAM.2022.22.6.125; 12 Gangwon sites; Van Wagner crown-fire criterion. → `lim2022fueldanger` |

## Round 5 — Korean fire-danger rating / occurrence models (Consensus, English)

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 19 | 2026-09-19 | Consensus | `Korea forest fire danger rating index prediction model national forest fire` | 10 returned, 8 Korea-specific: Choi 2025 (Land), Lee 2026 (Forests, KFDRI + human proximity), Han 2026 (Forests, KFDRS vs NFDRS/CFFDRS/EFFIS/AFDRS), Kang 2020 (Applied Sciences, HFRI), Won 2016, Lim 2025 (Forests, FWI), Jo 2023 (Remote Sensing, FLAM), Roh 2024 (Forests), Won 2012 (DWI). |
| 20 | 2026-09-19 | WebSearch | `국가산불위험예보시스템 산불위험지수 daily fire danger rating index Korea NIFoS` | Operational system confirmed: NIFoS 산림재난예측분석센터, statutory basis 산림보호법 제31조, index 1–100, daily/hourly, inputs = weather + terrain + 임상 (forest type). → `nifos2026kfdrs` |

## Round 6 — 2025–2026 separate sweep (the March 2025 Uiseong/Andong wave)

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 21 | 2026-09-19 | WebSearch | `2025 Uiseong Andong wildfire March 2025 Korea burned area fatalities study` | Event framing + figures (secondary press; superseded by KFS official table, query 27). |
| 22 | 2026-09-19 | WebSearch | `2025 의성 안동 산불 확산 분석 논문 2026 연구 대피` | Greenpeace Korea 「2025 영남 초대형 산불 실태조사 최종보고서」 (2026-03, NGO report — not peer-reviewed, not recorded as literature); 서울환경연합 2025 경북산불 피해확산 원인조사 연구 보고서; KFS 국가산불정보시스템. Evacuation rates quoted (Uiseong 87%, Andong 85%) — NGO source, **not** recorded as verified. |
| 23 | 2026-09-19 | WebSearch | `Korea wildfire 2025 Uiseong fire spread analysis remote sensing paper 2026 journal` | **HIGH VALUE**: Choi & Chae 2026 `Fire` 9(6):247 (ridge-line null-model benchmark, 118 Korean fires); Sung et al. 2025 *Korean J. Remote Sensing* 41(3) (geostationary detection latency, March 2025 fires); Heo et al. 2026 `Forests` 17(2):182 (XAI vulnerability, 2025 fire). |
| 24 | 2026-09-19 | WebSearch | `2026 Korea wildfire evacuation study Uiseong Gyeongbuk elderly residents warning response journal paper` | Park et al. 2025 `Forests` 16(9):1476 (1980–2024 drivers, WUI); Lim & Chae 2025 `Forests` 16(7):1058. **No peer-reviewed paper found that analyses evacuation *timing* in the 2025 Uiseong fires.** |
| 25 | 2026-09-19 | WebFetch (kjrs.org) | `doi=10.7780/kjrs.2025.41.3.6` | Verified: Sung et al. (2025) 41(3):565–580, OA. Mean detection delay AMI-LGBM 12.9 min, AHI-WLF 16.3, AMI-FF 18.2, MODIS-AF 210.1, VIIRS-AF 318.1 min; Uiseong 99,289 ha. → `sung2025geostationary` |

## Round 7 — Korean government technical documents and statistics

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 26 | 2026-09-19 | WebSearch | `산림청 산불통계연보 2024 산불발생 건수 피해면적 통계` | e-나라지표 indicator 1309 (source: 산림청「산불통계연보」); data.go.kr open dataset 산불통계데이터_20250911; 국가산불정보시스템 통계. |
| 27 | 2026-09-19 | WebFetch (KFS) | `center.forest.go.kr ... cmsId=FC_001157 (우리나라의 대형산불)` | **Official KFS major-fire table verified** (see review §e). 2000 East Coast 23,794 ha / 190 h; 2005 Yangyang 973 ha / 32 h; 2019 Goseong-Gangneung-Inje 2,872 ha / 51 h; 2022 Uljin-Samcheok 16,302 ha / 222 h; 2025 Uiseong-Andong-Cheongsong-Yeongyang-Yeongdeok 99,417 ha / 222 h. → `kfs2025majorfires` |
| 28 | 2026-09-19 | WebFetch (index.go.kr) | `EachDtlPageDetail.do?idx_cd=1309` | 2025: 459 fires, 105,099.44 ha; 10-yr means 529 fires / 14,471 ha; 99% of 2025 damage in Feb–May. Source attributed to 산림청 산불방지과. |
| 29 | 2026-09-19 | WebFetch (book.nifos.go.kr) | `library/10130/contents/7732481` | Catalogue record verified: 「(2025년) 산불통계 연보」, 산림청, 대전, 2026, 255 p. 발간등록번호 not in catalogue → UNVERIFIED. → `kfs2026statistics` |
| 30 | 2026-09-19 | WebSearch | `국립산림과학원 "산불통계연보" 발간 연보 보고서` | Confirms annual February publication, statutory basis 산림재난방지법 시행규칙 제19조제2항. 2018 edition PDF shows 발간등록번호 11-1400000-000424-10 (for the 2018 volume only). |
| 31 | 2026-09-19 | WebFetch (forest.go.kr) | `sb_all.pdf` (산불 제대로 알기) | **FAILED** — exceeded WebFetch 10 MB content limit. Not recorded. |
| 32 | 2026-09-19 | WebFetch (east.forest.go.kr) | `sb_7_06.pdf`, `sb_3_09.pdf` | **FAILED** — PDFs returned unparseable binary. Figures from these two leaflets are therefore NOT recorded; the KFS major-fire table (query 27) is used instead. |

## Round 8 — Korean assisted / vulnerable-population evacuation

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 33 | 2026-09-19 | WebSearch | `산불 대피 트리거 대피 시작 시점 결정 연구 고령자 농촌 마을 대피계획 한국` | Ready/Set/Go three-stage detail (정책주간지 공감); 한국농어민신문 one-year-after review noting evacuation-system blind spots for 고령자; MOIS/KFS 국민행동요령. |
| 34 | 2026-09-19 | WebSearch | `산불 재난취약계층 대피 마을 단위 대피계획 연구 한국방재학회 논문 고령자` | **HIGH VALUE**: ScienceON report TRKO201800042755 「산림재해 피해저감을 위한 대피 및 경계피난시스템 개발」; Seoul 「산불 취약 특수보호시설, 대피계획 수립 가이드라인」 (opengov page HTTP 503 — NOT recorded). |
| 35 | 2026-09-19 | WebFetch (ScienceON) | `selectPORSrchReport.do?cn=TRKO201800042755` | Verified: NIFoS for KFS, PI 윤호중, 2018. Develops a **smoke-dispersion-based evacuation-range model**, alert-evacuation priority selection, hazard-alert service for vulnerable residents, evacuation support measures for socially vulnerable groups. → `nifos2018evacsystem` |
| 36 | 2026-09-19 | WebFetch (Crossref) | `query.bibliographic=wildfire evacuation disaster vulnerable floating population Donghae` | An & Choi (2026), *Forum of Public Safety and Culture* 56:135–147, DOI 10.52902/kjsc.2026.56.135. → `an2026donghae` |
| 37 | 2026-09-19 | WebFetch (OpenAlex) | `works?filter=title_and_abstract.search:...,authorships.countries:KR,...evacuation` | 21 Korea-authored evacuation works returned — **all building/indoor/subway/LNG-terminal fire or disability egress, none wildfire**. Confirms how thin the Korean *wildfire* evacuation literature is. |
| 38 | 2026-09-19 | WebSearch | `Korea wildfire evacuation trigger buffer "trigger boundary" Cova Korean study 산불 대피 기준선` | **No Korean trigger-boundary paper found.** All trigger-buffer hits are Cova/Dennison/Larsen/Li/Mitchell (US/UK). Only Korean hit is Kwon 2025 (shelter siting, no trigger). |

## Round 9 — Bibliographic verification pass (Agent C role)

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 39 | 2026-09-19 | WebFetch (OpenAlex) | `works/doi:10.3390/systems13121125` | Kwon, Kim, Han (2025), `Systems` 13(12):1125, gold OA. |
| 40 | 2026-09-19 | WebFetch (OpenAlex) | `works/doi:10.3390/fire9060247` | Choi & Chae (2026), `Fire` 9(6):247, gold OA. Mean ridge enrichment 2.3 (combined) vs 1.5 (proximity only). |
| 41 | 2026-09-19 | WebFetch (OpenAlex) | `works/doi:10.3390/f17020182` | Heo, Ahn, Lee, Jung, Jang (2026), `Forests` 17(2):182, gold OA. |
| 42 | 2026-09-19 | WebFetch (OpenAlex) | `works/doi:10.52902/kjsc.2026.56.135` | An & Choi (2026), vol 56:135–147, closed access. (Both Crossref and OpenAlex additionally list "Korea Safety Culture Society" in the author field — recorded as a probable indexing artefact, not asserted as an author.) |
| 43 | 2026-09-19 | WebFetch (OpenAlex) | `title.search:Spatial Prediction of Forest Fire Occurrence Integrating Human Proximity` | Lee, Ahn, Im (2026), `Forests` 17(2):281, DOI 10.3390/f17020281. **Consensus had reported no page/DOI — corrected here.** |
| 44 | 2026-09-19 | WebFetch (OpenAlex) | `title.search:Comparative Review of Wildfire Danger Rating Systems Fuel Moisture` | Han, Heo, Lee, Jang, Jung, Ahn (2026), `Forests` 17(4):486, DOI 10.3390/f17040486. |
| 45 | 2026-09-19 | WebFetch (OpenAlex) | `title.search:Developing a New Hourly Forest Fire Risk Index Based on Catboost` | Kang, Jang, Im, Kwon, Kim (2020), `Applied Sciences` 10(22):8213, DOI 10.3390/app10228213. |
| 46 | 2026-09-19 | WebFetch (OpenAlex) | `title.search:Forest Fire Risk Prediction in South Korea Using Google Earth Engine` | Choi, Yun, Chae (2025), `Land` 14(6):1155, DOI 10.3390/land14061155. |
| 47 | 2026-09-19 | WebFetch (OpenAlex) | `title.search:Application of the Canadian Fire Weather Index ... South Korea` | Lim & Chae (2025), `Forests` 16(7):1058, DOI 10.3390/f16071058. |
| 48 | 2026-09-19 | WebFetch (OpenAlex) | `works/doi:10.3390/f16091476` | Park, Suh, Baek (2025), `Forests` 16(9):1476, gold OA. +1 m/s peak wind ⇒ ~+8.5 ha burned; +1% RH ⇒ ~−3 ha. |
| 49 | 2026-09-19 | WebFetch (OpenAlex) | `works/doi:10.7780/kjrs.2025.41.3.6` | Confirms Sung et al. 2025, 41(3):565–580, diamond OA, **language: English** (Korean-domiciled journal). |

---

## Queries that returned NOTHING usable (recorded because null results are part of the protocol)

| # | Date | Source | Query | Result |
|---|---|---|---|---|
| N1 | 2026-09-19 | WebSearch | `Korea wildfire evacuation trigger buffer "trigger boundary" Cova Korean study 산불 대피 기준선` | No Korean trigger-boundary / trigger-buffer study exists in the indexed literature. |
| N2 | 2026-09-19 | WebFetch (KCI) | KCI portal search for `산불 대피` | KCI's server-side search could not be driven through WebFetch (returned the unfiltered 2.4 M-record default listing). Korean-language coverage therefore rests on WebSearch + per-record fetches. **Gap: a proper KCI/RISS/DBpia keyword sweep is still owed.** |
| N3 | 2026-09-19 | WebSearch | `"Forum of Public Safety and Culture" 2026 wildfire evacuation Donghae ...` | English-language web search could not reach this Korean journal; resolved instead via Crossref (#36). |
| N4 | 2026-09-19 | WebSearch | `Korea ICT IoT AI wildfire detection system deployed Korea Forest Service ...` | Only generic international IoT/AI detection literature. **No evidence retrieved of a peer-reviewed description of a KFS-deployed IoT detection network.** |
| N5 | 2026-09-19 | WebFetch | `dbpia.co.kr ... NODE09436466` (산불확산예측모델의 개발) and `NODE11595160` | HTTP 503. Not recorded. Needs re-attempt. |
| N6 | 2026-09-19 | WebFetch | `opengov.seoul.go.kr/sanction/35360436` (산불 취약 특수보호시설 대피계획 수립 가이드라인) | HTTP 503. **Lead only — not recorded in metadata.** |

---

## RECALL_UNVERIFIED leads (training-memory only; NOT entered in metadata or notes)

These are search leads, not citations. Each must be retrieved before it may be cited.

- `RECALL_UNVERIFIED` — A NIFoS-developed operational wildfire spread prediction system
  (「산불확산예측시스템」) is widely referred to in Korean policy text as using a Rothermel-type
  surface-fire rate-of-spread formulation re-parameterised for Korean fuel types keyed to the
  임상도 forest-type map. The system's existence and its use of 기상·지형·연료 inputs **is**
  verified (queries 7, 9, 12, 13, 20); its internal *equations* are not. Do not attribute a
  Rothermel adaptation to NIFoS in writing until a primary technical document is retrieved.
- `RECALL_UNVERIFIED` — Korean fuel-model classification work associating 임상도 forest-type
  classes to Anderson/Scott-Burgan fuel models. Not retrieved.
- `RECALL_UNVERIFIED` — 「산불확산예측모델의 개발」 (DBpia NODE09436466) — 503; author/year unknown.

---

## Open questions carried out of this log

1. The **official MOIS press release** for the 2026-09-15 AI programme was not retrieved
   (only ≥6 independent news reports of it). Needed before the programme is cited in a paper.
2. The **NIFoS 「AI 기반 산불확산예측시스템 사용자가이드」** (book.nifos.go.kr/art.do/10130/contents/7732761)
   returned 503. This is the single most important document for determining whether the Korean
   operational spread model is Rothermel-derived and what its fuel classes are.
3. Whether the MOIS/KFS 5 h / 8 h thresholds were **derived** from an evacuation-time analysis or
   set administratively. The press coverage gives no derivation. NEEDS_FULL_TEXT.
4. A KCI/RISS/DBpia keyword sweep in Korean (`산불 대피`, `대피 시간`, `대피 경로`, `취약계층 대피`)
   was not completable through the available tools.
