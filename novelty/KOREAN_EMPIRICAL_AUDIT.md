# KOREAN_EMPIRICAL_AUDIT.md — is a specific Korean empirical result still available?

**Author:** Agent B — Prior-Art Adversary
**Date:** 2026-09-20
**Query log and access-failure table:** `docs/search-logs/agent-dbd-korea.md`

---

## 0. What is and is not being asked

**Korea is not in question.** `NOVELTY_STANDARD.md` §4 rules out geography as novelty, and
Korean wildfire evacuation optimisation already exists (`kwon2025koreaevac`), as does Korean
wildfire evacuation mapping (`kim2011evacmap`, 2011; `kwak2021evacroute`, 2021) and a
nationwide operational fire-relative evacuation-timing rule (`mois2025evacuationstages`, 5 h /
8 h, in force since April 2025). Nobody may say "first in Korea" about any of those.

The only question here is narrower: **does a specific Korean empirical result remain
available** — a number, for this setting, that nobody has published. Under
`NOVELTY_STANDARD.md` §8 that is the `empirical` axis, and an empirical contribution is a
legitimate contribution.

**Evidence grade for this whole file.** Everything is `ABSTRACT_VERIFIED` or below unless
stated. No Korean full text was read. Every "not found" below is a *search result*, never a
finding (`NOVELTY_STANDARD.md` §3.2).

---

## Q1 — Household- or village-level **dispatch-by maps** in Korea

**Answer: not found. The map *product* at village scale is occupied; the dispatch-by
*content* was not found.**

**What exists.**

| Record | What it is | Unit | Output |
|---|---|---|---|
| `kim2011evacmap` **(new record)** | 「산불대피지도 작성 알고리즘에 관한 연구」, 김명훈·이병두·김응식, 한국화재소방학회 학술대회 논문집 2011.11a: 289–293. **CONFERENCE PROCEEDINGS — not peer-reviewed.** | adjacent villages (인접 마을) | evacuation **routes** on a map, set "according to the wildfire's progression path and spread" |
| `kwak2021evacroute` | GIS route enumeration, up to 15 routes per origin | resident origin points | routes |
| `kwon2025koreaevac` | MIP shelter siting + backup linkages, Uiryeong County | county / shelter network | a network plan, no time axis |
| `mois2025evacuationstages` | **GOVERNMENT_REPORT.** Predicted fire-line arrival ≤5 h ⇒ 위험구역; ≤8 h ⇒ 잠재적 위험구역 | zone | an act-by rule over Korean geometry, operationally in force |
| `nifos2018evacsystem` | **GOVERNMENT_REPORT.** Evacuation **range** from smoke dispersion | area | range, not time |
| NIFoS TRKO201600011244, 「산불지도 작성 알고리즘 개발 및 제작기법 연구」, PI 이병두, 2015. **GOVERNMENT_REPORT.** | wildfire thematic-map algorithms for prevention/suppression/spread/recovery | unspecified | the ScienceON record's abstract does **not** mention 대피지도; no time computed |

**The 2011 abstract, verbatim** (retrieved from the OpenAlex record, not translated by this
agent except where marked):

> 「대형 산불이 발생했을 경우 인접 마을 등에 대한 피난 연구는 국내에서 아직까지 이루어지지 않고
> 있으며 대부분의 대피 대상자들이 재해 약자들로 구성되어있어 산불 대피에 관한 연구가 필요한
> 실정이다. 이에 본 연구에서는 산불 대피지도 알고리즘을 개발하여 산불의 진행경로 및 확산에 따른
> 적정한 대피경로를 제시함으로서 인적 피해를 저감하는 데 그 목적이 있다.」

*[translation]* "When a large wildfire occurs, evacuation research for adjacent villages and
the like has not yet been carried out domestically, and most of those to be evacuated consist
of disaster-vulnerable people, so research on wildfire evacuation is needed. This study
therefore develops a wildfire evacuation-map algorithm to present appropriate evacuation
routes according to the wildfire's progression path and spread, with the aim of reducing human
casualties."

**Why this matters more than its venue suggests.** Korea's wildfire-evacuation-map lineage
begins in 2011, is village-scale, is explicitly motivated by 재해 약자, and is already driven by
the fire's progression. Three sentences WildfireGuardian might have used are therefore dead:
"the Korean wildfire evacuation map does not exist", "nobody in Korea maps evacuation against
the fire's spread direction", and "Korean wildfire evacuation work ignores vulnerable
residents".

