## Q1
bt-xgb-v3 is the note in force at the end of the bt-xgb-v1 → v2 → v3 line; it replaced the depth-5 xgboost model (bt-xgb-v2) and is built on bt-xgb-v2, dec-bt-margin-label and the margin-weighted label experiment (exp-107-margin-label).
Notes: work/bt-xgb-v1.md, work/bt-xgb-v2.md, work/bt-xgb-v3.md, work/dec-bt-margin-label.md, work/exp-107-margin-label.md

## Q2
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily (via feat-ae-active-days-v1 and feat-ae-depth-v1) and ds-ae-push-log (via feat-ae-push-open-v1). ds-ae-push-log itself builds on the daily sessions table, so ds-ae-sessions-daily is the root of both branches.
Notes: work/ae-score-v1.md, work/feat-ae-active-days-v1.md, work/feat-ae-depth-v1.md, work/feat-ae-push-open-v1.md, work/ds-ae-sessions-daily.md, work/ds-ae-push-log.md

## Q3
The two notes share feat-c25-payment-behaviour (payment ratio and late counts) and feat-c25-txn-recency (days since last card transaction). The other inputs differ: churn-lr-base-2025 uses the 2024 holdout, app sessions and the old util-v1, while churn-gbm-2025-v2 uses util-v2 and the dropped-app-sessions decision.
Notes: work/churn-gbm-2025-v2.md, work/churn-lr-base-2025.md, work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md

## Q4
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3 (directly, via app-scorecard-v3), dec-app-no-gbm (via exp-503 and exp-504, both built on app-scorecard-v3 or app-gbm-v1), dec-app-rebuild-v4 (via app-gbm-v2 and find-app-gini-v3-drift), and dec-app-cutoff-v4 (via app-scorecard-v4, which is built on app-gbm-v2). The link from feat-app-util-new to app-scorecard-v3 is inferred from app-scorecard-v3's "external card utilisation feature at application" wording, because no note names feat-app-util-new in a Builds-on line.
Notes: work/dec-app-cutoff-v3.md, work/dec-app-cutoff-v4.md, work/dec-app-no-gbm.md, work/dec-app-rebuild-v4.md, work/feat-app-util-new.md, work/app-scorecard-v3.md, work/app-gbm-v1.md, work/app-gbm-v2.md, work/app-scorecard-v4.md, work/exp-503-application-scorecard.md, work/exp-504-application-scorecard.md, work/exp-506-application-scorecard.md, work/exp-507-application-scorecard.md, work/find-app-gini-v3-drift.md, work/find-app-income-lift.md

## Q5
cr-lgbm-v3 is the note in force at the end of the cr-lgbm-v1 → v2 → v3 line; it is built on cr-lgbm-v2, exp-106-call-center-routing, ds-cr-intent-labels and the cost-matrix finding fnd-cr-threshold.
Notes: work/cr-lgbm-v1.md, work/cr-lgbm-v2.md, work/cr-lgbm-v3.md, work/exp-106-call-center-routing.md, work/ds-cr-intent-labels.md, work/fnd-cr-threshold.md