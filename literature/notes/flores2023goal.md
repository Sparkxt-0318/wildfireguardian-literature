# flores2023goal

## Citation
Flores, I., Ortuño, M. T., & Tirado, G. (2023). "A goal programming model for early evacuation of
vulnerable people and relief distribution during a wildfire." *Safety Science*, 164, 106117.
DOI: 10.1016/j.ssci.2023.106117.

## Publication status
`PEER_REVIEWED`, journal article, CLOSED access (CC-BY-NC-ND per Unpaywall licence field).
**Abstract NOT retrieved from the publisher or Semantic Scholar** (abstract field null). Content
below is reconstructed from (a) the literature review in Moradi et al. (2026) §2, which describes
this paper in detail, and (b) the publisher landing page summary returned by WebSearch.
Evidence level **E2 / second-hand**. `NEEDS_FULL_TEXT` — this record must be verified by Agent C
before it is cited.

## Problem
Early evacuation of vulnerable people during a wildfire, jointly with relief-supply distribution.
Vulnerable people who cannot evacuate independently either receive assistance or make their way to
designated **pick-up points**, arriving there dynamically according to their own perception of the
situation.

## Method
Mixed-integer **goal programming** (per Moradi et al., a lexicographic/goal formulation in the
Flores line). The evacuation process is modelled as a dynamic network of **safe areas** (shelters
and hospitals) and **unsafe areas** (pick-up points), with health-priority classification of
evacuees, dynamic arrivals at pick-up points, and heterogeneous vehicles. Objectives: maximise the
number of evacuees (weighted toward high-priority individuals) while minimising evacuation time,
cost, and unmet supply needs.

## Data
Case study based on the **2019 Saddleridge Fire**, San Fernando Valley, Los Angeles County,
California.

## Outputs
An evacuation-and-distribution plan: who is collected, by which vehicle, in what order, and how
relief supplies are distributed, under a lexicographic ordering of objectives.

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Per Moradi et al.'s critique: temporary shelters are treated as already built (no facility-location
decision), and the model does **not** incorporate uncertainty in evacuee numbers, travel times,
route availability, or service capacity.

## Validation
Retrospective case study on a real wildfire; no validation against observed evacuation outcomes.

## Limitations
No uncertainty. No facility location. Critically for WildfireGuardian: **no hazard-progression
feasibility constraint on any leg is evidenced** — the "unsafe area" designation is static.

## WildfireGuardian overlap
- Wildfire. Vulnerable people who cannot self-evacuate. Pick-up points. Heterogeneous vehicles
  routed from safe areas to unsafe areas and back. Health-priority-driven allocation.
- The *dynamic arrival* of evacuees at pick-up points is a modelling refinement WildfireGuardian
  has not proposed and would have to concede.
- Health-priority classification governs who is served first — this is scarce-resource allocation
  for assisted wildfire evacuation, published in 2023.

## WildfireGuardian difference
- No fire-arrival constraint on legs; the fire does not close routes over time in this model.
- No timing output: the temporal question answered is "how long does the plan take," not
  "how late may it start."
- Medical priority is the allocation criterion, where PROJECT_CONTEXT forbids WildfireGuardian from
  medicalising residents. **This is a genuine and defensible difference of framing** — but note it
  cuts both ways: Flores et al. establish that prioritisation in supported wildfire evacuation is
  normally done on health grounds, so WildfireGuardian must justify a mobility/transport-access
  criterion rather than assume it.

## Novelty threat
**level: HIGH**
- **WG-C-005** → `OCCUPIED`. Assisted wildfire evacuation of vulnerable people, published, in a
  safety-science journal, with a real California fire case.
- **WG-C-011** → `OCCUPIED`. Priority-based allocation of a heterogeneous fleet among vulnerable
  evacuees is exactly the WG-C-011 sentence.
- **WG-C-003** → no direct threat (no deadline, no hazard progression on legs).

## Quotes / page references
No verbatim quotation is recorded because the article body and abstract were not retrieved.
Do not attribute quoted text to this paper until the full text is obtained.

## Follow-up papers
- Flores, Ortuño, Tirado & Vitoriano (2020), *Mathematics* 8(4):648 — the originating supported-
  evacuation lexicographic goal programme (Palu earthquake/tsunami case). Open access; retrieved.
- Moradi, Sauré & Patrick (2026) — critiques and extends this work.
- Kamyabniya (2022) — cited alongside this work by Moradi et al.; **primary record not retrieved**.
