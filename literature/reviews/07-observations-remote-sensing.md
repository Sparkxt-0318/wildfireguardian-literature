# 07 — Wildfire Observations and Remote Sensing

**Scope (Category 7):** what can actually be observed about a running wildfire, at what resolution, how often,
and — the column that matters most for WildfireGuardian — **how late**.

**Why this review exists.** WG-C-012 claims forecast *latency*, not only skill, is a first-class decision
variable. That claim is only meaningful if the latency numbers are real. This review assembles them from
retrieved sources and refuses to fill gaps with plausible-sounding values.

**Compiled by:** Agent A/C, 2026-09-19. Query log: `docs/search-logs/agent-spread-observations.md`.

---

## 1. Observation modality table

**Reading the table.** "Directly observed" is the physical measurement. "Inferred" is everything a
decision-maker actually wants, which is derived. The gap between those two columns is where most of the
uncertainty in a fire-position estimate lives, and it is routinely elided in operational discussion.

`UNVERIFIED` means no retrieved source stated it. **Nothing here was estimated.**

| Modality | Spatial resolution | Cadence / revisit | Latency to availability | Directly observed quantity | Inferred quantity | Source |
|---|---|---|---|---|---|---|
| **VIIRS I-band active fire (S-NPP, NOAA-20, NOAA-21)** | **375 m** (detection reported at pixel centre) | Polar orbit; per-satellite overpasses only. Exact revisit UNVERIFIED | **NRT ~3 h** global [E2]; **RT 20–30 min**; **URT <60 s** (VIIRS ~50 s) — URT/RT only via direct-readout ground stations, **CONUS/Canada only** | Radiance anomaly in mid-IR → a *detection point* | Fire presence, rough front location, FRP; perimeter and ROS are further inferences | `schroeder2014viirs`; `nasafirms2026latency` |
| **MODIS active fire (Terra, Aqua), Collection 6** | **1 km** | Polar orbit; exact revisit UNVERIFIED | **NRT ~3 h** [E2]; **URT ~25 s** via direct readout (CONUS/Canada only) | Radiance anomaly → detection point | As above, coarser | `giglio2016modis`; `nasafirms2026latency` |
| **GOES-R ABI, Fire Detection & Characterization (FDC)** | **2 km** | **10 min full disk; 5 min CONUS/PACUS; 30–60 s mesoscale sector** (15 min full disk before April 2019) | UNVERIFIED as a stated product latency; cadence is the effective bound | FRP, instantaneous fire temperature, fire size, fire mask | Fire growth rate, front position | `hall2023geostationary` (Section 2.1) |
| **GOES-R ABI — accuracy** | — | — | — | — | **False alarm 4–7% (high-confidence pixels); was 48% in summer 2018 → 4% in 2020.** Pixel locations **not terrain-corrected**: positioning error "on the order of several kilometres depending on terrain elevation and view zenith angle" | `hall2023geostationary` |
| **LSA-SAF FRP-PIXEL (MSG SEVIRI and others)** | UNVERIFIED | **15 min** full SEVIRI disk | UNVERIFIED | FRP | Fire intensity, energy release | `hall2023geostationary` |
| **Himawari AHI** | UNVERIFIED in retrieved text | UNVERIFIED in retrieved text | UNVERIFIED | Active fire detection / FRP | — | `hall2023geostationary` (validated, specs not extracted) |
| **GK2A / AMI (Korea)** | **2 km** infrared channels; 500 m–1 km visible/NIR | **Full disk and East Asia: 10 min. Korean Peninsula local area: 2 min** | **Average detection delay 12.9 min** (LGBM detector, March 2025 Korean fires) | SWIR 3.8 µm and LWIR 9.6/11.2 µm brightness | Fire detection (**recall 0.329, precision 0.987, F1 0.494**) | `sung2025geostationary` |
| **MTG-FCI (Meteosat Third Generation)** | UNVERIFIED | **10 min** over Europe/Africa | UNVERIFIED | Hotspot detections, FRP | Persistent fire-event identity, geometry, and **rate of spread updated every 10 min** | `paugam2026mtgfci` (PREPRINT) |
| **Tasked satellite constellation (CYGNSS, GNSS-R)** | UNVERIFIED | Scheduled by MIP; 98–100% of available opportunities captured | **Observation-to-downlink <24 h; end-to-end workflow 6–30 h** (vs "multiple days" currently) | GNSS-R specular reflections (sees through cloud and smoke) → soil moisture | Fire danger, burn prediction, fire arrival time for WRF-SFIRE assimilation | `roysingh2025constellation` (PREPRINT) |
| **Ground camera networks (ALERTCalifornia / ALERTWildfire type)** | UNVERIFIED | Continuous video | Alerts "within minutes" of AI detection; operator reports >50% of 2025 alerts preceded any 9-1-1 call, earliest 2.5 h before | Visible/NIR imagery of smoke column | Ignition location and bearing; **not** fire perimeter, **not** ROS | **Operator press material only — E3. Deliberately not filed as a metadata record.** No peer-reviewed performance figures retrieved |
| **UAV / drone thermal imagery** | GSD ~17.6 cm/px at 122 m AGL (secondary source, **E3**); sensors commonly 640×512 | Flight-limited; UNVERIFIED | UNVERIFIED | Radiometric thermal field over a local fire segment | Active fire edge, heat intensity, spot fires across control lines | FLAME 3 dataset and UAV segmentation literature located but **no verified latency or ROS-accuracy numbers found** |
| **UAV fleet with planned observation (SAOP)** | UNVERIFIED | Determined by the plan | UNVERIFIED | Aerial fire observations fused into a fire map | Fire perimeter and its evolution; a spread forecast then defines the next observation plan | `bailonruiz2022uavfleet` |
| **Adaptive single-drone monitoring** | UNVERIFIED | Rolling finite horizon | UNVERIFIED | Point/local measurements along a chosen trajectory | Posterior over the fire front; trajectory chosen to minimise that posterior's uncertainty | `papaioannou2026adaptive` (PREPRINT, simulation only) |
| **Satellite-derived daily perimeters (e.g. CFSDS)** | Perimeter polygons from satellite detections | **Daily** | UNVERIFIED | Aggregated detections → a closed perimeter | Daily burned area; used as *truth* for model validation and as the observation in assimilation | `bennett2026wise`; `cheng2022surrogate` |

