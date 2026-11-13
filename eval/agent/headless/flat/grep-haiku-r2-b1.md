## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-suppress-018, dec-aml-sample-10 and dec-aml-ranker-v3. They reach it through the dispositions dataset, aml-xgb-v1, exp-401, exp-405, feat-aml-kyc-band and ds-aml-oot.
Notes: work/dec-aml-queue-only.md, work/dec-aml-suppress-018.md, work/dec-aml-sample-10.md, work/dec-aml-ranker-v3.md, work/ds-aml-dispositions.md, work/ds-aml-oot.md, work/exp-405-aml-alerts.md, work/aml-find-fp-baseline.md, work/aml-xgb-v3.md

## Q2
The note in force at the end of the aml-xgb-v1 line is aml-xgb-v3, which replaced aml-xgb-v2. It builds on aml-xgb-v2, ds-aml-oot, exp-405-aml-alerts and exp-407-aml-alerts.
Notes: work/aml-xgb-v1.md, work/aml-xgb-v2.md, work/aml-xgb-v3.md

## Q3
aml-xgb-v1 rests on the dataset notes ds-aml-dispositions, ds-aml-alerts and ds-aml-cash-txn. The first two come through the analyst dispositions dataset, and ds-aml-cash-txn comes through feat-aml-new-counterparty and feat-aml-structuring-v1.
Notes: work/aml-xgb-v1.md, work/ds-aml-dispositions.md, work/ds-aml-alerts.md, work/ds-aml-cash-txn.md, work/feat-aml-new-counterparty.md, work/feat-aml-structuring-v1.md

## Q4
cr-lgbm-v1 and cr-logreg-v1 both build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: work/cr-lgbm-v1.md, work/cr-logreg-v1.md, work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-score-v2, dec-ae-dashboard and dec-ae-tenure-norm. They reach it through ae-score-v1, ae-score-v2, feat-ae-active-days-v1 and feat-ae-depth-v1/v2.
Notes: work/dec-ae-no-push-credit.md, work/dec-ae-score-v2.md, work/dec-ae-dashboard.md, work/dec-ae-tenure-norm.md, work/ae-score-v1.md, work/ae-score-v2.md, work/feat-ae-active-days-v1.md, work/feat-ae-depth-v1.md, work/feat-ae-depth-v2.md, work/ds-ae-sessions-daily.md

## Q6
The bt-xgb-v1 line runs v1, then v2, then v3, and v3 is the current production model from 2026-03-01. bt-xgb-v3 builds on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: work/bt-xgb-v1.md, work/bt-xgb-v2.md, work/bt-xgb-v3.md, work/dec-bt-margin-label.md, work/exp-107-margin-label.md

## Q7
ae-score-v1 rests on the dataset notes ds-ae-sessions-daily and ds-ae-push-log. It builds on feat-ae-active-days-v1, feat-ae-depth-v1 and feat-ae-push-open-v1, and ds-ae-push-log builds on the daily sessions table, which is ds-ae-sessions-daily.
Notes: work/ae-score-v1.md, work/feat-ae-active-days-v1.md, work/feat-ae-depth-v1.md, work/feat-ae-push-open-v1.md, work/ds-ae-push-log.md, work/ds-ae-sessions-daily.md

## Q8
churn-gbm-2025-v2 and churn-lr-base-2025 both build directly on feat-c25-payment-behaviour and feat-c25-txn-recency.
Notes: work/churn-gbm-2025-v2.md, work/churn-lr-base-2025.md, work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md

## Q9
Two decision notes rest on feat-app-util-new: dec-app-cutoff-v3 directly, through app-scorecard-v3, and dec-app-rebuild-v4 through find-app-gini-v3-drift and app-scorecard-v3. The feature note says it is "used in app-scorecard-v3 and later", but app-scorecard-v4 does not name it, so I did not count the v4 chain.
Notes: work/feat-app-util-new.md, work/app-scorecard-v3.md, work/dec-app-cutoff-v3.md, work/find-app-gini-v3-drift.md, work/dec-app-rebuild-v4.md

## Q10
The cr-lgbm-v1 line runs v1, then v2, then v3, and v3 is the note in force. cr-lgbm-v3 builds on cr-lgbm-v2, ds-cr-intent-labels, exp-106-call-center-routing and the cost-matrix misroute finding fnd-cr-threshold.
Notes: work/cr-lgbm-v1.md, work/cr-lgbm-v2.md, work/cr-lgbm-v3.md, work/exp-106-call-center-routing.md, work/fnd-cr-threshold.md, work/ds-cr-intent-labels.md