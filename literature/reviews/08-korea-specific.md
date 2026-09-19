# Category 8 — Korea-Specific Wildfire Research (Korean and English)

**Author:** Agent A/C (Search Researcher + Verification Auditor)
**Date:** 2026-09-19
**Stance:** adversarial. This review exists to decide **WG-C-007** honestly, and to answer
fair judge question **Q7** ("isn't 'first in Korea' just a weak novelty claim?") before a
judge asks it.
**Search log:** `docs/search-logs/agent-korea.md` (49 logged queries + 6 logged null results).

**Evidence caveat.** Unless stated otherwise, items here were assessed at **evidence level
E2 (abstract or agency record retrieved; full text not read)**. MDPI (`www.mdpi.com`)
returns HTTP 403 and DBpia returns HTTP 503 to this agent, so all MDPI metadata was verified
through the **OpenAlex and Crossref APIs** rather than the publisher page. Every
`NEEDS_FULL_TEXT` below is a real gap.

**Publication-status caveat (binding).** Sections (a) and (b) are peer-reviewed literature.
**Section (c) is not.** NIFoS / KFS / MOIS documents are agency publications and are marked
`GOVERNMENT_REPORT` in their metadata. They may be cited as *evidence of operational
practice* and as *statistics of record*. They may never be described as peer-reviewed, and
their unvalidated thresholds may never be reported as findings.

---

## 0. The headline, stated first

Three things were found that a fair judge could use to end the Korean-novelty conversation:

1. **MOIS/KFS already operate a fire-arrival-time-based evacuation trigger with a separate,
   earlier trigger for vulnerable residents** — 5 hours and 8 hours before predicted fire-line
   arrival, adopted April 2025 (`mois2025evacuationstages`).
2. **The Korea Forest Service, under a MOIS-coordinated programme, is building an AI system
   that outputs resident evacuation routes *and inbound ingress routes for suppression
   personnel and equipment*** from a modelled fire and smoke field (announced 15 Sept 2026,
   `mois2026aievacroute`). The inbound leg is not unoccupied territory in Korea.
3. **A peer-reviewed wildfire evacuation-system design for a rural Korean county already
   exists** (`kwon2025koreaevac`, *Systems* 13(12):1125, Uiryeong County).

Against these, the honest verdict on WG-C-007 is in §(f): **WEAKENED**, admissible only via
NOVELTY_STANDARD §4(a)/(b), with candidate §4(a) evidence identified in §(g) but **not yet
demonstrated**.

---

## (a) Peer-reviewed Korean-language literature

Six items. All are genuine peer-reviewed journal articles in Korean journals; the Korean
title is the article's own, and English titles below are the journals' official English
titles, not translations by this agent.

| paper_id | Korean title | Journal | Year | What it does |
|---|---|---|---|---|
| `kwak2021evacroute` | 도시산불 대응을 위한 GIS 기반 주민최적대피경로설정 알고리즘 개발 | 한국방재학회논문집 21(6):63–70 | 2021 | GIS evacuation route enumeration (up to 15 routes/origin) for urban wildfire; hypothetical scenario |
| `gu2016spreadalgorithm` | 재난 재해 지역의 산불 확산경로와 이동속도 예측 알고리즘 | 한국정보통신학회논문지 20(8):1581–1586 | 2016 | Sensor-node-driven spread direction/speed prediction; abstract claims it could inform residents when evacuation must complete |
| `an2008slope` | 경사에 따른 산불의 확산속도 | 한국방재학회논문집 8(4):75–79 | 2008 | Experimental slope/rate-of-spread; upslope ≈ **4.68×** downslope at 30° |
| `lee2021crownfuel` | 수관연료 수직분포모델 개발을 통한 산불연료구조 분석 (경북 소나무림) | 한국농림기상학회지 23(1):46–54 | 2021 | *Pinus densiflora* crown fuel vertical distribution; canopy bulk density ≈ **1.6×** higher in unmanaged stands |
| `lim2022fueldanger` | 산림 내 연료 특성 분석을 통한 산불 위험도 예측 | 한국방재학회논문집 22(6):125–132 | 2022 | Field fuel loads at 12 Gangwon sites → fire intensity (kW/m) → 4-class danger via Van Wagner crown-fire criterion |
| `an2026donghae` | *(Korean original title `UNVERIFIED`)* — Analysis of Evacuation Behavior among Disaster-Vulnerable Groups… 2022 Donghae | Forum of Public Safety and Culture 56:135–147 | 2026 | Observed evacuation response from SKT floating-population data; **older adults had the lowest movement intensity** |

