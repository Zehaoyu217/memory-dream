## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm directly through the IVR path feature and cr-lgbm-v1, and dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot through the same chain. Some notes in the folder name links the tool could not place, so this may not be the full list.
Notes: work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-cost-matrix.md, work/dec-cr-pilot.md

## Q2
The note in force at the end of the cli-xgb-v1 line is cli-xgb-v3, a two-model uplift model that replaces cli-xgb-v2. cli-xgb-v3 builds on exp-106-credit-line-increase, exp-107-credit-line-increase and find-cli-uplift-wins, plus an out-of-time AUC check for v2 that no note records.
Notes: work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls directly through feat-cr-caller-history-v1 and cr-logreg-v1, and ds-cr-ivr-paths directly through feat-cr-ivr-path-v1.
Notes: work/ds-cr-calls.md, work/ds-cr-ivr-paths.md

## Q4
fraud25-gbm-v1 and fraud25-gbm-v2 both build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1.
Notes: work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500, all through the chain of cb-elasticity, experiment and finding notes built on it. As in Q1, some notes name links the tool could not place, so this may not be complete.
Notes: work/dec-cb-adopt-banded-tiers.md, work/dec-cb-extend-flat-pilot.md, work/dec-cb-threshold-2500.md