### 1.1 What is never directly observed

No modality in the table observes any of the following. Each is an inference, and each one carries its own error
on top of the detection error:

- **The fire front as a continuous line.** Every satellite product yields *points* or *pixels*. A perimeter is a
  reconstruction.
- **Rate of spread.** Always differenced between two observations, so its error is the detection geolocation
  error divided by the cadence. At GK2A's 2 km pixel and 2-minute Korean cadence, the geolocation error dominates
  completely: a 2 km positional uncertainty across a 2-minute interval is an ROS uncertainty of order 60 km/h.
  **This is why high cadence does not by itself give usable ROS.**
- **Spotting.** No retrieved source reports operational spotting detection.
- **Fire arrival time at a specific address** — the quantity WildfireGuardian's deadline is a function of.
- **Road trafficability under fire conditions**, which RQ2's ingress leg depends on entirely.

---

## 2. What this implies for achievable forecast latency

This section is the evidence base for **WG-C-012**.

### 2.1 The total lag budget

A forecast-aware decision cannot be made until: the fire is observed → the observation is delivered → the
observation is assimilated → the forecast is run → the forecast is interpreted → the decision is issued. Only
the first two are documented in Category 7; the rest is our own modelling responsibility. What we can say with
verified numbers:

| Stage | Best verified case | Typical verified case | Source |
|---|---|---|---|
| Detection delay (geostationary, Korea) | — | **12.9 min mean** | `sung2025geostationary` |
| Delivery, polar-orbiting NRT | **<60 s** (URT, direct readout, **US/Canada only**) | **~3 h** (NRT, global) [E2] | `nasafirms2026latency` |
| Delivery, polar-orbiting RT | 20–30 min (direct readout footprint only) | — | `nasafirms2026latency` |
| Delivery, geostationary | bounded by scan cadence: **2 min** (GK2A Korea local), 5 min (GOES CONUS), 10 min (full disk), 15 min (SEVIRI) | — | `sung2025geostationary`, `hall2023geostationary` |
| Tasked constellation, end-to-end | **6–30 h** | previously "multiple days" | `roysingh2025constellation` |
| Assimilation cadence in published fire DA | **daily** satellite perimeters | — | `cheng2022surrogate` |
| Operational forecast re-initialisation | ~**12-hourly** from satellite heat detection (PyreCast) [E2] | — | operator documentation |

