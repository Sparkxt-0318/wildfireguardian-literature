# CURRENT_NOVELTY_VERDICT.md

**Date:** 2026-09-19
**Corpus:** 165 verified records · 132 peer-reviewed · 21 preprints ·
10 government reports · 2 software docs · 67 paper notes · 10 thematic reviews
**Search tier attained:** S1–S2 across ten categories. **Not S3.** The Korean
database sweep (KCI/RISS/DBpia) could not be completed, and several citation
traversals failed. Under `NOVELTY_STANDARD.md` §5 this bounds every positive
finding below at `SUPPORTED_CANDIDATE`.

---

## The verdict in one paragraph

**WildfireGuardian has one surviving claim, and it is narrow.** Of nineteen
capability dimensions in the novelty matrix, eighteen are occupied — most of
them heavily. The nineteenth, *dispatch-by deadline*, is empty: no retrieved
work reports the latest fire-relative time at which a responder may depart such
that a full assisted-evacuation round trip still closes. Everything surrounding
that quantity is taken. Inbound responders, pickup dwell, fire-derived arc time
windows, supported evacuation of people who cannot self-evacuate, ensemble
trigger boundaries, forecast value in wildfire, accuracy-is-not-value, Korean
wildfire evacuation optimization, and Korean government AI evacuation routing
**all exist and are verified**. The program's contribution, if it has one, is a
single output quantity and its sensitivity surface — not a system, not a
framing, and not a country.

---

## 1. What claims definitely fail

Stated without softening. Each has a verified occupant.

| Claim | Verdict | Killed by |
|---|---|---|
| WG-C-001 first to model future fire spread for evacuation routing | **REJECTED** | `cova2005trigger` (2005) |
| WG-C-004 probabilistic / ensemble trigger boundaries | **OCCUPIED** | `kalogeropoulos2026ensemble` (5-model ensemble), `kalogeropoulos2023kperil`, `li2018coupling` |
| WG-C-005 modelling assisted evacuation of non-self-evacuating residents | **OCCUPIED** | `moradi2026supported`, `flores2023goal`, `shahparvari2017robust` |
| WG-C-011 scarce assisted-evacuation resource allocation | **OCCUPIED** | `moradi2026supported`, `shahparvari2019fleet`, `alexander2026nursing`, `xu2022multiparking` |
| WG-C-013 intervention ranking | **OCCUPIED** | `orphanoudakis2025mora`, `mendes2024robustsuppression`, `rodriguezfernandez2025mcda` |

And these framings are simply false, whatever we wish:

- "No one models responders moving inbound against evacuees" — `beyki2026modular` names that exact gap and fills it; `averill2007emergencyresponse` did counterflow in 2007.
- "Nobody has done forecast value for wildfire" — `ardid2026forecastvalue`.
- "We are first to note prediction accuracy ≠ decision quality" — `murphy1987accuracyvalue`, **1987**.
- "First Korean wildfire evacuation work" — `kwak2021evacroute`, `kwon2025koreaevac`, `nifos2018evacsystem`.
- "Korea has no evacuation timing rule / ignores people who cannot self-evacuate" — `mois2025evacuationstages` runs a 5 h / 8 h rule that explicitly directs 고령자 등 to evacuate in advance.

---

## 2. What claims remain plausible

**Only one is a real contribution.**

**P1 — The dispatch-by deadline.** `SUPPORTED_CANDIDATE`.
The latest fire-relative departure time for a responder such that ingress +
pickup dwell + egress all complete ahead of modelled fire arrival, reported as
the output and as a function of forecast error. Zero occupants found; the
literal search phrases return zero academic hits.
**Condition:** admissible only if we demonstrate a case where the *deadline*
and the *routing plan* give different operational answers. Otherwise it is
conjunction novelty, which `NOVELTY_STANDARD.md` §3.1 forbids.

**P2 — The sensitivity surface.** `SUPPORTED_CANDIDATE`, and the safer claim.
How that deadline degrades with forecast skill, lead time and latency. No
retrieved work uses a deadline as the dependent variable in a forecast-quality
study. Smaller than P1 and more robust. **Prepare this now as the retreat
position; do not improvise it at the fair.**

**P3 — Latency charged against Korea's operational budget.** Analysis
plausible, result `UNKNOWN`. Three verified numbers make the arithmetic
possible — the 5 h rule, the 12.9–18.2 min geostationary vs 210–318 min
polar-orbit latency gap, gust-driven spread — and nobody has done it. The
sixth agent's finding that **the sub-minute satellite tier does not exist over
Korea** (direct-readout is US/Canada only) is a citable §4(a) Korean
constraint, and it is the strongest Korea-specific material we have.

**P4 — Methodological compliance.** Not novelty. Defensive only.

Everything else — WG-C-002, WG-C-006, WG-C-007, WG-C-008, WG-C-012, WG-C-014 —
survives only in narrowed forms already folded into P1–P4.

---

## 3. The ten closest papers

