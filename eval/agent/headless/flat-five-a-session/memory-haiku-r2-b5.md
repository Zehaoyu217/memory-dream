## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. They reach it through feat-cr-ivr-path-v1, which was built on ds-cr-ivr-paths.
Notes: work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-cost-matrix.md, work/dec-cr-pilot.md

## Q2
cli-xgb-v1 was replaced by cli-xgb-v2, which was replaced by cli-xgb-v3, so cli-xgb-v3 is in force. It builds on exp-106-credit-line-increase, exp-107-credit-line-increase and find-cli-uplift-wins. Its note also cites an out-of-time AUC check for v2 that has no note of its own.
Notes: work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls, through feat-cr-caller-history-v1 and feat-cr-transcript-tfidf-v1, and ds-cr-ivr-paths, through feat-cr-ivr-path-v1.
Notes: work/ds-cr-calls.md, work/ds-cr-ivr-paths.md

## Q4
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. Note that feat-f25-amt-ratio is superseded by feat-f26-amt-zscore.
Notes: work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. Each reaches it through the dataset and feature notes built on it, 27 notes in all.
Notes: work/dec-cb-adopt-banded-tiers.md, work/dec-cb-extend-flat-pilot.md, work/dec-cb-threshold-2500.md