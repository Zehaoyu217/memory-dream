## Q1
bt-xgb-v1 was replaced by bt-xgb-v2, which was replaced by bt-xgb-v3, the note in force from 2026-03-01. bt-xgb-v3 is built on the depth-5 xgboost model (bt-xgb-v2), dec-bt-margin-label and the margin-weighted label experiment (exp-107-margin-label).
Notes: work/bt-xgb-v1.md, work/bt-xgb-v2.md, work/bt-xgb-v3.md, work/dec-bt-margin-label.md, work/exp-107-margin-label.md

## Q2
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily, through the active-days feature and the depth v1 feature, and ds-ae-push-log, through the push open rate feature. The push log note itself builds on the daily sessions table, so ds-ae-sessions-daily is the only root.
Notes: work/ae-score-v1.md, work/feat-ae-active-days-v1.md, work/feat-ae-depth-v1.md, work/feat-ae-push-open-v1.md, work/ds-ae-push-log.md, work/ds-ae-sessions-daily.md

## Q3
Both notes build directly on feat-c25-payment-behaviour (payment ratio and late counts) and feat-c25-txn-recency (days since last card transaction).
Notes: work/churn-gbm-2025-v2.md, work/churn-lr-base-2025.md, work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md

## Q4
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3 directly (via app-scorecard-v3), and dec-app-no-gbm (via app-gbm-v1), dec-app-rebuild-v4 (via app-gbm-v2 and find-app-gini-v3-drift) and dec-app-cutoff-v4 (via app-scorecard-v4 and exp-507, both resting on app-gbm-v2 → app-gbm-v1 → app-scorecard-v3) through the chain of notes they were built on.
Notes: work/feat-app-util-new.md, work/app-scorecard-v3.md, work/app-gbm-v1.md, work/app-gbm-v2.md, work/app-scorecard-v4.md, work/exp-507-application-scorecard.md, work/find-app-gini-v3-drift.md, work/dec-app-cutoff-v3.md, work/dec-app-no-gbm.md, work/dec-app-rebuild-v4.md, work/dec-app-cutoff-v4.md

## Q5
cr-lgbm-v1 was replaced by cr-lgbm-v2, which was replaced by cr-lgbm-v3, the current router. cr-lgbm-v3 is built on cr-lgbm-v2, ds-cr-intent-labels (adjudicated labels), exp-106-call-center-routing and the cost-matrix misroute finding (fnd-cr-threshold).
Notes: work/cr-lgbm-v1.md, work/cr-lgbm-v2.md, work/cr-lgbm-v3.md, work/ds-cr-intent-labels.md, work/exp-106-call-center-routing.md, work/fnd-cr-threshold.md