## Q1
Four decision notes rest on ds-cr-ivr-paths. dec-cr-lgbm rests on it through cr-lgbm-v1 and cr-logreg-v1. dec-cr-caller-v2 rests on it through fnd-cr-leak-corrected, exp-104 and cr-lgbm-v1. dec-cr-pilot and dec-cr-cost-matrix rest on it through cr-lgbm-v3, cr-lgbm-v2, exp-105 and cr-lgbm-v1.
Notes: work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-pilot.md, work/dec-cr-cost-matrix.md

## Q2
cli-xgb-v3 is the model in force at the end of the line, and nothing in the notes replaces it. It builds on exp-106-credit-line-increase (the out-of-time check of v2), exp-107-credit-line-increase and find-cli-uplift-wins.
Notes: work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes. ds-cr-ivr-paths comes in through feat-cr-ivr-path-v1, and ds-cr-calls comes in through feat-cr-caller-history-v1 and feat-cr-transcript-tfidf-v1.
Notes: work/ds-cr-ivr-paths.md, work/ds-cr-calls.md

## Q4
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on the same four feature notes: the amount-to-median ratio, device age, authorisation hour band and velocity v1.
Notes: work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decision notes rest on ds-cb-spend-panel. dec-cb-adopt-banded-tiers gets it through cb-elasticity-v2 and feat-cb-spend-base. dec-cb-threshold-2500 gets it through dec-cb-adopt-banded-tiers. dec-cb-extend-flat-pilot gets it through find-cb-flat-wins, cb-elasticity-v1 and feat-cb-spend-base.
Notes: work/dec-cb-adopt-banded-tiers.md, work/dec-cb-threshold-2500.md, work/dec-cb-extend-flat-pilot.md