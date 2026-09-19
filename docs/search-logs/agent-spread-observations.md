# Search Log — Agent A/C (Categories 6 & 7: Fire Spread Models, Wildfire Observations / Remote Sensing)

**Agent role:** Search Researcher + Verification / Citation Auditor
**Domain:** Cat 6 (fire spread modelling: Rothermel, FARSITE, FlamMap, WRF-SFIRE, FIRETEC, ELMFIRE, WISE/Prometheus, SPARK, ML emulators, ensembles, data assimilation);
Cat 7 (VIIRS, MODIS, GOES-R/ABI, Himawari, GK2A, ground cameras, UAV/thermal, fire-front extraction, ROS from observations)
**Target claims to support:** WG-C-010, WG-C-012
**Target claims to falsify:** WG-C-004, WG-C-002, WG-C-010, WG-C-008, WG-C-014
**Search date:** 2026-09-19
**Tools used:** Consensus (Semantic Scholar/PubMed/Scopus/arXiv), WebSearch, WebFetch, alphaXiv/arXiv,
Crossref REST API (`api.crossref.org`, bibliographic query) for all DOI/venue/volume/page verification,
USDA FS TreeSearch, FRAMES catalog, NOAA Institutional Repository, NASA Earthdata/FIRMS wiki, elmfire.io docs.

**Tool budget note:** the Consensus account exhausted its monthly quota after 4 searches
(2 remaining at end of session). Rounds 3+ were therefore run on WebSearch / alphaXiv /
Crossref / publisher pages. This is a documented coverage limitation, not a null result.

---

## Log format
`| # | Date | Source | Query | Usable hits |`

---

## Round 1 — Core Category 6 sweep (model error, ensembles, OSSE)

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 1 | 2026-09-19 | Consensus | `observing system simulation experiment wildfire data assimilation fire spread` | 10 returned; **HIGH VALUE for WG-C-010**: Zha 2024 (ETKF-distributed, OSSE-generated asynchronous fire fronts, explicit observation-resource allocation), Wu 2025 (DEnKF validated by OSSE, Fire Technology), Wu 2024 (FLC-GRU R-matrix, OSSE), Ge 2024 (UAV DA), Zhang 2017 FIREFLY/FireFlux I, Cheng 2022 latent DA surrogate, Rios 2019 Vall-llobrega, Gu 2009 DDDAS, Zhang 2018 front-shape similarity. **OSSE is a standard, named method in wildfire spread DA.** |
| 2 | 2026-09-19 | Consensus | `Rothermel fire spread model rate of spread prediction error validation accuracy` | 10 returned; **error magnitudes**: Zhang 2023 (Karst, relative error up to 50%), Xu 2025 (mixed fuels, uncalibrated MRE 135.1%), Geng 2024 (MRE 25.09% after calibration), Geng 2026 (direct Rothermel MRE 35.01%, overprediction bias), Xu 2025 subtropical (MRE 37.7%), Weise 2016 (Rothermel failed to spread in nearly all live-fuel fires with default values; models correct 49–69%; only physical models within factor of two) |
| 3 | 2026-09-19 | Consensus | `ensemble wildfire spread prediction evacuation trigger boundary decision support probabilistic` | **CLAIM-KILLER for WG-C-004**: Kalogeropoulos & Rein 2026 — ensemble of FARSITE + Prometheus/WISE + ELMFIRE + Google EPD + EPD-ConvLSTM used to define probabilistic evacuation trigger boundaries (Fort McMurray). Also Kalogeropoulos 2023 (k-PERIL stochastic triggers), Kalogeropoulos 2025 (dire evacuations / safety factor), Mitchell 2022 PERIL, Ramirez 2019 stochastic decision triggers, Allaire 2020 ensemble + probabilistic scores, Storey 2021 Bayesian ROS |
| 4 | 2026-09-19 | Consensus | `machine learning wildfire spread emulator surrogate model runtime speedup real-time forecasting` | Runtime evidence: Cheng 2022 (~1000x faster than CA), Allaire 2021 (speed-up "several thousands", MAPE 32.8%), Li 2024 (10^2–10^4x), Bolt 2022 (Jaccard 0.76 emulator vs simulator), Cheng 2024 JULES-INFERNO surrogate, Nematshahi 2026, Li 2026 cross-scale |
| — | 2026-09-19 | Consensus | `multi-model ensemble fire behaviour prediction operational forecast uncertainty quantification` | **RATE-LIMITED / QUOTA EXHAUSTED — not run.** Coverage gap; re-run in October. |
| — | 2026-09-19 | Consensus | `fire perimeter prediction accuracy metric IoU Jaccard relationship to emergency decision quality` | **RATE-LIMITED / QUOTA EXHAUSTED — not run.** Coverage gap for WG-C-014; re-run in October. |

