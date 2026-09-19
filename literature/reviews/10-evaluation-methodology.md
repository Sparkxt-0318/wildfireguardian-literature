# Category 10 — Evaluation Methodology

**Agent:** A/C (Search Researcher + Verification / Citation Auditor)
**Date:** 2026-09-19
**Claims in scope:** WG-C-002, WG-C-006, WG-C-010, WG-C-014 (and, indirectly, every claim
that rests on simulated evidence)
**Search log:** `docs/search-logs/agent-evaluation.md`

> This is an **operational manual**, not a survey. Each section states what the literature
> requires of WildfireGuardian and what happens if we ignore it. Every requirement carries
> a citation. Where the full text was not obtained, this is marked — do not upgrade an
> abstract-level reading into a quotation.

---

## 0. The shape of the attack

Almost nothing in this category threatens WildfireGuardian's *novelty*. Everything in it
threatens WildfireGuardian's *validity*. That distinction matters for how the program
should treat these papers: they are not competitors, they are the conditions under which
our results are allowed to count.

Four attacks are available to a competent reviewer or judge, and all four are cheap:

| # | Attack | Section |
|---|---|---|
| 1 | "What is your n? Those scenarios are not independent." | §1, §2 |
| 2 | "You did not beat your baseline; you failed to reject a difference." | §3 |
| 3 | "Your fire model produced both the truth and the forecast. That is an inverse crime / identical twin, and it flatters you." | §5, §6 |
| 4 | "Your forecast is calibrated on the same distribution you evaluate on." | §7 |

The checklist in §8 closes all four.

---

## 1. Pseudoreplication and our unit of analysis

**The error.** Hurlbert (1984) defines pseudoreplication as "the use of inferential
statistics to test for treatment effects with data from experiments where either
treatments are not replicated ... or replicates are not statistically independent"
(Abstract, p. 187) — equivalently, "testing for treatment effects with an error term
inappropriate to the hypothesis being considered". He found it in 27% of 176 surveyed
experimental studies.

**Why it is ours.** WildfireGuardian generates many scenarios per fire event: perturbed
ignition points, wind draws, resident placements, responder base locations. Those
scenarios share the event's terrain, fuel field, road network and weather regime. They are
subsamples of one event, not replicates of the treatment. A t-test or bootstrap over
n = 2,000 scenarios drawn from 6 events reports the precision of a 2,000-sample study
while carrying the information of a 6-sample one.

**The unit taxonomy to adopt.** Lazic, Clarke-Williams & Munafò (2018) separate the
*biological unit* (here: the fire event), the *experimental unit* (here: the policy
applied to an event), and the *observational unit* (here: the scenario). Their survey
found only 22% of a random sample of animal studies replicated the correct
entity–intervention pair; 46% pseudoreplicated. Adopt their three-level vocabulary
verbatim in our methods section — it makes the design legible in one paragraph.

**Note the counter-literature, honestly.** Oksanen (2001, *Oikos*), Davies & Gray (2015,
*Ecology and Evolution*) and Colegrave & Ruxton (2017, *TREE*) argue the doctrine is
applied dogmatically and that non-independence and pseudoreplication are not the same
thing. All three were read in abstract only (E2) and are not recorded as metadata items.
Their relevance to us is narrow: they defend large-scale designs where replication is
impossible. That defence is available to us for *real* events; it is not available for
*simulated* scenarios, which we can generate at will and therefore cannot claim we were
forced to pseudoreplicate.

**Requirement R1 (see §8).**

---

## 2. Event-level bootstrap — the recipe

### 2.1 Choosing the cluster
Cameron & Miller (2015), *J. Human Resources* 50(2):317–372, is the practitioner's guide:
cluster at the level at which the errors are correlated and at which the treatment varies.
For us that is the **fire event**. Not the scenario. Not the grid cell. Not the household.

### 2.2 The small-G problem — this is our regime
Cameron, Gelbach & Miller (2008), *REStat* 90(3):414–427, show that asymptotic
cluster-robust tests over-reject with "few (five to thirty) clusters": nominal 5% tests
reject at 10%. WildfireGuardian will plausibly have **G < 10 events**. We are not near the
edge of this problem; we are deep inside it.

### 2.3 The procedure
1. Fit the comparison (forecast-aware policy vs tuned trigger) with the event as cluster.
2. Compute the test statistic t̂.
3. **Wild cluster bootstrap with the null imposed:** re-estimate under H0, then for each
   bootstrap replication draw one weight v_g per *event* and multiply that event's entire
   residual vector by it: y*_g = X_g β̃ + û_g · v_g. The whole cluster shares v_g — that is
   what preserves within-event dependence. Recompute t*.
   *(Verify the exact DGP against Cameron, Gelbach & Miller 2008 §3 before implementing;
   the form above is recorded from the abstract-level reading plus standard practice.)*
