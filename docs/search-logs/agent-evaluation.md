# Search Log — Agent A/C (Category 10: Evaluation Methodology)

**Agent role:** Search Researcher + Verification / Citation Auditor
**Domain:** Cat 10 — pseudoreplication, event-level bootstrap, equivalence testing,
simulation V&V, inverse crime, OSSE design, calibration under shift, decision-focused
evaluation, baseline-strength critiques
**Target claims:** WG-C-002, WG-C-006, WG-C-010, WG-C-014
**Search date:** 2026-09-19
**Tools used:** Consensus (Semantic Scholar/PubMed/Scopus/arXiv), WebSearch, WebFetch,
Crossref REST API (`api.crossref.org`), arXiv API (`export.arxiv.org`), Semantic Scholar
Graph API, alphaXiv (`discover_papers`, `get_paper_content`)

---

## Log format
`| # | Date | Source | Query | Usable hits |`

---

## Round 1 — Pseudoreplication and unit of analysis

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 1 | 2026-09-19 | Crossref API | `query.bibliographic=Pseudoreplication and the design of ecological field experiments` | **Hurlbert 1984**, Ecol. Monogr. 54(2):187-211, DOI 10.2307/1942661 — metadata fully verified (authors, volume, issue, pages, year) |
| 2 | 2026-09-19 | Consensus | `pseudoreplication in simulation experiments unit of analysis independent replicates` | 10 returned. **Lazic et al. 2017/2018** (PLOS Biol, three-unit taxonomy), Hurlbert 1984, Hurlbert 2009 (J. Comp. Psychol., transdisciplinary restatement), Eisner 2021 (J. Gen. Physiol.), Lazic et al. 2019 (Sci. Rep., Bayesian predictive approach), plus the counter-literature: Oksanen 2001 (Oikos), Davies & Gray 2015 (Ecol. Evol.), Colegrave & Ruxton 2017 (TREE), Coss 2009 |
| 3 | 2026-09-19 | Crossref API | `query.bibliographic=What exactly is N in cell culture and animal experiments Lazic Clarke-Williams Munafo` | Returned the bioRxiv preprint (10.1101/183962) only — **preprint/journal trap avoided** |
| 4 | 2026-09-19 | Crossref API | DOI lookup `10.1371/journal.pbio.2005282` | **Lazic et al. 2018**, PLOS Biology 16(4):e2005282 — journal version confirmed |

**Note:** the counter-literature (Oksanen, Davies & Gray, Colegrave & Ruxton, Coss) was
read at abstract level only (E2) and is deliberately **not** recorded as metadata. It is
discussed in the review §1.

---

## Round 2 — Clustered inference and bootstrap

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 5 | 2026-09-19 | Consensus | `cluster bootstrap clustered standard errors few clusters inference wild bootstrap` | 10 returned. **Cameron, Gelbach & Miller 2008** (REStat, 3315 cites), **Cameron & Miller 2015** (JHR), MacKinnon & Webb 2013 (JAE, unequal cluster sizes), MacKinnon & Webb 2018 (Econom. J., few treated clusters), Webb 2014 (CJE, 6-point weights), Djogbenou et al. 2019 (J. Econom.), Roodman et al. 2018 (Stata J., `boottest`), MacKinnon et al. 2023 (JAE, jackknife CRVE) |
| 6 | 2026-09-19 | Crossref API | `query.bibliographic=Bootstrap-Based Improvements for Inference with Clustered Errors Cameron Gelbach Miller` | Returned NBER TWP 344 (10.3386/t0344) and SSRN 956890 — **working-paper trap**; resolved at #7 |
| 7 | 2026-09-19 | Crossref API | DOI lookup `10.1162/rest.90.3.414` | **Cameron, Gelbach & Miller 2008**, REStat 90(3):414-427 — journal version confirmed |
| 8 | 2026-09-19 | Crossref API | `query.bibliographic=A Practitioner's Guide to Cluster-Robust Inference Cameron Miller` | **Cameron & Miller 2015**, JHR 50(2):317-372, DOI 10.3368/jhr.50.2.317 |
| 9 | 2026-09-19 | Crossref API | `query.bibliographic=The jackknife and the bootstrap for general stationary observations Kunsch` + DOI lookup `10.1214/aos/1176347265` | **Künsch 1989**, Ann. Statist. 17(3) — **page range returned as null by Crossref; recorded as UNVERIFIED, not guessed** |

