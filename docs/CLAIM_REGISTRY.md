# CLAIM_REGISTRY.md

Every assertion WildfireGuardian might make in a paper, poster, or fair defense
lives here with an ID and a status. **If it is not in this registry, it may not
be claimed.**

Statuses: `SUPPORTED_CANDIDATE` `WEAKENED` `OCCUPIED` `REJECTED` `UNKNOWN`
`NEEDS_FULL_TEXT` (definitions in `docs/NOVELTY_STANDARD.md` §5).

`UNKNOWN` is the default and carries no credit. A claim is only as good as the
adversarial search that failed to kill it.

---

## Summary table

| ID | Claim (short) | Status | Threat papers | Last reviewed |
|---|---|---|---|---|
| WG-C-001 | First to model future fire spread for evacuation routing | REJECTED | many | 2026-09-19 |
| WG-C-002 | Forecast-skill boundary for protective action vs tuned trigger | UNKNOWN | — | 2026-09-19 |
| WG-C-003 | Inbound-inclusive assisted-evacuation dispatch deadline | UNKNOWN | — | 2026-09-19 |
| WG-C-004 | Probabilistic / ensemble trigger boundaries | UNKNOWN | — | 2026-09-19 |
| WG-C-005 | Assisted evacuation of non-self-evacuating residents modeled | UNKNOWN | — | 2026-09-19 |
| WG-C-006 | Tuned-trigger comparator as evaluation standard | UNKNOWN | — | 2026-09-19 |
| WG-C-007 | Korean-setting wildfire evacuation-timing analysis | UNKNOWN | — | 2026-09-19 |
| WG-C-008 | Decision-directed / deadline-aware wildfire sensing (VOI) | UNKNOWN | — | 2026-09-19 |
| WG-C-009 | Robust protectability under fire-model error | UNKNOWN | — | 2026-09-19 |
| WG-C-010 | OSSE methodology applied to wildfire evacuation decisions | UNKNOWN | — | 2026-09-19 |
| WG-C-011 | Scarce assisted-evacuation resource allocation | UNKNOWN | — | 2026-09-19 |
| WG-C-012 | Forecast *latency* (not just skill) as a decision variable | UNKNOWN | — | 2026-09-19 |
| WG-C-013 | Intervention ranking under fire uncertainty | UNKNOWN | — | 2026-09-19 |
| WG-C-014 | Spatial fire-prediction accuracy (IoU) ≠ evacuation decision quality | UNKNOWN | — | 2026-09-19 |

---

## Full records

```yaml
claim_id: WG-C-001
claim: "WildfireGuardian is the first system to model future wildfire spread for evacuation routing."
status: REJECTED
reason: >
  Coupling modeled fire progression to evacuation triggers or routing is the
  founding move of the wildfire trigger-modeling literature and has been done
  repeatedly since the mid-2000s. This sentence is false and must never be
  spoken.
closest_prior_art: [PENDING_SEARCH]
replacement_claim: WG-C-003
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-002
claim: >
  "We identify the forecast-quality boundary (skill x lead time x latency) at
  which forecast-aware wildfire protective action begins to outperform a tuned
  trigger/buffer policy."
status: UNKNOWN
novelty_type: N2 (quantity) with N4 risk
falsifier: >
  Any wildfire paper reporting decision performance as a function of forecast
  skill against an optimized positional-trigger baseline.
adjacent_risk: >
  Forecast-value / cost-loss theory (hurricane, flood, severe weather) already
  owns the general machinery. Only the wildfire instantiation can be novel.
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-003
claim: >
  "For residents who cannot self-evacuate, we compute the latest fire-relative
  responder dispatch time such that the full round trip (base -> resident ->
  pickup -> safe destination) completes, with fire-arrival feasibility enforced
  on the inbound leg as well as the outbound leg."
status: UNKNOWN
novelty_type: N2 (quantity)
why_it_could_survive: >
  The trigger literature computes egress deadlines for self-evacuating
  households; routing literature computes routes, not dispatch-by deadlines.
falsifier: >
  Any work computing a responder-inclusive latest-dispatch time under a modeled
  future fire, including PDPTW/VRP formulations with fire-derived time windows
  where the reported output is a dispatch deadline.
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-004
claim: "We use probabilistic / multi-model-ensemble fire predictions to define trigger boundaries."
status: UNKNOWN
expected_status: OCCUPIED
note: >
  Expected to be occupied by the probabilistic-trigger and PERIL/k-PERIL
  lineage. Registered anyway so the occupation is documented rather than
  discovered by a judge.
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-005
claim: "We model assisted/supported evacuation of residents who cannot self-evacuate."
status: UNKNOWN
expected_status: OCCUPIED or WEAKENED
note: >
  Assisted evacuation of vulnerable populations is an active area, especially
  2025-2026. This claim is a framing, not a contribution; the contribution must
  be WG-C-003's quantity.
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-006
claim: >
  "We evaluate forecast-aware policies against a tuned trigger/buffer
  comparator rather than a naive fixed buffer."
status: UNKNOWN
novelty_type: N3 (methodological, weak) / evaluation-standard claim
note: >
  This is a methodological hygiene claim. It is defensible as rigor but is a
  weak novelty claim on its own. Its real function is to protect WG-C-002 from
  the "you beat a strawman" objection.
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-007
claim: "We provide wildfire evacuation-timing analysis for the Korean setting."
status: UNKNOWN
novelty_type: N4 (application) -- weak by standard
gate: >
  Admissible only under NOVELTY_STANDARD §4 (a), (b), or (c). Must NOT be
  phrased as "first in Korea" without one of those demonstrated.
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-008
claim: >
  "We select wildfire observations by their effect on the evacuation decision
  (decision-directed / deadline-aware sensing) rather than by predictive
  accuracy."
status: UNKNOWN
open_question: >
  Is this methodological novelty (unlikely -- Bayesian experimental design and
  VOI are mature) or wildfire-application novelty (plausible)?
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-009
claim: "We characterize which locations remain protectable under fire-model error (robust protectability)."
status: UNKNOWN
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-010
claim: "We use an OSSE design to evaluate wildfire evacuation decision quality."
status: UNKNOWN
self_criticism: >
  An OSSE where the same model generates truth and forecast risks inverse
  crime. Must be declared, and forecast error must be injected in a way that is
  not simply the truth model's own noise. See FAILURE_MODES §2.
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-011
claim: "We allocate scarce assisted-evacuation resources (vehicles/crews) among residents."
status: UNKNOWN
expected_status: OCCUPIED
note: Emergency resource allocation and triage routing are mature OR topics.
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-012
claim: "We treat forecast latency -- not only skill -- as a first-class decision variable."
status: UNKNOWN
note: >
  Potentially the sharpest surviving edge of WG-C-002: a skilful forecast that
  arrives after the dispatch deadline has zero decision value. Search hard for
  prior art on timeliness/latency in forecast value.
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-013
claim: "We rank candidate protective interventions by their effect on mission feasibility."
status: UNKNOWN
last_reviewed: 2026-09-19
```

```yaml
claim_id: WG-C-014
claim: >
  "We show that spatial fire-prediction accuracy (e.g. IoU/Jaccard of predicted
  vs actual burned area) is not monotonically related to evacuation decision
  quality."
status: UNKNOWN
note: >
  If true and not already shown, this is a genuinely useful negative result and
  a strong judge answer (see JUDGE_QUESTIONS Q10).
last_reviewed: 2026-09-19
```
