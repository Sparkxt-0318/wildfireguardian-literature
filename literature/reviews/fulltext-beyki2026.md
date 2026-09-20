# Full-text extraction — `beyki2026modular` — **ATTEMPTED AND FAILED**

**Agent:** C — Verification Auditor
**Date:** 2026-09-20
**Target:** Beyki, S. M., Patricio, A. S., Gameiro Lopes, A., Santiago, A., & Laím, L. (2026).
"A modular agent-based framework for wildfire evacuation: Integrating fire spread, multimodal
transport, and dynamic routing." *Safety Science* **199**, 107200.
DOI `10.1016/j.ssci.2026.107200`.
**Scope:** full-text read, not a search. No new papers were added to the corpus.

> ## ⚠ HEADLINE: THE FULL TEXT WAS NOT OBTAINED.
>
> This document records a **failed retrieval**, an audit of what *is* verifiable without the
> body text, and an explicit list of what remains unread. It contains **no statement about the
> paper's methods, equations, or results**, because none could be read.
>
> `beyki2026modular` remains the **highest-priority unread item in the repository**. Its
> `NEEDS_FULL_TEXT` status is unchanged. Nothing in this document licenses moving WG-C-003 in
> either direction.

---

## 0. Retrieval outcome and evidence level

| Field | Value |
|---|---|
| `fulltext_status` | **`ABSTRACT_VERIFIED`** — publisher-deposited abstract and highlights retrieved and corroborated; **article body never retrieved** |
| `evidence_level` (content) | **E2** — abstract read. Per `docs/EVIDENCE_LEVELS.md`, E2 **may not** support any statement about method details or results |
| `evidence_level` (bibliographic metadata) | **E4-equivalent** — title, authors, affiliations, volume, article number, cover date, licence and reference list located in three independent primary records |
| `access_route` | **No successful route to the body.** Publisher-deposited metadata via Crossref API, Unpaywall API, OpenAlex API and the Elsevier Article-Retrieval API (`coredata` view, no key) |
| HTML full text | **Not obtainable.** ScienceDirect is the sole host and denies this network |
| PDF full text | **Not obtainable.** Same host, same denial |

### Why this is a network-level denial, not a captcha I failed to solve

Two distinct fetch surfaces were used against ScienceDirect: `curl` (HTTP/1.1 and HTTP/2, full
browser header sets, several user agents, `Referer: google.com`, `Sec-Fetch-*` headers) and a real
headless Chromium 127 via Playwright. Both returned **HTTP 403**. The browser-rendered body text
was, in full:

```
There was a problem providing the content you requested
Please contact our support team for more information and provide the details below.
Reference number: a3dd76b36884c9b9
IP Address: 160.79.106.136
Timestamp: 2026-09-20 02:40:08 UTC
CPE00001
```

The same block appeared on **SSRN** (also an Elsevier property), with the wording made explicit:

```
Content Blocked
We have detected that you may be using an automated script or search engine our site does not
support. Please retry using an alternate way of accessing our site.
Contact Content_Protection_Services@Elsevier.com for more information.
Reference Number: a3dd79613f2539c0   IP Address: 160.79.106.129
```

Elsevier additionally asserts a text-and-data-mining reservation on the article page
(`<meta name="tdm-reservation" content="1">`, `tdm-policy → elsevier.com/tdm/tdmrep-policy.json`)
and in its footer: *"All rights are reserved, including those for text and data mining, AI
training, and similar technologies. For all open access content, the relevant licensing terms
apply."*

**This is an Elsevier-side block on this IP range, not a solvable challenge.** The article is
genuinely CC-BY; the obstacle is access control on the only host that serves it, not the licence.

### Full log of access routes attempted