---

## Round 3 — Equivalence / non-inferiority

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 10 | 2026-09-19 | Consensus | `equivalence testing two one-sided tests TOST absence of evidence is not evidence of absence non-inferiority` | 10 returned. **Lakens 2017** (SPPS), **Lakens, Scheel & Isager 2018** (AMPPS), Linde et al. 2020 (Psychol. Methods — TOST underpowered at small n), Lauzon & Caffo 2009 (Am. Stat. — multiplicity), Tomek et al. 2026 (PNAS), Magara et al. 2024 (Lab. Anim.), Shen et al. 2026 (power/optimal design) |
| 11 | 2026-09-19 | Crossref API | `query.bibliographic=Equivalence Tests A Practical Primer ... Lakens` | Returned only the OSF preprint (10.31234/osf.io/97gpc) — **preprint trap**; resolved at #12 |
| 12 | 2026-09-19 | Crossref API | DOI lookups `10.1177/1948550617697177`, `10.1177/2515245918770963` | **Lakens 2017** SPPS 8(4):355-362 and **Lakens, Scheel & Isager 2018** AMPPS 1(2):259-269 — both journal versions confirmed |

---

## Round 4 — Simulation verification & validation

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 13 | 2026-09-19 | Crossref API | `query.bibliographic=Verification and validation of simulation models Sargent Winter Simulation Conference` | Four **conference** versions returned (WSC 1994 / 2005 / 2007 / 2008), all DOI-verified. Conference ≠ journal — flagged |
| 14 | 2026-09-19 | Crossref API | DOI lookups `10.1109/WSC.2011.6147750`, `10.1057/jos.2012.20` | WSC 2011 (183-198) and the **journal** version: **Sargent 2013**, J. Simulation 7(1):12-24 — the one to cite |
| 15 | 2026-09-19 | Crossref API | `query.bibliographic=Verification Validation and Confirmation of Numerical Models in the Earth Sciences Oreskes` | **Oreskes, Shrader-Frechette & Belitz 1994**, Science 263(5147):641-646 |
| 16 | 2026-09-19 | Crossref API | `query.bibliographic=Aligning simulation models a cyclical approach Axtell Axelrod Epstein Cohen` | **Axtell et al. 1996**, CMOT 1(2):123-141, DOI 10.1007/bf01299065. **Correction to prior recall: the actual subtitle is "A case study and results", not "A cyclical approach".** Recall corrected against the retrieved record |
| 17 | 2026-09-19 | Crossref API | `query.bibliographic=Using simulation studies to evaluate statistical methods Morris White Crowther` | **Morris, White & Crowther 2019**, Stat. Med. 38(11):2074-2102 |
| 18 | 2026-09-19 | WebSearch | `preregistration protocol for simulation studies Monte Carlo reporting guidelines statistical methods` | ADEMP-PreReg (Siepe et al.); Williams et al. 2024 MEE reporting items (17% report MC uncertainty, 32% no code); arXiv preprint of Morris et al. |
| 19 | 2026-09-19 | Crossref API | DOI lookups `10.1037/met0000695`, `10.1111/2041-210X.14415` | **Siepe et al. 2024**, Psychol. Methods (vol/issue/pages null → UNVERIFIED) and **Williams et al. 2024**, Methods Ecol. Evol. 15(11):1926-1939 |
| 20 | 2026-09-19 | WebSearch + Crossref + WebFetch | `verification of wildland-urban interface fire evacuation models Ronchi` → PMC10220130 | **Ronchi et al. 2023**, Nat. Hazards 117(2):1493-1519 — 24 verification tests across 8 components incl. Trigger buffers; verification/validation definitions quoted; explicit statement that validation data do not exist |