## Round 2 — Verification pass (Crossref REST API, bibliographic query)

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 5 | 2026-09-19 | Crossref API | `Defining probabilistic evacuation triggers wildfires ensemble flame spread models Fort McMurray` | **VERIFIED**: Kalogeropoulos & Rein, *Fire Safety Journal* 165:104912 (2026-11), DOI 10.1016/j.firesaf.2026.104912. Note: a plain WebSearch for the same title returned **zero** hits — Consensus/Crossref found it, general web search did not. Search-engine null results are not evidence. |
| 6 | 2026-09-19 | Crossref API | `Design of stochastic trigger boundaries for rural communities evacuating from a wildfire` | VERIFIED: Fire Safety Journal 140:103854, DOI 10.1016/j.firesaf.2023.103854; 5 authors (Kalogeropoulos, Mitchell, Ronchi, Gwynne, Rein) |
| 7 | 2026-09-19 | Crossref API | batch of 5: Lautenberger ELMFIRE; Mitchell PERIL; Kalogeropoulos Mati; Ramirez stochastic trigger; Allaire ensemble | All 5 VERIFIED with DOI, volume, pages, full author list |
| 8 | 2026-09-19 | Crossref API | batch of 8: Schroeder VIIRS 375 m; Giglio MODIS C6; Mandel WRF-SFIRE; Hall geostationary validation; Allaire emulation; Weise chaparral; Storey Bayesian; Bailon-Ruiz UAV fleet | All 8 VERIFIED |
| 9 | 2026-09-19 | Crossref API | batch of 8: Wu DEnKF; Zha distributed; Zhang Karst; Cheng surrogate; Tymstra Prometheus; Miller SPARK; Linn FIRETEC; (1 miss) | 7 VERIFIED. **Tymstra Prometheus NOR-X-417 NOT found in Crossref** — filed as `UNVERIFIED` DOI, not invented. |
| 10 | 2026-09-19 | Crossref API | `Uncertainty associated with model predictions of surface and crown fire rates of spread Cruz Alexander` | VERIFIED: Environ. Model. Softw. 47:16–28, DOI 10.1016/j.envsoft.2013.04.004 |
| 11 | 2026-09-19 | Crossref API | `Geospatial System for Wildfire Monitoring and Prediction Using Aerospace Data` | VERIFIED: Moldamurat et al., *Natural Hazards Research* 6(2):516–533, DOI 10.1016/j.nhres.2025.12.002. **NOT recorded** — could not retrieve the full text to confirm the latency/IoU numbers a search snippet attributed to it. See Open questions. |

