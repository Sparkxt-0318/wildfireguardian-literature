# ONE_SENTENCE_DIFFERENCES.md

One sentence per threatening paper, stating the difference **operationally**.

The test (`NOVELTY_STANDARD.md` §6): could a reader reproduce the distinction
without asking us what we meant? "We consider uncertainty, they do not" fails
that test. Different output quantity, different decision subject, different
units — those pass.

Memorise the top five. They are what you say in the first ten seconds.

---

## The five that matter

**`moradi2026supported`** (supported wildfire evacuation, PREPRINT)
> Moradi solves for *who drives where with how many vehicles*, given fire
> time windows sampled from a uniform distribution; we solve for *the latest
> clock time a vehicle may leave at all*, given fire arrival from a spread
> model, and report how that time moves with forecast error.

**`beyki2026modular`** (inbound rescue, *Safety Science*)
> Beyki simulates an extraction happening and reports what happened; we compute
> the boundary of when an extraction can still be started — a simulator answers
> "did it work", a deadline answers "is it too late to try."

**`kalogeropoulos2026ensemble`** (ensemble trigger boundaries, *Fire Safety Journal*)
> Kalogeropoulos draws a line on the ground that tells residents when to leave;
> we compute a time on the clock that tells a dispatcher when to send — a
> distance for the person in the house, a departure time for the vehicle at the
> station.

**`regnier2008public`** (forecast-quality boundary, *Management Science*)
> Regnier bounds *evacuate or not* against hurricane track uncertainty for a
> whole population; we bound *dispatch or not* for one responder serving one
> resident, where the payoff is discontinuous — the mission closes or it does
> not — rather than a scalar cost.

**`li2018coupling`** (percentile-indexed trigger buffers, *Fire Technology*)
> Li reports a buffer distance at a chosen clearance percentile for
> self-evacuating traffic; we use exactly that construction as our **baseline**
> and ask what a forecast adds beyond it.

---

## Trigger-modelling lineage

**`cova2005trigger`** — Cova computes a level set of fire arrival time around a
community from one deterministic run; we compute a scalar departure time for a
vehicle whose route enters and leaves that region.

**`dennison2007wuivac`** — WUIVAC produces trigger buffers across strategic
scenarios; the subject is the household's egress, never a responder's round trip.

**`larsen2011cedar`** — Larsen evaluates buffers against a real fire's
progression retrospectively; the quantity evaluated is buffer adequacy, not
dispatch feasibility.

**`li2015household`** — Li stages warnings household by household; staging
orders *who is told when*, not *when a vehicle must depart*.

**`mitchell2023peril`** — PERIL integrates spread and evacuation times into a
safe trigger; the evacuation time is the community's, and the output is a
boundary.

**`kalogeropoulos2023kperil`** — k-PERIL makes that boundary stochastic with
uncertainty rosettes; still a boundary, still egress.

**`kalogeropoulos2025dire`** — outputs an evacuation safety factor for egress;
structurally the closest *kind* of output to ours, for the other direction of
travel.

---

## Assisted evacuation and routing

**`flores2023goal`** — goal programming for early evacuation of vulnerable
people plus relief distribution; the decision is the allocation, ours is the
clock.

**`shahparvari2017robust` / `shahparvari2019fleet`** — computes how many
vehicles are needed to clear late evacuees inside hard time windows; the
windows are *inputs*, ours is the *output*.

**`alexander2026nursing`** — minimises waiting time and makespan for shuttling
mobility-impaired residents; no hazard progression constrains any leg.

**`rambha2021staged`** — staged hospital evacuation timing under an evolving
hurricane forecast; the staging decision is *which patients move in which
wave*, not the departure instant of a collecting vehicle.

**`tang2025transit`** — RL policy for equitable transit evacuation; a learned
policy prescribes actions, it does not report a feasibility boundary.
**(Difference provisional — abstract not retrieved.)**

**`xu2022multiparking`** — heterogeneous VRP with split pickup matching
mobility classes to vehicle classes; solves assignment, not timing.

**`yu2020disruption`** — measures national-scale loss of emergency access to
vulnerable populations during floods; a statistic over a population, not a
deadline for one mission.

---

## Forecast value, sensing, evaluation

**`ardid2026forecastvalue`** — maps skill to economic value for wildfire danger
forecasting; the decision is a fire-danger action threshold, not mission
feasibility.

**`murphy1987accuracyvalue` / `chen1987qualityvalue`** — establish that accuracy
is not monotone with value in the scalar cost-loss setting; we ask whether it
holds when the "forecast" is a spatial field and the loss is a binary mission
closure — and *where* on the map the error has to be to matter.

**`bischiniotis2019tradeoffs` / `lopez2020bridging`** — optimise *lead time*
jointly with skill; we hold lead time fixed and vary *latency*, the
observation-to-product delay, which those papers do not separate.

**`sun2025decisionfocusedsensing`** — selects sensors by evacuation decision
regret in floods; our sensing question is conditioned on a deadline, so the
value of an observation falls to zero once the dispatch time has passed.

**`raeth2025decisionskill`** (PREPRINT) — shows forecast rankings do not survive
transfer to decision tasks with scalar costs; ours is a spatial field feeding a
routing feasibility test.

**`mois2026aievacroute`** (GOVERNMENT REPORT, not peer-reviewed) — the Korean
programme outputs *routes* for residents and for suppression crews; a route
says where to go, a deadline says whether to go at all.

**`wu2025denkf` / `zha2024distributed`** — use OSSEs to evaluate fire-state
accuracy; we use one to evaluate a decision, which is the extension
`zeng2020osse` lists as open.
