## Q1
Four decision notes rest on ds-cr-ivr-paths. dec-cr-lgbm does so through feat-cr-ivr-path-v1 and cr-lgbm-v1, and dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot do so through the notes built on those.
Notes: work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-cost-matrix.md, work/dec-cr-pilot.md

## Q2
cli-xgb-v3 is in force. It builds on exp-106-credit-line-increase, exp-107-credit-line-increase and find-cli-uplift-wins, and also on an out-of-time AUC check for v2 that the memory does not link to a note.
Notes: work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls (via feat-cr-caller-history-v1 and feat-cr-transcript-tfidf-v1) and ds-cr-ivr-paths (via feat-cr-ivr-path-v1).
Notes: work/ds-cr-calls.md, work/ds-cr-ivr-paths.md

## Q4
Both build directly on feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. fraud25-gbm-v2 also builds directly on feat-f25-mcc-travel.
Notes: work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. The memory's dependency chain reaches 27 notes in total.
Notes: work/dec-cb-adopt-banded-tiers.md, work/dec-cb-extend-flat-pilot.md, work/dec-cb-threshold-2500.md