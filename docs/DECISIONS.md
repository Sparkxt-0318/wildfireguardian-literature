# DECISIONS.md

Append-only record of research-direction and claim decisions. Never edit or
delete an entry; supersede it with a new one. This file is the defense against
novelty drift (`FAILURE_MODES.md` §9) — it makes claim rewording visible.

Format:

```
## D-### — <title>
Date:
Decision:
Rationale:
Evidence:        (paper_ids / claim_ids / review sections)
Supersedes:      (D-### or none)
Consequences:    (what changes in the repo or the research plan)
```

---

## D-001 — Repository is adversarial by construction
Date: 2026-09-19
Decision: The literature process attempts to **disprove** WildfireGuardian's
novelty. Threatening papers are filed at full threat level and never softened.
A strong negative novelty result is a successful outcome.
Rationale: The failure mode of a self-run literature review is advocacy. The
only structural defense is to make disproof the stated goal and to separate the
agent that finds a paper from the agent that rates its threat.
Evidence: `docs/FAILURE_MODES.md` §9.
Supersedes: none.
Consequences: `AGENTS.md` §2; threat levels assigned by overlap, not prestige.

## D-002 — Conjunction novelty is inadmissible
Date: 2026-09-19
Decision: "No one combines all of A, B, C, D" may not be used as a novelty
argument anywhere in this program.
Rationale: Any sufficiently long conjunction is unique; it is therefore not
evidence. It is also the argument judges are best at dismantling.
Evidence: `docs/NOVELTY_STANDARD.md` §3.1.
Supersedes: none.
Consequences: Claims must rest on N1/N2, or N3, or N4 with a demonstrated
domain-specific effect. Combination claims must state what conclusion the
combination produces that the parts cannot.

## D-003 — Korean setting is not, by itself, novelty
Date: 2026-09-19
Decision: WG-C-007 is admissible only under `NOVELTY_STANDARD.md` §4 (a), (b),
or (c). "First in Korea" may not be said without one of them demonstrated.
Rationale: Geographic application novelty is N4, the weakest type, and is the
easiest claim for a judge to puncture ("so you ported an existing method?").
Evidence: `docs/NOVELTY_STANDARD.md` §4.
Supersedes: none.
Consequences: Korean-specific evidence-gathering is retargeted at showing that
Korean conditions *change the answer*, not merely that they differ.

## D-004 — Comparator strength is part of the claim
Date: 2026-09-19
Decision: Results against an untuned buffer/trigger baseline are treated as
failed experiments, not as findings.
Rationale: `FAILURE_MODES.md` §1 — the highest-probability failure of this
program, and the first thing a reviewer will ask.
Evidence: `docs/FAILURE_MODES.md` §1; claim WG-C-006.
Supersedes: none.
Consequences: Every RQ1 experiment must report the baseline tuning sweep. If
the tuned baseline wins, that is the publishable finding.

## D-005 — Priority is set by public disclosure, not peer review
Date: 2026-09-19
Decision: A preprint that computes our quantity occupies the claim, regardless
of review status. Preprint date is the priority date.
Rationale: Novelty is about what is publicly prior. Excluding preprints would
make our novelty assessment systematically over-optimistic, and 2025–2026
preprints are the most likely claim-killers.
Evidence: `docs/CITATION_RULES.md` (Priority dating); `INCLUSION_CRITERIA.md`.
Supersedes: none.
Consequences: Dedicated preprint sweeps in every search round.