---

## Round 5 — Inverse crime

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 21 | 2026-09-19 | Crossref API | `query.bibliographic=inverse crime inverse problems synthetic data same model` | 0 usable — all hits were inverse **synthetic aperture radar**. Term collision noted |
| 22 | 2026-09-19 | Consensus | `inverse crime synthetic data generated by same forward model used for inversion` | **Henderson & Subbarao** 'Inverse Crime and Model Integrity in Lightcurve Inversion' (J. Astronaut. Sci.) — empirical demonstration of misleading optimism |
| 23 | 2026-09-19 | Crossref API | `query.bibliographic=Inverse Crime and Model Integrity in Lightcurve Inversion ...` | **Henderson & Subbarao 2016**, J. Astronaut. Sci. 64(4):399-413, DOI 10.1007/s40295-016-0105-1. Note Consensus listed 2016 and 2017 duplicates; Crossref issue date is 2016-12-20 — **year recorded as 2016** |
| 24 | 2026-09-19 | Crossref API | `query.bibliographic=Statistical and Computational Inverse Problems Kaipio Somersalo` | Monograph (10.1007/b138659, 2005) **and the key journal paper**: **Kaipio & Somersalo 2007**, 'Statistical inverse problems: Discretization, model reduction and inverse crimes', JCAM 198(2):493-504 |
| 25 | 2026-09-19 | WebSearch + arXiv abs page | `Wirgin "The inverse crime" arXiv 2004 mathematical physics` | **Wirgin 2004**, arXiv:math-ph/0401050 — **PREPRINT**. Abstract retrieved verbatim; definition quoted in review §5.1. No journal version found — recorded as PREPRINT with DOI UNVERIFIED |
| 26 | 2026-09-19 | Semantic Scholar Graph API | DOI `10.1016/J.CAM.2005.09.027` fields=abstract | **Abstract elided by publisher**; ScienceDirect returned HTTP 403. Kaipio & Somersalo 2007 recorded as **NEEDS_FULL_TEXT**; no quotation taken |

---