**Reading.** The Korean-language wildfire literature is strong on *fuel*, *danger rating*
and *spread*, and thin on *evacuation*. Of six items only two touch evacuation at all
(`kwak2021evacroute`, `an2026donghae`), and **neither computes a time**. `kwak2021evacroute`
gives routes under a static spread zone; `an2026donghae` measures behaviour after the fact.
DOIs for `an2008slope` and `lee2021crownfuel` are recorded as `UNVERIFIED` — they were not
shown in the KCI/ScienceON records and have not been guessed.

**Coverage gap, stated honestly.** KCI's server-side search could not be driven through the
available tools (log entry N2), and DBpia returned 503 (N5). Korean-language coverage here
rests on WebSearch discovery plus per-record verification. A proper KCI/RISS/DBpia keyword
sweep on 산불 대피 / 대피 시간 / 취약계층 대피 is **still owed** and could still surface a
killer.

---

## (b) Peer-reviewed English-language literature on Korean wildfire

Ten items. This literature is much larger than the Korean-language evacuation literature and
is overwhelmingly about **occurrence risk and danger rating**, not about people moving.

**Evacuation / people (1 item)**
- `kwon2025koreaevac` — Kwon, Kim & Han (2025), *Systems* 13(12):1125. MIP shelter siting
  + main/backup linkages for **Uiryeong County**, a rural Korean county, using a *static*
  terrain-derived risk index. **No time axis at all.** This is the closest peer-reviewed
  Korean prior art to WildfireGuardian's setting, and the reason "first Korean rural
  wildfire evacuation study" is a dead sentence.

**Fire behaviour / terrain (2 items)**
- `choi2026ridgeline` — Choi & Chae (2026), *Fire* 9(6):247. 118 Korean fire perimeters
  2018–2025 vs a ridge-line null model; combined proximity+alignment enrichment **2.3** vs
  **1.5** for proximity alone. An observational **benchmark for fire-spread modelling in
  Korea**.
- `park2025drivers` — Park, Suh & Baek (2025), *Forests* 16(9):1476. 905 Korean fires
  1980–2024: **+1 m/s peak wind ⇒ ≈ +8.5 ha burned; +1 % RH ⇒ ≈ −3 ha**; conifer dominance
  amplifies, broadleaf limits. R² 0.62–0.66.

**Detection / latency (1 item)**
- `sung2025geostationary` — Sung et al. (2025), *Korean J. Remote Sensing* 41(3):565–580
  (English-language article in a Korean journal). Mean detection delay **12.9 min**
  (GK-2A AMI LGBM), 16.3 (AHI WLF), 18.2 (AMI FF), **210.1** (MODIS AF), **318.1** (VIIRS
  AF). Uiseong detected in 22–36 min geostationary vs 93–196 min polar-orbiting.

**Occurrence risk / danger rating (6 items)** — none has any evacuation, timing or decision
content; they are inputs, not competitors.
- `heo2026vulnerability` — Heo et al. (2026), *Forests* 17(2):182. XAI susceptibility for
  the 2025 fire; high-susceptibility corridors coincide with high-elderly-share counties.
- `lee2026occurrence` — Lee, Ahn & Im (2026), *Forests* 17(2):281. RF ignition probability
  on Korea's east coast, proposed to run **alongside the operational KFDRI**.
- `han2026dangerrating` — Han et al. (2026), *Forests* 17(4):486. Comparative review placing
  **KFDRS** against NFDRS/CFFDRS/EFFIS/AFDRS.
- `kang2020hfri` — Kang et al. (2020), *Applied Sciences* 10(22):8213. Hourly 1 km CatBoost
  risk index, AUC 0.8434, benchmarked against Korea's operational DWI.
- `choi2025gee` — Choi, Yun & Chae (2025), *Land* 14(6):1155. Nationwide GEE/ML risk,
  XGBoost F1 0.511 / AUC 0.76.
- `lim2025fwi` — Lim & Chae (2025), *Forests* 16(7):1058. Canadian FWI transferred to Korea,
  2004–2023.

**Reading.** In the English-language Korean wildfire literature, the ratio is roughly
**9 : 1 risk-mapping to evacuation**. Nobody in it computes an evacuation time.