4. p = fraction of |t*| ≥ |t̂|.
5. **Weights:** Rademacher (±1) if G ≥ ~11. Below that, the p-value is not point
   identified and Webb's (2014) 6-point weights are the standard remedy (abstract only,
   E2 — follow up before use).
6. Report G, the weight scheme, and the number of bootstrap replications next to every
   p-value. With G = 6 and Rademacher weights, the smallest attainable p-value is 2/2^6;
   say so rather than reporting "p < 0.05".

### 2.4 Serial dependence inside an event
Scenarios indexed along a fire's timeline are serially dependent. Künsch (1989), *Annals
of Statistics* 17(3), gives the moving-block bootstrap for general stationary
observations: resample contiguous blocks, not individual time points. Use this *within* an
event if we compute time-series quantities; use the cluster bootstrap *across* events.
They compose — block within, cluster across.

### 2.5 The uncomfortable consequence
Morris, White & Crowther (2019), *Statistics in Medicine* 38(11):2074–2102, require a
Monte Carlo standard error on every performance measure, and require the repetition count
to be justified from a target MCSE. If MCSE is recomputed at the *event* level it will be
much larger than the per-scenario MCSE, and some headline separations in the
forecast-quality plane may collapse into noise. **This calculation should be run before
any result is presented, not after a reviewer asks.** A boundary in forecast-quality space
that is not distinguishable from noise at the event level is not a boundary.

**Requirements R2–R5.**

---

## 3. Equivalence / non-inferiority — the recipe, and why it matters for a tuned baseline

### 3.1 The failure mode this prevents
WG-C-006 exists to protect WG-C-002 from "you beat a strawman". But it creates a second,
subtler exposure. RQ1's *interesting* region is exactly where the forecast-aware policy
does **not** clearly beat the tuned trigger. If we describe that region as "no significant
difference", we have asserted the null — the single most common statistical
misinterpretation in the literature (Lakens 2017; Lakens, Scheel & Isager 2018). And
CURRENT_THESIS falsifier #3 ("tuned fixed buffers are within noise of any forecast-aware
policy") is a claim of *equivalence*, which cannot be established by failing to reject a
difference.

### 3.2 TOST
Lakens, Scheel & Isager (2018), *AMPPS* 1(2):259–269:
1. Specify a smallest effect size of interest (SESOI), giving bounds −Δ, +Δ, **before**
   analysis.
2. Test H0a: effect ≤ −Δ and H0b: effect ≥ +Δ, each one-sided at α.
3. Reject both ⇒ statistical equivalence. p_TOST = max(p_lower, p_upper).
4. The four outcomes are: significant & equivalent; significant & not equivalent;
   non-significant & equivalent; non-significant & not equivalent (**inconclusive**).

