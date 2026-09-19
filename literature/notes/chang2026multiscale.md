# chang2026multiscale

## Citation
Chang, S., Comfort, L., Soga, K., Li, P., & Wang, Y. (2026). "Multiscale Wildfire-Evacuation
Modeling: Assessing Differential Access to Safe Egress in Marin County, CA." *Risk Analysis*.
DOI: 10.1111/risa.70338. PubMed ID 42642826. Volume/issue/pages: UNVERIFIED.

## Publication status
`PEER_REVIEWED`, journal article, open access (BRONZE). Full abstract retrieved via Semantic
Scholar. Body NOT retrieved. Evidence level **E2**.

First author affiliated with the Graduate School of Energy and Environment, Korea University
(per a WebSearch result; affiliation NOT independently verified against the article).

## Problem
Wildfire evacuation outcomes vary because of interactions among fire progression, human behaviour,
and traffic dynamics, which most models treat separately. The paper asks who actually gets out, and
why the answer is unequal.

## Method
**Tri-coupled framework**: a fire-spread model + a **multichannel communications model capturing
varied cognition times** + a spatial-queue traffic model. Analysed through a multi-scalar strategic
action fields lens (macro / meso / micro).

## Data
Three real Marin County, California communities.

## Outputs
- Evacuation efficiency as a function of communication timing and coordination.
- Demonstration that cognitive/notification delays produce **nonlinear** congestion.
- Peak background traffic reduces available capacity.
- Community-level differences driven by demographic, infrastructural, and temporal characteristics.
- Micro-level finding: everyday responsibilities (e.g. child pickup) disproportionately affect
  congestion.
- Framing conclusion: **evacuation capacity functions as a form of access to safety, unevenly
  distributed by communications access, mobility constraints, and network characteristics.**

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Households self-evacuate by private vehicle; no assisted-evacuation vehicle is dispatched to anyone.

## Validation
Three real communities with real network data; scenario-based, not event-validated.

## Limitations
No responder. No pickup. No assisted evacuation. Fire progression constrains network state but no
feasibility deadline is computed.

## WildfireGuardian overlap
Two overlaps, one of which is uncomfortable:
1. **Latency as a decision-relevant variable.** This paper's central mechanism is that *when the
   alert arrives* determines who escapes, and that late alerting translates structurally into
   unequal access to evacuation capacity. That is the substance of WG-C-012 (forecast latency as a
   first-class decision variable), demonstrated in wildfire, in 2026, in *Risk Analysis*.
   WildfireGuardian's latency claim is about *forecast* latency rather than *alert* latency, but a
   hostile judge will not grant that distinction without an operational statement of the difference.
2. **Differential access framing.** "Access to safety, unevenly distributed by ... mobility
   constraints" is WildfireGuardian's motivating premise, already published.

## WildfireGuardian difference
- Chang et al. model the *communication* channel to the household; WildfireGuardian models the
  *forecast* pipeline to the decision-maker. The operational difference: Chang et al.'s delay sits
  between a decision already made and a household acting on it; WildfireGuardian's latency sits
  between an observation and the decision itself, and therefore interacts with forecast skill.
  This distinction is stateable but must be stated carefully.
- No responder, no round trip, no deadline.
- Self-evacuating households only — the population that WildfireGuardian explicitly excludes.

## Novelty threat
**level: MODERATE** (for Categories 2/9; **the Category 4 / WG-C-012 agent should be told about
this paper**)
- **WG-C-005** → not threatened directly (no assistance modelled), but it removes any claim that
  differential mobility access in wildfire evacuation is unexamined.
- **WG-C-007** → weakens the Korean-setting angle: a Korea-affiliated group is already publishing
  wildfire-evacuation modelling, in a top risk journal, on a US case. "First Korean researcher to do
  wildfire evacuation modelling" is false.
- **WG-C-012** → `NEEDS_FULL_TEXT`; potentially WEAKENING.

## Quotes / page references
From the retrieved abstract:
- "a communications model capturing varied cognition times" (Abstract).
- "cognitive delays producing nonlinear congestion" (Abstract).
- "evacuation capacity functions as a form of access to safety, unevenly distributed by
  communications access, mobility constraints, and network characteristics" (Abstract).

## Follow-up papers
- Beyki et al. (2026), *Safety Science* 199:107200 — the other 2026 fire-coupled ABM, with inbound
  rescue.
- Siam et al. (2022), *TR-D* 103:103147 — interdisciplinary multimodal wildfire evacuation ABM.
- Grajdura, Borjigin & Niemeier (2022), *TR-D* 104:103190 — awareness delay and reduced vehicle
  access in a fast-moving fire.
