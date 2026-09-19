# hurlbert1984pseudoreplication

## Citation
Hurlbert, S. H. (1984). Pseudoreplication and the Design of Ecological Field Experiments.
*Ecological Monographs*, 54(2), 187–211. DOI: 10.2307/1942661

## Publication status
Published, peer-reviewed journal article. Metadata verified via Crossref API 2026-09-19.

## Problem
Inferential statistics are routinely applied to data in which the treatments are not
replicated, or in which the "replicates" are not statistically independent. The resulting
p-values are not valid tests of the treatment hypothesis.

## Method
Definitional / methodological paper plus a survey of 176 published experimental studies
(1960–early 1980s), classifying each by whether inference was made with an error term
appropriate to the hypothesis.

## Data
Published ecological field experiments; no new empirical data.

## Outputs
- A definition of pseudoreplication as a specific error of inference.
- An incidence estimate: pseudoreplication in 27% of the 176 studies, and 48% of those
  that applied inferential statistics (per abstract).
- Design prescriptions: interspersion of treatments; the distinction between pre-layout
  and layout-specific alpha; "nondemonic intrusion".

## Key equations
None used here. The operative structure is the ANOVA error term: the denominator must be
the mean square that varies across *experimental* units, not across subsamples.

## Assumptions
That the inferential target is a treatment effect defined over a population of
independently assigned experimental units.

## Validation
Not applicable (methodological). Support is the literature survey.

## Limitations
- The strong form of the doctrine is contested: Oksanen (2001, *Oikos*) argues it
  stigmatises legitimate large-scale designs; Davies & Gray (2015) and Colegrave &
  Ruxton (2017) argue it is applied dogmatically in peer review. **Those responses were
  seen in abstract only (E2) and are not recorded as metadata items.**
- Hurlbert's framing is about designed field experiments; the mapping onto *simulation*
  scenario sets requires an argument we must supply, not one he supplies.

## WildfireGuardian overlap
Our scenario set is generated from a finite number of fire events. Many scenarios derived
from one event (different ignition offsets, wind perturbations, resident placements) are
subsamples of that event, not independent replicates. Any test that counts n = number of
scenarios commits exactly the error Hurlbert defines.

## WildfireGuardian difference
**Requirement imposed on us:** the experimental unit is the *fire event*. All headline
inferential statements (forecast-aware vs tuned trigger; dispatch-deadline sensitivity)
must use an error term that varies across events, e.g. event-level random effects or an
event-level cluster bootstrap. Per-scenario n may be reported descriptively but never as
the denominator of a test. We must state the number of *events* next to every p-value.

## Novelty threat
BACKGROUND. It threatens no WildfireGuardian claim. It threatens our *statistics* if
ignored — and a judge who knows this paper will ask "what is your n?".

## Quotes / page references
- "the use of inferential statistics to test for treatment effects with data from
  experiments where either treatments are not replicated ... or replicates are not
  statistically independent" (Abstract, p. 187).
- "it is the testing for treatment effects with an error term inappropriate to the
  hypothesis being considered" (Abstract, p. 187).

## Follow-up papers
- Lazic, Clarke-Williams & Munafò (2018), *PLOS Biology* 16(4):e2005282 — recorded.
- Oksanen (2001), *Oikos* — critique. RECALL/abstract-only; not recorded as metadata.
- Colegrave & Ruxton (2017), *Trends in Ecology & Evolution* — critique. Abstract only.
- Davies & Gray (2015), *Ecology and Evolution* — critique. Abstract only.
