# 06 — Fire Spread Models

**Scope (Category 6):** the fire spread models WildfireGuardian *consumes*, their input requirements,
runtime class, documented error characteristics, ensemble capability, and whether prior work has used them
to support evacuation decisions.

**Framing.** This is not a physics review. WildfireGuardian does not build spread models
(`docs/PROJECT_CONTEXT.md`). The question this review answers is narrower and more useful:
**what does WildfireGuardian's OSSE have to assume, and how wrong is it allowed to assume the forecast is?**

**Compiled by:** Agent A/C (Search Researcher + Verification Auditor), 2026-09-19.
Query log: `docs/search-logs/agent-spread-observations.md`.

---

## 1. Model-by-model table

Runtime classes used below:
`RT` real-time (seconds; many runs feasible inside a decision) ·
`NRT` near-real-time (minutes per run; small ensembles feasible) ·
`HPC` cluster-scale (hours; not an in-decision ensemble) ·
`ML` learned emulator (sub-second per run after training).

Where a cell says `UNVERIFIED`, no retrieved source stated it. **No number in this table was estimated.**

| Model | Type | Inputs required | Outputs | Runtime class | Documented error characteristics | Ensemble-capable? | Used for evacuation decisions in prior work? |
|---|---|---|---|---|---|---|---|
| **Rothermel (1972)** `rothermel1972spread`, equations in `andrews2018rothermel` | Quasi-empirical (semi-empirical) surface ROS kernel | Fuel model (load, SAV, bed depth, moisture of extinction), dead + live fuel moisture, midflame wind, slope | Steady-state surface ROS, reaction intensity | RT (closed form) | Relative error up to 50% on Karst fuels (`zhang2023karst`); failed to spread in nearly all 240 live chaparral fires at default values (`weise2016chaparral`); see §3 for the cross-study synthesis | Only as a kernel inside an ensemble driver | Indirectly — it is the kernel under FARSITE in `cova2005trigger`, PERIL, k-PERIL |
| **FARSITE** `finney1998farsite` | Deterministic 2-D growth (Huygens wavelet) over Rothermel + crown + spotting | Gridded fuel model, canopy (cover, height, base height, bulk density), elevation/slope/aspect, gridded weather + winds, fuel moisture, ignition | Fire arrival time, perimeter, intensity, flame length | NRT | Mean Jaccard **0.176**, Sorensen **0.274**, Cohen's kappa **0.249** on a historic CONUS set (`elmfire2025validation`); Sorensen 0.69 vs 0.77 for MTT in a two-case comparison (secondary source, E3) | Only by external Monte Carlo wrapping | **Yes** — the engine behind PERIL (`mitchell2023peril`) and one member of the ensemble in `kalogeropoulos2026ensemble` |
| **FlamMap / MTT** | Deterministic minimum-travel-time over Rothermel | As FARSITE, with constant weather | Arrival time, major flow paths, burn probability | NRT | Sorensen 0.77 in a two-case comparison; both FARSITE and MTT over-estimated burned area, FARSITE more so (secondary source, **E3**, not separately filed) | Yes (burn probability / FSim lineage) | Trigger-buffer literature uses the arrival-time surface |
| **ELMFIRE** `lautenberger2013elmfire` | Semi-empirical level-set (Rothermel + CFFDRS) with crown transition and spotting | Gridded fuels, topography, weather, moisture (GeoTIFFs) | Time of arrival, fireline intensity, spread rate, flame length (raster) | RT–NRT, MPI-parallel, laptop→cluster | Mean Jaccard **0.178**, Sorensen **0.278**, kappa **0.241** (`elmfire2025validation`); on the 2001 Dogrib fire it under-predicted relative to Prometheus and observation | **Yes, natively** — MPI Monte Carlo ensemble mode; PyreCast runs **1000 members per fire** (operator doc, E2) | **Yes** — ensemble member in `kalogeropoulos2026ensemble`; PyreCast 10/50/90 percentile envelopes are consumed operationally |
| **Prometheus / W.I.S.E.** (Canada), assessed in `bennett2026wise` | Semi-empirical, Canadian FBP system | FBP fuel type grid, topography, hourly weather, FWI moisture codes, ignition | Perimeters, arrival time, head/flank/back ROS | NRT | **19,848 fire-days / 2,210 fires.** Default parameters: F1 **0.259**, IoU **0.194**, precision **0.200**, recall **0.856**, Hausdorff **2828 m**. Hindsight-optimised burn duration: F1 0.498, IoU 0.284. Plus wind direction: F1 0.539, IoU 0.309 | Yes (scenario ensembles) | **Yes** — Prometheus/WISE is an ensemble member in `kalogeropoulos2026ensemble` |
| **WRF-SFIRE** `mandel2014wrfsfire` | Coupled atmosphere–fire (NWP + semi-empirical spread + prognostic dead fuel moisture) | Full NWP initial/boundary conditions, fuel map, terrain, plus satellite fire detections for assimilation | Fire perimeter + arrival time **and** fire-induced winds, plume, smoke | **HPC** (explicitly requires high-performance computing, per `roysingh2025constellation` §3) | UNVERIFIED as a quantitative agreement statistic in retrieved sources | In principle; cost is prohibitive for large decision-time ensembles | Not for evacuation timing in retrieved sources |
| **FIRETEC** `linn2002firetec` | Physical / CFD, fully resolved combustion-atmosphere | 3-D fuel structure, atmospheric state, fine-scale terrain | Resolved fire behaviour, fire–atmosphere interaction | **HPC** (research scale) | Physically based models were the only ones within a factor of two of observed live-fuel ROS (`weise2016chaparral`) | No (not at decision time) | No |
| **SPARK** `miller2015spark` | Level-set on GPU, pluggable empirical ROS | Fuel/vegetation grid, terrain, weather, ROS rule set | Perimeter evolution, arrival time | RT (GPU) | UNVERIFIED in retrieved sources | Yes (low per-run cost) | Not in retrieved sources |
| **ML emulators — Allaire** `allaire2021emulation` | Deep NN emulating a physical simulator | Landscape spatial fields + scalar environmental inputs | 1-hour burned area | **ML** — speed-up factor "several thousands" on 32 cores; whole of Corsica in under a minute | Burned-area **MAPE 32.8%** against the simulator it emulates (not against reality) | Yes — emulation exists specifically to make ensembles affordable | Fire danger mapping, not evacuation |
| **ML surrogate + DA — Cheng** `cheng2022surrogate` | ROM + LSTM surrogate with latent data assimilation | Historical simulation training set; daily satellite perimeters as observations | Fire progression forecast | **ML** — ~1000× faster than the cellular-automata simulator | DA + covariance tuning cut relative RMSE by ~50% vs no assimilation; absolute skill UNVERIFIED | Yes | No |
| **Ensemble framework — Allaire** `allaire2020ensemble` | Monte Carlo over input uncertainty, single spread model | Input probability distributions + all simulator inputs | Burn probability map + proper probabilistic scores | NRT × hundreds of members | "Fair performance in some of the cases"; accuracy and reliability both flagged as needing improvement, on 7 Corsican fires | **Yes — this is the ensemble paper** | No (decision layer absent) |
| **Stochastic trigger modelling** `ramirez2019stochastic` | Monte Carlo perturbation of inputs, any empirical propagation engine | Fire model inputs + deviation ranges | **Probability map of fire arrival at the asset to be protected**; probabilistic trigger buffers | RT (authors state it may be solved in real time) | UNVERIFIED (Tubbs fire case study) | Yes | **Yes — explicitly for evacuation trigger buffers** |
| **Multi-model ensemble triggers** `kalogeropoulos2026ensemble` | Ensemble of five heterogeneous engines: FARSITE, Prometheus/WISE, ELMFIRE, Google EPD, EPD-ConvLSTM | Each member's own inputs, common landscape | **Probabilistic evacuation trigger boundaries** | Mixed (NRT + ML) | Individual models produce *different* trigger boundaries, attributed to differences in fuel representation, fire dynamics and spread rates | **Yes — multi-model, not multi-input** | **Yes — this is exactly and only what it is for** |
| **DA schemes (ETKF / DEnKF)** `zha2024distributed`, `wu2025denkf` | Ensemble Kalman family over a spread model | Spread model + fire-front observations + observation error covariance | Corrected fire front, forward forecast | NRT per assimilation cycle | Both validated **by OSSE**, not against real fires | Yes (ensemble is intrinsic) | No |
| **Conformal spread models** `dayan2026conformal` | ML (LightGBM / U-Net / ResGNN-UNet) + conformal risk control | Gridded spread predictors | SAFE / MONITOR / EVACUATE zones with FNR ≤ 0.05 | ML | AUROC up to 0.969, yet **standard thresholds captured only 7–72% of actual spread** | Yes | **Yes — zones are the decision output** |