## Round 6 — OSSE design and the identical-twin question

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 27 | 2026-09-19 | Consensus | `observing system simulation experiment identical twin fraternal twin overestimate impact data assimilation` | 10 returned, **highest-value query of the sweep**: **Yu et al. 2019** (Ocean Sci. — the quantitative identical-twin-bias result), **Halliwell et al. 2014** (JTECH — fraternal-twin design criteria), **Zeng et al. 2020** (BAMS — societal-impact recommendation), Kleist & Ide 2015 (MWR), Privé et al. 2018, Paul et al. 2025 (QJRMS), Mendonça et al. 2025 (JMSE), Pflug et al. 2024 (HESS), Shohan et al. 2025 (JGR-A) |
| 28 | 2026-09-19 | Crossref API | 5 bibliographic queries: Yu 2019 / Halliwell 2014 / Zeng 2020 / Hoffman & Atlas / Arnold & Dey | All five verified: **Yu 2019** Ocean Sci. 15(6):1801-1814 (plus its discussion-stage preprint 10.5194/os-2019-85 under a **different title** — trap flagged); **Halliwell 2014** JTECH 31(1):105-130; **Zeng 2020** BAMS 101(8):E1427-E1438 (**plus Privé 2021 Comment**, BAMS 102(1):E80-E83); **Hoffman & Atlas 2016** BAMS 97(9):1601-1616; **Arnold & Dey 1986** BAMS 67(6):687-695 |
| 29 | 2026-09-19 | WebFetch | `os.copernicus.org/articles/15/1801/2019/` | Full open-access text. Extracted twin definitions (identical / fraternal / nonidentical), the bias direction, the quantitative table (45% vs 29% temperature; 46% vs 25% velocity; 67% vs 45% subsurface), and the **three atmospheric sources cited for the prior result: Arnold & Dey 1986, Atlas 1997, Hoffman & Atlas 2016** |
| 30 | 2026-09-19 | WebSearch | `"identical twin" experiment overestimates observation impact data assimilation known bias atmospheric` | Confirms the claim is standard; surfaced **Privé et al. 2023** (Tellus A) on OSSE robustness |
| 31 | 2026-09-19 | WebFetch | `tellusjournal.org/articles/10.16993/tellusa.3254` | **Privé et al. 2023**, Tellus A 75(1):309-333. Key finding: insufficient model error is the characteristic OSSE pathology; impacts rose from ~60% to >70% of real-world values with more model error; "a range of fraternal twin OSSEs should give robust experimental results, as long as the degree of twinning is well-understood" |
| 32 | 2026-09-19 | Crossref API | DOI `10.16993/tellusa.3254`; `query.bibliographic=Atlas Atmospheric observations ... JMSJ`; Privé/Errico QJRMS | **Privé et al. 2023** verified; **Atlas 1997** JMSJ 75(1B):111-130, DOI 10.2151/jmsj1965.75.1b_111; **Errico et al. 2013** QJRMS 139(674):1162-1178; Privé, Errico & Tai 2013 QJRMS 139(674):1354-1363 |
| 33 | 2026-09-19 | WebFetch | `journals.ametsoc.org/.../bams-d-15-00200.1.xml` (Hoffman & Atlas 2016) | **HTTP 403.** Full text not obtained |
| 34 | 2026-09-19 | WebFetch | `repository.library.noaa.gov/view/noaa/20389/noaa_20389_DS1.pdf` (Hoffman & Atlas 2016) | PDF unreadable / binary garbage. **Hoffman & Atlas 2016 recorded as NEEDS_FULL_TEXT** |

---

