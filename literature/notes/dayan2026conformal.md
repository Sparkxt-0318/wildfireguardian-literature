# dayan2026conformal

## Citation
Dayan, B. (2026). *Conformal Risk Control for Safety-Critical Wildfire Evacuation Mapping: A Comparative Study of Tabular, Spatial, and Graph-Based Models.* arXiv:2603.22331 (submitted 20 March 2026).

## Publication status
**PREPRINT** (arXiv), single author. No DOI. Abstract/summary read; full text not retrieved (**E2**).
Single-author preprints warrant extra caution, but under NOVELTY_STANDARD §3.3 venue prestige is irrelevant to
whether a claim is occupied.

## Problem
Wildfire spread models are scored by accuracy metrics that carry no guarantee about the thing that matters — not
missing fire that will reach people. Can a distribution-free guarantee be imposed instead?

## Method
Conformal risk control (CRC) applied to wildfire spread prediction, giving finite-sample guarantees on the false
negative rate (FNR ≤ 0.05). A shift-aware three-way CRC framework assigns **SAFE / MONITOR / EVACUATE** zones for
operational triage. Three model classes compared.

## Data
Wildfire spread dataset (source not confirmed from the abstract — NEEDS_FULL_TEXT).

## Outputs
- Models: LightGBM AUROC 0.854; Tiny U-Net AUROC 0.969; hybrid ResGNN-UNet AUROC 0.964.
- **Standard thresholds captured only 7-72% of actual fire spread across models.**
- With CRC, both spatial models achieved ~95% fire coverage while flagging only ~15% of total pixels, reported as
  4.2x more efficient than LightGBM.

## Key equations
Conformal risk control calibration; not retrieved.

## Assumptions
- Exchangeability (or the shift-aware relaxation the author claims) between calibration and deployment fires.
- That a three-way zoning is the operationally relevant decision.

## Validation
Held-out evaluation; not an operational trial.

## Limitations
Zones are spatial triage categories, not timed actions. Nothing about when to act, how long evacuation takes, or
who cannot self-evacuate.

## WildfireGuardian overlap
Two claims are touched:
- **WG-C-014.** This is the closest published work to "spatial accuracy is not decision quality". The finding that
  a model with AUROC 0.969 still captured as little as 7% of actual spread at standard thresholds is a concrete
  demonstration that a headline accuracy metric and operational adequacy come apart.
- **WG-C-004.** It produces decision-relevant zones from probabilistic spread predictions across several models.

## WildfireGuardian difference
Dayan repairs the *threshold*: given a prediction, choose a cut that guarantees coverage. WildfireGuardian's
question is different and, if anything, harder — whether improving a spatial accuracy metric improves decision
quality at all, i.e. whether the relationship is even monotone. Dayan does not test monotonicity; he sidesteps
accuracy metrics by imposing a risk constraint. Also: his decision subject is a zone, ours is a dispatch time.

## Novelty threat
**HIGH for WG-C-014**, but **not fatal**. It shows accuracy ≠ adequacy; it does not show that accuracy and
decision quality are non-monotonically related, which is the specific WG-C-014 sentence. WG-C-014 should be
narrowed to the non-monotonicity claim and this paper cited as the nearest neighbour. **MODERATE for WG-C-004**
(kalogeropoulos2026ensemble is the fatal one there).

## Quotes / page references
Abstract: delivers "finite-sample guarantees on false negative rate (FNR <= 0.05)".
Abstract: "shift-aware three-way CRC framework that assigns SAFE/MONITOR/EVACUATE zones for operational triage".

## Follow-up papers
- kalogeropoulos2026ensemble (already filed).
- bennett2026wise, elmfire2025validation (the accuracy numbers the CRC framing is reacting to).
