# SEARCH_PROTOCOL.md

How literature search is conducted here, and the log of what was actually run.

**Honesty rule:** we do not describe a search as exhaustive unless it actually
followed the exhaustive protocol below and the query log proves it. A search
that stopped when it found a satisfying answer is a *convenience search* and
must be labeled as one.

---

## §1. Search tiers

| Tier | Name | Requirement | Supports claim status up to |
|---|---|---|---|
| **S0** | Convenience | Any ad-hoc query | `UNKNOWN` only |
| **S1** | Structured | ≥4 wording variants on ≥2 databases, logged | `WEAKENED` / `OCCUPIED` findings valid; cannot support novelty |
| **S2** | Protocol | S1 + backward citation chase + forward citing-paper chase + ≥1 preprint server + ≥1 adjacent field + ≥1 non-English pass, all logged | `SUPPORTED_CANDIDATE` |
| **S3** | Exhaustive | S2 + systematic-review-style database coverage with recorded inclusion/exclusion counts (PRISMA-style) | `SUPPORTED_CANDIDATE` with high confidence |

Any paper found at any tier can *kill* a claim. The tier only limits how much
support a *null* result may confer. This asymmetry is deliberate.

---

## §2. Required query dimensions

For each research question, search across all six:

1. **Exact phrasing** — the term as we would write it
   (e.g. "evacuation trigger buffer")
2. **Synonyms / community variants** — other fields' names for the same thing
   (trigger boundary, trigger point, set-back distance, protective action
   decision point, warning threshold)
3. **Broader terms** — the parent concept (evacuation timing, protective action
   decision-making)
4. **Adjacent disciplines** — operations research, transportation science,
   emergency management, decision analysis, meteorology, robotics
5. **Recent citing literature** — who cites the anchor papers, last 24 months
6. **Preprints and non-English** — arXiv, EarthArXiv, SSRN, Research Square;
   Korean (KCI, ScienceON, RISS), and where relevant Chinese/Japanese/Spanish

---

## §3. Anchor papers for citation chasing

Backward (their references) and forward (who cites them). Anchors are the
papers whose citation neighbourhoods contain our competition.

Anchors are established by the category reviews in `literature/reviews/` and
are listed there. Anchors must themselves be verified before being used as
chase seeds — an unverified anchor propagates error through the whole chase.

---

## §4. Stop rules

Stop a search line when **either**:
- (a) three consecutive query variants return no new relevant records
  (saturation), **or**
- (b) a claim-killing paper is found (record it and stop; further search on
  that line is wasted effort).

Do not stop merely because you have "enough" papers. Volume is not the goal;
coverage of the *threat space* is.

---

## §5. Anti-redundancy

Do not re-query the same source with the same string. Log every query below so
the next agent can see what was already tried. Repeated identical querying is
both wasteful and creates false confidence in coverage.

---

## §6. Query log

Per-agent logs live in `docs/search-logs/` and are the primary record:

| Log file | Domain |
|---|---|
| `search-logs/agent-trigger-traffic.md` | Cat 1 (trigger modeling), Cat 3 (wildfire + traffic) |
| `search-logs/agent-assisted-vulnerable.md` | Cat 2 (assisted evacuation), Cat 9 (vulnerable populations) |
| `search-logs/agent-forecast-voi.md` | Cat 4 (forecast value), Cat 5 (VOI / active sensing) |
| `search-logs/agent-spread-observations.md` | Cat 6 (fire spread models), Cat 7 (observations) |
| `search-logs/agent-korea.md` | Cat 8 (Korea-specific) |
| `search-logs/agent-evaluation.md` | Cat 10 (evaluation methodology) |

Each entry records: date, source searched, exact query string, number of hits,
number of usable hits, and what it changed.

### Tier attained per category

Updated after each search round. See `novelty/CURRENT_NOVELTY_VERDICT.md` for
how this constrains the verdict.

| Category | Tier attained | Notes |
|---|---|---|
| 1 Trigger modeling | **S1→S2 (incomplete)** | Backward refs of `cova2005trigger` never traversed (publisher 403); forward chain of `li2018coupling` returned empty and was not retried |
| 2 Assisted evacuation | **S2** | 37 queries, 5 sources, Korean pass, preprint sweep. Closest to a full protocol search of any category |
| 3 Wildfire + traffic | **S1→S2 (incomplete)** | No Greek/Portuguese/Spanish pass despite three relevant national literatures |
| 4 Forecast value | **S2** | 37 queries; Korean pass run; Consensus quota exhausted at 6 |
| 5 VOI / active sensing | **S1 (incomplete)** | Peer-reviewed sweep incomplete; hard-deadline POMDP/sensor-scheduling variants searched only shallowly |
| 6 Fire spread models | **S1→S2** | Consensus quota exhausted after 4 queries; no Korean-language pass |
| 7 Observations | **S1→S2** | GK2A *product* latency and MTG-FCI specs unresolved |
| 8 Korea-specific | **S1 (blocked)** | 49 queries, Korean recorded in Korean, **but KCI/RISS/DBpia keyword sweep could not be completed** (server-side search undrivable, DBpia 503). Largest blind spot in the corpus |
| 9 Vulnerable populations | **S2** | Covered jointly with category 2 |
| 10 Evaluation methodology | **S2** | 53 queries over 8 rounds; no non-English pass |

**Consequence.** No category reached S3, and categories 5 and 8 did not reach
S2. Under §1, that caps every positive novelty finding at
`SUPPORTED_CANDIDATE`, and means **no Korean claim may be described as
searched** until the KCI/RISS/DBpia sweep is completed.