See `NOVELTY_THREATS.md` §1 for the full table with what each does and does not
do. In rank order:

1. `moradi2026supported` — supported wildfire evacuation, fire-arrival time windows on every arc (**PREPRINT**)
2. `beyki2026modular` — inbound rescue under a coupled fire model, drill-validated
3. `kalogeropoulos2026ensemble` — multi-model ensemble trigger boundaries
4. `li2018coupling` — percentile-indexed trigger buffers from traffic simulation
5. `regnier2008public` — the forecast-quality boundary for evacuation ordering
6. `ardid2026forecastvalue` — skill→economic value in wildfire
7. `murphy1987accuracyvalue` — accuracy ≠ value, 1987
8. `mois2026aievacroute` — Korean government AI outputting resident **and responder ingress** routes (**GOVERNMENT REPORT**)
9. `sun2025decisionfocusedsensing` — decision-focused sensing on evacuation regret
10. `yu2020disruption` — inbound responder feasibility under a modelled hazard

---

## 4. Which research question is strongest

**RQ2 (the dispatch deadline), decisively — but for a different reason than
the program assumed.**

RQ2 is strongest not because assisted evacuation is unexplored (it is
thoroughly explored) but because the whole literature reports **plans** —
routes, fleet sizes, shelter locations — and none reports a **deadline**. That
is a genuine gap in the output space, and it is the only one we found.

**RQ1 is in serious trouble.** Its object was occupied in hurricanes in 2008
(`regnier2008public`) and in wildfire in 2026 (`ardid2026forecastvalue`). Worse,
the sixth agent could not verify **any published curve of wildfire forecast
error growth with lead time**. RQ1's skill axis therefore has no empirical
anchor, and we must not invent a decay rate. RQ1 should be demoted to the
sensitivity axis of RQ2 (i.e. P2) rather than run as an independent question.

---

## 5. What literature could still invalidate this

In priority order — all detailed in `OPEN_QUESTIONS.md`:

1. **`beyki2026modular` full text.** If it reports a latest-extraction or
   safe-time-remaining quantity, **P1 dies and RQ2 must be re-scoped.** This is
   the single highest-priority read in the repository.
2. **`moradi2026supported` journal version.** If peer review adds
   spread-model-derived time windows, the last structural difference closes.
3. **`tang2025transit`** — transit evacuation of carless populations, abstract
   never retrieved, not indexed as wildfire work.
4. **Kamyabniya (2022)** — unidentified two-stage supported-evacuation lead
   inside Moradi's reference list.
5. **The incomplete Korean sweep (KCI/RISS/DBpia).** The largest blind spot,
   and it is in the setting we intend to publish in.
6. **Evidence that dispatch is constrained by tasking and communication rather
   than travel time.** This does not invalidate a claim — it invalidates the
   *decision variable*, and the vulnerable-populations literature currently
   points that way.

---

## 6. What should be searched next

1. `beyki2026modular` full text (CC-BY, obtainable) — **do this first.**
2. Resolve Kamyabniya (2022) from Moradi's reference list.
3. Complete the Korean KCI/RISS/DBpia keyword sweep; no Korean claim is
   searched until this is done.
4. Backward references of `cova2005trigger`; forward citations of
   `li2018coupling` — the founding neighbourhood is only partly mapped.
5. Hard-deadline variants in sensor scheduling / POMDPs, and the
   early-classification "earliness vs accuracy" literature — the two places
   where P2 and WG-C-012's repaired form would die.
6. Greek, Portuguese and Spanish passes — three relevant national literatures,
   entirely unsearched.
7. Full text of `murphy1987accuracyvalue` and `chen1987qualityvalue` — the
   load-bearing killers of WG-C-014, currently known at E1/E2 only.
8. Any published curve of wildfire forecast error vs lead time. If it does not
   exist, that absence must be stated in the paper rather than papered over.

---

## 7. The uncomfortable summary

If the program continues to describe itself as a *system* — Korean, AI-assisted,
uncertainty-aware, assisted-evacuation — every one of those adjectives is
occupied and a prepared judge can name the occupant. If it describes itself as
*computing one number nobody computes, and showing when that number changes
what a commander does*, the claim is small, defensible, and true.

There is a further possibility this repository must state plainly: **the tuned
baseline may win.** If a well-tuned fixed buffer performs within noise of any
forecast-aware policy across realistic forecast quality, that is
`CURRENT_THESIS.md` falsifier #3. It would be a negative result, it would be
publishable, and it must not be suppressed by retuning until the forecast wins.

**Confidence in this verdict:** moderate. The corpus is large and verified, but
three of the six most dangerous items (`beyki2026modular`, `tang2025transit`,
Kamyabniya 2022) are known at abstract level or less, and the Korean sweep is
incomplete. **This verdict should be re-run after the Tier A questions in
`OPEN_QUESTIONS.md` are resolved, and it expires in 90 days under
`NOVELTY_STANDARD.md` §7.**
