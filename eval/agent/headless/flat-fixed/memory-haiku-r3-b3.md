## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. They reach it through feat-cr-ivr-path-v1 and the cr-lgbm and exp-10x chain.
Notes: work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-cost-matrix.md, work/dec-cr-pilot.md

## Q2
cli-xgb-v1 was superseded by cli-xgb-v2, which was superseded by cli-xgb-v3. cli-xgb-v3 is in force and is built on exp-106-credit-line-increase, exp-107-credit-line-increase and find-cli-uplift-wins.
Notes: work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls directly (through feat-cr-caller-history-v1 and feat-cr-transcript-tfidf-v1) and ds-cr-ivr-paths (through feat-cr-ivr-path-v1).
Notes: work/cr-lgbm-v1.md, work/ds-cr-calls.md, work/ds-cr-ivr-paths.md

## Q4
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1.
Notes: work/fraud25-gbm-v1.md, work/fraud25-gbm-v2.md, work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. They reach it through the cb-elasticity, feat-cb and exp-20x chain.
Notes: work/dec-cb-adopt-banded-tiers.md, work/dec-cb-extend-flat-pilot.md, work/dec-cb-threshold-2500.md

## Q6
disp-lgbm-v1 was superseded by disp-lgbm-v2, which was superseded by disp-lgbm-v3. disp-lgbm-v3 is in force and is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307-dispute-triage and feat-disp-fraud-score.
Notes: work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/disp-lgbm-v2.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q7
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel through feat-cb-spend-base.
Notes: work/cb-elasticity-v1.md, work/ds-cb-pilot-2025q4.md, work/ds-cb-spend-panel.md

## Q8
Both mq3-response-gbm-v1 and mq3-uplift-tlearner-v1 build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1.
Notes: work/mq3-response-gbm-v1.md, work/mq3-uplift-tlearner-v1.md, work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md

## Q9
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h through other notes.
Notes: work/dec-cb-metric-24h.md, work/dec-cb-rollout-60.md, work/dec-cb-handoff-v2.md, work/dec-cb-metric-48h.md

## Q10
ed-gbm-v1 was superseded by ed-gbm-v2, which was superseded by ed-gbm-v3. ed-gbm-v3 is in force and is built on ed-gbm-v2, exp-207-early-delinquency and feat-ed-bureau-slope-v1.
Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md