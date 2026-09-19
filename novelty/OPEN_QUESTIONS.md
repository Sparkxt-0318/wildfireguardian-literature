# OPEN_QUESTIONS.md

Unresolved prior-art questions, ordered by how much damage an unfavourable
answer does. Each names what would resolve it.

An honest gap here is worth more than a confident guess, and a guess in this
repository will eventually be read aloud to a judge.

---

## Tier A — could end a research question

**A1. Does `beyki2026modular` report a latest-extraction or safe-time-remaining
quantity per waypoint?**
If yes, WG-C-003 moves to `OCCUPIED` and RQ2 must be abandoned or re-scoped.
The paper explicitly names "the lack of inbound traffic and rescue operations"
as the gap it fills. *Resolution: full text (CC-BY, obtainable; ScienceDirect
returned 403 to the agent).* **Highest-priority read in the repository.**

**A2. What is Kamyabniya (2022)?**
A citation-only lead inside `moradi2026supported` §2, described there as a
two-stage stochastic supported-evacuation model with shelter location and
routing. Unidentified — we do not know if it is a thesis, a paper, or what it
outputs. *Resolution: resolve the citation from Moradi's reference list.*
Could be another CRITICAL.

**A3. Does `tang2025transit` report a departure deadline?**
Transit evacuation of carless populations by RL (*TR-C* 180:105342). Abstract
never retrieved. Structurally our trip, and **not indexed as wildfire work** —
which is exactly how a claim-killer stays unnoticed. *Resolution: full text.*

**A4. Is travel-time feasibility ever documented as the binding constraint in a
real assisted wildfire evacuation?**
This is `CURRENT_THESIS.md` falsifier #4, and the Category 9 literature
currently points *toward* it: `matsuo2025evacuation` names communication, not
travel time, among its four failure areas; `chang2026multiscale` finds
communication timing governs outcomes; `shahparvari2019fleet` found 1,100 late
evacuees could have been moved with 7 vehicles. **If dispatch is really
constrained by tasking and communication rather than travel time, RQ2 optimises
the wrong variable.** *Resolution: after-action reviews and incident reports;
failing that, declare the regime as an explicit assumption (responder exists
and is tasked; the question is send-now-vs-wait).*

---

## Tier B — could force a claim to be restated

**B1. Does any wildfire paper use a *tuned* trigger as its baseline?**
WG-C-006's entire defensive value rests on the answer being no. Needs a
baselines-focused re-read of Categories 1–3. `li2018coupling`'s
percentile-indexed buffers are the closest and may already qualify.

**B2. Hard-deadline variants in sensor scheduling / POMDPs.**
Searched shallowly. This is where WG-C-008's last surviving corner
(deadline-conditioned observation value) would die.

**B3. The early-classification "earliness vs accuracy" literature.**
The closest formal treatment of latency-as-decision-variable, and it was not
systematically searched. Directly threatens WG-C-012's repaired form.

**B4. Is the MOIS 5 h / 8 h threshold derived or administrative?**
If it has a published derivation, it is a *tuned* comparator and WG-C-006's
framing changes. If it is administrative fiat, we must tune it ourselves before
claiming to beat it. *Resolution: MOIS/KFS primary documents.*

**B5. Murphy & Ehrendorfer 1987 and Chen et al. 1987 are known at E1/E2 only.**
They are the load-bearing killers of WG-C-014 and we have not read them. Per
`EVIDENCE_LEVELS.md` §1, a status change to `OCCUPIED` requires E3.

---

## Tier C — coverage gaps that could hide anything

**C1. The Korean KCI / RISS / DBpia keyword sweep could not be completed.**
KCI's server-side search is not drivable via fetch; DBpia returned 503. This is
the single largest blind spot in the corpus, and it is in the setting we intend
to publish in. **No Korean claim may be called searched until this is done.**

**C2. Backward references of `cova2005trigger` were never traversed**
(publisher 403), and the forward-citation chain of `li2018coupling` returned
empty from one source and was not retried. The founding paper's citation
neighbourhood is therefore only partially mapped.

**C3. No Greek, Portuguese, Spanish, or Japanese pass** — despite three
relevant national wildfire-evacuation literatures (`kalogeropoulos2025dire` is
Greek, `beyki2026modular` is Portuguese, `rodriguezfernandez2025mcda` is
Portuguese).

**C4. No verified Korean road-geometry evidence exists.**
`PROJECT_CONTEXT.md` asserts "narrow mountain road networks." **That assertion
is currently unsourced and must not be used until it is.**

**C5. Primary MOIS press release for the 2026 AI programme was not retrieved** —
six independent Korean news outlets corroborate it, but the primary document
was not obtained. `mois2026aievacroute` is a HIGH threat resting on secondary
sources.

**C6. Korean human-impact statistics** (deaths, evacuee counts, assisted
evacuations) could not be verified from primary sources. Three KFS PDFs failed
to parse. **Deliberately not recorded**, and must not appear on a poster.

---

## Standing methodological questions

**M1. The OSSE has no calibration anchor.** `halliwell2014fraternal` makes OSSE
credibility depend on OSE↔OSSE benchmarking, and `ronchi2023verification`
states the validation data for WUI evacuation models do not exist. Every
magnitude WG-C-002 produces is therefore an uncalibrated OSSE output. The fix
is not more scenarios: declare it uncalibrated, claim orderings not magnitudes,
and publish the identical-vs-non-identical twin gap.

**M2. With fewer than ~10 independent fire events, is the forecast-quality
boundary distinguishable from noise at all?** Event-level MCSE must be computed
*before* any boundary is presented, not after.
