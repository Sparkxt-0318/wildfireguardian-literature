# mois2026aievacroute

## Citation
산림청 (Korea Forest Service), within the 행정안전부 (MOIS) public-sector AI services
programme. 「AI 기반 산불·연무 확산 감시·예측」 [AI-based wildfire and smoke spread
monitoring and prediction — *translation*]. Programme announced 15 September 2026 as one
of four safety/living-inconvenience AI tasks. Reported by aitimes.kr (no. 41932),
newspim.com (20260915000178), koit.co.kr, dailian.co.kr, public25.com, anjunj.com.

## Publication status
**GOVERNMENT_REPORT — NOT peer-reviewed.** Language: Korean. It is a government programme
announcement, and — importantly — the **originating MOIS press-release page was not
retrieved**; the record rests on six independent Korean news reports, two fetched in full.
Verification level is therefore secondary-source corroboration, not primary.

## Problem
Field commanders in Korean wildfires must simultaneously decide where residents should go
and where suppression crews and equipment can be sent in.

## Method
Not disclosed beyond: historical spread data from past Korean burn areas combined with
meteorological, topographic and fuel information, used to analyse spread direction and
speed, plus a smoke-dispersion path component. No model family, no validation design, no
resolution, no uncertainty treatment is given in any of the six reports.

## Data
과거 산불 피해지역의 확산 자료 (spread data from past Korean fire-damaged areas) +
기상·지형·연료 정보 (weather, terrain, fuel).

## Outputs
Three, per the reporting:
1. 주민 대피경로 — resident evacuation routes;
2. **진화 인력·장비의 투입 경로 — ingress routes for suppression personnel and equipment**;
3. 현장의 대피·진화 판단 지원 — support for field evacuation and suppression judgement.

## Key equations
None disclosed.

## Assumptions
Unknown. Nothing published on how the smoke path constrains route feasibility, or whether
the ingress route is checked against a time-varying fire front.

## Validation
Unknown. Development stage explicitly reported as 개발 중 / not yet operationally deployed;
no completion date was given in any report.

## Limitations
- Routes, not times. No report mentions a departure time, a deadline, or a feasibility
  window on either leg.
- No mention of residents who cannot self-evacuate, of vehicles sent to collect them, or
  of a round trip.
- No published accuracy, no published comparator.
- Cannot currently be cited in a paper from a primary source.

## WildfireGuardian overlap
**This is the most direct Korean overlap found anywhere in category 8.** A Korean agency
is building a system that computes, from a modelled future fire, an **inbound route for
responders moving toward the fire** at the same time as outbound resident routes. The
inbound-leg idea — the thing WG-C-003 leans on hardest — is not unoccupied in Korea.

## WildfireGuardian difference
Operational: the KFS system answers "which way should the crew go in"; WildfireGuardian
answers "how late may the crew leave and still complete base → resident → pickup →
destination". A route is a path in space; a dispatch deadline is a scalar time with a
feasibility guarantee attached to it. Also: the KFS system's inbound leg serves
*suppression* units, not *assisted-evacuation* units, and it carries no pickup dwell and
no return leg.

## Novelty threat
**HIGH for WG-C-007, MODERATE for WG-C-003.**
- WG-C-007 cannot be phrased as "first Korean use of modelled fire spread for evacuation
  routing" — that is WG-C-001, already REJECTED, and this programme re-kills it in Korea.
- WG-C-003 survives on the *quantity* (dispatch-by deadline, round trip, pickup dwell),
  not on the *setting* and not on "no one routes responders inbound in Korea."
- This must be disclosed unprompted in the fair defence. A judge who knows about the
  September 2026 announcement and hears us claim Korean-first anything will end the
  conversation there.

## Quotes / page references
> 「과거 산불 피해지역의 확산 자료에 기상·지형·연료 정보를 결합해 산불의 확산 방향과
> 속도를 분석한다. 연기 확산 경로까지 반영해 주민 대피경로와 진화 인력·장비의 투입
> 경로를 제시」
> *Translation:* "It analyses fire spread direction and speed by combining spread data from
> past fire-damaged areas with weather, terrain and fuel information. Reflecting even the
> smoke-dispersion path, it presents resident evacuation routes and ingress routes for
> suppression personnel and equipment." (aitimes.kr, 15 Sept 2026.)

## Follow-up papers
- The primary MOIS press release (not yet retrieved — Open question 1 in the search log).
- Any KFS technical specification or NIFoS user guide for the system.
- `mois2025evacuationstages` (the policy this builds on).