## Round 3 — Category 6 government reports / software documentation

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 12 | 2026-09-19 | WebSearch + WebFetch (USDA FS TreeSearch 32533) | `Rothermel 1972 mathematical model predicting fire spread wildland fuels INT-115` | VERIFIED record: Res. Pap. INT-RP-115, Ogden UT, 40 p., DOI 10.2737/INT-RP-115. **GOVERNMENT_REPORT, not peer-reviewed** |
| 13 | 2026-09-19 | WebSearch + WebFetch (TreeSearch 55928) | `Andrews 2018 RMRS-GTR-371 Rothermel surface fire spread model comprehensive explanation` | VERIFIED: GTR RMRS-GTR-371, Fort Collins CO, 121 p., DOI 10.2737/RMRS-GTR-371. **GOVERNMENT_REPORT** |
| 14 | 2026-09-19 | WebSearch | `Finney 1998 FARSITE fire area simulator model development evaluation RMRS-RP-4 revised 2004` | Record located (TreeSearch 4617); series RMRS-RP-4, Ogden UT, revised 2004. **GOVERNMENT_REPORT.** DOI and page count not retrieved → `UNVERIFIED` |
| 15 | 2026-09-19 | WebSearch + WebFetch (github.com/lautenberger/elmfire) | `ELMFIRE fire spread model runtime ensemble Monte Carlo operational forecast open source` | ELMFIRE README: Rothermel + CFFDRS + level-set, EPLv2, Monte Carlo ensemble, primary citation Lautenberger 2013 FSJ 62:289–298 |
| 16 | 2026-09-19 | WebFetch (elmfire.io/validation.html) | ELMFIRE automated CONUS validation | **HIGH VALUE error magnitudes**: ELMFIRE mean Jaccard 0.178, Sorensen 0.278, Cohen's kappa 0.241; FARSITE on the same dataset Jaccard 0.176, Sorensen 0.274, kappa 0.249. Also Dogrib 2001 vs Prometheus. **SOFTWARE_DOC** |
| 17 | 2026-09-19 | WebSearch | `Pyregence Pyrecast ELMFIRE active fire forecast ensemble simulations updates lead time` | PyreCast: 14-day forecasts, 1000-member ensemble per fire, 10/50/90 percentile envelope, ~12-hourly re-initialisation from satellite heat detections, two models (ELMFIRE + GridFire). Recorded as operational-practice evidence; secondary source, flagged E2 |
| 18 | 2026-09-19 | WebSearch | `WISE Wildfire Intelligence and Simulation Engine Canada Prometheus successor open source` | Located Bennett et al. 2026 IJWF assessment (below) and WISE-Developers GitHub |
| 19 | 2026-09-19 | WebFetch (connectsci.au, IJWF) | `Assessment of fire spread predictions from W.I.S.E. using satellite-derived wildfire perimeters` | **HIGHEST-VALUE error magnitudes found**: Bennett, Jain, Moore & Boisvert 2026, IJWF 35(8):WF26072, DOI 10.1071/WF26072. 19,848 fire-days / 2210 wildfires. Default params: mean F1 0.259, IoU 0.194, precision 0.200, recall 0.856, Hausdorff 2828 m. Hindsight-optimised duration + wind: F1 0.539, IoU 0.309 |
| 20 | 2026-09-19 | WebSearch + WebFetch (FRAMES 16277) | `Cruz Alexander 2013 uncertainty model predictions surface crown fire rates of spread` | **VERIFIED via FRAMES HTML abstract**: 49 evaluation datasets, 1278 observations, 7 fuel type groups; 3% of predictions exact; mean percent error 20–310%; over half of datasets 51–75%; ±35% proposed as reasonable performance |
| 21 | 2026-09-19 | WebFetch (nrfirescience.org PDF) | same paper, PDF fetch | **DISCARDED.** The PDF-reading model returned "13 datasets / 1,455 observations / −23.8% to +16.9% / ±15%" — irreconcilable with the published abstract. Treated as extraction hallucination; the FRAMES HTML abstract numbers are used instead. **Lesson logged: do not accept numbers from a binary-PDF WebFetch without a text cross-check.** |