**What is still available.** A map whose cell value is a **time** — a latest responder
departure instant — rather than a route or a zone. Nothing retrieved computes that.
**Empirical axis: PLAUSIBLE. Operational-artifact axis: PLAUSIBLE.**

**Searched:** KoreaScience keyword search (산불 대피, 산불대피지도, 대피 소요시간, 산불 취약계층,
산불 확산 예측); OpenAlex `language:ko` sweep of **all 406** Korean-language records matching 산불,
grepped for 대피/피난/출동/골든/취약/고령/주민; KCI and ScienceON record pages; WebSearch in Korean.
**Not searched:** RISS, DBpia (503), KCI keyword search (undrivable — see below), NDSL,
국립산림과학원 연구보고 series beyond two reports.

---

## Q2 — **Assisted-evacuation deadlines** in Korea

**Answer: an operational deadline exists and is a government rule; no peer-reviewed Korean
derivation of one was found.**

**Occupied, operationally.** `mois2025evacuationstages` directs 안전취약계층 (e.g. 고령자) to
evacuate **in advance (사전 대피)** at the 8-hour predicted-arrival boundary, three hours earlier
than the general population's 5-hour boundary. That is, functionally, an assisted/vulnerable
evacuation deadline for the whole country, in force since April 2025. Anyone who says "Korea
has no assisted-evacuation deadline" is wrong.

**Not occupied, scientifically.** No published derivation of 5 h or 8 h was found; no Korean
peer-reviewed work computes a deadline for moving a person who cannot self-evacuate.
`an2026donghae` measures **observed** evacuation response and finds older adults had the lowest
movement intensity — behaviour after the fact, not a deadline. `nifos2018evacsystem` produces a
range, not a time.

**The consequence the program must accept.** `WG-C-006` requires a *tuned* comparator. The
5 h / 8 h rule is untuned and undocumented, so beating it is not a result
(`docs/CURRENT_THESIS.md`, RQ1 comparator clause). It must be tuned by us before it is beaten.

**Still available:** a derivation — what lead time the 8-hour rule *should* be for an assisted
round trip, and how far the answer is from 8 h. **Empirical axis: PLAUSIBLE.**

---

## Q3 — **Responder staging deadlines** under wildfire (Korea)

**Answer: not found for wildfire. A Korean fire-service response-time literature exists and
must be cited rather than re-derived.**

Retrieved as KoreaScience search-result titles on 소방 출동 시간 (29 results; **titles and
journals only — no record-level verification, no authors confirmed, treat as leads**):

- "An Analysis of Fire Area in Jinju City Based on Fire Mobilization Time", *Journal of Korean
  Society for Geospatial Information Science*, 2012
- "Effect Analysis on Emergency Vehicle Priority System for Securing Golden Time", *Fire Science
  and Engineering*, 2019
- "Deriving the Priority of Emergency Vehicle Dispatch Delay Factors Using Spatial Regression
  Analysis", *Journal of Cadastre & Land Information*, 2023
- "Complex Disaster Risk Prediction and Fire Resource Allocation Using Rainfall, Fire Service,
  and Social Vulnerability Data", *Journal of the Society of Disaster Information*, 2025
- "A Study on the Effect of Road Requirements at Fire Point on Fire Response", *Journal of the
  Society of Disaster Information*, 2026

All of these are **urban fire / EMS response-time and golden-time** work. None is wildfire.
None computes a *deadline* — they compute coverage, delay factors and priority.

**Government-side occupancy of the ingress leg.** `mois2026aievacroute` (GOVERNMENT_REPORT,
announced 2026-09) outputs 진화 인력·장비의 투입 경로 — ingress routes for suppression personnel
and equipment. Routes, under development, not deployed, and not a deadline. "No one routes
responders inbound in Korea" remains a forbidden sentence.

**Still available:** a latest-departure instant for a Korean wildfire assisted-evacuation
mission. **Empirical axis: PLAUSIBLE**, conditional on the WG-DBD-3 residue in
`DBD_DECOMPOSITION.md` surviving — the *quantity* is occupied outside Korea, so Korea cannot
rescue it; Korea can only supply the numbers.