### 2.2 The three consequences for WildfireGuardian

**C1 — The fast latency tier does not exist over Korea.** Sub-minute FIRMS URT is a direct-readout product for
the continental US and Canada. Korea's fastest verified channel is GK2A, whose published mean detection delay is
**12.9 minutes** at **2 km**. Any WildfireGuardian experiment that assumes minute-scale, high-resolution fire
position over Korea is assuming an observing system that has not been shown to exist. This is a concrete,
citable Korean-specific constraint and therefore a legitimate route under `NOVELTY_STANDARD` §4(a).

**C2 — Recall, not latency, may be the binding constraint.** `sung2025geostationary` reports **recall 0.329**. A stream
that misses roughly two out of three observations is not a continuous fire-position signal; it is a sparse and
probably biased sample. Modelling "the forecast arrives 13 minutes late" while assuming every observation arrives
would be the wrong model of the Korean observing system.

**C3 — Latency is structurally coupled to resolution, and the coupling is adverse in Korea.** The fastest
modality (geostationary, 2 min) is also the coarsest (2 km) and the worst geolocated in steep terrain —
`hall2023geostationary` puts ABI positioning error at "the order of several kilometres depending on terrain
elevation and view zenith angle", and Korea is both mountainous and at a substantial view zenith angle from
geostationary. The finest routinely available modality (VIIRS, 375 m) is the slowest to arrive outside North
America (~3 h). **There is no verified modality that is simultaneously fast, fine and well-geolocated over
Korean terrain.** That trade-off is a real research object, and it is the sharpest thing WG-C-012 has going for
it.

### 2.3 Honest statement of what latency evidence does *not* support

- We have **no verified end-to-end measurement** of "time from ignition to a forecast on a decision-maker's
  screen" for any operational Korean system. The 12.9 min figure is detection delay only.
- We have **no verified relationship between observation latency and forecast error.** That is exactly the
  relationship WG-C-012 asserts matters, and it is currently unmeasured in the retrieved literature.
  We must generate it ourselves and label it as our own result, not cite it as background.
- A search snippet attributed a ~300-minute median end-to-end latency and a 24-hour forecast IoU of 0.84 to
  Moldamurat et al. 2026 (*Natural Hazards Research* 6(2):516–533). The DOI is verified but the **full text was
  not retrieved and these numbers are not used anywhere in this repository.**

---

## 3. Korea and GK2A

### 3.1 The system
GEO-KOMPSAT-2A (GK2A), operated by the National Meteorological Satellite Center of the Korea Meteorological
Administration, carries the Advanced Meteorological Imager (AMI). Wildfire detection products over East Asia
have been provided since 2018. Infrared channels are **2 km**; visible/near-IR bands run 500 m–1 km. The AMI
scans the **full disk every 10 minutes and the Korean Peninsula every 2 minutes** — a cadence advantage over
GOES full-disk and MSG. Detection uses regionally optimised contextual algorithms on SWIR 3.8 µm and LWIR
9.6 µm / 11.2 µm, with lapse-rate correction. [`sung2025geostationary`; corroborated by WebSearch of NMSC/KMA material]

