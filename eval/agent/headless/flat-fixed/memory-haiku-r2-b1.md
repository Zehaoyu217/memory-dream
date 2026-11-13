## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. They reach it through aml-xgb-v1/v2/v3 and the AML findings and experiments built on those.
Notes: work/dec-aml-queue-only.md, work/dec-aml-ranker-v3.md, work/dec-aml-sample-10.md, work/dec-aml-suppress-018.md

## Q2
The note in force is aml-xgb-v3, which replaced aml-xgb-v2 and carries no superseded marker. It is built on ds-aml-oot, exp-407-aml-alerts, aml-xgb-v2 and exp-405-aml-alerts.
Notes: work/aml-xgb-v3.md, work/ds-aml-oot.md, work/exp-407-aml-alerts.md, work/aml-xgb-v2.md, work/exp-405-aml-alerts.md

## Q3
aml-xgb-v1 rests on three dataset notes: ds-aml-dispositions directly, and ds-aml-alerts and ds-aml-cash-txn through the feature and experiment notes it uses.
Notes: work/ds-aml-dispositions.md, work/ds-aml-alerts.md, work/ds-aml-cash-txn.md

## Q4
Both cr-lgbm-v1 and cr-logreg-v1 build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-score-v2, dec-ae-tenure-norm and dec-ae-dashboard. They reach it through the engagement features, scores and experiments.
Notes: work/dec-ae-no-push-credit.md, work/dec-ae-score-v2.md, work/dec-ae-tenure-norm.md, work/dec-ae-dashboard.md

## Q6
The note in force is bt-xgb-v3, which replaced bt-xgb-v2 and carries no superseded marker. It is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: work/bt-xgb-v3.md, work/bt-xgb-v2.md, work/dec-bt-margin-label.md, work/exp-107-margin-label.md

## Q7
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily and ds-ae-push-log. It reaches them through its feature notes.
Notes: work/ds-ae-sessions-daily.md, work/ds-ae-push-log.md

## Q8
churn-gbm-2025-v2 and churn-lr-base-2025 both build directly on feat-c25-payment-behaviour and feat-c25-txn-recency.
Notes: work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md

## Q9
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3, dec-app-no-gbm, dec-app-rebuild-v4 and dec-app-cutoff-v4. They reach it through app-scorecard-v3, app-scorecard-v4 and the application GBM and experiment notes built on them.
Notes: work/dec-app-cutoff-v3.md, work/dec-app-no-gbm.md, work/dec-app-rebuild-v4.md, work/dec-app-cutoff-v4.md

## Q10
The note in force is cr-lgbm-v3, which replaced cr-lgbm-v2 and carries no superseded marker. It is built on cr-lgbm-v2, ds-cr-intent-labels, exp-106-call-center-routing and fnd-cr-threshold.
Notes: work/cr-lgbm-v3.md, work/cr-lgbm-v2.md, work/ds-cr-intent-labels.md, work/exp-106-call-center-routing.md, work/fnd-cr-threshold.md