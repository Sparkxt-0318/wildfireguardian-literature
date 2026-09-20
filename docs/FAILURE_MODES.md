# FAILURE_MODES.md

The ways this research program can be wrong, and the ways this repository can
lie to us. Written in advance, because every one of these is more persuasive
from the inside than from the outside.

---

## §1. Weak-baseline failure (highest probability)

**The failure:** forecast-aware policy beats a *naive* fixed buffer, and we
report it as a result.

**Why it happens:** tuning the baseline is work that makes our numbers worse.
The incentive is structural.

**Why it is fatal:** any competent reviewer or judge asks "what if you just used
a bigger buffer?" If we cannot answer with a *tuned* buffer sweep, the result
is worthless.

**Guard:** WG-C-006. The baseline buffer/trigger lead time must be optimized
over the same scenario distribution the forecast-aware policy sees, and the
sweep must be reported. If the tuned baseline wins, that is the finding.

---

## §2. Inverse crime / self-generated uncertainty

**The failure:** the same fire model generates both the "truth" and the
"forecast," so forecast error is just the model's own noise. Our uncertainty
model is then self-fulfilling, and measured forecast value is an artifact.

**Why it is fatal:** it makes the central result circular. This is judge
question Q8 and it is a good question.

**Guard:**
- Declare the OSSE design explicitly (`WG-C-010`).
- Use **fraternal twin**, not identical twin: truth and forecast must come from
  different models or at minimum different parameterizations/fuel inputs.
- Report results as a function of *injected* forecast error, so the conclusion
  is a boundary in error-space rather than a single number that depends on our
  error model.
- Cite the OSSE-design literature that documents identical-twin optimism
  (see `literature/reviews/10-evaluation-methodology.md`).

---

## §3. Pseudoreplication

**The failure:** 10,000 simulated scenarios from 3 fire events are reported as
10,000 independent samples. Confidence intervals become fictitious.

**Guard:** the unit of analysis is the **event**, not the scenario. Event-level
(cluster) bootstrap. Report the number of independent events prominently, and
never let scenario count masquerade as sample size.

---

## §4. Hindsight leakage

**The failure:** the decision policy sees information that would not have been
available at decision time — final fire perimeter, the actual wind shift, the
event's known duration.

**Guard:** every quantity the policy consumes carries an availability
timestamp. A quantity may be used only if `t_available <= t_decision`. This
must be enforced in code and stated in the paper. See judge question Q9.

---

## §5. Deadline realism failure

**The failure:** the computed dispatch deadline is travel-time feasible but
operationally meaningless, because real dispatch is constrained by resource
availability, incident command, communication, and the resident's own
readiness — not by travel time.

**Why it matters:** this would make RQ2's decision variable the wrong one. It
is the falsifier listed in `CURRENT_THESIS.md` §4.

**Guard:** seek evidence from the assisted-evacuation and post-incident
literature on what actually binds. If travel-time feasibility is not the
binding constraint, say so and reframe. Do not defend the deadline because it
is what we built.

---

## §6. Metric-decision mismatch

**The failure:** we optimize or report a spatial accuracy metric (IoU, Jaccard,
burned-area agreement) and assume it tracks decision quality. It may not:
a forecast that is spatially excellent but late, or excellent overall but wrong
in one direction, can be decision-useless.

**Guard:** WG-C-014. Report decision-relevant loss directly. If we can
*demonstrate* the non-monotonicity, that is a contribution; if we merely assume
it, it is a hole.

---

## §7. Vulnerability overreach

**The failure:** describing residents in clinical or deficit terms not
supported by evidence — inferring medical conditions from age, or treating
"elderly" as synonymous with "immobile."

**Guard:** "cannot self-evacuate" is defined operationally as a transport-access
and mobility condition, sourced from transport-disadvantage and
evacuation-assistance literature. No diagnostic language. No invented
prevalence rates. See `literature/reviews/09-vulnerable-populations.md`.

---

## §8. Simulation-as-world

**The failure:** stating conclusions about the world when we have conclusions
about a simulation.

**Guard:** every result sentence names its domain of validity. "In our
simulated Korean mountain-village network under the stated fuel and wind
distributions, ..." The transfer argument is separate, explicit, and weaker
than the simulation result.

---

## §9. Repository failure modes (how this repo lies to us)