---

## (c) Government / agency technical documents — **NOT PEER-REVIEWED**

> Everything in this section is an agency publication. None of it has been peer reviewed.
> None of the numerical thresholds below has a published derivation or validation.

| paper_id | Document | Body | Year | Status |
|---|---|---|---|---|
| `mois2025evacuationstages` | 「정부, 초고속 산불 대비 주민대피 체계 개선키로」 press release | MOIS + KFS | 2025-04-16 | GOVERNMENT_REPORT |
| `mois2026aievacroute` | 「AI 기반 산불·연무 확산 감시·예측」 programme | KFS under MOIS AI programme | 2026-09-15 | GOVERNMENT_REPORT (press coverage only) |
| `nifos2018evacsystem` | 「산림재해 피해저감을 위한 대피 및 경계피난시스템 개발」 (TRKO201800042755) | NIFoS for KFS, PI 윤호중 | 2018 | GOVERNMENT_REPORT |
| `nifos2026kfdrs` | 국가산불위험예보시스템 (operational KFDRS) | NIFoS 산림재난예측분석센터 | ongoing | GOVERNMENT_REPORT / operational system |
| `kfs2026statistics` | 「(2025년) 산불통계 연보」, 255 p., 대전 | KFS | 2026 | GOVERNMENT_REPORT |
| `kfs2025majorfires` | 「우리나라의 대형산불」 web table | KFS | 2025 | GOVERNMENT_REPORT |

**`mois2025evacuationstages` — the single most important document in this category.**
Adopted after the March 2025 Gyeongbuk fires. The national spread-prediction system
(산불확산예측시스템) was changed to ingest **maximum instantaneous wind speed** as well as
mean wind, and its predicted fire-line arrival time now partitions space into:

- **위험구역** (danger zone), arrival **≤ 5 h** → stage **Go**: evacuation order now;
- **잠재적 위험구역** (potential danger zone), arrival **≤ 8 h** → stage **Set**: residents
  prepare, and **안전취약계층 (vulnerable groups, e.g. 고령자) evacuate in advance (사전 대피)**;
- stage **Ready**: a fire in a neighbouring province; be alert.

> 「화선 도달거리가 5시간 이내로 예상된 지역은 '위험구역'으로, 8시간 이내인 경우는
> '잠재적 위험구역'으로 설정」
> *[translation]* "Areas where the fire line is predicted to arrive within 5 hours are set
> as 'danger zones'; within 8 hours, as 'potential danger zones'."

This is a **fixed-lead-time trigger against a deterministic modelled arrival time**, with a
**3-hour differential granted to people who move slowly**. There is no published derivation
of 5 h or 8 h, no uncertainty treatment, no household or facility resolution, and no
responder. It is exactly the kind of tuned-but-unvalidated positional/temporal rule that
WG-C-006 says must be the comparator.

**`nifos2018evacsystem`** develops an evacuation **range** model from wildfire **smoke**
dispersion, a warning-evacuation priority ranking, a hazard-alert service for vulnerable
residents, and evacuation support measures for socially vulnerable groups. Range, not time;
smoke, not fire front.

**`nifos2026kfdrs`** issues a 1–100 danger index daily/hourly from weather + terrain +
forest type (임상), under 산림보호법 제31조. Independently characterised by `han2026dangerrating`
as daily, district-resolution, empirical, weather-driven, with **no live-fuel-moisture
model and no AI-augmented hybrid component**.

---

## (d) Operational systems actually deployed in Korea

| System | Body | Status as of 2026-09-19 | Evacuation timing? | AI? |
|---|---|---|---|---|
| 국가산불위험예보시스템 (KFDRS) | NIFoS | **Deployed**, statutory | No — ignition danger only | No (empirical/weather-driven) |
| 산불확산예측시스템 (spread prediction) | KFS/NIFoS | **Deployed**; upgraded April 2025 to use max instantaneous wind | Yes — supplies the arrival time behind the 5 h / 8 h zones | Not verified. A NIFoS 「AI 기반 산불확산예측시스템 사용자가이드」 exists in the NIFoS library catalogue but the page returned HTTP 503 |
| Ready / Set / Go 주민대피 3단계 | MOIS + KFS | **In force since April 2025** | **Yes** — 5 h general, 8 h vulnerable | No AI component reported |
| 「AI 기반 산불·연무 확산 감시·예측」 | KFS under MOIS AI programme | **Under development (개발 중), not deployed** | Routes, not times | **Yes** |
| 국가산불정보시스템 (fd.forest.go.kr) | KFS | Deployed | No | No |

