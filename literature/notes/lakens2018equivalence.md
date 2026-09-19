# lakens2018equivalence

## Citation
Lakens, D., Scheel, A. M., & Isager, P. M. (2018). Equivalence Testing for Psychological
Research: A Tutorial. *Advances in Methods and Practices in Psychological Science*, 1(2),
259–269. DOI: 10.1177/2515245918770963

## Publication status
Published, peer-reviewed. Metadata verified via Crossref API. Abstract retrieved via
Consensus. Companion primer: Lakens (2017), *SPPS* 8(4):355–362,
DOI 10.1177/1948550617697177 — also recorded.

## Problem
Researchers routinely report a non-significant difference as if it established the absence
of an effect. Null-hypothesis significance testing cannot support that conclusion; a
non-significant result is equally consistent with "no meaningful difference" and "an
underpowered test".

## Method
Two one-sided tests (TOST). Specify a smallest effect size of interest (SESOI), giving
lower and upper equivalence bounds −Δ and +Δ. Test H0a: effect ≤ −Δ and H0b: effect ≥ +Δ,
each at α. Reject both ⇒ conclude statistical equivalence at α. The p-value of the
equivalence test is the maximum of the two one-sided p-values.

## Data
Worked examples from psychological research; no new data.

## Outputs
- The TOST decision procedure and its power analysis.
- A taxonomy of ways to justify a SESOI (smallest effect of practical interest,
  benchmarks, resource-constrained minimum detectable effect).
- The four-way outcome table: significant & equivalent, significant & not equivalent,
  non-significant & equivalent, non-significant & not equivalent (= inconclusive).

## Key equations
TOST with unequal variances (Welch form), per the tutorial:
  t_lower = (M1 − M2 − (−Δ)) / SE ,  t_upper = (M1 − M2 − Δ) / SE
  p_TOST = max(p_lower, p_upper); reject non-equivalence if p_TOST < α.
(Structure reproduced from the standard TOST definition; verify against the paper's
Equations before typesetting them in our manuscript.)

## Assumptions
A SESOI specified **before** seeing the data; the usual parametric assumptions of the
underlying t-test (or a robust/bootstrap analogue).

## Validation
Not applicable (methodological tutorial).

## Limitations
- TOST has limited discriminating power at small n. Linde et al. (2020, *Psychological
  Methods*) report that TOST and HDI-ROPE generally need large samples for equivalence
  margins around 0.2–0.3 and favour a Bayes factor interval-null approach — **abstract
  only (E2), not recorded as metadata.** With few fire events this limitation bites us
  directly.
- Choosing the SESOI is a substantive, contestable judgement, not a statistical one.

## WildfireGuardian overlap
WG-C-006 asserts that our tuned trigger/buffer comparator is genuinely strong. WG-C-002's
interesting region is precisely where forecast-aware action does *not* clearly beat it. If
we write "the tuned baseline and the forecast-aware policy did not differ significantly",
we have made exactly the error this tutorial exists to stop.

## WildfireGuardian difference
**Requirement imposed on us:**
1. Pre-register a SESOI in *decision units*, not standardised units — e.g. "a difference
   of less than 3 minutes in latest-safe-dispatch time is not decision-relevant". A
   Cohen's-d SESOI is not defensible here because the quantity has physical units and an
   operational threshold.
2. In every region of forecast-quality space where the forecast-aware policy does not win,
   run TOST at the event level and report one of: **equivalent**, **not equivalent**, or
   **inconclusive**. Never "no significant difference".
3. Report the equivalence bound next to every such statement so a reader can disagree with
   our SESOI without re-running the study.

## Novelty threat
BACKGROUND. It is a methodological requirement, not a prior-art threat. Note that
satisfying it is *not* a novelty claim either (NOVELTY_STANDARD §2: N3-weak) — WG-C-006's
function is defensive.

## Quotes / page references
- "Psychologists must be able to test both for the presence of an effect and for the
  absence of an effect" (Abstract).
- "researchers can use the two one-sided tests (TOST) procedure to test for equivalence
  and reject the presence of a smallest effect size of interest" (Abstract).

## Follow-up papers
- Lakens (2017), *SPPS* 8(4):355–362 — recorded.
- Linde, Tendeiro, Selker, Wagenmakers & van Ravenzwaaij (2020), *Psychological Methods* —
  TOST vs HDI-ROPE vs Bayes factor. Abstract only; **follow up, may change our test
  choice given small event counts.**
- Lauzon & Caffo (2009), *The American Statistician* — multiplicity control for TOST;
  relevant because we will test equivalence at many points of the forecast-quality grid.
  Abstract only.