| # | Route | Result |
|---|---|---|
| 1 | `https://doi.org/10.1016/j.ssci.2026.107200` | HTTP 302 → `linkinghub.elsevier.com/retrieve/pii/S0925753526000913` |
| 2 | `linkinghub.elsevier.com/retrieve/pii/S0925753526000913` | HTTP 200, 2.7 KB meta-refresh stub → ScienceDirect |
| 3 | ScienceDirect article page, `curl` + browser headers | HTTP 403, 1.2 MB bot-challenge page |
| 4 | ScienceDirect article page, `curl --http2` + full `Sec-Fetch-*` set + Google referer | HTTP 403 |
| 5 | ScienceDirect `/pdfft?isDTMRedir=true&download=true` | HTTP 403 |
| 6 | ScienceDirect `/sdfe/reader/pii/…` | HTTP 403 |
| 7 | ScienceDirect `/science/article/am/pii/…` (accepted manuscript path) | HTTP 403 |
| 8 | ScienceDirect via headless Chromium 127 (Playwright, real TLS fingerprint) | HTTP 403, `CPE00001` |
| 9 | Elsevier Article-Retrieval API, default view, no key | **HTTP 200 — `coredata` only, no body** |
| 10 | Elsevier Article-Retrieval API, `view=FULL` | HTTP 401 `AUTHENTICATION_ERROR / Invalid API Key` |
| 11 | Crossref-advertised TDM links (`api.elsevier.com/content/article/PII:…`, `text/xml` and `text/plain`) | HTTP 401 `APIKEY_INVALID` |
| 12 | Unpaywall | `is_oa: true`, `oa_status: hybrid`, **`has_repository_copy: false`**, sole OA location = the DOI itself |
| 13 | OpenAlex | `best_oa_location.pdf_url: null`, `any_repository_has_fulltext: false` |
| 14 | Semantic Scholar Graph API | `openAccessPdf.url` = the DOI landing page; no hosted PDF |
| 15 | Europe PMC | **0 hits** (Safety Science is not PMC-deposited) |
| 16 | CORE API | no record |
| 17 | OpenAIRE | 1 record, Crossref-collected, **no repository instance** |
| 18 | BASE | no result |
| 19 | Universidade de Coimbra "Estudo Geral" (DSpace REST + discover API) | no deposit of this article found |
| 20 | ResearchGate search | HTTP 403 captcha |
| 21 | SSRN (via citing preprint's PDF link, and landing page via Playwright) | HTTP 403, Elsevier `Content Blocked` |
| 22 | `r.jina.ai` text renderer against ScienceDirect | HTTP 200 relaying the ScienceDirect captcha page — **no content** |
| 23 | Internet Archive Wayback (`web.archive.org` CDX) | **"Blocked by egress policy"** — reported, not routed around, per `/root/.ccr/README.md` |
| 24 | `api.fatcat.wiki` (scholar.archive.org) | connection reset (host appears unreachable from this network) |
| 25 | Authors' project site `evacuarfloresta.enb.pt` (hosts their other PDFs) | site's media library ends **2025-07-28**; the 2026 article is not there |

Route 25 is worth recording because it nearly worked: the EVACUARFLORESTA project site openly
hosts this group's other papers as publisher PDFs. It simply has not been updated since the 2026
article appeared. **If the site is updated, the full text becomes freely retrievable there.** This
is the cheapest future route and should be re-checked.

---

## 1. Metadata audit (this part is complete and passes)

Corroborated across **three independent primary records** — Crossref, Unpaywall, and Elsevier's
own Article-Retrieval API — satisfying `docs/EVIDENCE_LEVELS.md` Rule 4.

| Field | Verified value | Sources agreeing |
|---|---|---|
| Title | "A modular agent-based framework for wildfire evacuation: Integrating fire spread, multimodal transport, and dynamic routing" | Crossref, Unpaywall, Elsevier API, OpenAlex |
| Journal | *Safety Science* (ISSN 0925-7535 / 1879-1042) | all |
| Volume / article number / page | **199 / 107200 / 107200** | Crossref, Elsevier API |
| Issue | none (article-number journal) | Crossref |
| Type | `journal-article` | Crossref |
| PII | `S0925-7535(26)00091-3`; EID `1-s2.0-S0925753526000913` | Elsevier API |
| Online (OA) date | **2026-03-21** | Unpaywall |
| Cover / issue date | **July 2026** (`prism:coverDate 2026-07-31`; Crossref `issued 2026-07`) | Elsevier API, Crossref |
| Licence | **CC-BY 4.0**, `openaccessType: Full` | Elsevier API, Unpaywall, OpenAlex |
| OA funding | `openaccessSponsorName: "Portugal institutions: Core Hybrid journals RAP 2025"`, `openaccessSponsorType: ElsevierWaived` | Elsevier API |
| Reference count | **43** | Crossref |
| DOI | `10.1016/j.ssci.2026.107200` — **VERIFIED, not invented** | all |

### Author list and affiliations — one correction to the repository

| # | Name | Affiliation (Unpaywall raw strings) |
|---|---|---|
| 1 | **Shahab Mohammad Beyki** (corresponding) | University of Coimbra, Dept. of Mechanical Engineering |
| 2 | **Anne S. Patricio** | **MaaSLab, 78 Spyrou Kyprianou, Limassol 4043, Cyprus** |
| 3 | **António Gameiro Lopes** | University of Coimbra, Dept. of Mechanical Engineering (Pólo II) |
| 4 | **Aldina Santiago** | University of Coimbra, Dept. of Civil Engineering |
| 5 | **Luís Laím** | University of Coimbra, Dept. of Civil Engineering |

**Correction:** the task brief and prior notes treat the author team as uniformly
Coimbra-affiliated. Four of five are; the **second author is at MaaSLab, Cyprus** — a mobility-
as-a-service transport lab. This is a small but real correction, and it explains the paper's
multimodal-transport component. It is also why searching Coimbra's repository alone was never
going to be sufficient.

The existing note renders author 1 as "Beyki, S. M." and author 2 as "Patricio, A. S." — both
consistent with the deposited records. The surname string is **"Laím"** (with acute í) in Unpaywall
and Crossref; the YAML currently stores the unaccented "Luis Laim", which is acceptable as an
ASCII-folded form but should not be presented as the authoritative spelling.

---

## 2. What content *was* verified (E2 ceiling)

The publisher-deposited abstract, including the five highlight bullets, was retrieved from the
**OpenAlex `abstract_inverted_index`** (reconstructed to linear text) and is reproduced here in the
short-quote form `AGENTS.md` §8 permits. It is **identical in substance** to the abstract already
recorded in `literature/notes/beyki2026modular.md`, which is independent corroboration that the
existing note's abstract-level content is accurate.

**Highlights (publisher-deposited, verbatim, ≤25-word fragments):**

- "Fire-driven road-segment closures dynamically update network availability during the evacuation."
- "A custom waypoint-based routing algorithm enables adaptive rerouting for outbound and inbound evacuation."
- "Pedestrian movement, private vehicle, emergency extraction, and vehicle–pedestrian interactions are explicitly represented."
- "The model was applied to a WUI and validated against an evacuation drill to assess realism and operational consistency."

**Abstract, gap statement (verbatim fragment):**

- "…limited dynamic rerouting when roads are compromised, insufficient representation of multimodal evacuation, weak integration of high-resolution fire spread data, and the lack of inbound traffic and rescue operations."

**Abstract, contribution (verbatim fragments):**

- "It supports dynamic routing responsive to advancing fires, enables both outbound self-evacuation and inbound rescue operations, and incorporates multimodal transportation modes."
- "The model was tested in a case study in Portugal and validated against an evacuation drill, showing strong agreement in evacuation times…"

**Abstract, stated outputs (verbatim fragment):**

- "It improves evacuation planning by allowing scenario testing, 'what-if' analyses, and data-driven decision-making to enhance community safety and resilience."

That is the entirety of the verified content. **There is no section numbering, no page-numbered
evidence, no equation, and no result available below this line**, because the body was never read.

---

## 3. ⚠ AUDIT FINDING: an unsourced mechanism quote in the existing note

The existing note `literature/notes/beyki2026modular.md` contains this passage:

> "A secondary search result (WebSearch, not the paper itself) described a mechanism of
> 'determining safe time remaining for evacuation routes based on fire arrival time for each
> waypoint on the route, where the safe time remaining is the least of the fire arrival times.'"

**I attempted to trace this phrasing to a primary source and could not.**

- It does **not** appear in the publisher-deposited abstract or highlights (full text of both
  reconstructed and checked).
- It does **not** appear in any retrievable record of the article (Crossref, Unpaywall, OpenAlex,
  Semantic Scholar, Elsevier `coredata`).
- A targeted WebSearch reproduced **the same description again**, in the same
  search-engine-summary form — i.e. a second helping of the same class of source, not a second
  source.

**Status: `RECALL_UNVERIFIED` / unsourced.** Per `AGENTS.md` §3 and the Agent-C hard limit
("never trust a single secondary source"), this must not be cited, quoted, or relied upon, and it
must not be described as something "the paper says."

**Why it nevertheless matters, and why it is the single highest-value thing to check on the next
retrieval attempt:** if the paper really does compute, per route, a *safe time remaining* equal to
`min` over waypoints of fire arrival time, then the framework contains a per-route **time margin**
quantity — which is materially closer to WG-DBD-2 than the abstract implies. Note carefully what
it would and would not be:

- It **would** be a fire-relative feasibility margin for a route (bears on WG-DBD-2).
- It **would** be a min-over-waypoints rule, i.e. a **single scalar deadline per route** — which is
  precisely the *monotone, single-deadline* structure that WG-DBD-4 says WildfireGuardian must go
  beyond. A `min` rule cannot express a non-monotone feasible set.
- It **would not** be a dispatch instant for an inbound responder (WG-DBD-3), and it would be
  evaluated at routing time against waypoint arrival times, which says nothing on its own about
  full-traversal-interval hazard (WG-DBD-5).

So even in the worst case, the unverified mechanism threatens WG-DBD-2 and possibly WG-DBD-5,
**strengthens** the WG-DBD-4 differentiation, and leaves WG-DBD-3 untouched. But none of that is
evidence yet. It is a hypothesis to test.

---

## 4. Reference list — retrieved in full (43 items, Crossref, publisher-deposited)

This is the one piece of body-adjacent evidence that *is* primary and complete. It is
publisher-deposited, not scraped or summarised.

**The paper cites the trigger literature:** Cova (2002, *Environ. Plan. A*, microsimulation of
neighborhood evacuations); Cova (2013, *GeoJournal*, mapping wildfire evacuation vulnerability);
Dennison (2007, *Nat. Hazards*, **WUIVAC**); Li (2019, *Fire Technol.*, "Setting wildfire evacuation
triggers by coupling fire and traffic simulation models" — this is the repository's
`li2018coupling`); Mitchell (2023, *Safety Sci.*, "Integrating wildfire spread and evacuation times
to design safe triggers: Application to two rural communities using **PERIL** model").

**It cites the evacuation-simulation platforms:** Ronchi (2019, *Saf. Sci.*, e-Sanctuary open
multi-physics framework) and the 2017 e-Sanctuary report; Wahlqvist (2021, *Saf. Sci.*,
**WUI-NITY**); Veeraswamy (2018, *Saf. Sci.*, Swinley forest fire); Beloglazov (2016); Siam (2022,
*TR-D*); Grajdura (2022, *TR-D*); Gwynne (2019, *Fire Mater.*); Intini (2019); Wolshon (2007).

**It cites the authors' own fire-modelling lineage:** Lopes (1995, *Numer. Heat Transf. A*);
Lopes (2002, *Environ. Model. Software*, **FireStation**); Ross (1988, diagnostic wind field);
Rothermel (1972); Beyki (2023, *Appl. Sci.*), Beyki (2025, *Remote Sens. Appl.*), Beyki (2025,
*IJDRR*).

**What is conspicuously absent from all 43 references:**

- **No vehicle-routing, pickup-and-delivery, PDPTW, fleet-sizing or dispatch-optimisation paper.**
  No Shahparvari, no Moradi, no Kamyabniya, no supported/assisted-evacuation optimisation work of
  any kind.
- **No operations-research or scheduling literature at all.**
- No forecast-value, forecast-skill, ensemble or uncertainty-quantification reference.
- No paper whose title contains "deadline", "time window", "dispatch", or "departure time".

**How much weight this carries.** This is *inferential* evidence, and it is being labelled as such.
A 43-item reference list containing zero routing-optimisation or scheduling citations is a strong
indication that the paper does **not** formulate a dispatch-time optimisation and does **not**
report a latest-dispatch quantity as a contribution — a paper that computed a dispatch deadline
would be expected to situate itself against that literature, and Elsevier reviewers at *Safety
Science* would be expected to require it. But **absence of a citation is not absence of a
mechanism**, and under `docs/NOVELTY_STANDARD.md` §3.2 this is the shape of a search-failure
argument. **It may not be used to move a claim.** It is recorded as a prior on what the full text
will say, nothing more.

---

## 5. Q-B1 … Q-B6 — the six questions

Each answer is the honest one. The permitted vocabulary was YES / NO / NOT_ADDRESSED_IN_TEXT;
**none of those three is available to me**, because "NOT_ADDRESSED_IN_TEXT" is itself a claim about
the text, and I have not read the text. `AGENTS.md` §9 requires `UNKNOWN` in exactly this
situation.

| ID | Question | Answer | Basis |
|---|---|---|---|
| **Q-B1** | Computes/outputs a **latest feasible start time** for an inbound responder's complete extraction mission? | **`NOT_DETERMINED — NO FULL TEXT`** | Not among the outputs the abstract lists ("scenario testing, 'what-if' analyses"). No routing/scheduling references in 43. Neither fact is textual evidence about the body. |
| **Q-B2** | Evaluates `base → resident → pickup → destination` as ONE fire-relative mission? | **`NOT_DETERMINED — NO FULL TEXT`** | Abstract asserts "inbound rescue operations" and "emergency extraction" agents exist; whether one mission is chained end-to-end with a pickup dwell is a method detail E2 cannot support. |
| **Q-B3** | Produces a dispatch-feasible set/window or equivalent? | **`NOT_DETERMINED — NO FULL TEXT`** | Nothing in abstract/highlights. The unsourced "safe time remaining" lead (§3) would bear on this if verified. |
| **Q-B4** | Hazard over the **full traversal interval**, or only at route/edge decision times? | **`NOT_DETERMINED — NO FULL TEXT`** | "Fire-driven road-segment closures dynamically update network availability during the evacuation" establishes that network state is time-varying; it does **not** establish whether an agent already on an edge is re-checked against fire arrival mid-traversal. That distinction is exactly the question and is invisible at E2. |
| **Q-B5** | Models **non-monotone feasibility / reopening**? | **`NOT_DETERMINED — NO FULL TEXT`** | No indication either way. The word "closures" hints at one-way state transitions but cannot be read as evidence. |
| **Q-B6** | Is "latest extraction time" an **explicit scientific output**, or merely implicit in the machinery? | **`NOT_DETERMINED — NO FULL TEXT`** | The abstract's stated outputs are evacuation times, drill agreement, and scenario analysis. That is suggestive of "not an explicit output" but is not a reading of the body. |

**Exact passages requested on: inbound emergency responders; emergency extraction; responder
routing; pickup; egress; dynamic rerouting; fire-driven road closure; departure time; dispatch
time; latest feasible extraction; deadlines; time windows.**

Available at abstract level only, and only for four of the twelve:

| Topic | Passage available? | Verbatim fragment (abstract/highlights) |
|---|---|---|
| inbound emergency responders | partial | "enables both outbound self-evacuation and **inbound rescue operations**" |
| emergency extraction | partial | "Pedestrian movement, private vehicle, **emergency extraction**, and vehicle–pedestrian interactions are explicitly represented" |
| responder routing | partial | "custom waypoint-based routing algorithm enables adaptive rerouting for outbound and **inbound** evacuation" |
| dynamic rerouting | partial | "limited **dynamic rerouting** when roads are compromised" (gap statement); "adaptive rerouting" (highlight) |
| fire-driven road closure | partial | "**Fire-driven road-segment closures** dynamically update network availability during the evacuation" |
| pickup | **none** | — |
| egress | **none** (beyond "outbound self-evacuation") | — |
| departure time | **none** | — |
| dispatch time | **none** | — |
| latest feasible extraction | **none** | — |
| deadlines | **none** | — |
| time windows | **none** | — |

The eight empty rows are the reason this read mattered, and they are still empty.

---

## 6. WG-DBD-1 … WG-DBD-7 — decomposed component scoring

Scored **independently**, as instructed. `NOT_DETERMINED` is used where E2 cannot reach, and this is
not a formality: **`docs/EVIDENCE_LEVELS.md` Rule 1 forbids assigning `OCCUPIED` on E2 evidence.**
At this evidence level no component *can* legitimately be scored OCCUPIED by this paper.

| ID | Component | Score | Evidence and reasoning |
|---|---|---|---|
| **WG-DBD-1** | Complete assisted mission contains responder ingress + service + egress | **`PARTIALLY_OCCUPIED`** (provisional, E2) | Ingress and the existence of an extraction agent class are asserted **by the authors themselves** in the deposited abstract/highlights: "inbound rescue operations"; "emergency extraction … explicitly represented". These are topic-level statements, which E2 does support. **The `service` element (pickup/loading dwell) is wholly unevidenced**, and nothing establishes that ingress, service and egress are chained into one accounted mission rather than being three separately-simulated behaviours. Hence *partially*, not fully. |
| **WG-DBD-2** | Fire-relative feasible dispatch times are computed | **`NOT_DETERMINED`** | Nothing at E2. The unsourced "safe time remaining = min over waypoints of fire arrival time" lead (§3) would, if verified, push this toward PARTIALLY_OCCUPIED — for *routes*, not for *dispatch instants*. Unverified; carries no weight. |
| **WG-DBD-3** | Latest feasible dispatch instant reported as an operational quantity | **`NOT_DETERMINED`** | The decisive question, and the one I could not answer. Weak negative indicators only: not among the abstract's listed outputs; zero scheduling/routing references in a 43-item list. Neither is admissible to score it. |
| **WG-DBD-4** | Non-monotone feasible dispatch windows represented as a **set** rather than a single deadline | **`NOT_DETERMINED`** | No evidence either way. Recorded explicitly: **WG-DBD-1 being partially occupied does not touch this.** A framework that simulates an inbound rescue leg need not represent feasibility as anything at all, let alone as a non-singleton set. If the "safe time remaining" lead is confirmed, its `min` structure is a *single scalar per route* and would count **against** this component being occupied. |
| **WG-DBD-5** | Full traversal-interval hazard is evaluated | **`NOT_DETERMINED`** | "Fire-driven road-segment closures dynamically update network availability" shows the *network* is time-varying. Whether hazard is integrated over an agent's traversal of an edge, or only sampled when the edge is chosen, is unreadable at E2 and is precisely Q-B4. |
| **WG-DBD-6** | Dispatch feasibility conditioned on information available at decision time rather than oracle future knowledge | **`NOT_DETERMINED`** | Unreadable at E2. Worth flagging for the next attempt: the paper couples a high-resolution fire model to the evacuation run, and a coupled simulator can trivially hand the router the *true* future fire. Whether the authors gate the router's information is a first-order question for WildfireGuardian and is not addressed in any retrievable material. |
| **WG-DBD-7** | Dispatch-by maps applied to Korean rural wildfire geometry | **`NOT_OCCUPIED`** — **confirmed** | E2 is sufficient for this one, since it is a topic-level fact about the case study, not a method detail. Abstract: "The model was tested in a **case study in Portugal**." All four Coimbra-affiliated authors are Portuguese-institution based; the fifth is in Cyprus. Korea appears nowhere in the record. Confirmed as expected. |

---

## 7. Does this paper kill the dispatch-by-deadline claim?

**Cannot determine — without the article body, which Elsevier does not serve to this network.**

The state of the question is unchanged from 2026-09-19. What this audit adds is:

1. The metadata is clean, the DOI is real, the CC-BY status is real, and the paper is exactly what
   the registry says it is.
2. The abstract-level content in the existing note is **corroborated** by an independent
   publisher-deposited record.
3. One quoted "mechanism" in the existing note is **unsourced** and must be demoted (§3).
4. The 43-item reference list is now held at primary-source quality and contains **no routing,
   scheduling, or dispatch-optimisation work whatsoever** — a real but strictly *inferential*
   prior, usable for prioritisation and not for scoring.

---

## 8. ⚠ Second audit finding: an E2-backed `OCCUPIED` in `NOVELTY_THREATS.md`

Out of scope to edit, reported as required by the Agent-C role.

`novelty/NOVELTY_THREATS.md` §2, table for WG-C-003, contains:

> | Inbound responder simulated with outbound evacuation | `beyki2026modular`, `averill2007emergencyresponse` | **Occupied — this sentence must be struck from our claim** |

`beyki2026modular` is at **E2**. `docs/EVIDENCE_LEVELS.md` Rule 1 states that a status change to
`OCCUPIED` requires **E3 minimum**. That row therefore cannot rest on this paper.

This is a bookkeeping defect, **not** a reason to reclaim the territory: the row also cites
`averill2007emergencyresponse` (NIST IR 7425, 2007), and if that record is held at E3 the
occupation stands on it alone. The recommended fix is to reorder the row so the E3+ source is
load-bearing and `beyki2026modular` is listed as corroborating-pending-full-text. **The forbidden
sentence "No one models responders moving inbound against evacuees" should remain forbidden
either way** — the authors' own abstract says they do it, and a fair judge would not care about our
internal evidence grading when the abstract is on screen.

---

## 9. What I could not read — the explicit list

Everything below was sought and not obtained:

- The entire article body: all sections, all figures, all tables, all equations, the reference
  callouts, the limitations section and the conclusions.
- Any section numbering or pagination. **No page- or section-numbered evidence exists in this
  document, and none should be manufactured from it.**
- The definition and agent logic of the **"emergency extraction"** agent class — the single most
  decision-relevant object in the paper for WG-C-003.
- Whether a **pickup / loading dwell** is modelled at all.
- The **waypoint-based routing algorithm**: its objective, its inputs, and whether it consults
  actual or forecast fire arrival times (WG-DBD-6).
- Whether any **"safe time remaining"** quantity exists, and if so its definition (§3).
- The **road-closure rule**: threshold, hysteresis, and whether a closed segment can **reopen**
  (WG-DBD-5, and Q-B5 directly).
- Whether hazard is checked **on entry to an edge** or **across the traversal** (Q-B4).
- The Portuguese case-study site, the drill used for validation, and every reported number.
- The limitations and future-work sections, where authors most often state plainly whether they
  compute a deadline.

---

## 10. Recommended next actions, in cost order

1. **Re-check `evacuarfloresta.enb.pt`** (route 25). The group open-posts its own publisher PDFs;
   the site is simply stale. Cheapest possible route to E3/E4, requires no institutional access.
2. **Email the corresponding author.** Shahab Mohammad Beyki is corresponding and the article is
   **CC-BY** — he is entitled to send it and the licence entitles us to redistribute it internally.
   For a paper this decision-critical, one email outranks any further scraping.
3. **Retrieve via an institutional network** (any university proxy / library link resolver). The
   block is on this IP range, not on the reader.
4. **Watch for a Coimbra "Estudo Geral" deposit.** Portuguese institutions routinely deposit
   post-publication; Unpaywall currently reports `has_repository_copy: false`, so set a re-check.
5. Only after the body is in hand, re-run §5 and §6 and rewrite this file at the achieved level.

Until step 1, 2, 3 or 4 succeeds, `beyki2026modular` stays `NEEDS_FULL_TEXT`, stays **CRITICAL**,
and stays the highest-priority read in the repository.
