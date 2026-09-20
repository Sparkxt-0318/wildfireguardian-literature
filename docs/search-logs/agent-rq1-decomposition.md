# Search Log — Agent C + B (RQ1 Decomposition + Ardid Full Text)

**Agent role:** C (Verification / Citation Auditor) + B (Prior-Art Adversary)
**Domain:** Category 4 (forecast value), re-opened at component level
**Claims attacked:** WG-C-002, WG-C-006, WG-C-012, WG-C-014
**Components scored:** WG-FV-1 … WG-FV-7, WG-COMB-1
**All searches run:** 2026-09-20
**Deliverables:** `literature/reviews/fulltext-ardid2026.md`,
`novelty/RQ1_DECOMPOSITION.md`, 2 new metadata + 2 new notes, this log.

**Sources used:** WebFetch (publisher HTML), WebSearch (general web, incl. one
Korean-language pass), alphaXiv `discover_papers` and `get_paper_content`,
Crossref REST API via curl, OpenAlex REST API via curl, `curl` direct.

**Sources UNAVAILABLE today:** **Consensus — quota exhausted, 30/30 used this
month, resets 1 October 2026.** Error returned verbatim on the first attempt.
This is the second consecutive agent blocked by it (see
`agent-forecast-voi.md`, "quota exhausted after 6"). No peer-reviewed-corpus
query could be run. **Every null in this log is therefore at best S1 for the
external pass**, and the affected component scores say so.

---

## A. Full-text acquisition — `ardid2026forecastvalue`

| # | Target | Method | Result |
|---|---|---|---|
| A.1 | `https://doi.org/10.1071/WF25221` | WebFetch | HTTP 302 → ConnectSci article URL. Redirect not auto-followed. |
| A.2 | ConnectSci article page | WebFetch | **SUCCESS.** Open Access CC BY-NC-ND 4.0. Full section-heading list retrieved. |
| A.3 | Same URL | `curl` (browser UA) | **HTTP 403**, 5,875 bytes (Cloudflare). |
| A.4 | `api.openalex.org/works/doi:10.1071/WF25221` | curl | OA hybrid, `cc-by-nc-nd`, `publishedVersion`, `any_repository_has_fulltext: false`. Second location found: UC repository `hdl.handle.net/10092/109982`. |
| A.5 | `hdl.handle.net/10092/109982` | curl | **HTTP 403** → `ir.canterbury.ac.nz`, Cloudflare block page. |
| A.6 | `ir.canterbury.ac.nz/handle/10092/109982` | WebFetch | **HTTP 403.** |
| A.7 | `www.publish.csiro.au/WF/WF25221` | WebFetch | HTTP 301 back to the same ConnectSci host. Not an independent rendering. |
| A.8 | Preprint / repository sweep | WebSearch | No arXiv / EarthArXiv / SSRN version. Surfaced the precursor `10.1071/WF24113` (already a logged lead). |

**Outcome: one rendering only.** Evidence level capped at **E3**; no number from
this paper is citable as a WildfireGuardian figure until a second rendering
exists (`docs/EVIDENCE_LEVELS.md` rule 3).

### A.9 Anti-fabrication controls (mandated by the brief)

The project previously had a summarising fetch of a binary PDF return invented
statistics. Controls run against the HTML rendering, and results:

| Control | Design | Result |
|---|---|---|
| Negative-control term sweep | PRESENT/ABSENT + quote for 11 terms | 10 ABSENT (`latency`, `lead time`, `delay`, `timeliness`, `evacuation`, `trigger boundary`, `buffer`, `OSSE`, `synthetic`, `perturb`), 1 PRESENT with in-context quote (`noise`). **Passed.** |
| False-premise trap | Asked it to quote "the Korean case study" and "the latest-safe dispatch time for rescue vehicles" | **Both returned ABSENT**, with the correct correction (three Australian regions). **Passed.** |
| Repeated-table cross-check | Table 1 requested twice, differently worded, separate calls | FBI rows identical both times (19.53 / 12.97 / 24.99; PEV 0.23 / 0.407 / 0.239). **Passed.** |

