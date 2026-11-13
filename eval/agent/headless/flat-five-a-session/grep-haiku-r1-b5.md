## Q1
Four decision notes rest on ds-cr-ivr-paths, directly or through the chain built on it: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. They reach it through feat-cr-ivr-path-v1, cr-lgbm-v1, cr-lgbm-v3 and fnd-cr-leak-corrected.
Notes: work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-cost-matrix.md, work/dec-cr-pilot.md

## Q2
The note in force at the end of the line is cli-xgb-v3, which replaced cli-xgb-v2 (itself a replacement for cli-xgb-v1). cli-xgb-v3 is built on exp-106-credit-line-increase (the out-of-time AUC check for v2), exp-107-credit-line-increase (which confirms the T-learner) and find-cli-uplift-wins (uplift beats propensity).
Notes: work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-ivr-paths directly, via feat-cr-ivr-path-v1, and ds-cr-calls, which it reaches through the caller-history and related feature notes.
Notes: work/ds-cr-ivr-paths.md, work/ds-cr-calls.md

## Q4
fraud25-gbm-v1 and fraud25-gbm-v2 both build directly on four feature notes: feat-f25-velocity-v1, feat-f25-amt-ratio, feat-f25-device-age and feat-f25-hour-band. The fraud label arrival lag is shared too, but it is a dataset note (ds-f25-labels), not a feature note, so I have left it out of the list.
Notes: work/feat-f25-velocity-v1.md, work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md

## Q5
Three decision notes rest on ds-cb-spend-panel: dec-cb-extend-flat-pilot, dec-cb-adopt-banded-tiers and dec-cb-threshold-2500. The last two come through the elasticity and break-even chain, and the flat-pilot decision comes through find-cb-flat-wins and exp-201.
Notes: work/dec-cb-extend-flat-pilot.md, work/dec-cb-adopt-banded-tiers.md, work/dec-cb-threshold-2500.md