| Failure | Symptom | Guard |
|---|---|---|
| **Threat suppression** | Threatening papers described in weaker terms, or filed at a lower level than they deserve | Threat level set by overlap, reviewed adversarially by a different agent than the one who found the paper |
| **Novelty drift** | Claims silently reworded to dodge prior art without a decision record | Every claim reword needs a `docs/DECISIONS.md` entry; old text retained |
| **Fabricated citation** | A DOI that does not resolve; an author list that is subtly wrong | `UNVERIFIED` discipline; ≥2 independent sources; `doi_registry.csv` resolution checks |
| **Search theater** | Long query logs that all hit the same neighbourhood | Required adjacent-field, preprint, and non-English dimensions in `SEARCH_PROTOCOL.md` §2 |
| **Stale confidence** | A 2024-searched claim still marked SUPPORTED in 2026 | 90-day auto-expiry to `UNKNOWN` (`NOVELTY_STANDARD.md` §7) |
| **Conjunction creep** | "No one combines all of..." reappearing in drafts | Explicitly forbidden, `NOVELTY_STANDARD.md` §3.1 |

---

## §10. Tool-induced fabrication (observed 2026-09-19)

**The failure:** a fetch of a binary PDF returned plausible-looking statistics
that **contradicted the paper's actual abstract**. The numbers were fluent,
specific, and wrong. Had they been recorded, they would have entered the
bibliography as verified quantities attributed to a real, correctly-cited
paper — the hardest kind of error to detect downstream, because every
surrounding field is correct.

**How it was caught:** the agent cross-checked against an HTML rendering of the
same source and found the figures disagreed, then discarded them.

**Guard:**
1. **Never extract numbers from a binary PDF through a summarising fetch.** Use
   an HTML rendering, the publisher's landing page, or a real text extractor.
   **A real extractor now exists in this repository:**
   `python3 bibliography/extract_pdf_text.py <file.pdf>` (pdfminer, with pypdf
   fallback) emits page-marked text, and `--grep` reports whether a term
   appears at all, with its page. Use it instead of asking a model to read a
   PDF. It also warns when a PDF yields too little text per page, which is the
   signature of a scanned document or a form — the case where a summarising
   fetch is most likely to invent content. An earlier agent reported that no
   extraction toolchain was available; that was wrong, and the wrong belief
   cost a retrieval.
2. Any quantitative value requires evidence level **E4** — located at a
   specific page or section — and corroboration from a second rendering.
3. When a retrieved number and an abstract disagree, **discard the number**.
   Do not average, reconcile, or pick the more convenient one.

This is not a hypothetical. It happened during the first sweep, and the only
reason it did not enter the repository is that the agent checked.

---

## §11. Self-citation contamination (observed 2026-09-20)

**The failure:** a literature search returned **the project's own GitHub
repository**, and the search engine paraphrased its README back as though it
were an independent source. A novelty search that finds our own writing and
reports it as prior art is not merely useless — it is self-confirming in the
most dangerous direction, because our own README says what we want to be true.

**Why it is insidious:** the returned text is topically perfect, fluently
phrased, and agrees with us. Every heuristic an agent uses to judge relevance
fires positively.

**Guard:**
1. Any result from `github.com/Sparkxt-0318/*`, this repository, or any
   WildfireGuardian project surface is **self-citation, never prior art, and
   never corroboration.** Discard it and log the query as contaminated.
2. A source that agrees with us unusually well deserves *more* scrutiny than
   one that contradicts us, not less.
3. Corroboration requires a source with an independent origin. Two aggregators
   copying one upstream record are one source (`CITATION_RULES.md`); our own
   repository echoed back is zero sources.

---

## §12. Verifying a fact and then asserting its opposite (observed 2026-09-20)

**The failure:** the repository recorded that wildfire forecast-value
evaluations do not use tuned baselines, and built a defensive claim (WG-C-006)
on that gap. Full-text reading of `ardid2026forecastvalue` showed the opposite:
it selects the optimal classification threshold per region, retrospectively, to
maximise the same value metric it then reports. The comparator **is** tuned.

The belief was formed at E2 — the abstract does not mention thresholds — and
was never revisited when the paper was promoted to a CRITICAL threat.

**Why it matters beyond the one fact:** the defence "their comparator wasn't
tuned" would have been spoken to a judge who had read the Methods section.

**Guard:**
1. A claim of the form "nobody does X" must be re-checked against the full text
   of the closest work **before** any argument is built on it, not after.
2. When a paper is promoted to `CRITICAL` or `HIGH`, every existing assertion
   about it is re-opened, not inherited.
3. Absence claims are E3 claims (`EVIDENCE_LEVELS.md`). This one was made at E2
   and stood for a day.
