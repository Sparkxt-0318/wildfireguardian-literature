# ronchi2023verification

## Citation
Ronchi, E., Wahlqvist, J., Ardinge, A., Rohaert, A., Gwynne, S. M. V., Rein, G.,
Mitchell, H., Kalogeropoulos, N., Kinateder, M., Bénichou, N., Kuligowski, E., &
Kimball, A. (2023). The verification of wildland–urban interface fire evacuation models.
*Natural Hazards*, 117(2), 1493–1519. DOI: 10.1007/s11069-023-05913-2

## Publication status
Published, peer-reviewed, open access (also PMC10220130). Metadata verified via Crossref;
content retrieved via WebFetch of the PMC full text.

## Problem
WUI fire evacuation models couple fire spread, pedestrian/traffic movement and human
behaviour. There was no agreed way to check that such a model does what its developers
intend — and validation against real events is impossible because the empirical data do
not exist.

## Method
A verification protocol: 24 tests grouped by model component. The eight components are
Population, Pre-evacuation, Movement, Route/destination selection, Flow constraints,
Events, Wildfire spread, and **Trigger buffers**. Each test isolates one component with a
known expected behaviour.

## Data
No field data. The tests are analytic/component-level. An example application uses the
open WUI-NITY platform and the k-PERIL trigger-buffer model.

## Outputs
The 24-test protocol, plus a worked application showing what passing looks like.

## Key equations
None extracted.

## Assumptions
That component-level correctness is a necessary (not sufficient) condition for model
credibility, and that verification is a meaningful activity in the absence of validation
data.

## Validation
Deliberately none — the paper is explicit that validation is out of scope because the
empirical data do not exist.

## Limitations
- Verification ≠ validation. The paper says so and we must repeat it.
- The trigger-buffer tests are tied to the k-PERIL/WUI-NITY conception of trigger
  boundaries, i.e. to household egress, not to responder round trips.

## WildfireGuardian overlap
This is the domain-specific counterpart to Sargent (2013). It also confirms something
important for the program's framing: the authoritative WUI evacuation-modelling community
states that validation data are not available. Our simulated results are therefore in the
same evidential position as everyone else's — which is a defence, but only if we say it
ourselves.

## WildfireGuardian difference
**Requirement imposed on us:**
1. Run the published component tests that apply to our model (at minimum: Wildfire spread,
   Movement, Flow constraints, Trigger buffers) and report pass/fail per test. This is
   cheap, citable, and converts "we wrote a simulator" into "we verified a simulator
   against a published protocol".
2. Use their verification/validation vocabulary exactly. We **verify**; we do not
   **validate**. Combined with Oreskes et al. (1994), this fixes the language for the
   whole program.
3. Note the gap: this protocol has no test for an **inbound** responder leg or a
   dispatch-by deadline. Our RQ2 quantity is not covered by any published verification
   test, so we must define and publish our own component test for it — a small but real
   methodological contribution, and a much safer one than claiming decision novelty.

## Novelty threat
BACKGROUND for Category 10. It does bear on WG-C-004 (trigger buffers are a named,
standardised model component with published verification tests — further evidence that the
probabilistic-trigger space is occupied, as CLAIM_REGISTRY already expects).

## Quotes / page references
- "Verification is here defined as the process of determining that a correct
  implementation of the developer's conceptual description has been performed"
  (Introduction).
- "Validation refers to the process of determining the degree to which a simulation is an
  accurate representation of the real world" (Introduction).
- "future research efforts are clearly needed to provide empirical data for validation
  purposes" (Discussion).

## Follow-up papers
- Sargent (2013), *Journal of Simulation* 7(1):12–24 — recorded.
- Oreskes, Shrader-Frechette & Belitz (1994), *Science* 263:641–646 — recorded.
- WUI-NITY and k-PERIL primary papers — **not retrieved here; Category 1/3 agents' domain.**
