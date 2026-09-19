# ABANDONED_CLAIMS.md

Claims WildfireGuardian may **not** make, and the verified paper that ended
each one.

This is the most valuable document in the repository. It is what keeps us from
over-claiming under pressure, and it is the first thing to recite when a judge
starts probing — conceding the occupied ground early removes most of the
attack surface (`fair/BINDER_STRUCTURE.md`, Tab 2).

---

## Fully rejected

| Claim | Killed by | The specific finding |
|---|---|---|
| **WG-C-001** — first to model future fire spread for evacuation routing | `cova2005trigger` (2005) | Trigger buffers computed from fire-spread modelling and GIS, Calabasas Fire case study. The founding move of the field, twenty-one years ago. |
| **WG-C-004** — probabilistic / ensemble trigger boundaries | `kalogeropoulos2026ensemble`, `kalogeropoulos2023kperil`, `li2018coupling` | k-PERIL produces stochastic trigger boundaries with uncertainty rosettes; the 2026 paper builds them from a **five-model ensemble** of flame-spread models. Three independent occupants. |
| **WG-C-005** — modelling assisted evacuation of people who cannot self-evacuate | `moradi2026supported`, `flores2023goal`, `shahparvari2017robust` | Title-level occupancy, in wildfire, with a non-medical population definition ("people with no vehicles"). Demote to a scope statement. |
| **WG-C-011** — scarce assisted-evacuation resource allocation | `moradi2026supported`, `shahparvari2019fleet`, `alexander2026nursing`, `xu2022multiparking` | Fleet sizing, shelter activation and mobility-class↔vehicle-class matching are all solved. Any surviving allocation claim must be about allocating *by deadline slack*, which is a consequence of S1, not an independent claim. |
| **WG-C-013** — intervention ranking | `orphanoudakis2025mora`, `mendes2024robustsuppression`, `rodriguezfernandez2025mcda` | Multicriteria wildfire resource allocation, robust suppression placement and participatory spatial prioritisation are mature. |

---

## Severely weakened — claimable only in the narrowed form

| Claim | Weakened by | What is left |
|---|---|---|
| **WG-C-002** — forecast-skill boundary | `regnier2008public` (the boundary, hurricanes, 2008); `ardid2026forecastvalue` (skill→value, wildfire, 2026) | Only: *how the boundary moves when the comparator is strengthened from a fixed buffer to a tuned one* — **and only if it actually moves.** If it does not, this is `CURRENT_THESIS.md` falsifier #3 and the finding is negative. |
| **WG-C-006** — tuned comparator | `li2018coupling` (percentile-indexed buffers); `berlinghieri2024pm25` (decision-level evaluation vs a strong baseline) | Defensive hygiene, not novelty. Keep doing it; never claim it. |
| **WG-C-007** — Korean setting | `kwon2025koreaevac`, `chang2026multiscale`, `kwak2021evacroute`, `mois2025evacuationstages`, `mois2026aievacroute` | Fails `NOVELTY_STANDARD.md` §4(a) and §4(b) — **not demonstrated**. Admissible only under §4(c): Korea is *incidental* to an N2 quantity claim. Absorb into S1 as a setting statement. |
| **WG-C-008** — decision-directed sensing | `malings2016voisensor` (method), `sun2025decisionfocusedsensing` (hazard evacuation), `shao2026beliefaware` (wildfire sensing) | The registry's open question is answered: **N4, not N3**, and even the N4 is partial. Only *deadline-conditioned* observation value survives, and only bundled with S1. Standing alone it is not a contribution. |
| **WG-C-012** — forecast latency | `bischiniotis2019tradeoffs`, `lopez2020bridging`, `regnier2006dynamic` | "Timeliness matters" is owned. Only *latency proper* — observation-to-product delay at fixed skill **and** fixed lead time — survives. The claim text must be repaired to say that, or it is OCCUPIED. |
| **WG-C-014** — accuracy ≠ decision quality | `murphy1987accuracyvalue` (1987), `chen1987qualityvalue` (1987), `mandi2024dfl`, `raeth2025decisionskill`, `xu2026wildfirefm` | The proposition has been owned for **thirty-nine years**. Claimable only with the *geometric mechanism* stated — error location relative to the ingress/egress route — never as the slogan. |
| **WG-C-009** — robust protectability | `mendes2024robustsuppression`, `dayan2026conformal`, `kalogeropoulos2026ensemble` | Searched only at tier S1. Not resolved; do not claim. |
| **WG-C-010** — wildfire decision OSSE | — (no occupant found) | Survives, but **must not** be claimed as "first wildfire decision OSSE" — that is search-failure novelty (§3.2). Claim instead as instantiating the extension to societal impacts that `zeng2020osse` lists as an open recommendation. |

---

## The pattern

Read together, these tell one story: **WildfireGuardian's components are all
occupied, and only one output quantity is not.** Every framing claim — Korean
setting, assisted evacuation, ensembles, uncertainty, inbound responders,
sensing — belongs to someone else. That is not a disaster; it is the normal
condition of a well-populated field, and knowing it precisely is what lets the
one surviving claim be stated sharply instead of defensively.

The program's risk is not that it has too little novelty. It is that it will be
tempted to claim the occupied ground anyway.