These raise confidence that the body was genuinely read. They are **not** a
substitute for a second rendering.

### A.10 Extraction queries run against the ConnectSci HTML

| # | What was asked | Usable result |
|---|---|---|
| A.10.1 | Cost–loss subsection verbatim; is the baseline tuned? | "The optimal classification threshold for each model is selected retrospectively to maximise PEV"; per-region FBI thresholds reported. **Corrects the repository's "not stated".** |
| A.10.2 | 11-term PRESENT/ABSENT sweep | See A.9. |
| A.10.3 | Forecast target and horizon; decision maker | "label = 1 indicated that a fire occurred within a future look-ahead window (2, 5 or 10 days)"; C = A$50,000 precautionary deployment vs L = A$10 million. |
| A.10.4 | Metrics list; PEV definition; is FBI tuned too? | TPR/FPR/ROC/PR/AUC; PEV expressions; threshold optimisation applied per model. |
| A.10.5 | Table 1 verbatim; headline numbers | Full 9-row table; "improved forecast skill over the FBI by 10–30%"; "doubling potential savings". |
| A.10.6 | Break-even / frontier? C/L sweep? error manipulation? PDF link? | **ABSENT, ABSENT, evaluated as-is.** Fixed C and L; only "Sensitivity tests (Supplementary Text S2)". |
| A.10.7 | False-premise trap + Table 1 re-ask + AUC | Trap refused; table reproduced identically. |
| A.10.8 | Limitations, Discussion, Conclusion; any human-safety claim?; truth data | Conclusion quoted; human-safety **ABSENT**; ~50 years AWS + 126 documented fires from official incident reports. |
| A.10.9 | Cost–loss paragraph + equations; latency statement?; FBI justification; persistence/climatology baseline? | Equations recorded; latency **ABSENT**; FBI = AFDRS operational index, "only a single daily rating is released publicly"; **no persistence/climatology/spatial baseline**. |
| A.10.10 | What does "sub-hourly" mean? 2/5/10-day window quotes; 10–30% sentence | "Each forecast cycle ingests 30-min AWS observations" → cadence, not lead. |

---

## B. Component searches — WG-FV-1 … WG-FV-7

Corpus-first, per the brief. **No broad corpus expansion was attempted.**

### B.0 Corpus scan (no external calls)

| # | Method | Result |
|---|---|---|
| B.0.1 | Scanned all 165 `literature/metadata/*.yaml` for matrix fields `forecast_latency`, `forecast_skill_boundary`, `decision_value`, `osse`, `korean_setting`, `voi`, `active_sensing`, `probabilistic_trigger`, `future_fire`, `real_validation` | 25 latency-flagged, 24 skill-boundary, 51 decision-value, 4 OSSE, 23 Korean. Drove every component's shortlist. |
| B.0.2 | `grep -ilE "perturb\|sensitivity analys\|injected\|degrad"` across all 71 notes | 12 files, **none** of them a wildfire paper injecting forecast error along named axes to test a decision. Drove WG-FV-1. |
| B.0.3 | Keyword scan of `bibliography/literature.csv` `one_line_difference` for `latenc\|stale\|frontier\|break-even\|deadline` | Surfaced `chang2026multiscale`, `zha2024distributed`, `sung2025geostationary`, `roysingh2025constellation`, `cheng2022surrogate`, `nasafirms2026latency` as the latency cluster. Drove WG-FV-2. |

### B.1 External queries

