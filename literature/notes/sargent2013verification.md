# sargent2013verification

## Citation
Sargent, R. G. (2013). Verification and validation of simulation models. *Journal of
Simulation*, 7(1), 12–24. DOI: 10.1057/jos.2012.20

## Publication status
Published, peer-reviewed journal article. Metadata verified via Crossref API (DOI
lookup). **Important for citation hygiene:** Sargent published near-identical tutorials in
the Winter Simulation Conference proceedings for many years (1994 DOI
10.1109/WSC.1994.717077; 2005 DOI 10.1109/WSC.2005.1574246; 2007 DOI
10.1109/WSC.2007.4419595; 2008 DOI 10.1109/WSC.2008.4736065; 2011 DOI
10.1109/WSC.2011.6147750 — all verified in Crossref). Conference ≠ journal. Cite the
*Journal of Simulation* version and do not silently substitute a WSC year.

## Problem
How to establish that a simulation model is a sufficiently accurate representation of the
system it is meant to represent, for the model's intended purpose.

## Method
A framework distinguishing the real system, the conceptual model, and the computerised
model, with three corresponding activities:
- **conceptual model validation** — are the theories and assumptions right for the
  intended purpose;
- **computerised model verification** — was the conceptual model implemented correctly;
- **operational validity** — does the model's output behaviour have sufficient accuracy.

Plus a catalogue of validation techniques (face validity/expert review, comparison to
other models, degenerate tests, extreme-condition tests, sensitivity analysis, historical
data validation, predictive validation, Turing tests) and the paradigm of
accreditation/documentation.

## Data
None; methodological tutorial.

## Outputs
The V&V taxonomy and technique catalogue; the principle that validity is relative to the
model's **intended purpose** and to a specified **domain of applicability**.

## Key equations
None (the paper does discuss statistical procedures for comparing model and system output,
but no equation is recorded here — full text not retrieved).

## Assumptions
That a stated intended purpose exists against which adequacy can be judged.

## Limitations
- Full text not retrieved (evidence level E2); the technique list above is standard across
  all versions of this tutorial but should be checked against the journal text before
  being enumerated in our manuscript.
- Written for discrete-event/industrial simulation; does not address the case where the
  model's *own output* is the object of study (our OSSE).

## WildfireGuardian overlap
We must say which of these techniques we applied. Right now the program has an implicit
answer ("we ran it and the numbers looked sensible") which is face validity only — the
weakest item on Sargent's list.

## WildfireGuardian difference
**Requirement imposed on us:** state the intended purpose and the domain of applicability
explicitly ("this model is valid for computing relative orderings of dispatch deadlines
under the stated fuel/terrain/road assumptions; it is not valid for absolute time
prediction"), and then name the specific techniques used: extreme-condition tests
(zero wind, instantaneous fire), degenerate tests (no responder, infinite responder),
sensitivity analysis over the scenario grid, and **comparison to other models** — which
for us means docking the truth fire model against the forecast fire model (Axtell et al.
1996). Face validity alone is not an answer to a judge.

## Novelty threat
BACKGROUND.

## Quotes / page references
None. Full text not retrieved; no verbatim quotation recorded.

## Follow-up papers
- Oreskes, Shrader-Frechette & Belitz (1994), *Science* 263(5147):641–646 — recorded.
- Axtell, Axelrod, Epstein & Cohen (1996), *CMOT* 1(2):123–141 — docking. Recorded.
- Ronchi et al. (2023), *Natural Hazards* 117(2):1493–1519 — domain instance. Recorded.
