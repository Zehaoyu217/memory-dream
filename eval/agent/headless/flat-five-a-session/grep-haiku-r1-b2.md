## Q1
bt-xgb-v3 is the note in force, since nothing replaces it. It is built on bt-xgb-v2 (the depth-5 model that replaced v1), dec-bt-margin-label and exp-107-margin-label.
Notes: work/bt-xgb-v3.md, work/bt-xgb-v2.md, work/dec-bt-margin-label.md, work/exp-107-margin-label.md

## Q2
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily, via feat-ae-active-days-v1 and feat-ae-depth-v1, and ds-ae-push-log, via feat-ae-push-open-v1.
Notes: work/ae-score-v1.md, work/feat-ae-active-days-v1.md, work/feat-ae-depth-v1.md, work/feat-ae-push-open-v1.md, work/ds-ae-sessions-daily.md, work/ds-ae-push-log.md

## Q3
The two feature notes both churn-gbm-2025-v2 and churn-lr-base-2025 build on directly are feat-c25-payment-behaviour and feat-c25-txn-recency.
Notes: work/churn-gbm-2025-v2.md, work/churn-lr-base-2025.md, work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md

## Q4
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3 directly on app-scorecard-v3, dec-app-no-gbm via exp-503 and exp-504 back to app-gbm-v1, dec-app-rebuild-v4 via find-app-gini-v3-drift and app-gbm-v2, and dec-app-cutoff-v4 via app-scorecard-v4, find-app-income-lift and exp-507.
Notes: work/feat-app-util-new.md, work/app-scorecard-v3.md, work/app-gbm-v1.md, work/app-gbm-v2.md, work/app-scorecard-v4.md, work/exp-503-application-scorecard.md, work/exp-504-application-scorecard.md, work/exp-506-application-scorecard.md, work/exp-507-application-scorecard.md, work/find-app-gini-v3-drift.md, work/find-app-income-lift.md, work/dec-app-cutoff-v3.md, work/dec-app-no-gbm.md, work/dec-app-rebuild-v4.md, work/dec-app-cutoff-v4.md

## Q5
cr-lgbm-v3 is the note in force, since nothing replaces it. It is built on cr-lgbm-v2, ds-cr-intent-labels, exp-106-call-center-routing and fnd-cr-threshold.
Notes: work/cr-lgbm-v3.md, work/cr-lgbm-v2.md, work/ds-cr-intent-labels.md, work/exp-106-call-center-routing.md, work/fnd-cr-threshold.md