| # | Component | Query | Source | Usable hits |
|---|---|---|---|---|
| B.1 | WG-FV-1 | synthetic forecast error injection controlled degradation of forecast skill evacuation decision quality experiment | WebSearch | NWP OSSE observation-error scaling ("zero to twice the estimated realistic error"); Privé et al. 2013 Tellus A model/initial-condition error OSSE — **search leads, metadata UNVERIFIED**. No evacuation instance. |
| B.2 | WG-FV-1 | wildfire spread forecast error perturbation experiment effect on evacuation trigger boundary decision outcome | WebSearch | Only the known trigger lineage (`cova2005trigger`, `mitchell2023peril`, `larsen2011cedar`, `li2018coupling`). Safety factors added for error, but **no controlled error experiment**. **Null for the component.** |
| B.3 | WG-FV-2 | "forecast latency" OR "data latency" varied experimental factor decision quality simulation hazard warning value | WebSearch | NASA GSFC *Study on Data Latency Needs and Requirements* (report, lead); an OSE varying satellite-sounder data **cut-off windows** to measure latency impact on severe-storm forecasts — **latency varied as a factor, outcome = forecast score** (lead, UNVERIFIED); an edge-computing sim injecting 5/10/20/30% forecast noise. Confirms the move exists outside hazard decision-making. |
| B.4 | WG-FV-3 | wildfire evacuation "trigger buffer" optimized baseline compared against forecast-based policy benchmark tuned | WebSearch | Only the known trigger lineage. Search engine explicitly reported no comparative study of that design. **Null.** |
| B.5 | WG-FV-4 | "break-even" forecast skill latency two-dimensional region decision policy outperforms baseline hazard evacuation | WebSearch | Evacuation-prediction ML papers beating baselines; nothing in error x latency space. **Null.** |
| B.6 | WG-FV-6 | "observing system simulation experiment" evacuation decision quality hidden truth synthetic fire wildfire protective action evaluation | WebSearch | Generic OSSE definitions + behavioural evacuation experiments. No decision-level wildfire OSSE. **Null**, consistent with `zeng2020osse` listing societal-impact OSSEs as an open recommendation. |
| B.7 | WG-FV-3 | optimized buffer distance baseline benchmark compared forecast-informed policy wildfire evacuation simulation "fixed buffer" tuned comparator | WebSearch | Baseline-comparison practice in suppression-crew routing (arXiv 2605.04510, already a logged lead). **Null for a tuned positional-trigger benchmark.** |
| B.8 | WG-FV-7 | 산불 예측 정보 지연 대피 결정 요양원 구조 출동 시한 정보가치 (Korean) | WebSearch | **No academic study.** Agency action guidelines (MOIS, KFS, provincial centres), a 2025 YTN item on the forecast system failing to anticipate ~27 m/s gusts, and blog material quoting 119 response times to care facilities. **Recorded as leads only; no number from these enters the corpus.** Korean null stands, and does **not** lift the KCI/RISS/DBpia block. |

### B.2 alphaXiv discovery

| # | Component | Keywords / question | Usable hits |
|---|---|---|---|
| B.9 | WG-FV-1..7 | wildfire · forecast latency · evacuation deadline · assisted evacuation · decision loss · break-even · trigger boundary · OSSE | `moradi2026supported` (already filed), **`sezer2026infodesign` (arXiv 2606.30320)** — previously only a search lead in `agent-forecast-voi.md` 5.11, now **filed**; the rest were EV-charging, traffic and UQ papers already known or out of scope. |

---

## C. WG-COMB-1 searches

*"Is useful wildfire forecast/observation information available before an
assisted-evacuation option expires?"*

