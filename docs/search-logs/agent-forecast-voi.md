# Search Log — Agent A/B (Forecast Value + VOI / Active Sensing)

**Agent role:** A/B — Search Researcher + Prior-Art Adversary
**Domain:** Category 4 (forecast value) and Category 5 (VOI / active sensing)
**Claims attacked:** WG-C-002, WG-C-006, WG-C-008, WG-C-012, WG-C-014
**All searches run:** 2026-09-19
**Deliverables:** `literature/reviews/04-forecast-value.md`,
`literature/reviews/05-voi-active-sensing.md`, 14 notes, 34 metadata files.

Sources used: WebSearch (general web), Consensus (peer-reviewed corpus;
**quota exhausted after 6 searches — resets 1 Oct**), alphaXiv
(`discover_papers`, `get_paper_content`), WebFetch (publisher pages),
Crossref REST API via curl (bibliographic verification).

---

## A. Category 4 — forecast value

| # | Query | Source | Usable hits |
|---|---|---|---|
| 4.1 | cost-loss ratio decision model economic value of weather forecasts | Consensus | `murphy1977costloss`, `murphy1985generalized`*, `murphy1985dynamic`*, `stephenson2025extremeloss`, `olivetti2026compounding`, `macleod2021anticipatory`, Lee et al. 2007 (KMA/CMA profit-loss)*, Shanker et al. 2024 (NCMRWF REV)* |
| 4.2 | Murphy 1977 value of climatological categorical probabilistic forecasts cost-loss ratio situation | WebSearch | `murphy1977costloss` confirmed (MWR 105:803-816); `murphy1994assessing` surfaced |
| 4.3 | hurricane evacuation order timing optimal stopping track forecast uncertainty decision model | WebSearch | `regnier2008public`; "optimal time to evacuate: behavioral dynamic model, Louisiana" (Transp. Res. B — search lead); hurricane preparedness robust optimisation (search lead) |
| 4.4 | Regnier 2008 "public evacuation decisions" hurricane forecast accuracy lead time tradeoff | WebSearch | `regnier2008public` details (4 target locations, 10% miss -> >=76% false alarms) |
| 4.5 | wildfire evacuation trigger buffer forecast skill decision value comparison tuned baseline | WebSearch | `berlinghieri2024pm25` (**key**); Larsen/Dennison Cedar Fire trigger buffers (other agent's domain) |
| 4.6 | "smart predict then optimize" decision-focused learning prediction accuracy not aligned with decision quality | WebSearch | DFL portfolio instances; led to `mandi2024dfl` |
| 4.7 | flood early warning system cost-loss relative economic value lead time Verkade Werner | WebSearch | `verkade2011estimating`; Pappenberger monetary benefit (search lead); ASCE NHR review of flood-forecast economic value (search lead) |
| 4.8 | forecast latency timeliness as decision variable warning lead time value information delay emergency | WebSearch | weak — mostly supply-chain lead time; one dengue "optimal lead time for forecast" hit (search lead) |
| 4.9 | "how good"/"how skillful" must a forecast be threshold before forecast-based action beats climatology | WebSearch | **`raeth2025decisionskill` (critical)**; `bouttier2024optimal` (**key**) |
| 4.10 | relative economic value fire danger forecast cost-loss wildfire prescribed burn ensemble | WebSearch | **`ardid2026forecastvalue` (key wildfire hit)**; "Socioeconomic value of fire weather service ... prescribed burning" (FRAMES 12999 — search lead, metadata not retrieved) |
| 4.11 | "From forecast skill to economic value" sub-hourly wildfire potential forecasting Australian regions cost-loss | WebSearch + WebFetch(FRAMES 71772, ConnectSci) | `ardid2026forecastvalue` full metadata + abstract; also surfaced Nat. Commun. 2026 eruption-forecast value paper (**search lead, UNVERIFIED**) |
| 4.12 | tornado severe weather warning lead time value false alarm ratio protective action Hoekstra | WebSearch | Simmons & Sutter-type result: lead time >15 min does not further reduce fatalities — **`RECALL_UNVERIFIED` / secondary-source only**; Hoekstra et al. 2011 lead-time preferences (search lead) |
| 4.13 | "decision-relevant" evaluation metric fire spread model IoU Jaccard burned area prediction decision quality | WebSearch | **`xu2026wildfirefm`**; Filippi-type burnt-area evaluation indices (Environ. Model. Softw. — search lead) |
| 4.14 | warning dissemination delay latency decision deadline "time to act" information arrives too late value zero | WebSearch | mostly patents; "Open challenges for ML-based Early Decision-Making" arXiv:2204.13111 (**search lead**, earliness/accuracy tradeoff) |
| 4.15 | "timeliness" of forecast explicit tradeoff accuracy versus timeliness early warning economic value quantified | WebSearch | **`bischiniotis2019tradeoffs` (key for WG-C-012)**; "Forecasts and actuals: the trade-off between timeliness and accuracy" (Int. J. Forecasting 1989 — search lead) |
| 4.16 | Lopez Coughlan de Perez "time, cost and quality trade-offs..." potential economic value lead time | WebSearch | `bischiniotis2019tradeoffs` finding ("optimal lead time to trigger action is a function of forecast quality..."); **`lopez2020bridging`** |
| 4.17 | "Bridging forecast verification and humanitarian decisions" valuation approach | WebSearch | `lopez2020bridging` full citation (WACE 27:100167) |
| 4.18 | flood forecast lead time versus accuracy tradeoff "value of information" decision to evacuate warning | WebSearch | EWASE flash-flood effectiveness (search lead); confirms lead-time/reliability tradeoff is standard |
| 4.19 | wildfire evacuation decision ensemble fire spread forecast uncertainty probability of arrival trigger performance skill | WebSearch | stochastic decision trigger modelling (Sci. Total Environ. — other agent's domain); probabilistic diffusion fire-spread surrogate (search lead) |
| 4.20 | "forecast latency"/"data latency" satellite observation delay operational decision value wildfire emergency | WebSearch | VIIRS ultra-real-time latency ~50 s; Swedish end-to-end detection system mean alarm latency <17 min (Sci. Remote Sens. 2026 — **search leads**). **Finding: latency is measured operationally but never converted to decision value.** |
| 4.21 | 2026 AI weather model decision value evacuation protective action skill threshold study | WebSearch | **`masiwal2026decisionoriented`**; AIES 2026 severe-weather-from-AIWP (search lead) |
| 4.22 | 2026 preprint forecast value protective action decision boundary skill lead time wildfire evacuation arXiv | WebSearch | "Predictive and Prescriptive AI toward Optimizing Wildfire Suppression" arXiv:2605.04510 (**search lead** — predict-then-optimize in wildfire suppression, relevant to WG-C-011/014) |
| 4.23 | **Korean-language pass:** 산불 대피 의사결정 예측 정보 가치 기상예보 경제적 가치 연구 | WebSearch | **No Korean forecast-value or evacuation-decision-value study found.** Hits were fire-occurrence prediction, macroeconomic damage accounting (J. Korean Soc. Hazard Mitig.), and vendor material. Korean gap is real but N4-weak per NOVELTY_STANDARD §4. |
| 4.24 | Zhu Toth Wobus Richardson Mylne 2002 economic value of ensemble-based weather forecasts | WebSearch | `zhu2002economic` (BAMS 83(1):73-83) |
| 4.25 | Richardson 2000 skill and relative economic value ECMWF EPS | WebSearch | `richardson2000relative` (QJRMS 126(563):649-667) |

\* Recorded as search leads or lower-priority metadata; see §D.

---

## B. Category 5 — VOI / active sensing

| # | Query | Source | Usable hits |
|---|---|---|---|
| 5.1 | adaptive observation targeting meteorology value of information sensitivity singular vectors Majumdar review | WebSearch | `palmer1998singular`; Majumdar ETKF targeting lineage (search lead); "Methods, current status and prospect of targeted observation" Sci. China Earth Sci. (search lead) |
| 5.2 | value of information environmental decision making Bayesian expected value of sample information natural hazard | WebSearch | Williams & Johnson EVSI in natural resources (search leads); Frontiers "VOI and Decision Pathways" (search lead) |
| 5.3 | wildfire UAV informative path planning information gain active sensing fire front monitoring | WebSearch | PyroTrack (arXiv 2403.11095), distributed wildfire surveillance with deep RL (JGCD), real-time UAV fleet monitoring (Robot. Auton. Syst.) — **all search leads, metadata unverified** |
| 5.4 | value of information wildfire management decision fire monitoring observation worth | WebSearch + WebFetch(Frontiers) | **`simon2022wildfirevoi` (full text read)**, `hope2024wildfiresat`, `frisvold2024demandinfo` |
| 5.5 | wildfire spread forecast data assimilation targeted observation optimal sensor placement fire front information | WebSearch | fire-front EnKF assimilation literature (search leads). **Finding: wildfire DA assimilates whatever observations arrive; nobody selects them by decision impact.** |
| 5.6 | value of information optimal sensor placement decision-directed sensing under time deadline | Consensus | **`malings2016voisensor` (critical)**, `malings2018voispatiotemporal`, Malings & Pozzi 2019 submodularity (DOI UNVERIFIED), SHM VOI sensor-design papers (Cantero-Chinchilla, Chadha, Ercan) — all structural-health, no deadline |
| 5.7 | Bayesian experimental design review Rainforth "modern Bayesian experimental design" expected information gain | WebSearch | `rainforth2024modernbed`; **`rossa2026actionbed`** |
| 5.8 | sensor tasking scheduling under deadline time-constrained information gathering myopic value of information POMDP | WebSearch | **`veiga2023activesensing`**; myopic policy bounds for information-acquisition POMDPs (arXiv 1601.07279 — search lead); POMDP controlled sensing (search lead) |
| 5.9 | task-driven decision-theoretic Bayesian experimental design downstream decision utility not information gain | WebSearch | `rossa2026actionbed` abstract; "Amortized Bayesian Experimental Design for Decision-Making" NeurIPS 2024 / arXiv:2411.02064 (**search lead**); "Goal-driven Bayesian Optimal Experimental Design..." arXiv:2605.26093 (**search lead**) |
| 5.10 | decision-focused learning survey Mandi Kotary 2024 predict-then-optimize review | WebSearch | `mandi2024dfl` (JAIR 80:1623-1701) |
| 5.11 | alphaXiv `discover_papers`: decision-focused learning / predict-then-optimize / wildfire / evacuation / VOI / forecast value / active sensing | alphaXiv | **`liu2026dflfail`**, "Strategic Decision Focused Learning" arXiv:2609.14907 (search lead), "Value of Information in Dynamic Decision Making" arXiv:2608.29273 (search lead), `xu2026wildfirefm`, "Continuous-Time Information Design for Hurricane Evacuation" arXiv:2606.30320 (**search lead — relevant to WG-C-002**) |
| 5.12 | alphaXiv `discover_papers`: forecast latency / timeliness / cost-loss / informative path planning / sensor scheduling / deadline / wildfire monitoring | alphaXiv | **`shao2026beliefaware` (wildfire active sensing)**, **`sun2025decisionfocusedsensing` (critical)**, "Denial of Deadline" arXiv:2607.24692 (search lead), maneuverable EO satellite wildfire scheduling arXiv:2602.08924 (search lead), quantum satellite scheduling for wildfire arXiv:2606.12310 (search lead) |

---

## C. Verification passes (Crossref REST API, `api.crossref.org`)

Bibliographic fields (authors, venue, volume, issue, pages, year, DOI, type)
verified for: `murphy1977costloss`, `murphy1987accuracyvalue`,
`chen1987qualityvalue`, `murphy1994assessing`, `richardson2000relative`,
`zhu2002economic`, `regnier2006dynamic`, `regnier2008public`,
`verkade2011estimating`, `bischiniotis2019tradeoffs`, `lopez2020bridging`,
`macleod2021anticipatory`, `stephenson2025extremeloss`,
`olivetti2026compounding`, `georgakakos2025evacuationtiming`,
`palmer1998singular`, `malings2016voisensor`, `malings2018voispatiotemporal`,
`veiga2023activesensing`, `rainforth2024modernbed`, `mandi2024dfl`,
`sun2025decisionfocusedsensing`, `simon2022wildfirevoi`, `hope2024wildfiresat`,
`frisvold2024demandinfo`.

**Serendipitous finds from Crossref queries** (i.e. found by verification, not by
a planned query — the two most damaging papers of the whole pass):
- `murphy1987accuracyvalue` — surfaced as the second Crossref result when
  verifying `murphy1977costloss`.
- `chen1987qualityvalue` — surfaced when verifying the above.
- `georgakakos2025evacuationtiming` — surfaced when verifying `regnier2008public`.

Publisher pages that **refused** retrieval (403 / paywall / bot wall):
ScienceDirect, AMS journals, ACM DL, Springer Link, IIASA PURE. Those records are
marked E1 or E2 in their metadata files and listed as `NEEDS_FULL_TEXT`.

---

## D. Search leads NOT recorded as metadata (`RECALL_UNVERIFIED` / unverified)

These appeared in search output but were not verified to the standard required
for a metadata entry. They are follow-up work, not citations.

1. Murphy 1985 (x2): "Decision Making and the Value of Forecasts in a Generalized
   Model of the Cost-Loss Ratio Situation" and "Repetitive decision making and
   the value of forecasts ... a dynamic model", both MWR. Seen via Consensus
   abstracts; co-author lists and volume/pages not verified.
2. Simmons & Sutter tornado lead-time/false-alarm casualty results — relayed
   through secondary sources only. **`RECALL_UNVERIFIED`.**
3. Hoekstra et al. 2011, lead-time preferences for tornado warnings — secondary
   relay only.
4. "Socio-economic value of data-driven eruption forecasts to balance false
   alarms against catastrophic loss", Nature Communications 2026 — title and
   venue seen in search results only.
5. Malings & Pozzi 2019, "Submodularity issues in value-of-information-based
   sensor placement", Reliab. Eng. Syst. Saf. — Consensus abstract only, DOI
   unverified. **Important caveat paper; verify before relying on it.**
6. Huang et al., "Amortized Bayesian Experimental Design for Decision-Making",
   NeurIPS 2024 / arXiv:2411.02064 — full author list unverified.
7. "Goal-driven Bayesian Optimal Experimental Design for Robust Decision-Making
   Under Model Uncertainty", arXiv:2605.26093 — authors unverified.
8. "Continuous-Time Information Design for Hurricane Evacuation: Disclosure,
   Congestion, and Optimal Phasing under Model Uncertainty", arXiv:2606.30320 —
   **should be read; touches WG-C-002 and WG-C-011.**
9. "Predictive and Prescriptive AI toward Optimizing Wildfire Suppression",
   arXiv:2605.04510 — **should be read; predict-then-optimize in wildfire.**
10. "Open challenges for Machine Learning based Early Decision-Making research",
    arXiv:2204.13111 — earliness/accuracy tradeoff; relevant to WG-C-012.
11. Wildfire UAV informative-path-planning cluster: PyroTrack (arXiv 2403.11095);
    distributed wildfire surveillance with deep RL (J. Guid. Control Dyn.);
    real-time UAV fleet wildfire monitoring (Robot. Auton. Syst.); "Real-time
    autonomous path planning for dynamic wildfire monitoring with uneven
    importance" (Appl. Intell.). None verified.
12. "Socioeconomic value of fire weather service: a case study of fire weather
    information for prescribed burning" — FRAMES catalog 12999. Directly relevant
    to WG-C-002 (wildfire forecast value); **metadata not retrieved. Priority
    follow-up.**
13. Lee, K.-K. et al. 2007, Meteorological Applications — profit/loss forecast
    value using **KMA** and CMA forecasts. The only Korea-adjacent forecast-value
    item found; abstract seen via Consensus, not verified.
14. VIIRS ~50 s ultra-real-time latency; <17 min mean end-to-end alarm latency in
    a Swedish validated detection system — operational latency figures, sources
    not verified.

---

## E. Unresolved prior-art questions

- **U1.** Does any wildfire paper compare a forecast-aware protective-action
  policy against a *tuned* trigger/buffer? Not found in this pass. Needs a
  dedicated pass over the trigger-modelling literature (agent covering
  Categories 1-3) looking specifically at *baselines*, not methods.
- **U2.** Does the sensor-scheduling / POMDP literature contain a
  **hard-deadline** variant where observation value collapses at a decision
  time? Touched only via query 5.8. Needs a dedicated pass (keywords: "deadline
  constrained active sensing", "time-critical information gathering", "stopping
  time for information acquisition", "search and rescue POMDP deadline").
- **U3.** Early-classification / "earliness vs accuracy" literature
  (arXiv:2204.13111 and its lineage) is the closest formal treatment of
  *latency-as-a-decision-variable* and was not searched systematically.
- **U4.** Non-English beyond Korean: no Japanese, Chinese, Spanish or French pass
  was run. `NOVELTY_STANDARD` §5 requires >=1 non-English pass for
  `SUPPORTED_CANDIDATE`; one Korean pass was run (query 4.23), so the minimum is
  met but coverage is thin.
- **U5.** Consensus quota exhausted after 6 of a planned ~12 searches. The
  peer-reviewed-corpus sweep for Category 5 is therefore incomplete; rerun after
  1 October.
- **U6.** `murphy1987accuracyvalue` and `chen1987qualityvalue` are the load-bearing
  killers of WG-C-014 and were verified **bibliographically only (E1)**. Their
  full texts must be obtained before WG-C-014 is finalised in either direction.