---

## 2. Assumptions WildfireGuardian inherits

Every one of these arrives through the spread model, not through anything we build. They must be declared in the
methods section, because each is a way our result could be wrong for reasons that have nothing to do with our
decision logic.

### A1. Steady-state spread — `rothermel1972spread`
Rothermel's equation predicts **equilibrium** spread rate. Acceleration, and the sudden runs that actually cause
entrapment, are outside it. FARSITE, FlamMap, ELMFIRE, SPARK and the surface component of WRF-SFIRE all inherit
this. **Consequence for us:** a dispatch deadline computed from a steady-state arrival-time field is
systematically optimistic in exactly the scenarios where it matters most.

### A2. Homogeneous, continuous fuel beds calibrated on laboratory arrays — `rothermel1972spread`, `weise2016chaparral`
The kernel was fitted to uniform-particle laboratory beds (excelsior and sticks). Weise et al. show it fails
outright in live fuels. **Consequence for us:** Korean *Pinus densiflora* on steep terrain is further from the
calibration domain than chaparral is; we may not assume US fuel-model ROS transfers, and
`docs/NOVELTY_STANDARD.md` §4(b) makes documenting that failure a legitimate (and the only strong) Korean
novelty route.

### A3. Fire growth is an elliptical/Huygens expansion from a point or line — `finney1998farsite`, `papaioannou2026adaptive`
The 2-D growth engines and the adaptive-sensing literature alike assume local elliptical expansion. Spotting is
bolted on as a separate submodel. **Consequence for us:** long-range spotting — which is what cut off escape
routes in several of the fatal fires our motivation rests on — is the least-modelled and most
decision-relevant mechanism in the chain.