**Note on the spread model's internals.** Korean policy text describes the operational
spread system as combining 기상·지형·연료 (weather, terrain, fuel). Whether it is a
Rothermel-derived surface rate-of-spread formulation re-parameterised for Korean fuel classes
keyed to the 임상도 forest-type map is **`RECALL_UNVERIFIED`** — plausible, widely assumed,
and **not retrieved**. Do not assert it. The NIFoS user guide (Open question 2 in the search
log) is the document that would settle it.

---

## (e) Major Korean wildfire events — verified statistics only

Source of record: KFS 「우리나라의 대형산불」 (`kfs2025majorfires`), fetched 2026-09-19.
Burned area and duration below are **as published by KFS**. Damage figures are omitted here
because the units on the source table were not independently confirmed.

| Year | Event | Duration | Burned area (ha) |
|---|---|---|---|
| 2000 | East Coast (Gangneung, Goseong, Donghae, Sokcho) | 190 h | **23,794** |
| 2002 | Cheongyang | 28 h | 3,095 |
| 2003 | Hongseong | 53 h | 1,337 |
| 2005 | **Yangyang** | 32 h | **973** |
| 2017 | Gangneung, Samcheok | 71 h | 1,017 |
| 2019 | **Goseong, Gangneung, Inje** | 51 h | **2,872** |
| 2020 | Andong | 74 h | 1,944 |
| 2022 | **Uljin, Samcheok** | 222 h | **16,302** |
| 2022 | Gangneung Okgye | 155 h | 4,190 |
| 2022 | Yanggu | 53 h | 716 |
| 2022 | Hapcheon | 75 h | 814 |
| 2023 | Geumsan | 52 h | 889 |
| 2025 | Sancheong, Hadong | 292 h | 3,397 |
| 2025 | Ulju | 128 h | 1,190 |
| 2025 | **Uiseong, Andong, Cheongsong, Yeongyang, Yeongdeok** | 222 h | **99,417** |

**National totals for 2025** (e-나라지표 indicator 1309, sourced to KFS 산불방지과):
**459 fires, 105,099.44 ha**, against 10-year means of **529 fires / 14,471 ha**; ~99 % of
2025 damage occurred Feb–May.

**Cross-source discrepancy, recorded rather than smoothed.** The Uiseong complex is given as
**99,417 ha** by KFS and as **99,289 ha** by `sung2025geostationary`. A widely circulated
press figure of ~104,788 ha refers to the **whole March–May 2025 national outbreak**, not the
Uiseong complex; an NGO report circulates ~116,000 ha. Use **99,417 ha (KFS)** for the
Uiseong complex and **105,099 ha (KFS via e-나라지표)** for the 2025 national total, and say
which is which.

**Deliberately NOT recorded as verified:** the 2019 figure of 1,289 displaced persons /
566 households (secondary press); the 2025 death toll (press figures ranged 18→32 during the
event and were not confirmed from a KFS or MOIS source in this session); evacuation-compliance
rates of 87 % Uiseong / 85 % Andong (NGO report, `RECALL`-grade). **Do not put these on a
poster.**

**Absence worth naming:** two KFS leaflets that should contain casualty and evacuee counts
(`sb_7_06.pdf`, `sb_3_09.pdf`) returned unparseable binary, and `sb_all.pdf` exceeded the
fetch size limit (log entries 31–32). Korean **human-impact** statistics are therefore the
weakest verified area of this review.

---

## (f) Verdict on WG-C-007 against NOVELTY_STANDARD §4

> **WG-C-007:** "We provide wildfire evacuation-timing analysis for the Korean setting."
> Prior status: `UNKNOWN`. Novelty type N4 (application).

### Recommended status: **WEAKENED**

Not `OCCUPIED`, not `REJECTED`, not `SUPPORTED_CANDIDATE`. Reasoning, gate by gate:

**§4(a) — "a Korean-specific condition *changes the answer*, and we show the change."**
**NOT YET DEMONSTRATED.** Candidate evidence exists and is unusually good (see §(g)), but
NOVELTY_STANDARD §4 requires the change to be *shown*, not the inputs to be *different*.
Nothing in this repository yet shows a Korean condition flipping a conclusion. Until an
experiment does, §4(a) is unavailable.