## Round 4 — Category 7 sweep (observation modalities, resolution, cadence, latency)

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 22 | 2026-09-19 | WebSearch | `VIIRS 375 m active fire product latency spatial resolution revisit NRT FIRMS` | 375 m pixel centre; complements MODIS; better small-fire and night performance. No latency in these pages |
| 23 | 2026-09-19 | WebSearch + WebFetch (earthdata wiki FIRMS blog 2022-07-14) | `NASA LANCE FIRMS ultra real-time URT VIIRS MODIS latency direct readout` | **VERIFIED latency numbers**: URT <60 s from observation (MODIS ~25 s, VIIRS ~50 s) for CONUS/Canada direct-readout footprint; RT 20–30 min; URT/RT roll off after 6 h |
| 24 | 2026-09-19 | WebSearch | `near real-time NRT MODIS VIIRS active fire FIRMS within 3 hours LANCE` | NRT within 3 h of satellite observation (global). NASA Earthdata direct page returned HTTP 403 — number taken from the indexed LANCE/FIRMS text, flagged E2 |
| 25 | 2026-09-19 | WebSearch | `GOES-16 ABI fire detection FDC latency 5 minutes 2 km WF-ABBA validation` | 2 km; 5 min CONUS, 10 min full disk; FDC is a WF-ABBA descendant |
| 26 | 2026-09-19 | WebFetch (NOAA Institutional Repository PDF 53332) + local pypdf extraction | Hall et al. 2023 geostationary validation, full text | **VERIFIED from extracted text**: false alarm 4–7% (FDC) / 2–6% (FRP-PIXEL) high-confidence; 48% (2018) → 4% (2020) FDC false alarms; ABI FDC every 10 min full disk, 5 min CONUS, 30–60 s mesoscale (15 min pre-April 2019); MSG FRP-PIXEL every 15 min; **"positioning error … on the order of several kilometres depending on terrain elevation and view zenith angle"** (Section 2.1) — critical for steep Korean terrain |
| 27 | 2026-09-19 | WebSearch + WebFetch (kjrs.org) | `GK2A AMI Korea geostationary wildfire detection 2 km 10 minute NMSC` | **VERIFIED**: Sung, Lee, Kim, Kim, Yang & Im 2025, *Korean Journal of Remote Sensing* 41(3):565–580, DOI 10.7780/kjrs.2025.41.3.6. GK2A/AMI 2 km IR; 10 min full disk / regional, **2 min Korean Peninsula local**; LGBM detector; recall 0.329, precision 0.987, F1 0.494; **average detection delay 12.9 minutes**; March 2025 South Korea wildfires |
| 28 | 2026-09-19 | WebSearch | `ALERTWildfire ALERTCalifornia camera network detection time AI before 911 call` | Operator-reported (non-peer-reviewed): >1,200 cameras; 3,600 fires alerted in 2025; >50% alerted before any 9-1-1 report; earliest case 2.5 h before first 911 call. **Filed as RECALL/press-level, E3 — NOT entered as a metadata record** |
| 29 | 2026-09-19 | WebSearch + WebFetch (arXiv 2606.06016) | `MTG-FCI fire observations event-based fire behaviour monitoring near-real-time` | Paugam et al. 2026 arXiv preprint: Fire Event Tracker, spatio-temporal clustering, FRP + rate of spread updated at **10-minute intervals**. Spatial resolution / latency **not stated on the abstract page → UNVERIFIED** |
| 30 | 2026-09-19 | WebSearch | `UAV drone thermal infrared wildfire GSD latency fire front extraction ROS accuracy` | FLAME 3 dataset, UAV fire-front segmentation. GSD ~17.6 cm/px at 122 m AGL quoted by a secondary source; **no verified latency or ROS-accuracy numbers found → UNVERIFIED in the table** |

