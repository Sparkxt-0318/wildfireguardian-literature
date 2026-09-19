# mois2025evacuationstages

## Citation
행정안전부 (Ministry of the Interior and Safety), with 산림청 (Korea Forest Service).
「정부, 초고속 산불 대비 주민대피 체계 개선키로」 [Government to improve the resident
evacuation system in preparation for ultra-fast wildfires — *translation*]. MOIS press
release, 16 April 2025. nttId=117125. Contact: 사회재난대응조정과.

## Publication status
**GOVERNMENT_REPORT — NOT peer-reviewed.** Language: Korean. This is an agency press
release announcing an operational policy change. It must never be described as a study.

## Problem
The March 2025 Gyeongbuk fires spread faster than the existing resident-evacuation
procedure assumed. The operational question: at what point before fire arrival must
residents — and separately, residents who cannot move quickly — be told to leave?

## Method
Administrative rule change, not analysis. The national wildfire spread prediction system
(산불확산예측시스템) was modified to take **maximum instantaneous wind speed**
(최대 순간풍속) as well as mean wind speed. Predicted fire-line arrival time is then used
to partition area into two zones, which map onto a three-stage Ready / Set / Go protocol.

## Data
Operational: the spread prediction system's output plus KMA wind fields. The release cites
the March 2025 Gyeongbuk event, where gusts reached 27.6 m/s and the fire advanced at
8.2 km/h (figure reported in the corroborating edaily coverage).

## Outputs
- **위험구역 (danger zone)** — predicted fire-line arrival **within 5 hours** → stage 3
  "Go": immediate evacuation order to residents.
- **잠재적 위험구역 (potential danger zone)** — arrival **within 8 hours** → stage 2 "Set":
  residents check disaster information / hazard area / shelter routes and prepare, and
  **안전취약계층 (safety-vulnerable groups, e.g. 고령자) evacuate in advance (사전 대피)**.
- **Stage 1 "Ready"** — a fire in a neighbouring city/province; be alert to the
  possibility of an order.

## Key equations
None published. The 5 h / 8 h thresholds are stated, not derived. Whether they came from
an evacuation-time analysis or were set administratively is **NEEDS_FULL_TEXT**.

## Assumptions
- A single deterministic predicted arrival time is adequate to define the zone boundary.
- Vulnerable residents need approximately 3 extra hours relative to the general population.
- Evacuation is self-mobility; no responder trip is represented.

## Validation
None reported. No retrospective test against the March 2025 fires is given in the release.

## Limitations
- Deterministic: no ensemble, no forecast-error treatment, no stated confidence level.
- The vulnerable-group provision is "evacuate earlier", not "someone will come and get
  you". No logistics, no vehicle, no responder.
- Zone-level, not household-level or facility-level.
- The lead times are fixed nationally — they do not vary with road access, village
  geometry, or how many people actually need assistance.

## WildfireGuardian overlap
Large and direct. This is Korean wildfire evacuation **timing**, keyed to a **modelled
future fire arrival time**, with an **explicitly earlier trigger for people who cannot
move quickly**. That is the same decision space as WG-C-003/WG-C-005 and it is the core
reason WG-C-007 cannot be stated as "first Korean evacuation-timing analysis".

## WildfireGuardian difference
MOIS emits a *fixed lead time against a deterministic arrival forecast*. WildfireGuardian
emits a *latest responder dispatch time such that base → resident → pickup → destination
closes under a stated quantile of an ensemble arrival-time distribution*. Different unit
(hours-before-arrival threshold vs fire-relative dispatch clock), different subject (the
resident's own departure vs a responder's departure), different uncertainty treatment
(none vs explicit).

## Novelty threat
**HIGH for WG-C-007.** It does not kill WG-C-003 — MOIS computes no round trip and no
dispatch time — but it does two damaging things:
1. It removes "no Korean evacuation timing rule exists" as an available sentence.
2. It **supplies the tuned comparator** WG-C-006 demands. A judge can now ask: "does your
   method beat the 5 h / 8 h rule?" If the answer is not measured, WG-C-002 and WG-C-006
   are both exposed. This should be treated as a gift, not a wound: it gives the program a
   real, operational, nationally-mandated baseline instead of a strawman buffer.

## Quotes / page references
> 「화선 도달거리가 5시간 이내로 예상된 지역은 '위험구역'으로, 8시간 이내인 경우는
> '잠재적 위험구역'으로 설정」
> *Translation:* "Areas where the fire line is predicted to arrive within 5 hours are set
> as 'danger zones'; within 8 hours, as 'potential danger zones'."
(Quoted in edaily, 15 April 2025, reporting the MOIS/KFS announcement.)

The MOIS release itself states general residents should be organised for evacuation about
5 hours before anticipated impact and disaster-vulnerable residents about 8 hours before.

## Follow-up papers
- Any evaluation of how the 5 h / 8 h rule performed in the 2026 fire season — none found.
- `mois2026aievacroute` (the follow-on AI programme).
- `sung2025geostationary` — supplies the detection-latency term that eats into these lead
  times.