**§4(b) — "the published method *fails* on Korean data in a way we document."**
**NOT YET DEMONSTRATED, but the cleanest route.** Two documented Korean failure surfaces now
exist that a US/European method can be run against:
1. `choi2026ridgeline` gives a quantified Korean ridge-alignment signal (enrichment 2.3)
   that an imported spread model either reproduces or does not — a falsifiable target.
2. `han2026dangerrating` states, in a peer-reviewed venue, that KFDRS lacks live-fuel-moisture
   modelling and runs at district/daily resolution — an operational limitation someone else
   has already documented, so we are not asserting it ourselves.
Neither has yet been turned into a demonstrated failure by WildfireGuardian. `NEEDS_FULL_TEXT`
on both, plus an actual experiment.

**§4(c) — "no comparable analysis exists anywhere, and Korea is incidental."**
**This is the gate the program should actually walk through.** If the inbound-inclusive
dispatch deadline (WG-C-003) survives Agent B's assault, then the novelty is **N2 (quantity)**
and Korea is *where we did it*, not *why it matters*. In that case WG-C-007 should be
**absorbed into WG-C-003 and demoted to a setting statement**, exactly as §4(c) instructs.

### What must never be said
- ✗ "First wildfire evacuation study in Korea." — `kwak2021evacroute` (2021),
  `kwon2025koreaevac` (2025), `nifos2018evacsystem` (2018).
- ✗ "First to use modelled fire spread for evacuation decisions in Korea." —
  `mois2025evacuationstages` does this nationally and operationally; `mois2026aievacroute`
  extends it to routes.
- ✗ "Korea has no evacuation timing rule." — 5 h / 8 h, in force since April 2025.
- ✗ "Korea does not consider residents who cannot self-evacuate." — the 8-hour
  사전 대피 provision, `nifos2018evacsystem`, and `an2026donghae` all do.
- ✗ "No one routes responders inbound toward a Korean fire." — `mois2026aievacroute`.

### What can be said, and is defensible
> "Korea already sets wildfire evacuation timing: since April 2025, MOIS and the Korea Forest
> Service order evacuation when a modelled fire line is 5 hours away, and 8 hours away for
> vulnerable residents. Those are fixed lead times against a single deterministic forecast,
> with no published derivation and no uncertainty treatment. We do not claim to be first in
> Korea. We treat the 5 h / 8 h rule as our comparator, and we ask a different question:
> not when the resident should leave, but the latest moment a responder can depart and still
> complete the round trip that brings a non-self-evacuating resident out."

That sentence survives Q7 because it concedes the geography and relocates the claim onto the
quantity.

### Consequential edits recommended (for whoever holds the registry)
- `WG-C-007`: `UNKNOWN` → **`WEAKENED`**; threat papers `mois2025evacuationstages`,
  `mois2026aievacroute`, `kwon2025koreaevac`, `kwak2021evacroute`, `nifos2018evacsystem`;
  add gate note "admissible only via §4(b) or by absorption into WG-C-003 under §4(c)."
- `WG-C-006`: the tuned comparator is no longer hypothetical — it is the MOIS 5 h / 8 h rule.
  This *strengthens* WG-C-006's rationale and raises the bar for WG-C-002.
- `WG-C-005`: Korean empirical support now exists (`an2026donghae`); the claim remains a
  framing, not a contribution, as the registry already notes.
- `WG-C-012`: `sung2025geostationary` supplies Korean latency numbers (12.9–318.1 min) that
  must be cited, not re-derived.

---

## (g) Korean-specific evidence that Korean conditions change evacuation-timing answers

This is the §4(a) shopping list. Each row is **retrieved evidence**; none of it yet
constitutes a demonstrated change of answer.

