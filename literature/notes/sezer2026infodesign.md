# sezer2026infodesign

## Citation
Sezer, F., 2026: *Continuous-Time Information Design for Hurricane Evacuation:
Disclosure, Congestion, and Optimal Phasing under Model Uncertainty.*
arXiv:2606.30320v1 [math.OC], submitted 2026-06-29. Texas A&M University.
**PREPRINT — not peer reviewed. DOI: UNVERIFIED.**

## Publication status
Preprint. Single-source metadata (alphaXiv full-text retrieval and record). No
Crossref record and no journal version located, so nothing here is corroborated
by a second independent source. Evidence level **E3** for the passages read
directly; the abstract's headline percentages are **not** independently checked
and must not be cited.

This paper was already sitting in `docs/search-logs/agent-forecast-voi.md` entry
5.11 as an unfiled **search lead** flagged "relevant to WG-C-002". It is filed
now because its Experiment 2 turns out to occupy an RQ1 component.

## Problem
How much should an emergency management agency tell the public, and when, when
sharper information makes genuine departures *synchronise* and gridlock the
shared corridors?

## Method
Continuous-time Stackelberg game. The agency (leader) chooses two levers:
public-advisory **precision** and a **tiered release schedule**. The latent
storm is a jump-diffusion with an exact finite-dimensional belief filter. Zones
(followers) play a capacity-constrained congestion game on shared corridors with
belief-weighted hazard exposure. Solved via a potential reduction and an Isaacs
equation (distributionally robust, relative-entropy ambiguity).

## Data
Calibrated to Hurricane Rita using NHC archives, TxDOT capacities and HRRC
surveys. Two asymmetric zones sharing the I-45 trunk.

## Outputs
- Staggered release dominates simultaneous advisories; phased evacuation emerges
  endogenously as optimal information design.
- **Experiment 2 is the part that matters here.** Expected social cost is
  plotted **against public-signal precision**, and the sign of the relationship
  flips with the number of tiers:
  > "Under a single common signal (K = 1) cost rises with precision and the
  > optimum is the vague corner … under staggered orders (K = 2) the sign
  > reverses and full precision is optimal." (Fig. 6 caption)
  > "Sequencing and precision are therefore complements: precision is
  > self-defeating as a single broadcast" (§6.4)
- Headline reductions in social cost are stated in the abstract; **recorded but
  not verified, do not cite.**

## Key equations
Isaacs equation / viscosity-solution characterisation; convex congestion
externality coupling beliefs to corridor load. Not extracted in detail.

## Assumptions
Zones are strategic and respond to beliefs; congestion cost is convex; hazard
exposure is belief-weighted; the agency can commit to a signalling channel.

## Validation
Calibration reproduces the observed I-45 gridlock in Rita. Not validated against
counterfactual outcomes.

## WildfireGuardian overlap
Narrow but real, and it lands squarely on **WG-FV-1** and **WG-FV-5**:

- An **information-quality parameter is swept in a controlled experiment** and
  the outcome plotted is **decision loss** (expected social cost), for an
  evacuation, against a hazard deadline ("evacuation routes flood at a surge
  deadline"). That is the shape of the RQ1 experiment.
- It also produces the *kind* of result RQ1 hopes for — a **non-trivial,
  sign-reversing** relationship between information quality and outcome, rather
  than "better information always wins". CURRENT_THESIS explicitly names "the
  boundary is trivially forecast-aware always wins when skill > 0" as the known
  risk to RQ1; Sezer is an existence proof that non-trivial answers are
  publishable in adjacent hazards, and that someone else has already found one.
- Murphy/Ehrendorfer decoupling again, constructively: sharper information makes
  outcomes *worse* under the wrong release policy.

## WildfireGuardian difference
Operational, per NOVELTY_STANDARD §6:

1. **What is varied is not forecast error.** Sezer varies the precision of a
   *deliberately designed public signal* — a policy lever the agency chooses.
   WildfireGuardian proposes to vary the *error of the forecast itself*, which
   the decision maker does not choose. The mechanisms differ: Sezer's harm from
   precision runs through behavioural synchronisation and congestion; RQ1's
   harm from error runs through misplaced fire-arrival estimates relative to a
   route.
2. **No comparator policy.** There is no positional trigger or buffer, tuned or
   otherwise; the comparison is between disclosure designs.
3. **No observation-to-product latency.** Disclosure *timing* (the release
   schedule) is a lever; the delay between observing the storm and having a
   product is not modelled. `forecast_latency: no`.
4. **No assisted evacuation, no responder, no pickup, no inbound leg, no
   dispatch deadline.** Zones self-evacuate.
5. **Preprint, and single-source.** It cannot be used to *kill* a claim on its
   own (EVIDENCE_LEVELS rule 1 needs E3 — met — but CITATION_RULES needs two
   independent metadata sources — not met).

## Novelty threat
**MODERATE** to WG-C-002; **MODERATE** to WG-C-014.

It does not occupy RQ1. It does mean that "we sweep an information-quality
parameter and report decision loss, and the answer is non-monotone" is, as a
research move, already in the 2026 evacuation literature. WildfireGuardian's
version has to be distinguished by the axes (true forecast error, and latency)
and by the comparator (tuned positional trigger), not by the move itself.

## Quotes / page references
Quotes above are from the retrieved full text: Abstract; §6.4 "Experiment 2:
staggered disclosure and the value of precision"; Figure 6 caption. Line
references into the retrieved text rather than journal pages, as this is a
preprint.

## Follow-up papers
- `regnier2008public` — the hurricane decision-frontier ancestor.
- `jewson2026evacuation` — the other 2026 paper that sweeps an information
  parameter to a decision flip.
- `chang2026multiscale` — the wildfire cousin: alert timing, congestion,
  differential escape.
- Forward citation chase **NOT DONE**.
