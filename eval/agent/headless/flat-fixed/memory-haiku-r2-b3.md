## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. They reach it through feat-cr-ivr-path-v1 and the cr-lgbm and cr-logreg model line.
Notes: work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-cost-matrix.md, work/dec-cr-pilot.md

## Q2
The note in force is cli-xgb-v3, a two-model T-learner uplift model. It is built on exp-106-credit-line-increase, exp-107-credit-line-increase and find-cli-uplift-wins.
Notes: work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls, directly through feat-cr-caller-history-v1 and feat-cr-transcript-tfidf-v1, and ds-cr-ivr-paths, through feat-cr-ivr-path-v1.
Notes: work/cr-lgbm-v1.md, work/ds-cr-calls.md, work/ds-cr-ivr-paths.md

## Q4
fraud25-gbm-v1 and fraud25-gbm-v2 both build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. v2 also adds feat-f25-mcc-travel, which v1 does not use.
Notes: work/fraud25-gbm-v1.md, work/fraud25-gbm-v2.md, work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. The chain is not fully closed, since dec-xs-retrain-quarterly may also rest on it, but the note never names a link that would confirm it.
Notes: work/dec-cb-adopt-banded-tiers.md, work/dec-cb-extend-flat-pilot.md, work/dec-cb-threshold-2500.md

## Q6
The note in force is disp-lgbm-v3, which adds the fraud-2026 score. It is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307-dispute-triage and feat-disp-fraud-score.
Notes: work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/disp-lgbm-v2.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q7
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4, directly, and ds-cb-spend-panel, which it reaches through feat-cb-spend-base.
Notes: work/cb-elasticity-v1.md, work/ds-cb-pilot-2025q4.md, work/ds-cb-spend-panel.md

## Q8
mq3-response-gbm-v1 and mq3-uplift-tlearner-v1 both build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1.
Notes: work/mq3-response-gbm-v1.md, work/mq3-uplift-tlearner-v1.md, work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md

## Q9
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h through other notes.
Notes: work/dec-cb-metric-24h.md, work/dec-cb-rollout-60.md, work/dec-cb-handoff-v2.md, work/dec-cb-metric-48h.md

## Q10
The note in force is ed-gbm-v3, the v2 model plus the bureau 6-month slope. It is built on ed-gbm-v2, exp-207-early-delinquency and feat-ed-bureau-slope-v1.
Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md