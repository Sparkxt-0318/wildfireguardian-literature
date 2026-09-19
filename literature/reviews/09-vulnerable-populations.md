# 09 — Vulnerable Populations in Wildfire Evacuation

**Category 9.** Agent A/B (Search Researcher + Prior-Art Adversary).
**Compiled:** 2026-09-19.
**Claims touched:** WG-C-005 (framing), WG-C-007 (Korean setting), WG-C-003 (population premise).
**Search log:** `docs/search-logs/agent-assisted-vulnerable.md`.

> **Standing constraint (PROJECT_CONTEXT).** WildfireGuardian does not medicalize residents.
> "Cannot self-evacuate" must be a **mobility and transport-access condition**, evidenced from the
> transport-disadvantage and evacuation-assistance literature — not a diagnosis. This review reports
> what the literature actually uses, which is **not** what that constraint requires, and states the
> gap plainly.

---

## 1. Headline finding

**The literature has no operational definition of "cannot self-evacuate."**

It has three incompatible things instead:

1. **Categorical population labels** in the public-health and review literature
   (older adults, people with disabilities, people with chronic conditions).
2. **Operational transport predicates** in the transportation and equity literature
   (no household vehicle, does not drive, no accessible transport, no driver available).
3. **Institutional/registry predicates** in emergency-management practice
   (enrolment in a special-needs registry; residence in a licensed care facility).

Optimisation papers in Category 2 almost always use **(3)** implicitly — the population is defined by
*being at an assembly area or in a facility* — which converts the definitional problem into a
location problem and makes it disappear. WildfireGuardian cannot do that, because its unit of
analysis is a resident at home in a dispersed mountain village.

---

## 2. Operational definitions actually used in the literature

### 2.1 Public-health / scoping-review stream

**Matsuo, Kietzman, Hays & Song (2025)**, *IJERPH* 22(11):1680 — PRISMA-ScR scoping review,
five databases, 20 primary studies, STEPS framework.

Population defined **categorically**, not operationally:
> "older adults (55 years old and above), adults of any age with disabilities or chronic illnesses,
> or official/unofficial support personnel for these populations."

The barrier criteria it reports are the closest thing to an operational definition available, and
they are a **mixture of transport and physiological criteria**:

| Criterion | Type | Usable under PROJECT_CONTEXT? |
|---|---|---|
| No private vehicle / does not drive (reported: 43% of participants did not drive; 50% lacked public-transport access) | **Transport access** | **Yes** |
| Requires assistive devices (cane, wheelchair) → needs an accessible vehicle | **Mobility** | **Yes** |
| Hearing or vision loss | Sensory / physiological | No — this is a *message-receipt* barrier, belongs in alerting, not in the dispatch model |
| Dependence on life-sustaining equipment (e.g. ventilators) | Medical | **No** |
| Relies on family, caregivers, or medical staff for transportation | **Social/transport access** | **Yes, if phrased as "no driver available"** |

**Evidence base:** predominantly qualitative studies (interviews, focus groups) and cross-sectional
surveys of disaster survivors collected **after** the event. Per the full-text reading, **no
population registry or baseline census instrument that systematically identifies
evacuation-disadvantaged persons in advance is reported.** This is the review's own gap finding and
it is directly consequential for WildfireGuardian: there is no published, validated instrument for
counting how many residents in a given area cannot self-evacuate.

### 2.2 Transportation / equity stream

This stream is where the operational predicates live, and they are **transport-access predicates,
which is exactly what WildfireGuardian needs**:

- **Carless / zero-vehicle household.** The census-derived predicate. Used throughout the
  transit-evacuation OR literature (Bish 2011 and successors) under the label
  "transit-dependent" or "transit-captive."
- **More adults than vehicles in the household.** A finer predicate that appears in the
  transport-disadvantage framing; captures households where a vehicle exists but is unavailable at
  the decision time.
- **Reliance on non-automobile modes.** The UCLA ITS 2025 studies of transit riders in the January
  2025 Los Angeles fires report that transportation-disadvantaged groups (low-income, Black, and
  carless residents) disproportionately used public transit or walking/biking, that prolonged
  evacuations were especially common among those without access to personal vehicles (**52%**), and
  that longer evacuation times meant greater PM2.5 and debris exposure.
  *(Institutional reports, not peer-reviewed — record them as such.)*
- **Mobility-class matching.** **Xu et al. (2022)**, *IEEE Access* 10:36073–36090 is the cleanest
  operationalisation found in an optimisation paper: it splits residents into "individuals with high
  mobility" and "individuals with low mobility, such as the elderly," and imposes
  **matching constraints between individual type and vehicle type** (wheelchair-equipped vehicles,
  volunteers). This is a transport/mobility predicate with no diagnosis attached, and it is the
  closest published precedent for how WildfireGuardian should define its population.

### 2.3 Optimisation-literature stream (implicit definitions)