### 3.2 The March 2025 South Korea wildfires
`sung2025geostationary` is the retrieved peer-reviewed analysis of GK2A performance during the March 2025 fires — the
event WildfireGuardian's Korean motivation will rest on. Reported: **recall 0.329, precision 0.987, F1 0.494,
average detection delay 12.9 minutes.** The authors note that real-time tracking of fire progression "can support
timely decision-making" but do not implement or evaluate any decision workflow. The gap between "can support
decision-making" and *demonstrating* it is, precisely, the space WildfireGuardian is aiming at.

### 3.3 What is NOT established for Korea
- **No published rate-of-spread validation study** for the March 2025 Uiseong/Andong fires was found. A figure
  of 7.4 km/h circulates on non-academic Korean blogs; it is **not recorded and must not be cited.**
- **No published Korean fire spread model validation** against those fires.
- **No published GK2A product latency** (as distinct from detection delay).
- **No Korean-language database pass was performed** (RISS, KCI, DBpia). Korean NIFoS/KFS technical reports are
  therefore unsampled, and this blocks promoting any Korea-related claim to `SUPPORTED_CANDIDATE` under
  `NOVELTY_STANDARD` §5.
- Korean fuel work that *was* located but not filed here (Category 6/8 territory): a *Pinus densiflora* wildfire
  fuel-load model from a forest-growth model (*Forests* 13:1372) and the Korean Forest Fire Smoke Dispersion
  Prediction system (*Forests* 10:219). Flagged for whichever agent owns Korean fuels.

---

## 4. Claim implications

| Claim | Effect of this review | Recommended status |
|---|---|---|
| **WG-C-012** — forecast latency as a first-class decision variable | Latency is *budgeted* in prior work (`roysingh2025constellation` 6–30 h; `zha2024distributed` treats observation staleness as the central problem) but is never **traded against decision value**. The Korean latency/resolution/recall constraints in §2.2 are real, verified and specific | **UNKNOWN**, best-evidenced of our surviving claims |
| **WG-C-008** — decision-directed wildfire sensing | Observation targeting in wildfire exists and is well developed, but every retrieved objective is **accuracy- or coverage-driven**: `zha2024distributed` targets the fastest-spreading front; `papaioannou2026adaptive` minimises estimation uncertainty; `roysingh2025constellation` maximises a science reward with active fire weighted ×10; `braydwood2026quantum` maximises scheduling efficiency; `bailonruiz2022uavfleet` covers the predicted perimeter. None optimises a protective-action consequence. But the *decision-focused* objective itself is occupied in an adjacent hazard (`sun2025decisionfocusedsensing`, flood) and the general method is a mature field (`veiga2023activesensing`) | **WEAKENED** — survives only as the wildfire+deadline instantiation, and only if we demonstrate a case where the two objectives choose different observations |
| **WG-C-007** — Korean-setting analysis | Korean-setting wildfire remote sensing is already published (`sung2025geostationary`) on the exact 2025 fires. "First in Korea" is unavailable on the observation side. §2.2 C1/C3 offer a legitimate §4(a) route instead: the Korean observing system has a documented fast/fine/well-geolocated trade-off that published (US) settings do not | **UNKNOWN**, reframe required |

---

## 5. Open questions

1. What is GK2A's stated **product latency** (not detection delay)? Not found. KMA/NMSC documentation, likely
   Korean-language.
2. MTG-FCI spatial resolution and product latency — not obtained from `paugam2026mtgfci`. NEEDS_FULL_TEXT.
3. Himawari AHI resolution and cadence — validated in `hall2023geostationary` but the specifications were not in
   the extracted text.
4. Is there any **peer-reviewed** evaluation of ground camera network detection timing? Only operator press
   material was found, and it is not citable at this repository's standard.
5. Is there any published measurement of **observation latency versus forecast error** for wildfire? Nothing
   found. If it does not exist, it is WildfireGuardian's to produce — and to label as a result, not a citation.
