# choi2026ridgeline

## Citation
Choi, J. H.; Chae, HeeMun (2026). "Wildfire Perimeters Align with Topographic Ridge Lines:
A Null Model Benchmark for Fire-Spread Modelling in 118 Korean Wildfires (2018–2025)."
*Fire* 9(6): 247. DOI 10.3390/fire9060247. Gold OA (CC-BY).

## Publication status
**PEER_REVIEWED.** Language: English. Evidence level **E2** — OpenAlex-deposited abstract
read; full text not retrieved (MDPI blocks WebFetch with HTTP 403).

## Problem
Is there a systematic, testable geometric signature of Korean wildfire spread that a
fire-spread model ought to reproduce — and against what null is "reproduce" judged?

## Method
118 final fire perimeters in the Republic of Korea, 2018–2025. Burn masks and perimeters
from pre-/post-fire Sentinel-2 imagery plus official fire metadata. Ridge network derived
from a 30 m DEM. Two metrics — **proximity** to ridge lines and **alignment** with them —
each evaluated against a **null model** (randomised placement), reported as enrichment
ratios. A valley-inclusive comparator is used as a control.

## Data
Sentinel-2 imagery; 30 m DEM; official Korean fire metadata (KFS).

## Outputs
Most fires are both ridge-proximal and ridge-aligned. Mean enrichment ≈ **2.3** for the
combined proximity+alignment metric versus ≈ **1.5** for proximity alone, with a stronger
directional signal than the valley-inclusive comparator.

## Key equations
Enrichment ratio of observed metric against a null distribution (exact form NEEDS_FULL_TEXT).

## Assumptions
Final perimeters carry the directional signal of the spread process; a 30 m DEM resolves the
ridge network adequately for Korean terrain; the randomisation null is the right baseline.

## Validation
Observational, 118 real events — this is the benchmark, not a model being validated.

## Limitations
Final perimeters only, so no time information: the paper says nothing about *when* the fire
reached anywhere. No fire-spread model is actually scored against the benchmark here.

## WildfireGuardian overlap
None on the decision side. Substantial on the **evidence** side: this is a published,
Korea-specific, quantified terrain–spread relationship.

## WildfireGuardian difference
Geometry of where fires went, not timing of when residents must leave.

## Novelty threat
**LOW for WG-C-007; relevant to WG-C-014.** Its real value is the opposite of a threat: it
is the most usable published basis for a NOVELTY_STANDARD **§4(a)/(b)** argument. If a
spread model imported from US/Mediterranean settings fails to reproduce the ridge-alignment
enrichment on Korean terrain, that is a *documented* failure of a published method on Korean
data — §4(b) — rather than an assertion that "Korean terrain is different." It also feeds
WG-C-014: ridge alignment is a spatial-accuracy property that may be uncorrelated with
arrival-time accuracy, which is what an evacuation deadline actually depends on.

## Quotes / page references
> "mean enrichment 2.3 for combined metrics versus 1.5 for proximity alone" (abstract, as
> deposited).
Page references unavailable — abstract only.

## Follow-up papers
- Full text (needed: the null-model construction and whether any spread model was scored).
- `park2025drivers` (wind/conifer drivers over 905 Korean fires) as a complementary
  Korean-condition evidence source.
