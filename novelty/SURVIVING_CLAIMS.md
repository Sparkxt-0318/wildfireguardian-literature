# SURVIVING_CLAIMS.md

Claims that survived the 2026-09-19 adversarial sweep. **Surviving is not the
same as proven.** Every entry here is `SUPPORTED_CANDIDATE` at best and remains
falsifiable by the watch-list papers in `NOVELTY_THREATS.md` §4.

Per `NOVELTY_STANDARD.md` §5, no claim below reached a full S2 protocol search
(the Korean database sweep and several citation traversals are incomplete), so
**strictly these are `UNKNOWN`-with-evidence rather than confirmed survivors.**
They are listed as candidates because the adversarial search that *should* have
killed them did not.

---

## S1 — The dispatch-by deadline (from WG-C-003)

> **For a resident who cannot self-evacuate, we compute and report the latest
> fire-relative time at which a responder may depart its base such that
> ingress, pickup dwell and egress all complete ahead of modelled fire arrival
> on their respective legs — and we report how that time moves with forecast
> skill, lead time and latency.**

**Status:** `SUPPORTED_CANDIDATE`, narrowly.

**Why it survives.** The novelty matrix has one empty column out of nineteen:
`dispatch-by deadline` (0 papers do it, 2 partially). Everything around it is
occupied — inbound responders, pickup, fire-derived time windows, supported
evacuation — but no occupying prior art *reporting the deadline as its output*
was identified in the searched corpus. The
literal phrases "latest dispatch time" and "latest safe departure time"
returned zero academic hits.

**What it is NOT.** Not the first model of assisted evacuation. Not the first
inbound responder. Not the first fire-derived time window. Every one of those
is occupied and must be conceded before this claim is stated.

**How it dies.** `beyki2026modular` full text reporting a latest-extraction
time; or the `moradi2026supported` journal version adding spread-derived
windows; or `tang2025transit` turning out to report a departure deadline.

**The honesty condition.** This margin is uncomfortably close to the
conjunction novelty forbidden by `NOVELTY_STANDARD.md` §3.1. It is admissible
**only** if WildfireGuardian demonstrates a case where the *deadline* and the
*routing plan* give different operational answers — i.e. where knowing the
deadline changes what a commander does relative to having a plan. If we cannot
show that, this claim must be abandoned for the narrower S2 below.

---

## S2 — The sensitivity surface (fallback if S1 fails)

> **We characterise how the latest-feasible-dispatch time degrades as a
> function of forecast skill, lead time and observation latency, for a fixed
> assisted-evacuation mission structure.**

**Status:** `SUPPORTED_CANDIDATE`.

This survives independently of S1 because no occupying prior art reporting a
*deadline* as the dependent variable in a forecast-quality sensitivity study —
wildfire or otherwise — was identified in the searched corpus. It is a smaller claim and it is more robust. If S1 dies,
this is the retreat position, and it should be prepared now rather than
improvised at the fair.

---

## S3 — Latency charged against the decision budget, in Korea

> **Korea's operational 5-hour evacuation-order threshold is set against a
> gust-driven spread process using fire information that is already 13–320
> minutes old; charging observation latency against that budget leaves an
> effective lead time of roughly 2.7–4.7 hours, and we show whether an assisted
> round trip fits inside what remains.**

**Status:** `SUPPORTED_CANDIDATE` as an *analysis*, `UNKNOWN` as a result.

**Why it survives.** Three verified Korean numbers make this arithmetic
possible — the MOIS 5 h/8 h rule (`mois2025evacuationstages`), the observation
latency gap of 12.9–18.2 min geostationary vs 210–318 min polar-orbiting
(`sung2025geostationary`), and gust-driven spread (`park2025drivers`) — and
**no one has done the arithmetic.**

**Why it is weaker than it looks.** This is an argument, not a result, until
the round-trip durations are computed. And it satisfies
`NOVELTY_STANDARD.md` §4(a) only if the Korean numbers **change the answer**
relative to published settings, which we have not yet shown.

---

## S4 — Methodological compliance (defensive only)

> **We evaluate against a tuned trigger/buffer comparator, on a non-identical-
> twin OSSE, with event-level inference and equivalence testing.**

**Status:** `SUPPORTED_CANDIDATE` as practice; **not a novelty claim**.

`li2018coupling` already supplies percentile-indexed trigger buffers, so the
tuned comparator is available rather than invented. `ronchi2023verification`
supplies the WUI evacuation verification standard. `yu2019twin` establishes
that identical-twin designs bias impact estimates. Our contribution here is
*compliance*, and it should be described that way — its function is to protect
S1–S3 from the "you beat a strawman" and "your uncertainty is self-generated"
objections, not to be a contribution in itself.

---

## What is NOT here, and why that matters

WG-C-001, WG-C-004, WG-C-005, WG-C-011 and WG-C-013 are absent because they are
dead. WG-C-002, WG-C-006, WG-C-007, WG-C-008, WG-C-012 and WG-C-014 are absent
because they survive only in narrowed forms that are already folded into
S1–S4. See `ABANDONED_CLAIMS.md` for the full list and the reason each fell.
