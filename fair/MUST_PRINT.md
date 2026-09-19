# MUST_PRINT.md

What goes in the physical binder for the Korea Code Fair, and in what tier.

Tiering is by **how likely you are to be asked about it**, not by how much we
like it. Three of the Tier 1 papers are papers that *damage* our claims — those
are precisely the ones a prepared judge will raise, and being unable to discuss
them is worse than the papers themselves.

Print rules and rehearsal checklist: `BINDER_STRUCTURE.md`.

---

## TIER 1 — MUST KNOW COLD (12)

Each needs a one-page annotation sheet (template below) and evidence level
**E3 minimum** before the fair. Items currently below E3 are flagged; that is a
work item, not a footnote.

| # | Paper | Status | Why Tier 1 | Evidence now |
|---|---|---|---|---|
| 1 | `moradi2026supported` | **PREPRINT** | Closest prior art overall. Occupies WG-C-005 and WG-C-011 and matches WG-C-003's constraint structure | E2/E3 — **read fully before the fair** |
| 2 | `beyki2026modular` | Peer-reviewed | Names "lack of inbound traffic and rescue operations" as the gap and fills it. Could still move WG-C-003 to OCCUPIED | **E2 — highest-priority read in the repo** |
| 3 | `cova2005trigger` | Peer-reviewed | Judge Q1. The founding paper; you will be asked | E3 |
| 4 | `kalogeropoulos2026ensemble` | Peer-reviewed | Kills WG-C-004 outright | **E2 — needed before WG-C-014 or WG-C-009 is spoken** |
| 5 | `li2018coupling` | Peer-reviewed | Judge Q3. Supplies our tuned baseline | E3 |
| 6 | `regnier2008public` | Peer-reviewed | Occupies WG-C-002's object since 2008 | E2/E3 |
| 7 | `ardid2026forecastvalue` | Peer-reviewed | Kills "nobody has done forecast value in wildfire" | E2 |
| 8 | `murphy1987accuracyvalue` | Peer-reviewed | Judge Q10. Owns WG-C-014's proposition since 1987 | **E1 — we have not read the paper that owns this** |
| 9 | `mois2025evacuationstages` | **GOVERNMENT REPORT** | Judge Q7. Korea's operational 5 h/8 h rule; our real comparator | E3 |
| 10 | `mois2026aievacroute` | **GOVERNMENT REPORT** | Judge Q7. Korean AI producing responder ingress routes | E2 — primary release not retrieved |
| 11 | `cruz2013uncertainty` | Peer-reviewed | Judge Q5. Our fire-model error numbers | E3 |
| 12 | `yu2019twin` | Peer-reviewed | Judge Q8. Why our OSSE is non-identical-twin | E3 |

**Four of twelve are below E3.** Numbers 2, 4 and 8 are the urgent ones: #2 and
#4 can change a claim status, and #8 is a paper we cite as owning a proposition
without having read it.

---

## TIER 2 — PRINT / SUPPORTING (annotation sheet only)

Asked about only if the judge goes deep, but each anchors a specific answer.

`kalogeropoulos2023kperil` · `mitchell2023peril` · `dennison2007wuivac` ·
`larsen2011cedar` · `li2015household` · `kalogeropoulos2025dire` ·
`shahparvari2019fleet` · `shahparvari2017robust` · `flores2023goal` ·
`alexander2026nursing` · `rambha2021staged` · `tang2025transit` ·
`yu2020disruption` · `kwon2025koreaevac` · `chang2026multiscale` ·
`sung2025geostationary` · `bennett2026wise` · `ronchi2023verification` ·
`sun2025decisionfocusedsensing` · `raeth2025decisionskill` (PREPRINT) ·
`bischiniotis2019tradeoffs` · `chen1987qualityvalue` · `rothermel1972spread`
(GOVERNMENT REPORT) · `hurlbert1984pseudoreplication` · `zeng2020osse`

---

## TIER 3 — DIGITAL ONLY

Everything else in `bibliography/literature.csv` (165 records). Carry offline
copies on a device — **assume no network at the venue.**

Includes the full BACKGROUND set: fire-spread model documentation, remote-sensing
specifications, statistical methodology, and the adjacent-field occupancy
records (PDPTW, Bayesian experimental design, decision-focused learning) that
exist to stop us re-claiming a solved formulation.

---

## Annotation sheet template

One page per Tier 1 paper. Footer carries the `paper_id`. Preprints stamped
**PREPRINT**; agency documents stamped **GOVERNMENT REPORT — NOT PEER
REVIEWED**.

```
PAPER            <paper_id>  —  <short citation>
STATUS           PEER_REVIEWED | PREPRINT | GOVERNMENT REPORT     EVIDENCE  E_

PROBLEM          (one sentence: what question does it answer?)

METHOD           (one sentence: how?)

DATA             (what was it run on? real event, synthetic, benchmark?)

RESULT           (the headline number or finding, with its units)

LIMITATION       (the honest one, in their words where possible)

WHAT THIS        (which WG-C-### it threatens, and at what level.
THREATENS         Write the damage plainly. If it kills a claim, say so.)

HOW GUARDIAN     (the operational difference, from
DIFFERS           ONE_SENTENCE_DIFFERENCES.md. Different output quantity /
                  decision subject / units. Never "they ignore uncertainty".)

LIKELY JUDGE     (the question this paper prompts)
QUESTION

30-SECOND        (spoken answer. Concede the occupied ground FIRST.)
ANSWER
```

---

## Preparation status

- [ ] 12 Tier 1 annotation sheets written
- [ ] Tier 1 items 2, 4, 8, 10 raised to E3
- [ ] `bibliography/verify_dois.py` exits clean over the printed set
- [ ] `bibliography/check_references.py` exits clean
- [ ] `ABANDONED_CLAIMS.md` recitable from memory — this is what stops
      over-claiming when a question is going badly
- [ ] Every judge question answerable in ≤30 seconds without notes