### A4. Input uncertainty dominates structural uncertainty — `allaire2020ensemble` vs `kalogeropoulos2026ensemble`
Almost all "ensemble fire prediction" is Monte Carlo over *inputs* of a *single* model. Kalogeropoulos & Rein
falsify the sufficiency of that: five different engines on the same landscape produce **different trigger
boundaries**. **Consequence for us:** an OSSE whose forecast error is generated by perturbing one model's inputs
understates real forecast error, and is a species of the inverse-crime problem `docs/FAILURE_MODES.md` §2 already
warns about. If we use a single engine for both truth and forecast, we must say so and treat our skill axis as a
lower bound on error.

### A5. Fire-position observation is sparse, late and biased — `nasafirms2026latency`, `sung2025geostationary`, `hall2023geostationary`
Every assimilating model in the table (`cheng2022surrogate` daily perimeters; `zha2024distributed` asynchronous
fronts) is bounded by what can actually be observed. **Consequence for us:** see
`literature/reviews/07-observations-remote-sensing.md`. This is the assumption WG-C-012 is built on.

*(Runner-up, not in the top five but worth stating: **A6 — validation is against burned area, not against arrival
time at a location.** Every agreement statistic in §3 is a set-overlap measure over a daily or final perimeter.
None of them tells us the error in "when will fire reach this house", which is the only quantity our deadline
needs.)*

---

## 3. Documented error magnitudes we can cite for forecast-skill ranges

All figures below were read in a retrieved source. Evidence level in brackets.

### 3.1 Rate-of-spread error (scalar)

