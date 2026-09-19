# kaipio2007inversecrime

## Citation
Kaipio, J., & Somersalo, E. (2007). Statistical inverse problems: Discretization, model
reduction and inverse crimes. *Journal of Computational and Applied Mathematics*, 198(2),
493–504. DOI: 10.1016/j.cam.2005.09.027

## Publication status
Published, peer-reviewed. Bronze OA. Metadata verified via Crossref and Semantic Scholar
Graph API. **NEEDS_FULL_TEXT** — the abstract is elided by the publisher in the Semantic
Scholar record and ScienceDirect returned HTTP 403; the substantive claims below are drawn
from the title, the companion monograph, and Wirgin (2004), not from this paper's text.

## Problem
When synthetic measurement data are generated with the same discretisation/forward model
that is then used in the inversion, the inverse solution is unrealistically good. The
paper addresses discretisation, model reduction, and the resulting "inverse crimes".

## Method
Statistical (Bayesian) treatment of inverse problems in which the discrepancy between an
accurate forward model and the reduced model actually used is represented as an explicit
*approximation error* random variable with its own statistics, rather than being neglected.

## Data
UNVERIFIED (full text not retrieved).

## Outputs
UNVERIFIED (full text not retrieved). The reusable idea is the Bayesian
approximation-error approach.

## Key equations
UNVERIFIED — do not cite an equation from this paper until the full text is obtained.
Conceptually: y = A_accurate(x) + e  is replaced by  y = A_reduced(x) + [A_accurate(x) −
A_reduced(x)] + e, with the bracketed term modelled rather than dropped.

## Assumptions
That the approximation error can be characterised (e.g. by sampling the accurate model).

## Validation
UNVERIFIED.

## Limitations
- Full text not retrieved; treat as evidence level E2/NEEDS_FULL_TEXT.
- Developed for continuum inverse problems (EIT, tomography); the mapping to a fire-spread
  forward model is ours to justify.

## WildfireGuardian overlap
WG-C-010's OSSE is structurally an inverse problem: a fire-spread model generates the
synthetic "truth", and a (possibly identical) fire-spread model is used to produce the
forecast on which the decision is based. That is the inverse crime.

## WildfireGuardian difference
**Requirement imposed on us:** do not merely *differ* the forecast model from the truth
model — characterise the difference. Sample the truth model, compute the arrival-time
discrepancy distribution, and carry that discrepancy as an explicit error term in the
forecast used by the decision policy. A forecast that is the truth model plus white noise
is still an inverse crime with noise added; the required error must have the *structure*
of real model error (biased, spatially correlated, regime-dependent).

## Novelty threat
BACKGROUND.

## Quotes / page references
None. No verbatim text was retrieved. Do not attribute a quotation to this paper.

## Follow-up papers
- Wirgin (2004), arXiv math-ph/0401050 — definition, PREPRINT. Recorded.
- Henderson & Subbarao (2016), *J. Astronaut. Sci.* 64(4):399–413 — empirical
  demonstration. Recorded.
- Kaipio & Somersalo (2005), *Statistical and Computational Inverse Problems*, Springer,
  DOI 10.1007/b138659 — monograph; verified in Crossref but not read. Not recorded.
