# Search log — Lead researcher (cross-cutting claims + verification audit)

Role: Agent C (verification) and Agent A for the two claims that fell between
the category agents' assignments — WG-C-009 (robust protectability) and
WG-C-013 (intervention ranking).

Tier attained: **S1 (structured)** for WG-C-009 and WG-C-013. Not S2 — no
backward/forward citation chase or non-English pass was run on these two
lines. They therefore cannot support a novelty claim, only record occupancy.

---

## Queries run

| Date | Source | Query | Hits | Usable | Effect |
|---|---|---|---|---|---|
| 2026-09-19 | Web search | `Cova Dennison Kim Moritz 2005 "Setting wildfire evacuation trigger points" fire spread modeling` | 10 | 4 | Anchor verification; surfaced Chang 2026 Risk Analysis lead |
| 2026-09-19 | Web search | `k-PERIL evacuation trigger boundary wildfire ensemble Mitsopoulos` | 9 | 6 | Anchor verification; PERIL/k-PERIL lineage confirmed |
| 2026-09-19 | Web search | `wildfire "defensible space" structure survival protectability under model uncertainty robust decision making` | 9 | 1 | Mostly practitioner guidance; academic robust-protectability framing not found |
| 2026-09-19 | Web search | `robust optimization evacuation planning uncertain hazard "robust" protective action worst-case wildfire` | 9 | 5 | **Surfaced kwon2025koreaevac (HIGH threat to WG-C-007)** |
| 2026-09-19 | Web search | `"prioritizing emergency evacuations" compounding uncertainty ranking which communities evacuate first wildfire` | 9 | 0 | Returned practitioner material only; academic lead arXiv 2210.08975 carried over from prior query, NOT yet verified |
| 2026-09-19 | Web search | `wildfire suppression resource allocation "intervention" ranking marginal value simulation decision support 2025` | 9 | 4 | Surfaced MORA, Mendes & Alvelos, Rodriguez-Fernandez MCDA |
| 2026-09-19 | Crossref API | DOI resolution: `10.1111/j.1467-9671.2005.00237.x` | 1 | 1 | Cova 2005 confirmed: Transactions in GIS 9(4):603-617 |
| 2026-09-19 | Crossref API | DOI resolution: `10.3390/systems13121125` | 1 | 1 | Kwon et al. confirmed; abstract retrieved |
| 2026-09-19 | Crossref API | DOI resolution: `10.3390/a18110677`, `10.1111/itor.13524`, `10.3389/ffgc.2025.1654107` | 3 | 3 | All confirmed; **year correction caught** (see below) |
| 2026-09-19 | arXiv (WebFetch) | `arxiv.org/abs/2608.05413` | 1 | 1 | Independent verification of the CRITICAL threat found by the assisted-evacuation agent |

---

## Metadata corrections caught by verification

1. **mendes2024robustsuppression** — secondary sources (search result listings)
   presented this as a 2025 paper. Crossref gives issued 2024-08-05, volume
   32(3), pages 1312–1342. Recorded as **2024**. This is precisely the
   single-secondary-source error `CITATION_RULES.md` forbids.
2. **moradi2026supported** — arXiv abstract page gives submission date
   2026-08-05; the PDF title page reportedly carries "Preprint submitted to
   Elsevier August 8, 2025". Both recorded; **priority date is the earlier
   disclosure** and must be resolved at full text (`NEEDS_FULL_TEXT`).

---

## Independent verification of the CRITICAL threat

`moradi2026supported` was found by the assisted-evacuation agent. Per
`CITATION_RULES.md` ("never trust metadata from a single secondary source"),
the lead independently fetched the arXiv abstract page. Confirmed:

- Title and three-author list match exactly.
- Problem: two-stage stochastic optimization of **facility location, fleet
  sizing, and vehicle routing under strict time windows** for supported
  evacuation of vulnerable populations (hospital patients, long-term care
  residents) in wildfires.
- The abstract does **not** report a latest-feasible-dispatch-time.
- Fire enters through time windows rather than a dynamically coupled spread
  model, per the abstract.

The agent's differentiation therefore holds **on abstract evidence (E2)**.
Because this is the paper most likely to end RQ2, E2 is not sufficient:
promoted to `NEEDS_FULL_TEXT` and Tier 1 of the binder.

---

## Unverified leads carried forward (RECALL/LEAD, not citations)

- `arXiv 2210.08975` — "Prioritizing emergency evacuations under compounding
  levels of uncertainty". Relevant to WG-C-011/WG-C-013. **Not verified.**
- Chang et al. 2026, *Risk Analysis*, "Multiscale Wildfire-Evacuation
  Modeling: Assessing Differential Access to Safe Egress in Marin County, CA".
  Differential access is close to WG-C-005/WG-C-009. **Not verified.**
- `arXiv 2603.29865` — "Wildfire Suppression: Complexity, Models, and
  Instances". **Not verified.**
- Wei et al., "A spatial optimization model for resource allocation for
  wildfire suppression and resident evacuation". **Not verified.**