## Round 7 — WG-C-010 adversarial: is there a wildfire *decision* OSSE?

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 35 | 2026-09-19 | Consensus | `observing system simulation experiment wildfire fire spread model evacuation decision` | **Rate-limit error — query not executed.** Retried via WebSearch (#36-38) |
| 36 | 2026-09-19 | WebSearch | `"observing system simulation experiment" wildfire fire spread OSSE nature run synthetic observations` | Wildfire OSSEs exist **at the fire-model / DA level only**: FireFlux parameter estimation, Cell2Fire, data-driven spread forecasting. Explicit statements that "synthetic observations are generated using the fire propagation solver" — i.e. **identical-twin structure is common practice in the wildfire DA literature**. No decision-level OSSE |
| 37 | 2026-09-19 | WebSearch | `OSSE "societal impact" decision value observing system simulation experiment beyond forecast skill` | Confirms **Zeng et al. 2020** lists "extension of OSSEs to societal impacts" as an outstanding recommendation, not accomplished work. Also surfaced OSSEs for air quality (ScienceDirect S1352231015301059 — not retrieved) |
| 38 | 2026-09-19 | WebSearch | `Rochoux wildfire spread data assimilation "observing system simulation experiment" twin experiment parameter estimation` | Rochoux EnKF/polynomial-chaos lineage; shape-oriented DA; FIREFLY. All evaluate **fire-state accuracy**, not decision quality. Category 1/8 territory — **not recorded here** |
| 39 | 2026-09-19 | WebSearch | `wildfire evacuation decision "synthetic truth" simulation experiment evaluating forecast value trigger buffer "nature run"` | 0 decision-OSSE hits. Returned the trigger-buffer lineage instead (WUIVAC/Larsen, Li et al. coupled fire-traffic, WUI-NITY/k-PERIL, Ronchi et al. verification) — all Category 1/3 |
| 40 | 2026-09-19 | WebSearch | `wildfire OSSE ... evacuation triggers protective action decision quality evaluation 2024 2025 2026` | 0 decision-OSSE hits. PADM/IoT, evacuation-behaviour prediction, Facebook-data evacuation analysis |
| 41 | 2026-09-19 | WebSearch | `"value of information" OR "observation impact" simulation experiment wildfire management decision synthetic truth fire model different from forecast model` | VOI framing exists for wildfire *management economics* (Frontiers Env. Sci. 2022 conceptual framework) but not as an OSSE. Surfaced **Xu et al. 2026 arXiv 2605.18911** |
| 42 | 2026-09-19 | Consensus | `observing system simulation experiment evaluating value of observations for emergency evacuation decisions rather than forecast skill` | **Quota exhausted (30/30 for the month) — query not executed.** Logged as an unexecuted intended query |

**Verdict recorded:** WG-C-010 → **UNKNOWN** (not SUPPORTED_CANDIDATE). See review §9.
Wording variants not yet tried: "perfect-model experiment", "synthetic-truth decision
experiment", "value-of-information simulation", "pseudo-observation decision experiment".
No non-English pass was performed.

---

## Round 8 — Calibration under shift, proper scoring, decision-focused evaluation

| # | Date | Source | Query | Usable hits |
|---|---|---|---|---|
| 43 | 2026-09-19 | Crossref API | DOI `10.1198/016214506000001437` | **Gneiting & Raftery 2007**, JASA 102(477):359-378. (Bibliographic query alone returned only the 2004/2005 DTIC technical reports — **report trap** avoided) |
| 44 | 2026-09-19 | Crossref API | `query.bibliographic=Can you trust your model's uncertainty ... Ovadia` | 0 usable — no Crossref record. Escalated to arXiv |
| 45 | 2026-09-19 | arXiv API | `all:"Can You Trust Your Model's Uncertainty"` | **Ovadia et al.**, arXiv:1906.02530v2, 2019-06-06, 9 authors verified. **No journal_ref, no DOI in the arXiv record** → venue recorded as PREPRINT/conference, DOI UNVERIFIED |
| 46 | 2026-09-19 | arXiv API | `all:"Conformal Prediction Under Covariate Shift"` | **Tibshirani, Barber, Candès & Ramdas**, arXiv:1904.06019v3, 2019-04-12. No journal_ref/DOI → PREPRINT/conference, DOI UNVERIFIED |
| 47 | 2026-09-19 | Crossref API | `query.bibliographic=Conformal Prediction Under Covariate Shift Tibshirani ...` | Returned the **successor** paper: Barber, Candès, Ramdas & Tibshirani 2023, 'Conformal prediction beyond exchangeability', Ann. Statist. 51(2), DOI 10.1214/23-aos2276 — recorded in review §7.3, not as metadata |
| 48 | 2026-09-19 | Crossref API | `query.bibliographic=Smart Predict then Optimize Elmachtoub Grigas Management Science` | **Elmachtoub & Grigas 2022**, Manage. Sci. 68(1):9-26, DOI 10.1287/mnsc.2020.3922 |
| 49 | 2026-09-19 | Crossref API | `query.bibliographic=Decision-focused learning foundations state of the art benchmark ... Mandi` | **Mandi et al. 2024**, JAIR 80:1623-1701, DOI 10.1613/jair.1.15320 |
| 50 | 2026-09-19 | Crossref API | `query.bibliographic=Are we really making much progress A worrying analysis of recent neural recommendation approaches` | **Ferrari Dacrema, Cremonesi & Jannach 2019**, RecSys '19, pp. 101-109, DOI 10.1145/3298689.3347058. **Conference proceedings, not a journal** — recorded as such |
| 51 | 2026-09-19 | WebSearch | `decision-focused evaluation fire prediction model IoU accuracy does not translate decision quality evacuation` | Surfaced arXiv 2603.22331 (conformal risk control for wildfire evacuation mapping) and arXiv 2605.18911 |
| 52 | 2026-09-19 | alphaXiv `discover_papers` | keywords: conformal risk control / wildfire evacuation mapping / decision-focused learning / predict-then-optimize / calibration under distribution shift | 14 returned. Confirms DFL is a mature named area (Mandi et al. 2307.13565, Sadana et al. 2306.10374) and surfaces wildfire-specific conformal risk control (2603.22331) |
| 53 | 2026-09-19 | alphaXiv `get_paper_content` | arXiv 2605.18911 | Full text of **Xu et al. 2026**, 'Does Your Wildfire Prediction Model Actually Work, or Just Score Well?' — **PREPRINT**. Defines "selection regret" = decision-score loss from choosing a head by PR-AUC rather than decision-F1. Filed **LOW threat to WG-C-014**: it is a classification-metric result, not an evacuation-decision result, but it narrows the claim |

---

## Verification / audit actions taken (Agent C role)

Every item recorded in `literature/metadata/` was resolved against a **retrieved record**,
not recall. Specific audit catches:

1. **Preprint/journal traps caught and resolved:** Lakens 2017 (OSF → SPPS); Cameron,
   Gelbach & Miller 2008 (NBER/SSRN → REStat); Lazic et al. 2018 (bioRxiv → PLOS Biology);
   Siepe et al. 2024 (PsyArXiv → Psychological Methods); Morris et al. 2019 (arXiv noted);
   Yu et al. 2019 (Copernicus discussion preprint carries a **different title** — "fraternal"
   vs "nonidentical" — and must not be cited as the journal article).
2. **Conference/journal traps caught:** Sargent has ≥5 near-identical WSC proceedings
   papers plus the *Journal of Simulation* article; the journal version is recorded.
   Ferrari Dacrema et al. 2019 is RecSys proceedings and is recorded as `conference`.
   Gneiting & Raftery has two DTIC technical reports predating the JASA article.
3. **Recall corrected against record:** Axtell et al. 1996 is "Aligning simulation models:
   A case study and results", **not** "…A cyclical approach" (the recalled subtitle was
   wrong and has been discarded).