| # | Query | Source | Usable hits |
|---|---|---|---|
| C.1 | assisted evacuation deadline "information" available in time rescue dispatch wildfire warning lead time expires | WebSearch | Practitioner material only (USFA, Ready.gov, NIST WUI-RSET, LAFD). NIST's WUI-RSET decomposition (ignition → notification → response/movement) is the right *shape* but is a planning framework, not an evaluation. **Null.** |
| C.2 | "latest dispatch time" OR "last feasible departure" rescue vehicle hazard arrival forecast information available deadline flood tsunami | WebSearch | Flood rescue-force dispatch routing (Sci. Rep., A* worst-case travel times) — routing, no information axis. SAR 72-hour survival window. **Null.** |
| C.3 | nursing home hospital evacuation decision sufficient warning lead time before hurricane landfall forecast uncertainty shelter-in-place decision analysis | WebSearch | US *National Criteria for Evacuation Decision-Making in Nursing Homes*; GAO-06-443R; the Katrina nursing-home mortality literature. Warning time discussed **qualitatively** as a determinant; no evaluation of information availability against option expiry. **Adjacent-hazard null.** Leads UNVERIFIED. |
| C.4 | "decision window" closes before forecast information arrives "too late to act" quantified hazard warning latency evacuation option expiry study | WebSearch | **Found `jewson2026evacuation`** (see §D). Also surfaced a contamination hit — see §F. |
| C.5 | wildfire detection latency versus time available to evacuate vulnerable residents quantified comparison observation delay evacuation feasibility | WebSearch | No-notice wildfire awareness/departure literature; socially-vulnerable evacuation delay studies. Latency and vulnerability appear **side by side**, never joined by an evaluation. **Null.** |
| C.6 | alphaXiv: warning lead time · rescue deadline · latest departure time · information arrives too late · flood · tsunami · landslide · vertical evacuation · value of information | alphaXiv | `moradi2026supported`, `sezer2026infodesign`, landslide EWS under rainfall forecast uncertainty (arXiv 2605.17419, **lead**), tsunami DTN routing, flash-flood anticipatory warning. **No occupant.** |
| C.7 | Consensus (peer-reviewed corpus) | Consensus | **BLOCKED — quota 30/30, resets 1 October 2026.** |

**Coverage actually achieved for WG-COMB-1: S1.** 6 web queries + 1 alphaXiv
round + corpus scan, English plus one Korean query, no peer-reviewed-corpus
search, no Scopus/WoS/TRID, no KCI/RISS/DBpia. Under `SEARCH_PROTOCOL` §1 an S1
null supports nothing. Scored `UNKNOWN`.

---

## D. New papers found and filed

### D.1 `jewson2026evacuation` — **the significant find**

Jewson, S. (2026), *An extreme weather evacuation cost-lost model and the
implications for early warning weather forecasting systems*, **Frontiers in
Communication 11:1762033**, DOI **10.3389/fcomm.2026.1762033**, published
2026-04-10, **CC BY 4.0**.

- Found by query **C.4**, which was aimed at WG-COMB-1 and hit WG-FV-1 instead.
- **Verified by two independent sources** per `docs/CITATION_RULES.md`: Crossref
  REST API work record and the Frontiers publisher page. The abstracts agree
  word for word.
- The published title really does read "cost-**lost**". Both sources carry it.
  Do not silently normalise it in the `.bib`.
- Why it matters: it sweeps a **named forecast-uncertainty dimension** (the
  standard deviation of the change in forecast probability between issuances)
  and reports where the recommended action flips from evacuate to wait, using
  **decision loss** as the criterion. That is the shape of the RQ1 experiment,
  published in April 2026, in an adjacent hazard.
- Threat: **HIGH** to WG-C-002 and WG-C-012, MODERATE to WG-C-014.

### D.2 `sezer2026infodesign`

Sezer, F. (2026), arXiv:2606.30320v1 [math.OC], **PREPRINT**, DOI UNVERIFIED.

- Was already a logged search lead (`agent-forecast-voi.md` 5.11) marked
  "relevant to WG-C-002" and never filed. Filed now because Experiment 2 (§6.4,
  Fig. 6) sweeps public-signal precision against expected social cost and finds
  a **sign reversal**.
- Single-source metadata; no Crossref record. Cannot kill a claim alone.
- Threat: **MODERATE**.

### D.3 Deliberately NOT filed (leads only, metadata UNVERIFIED)

Per the brief's "do not pad" instruction:
NASA GSFC data-latency requirements report; the satellite-sounder data-cut-off
OSE; Privé et al. 2013 (Tellus A) model/initial-condition-error OSSE; landslide
EWS under rainfall forecast uncertainty (arXiv 2605.17419); the US national
nursing-home evacuation criteria document; GAO-06-443R; the 2025 YTN item on
Korean forecast-system shortfall. **None cited, none used to move a score.**