| Korean condition | Verified evidence | Why it could change an evacuation-timing answer | Status |
|---|---|---|---|
| **Steep slope** | `an2008slope`: upslope spread ≈ **4.68×** downslope at 30° | Trigger-boundary geometry derived on gentler terrain under-buffers the upslope direction; lead time collapses asymmetrically around a village | Input only — no timing experiment yet |
| **Ridge-channelled spread** | `choi2026ridgeline`: 118 Korean fires, combined ridge enrichment **2.3** vs **1.5** proximity-only | Arrival-time fields in Korea are directionally structured by ridges; a model that gets burned *area* right can get arrival *direction and time* wrong — which is what a deadline depends on | **Best §4(b) candidate.** Needs the experiment |
| **Gust-driven, not mean-wind-driven** | `park2025drivers`: +1 m/s **peak** wind ⇒ ≈ +8.5 ha; MOIS itself switched the operational system to **max instantaneous wind** in April 2025 after 27.6 m/s gusts drove 8.2 km/h spread | If Korean spread is gust-governed, a mean-wind forecast has systematically worse *effective* skill at exactly the lead times that matter — a direct WG-C-002/WG-C-012 mechanism | Strong, and unusually well corroborated (peer-reviewed + operational policy change) |
| **Dense *Pinus densiflora*, unmanaged stands** | `lee2021crownfuel`: canopy bulk density ≈ **1.6×** higher unmanaged; `lim2022fueldanger`: Van Wagner crown-fire transition at 12 Gangwon sites; `park2025drivers`: conifer dominance amplifies, broadleaf limits | Crown-fire transition thresholds shift the arrival-time distribution's tail, which is what a *quantile-based* deadline is sensitive to | Input only |
| **Ageing rural population** | `an2026donghae`: older adults had the **lowest movement intensity** under identical warning content, measured from real mobility data; `heo2026vulnerability`: high-susceptibility corridors coincide with high-elderly-share counties | The assisted-evacuation premise is a measured Korean fact, not a transferred assumption — and the movement-intensity deficit is a *speed* term in a round-trip feasibility calculation | Premise support, not yet a changed answer |
| **Observation latency** | `sung2025geostationary`: 12.9–18.2 min geostationary, 210–318 min polar-orbiting; Uiseong 22–36 vs 93–196 min | A 5-hour operational lead time is really ~4.7 h at best and ~2.7 h at worst once detection latency is charged against it. If the dispatch deadline sits inside that gap, latency *decides* the outcome — precisely WG-C-012 | **Best quantitative §4(a) candidate**: Korean numbers, Korean policy budget, arithmetic not yet done by anyone |
| **Narrow mountain road networks** | **No verified Korean evidence found.** `kwon2025koreaevac` models link failure but publishes no road-geometry statistics | Would matter for ingress against outbound traffic | **GAP.** Do not assert Korean road narrowness without a source |

### The single strongest §4(a) argument available
Combine rows 3 and 6: Korea's operational lead times (5 h / 8 h) are set against a
**gust-driven** spread process using a forecast whose usable horizon is already reduced by
**13–320 minutes of detection latency**. If the assisted-evacuation round trip — ingress +
pickup dwell + egress — is long relative to what remains, then in the Korean setting the
binding constraint is *latency*, not *distance*, and the answer to "when do we act" changes
in a way it would not in a setting with gentler terrain, mean-wind-dominated spread and
faster-moving residents. That is a §4(a) argument with three verified Korean numbers in it.

**It is an argument, not a result.** It becomes §4(a)-admissible only when an experiment in
this program *shows the change*. Until then WG-C-007 stays `WEAKENED` and the honest fair
answer to Q7 is the paragraph in §(f).

---

## Open questions carried forward

1. **Primary MOIS source** for `mois2026aievacroute` not retrieved (six independent news
   reports only). Must be obtained before it appears in a paper.
2. **NIFoS 「AI 기반 산불확산예측시스템 사용자가이드」** (HTTP 503). Would settle whether the
   operational Korean spread model is Rothermel-derived and what its 임상도-keyed fuel
   classes are. Currently `RECALL_UNVERIFIED` — must not be asserted.
3. **Derivation of 5 h / 8 h** — analysis or administrative choice? `NEEDS_FULL_TEXT`.
   If administrative, WG-C-006's "tuned comparator" bar means we must *tune it ourselves*
   before beating it; beating an untuned administrative number is not a result.
4. **KCI / RISS / DBpia Korean-language keyword sweep** not completable with available tools.
   The largest remaining risk of a missed killer paper lives here.
5. **Korean human-impact statistics** (deaths, evacuees, assisted evacuations) not verified
   from an agency source. Needed for WG-C-005's motivation section.
6. **Korean road-geometry evidence** — no source found. Named as a gap above.
7. `an2026donghae` **full text** — the abstract withholds the actual response-time values,
   which are the numbers WG-C-005 would want.