## Round 5 — Adversarial sweep (WG-C-008, WG-C-010, WG-C-014) + 2025–2026 / preprint pass

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 31 | 2026-09-19 | alphaXiv | keywords `wildfire, fire spread, evacuation, observing system simulation experiment, value of information, sensor tasking, forecast latency` (difficulty 8) | **HIGH VALUE**: Roy-Singh et al. 2025 (2508.06687, NASA CYGNSS constellation tasking); Braydwood et al. 2026 (2606.12310, satellite scheduling for wildfire); Paugam 2026 (2606.06016); Fujitsu 2026 (2606.13633, aerial suppression intervention design); 2608.05413 (supported evacuation decomposition); 2605.04510 (prescriptive suppression allocation); 2603.29055 (Lahaina traffic). **No wildfire-evacuation OSSE returned.** |
| 32 | 2026-09-19 | WebSearch | `"observing system simulation experiment" OR OSSE wildfire evacuation decision synthetic truth protective action` | **ZERO hits on OSSE + evacuation decision.** Only evacuation-behaviour ML/LLM papers. Recorded as `UNKNOWN`, not as support (NOVELTY_STANDARD §3.2) |
| 33 | 2026-09-19 | WebSearch | `wildfire adaptive observation targeting information gain expected value of information fire front sensor placement` | **Closest prior art to WG-C-008**: Papaioannou et al. 2026 (arXiv 2601.11231) — information-seeking predictive control for drone fire-front monitoring. Objective is **estimation uncertainty**, not a downstream decision. Also Bailon-Ruiz 2022 SAOP (forecast-driven UAV observation plan), Multi-UAV QoS coverage (2206.10544), evidential-reasoning sensor guidance |
| 34 | 2026-09-19 | WebSearch + WebFetch (arXiv 2508.06687, alphaXiv full text) | NASA constellation tasking full text grep for `latency`, `objective`, `reward`, `WRF-SFIRE` | **VERIFIED**: MIP scheduler maximises **science reward** (active-fire targets weighted 10x pre-fire); 98–100% of available rewards collected; observation-to-downlink latency expected **<24 h**; end-to-end workflow latency **6–30 h** vs current "multiple days"; assimilated into WRF-SFIRE/WRFx. Objective is **science value, not decision consequence** |
| 35 | 2026-09-19 | WebFetch (arXiv 2606.12310) | Quantum satellite scheduling for urgent wildfire response | Braydwood et al. 2026. Objective is scheduling efficiency / NRT access — **accuracy- and coverage-driven, not decision-consequence-driven** |
| 36 | 2026-09-19 | WebSearch + WebFetch (arXiv 2603.22331) | `fire spread ensemble decision support evacuation multiple models comparison` → conformal risk control | **Closest prior art to WG-C-014**: Dayan 2026 (2603.22331). Standard thresholds captured only **7–72%** of actual fire spread across models; three-way SAFE/MONITOR/EVACUATE triage with FNR ≤ 0.05; ~95% fire coverage at ~15% of pixels flagged. Demonstrates accuracy metric ≠ operational adequacy, but does **not** show non-monotonicity of accuracy vs decision quality |
| 37 | 2026-09-19 | WebSearch | `"fire spread" prediction accuracy metric misleading decision quality burned area overlap not sufficient` | Qualitative statements only (Jaccard/Sorensen/kappa "have limitations in extreme scenarios"; need for domain-specific metrics). **No paper found that quantifies the accuracy→decision-quality mapping.** WG-C-014 remains `UNKNOWN` |
| 38 | 2026-09-19 | WebSearch | `wildfire forecast timeliness latency decision timeline incident action plan 24 hour operational period` | NWCG: fire behaviour forecast written into next-day IAP; IMT assembly/transition may take up to 24 h; fire potential forecasts 24 h to 7 d. Useful operational-latency context (agency doc, E2) |
| 39 | 2026-09-19 | WebSearch | `Korea forest fire spread prediction NIFoS Pinus densiflora rate of spread validation 2025 Uiseong Andong` | Korean fuel-load and smoke-dispersion modelling located (KFSDP, Pinus densiflora fuel-load model). **No published ROS-validation study for the March 2025 Uiseong/Andong fires found.** A 7.4 km/h spread figure circulates on non-academic Korean blogs — **NOT recorded, UNVERIFIED** |

---

## Coverage limitations (honest statement)

1. **Consensus quota exhausted after 4 queries.** Two planned queries (multi-model operational
   ensembles; IoU-vs-decision-quality) were never run. Rounds 3–5 substituted WebSearch/alphaXiv,
   which index differently — the Kalogeropoulos 2026 case (found by Consensus, invisible to
   WebSearch) shows the two are not interchangeable.
2. **No non-English (Korean) database pass.** RISS / KCI / DBpia were not searched. Korean-language
   NIFoS and KFS technical reports on fire spread and GK2A operational use are therefore unsampled.
   This blocks any `SUPPORTED_CANDIDATE` promotion under NOVELTY_STANDARD §5.
3. **Paywalls.** ScienceDirect, MDPI, Springer, Taylor & Francis and NASA Earthdata returned
   HTTP 403 to WebFetch. Where a number could not be reached in text form it is `UNVERIFIED`.
4. **No backward/forward citation chase was completed** on Kalogeropoulos & Rein 2026 — its
   reference list and citing works are the highest-priority next step for WG-C-004 and WG-C-002.

## Open questions raised by this log

- Does Kalogeropoulos & Rein (2026) report any *decision-quality* comparison between ensemble
  members, or only boundary geometry? (NEEDS_FULL_TEXT — paywalled.)
- Moldamurat et al. 2026 (*Nat. Hazards Res.* 6(2):516–533) was attributed by a search snippet with
  ~300 min median end-to-end latency, 6 h issuance cadence and 24 h forecast IoU 0.84 ± 0.02. The
  full text was not retrieved and **these numbers are not recorded anywhere in this repository.**
- MTG-FCI spatial resolution and product latency — not obtained.
- Is there any Korean-language OSSE or ensemble fire-spread study? Unsearched.