4. **Fields left UNVERIFIED rather than filled:** Künsch 1989 page range (Crossref returns
   null); Siepe et al. 2024 volume/issue/pages (Crossref returns null); DOIs for Ovadia
   et al. 2019 and Tibshirani et al. 2019 (no DOI in the arXiv record, NeurIPS proceedings
   record not retrieved); Wirgin 2004 DOI.
5. **NEEDS_FULL_TEXT recorded, not paraphrased:** Kaipio & Somersalo 2007 (403 + elided
   abstract); Hoffman & Atlas 2016 (403 + unreadable PDF); Arnold & Dey 1986 and
   Atlas 1997 (cited secondhand via Yu et al. 2019 only); Errico et al. 2013;
   Privé 2021 Comment.
6. **No quotation was taken from any source whose text was not retrieved.** The notes for
   `sargent2013verification`, `morris2019simulation` and `kaipio2007inversecrime` state
   explicitly that no verbatim text was obtained.

---

## Coverage gaps in this sweep (blocking any SUPPORTED_CANDIDATE upgrade)

- **No non-English pass** (Korean, Japanese, French, Chinese). NOVELTY_STANDARD §5
  requires one.
- **Preprint coverage was arXiv/alphaXiv only** — no SSRN, OSF, EarthArXiv, or
  ESSOAr/ESS Open Archive sweep, which is where earth-science methodology preprints live.
- **Consensus quota exhausted at query #42**; the sharpest WG-C-010 adversarial query was
  never executed.
- **Wording variants for decision-level OSSEs not exhausted:** "perfect-model experiment",
  "synthetic-truth decision experiment", "value-of-information simulation",
  "pseudo-observation experiment", "closed-loop simulation evaluation".
- **Adjacent fields not swept for decision-level OSSEs:** flood/hurricane warning
  decision evaluation, public-health decision modelling, air-quality OSSEs
  (ScienceDirect S1352231015301059 identified but not retrieved).