### 3.3 Our SESOI must be in decision units
Do not use a standardised SESOI (Cohen's d). Our estimands have physical units and
operational meaning. Suitable SESOIs:
- latest-safe-dispatch time: **Δ = the operational dispatch granularity** (e.g. 3 minutes,
  or whatever the KFS/fire-service dispatch cycle actually is);
- mission completion rate: **Δ = one mission in the scenario set**, or a stated fraction.

Justify the SESOI from operations, cite the justification, and report it next to every
equivalence statement so a reader may disagree with the bound without re-running the
study.

### 3.4 Power warning
Linde et al. (2020, *Psychological Methods*) report that TOST and HDI-ROPE discriminate
poorly at small n and favour a Bayes-factor interval-null approach (abstract only, E2).
With G < 10 events, TOST at the event level may be unable to reject non-equivalence for
any plausible Δ. **If so, the correct report is "inconclusive", and the correct
programmatic response is more events, not a smaller Δ.** Lauzon & Caffo (2009,
*The American Statistician*) give the multiplicity correction we need if we test
equivalence at many points of the forecast-quality grid (abstract only, E2).

### 3.5 Making the baseline genuinely strong
Dacrema, Cremonesi & Jannach (2019), RecSys '19, pp. 101–109, is the canonical
demonstration that weak or untuned baselines manufacture apparent progress in applied ML.
The defence is procedural, not rhetorical: **equal tuning budget, same scenario
distribution, published tuning grid, and a pre-registered tuning protocol** (Siepe et al.
2024). "We tuned it" is not evidence; a committed tuning grid is.

**Requirements R6–R9.**

---

## 4. Simulation validation frameworks

| Source | What it gives us |
|---|---|
| Sargent (2013), *J. Simulation* 7(1):12–24 | The three-part frame — conceptual model validation, computerised model verification, operational validity — plus the technique catalogue (face validity, extreme-condition tests, degenerate tests, sensitivity analysis, comparison to other models, historical/predictive validation). Validity is relative to a stated **intended purpose** and **domain of applicability**. |
| Oreskes, Shrader-Frechette & Belitz (1994), *Science* 263(5147):641–646 | Numerical models of open natural systems cannot be verified or validated in the strict sense; they can only be **confirmed** against data, and confirmation is not proof. |
| Axtell, Axelrod, Epstein & Cohen (1996), *CMOT* 1(2):123–141 | **Docking** / model alignment: the evidentiary standard when two models are supposed to represent the same system — run both, compare, report where they diverge. |
| Ronchi et al. (2023), *Natural Hazards* 117(2):1493–1519 | The domain instance: 24 verification tests for WUI fire evacuation models across eight components including **Trigger buffers**; and the community's own statement that validation data do not exist. |
| Morris, White & Crowther (2019) | ADEMP reporting structure + MCSE. |
| Siepe et al. (2024), *Psychological Methods*, DOI 10.1037/met0000695 | ADEMP-PreReg: a preregistration template for simulation studies. |
| Williams et al. (2024), *Methods Ecol. Evol.* 15(11):1926–1939 | Reporting items; found only 17% of surveyed articles reported Monte Carlo uncertainty and 32% released no code. |

**Calibration vs validation.** Keep these separate and say which is which. Tuning the fire
model's parameters so it reproduces an observed fire is **calibration**. Testing the
calibrated model against a *different* fire is **validation** (in Oreskes's stricter
sense, confirmation). A model calibrated and evaluated on the same event has been
calibrated, not validated — and in the OSSE setting this becomes the inverse crime (§5).

**Language discipline.** Ronchi et al. give the definitions: verification = "a correct
implementation of the developer's conceptual description"; validation = "the degree to
which a simulation is an accurate representation of the real world" (Introduction).
WildfireGuardian **verifies**. It does not validate. Every sentence in the paper, the
poster, and the spoken defence must obey this.

**Requirements R10–R13.**

---

## 5. Inverse crime and how our OSSE avoids it

### 5.1 The definition
Wirgin (2004), arXiv:math-ph/0401050 — **PREPRINT, never cite as a journal article**:

> "The inverse crime occurs when the same (or very nearly the same) theoretical
> ingredients are employed to synthesize as well as to invert data in an inverse problem."
> (Abstract)

The peer-reviewed treatment is Kaipio & Somersalo (2007), *J. Comput. Appl. Math.*
198(2):493–504, "Statistical inverse problems: Discretization, model reduction and inverse
crimes". **NEEDS_FULL_TEXT** — ScienceDirect returned 403 and the Semantic Scholar
abstract is publisher-elided; nothing is quoted from it here.

Henderson & Subbarao (2016), *J. Astronaut. Sci.* 64(4):399–413, is the empirical
demonstration: when the same model generates and inverts synthetic lightcurves, the
shape/size estimates are "significantly better", and the authors warn the results may be
"misleadingly optimistic" (Abstract).

### 5.2 Exactly where we commit it
WG-C-010's self-criticism already names it. Concretely, the crime occurs if:
- the truth fire is generated by spread model M with parameter set θ*, **and**
- the forecast consumed by the decision policy is produced by the same M with θ* plus
  zero-mean noise.

Adding noise does not fix it. Noise makes the forecast *less certain*; it does not make it
*wrong in the way a real model is wrong*. Real fire-model error is biased,
spatially correlated, and regime-dependent (it is worst exactly under the extreme wind and
slope conditions that matter for evacuation). Zero-mean isotropic perturbation of the
truth model is still an inverse crime, dressed.

### 5.3 The three-tier fix, in increasing strength

**Tier 1 — Different parameterisation (fraternal).** Same spread model family, materially
different configuration: different fuel model assignment, different rate-of-spread
sub-model, different resolution, different wind interpolation. This is the fraternal-twin
standard of Halliwell et al. (2014).

**Tier 2 — Different model (non-identical).** Truth from one spread model, forecast from a
structurally different one. This is what Yu et al. (2019) show is required to avoid biased
impact estimates.

**Tier 3 — Structured approximation error.** Characterise the discrepancy rather than
assume it: sample the truth model, compute the arrival-time discrepancy field of the
forecast model against it, and carry that discrepancy (with its bias and spatial
correlation) as an explicit error term. This is the Bayesian approximation-error idea
underlying Kaipio & Somersalo (2007) — **apply it, but do not quote that paper until the
full text is obtained.**

**Do not do Tier 0** (same model + white noise) and call it uncertainty.

### 5.4 And report the crime
Henderson & Subbarao's design is the right one for us: run the experiment **both ways** —
crime and non-crime — and report the gap. The size of the optimism is then measured rather
than asserted, and it becomes a result in its own right. This costs one extra experimental
arm and buys the strongest possible answer to attack #3.

**Requirements R14–R17.**

---

## 6. OSSE design requirements (fraternal vs identical twin)

### 6.1 The vocabulary — get it right in the spoken defence
Yu et al. (2019), Introduction, give the definitions:
- **Identical twin:** truth and forecast are "same model implementation but with perturbed
  initial, forcing or boundary conditions".
- **Fraternal twin:** "same model type ... but with sufficiently different configurations
  (e.g., different physical parameterizations and/or spatial resolution)".
- **Nonidentical twin:** "two different model types are used".

### 6.2 The result we need, and it is established
**Yes — "identical twin OSSE overestimates impact" is an established, citable result.**

Primary citable source:
> Yu, L., Fennel, K., Wang, B., Laurent, A., Thompson, K. R., & Shay, L. K. (2019).
> *Ocean Science* 15(6), 1801–1814. DOI: 10.5194/os-15-1801-2019.

They report the first direct side-by-side comparison in an ocean DA system. Quantitatively
(their §3.3 / Discussion, retrieved from the open-access full text):

| Metric | Identical twin | Nonidentical twin |
|---|---|---|
| Temperature MAD reduction | 45% | 29% |
| Velocity MAD reduction | 46% | 25% |
| Subsurface circulation (400 m) | ~67% | ~45% |

Direction: identical twins **overestimate** the value of the cheap/surface observations
and **underestimate** the value of the informative/profile observations. Abstract: "the
identical twin produces a biased skill assessment, overestimating the improvement from
assimilating sea surface height and sea surface temperature observations".

**Critically, they also show the obvious sanity check does not save you:** error growth
rates were comparable in both designs while the impact estimates were biased. A plausible
forecast-error growth curve is **not** evidence that the OSSE design is sound.

They attribute the prior atmospheric result to **Arnold & Dey (1986)** *BAMS*
67(6):687–695, **Atlas (1997)** *JMSJ* 75(1B):111–130, and **Hoffman & Atlas (2016)**
*BAMS* 97(9):1601–1616. All three are metadata-verified via Crossref but are
**NEEDS_FULL_TEXT** — AMS returned 403 and the NOAA PDF was unreadable. Cite Yu et al.
(2019) as the quantitative source; cite the atmospheric three only as "long recognised in
NWP (Arnold and Dey 1986; Atlas 1997; Hoffman and Atlas 2016)" until their texts are
obtained.

### 6.3 Design requirements from the OSSE literature
From Halliwell et al. (2014), *JTECH* 31(1):105–130 — an OSSE system needs:
1. a **nature run** stipulated as truth, whose climatology and variability are realistic;
2. a **forecast model** configured so that its errors against the NR "grow at the same
   rate as errors that develop between state-of-the-art ... models and the true"
   system (Abstract);
3. software to **simulate observations** from the NR with realistic errors;
4. **validation by OSE benchmarking**: run real observing-system experiments, then OSSEs
   identical except for synthetic observations, and require the impact pairs to match.
   The stated purpose is "to determine a priori that the OSSE system does not overestimate
   or underestimate observing system impacts" (Abstract).

From Privé et al. (2023), *Tellus A* 75(1):309–333: the characteristic OSSE pathology is
**insufficient model error** relative to the real world. Increasing model error moved their
FSOI observation impacts from ~60% to >70% of real-world values. Their conclusion is the
standard to adopt: "a range of fraternal twin OSSEs should give robust experimental
results, as long as the degree of twinning is well-understood." Impact *magnitudes* shift
with the degree of twinning; spatial *patterns* are more robust.

From Errico et al. (2013), *QJRMS* 139(674):1162–1178: validate the OSSE itself before
using it (NEEDS_FULL_TEXT).

### 6.4 The requirement we cannot meet, and what to do about it
Halliwell's acceptance test — OSE/OSSE agreement — **is unavailable to us.** There is no
real observing-system experiment for wildfire evacuation decision quality to benchmark
against. Therefore:

- We must **declare the OSSE uncalibrated**, and state that impact *magnitudes* are not
  real-world magnitudes. Following Privé et al. (2023), claim **orderings and patterns**,
  not magnitudes.
- Where any anchor is available — e.g. the forecast model's arrival-time error against a
  documented Korean fire — report it, as a partial and explicitly weak substitute.
- Report the **degree of twinning** as a measured quantity (e.g. distribution of
  arrival-time discrepancy between truth and forecast models), not as a design assertion.

This is not a weakness to be minimised. It is the honest statement of what a
non-benchmarkable OSSE can yield, and stating it first removes the attack.

### 6.5 WG-C-010: is the space occupied?
See §9.

**Requirements R18–R22.**

---

## 7. Calibration under shift

### 7.1 Score properly
Gneiting & Raftery (2007), *JASA* 102(477):359–378, is the reference for strictly proper
scoring rules and the calibration/sharpness decomposition. Probabilistic fire-arrival
forecasts must be scored with a strictly proper rule (CRPS for continuous arrival times,
Brier/log for binary arrival-before-deadline). A rule that a hedged forecast can game will
reward a policy that is not actually better.

### 7.2 In-distribution calibration does not transfer
Ovadia et al. (2019), arXiv:1906.02530 (presented at NeurIPS 2019 — **arXiv record
verified; the proceedings record was not verified, so treat the venue as
PREPRINT/conference**), show empirically that predictive uncertainty degrades under
dataset shift and that post-hoc recalibration fitted in-distribution does not survive the
shift. The practical consequence: calibrating the forecast model on the same scenario
distribution used for evaluation proves nothing about behaviour on a new fire.

### 7.3 Coverage guarantees under shift
Tibshirani, Barber, Candès & Ramdas (2019), arXiv:1904.06019 (NeurIPS 2019; same venue
caveat), give **weighted conformal prediction**: exchangeability-based coverage is void
under covariate shift, but coverage is restored by weighting with the covariate-shift
likelihood ratio, which must be known or estimable. If WildfireGuardian claims
distribution-free coverage for fire-arrival intervals or for trigger boundaries on a
shifted scenario set, it must use the weighted form and must state where the likelihood
ratio comes from. Barber, Candès, Ramdas & Tibshirani (2023), *Annals of Statistics*
51(2), DOI 10.1214/23-aos2276, extends this beyond exchangeability (metadata verified via
Crossref; not read).

### 7.4 What calibration evidence is required when forecast model ≠ truth model
This is the specific question the mission poses, and the answer follows from §6 and §7:

1. **Reliability diagram + proper score, computed at the event level**, for the forecast
   model's predictions against the truth run — reported separately for each fire event,
   not pooled. Pooling across events hides event-specific miscalibration behind the
   average and is a form of pseudoreplication applied to calibration.
2. **Held-out-event calibration.** Fit/tune any recalibration on events E1..E_{k−1};
   report calibration on event E_k. Anything else is in-distribution calibration, which
   Ovadia et al. show does not transfer.
3. **Calibration under the shift that matters.** Report calibration stratified by the
   regime that drives decisions — high wind, steep slope, short lead time — not only on
   average. Average calibration with tail miscalibration is precisely the failure that
   kills people and the failure a judge will ask about.
4. **Sharpness alongside calibration** (Gneiting & Raftery): a forecast that always
   predicts the climatological arrival distribution is perfectly calibrated and
   decision-useless. Report both, or report a proper score that combines them.
5. **The degree-of-twinning statistic** from §6.4, so the reader knows how different the
   two models actually are.

**Requirements R23–R26.**

---

## 7A. Decision-focused evaluation (bearing on WG-C-014)

Elmachtoub & Grigas (2022), *Management Science* 68(1):9–26, establish in general that
prediction error and decision regret are different objectives, and give the SPO loss.
Mandi et al. (2024), *JAIR* 80:1623–1701, survey the field: decision-focused learning is a
named, mature area. **WG-C-014 must therefore be phrased as a wildfire-specific
instantiation, not as a new observation** — the general fact that accuracy metrics and
decision metrics diverge is owned.

Within wildfire specifically, Xu, Dai, Chang, Wang & Dong (2026), arXiv:2605.18911
(**PREPRINT**), report "selection regret": choosing a model head by a ranking metric
(PR-AUC) rather than a decision metric (F1) costs measurable decision performance on
wildfire occupancy and spread tasks. This is a classification-metric result, not an
evacuation-deadline result, so it does not occupy WG-C-014 — but it narrows it. WG-C-014's
survivable form is specifically: *spatial fire-prediction accuracy (IoU) is not
monotonically related to **evacuation decision** quality (dispatch feasibility)*. Filed as
threat_level LOW against WG-C-014.

---

## 8. Checklist — what WildfireGuardian must do to be methodologically defensible

Each item is concrete, testable, and cites its source. Items marked **[BLOCKING]** should
be satisfied before any result is presented externally.

### Unit of analysis and inference

**R1. [BLOCKING]** Declare the **fire event** as the experimental unit in the methods
section, using the biological/experimental/observational unit taxonomy.
*Hurlbert (1984), Ecol. Monogr. 54(2):187–211; Lazic et al. (2018), PLOS Biol. 16(4):e2005282.*

**R2. [BLOCKING]** Report the number of **events (G)** next to every p-value, confidence
interval and headline number — not only the number of scenarios.
*Cameron & Miller (2015), J. Hum. Resour. 50(2):317–372.*

**R3. [BLOCKING]** Use the **wild cluster bootstrap-t with the null imposed**, clustering
on event, instead of asymptotic cluster-robust standard errors.
*Cameron, Gelbach & Miller (2008), REStat 90(3):414–427.*

**R4.** If G < ~11, use Webb's 6-point weights and state the granularity of the attainable
p-values. *Webb (2014), Can. J. Econ. — abstract only; obtain before implementing.*

**R5.** For time-indexed quantities within an event, resample contiguous **blocks**, not
individual time points. *Künsch (1989), Ann. Statist. 17(3), DOI 10.1214/aos/1176347265.*

### Comparator and equivalence

**R6. [BLOCKING]** Pre-register the baseline **tuning protocol and grid** (search space,
budget, scenario distribution) before running the comparison; give the forecast-aware
policy and the tuned trigger equal tuning budget on the same distribution.
*Dacrema, Cremonesi & Jannach (2019), RecSys '19, 101–109; Siepe et al. (2024), Psychol. Methods, DOI 10.1037/met0000695.*

**R7. [BLOCKING]** Pre-specify a **SESOI in decision units** (minutes of dispatch margin;
missions completed), justified operationally, not a standardised effect size.
*Lakens, Scheel & Isager (2018), AMPPS 1(2):259–269.*

**R8. [BLOCKING]** Wherever the forecast-aware policy does not beat the tuned baseline,
run **TOST at the event level** and report exactly one of: equivalent / not equivalent /
**inconclusive**. The phrase "no significant difference" is banned from the program.
*Lakens (2017), SPPS 8(4):355–362; Lakens, Scheel & Isager (2018).*

**R9.** Correct for multiplicity when testing equivalence at many grid points of the
forecast-quality plane. *Lauzon & Caffo (2009), Am. Stat. — abstract only; obtain.*

### Simulation study conduct

**R10. [BLOCKING]** Report the experiment as **ADEMP** (Aims, Data-generating mechanism,
Estimands, Methods, Performance measures).
*Morris, White & Crowther (2019), Stat. Med. 38(11):2074–2102.*

**R11. [BLOCKING]** Attach a **Monte Carlo standard error to every headline number**,
computed **at the event level**, and justify the scenario count from a target MCSE rather
than from compute budget. *Morris et al. (2019); Williams et al. (2024), Methods Ecol. Evol. 15(11):1926–1939.*

**R12.** Preregister the full simulation design (generator, grid, performance measures) and
timestamp it. *Siepe et al. (2024).*

**R13. [BLOCKING]** Use the words correctly, everywhere: we **verify**, we do not
**validate**; models of open systems are **confirmed**, not validated.
*Ronchi et al. (2023), Nat. Hazards 117(2):1493–1519 (Introduction); Oreskes, Shrader-Frechette & Belitz (1994), Science 263(5147):641–646.*

**R13b.** Run the applicable tests from the published WUI evacuation **verification
protocol** (Wildfire spread, Movement, Flow constraints, Trigger buffers) and report
pass/fail; define and publish a new component test for the inbound/dispatch-deadline leg,
which no existing test covers. *Ronchi et al. (2023).*

**R13c.** State the model's **intended purpose and domain of applicability**, and name the
validation techniques used beyond face validity (extreme-condition, degenerate,
sensitivity, model-to-model comparison). *Sargent (2013), J. Simul. 7(1):12–24.*

### OSSE design (WG-C-010)

**R14. [BLOCKING]** Never generate the truth fire and the forecast fire from the same model
with the same configuration plus zero-mean noise. That is the inverse crime.
*Wirgin (2004), arXiv:math-ph/0401050 (PREPRINT); Kaipio & Somersalo (2007), J. Comput. Appl. Math. 198(2):493–504 (NEEDS_FULL_TEXT).*

**R15. [BLOCKING]** Use at minimum a **fraternal-twin** configuration (materially different
parameterisation/resolution/sub-models); prefer a **nonidentical twin** (structurally
different spread model). *Halliwell et al. (2014), JTECH 31(1):105–130; Yu et al. (2019), Ocean Sci. 15(6):1801–1814.*

**R16.** Give the injected forecast error the **structure** of real model error — biased,
spatially correlated, regime-dependent — derived by sampling the truth–forecast
discrepancy, not white noise. *Kaipio & Somersalo (2007) (approximation-error approach; NEEDS_FULL_TEXT).*

**R17.** Run the experiment **both ways** (identical-twin and non-identical) and report the
gap, so the optimism is measured rather than asserted.
*Henderson & Subbarao (2016), J. Astronaut. Sci. 64(4):399–413.*

**R18. [BLOCKING]** Do not cite forecast-error growth rate as evidence the OSSE is sound —
Yu et al. show that check passes while impacts are still biased. *Yu et al. (2019).*

**R19. [BLOCKING]** Declare the OSSE **uncalibrated** (no OSE benchmark exists for wildfire
evacuation decisions) and claim **orderings and patterns, not magnitudes**.
*Halliwell et al. (2014) for the missing acceptance test; Privé et al. (2023), Tellus A 75(1):309–333 for pattern-vs-magnitude robustness.*

**R20.** Report the **degree of twinning** as a measured statistic (distribution of
arrival-time discrepancy between truth and forecast models). *Privé et al. (2023): results are robust "as long as the degree of twinning is well-understood".*

**R21.** Simulate observations with realistic error characteristics, not white noise.
*Halliwell et al. (2014); Hoffman & Atlas (2016), BAMS 97(9):1601–1616 (NEEDS_FULL_TEXT).*

**R22.** State as a limitation that OSSE conclusions inherit the deficiencies of the
underlying fire and decision models. *Zeng et al. (2020), BAMS 101(8):E1427–E1438, recommendation 3.*

### Calibration and forecast quality

**R23. [BLOCKING]** Score probabilistic forecasts with a **strictly proper** rule (CRPS,
Brier, log) and report calibration **and** sharpness. *Gneiting & Raftery (2007), JASA 102(477):359–378.*

**R24. [BLOCKING]** Report reliability **per event** and on a **held-out event**, never
pooled-and-in-distribution. *Ovadia et al. (2019), arXiv:1906.02530 (PREPRINT/NeurIPS).*

**R25.** Report calibration **stratified by decision-relevant regime** (high wind, steep
slope, short lead time), not only on average. *Ovadia et al. (2019).*

**R26.** If distribution-free coverage is claimed under a shifted scenario set, use
**weighted conformal prediction** with a stated likelihood ratio.
*Tibshirani, Barber, Candès & Ramdas (2019), arXiv:1904.06019 (PREPRINT/NeurIPS); Barber et al. (2023), Ann. Statist. 51(2), DOI 10.1214/23-aos2276.*

### Decision-focused reporting

**R27.** Report **decision regret** as the primary metric and prediction error as a
secondary diagnostic. *Elmachtoub & Grigas (2022), Manage. Sci. 68(1):9–26.*

**R28.** Position WG-C-014 as a wildfire-specific instantiation of a known
prediction-metric/decision-metric divergence, and narrow it to *evacuation-decision*
quality. *Mandi et al. (2024), JAIR 80:1623–1701; Xu et al. (2026), arXiv:2605.18911 (PREPRINT).*

---

## 9. Adversarial finding on WG-C-010

**Question asked:** has anyone already published an OSSE for wildfire **decision**
evaluation (not just fire-model evaluation)?

**Answer, with the protocol caveat:** not found in this sweep. Per NOVELTY_STANDARD §3.2
and §5, that yields **UNKNOWN**, not support, and this sweep does not meet the
`SUPPORTED_CANDIDATE` bar (no non-English pass; preprint coverage was arXiv-only;
Consensus quota exhausted mid-sweep).

What was found:

1. **Wildfire OSSEs exist, but at the fire-model / data-assimilation level.** Synthetic
   "true" fire states generated by a propagation solver and then re-estimated by a
   DA scheme are standard practice in the wildfire data-assimilation literature (Rochoux
   and colleagues; FIREFLY; FARSITE-EnKF; assimilation of fire perimeters). These were
   identified by WebSearch at abstract/summary level and are **Category 1/8 territory, not
   recorded here**. The evaluated quantity in all of them is *fire state accuracy*, not
   decision quality. Several of them explicitly commit or acknowledge the identical-twin
   structure ("synthetic observations are generated using the fire propagation solver").
2. **Decision/societal-impact OSSEs are an acknowledged open item, not an accomplished
   one.** Zeng et al. (2020), a NOAA Science Advisory Board–derived BAMS review, lists
   "extension of OSSEs to societal impacts" among five forward recommendations. As of
   2020 the authoritative US OSSE community treated this as work to be done.
3. **No wildfire evacuation-decision OSSE surfaced** under queries combining OSSE / nature
   run / synthetic truth with evacuation, trigger buffers, protective action, or dispatch.

**Recommended status for WG-C-010: UNKNOWN**, with the following strategic note. The
defensible claim is **not** "first OSSE for wildfire decisions" (that is search-failure
novelty, forbidden by NOVELTY_STANDARD §3.2, and a conjunction besides). The defensible
claim is the narrower, citable one:

> "We instantiate, for wildfire evacuation decisions, the extension of OSSE methodology to
> societal/decision impacts recommended by Zeng et al. (2020), and we adopt the
> non-identical-twin design that Yu et al. (2019) show is required for unbiased impact
> assessment."

That sentence is verifiable, cites its own authority, and cannot be killed by a reviewer
producing one wildfire-DA OSSE paper.

**Residual risk.** The searchable surface is narrow: hydrology, air quality
(OSSEs for air quality exist — ScienceDirect S1352231015301059, not retrieved), and
public-health decision modelling may contain decision-level OSSEs under other names
("value-of-information simulation", "synthetic-truth decision experiment", "perfect-model
experiment"). Those wording variants have **not** been exhausted.

---

## 10. Open questions and items needing full text

| Item | Why it matters | Status |
|---|---|---|
| Kaipio & Somersalo (2007), JCAM 198(2):493–504 | The peer-reviewed inverse-crime citation and the approximation-error method we intend to use | **NEEDS_FULL_TEXT** — ScienceDirect 403, S2 abstract elided |
| Hoffman & Atlas (2016), BAMS 97(9) | OSSE design requirements; cited by Yu et al. for twin bias | **NEEDS_FULL_TEXT** — AMS 403, NOAA PDF unreadable |
| Arnold & Dey (1986), BAMS 67(6); Atlas (1997), JMSJ 75(1B) | The original atmospheric identical-twin-bias statements | **NEEDS_FULL_TEXT** — currently cited secondhand via Yu et al. (2019) |
| Errico et al. (2013), QJRMS 139(674) | OSSE self-validation protocol | **NEEDS_FULL_TEXT** |
| Privé (2021), BAMS 102(1):E80–E83 | Published Comment on Zeng et al. (2020) — may qualify the recommendation we lean on | **NEEDS_FULL_TEXT** |
| Linde et al. (2020), Psychological Methods | May require Bayes-factor equivalence rather than TOST at our G | Abstract only (E2) |
| Webb (2014), Can. J. Econ.; MacKinnon & Webb (2018), Econom. J. | Bootstrap weights for very small G — likely required | Abstract only (E2) |
| Sargent (2013) full text | Technique list must be checked before enumeration | Abstract-level (E2) |
| Morris et al. (2019) MCSE equations | Must be checked before typesetting | Abstract-level (E2) |
| Ovadia et al. (2019); Tibshirani et al. (2019) | NeurIPS proceedings records not verified; currently PREPRINT | Venue **UNVERIFIED** |
| Decision-level OSSEs under other names | The residual WG-C-010 risk | Not searched |
| Non-English (Korean, Japanese, French) methodology literature | Required for any SUPPORTED_CANDIDATE upgrade | Not searched |

---

## 11. Repository bookkeeping note

AGENTS.md §5 requires that adding a paper also updates `bibliography/literature.csv`,
`bibliography/doi_registry.csv`, `bibliography/wildfireguardian.bib`,
`novelty/NOVELTY_MATRIX.md`, `novelty/NOVELTY_THREATS.md`, `docs/CLAIM_REGISTRY.md` and
`docs/SEARCH_PROTOCOL.md`. This agent was scoped to four paths only (this review, notes,
metadata, and its search log) and **did not** make those updates. The 32 metadata files in
`literature/metadata/` for Category 10 are therefore not yet reflected in the bibliography
or novelty files. `docs/SEARCH_PROTOCOL.md` and `novelty/NOVELTY_THREATS.md` did not exist
at the time of this sweep. **Flagged for Agent D / the repository owner.**