---

## E. Ready-to-paste registry rows (AGENTS.md §5 debt)

This agent's brief restricted it to metadata, notes, the review, the
decomposition and this log. **AGENTS.md §5 requires more.** The outstanding
edits are listed here, pre-computed, so the next agent applies them without
re-deriving anything. **Until they are applied, the two new papers are
incompletely filed and §5 is not satisfied.**

**`bibliography/literature.csv`** (columns: paper_id,title,authors,year,venue,
venue_type,volume,issue,pages,doi,url,publication_status,open_access_status,
date_verified,category,threat_level,threatens_claims,one_line_difference)

```
jewson2026evacuation,"An extreme weather evacuation cost-lost model and the implications for early warning weather forecasting systems",Stephen Jewson,2026,Frontiers in Communication,journal,11,,1762033,10.3389/fcomm.2026.1762033,https://doi.org/10.3389/fcomm.2026.1762033,PEER_REVIEWED,OA,2026-09-20,4,HIGH,WG-C-002; WG-C-012; WG-C-014,"Poses the RQ1 decision structure in its purest published form -- evacuate now or wait for the next forecast, solved by a cost-loss model -- and sweeps a NAMED forecast-uncertainty dimension (the standard deviation of the change in forecast probability between updates) to the point where the recommendation flips; tropical cyclone, explicitly idealized, no landscape, no comparator policy, no observation-to-product latency, no responder, and the frontier is one-dimensional."
sezer2026infodesign,"Continuous-Time Information Design for Hurricane Evacuation: Disclosure, Congestion, and Optimal Phasing under Model Uncertainty",Furkan Sezer,2026,arXiv,preprint,,,arXiv:2606.30320,UNVERIFIED,https://arxiv.org/abs/2606.30320,PREPRINT,OA,2026-09-20,4,MODERATE,WG-C-002; WG-C-014,"Sweeps the PRECISION of information released to evacuating zones and plots expected social cost against it, finding precision is self-defeating under a single broadcast and valuable only once releases are staggered -- an information-quality axis varied in a controlled experiment with decision loss as the outcome; the swept quantity is a designed signal's precision rather than forecast error, and there is no assisted evacuation, no responder round trip and no observation-to-product latency."
```

**`bibliography/doi_registry.csv`** (paper_id,doi,resolution_status,
metadata_agreement,resolved_title,resolved_year,resolved_container)

```
jewson2026evacuation,10.3389/fcomm.2026.1762033,RESOLVED,MATCH,An extreme weather evacuation cost-lost model and the implications for early warning weather forecasting systems,2026,Frontiers in Communication
sezer2026infodesign,,NO_DOI,,,,PREPRINT
```

**`bibliography/wildfireguardian.bib`** — the file header says it is GENERATED
from `literature/metadata/*.yaml` via `bibliography/build_bibliography.py`, so
**re-run the generator rather than hand-editing**. Expected entry types:
`@article` for `jewson2026evacuation`, `@misc` for `sezer2026infodesign`
(preprint — never `@article`, per the file header).

**`novelty/NOVELTY_MATRIX.md`** — column order is: Paper | Threat | future fire
| traffic | household trigger | prob. trigger | multi fire models | assisted
evac | inbound responder | pickup | egress | dispatch-by deadline | forecast
latency | skill boundary | decision value | scarce resources | VOI | active
sensing | Korean setting | real validation | OSSE.

```
| `jewson2026evacuation` | HIGH | . | . | ~ | Y | . | . | . | . | . | . | ~ | Y | Y | . | Y | . | . | . | . |
| `sezer2026infodesign` | MODERATE | ~ | Y | ~ | Y | . | . | . | . | Y | . | . | ~ | Y | ~ | Y | . | . | ~ | . |
```