- **Moradi et al. (2026)** — the broadest and most WildfireGuardian-compatible list:
  > "individuals with disabilities and limited mobility, seniors residing in long-term care
  > facilities and retirement homes, **people with no vehicles**, and tourists"

  Note that "people with no vehicles" sits alongside medical categories without distinction. The
  model then collapses all of them onto **assembly areas** with a **priority class** (high/low),
  where priority drives hospital-vs-shelter routing. So the operative predicate in the model is
  *"is at an assembly area"* plus *"has priority p"*.
- **Flores et al. (2020, 2023)** — evacuees "classified according to their health condition."
  Explicitly medical. WildfireGuardian must not follow this.
- **Alexander et al. (2026)** — "mobility-impaired nursing home residents." Defined by
  **facility residence**, which is an institutional predicate.
- **Shahparvari lineage (2015–2019)** — "late evacuees." A **behavioural/temporal** predicate:
  whoever is still there when the window closes. Notably this definition sidesteps capability
  entirely and may be the most operationally honest in the set — but it is unusable for *planning*,
  because you cannot identify a late evacuee in advance.

### 2.4 Practice / registry stream (not peer-reviewed)

Special-needs registries (e.g. Florida's statutory county registries) define the population by
**enrolment**: registered individuals are contacted with a pickup time and location and given
transport from home to shelter. This is the only stream that already has the
"vehicle-is-sent-to-your-home" operational model WildfireGuardian assumes.

Documented limitations, from advocacy and practitioner sources: registration does not guarantee
assistance; privacy concerns suppress enrolment; some people with disabilities are reluctant to
register; and many evacuation centres do not meet accessibility standards. Canadian advocacy
reporting on recent wildfires describes the same gaps.
**These are institutional/news sources — usable as motivation, not as evidence.**

---

## 3. What the evidence base actually supports

| Statement WildfireGuardian might want to make | Supported? | By what |
|---|---|---|
| A non-trivial share of residents in a WUI community cannot evacuate in a private vehicle | **Yes** | Matsuo 2025 (43% did not drive; 50% lacked transit access); UCLA ITS 2025 (52% of carless had prolonged evacuations) |
| Lacking vehicle access materially worsens wildfire evacuation outcomes | **Yes** | Grajdura et al. 2022 (agents with reduced vehicle access are trapped more often in a Camp Fire ABM); UCLA ITS 2025 (longer exposure to PM2.5 and debris) |
| Differential mobility produces differential access to safe egress in wildfire | **Yes, and recently** | Chang et al. 2026, *Risk Analysis* — "evacuation capacity functions as a form of access to safety, unevenly distributed by communications access, mobility constraints, and network characteristics" |
| There is a validated instrument for identifying, in advance, who cannot self-evacuate | **No** | Matsuo 2025 reports none; registries are enrolment-based and incomplete |
| Assisted-evacuation dispatch is constrained by travel-time feasibility rather than by resource availability or communication | **NOT SUPPORTED — and this is a falsifier of the thesis** | See §5 |

---

## 4. Korea (Category 9 ∩ WG-C-007)

The Korean-language pass (`산불 대피 거동불편자 구조 차량 배차`) returned **no peer-reviewed
Korean assisted-evacuation research.** It returned:

- **MOIS (2025)** press material on revising the resident-evacuation system for fast-moving wildfires.
- **Yeongyang County (경상북도 영양군)** disaster evacuation network: a scheme in which scheduled
  buses and charter buses move groups of residents while **taxis serve residents in locations large
  vehicles cannot reach or who need individual transport**, with the county and transport operators
  sharing standing information on available vehicles and personnel. The reporting frames the problem
  exactly as WildfireGuardian does — mountain villages, dispersed settlement, many elderly residents,
  residents without a car or unable to move independently, and the observation that *a difference of
  a few minutes in securing an evacuation vehicle is directly tied to resident safety*.
- **KFS / NIFoS / provincial** public action guidelines (국민행동요령) — generic, no timing model.

**Implication for WG-C-007.** These are news and government sources. They are excellent *motivation*
and they establish that the Korean operational problem is real and organised. They are **not**
literature and cannot support a novelty claim. Under NOVELTY_STANDARD §4, the Yeongyang scheme is
also a double-edged find: it demonstrates that Korean practice already allocates a **heterogeneous
fleet (bus vs. taxi) by resident mobility and location**, so WildfireGuardian's contribution in Korea
must be the *timing quantity*, not the *allocation idea*.

Separately: **Chang et al. (2026)** is first-authored from Korea University and published in
*Risk Analysis*. "First Korean wildfire-evacuation modelling" is false and must never be said.

---

## 5. The finding that most endangers the whole thesis

`CURRENT_THESIS.md` §"What would falsify the thesis," item 4:

> *"Evidence that assisted-evacuation dispatch is in practice constrained by resource availability
> and communication, not by travel-time feasibility. → the deadline is the wrong decision variable."*

**The Category 9 literature currently points toward that falsifier, not away from it.**

- Matsuo et al. (2025) identify **four** areas of concern, and the fourth is
  "inconsistent and inaccessible communication of transportation-related information during
  emergencies." Communication is named as a primary failure mode; travel-time feasibility is not
  named at all.
- Chang et al. (2026) find that **communication timing and coordination** determine evacuation
  efficiency, with cognitive delays producing nonlinear congestion — again, information, not travel
  time.
- The registry literature's failure mode is **enrolment and contact**, not vehicle travel time.
- Yu et al. (2020) *do* show travel-time degradation matters for responder arrival — but for floods,
  and against a regulatory standard.
- Shahparvari et al. (2019) found that 1,100 late evacuees **could** have been moved with seven
  vehicles and four shelters — i.e. in that case the binding constraint was not travel-time
  feasibility.

**Recommended action.** This should be logged as an open threat to RQ2 in `novelty/OPEN_QUESTIONS.md`
and answered, not ignored. The defensible position is narrow and must be stated as such:
*the deadline is the right decision variable in the regime where a responder exists, has been tasked,
and the question is whether to send it now or wait for a better forecast.* WildfireGuardian must
declare that regime as an assumption and show that it is non-empty — which the Yeongyang scheme,
where vehicles are pre-committed and standing information is shared, plausibly is.

---

## 6. Recommended operational definition for WildfireGuardian

Constructed from the transport-access subset of the literature, with sources:

> **A resident cannot self-evacuate if, at the decision time, the household has no operable vehicle
> available to it, or no licensed and present driver, or requires an accessible vehicle that the
> household does not have.**

Provenance of each clause:
- *no operable vehicle available* — carless/zero-vehicle household predicate; Bish (2011)
  transit-dependent framing; Matsuo et al. (2025) "43% did not drive"; UCLA ITS (2025) carless
  transit riders.
- *no licensed and present driver* — Matsuo et al. (2025) "rely on family members, caregivers, or
  medical staff for transportation."
- *requires an accessible vehicle* — Matsuo et al. (2025) assistive-device criterion;
  Xu et al. (2022) mobility-class↔vehicle-class matching constraint.

**Explicitly excluded**, and the exclusion must be stated in any paper: diagnosis, chronic-condition
status, ventilator dependency, and care-facility residence as a proxy. WildfireGuardian must say in
print that it adopts a **narrower** predicate than the literature uses, and why — otherwise a
reviewer will read the narrowing as an oversight rather than a design choice.

**Known weakness of this definition, to be conceded before a judge asks:** it is a *planning-time*
predicate applied to a *decision-time* question, and no validated instrument exists to measure it in
advance (Matsuo et al. 2025 report none). WildfireGuardian's population counts are therefore
assumptions, not measurements, and must be labelled as such under the simulation-transfer rules in
PROJECT_CONTEXT.

---

## 7. Category 9 papers recorded

| paper_id | Type | Threat | Role |
|---|---|---|---|
| `matsuo2025evacuation` | Journal (OA) | BACKGROUND | Evidence base and definitional gap |
| `chang2026multiscale` | Journal | MODERATE | Differential access; alert latency; Korea-affiliated authorship |
| `grajdura2022fastmoving` | Journal | MODERATE | Reduced vehicle access → trapped agents, Camp Fire |
| `xu2022multiparking` | Journal (OA) | MODERATE | Best published mobility-class operationalisation |
| `flores2020supported` / `flores2023goal` | Journal | MODERATE / HIGH | Health-priority classification (the approach we must *not* take) |
| `bish2011planning` | Journal | BACKGROUND | Transit-dependent / carless framing |
| `matsuo2025evacuation`, `zehra2024systematic` | Reviews | BACKGROUND | Gap statements |
| `ebrahimnejad2021disability` | Journal | MODERATE | `NEEDS_FULL_TEXT` |
| `sevim2025savrural` (provisional id) | Preprint | MODERATE | Rural + vulnerable + dispatched vehicles; `NEEDS_FULL_TEXT`, authors UNVERIFIED |
| `sun2024kincade` (provisional id) | Preprint | LOW | Social vulnerability, Kincade Fire; authors UNVERIFIED |
| `yu2020disruption` | Journal | HIGH | Responder reach to care homes under hazard |

**Non-literature sources recorded for motivation only (never cite as evidence):**
UCLA ITS (2025) LA-fires transit-rider studies; Natural Hazards Center "Transit Agencies and Wildfire
Evacuation"; Partnership for Inclusive Disaster Strategies (2025) disability evacuation transportation
planning guide; Florida statutory special-needs registries; MOIS (2025) Korean evacuation-system
revision; Yeongyang County bus/taxi evacuation network reporting.

---

## 8. Open questions for `novelty/OPEN_QUESTIONS.md`

1. Is there **any** validated instrument for measuring, in advance, the share of residents in an area
   who cannot self-evacuate? Matsuo et al. (2025) report none. If none exists, WildfireGuardian's
   population parameter is an assumption and every downstream number inherits that status.
2. Does the Korean National Fire Service / KFS / MOIS publish any **counted** figure for
   non-self-evacuating rural residents? (Korean-language pass found policy language, no counts.)
3. **Is travel-time feasibility ever the binding constraint in a documented real assisted wildfire
   evacuation?** Until this is answered, CURRENT_THESIS falsifier #4 is live.
4. Does Beyki et al. (2026) — the only fire-coupled inbound-rescue model — parameterise who needs
   extraction, and by what predicate?
