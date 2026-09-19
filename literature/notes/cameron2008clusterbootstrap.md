# cameron2008clusterbootstrap

## Citation
Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-Based Improvements for
Inference with Clustered Errors. *Review of Economics and Statistics*, 90(3), 414–427.
DOI: 10.1162/rest.90.3.414

## Publication status
Published, peer-reviewed. Metadata verified via Crossref API (DOI lookup). Earlier
versions exist as NBER technical working paper 344 (DOI 10.3386/t0344) and SSRN 956890 —
**cite the REStat version.**

## Problem
Cluster-robust standard errors assume the number of clusters G is large. With few clusters
(roughly 5–30), asymptotic cluster-robust t-tests over-reject: nominal 5% tests can reject
at 10% or more.

## Method
Cluster bootstrap-t (percentile-t) procedures that provide asymptotic refinement, in
particular the **wild cluster bootstrap**: impose the null, resample cluster-level
residual sign flips (Rademacher weights), recompute the t-statistic, and compare the
observed statistic to the bootstrap distribution rather than to a t or normal reference.

## Data
Monte Carlo experiments, plus the Bertrand–Duflo–Mullainathan (2004) placebo-law design.

## Outputs
Rejection rates of ~10% using standard cluster-robust methods are brought back to the
nominal 5% by the bootstrap-t procedures.

## Key equations
Wild cluster bootstrap DGP: y*_g = X_g β̃ + û_g · v_g, with β̃ the null-restricted
estimate, û_g the cluster-g residual vector, and v_g ∈ {−1, +1} drawn once **per cluster**
(Rademacher). The whole cluster's residual vector is multiplied by the same v_g — this is
what preserves within-cluster dependence. **Verify the exact form against the paper's
Section 3 before implementing.**

## Assumptions
Errors independent *across* clusters, arbitrarily dependent *within* cluster. Cluster
sizes not wildly unequal (relaxed by later work).

## Validation
Monte Carlo size studies; empirical replication.

## Limitations
- Fails when the number of *treated* clusters is very small (MacKinnon & Webb 2018,
  *Econometrics Journal*; abstract only, E2, not recorded).
- Rademacher weights give a discrete, non-point-identified p-value below ~11 clusters
  (Webb 2014, *Canadian Journal of Economics*; abstract only, E2). Webb's 6-point weights
  are the standard remedy.

## WildfireGuardian overlap
Our clusters are fire events. We will plausibly have far fewer than 30 of them —
realistically a handful of Korean fire events plus synthetic variants. That places us
squarely in the regime where this paper says the default method fails.

## WildfireGuardian difference
**Requirement imposed on us:**
1. Cluster at the fire-event level (Cameron & Miller 2015 for the choice rule).
2. Use the **wild cluster bootstrap-t with the null imposed**, not asymptotic
   cluster-robust standard errors.
3. With fewer than ~11 events, switch to Webb's 6-point weight distribution and say so;
   with very few events, report the bootstrap p-value's granularity honestly (e.g. "the
   smallest attainable p-value with G = 6 events is 1/32").
4. Report G next to every inferential statement. If G is small enough that no test can
   reject, say that — it is a real finding about the evidence base, not a failure to be
   hidden behind per-scenario n.

## Novelty threat
BACKGROUND.

## Quotes / page references
- "Standard asymptotic tests can over-reject ... with few (five to thirty) clusters"
  (Abstract).
- "Rejection rates of 10% using standard methods can be reduced to the nominal size of 5%
  using our methods" (Abstract).

## Follow-up papers
- Cameron & Miller (2015), *Journal of Human Resources* 50(2):317–372 — recorded.
- MacKinnon & Webb (2018), *Econometrics Journal* — few treated clusters. Abstract only.
- Webb (2014), *Canadian Journal of Economics* — 6-point weights. Abstract only. **Follow
  up: likely required for our G.**
- Roodman, MacKinnon, Nielsen & Webb (2019), *The Stata Journal* — `boottest`
  implementation. Abstract only.
- Künsch (1989), *Annals of Statistics* — block bootstrap for serial dependence within an
  event. Recorded.
