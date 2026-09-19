# kalogeropoulos2023kperil

## Citation
Kalogeropoulos, N.; Mitchell, H.; Ronchi, E.; Gwynne, S.; Rein, G. (2023). "Design of
stochastic trigger boundaries for rural communities evacuating from a wildfire."
*Fire Safety Journal* 140: 103854. DOI 10.1016/j.firesaf.2023.103854
Software: k-PERIL, Zenodo DOI 10.5281/zenodo.10277917 (2023-12-06).

## Publication status
PEER_REVIEWED (journal article). OPEN ACCESS, hybrid, CC-BY listed in the Crossref
license block. Evidence level E2 — full abstract retrieved from OpenAlex; full text not
read.

## Problem
PERIL's safety factor is a margin. It cannot express *how likely* a trigger boundary is to
be wrong, or *where* around a community the boundary is most sensitive.

## Method
k-PERIL: repeated wildfire simulations sampling **historic wind, weather and vegetation
variation** around a community; the resulting distribution of boundary positions gives a
**stochastic trigger boundary**. Introduces **uncertainty rosettes** — a directional map
of where boundary position varies most with fuel, wind or evacuation time.

## Data
Roxborough Park, Colorado, USA.

## Outputs
- Probabilistic trigger boundaries (boundary indexed by probability)
- Uncertainty rosettes (directional sensitivity fields)

## Key equations
NEEDS_FULL_TEXT.

## Assumptions
Uncertainty is *climatological* (drawn from historic variability), not *forecast*
uncertainty. One flame-spread model. Egress only. Evacuation time treated as a variable
input but not simulated as traffic within this paper.

## Validation
Application study on one community; no forecast-skill evaluation.

## Limitations
Historic-variability sampling answers "what could the fire do here in general," not "what
will this fire do given today's forecast." No responders, no traffic, no dispatch.

## WildfireGuardian overlap
**This paper is the reason WG-C-004 cannot be claimed.** Probabilistic/stochastic trigger
boundaries around a threatened community, complete with a spatial uncertainty product,
were published in 2023 in a peer-reviewed journal and released as open-source software.

## WildfireGuardian difference
The operational distinction that survives is the *source* of the distribution and the
*subject* of the boundary: k-PERIL samples historic variability to protect a community's
egress; WildfireGuardian proposes to condition on a live forecast ensemble and to evaluate
a responder's round-trip feasibility. That is a difference in conditioning and in decision
subject — it is NOT a difference in "we are probabilistic and they are not," which would
be false.

## Novelty threat
**level: CRITICAL** — occupies WG-C-004.

## Quotes / page references
Abstract: "k-PERIL, that calculates stochastic trigger boundaries, based on the
variability of wildfire behaviour around a community." (abstract via OpenAlex)
Abstract: "The concept of uncertainty rosettes is introduced." (abstract via OpenAlex)

## Follow-up papers
kalogeropoulos2025dire, kalogeropoulos2026ensemble, ronchi2023verification,
moradi2026supported (uses the same Roxborough Park setting).