**Caveat that weakens this answer.** A wildfire responder-dispatch study could sit in
소방방재 / 산림 technical report series that OpenAlex does not index and that RISS and DBpia would
surface. Both were unreachable. This is the single weakest "not found" in this file.

---

## Q4 — **Forecast skill or latency requirements** for Korean evacuation decisions

**Answer: not found. Korean latency *measurements* exist; no Korean *requirement* does.**

- `sung2025geostationary` gives Korean detection latencies — mean 12.9 min (GK-2A AMI LGBM),
  16.3 (AHI WLF), 18.2 (AMI FF), **210.1** (MODIS AF), **318.1** (VIIRS AF); Uiseong detected in
  22–36 min geostationary vs 93–196 min polar-orbiting. These are numbers to cite, not to
  re-derive.
- A KoreaScience sweep of 산불 확산 예측 (33 results) returned Korean spread-prediction work from
  1998 to 2025 — spread programs, wind-field studies, a DQN spread model (한국정보통신학회논문지,
  2025), `gu2016spreadalgorithm` — and **none** of the retrieved titles addresses prediction
  delay/latency or evacuation decision timing.
- The operational Korean spread system's skill is not published in any record retrieved here.
  Whether it is Rothermel-derived remains `RECALL_UNVERIFIED` (`literature/reviews/08`, §(d)).

**Still available:** the requirement itself — what skill and what latency the Korean 5 h / 8 h
budget actually demands. **Empirical axis: PLAUSIBLE**, but note that the *method* for turning
skill into a decision-quality requirement is occupied generically (`regnier2008public`) and in
wildfire (`ardid2026forecastvalue`), so this is Korean numbers inside an occupied frame — N4
bundled onto N2, not N2 itself.

---

## Q5 — Comparison of **observation availability** with **evacuation-option expiry**

**Answer: not found anywhere, in Korean or English, in this or the previous Korean sweep.**

The comparison is arithmetic nobody appears to have done: a 5-hour operational lead time is
~4.7 h at best and ~2.7 h at worst once `sung2025geostationary`'s detection latency is charged
against it, and if the assisted round trip is long relative to what remains, latency — not
distance — decides the outcome. `literature/reviews/08` §(g) already identified this as the
best quantitative §4(a) candidate; this agent searched for someone who had done it and did not
find them.

**Searches run:** 산불 확산 예측 지연; 산불 대피 골든타임; detection-latency-versus-lead-time
phrasings in English; the OpenAlex `language:ko` 산불 sweep. **Nothing matched.**

**Still available: yes — and this is the strongest remaining Korean empirical item**, because
(i) all three input numbers are already published by other people, (ii) the policy budget is a
government rule rather than our assumption, and (iii) the result is a *comparison*, which is
the one thing on this list that cannot be pre-empted by a routing paper.
**Empirical axis: PLAUSIBLE. Concept axis: WEAKENED** — `chang2026multiscale` treats alert
latency as decision-relevant in wildfire evacuation already, and `bischiniotis2019tradeoffs`
and `lopez2020bridging` own lead-time-as-a-variable. Say "we do the Korean arithmetic", never
"we discovered that latency matters".

---

## 1. Summary

| # | Korean empirical question | Available? | Blocking caveat |
|---|---|---|---|
| Q1 | household/village dispatch-by **maps** | **Yes**, as an artifact — the map product and village unit are occupied since 2011, the *time-valued* cell is not | RISS/DBpia unsearched |
| Q2 | assisted-evacuation **deadlines** | **Only as a derivation** — the deadline itself is a government rule (8 h 사전 대피) | the rule must be *tuned* before it is beaten |
| Q3 | responder **staging deadlines** under wildfire | **Yes**, but it inherits WG-DBD-3's occupancy — Korea supplies numbers, not novelty | weakest "not found"; Korean agency report series unsearched |
| Q4 | forecast **skill/latency requirements** | **Yes**, as Korean numbers inside an occupied frame | N4 on N2; do not oversell |
| Q5 | observation availability vs **option expiry** | **Yes — strongest remaining item** | concept axis already WEAKENED by `chang2026multiscale` |

**Verdict on WG-C-007: unchanged at `WEAKENED`.** Nothing found here moves it up, and
`kim2011evacmap` moves the Korean occupancy *earlier* by a decade. The Korean contribution that
survives is empirical and artifact-shaped (Q1 + Q5), not conceptual, and it must be described
that way.
