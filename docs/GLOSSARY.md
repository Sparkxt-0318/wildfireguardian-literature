# GLOSSARY.md

Terms used precisely in this repository. Where a term has different meanings in
different communities, both are given, because cross-community synonymy is the
main reason prior art gets missed.

---

**Trigger / trigger boundary / trigger buffer.** A spatial boundary around a
community such that when the fire crosses it, a protective action (usually
evacuation) is initiated. Introduced to wildfire by the Cova/Dennison lineage.
*Synonyms in other fields:* set-back distance, protective action decision
point, warning threshold, evacuation trip line.

**Egress.** Outbound movement from the threatened location to safety. The
quantity the classical trigger literature bounds.

**Ingress.** Inbound movement *toward* the threatened location — here, a
responder travelling from base to resident. Constrained by fire arrival on the
inbound path and by outbound traffic. **The classical trigger literature does
not bound this.**

**Pickup (dwell).** Time spent at the resident's location loading/assisting.
Non-zero and potentially dominant for mobility-limited residents.

**Round trip / full mission.** `base -> resident -> pickup -> safe destination`.
WildfireGuardian's RQ2 unit of analysis.

**Dispatch-by deadline.** The latest time a responder may *depart the base*
such that the full mission completes before fire arrival constrains any leg.
Distinct from an egress deadline, which asks when a person must *leave their
location*. Different decision subject, different units.

**Forecast skill.** How good a forecast is, measured against a reference.
*Not* the same as forecast value.

**Forecast value.** The benefit a decision-maker obtains by using the forecast,
given their cost/loss structure. A skilful forecast can have zero value; an
unskilful one can have value at extreme cost/loss ratios. The distinction is
foundational in the forecast-value literature and we must use it correctly.

**Forecast latency.** Delay between the observed state and the forecast being
*available to the decision-maker*. A perfectly skilful forecast arriving after
the dispatch deadline has zero value. See WG-C-012.

**Lead time.** How far ahead the forecast predicts. Orthogonal to latency.

**Cost-loss ratio.** The ratio of the cost of protective action to the loss
avoided. Determines the optimal probability threshold for action in the
classical forecast-value framework.

**OSSE (Observing System Simulation Experiment).** An experiment where a model
run supplies synthetic "truth," synthetic observations are drawn from it, and a
second system assimilates them — used to evaluate observing systems or
decisions without real deployment.

**Identical twin vs fraternal twin.** Identical twin: the same model produces
truth and forecast. Fraternal twin: different models. Identical-twin designs
are known to be optimistic about impact. We require fraternal twin — see
`FAILURE_MODES.md` §2.

**Inverse crime.** Using the same model to generate synthetic data and to
invert/solve with it, producing unrealistically good results. The inverse
problems community's name for the danger in §2.

**Pseudoreplication.** Treating non-independent observations as independent
replicates in statistical analysis. Our scenarios-within-events structure is a
textbook setup for it.

**Equivalence / non-inferiority testing.** Statistical procedures to show two
policies are *practically the same* (or that one is not meaningfully worse).
Necessary because a non-significant difference is not evidence of equivalence.

**VOI (Value of Information).** Expected improvement in decision outcome from
acquiring information before deciding. EVSI/EVPI are its standard measures.

**Decision-directed / decision-focused sensing.** Choosing observations by
their effect on the decision rather than on predictive accuracy. Closely
related to decision-focused learning ("smart predict-then-optimize") in ML.

**PDPTW.** Pickup-and-Delivery Problem with Time Windows. The OR formulation
that most closely matches the assisted-evacuation round trip. **Its maturity is
a standing threat to WG-C-003's formulation novelty.**

**Protectability.** Whether a location can be defended or its occupants
extracted, given the fire and available resources. "Robust protectability" =
holds under fire-model error.

**OA status.** Open access state, recorded so binder preparation knows what can
be printed and what requires institutional access.

**Occupied (claim status).** A prior work substantially does this already. The
space is taken. Distinct from `REJECTED`, which means our specific sentence is
false.

---

## Institutions (Korea)

**KFS — Korea Forest Service (산림청).** National forest agency; wildfire
response lead.
**NIFoS — National Institute of Forest Science (국립산림과학원).** KFS research
institute; fire behaviour, fuels, danger rating.
**MOIS — Ministry of the Interior and Safety (행정안전부).** Disaster
management, alerting, evacuation policy.
**NDMI — National Disaster Management Research Institute (국립재난안전연구원).**
**KMA — Korea Meteorological Administration (기상청).** Operates GK2A.
**GK2A — GEO-KOMPSAT-2A.** Korean geostationary meteorological satellite.

Publications from KFS, NIFoS, MOIS, and NDMI are `GOVERNMENT_REPORT` unless
they appear in a peer-reviewed journal.