**`novelty/NOVELTY_THREATS.md`** — `jewson2026evacuation` is threat **HIGH** and
therefore requires an entry (§5 triggers at MODERATE and above; both qualify).

**`docs/CLAIM_REGISTRY.md`** — WG-C-002 stays `WEAKENED` but its *reason* must
change (Ardid's baseline **is** tuned); WG-C-012 needs re-reading against
`zha2024distributed` and `chang2026multiscale`. See
`novelty/RQ1_DECOMPOSITION.md` §2.

---

## F. Contamination warning — read this before trusting a web hit

Query **C.4** returned, among its results:

> `github.com/Sparkxt-0318/wildfireguardian-forecast-value`

This is **WildfireGuardian's own repository**, not prior art. Fetched and
confirmed: its README opens "How good must a wildfire forecast be before it
deserves to change a protective decision? This repository develops the
experimental mathematics and statistics for answering that question."

Worse, the search engine's *summary* for C.4 paraphrased sentences that read
like they came from that repository ("a penalty makes a late forecast merely
worse; reality makes it absent, returning the decision maker to the policy they
had without it"). **The project's own framing is now indexed and will be fed
back to future agents as if it were external literature.**

Standing instruction for every subsequent agent: **any web hit on
`Sparkxt-0318`, `wildfireguardian`, or matching this project's own phrasing is
self-citation, must never be filed as prior art, and must never be counted as
independent corroboration of a null or a finding.** If a search summary asserts
something in this project's own voice, discard it.

---

## G. Stop-rule accounting (`SEARCH_PROTOCOL` §4)

| Line | Stopped because | Tier reached |
|---|---|---|
| WG-FV-1 | (b) claim-affecting paper found — `jewson2026evacuation` | S2 (inherits Cat 4) |
| WG-FV-2 | (a) saturation at 3 variants; **but** the two closest papers are only E2 | S1→S2 |
| WG-FV-3 | (a) saturation; 2 variants returned only the known trigger lineage | S2 (inherits Cat 4) |
| WG-FV-4 | (a) saturation at 2 variants — **thin; not a real saturation** | S1 |
| WG-FV-5 | (b) occupied, further search wasted | S2 |
| WG-FV-6 | (b) occupied, further search wasted | S2 |
| WG-FV-7 | **Blocked**, not saturated — KCI/RISS/DBpia undrivable | S1 (blocked) |
| WG-COMB-1 | Ran out of usable sources (Consensus quota), not out of ideas | S1 |

**Nothing here reached S3. Two lines (WG-FV-4, WG-COMB-1) did not reach S2 and
their nulls support nothing.**

---

## H. Next queries, for whoever picks this up

1. Consensus, **after 1 October 2026**: WG-COMB-1 and WG-FV-4, which are the two
   components starved by today's quota block.
2. Backward + forward citation chase on `jewson2026evacuation` (Crossref
   `is-referenced-by-count`, Semantic Scholar citations). Not traversed.
3. Full text of `zha2024distributed` (IJWF 33(7), DOI 10.1071/wf23165) — if its
   OSSE scores anything downstream of prediction error, **WG-FV-2 becomes
   `OCCUPIED`**.
4. Full text of `georgakakos2025evacuationtiming` (paywalled) — its
   evacuation-completion interval is the closest published object to an
   expiring evacuation option.
5. **Ardid et al. Supplementary Text S2.** It holds the cost-loss sensitivity
   tests. If it contains a C/L sweep, the one-dimensional form of WG-FV-4 is
   occupied *in wildfire* and RQ1 needs revision.
6. An independent rendering of Ardid et al. (institutional proxy, a colleague's
   PDF, or the UC repository once Cloudflare relents) to lift E3 → E4.
7. KCI / RISS / DBpia sweep — still the largest blind spot in the repository,
   and WG-FV-7 cannot move without it.
8. A Chinese-language pass around `zha2024distributed` and `wu2025denkf`, whose
   groups' adjacent work may not be in English.
