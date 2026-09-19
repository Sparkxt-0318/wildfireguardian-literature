# NOVELTY_MATRIX.md

**GENERATED** from `literature/metadata/*.yaml` by
`bibliography/build_bibliography.py`. Do not edit by hand — edit the metadata.

Rows are papers, sorted by threat level (conceptual overlap, never venue
prestige). Columns are the capability dimensions WildfireGuardian might claim.

Legend: `Y` = does it · `~` = partially / indirectly · `.` = does not · `?` = unrecorded

**How to read this for novelty.** A column that is dense with `Y` is a column
we cannot claim. A column that is empty is *not* thereby ours — it may simply
mean nobody indexes their work that way, or that we have not searched the field
that uses different vocabulary. Per `docs/NOVELTY_STANDARD.md` §3.2, an empty
column supports `UNKNOWN`, never novelty. The matrix shows where to *look*; it
does not by itself establish anything.

**Conjunction warning.** Reading across a row to find that no single paper has
`Y` everywhere is the forbidden argument (`NOVELTY_STANDARD.md` §3.1). The
useful reading is column-wise and pairwise, not row-wise.

| Paper | Threat | future fire | traffic | household trigger | prob. trigger | multi fire models | assisted evac | inbound responder | pickup | egress | dispatch-by deadline | forecast latency | skill boundary | decision value | scarce resources | VOI | active sensing | Korean setting | real validation | OSSE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `beyki2026modular` | CRITICAL | Y | Y | . | . | . | Y | Y | ~ | Y | . | . | . | . | ~ | . | . | . | Y | . |
| `cova2005trigger` | CRITICAL | Y | . | . | . | . | . | . | . | Y | . | . | . | ~ | . | . | . | . | . | . |
| `kalogeropoulos2023kperil` | CRITICAL | Y | . | . | Y | . | . | . | . | Y | . | . | . | ~ | . | . | . | . | . | . |
| `kalogeropoulos2025dire` | CRITICAL | Y | . | . | Y | . | . | . | . | Y | . | . | . | Y | . | . | . | . | ~ | . |
| `kalogeropoulos2026ensemble` | CRITICAL | Y | . | . | Y | Y | . | . | . | Y | . | . | . | Y | . | . | . | . | ~ | . |
| `li2018coupling` | CRITICAL | Y | Y | . | Y | . | . | . | . | Y | . | . | . | ~ | . | . | . | . | . | . |
| `malings2016voisensor` | CRITICAL | . | . | . | . | . | . | . | . | . | . | . | . | Y | . | Y | Y | . | . | . |
| `moradi2026supported` | CRITICAL | ~ | ~ | . | . | . | Y | Y | Y | Y | ~ | . | . | . | Y | . | . | . | ~ | . |
| `raeth2026decisionskill` | CRITICAL | . | . | . | . | . | . | . | . | . | . | . | ~ | Y | . | . | . | . | . | . |
| `rossa2026actionbed` | CRITICAL | . | . | . | . | . | . | . | . | . | . | . | . | Y | . | Y | Y | . | . | . |
| `sun2025decisionfocusedsensing` | CRITICAL | . | . | . | . | . | . | . | . | ~ | . | . | . | Y | Y | Y | Y | . | Y | . |
| `alexander2026nursing` | HIGH | . | ~ | . | . | . | Y | Y | Y | Y | . | . | . | ~ | Y | . | . | . | ~ | . |
| `ardid2026forecastvalue` | HIGH | . | . | . | . | . | . | . | . | . | . | . | ~ | Y | . | . | . | . | Y | . |
| `berlinghieri2024pm25` | HIGH | . | . | . | . | . | . | . | . | . | . | . | ~ | Y | . | . | . | . | Y | . |
| `bischiniotis2019tradeoffs` | HIGH | . | . | . | . | . | . | . | . | . | . | Y | Y | Y | . | . | . | . | . | . |
| `bouttier2024optimal` | HIGH | . | . | . | Y | . | . | . | . | . | . | . | Y | Y | . | . | . | . | . | . |
| `chen1987qualityvalue` | HIGH | . | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . | . | . |
| `dayan2026conformal` | HIGH | Y | . | . | Y | Y | . | . | . | ~ | . | . | ~ | ~ | ~ | . | . | . | ~ | . |
| `dennison2007wuivac` | HIGH | Y | . | . | . | . | . | . | . | Y | . | . | . | ~ | . | . | . | . | . | . |
| `flores2023goal` | HIGH | . | . | . | . | . | Y | Y | Y | Y | . | . | . | . | Y | . | . | . | ~ | . |
| `georgakakos2025evacuationtiming` | HIGH | . | . | . | Y | . | . | . | . | Y | . | Y | ~ | Y | . | . | . | . | . | Y |
| `kalogeropoulos2022kperil` | HIGH | Y | . | . | Y | . | . | . | . | Y | . | . | . | . | . | . | . | . | . | . |
| `kwon2025koreaevac` | HIGH | . | ~ | . | . | . | . | . | . | Y | . | . | . | . | Y | . | . | Y | . | . |
| `larsen2011cedar` | HIGH | Y | . | . | . | . | . | . | . | Y | . | . | . | ~ | . | . | . | . | ~ | . |
| `li2015household` | HIGH | Y | . | Y | . | . | . | . | . | Y | . | . | . | ~ | ~ | . | . | . | . | . |
| `liu2026dflfail` | HIGH | . | . | . | . | . | . | . | . | . | . | . | . | Y | . | ~ | . | . | . | . |
| `lopez2020bridging` | HIGH | . | . | . | Y | . | . | . | . | . | . | Y | Y | Y | . | . | . | . | . | . |
| `lu2026lahaina` | HIGH | . | Y | . | . | . | . | ~ | . | Y | . | . | . | . | ~ | . | . | . | ~ | . |
| `ma2025damaged` | HIGH | Y | Y | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . | . | . |
| `malings2018voispatiotemporal` | HIGH | . | . | . | . | . | . | . | . | . | . | . | . | Y | . | Y | Y | . | . | . |
| `mitchell2023peril` | HIGH | Y | . | . | . | . | . | . | . | Y | . | . | . | ~ | . | . | . | . | ~ | . |
| `mois2025evacuationstages` | HIGH | Y | . | ~ | . | . | ~ | . | . | Y | . | . | . | . | . | . | . | Y | . | . |
| `mois2026aievacroute` | HIGH | Y | ? | . | ? | ? | . | Y | . | Y | . | . | . | . | ? | . | ~ | Y | ? | . |
| `murphy1987accuracyvalue` | HIGH | . | . | . | . | . | . | . | . | . | . | . | ~ | Y | . | . | . | . | . | . |
| `orphanoudakis2025mora` | HIGH | ~ | . | . | . | . | . | ~ | . | . | . | . | . | ~ | Y | . | . | . | . | . |
| `papaioannou2026adaptive` | HIGH | Y | . | . | . | . | . | . | . | . | . | ~ | . | . | ~ | Y | Y | . | . | . |
| `rambha2021staged` | HIGH | . | Y | . | Y | . | Y | ~ | ~ | Y | ~ | . | . | Y | ~ | ~ | . | . | ~ | . |
| `ramirez2019stochastic` | HIGH | Y | . | Y | Y | . | . | . | . | Y | . | ~ | . | ~ | . | . | . | . | ~ | . |
| `regnier2006dynamic` | HIGH | . | . | . | . | . | . | . | . | . | . | ~ | ~ | Y | . | . | . | . | . | . |
| `regnier2008public` | HIGH | . | . | . | . | . | . | . | . | ~ | . | ~ | Y | Y | . | . | . | . | . | . |
| `roysingh2025constellation` | HIGH | Y | . | . | . | . | . | . | . | . | . | Y | . | . | Y | ~ | Y | . | ~ | . |
| `shahparvari2017robust` | HIGH | . | . | . | . | . | Y | Y | Y | Y | . | . | . | . | Y | . | . | . | ~ | . |
| `shao2026beliefaware` | HIGH | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | ~ | Y | . | . | Y |
| `tang2025transit` | HIGH | . | Y | . | . | . | Y | Y | Y | Y | . | . | . | . | Y | . | . | . | . | . |
| `wahlqvist2021wuinity` | HIGH | Y | Y | . | . | . | . | . | . | Y | . | . | . | ~ | . | . | . | . | . | . |
| `wu2025denkf` | HIGH | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y |
| `yu2020disruption` | HIGH | . | ~ | . | . | . | ~ | Y | . | . | . | . | . | ~ | ~ | . | . | . | Y | . |
| `zha2024distributed` | HIGH | Y | . | . | . | . | . | . | . | . | . | Y | . | . | ~ | ~ | ~ | . | . | Y |
| `abbasi2015vehicle` | MODERATE | ~ | . | . | . | . | Y | Y | ~ | Y | . | . | . | . | Y | . | . | . | ~ | . |
| `allaire2020ensemble` | MODERATE | Y | . | . | ~ | . | . | . | . | . | . | ~ | ~ | . | . | . | . | . | Y | . |
| `an2026donghae` | MODERATE | . | . | . | . | . | ~ | . | . | Y | . | . | . | . | . | . | . | Y | Y | . |
| `bailonruiz2022uavfleet` | MODERATE | Y | . | . | . | . | . | . | . | . | . | ~ | . | . | ~ | ~ | Y | . | ~ | . |
| `braydwood2026quantum` | MODERATE | . | . | . | . | . | . | . | . | . | . | Y | . | . | Y | . | Y | . | . | . |
| `chang2024stochastic` | MODERATE | . | Y | . | . | . | Y | Y | Y | Y | . | . | . | ~ | Y | . | . | . | ~ | . |
| `chang2026multiscale` | MODERATE | Y | Y | ~ | . | . | . | . | ~ | Y | . | ~ | . | ~ | . | . | . | ~ | ~ | . |
| `cova2011shelter` | MODERATE | ~ | . | . | . | . | . | . | . | Y | . | . | . | Y | . | . | . | . | . | . |
| `dubois2022capacitated` | MODERATE | . | . | . | . | . | Y | Y | ~ | ~ | . | . | . | ~ | Y | . | . | . | ~ | . |
| `ebrahimnejad2021disability` | MODERATE | ? | ? | . | ? | . | Y | ? | ? | ? | ? | . | . | ? | ? | . | . | . | ? | . |
| `flores2020supported` | MODERATE | . | . | . | . | . | Y | Y | Y | Y | . | . | . | . | Y | . | . | . | . | . |
| `fryer2013entrapment` | MODERATE | Y | . | . | . | . | . | . | . | Y | . | . | . | ~ | . | . | . | . | . | . |
| `grajdura2022fastmoving` | MODERATE | ~ | Y | Y | . | . | . | . | . | Y | . | ~ | . | . | ~ | . | . | . | Y | . |
| `gwynne2023roxborough` | MODERATE | . | Y | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . | Y | . |
| `hope2024wildfiresat` | MODERATE | . | . | . | . | . | . | . | . | . | . | . | . | Y | . | Y | . | . | . | . |
| `kim2024directional` | MODERATE | Y | Y | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . | . | . |
| `kwak2021evacroute` | MODERATE | ~ | . | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | Y | . | . |
| `masiwal2026decisionoriented` | MODERATE | . | . | . | . | . | . | . | . | . | . | ~ | Y | Y | . | . | . | . | Y | . |
| `mendes2024robustsuppression` | MODERATE | Y | . | . | ~ | . | . | ~ | . | . | . | . | . | . | Y | . | . | . | . | . |
| `nifos2018evacsystem` | MODERATE | ~ | . | . | . | . | ~ | . | . | ~ | . | . | . | . | . | . | ~ | Y | ? | . |
| `olivetti2026compounding` | MODERATE | . | . | . | . | . | . | . | . | . | . | . | Y | Y | . | . | . | . | . | . |
| `rodriguezfernandez2025mcda` | MODERATE | ~ | . | . | . | . | . | . | . | . | . | . | . | ~ | Y | . | . | . | . | . |
| `sevim2025savrural` | MODERATE | ? | Y | ? | . | . | Y | Y | Y | Y | ? | . | . | ? | Y | . | . | . | ? | . |
| `shahparvari2016enhancing` | MODERATE | ~ | . | . | . | . | Y | Y | ~ | Y | . | . | . | ~ | Y | . | . | . | ~ | . |
| `shahparvari2017possibilistic` | MODERATE | ? | ? | . | ~ | . | Y | ? | ? | Y | ? | . | . | ? | Y | . | . | . | ~ | . |
| `shahparvari2019fleet` | MODERATE | . | . | . | . | . | Y | Y | Y | Y | . | . | . | . | Y | . | . | . | . | . |
| `siam2022interdisciplinary` | MODERATE | ~ | Y | . | . | . | ~ | . | . | Y | . | . | . | ~ | . | . | . | . | . | . |
| `simon2022wildfirevoi` | MODERATE | . | . | . | . | . | . | . | . | . | . | . | . | Y | ~ | Y | . | . | . | . |
| `stephenson2025extremeloss` | MODERATE | . | . | . | . | . | . | . | . | . | . | . | Y | Y | . | . | . | . | . | . |
| `sung2025geostationary` | MODERATE | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . | ~ | Y | Y | . |
| `verkade2011estimating` | MODERATE | . | . | . | Y | . | . | . | . | . | . | . | Y | Y | . | . | . | . | . | . |
| `xu2022multiparking` | MODERATE | . | . | . | . | . | Y | Y | Y | Y | . | . | . | ~ | Y | . | . | . | . | . |
| `xu2026wildfirefm` | MODERATE | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | . |
| `zhao2020roundtrip` | MODERATE | . | . | . | . | . | Y | Y | Y | Y | . | . | . | . | Y | . | . | . | . | . |
| `zhu2002economic` | MODERATE | . | . | . | ~ | . | . | . | . | . | . | . | Y | Y | . | . | . | . | . | . |
| `borgwardt2024evacuation` | LOW | Y | ~ | . | . | . | . | . | . | Y | . | ~ | . | . | . | . | . | . | ~ | . |
| `choi2026ridgeline` | LOW | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | Y | . |
| `frisvold2024demandinfo` | LOW | . | . | . | . | . | . | . | . | . | . | . | . | . | . | ~ | . | . | . | . |
| `gu2016spreadalgorithm` | LOW | Y | . | . | . | . | . | . | . | ~ | . | . | . | . | ~ | . | Y | Y | ? | . |
| `han2026dangerrating` | LOW | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | . | . |
| `heo2026vulnerability` | LOW | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | ~ | . |
| `janfeshanaraghi2025silverado` | LOW | . | Y | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . | Y | . |
| `li2017reversegeocoding` | LOW | Y | . | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . | . | . |
| `macleod2021anticipatory` | LOW | . | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . | . | . |
| `nifos2026kfdrs` | LOW | ~ | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | ~ | . |
| `sun2024kincade` | LOW | . | ? | ? | . | . | ~ | . | . | Y | . | . | . | . | . | . | . | . | Y | . |
| `xu2026wildfirescoring` | LOW | . | . | . | . | . | . | . | . | . | . | . | . | ? | . | . | . | . | . | . |
| `allaire2021emulation` | BACKGROUND | Y | . | . | . | . | . | . | . | . | . | Y | ~ | . | . | . | . | . | . | . |
| `andrews2018rothermel` | BACKGROUND | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `arnold1986osse` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y |
| `atlas1997observations` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y |
| `averill2007emergencyresponse` | BACKGROUND | . | . | . | . | . | . | Y | . | Y | . | . | . | . | . | . | . | . | . | . |
| `axtell1996aligning` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `bennett2026wise` | BACKGROUND | Y | . | . | . | . | . | . | . | . | . | . | ~ | . | . | . | . | . | Y | . |
| `bish2011planning` | BACKGROUND | . | . | . | . | . | Y | Y | Y | Y | . | . | . | . | Y | . | . | . | . | . |
| `cameron2008clusterbootstrap` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `cameron2015clusterrobust` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `cheng2022surrogate` | BACKGROUND | Y | . | . | . | . | . | . | . | . | . | Y | ~ | . | . | . | . | . | Y | . |
| `cruz2013uncertainty` | BACKGROUND | Y | . | . | . | Y | . | . | . | . | . | . | ~ | . | . | . | . | . | Y | . |
| `dacrema2019progress` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `elmachtoub2022smartpredict` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | ? | . | . | . | . | . | . |
| `elmfire2025validation` | BACKGROUND | Y | . | . | . | Y | . | . | . | . | . | . | . | . | . | . | . | . | Y | . |
| `errico2013osse` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y |
| `finney1998farsite` | BACKGROUND | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | ~ | . |
| `giglio2016modis` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | ~ | . | . | . | . | . | . | Y | . |
| `gneiting2007scoring` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | ? | . | . | . | . | . | . |
| `hall2023geostationary` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . | . | . | Y | . |
| `halliwell2014fraternal` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y |
| `henderson2016inversecrime` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | ? |
| `hoffman2016osse` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y |
| `hurlbert1984pseudoreplication` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `kaipio2007inversecrime` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | ? |
| `kunsch1989blockbootstrap` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `lakens2017equivalence` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `lakens2018equivalence` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `lautenberger2013elmfire` | BACKGROUND | Y | . | . | ~ | . | . | . | . | . | . | . | . | . | . | . | . | . | ~ | . |
| `lazic2018pseudoreplication` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `linn2002firetec` | BACKGROUND | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `mandel2014wrfsfire` | BACKGROUND | Y | . | . | . | . | . | . | . | . | . | ~ | . | . | . | . | . | . | ~ | . |
| `mandi2024dfl` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | ? | . | . | . | . | . | . |
| `matsuo2025evacuation` | BACKGROUND | . | . | . | . | . | ~ | . | . | . | . | . | . | . | . | . | . | . | Y | . |
| `miller2015spark` | BACKGROUND | Y | . | . | ~ | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `morris2019simulation` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `nasafirms2026latency` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . | . | . | . | . |
| `oreskes1994verification` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `ovadia2019shift` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `paugam2026mtgfci` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . | . | . | Y | . |
| `prive2023robustness` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y |
| `ronchi2023verification` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | ? | . |
| `rothermel1972spread` | BACKGROUND | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | ~ | . |
| `sargent2013verification` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `schroeder2014viirs` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | ~ | . | . | . | . | . | . | Y | . |
| `siepe2024preregistration` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `tibshirani2019conformalshift` | BACKGROUND | . | . | . | ? | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `weise2016chaparral` | BACKGROUND | Y | . | . | . | Y | . | . | . | . | . | . | ~ | . | . | . | . | . | Y | . |
| `williams2024reporting` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `wirgin2004inversecrime` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | ? |
| `yu2019twin` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | . | . | ? | . | . | . | Y |
| `zehra2024systematic` | BACKGROUND | . | ~ | . | . | . | ~ | ? | . | Y | . | . | . | . | . | . | . | . | . | . |
| `zeng2020osse` | BACKGROUND | . | . | . | . | . | . | . | . | . | . | . | . | ? | . | . | . | . | . | Y |
| `zhang2023karst` | BACKGROUND | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| `an2008slope` | NONE | ~ | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | ~ | . |
| `choi2025gee` | NONE | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | ~ | . |
| `kang2020hfri` | NONE | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | ~ | . |
| `kfs2025majorfires` | NONE | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | ? | . |
| `kfs2026statistics` | NONE | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | ? | . |
| `lee2021crownfuel` | NONE | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | ~ | . |
| `lee2026occurrence` | NONE | . | . | . | . | . | . | . | . | . | . | . | . | . | ~ | . | . | Y | ~ | . |
| `lim2022fueldanger` | NONE | ~ | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | ~ | . |
| `lim2025fwi` | NONE | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | ~ | . |
| `murphy1977costloss` | HIGH (framework ownership) | . | . | . | . | . | . | . | . | . | . | . | ~ | Y | . | . | . | . | . | . |
| `murphy1994assessing` | MODERATE (review/ownership) | . | . | . | . | . | . | . | . | . | . | . | . | Y | . | . | . | . | . | . |
| `palmer1998singular` | HIGH (framework ownership) | . | . | . | . | . | . | . | . | . | . | . | . | . | . | ~ | Y | . | . | . |
| `park2025drivers` | NONE | ~ | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | ~ | . |
| `rainforth2024modernbed` | HIGH (field ownership) | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | Y | . | . | . |
| `richardson2000relative` | HIGH (framework ownership) | . | . | . | ~ | . | . | . | . | . | . | . | Y | Y | . | . | . | . | . | . |
| `veiga2023activesensing` | HIGH (field ownership) | . | . | . | . | . | . | . | . | . | . | . | . | . | . | Y | Y | . | . | . |