| Source | Scope | Reported error |
|---|---|---|
| `cruz2013uncertainty` **[E2]** | 49 evaluation datasets, 1278 observations, 7 fuel type groups | Only **3%** of predictions exact; **mean percent error 20–310%**; **over half of datasets 51–75%**; authors propose **±35%** as reasonable model performance |
| `weise2016chaparral` **[E2]** | 240 laboratory live-chaparral fires | Rothermel "failed to predict fire spread in nearly all of the fires that spread using default values"; models correct **49–69%** of the time; **only physical models within a factor of two** |
| `zhang2023karst` **[E2]** | Karst ecosystem fuels, China, lab | Direct Rothermel relative error **up to 50%** |
| Geng et al. 2026, *IJWF* **[E3, not filed]** | *Pinus koraiensis*, lab | Direct Rothermel **MAE 0.201 m/min, MRE 35.01%**, systematic over-prediction |
| Xu et al. 2025, *IJWF* **[E3, not filed]** | Mixed *P. koraiensis*/*Q. mongolica*, wind | Uncalibrated Rothermel **MAE 2.536 m/min, MRE 135.1%**; after wind-coefficient and reaction-intensity calibration **MRE 24.9%** |

### 3.2 Spatial agreement of operational fire growth models (set overlap)

| Source | Model | Sample | Agreement |
|---|---|---|---|
| `bennett2026wise` **[E1, publisher page]** | W.I.S.E. (Canada), default params | 19,848 fire-days / 2,210 fires | **F1 0.259, IoU 0.194**, precision 0.200, recall 0.856, Hausdorff 2828 m |
| `bennett2026wise` | W.I.S.E., hindsight-optimised duration + wind | same | **F1 0.539, IoU 0.309** |
| `elmfire2025validation` **[E1, software doc]** | ELMFIRE | historic CONUS set | **Jaccard 0.178, Sorensen 0.278, kappa 0.241** |
| `elmfire2025validation` **[E1, software doc]** | FARSITE, same pipeline | historic CONUS set | **Jaccard 0.176, Sorensen 0.274, kappa 0.249** |
| `dayan2026conformal` **[E2, preprint]** | ML spread models | held-out | AUROC to 0.969, but standard thresholds captured only **7–72%** of actual spread |

**The headline sentence WildfireGuardian may defend:** *three independent operational fire growth models —
W.I.S.E., ELMFIRE and FARSITE — agree with observed fire extent at an intersection-over-union of roughly 0.17–0.20
under default parameterisation, and even hindsight tuning of burn duration and wind direction only lifts that to
about 0.31.* Sources: `bennett2026wise`, `elmfire2025validation`.

### 3.3 Emulation error (the cost of making an ensemble affordable)

| Source | Speed-up | Error against the simulator |
|---|---|---|
| `allaire2021emulation` **[E2]** | several thousand × (32 cores) | burned-area **MAPE 32.8%** |
| `cheng2022surrogate` **[E2]** | ~1000 × vs cellular automata | DA + covariance tuning reduced relative RMSE by ~50% |

Note the compounding: an emulator with 32.8% burned-area error sitting on a simulator at IoU ~0.19.
Emulation error is *additional to*, not instead of, model error.

### 3.4 What we could **not** verify

- **Error growth with lead time.** Not a single retrieved source reports forecast error as a function of forecast
  horizon for wildfire spread. `bennett2026wise` is daily; `cruz2013uncertainty` is horizon-free. **This is the
  most important gap in Category 6 for WG-C-002 and WG-C-012**, because a skill-versus-lead-time surface is
  exactly what RQ1's boundary lives on. We currently have no published curve to anchor it. Recorded as an open
  question; do not invent a decay rate.
- **Arrival-time error at a point.** See A6. All published agreement statistics are areal.
- **Runtime in wall-clock seconds** for FARSITE, FlamMap, W.I.S.E., WRF-SFIRE and FIRETEC on a stated landscape
  and hardware. The runtime column above is a qualitative class, not a measurement.

---

## 4. Claim implications

| Claim | Effect of this review | Recommended status |
|---|---|---|
| **WG-C-004** — probabilistic / ensemble fire predictions define trigger boundaries | **Occupied three times over**: `ramirez2019stochastic` (stochastic trigger buffers, 2019), `kalogeropoulos2023kperil` (k-PERIL stochastic boundaries), and decisively `kalogeropoulos2026ensemble` (**multi-model** ensemble of FARSITE + Prometheus/WISE + ELMFIRE + Google EPD + EPD-ConvLSTM, purpose-built for evacuation triggers) | **OCCUPIED** |
| **WG-C-002** — forecast-skill boundary vs tuned trigger | No retrieved work reports decision performance as a function of forecast skill against an *optimised* positional-trigger baseline. But §3.4 shows we lack the published skill-vs-lead-time evidence to place such a boundary in a defensible range | **UNKNOWN**, with a named evidence gap |
| **WG-C-010** — OSSE for wildfire | OSSE is a standard, named method in wildfire spread data assimilation (`zha2024distributed`, `wu2025denkf`, plus Wu et al. 2024 *Fire Ecology*, Zhang et al. 2017 FIREFLY). The methodology is not ours to claim | **WEAKENED** — narrow to "OSSE evaluating an evacuation *decision*", and expect that to be attacked |
| **WG-C-014** — spatial accuracy ≠ decision quality | §3.2 shows the field's currency is set overlap and §3.4 shows nobody connects it to decisions. `dayan2026conformal` shows accuracy ≠ *adequacy* but not non-monotonicity | **UNKNOWN**, premise well-evidenced |
| **WG-C-009** — robust protectability under model error | `kalogeropoulos2026ensemble` reports Fort McMurray triggers extending beyond practical detection distances — i.e. a demonstrated un-protectability result | **UNKNOWN**, under pressure; needs full text |

---

## 5. Open questions

1. **Does any published work report wildfire forecast error as a function of lead time?** Nothing found.
   If it does not exist, WildfireGuardian must generate its own error-growth curve and label it as an assumption,
   not as evidence.
2. Does `kalogeropoulos2026ensemble` compare *decision outcomes* between ensemble members, or only boundary
   geometry? Paywalled. **NEEDS_FULL_TEXT — highest priority.**
3. What is the wall-clock runtime of an N-member ELMFIRE or W.I.S.E. ensemble on a stated landscape? The
   ensemble-in-decision-time question is currently answered only by operator documentation (PyreCast: 1000 members,
   ~12-hourly re-initialisation, 14-day horizon — **E2**).
4. No Korean-language search was run (RISS/KCI/DBpia). NIFoS and KFS spread-model work is unsampled.
5. Backward and forward citation chases on `kalogeropoulos2026ensemble` and `bennett2026wise` are not done.