---

## Column occupancy

| Column | Y | ~ | . | Reading |
|---|---|---|---|---|
| future fire | 46 | 14 | 102 | heavily occupied |
| traffic | 15 | 6 | 140 | heavily occupied |
| household trigger | 3 | 2 | 158 | occupied |
| prob. trigger | 12 | 7 | 143 | heavily occupied |
| multi fire models | 5 | 0 | 159 | heavily occupied |
| assisted evac | 19 | 8 | 138 | heavily occupied |
| inbound responder | 19 | 4 | 139 | heavily occupied |
| pickup | 12 | 6 | 145 | heavily occupied |
| egress | 50 | 6 | 108 | heavily occupied |
| dispatch-by deadline | 0 | 2 | 160 | sparse -- investigate whether this is genuinely open or merely unsearched |
| forecast latency | 12 | 13 | 140 | heavily occupied |
| skill boundary | 10 | 14 | 141 | heavily occupied |
| decision value | 31 | 21 | 105 | heavily occupied |
| scarce resources | 23 | 13 | 127 | heavily occupied |
| VOI | 9 | 8 | 147 | heavily occupied |
| active sensing | 13 | 4 | 148 | heavily occupied |
| Korean setting | 22 | 1 | 142 | heavily occupied |
| real validation | 25 | 35 | 97 | heavily occupied |
| OSSE | 12 | 0 | 150 | heavily occupied |

*165 papers recorded.*
