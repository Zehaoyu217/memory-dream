## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only (via aml-find-fp-baseline and exp-401-aml-alerts), dec-aml-suppress-018 (via aml-find-ranker-top40-revised and exp-405/ds-aml-oot), dec-aml-ranker-v3 (via aml-xgb-v3 and exp-407), and dec-aml-sample-10 (via dec-aml-suppress-018).
Notes: work/dec-aml-queue-only.md, work/dec-aml-suppress-018.md, work/dec-aml-ranker-v3.md, work/dec-aml-sample-10.md

## Q2
The line ends at aml-xgb-v3, which is in force now. It is built on aml-xgb-v2, ds-aml-oot, exp-405-aml-alerts and exp-407-aml-alerts (the last is cited only as "the experiment on recalibrated v3 top-40% capture").
Notes: work/aml-xgb-v3.md, work/aml-xgb-v2.md, work/ds-aml-oot.md, work/exp-405-aml-alerts.md, work/exp-407-aml-alerts.md

## Q3
Following aml-xgb-v1 back, it rests on ds-aml-dispositions, which builds on ds-aml-alerts, and on feat-aml-new-counterparty and feat-aml-structuring-v1, which both build on ds-aml-cash-txn. So the dataset notes are ds-aml-dispositions, ds-aml-alerts and ds-aml-cash-txn.
Notes: work/ds-aml-dispositions.md, work/ds-aml-alerts.md, work/ds-aml-cash-txn.md

## Q4
Both cr-lgbm-v1 and cr-logreg-v1 build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
Four decision notes rest on ds-ae-sessions-daily: dec-ae-score-v2 and dec-ae-no-push-credit (via ae-score-v1/v2 and feat-ae-active-days-v1), dec-ae-tenure-norm (via feat-ae-depth-v2 and feat-ae-depth-v1), and dec-ae-dashboard (via dec-ae-score-v2).
Notes: work/dec-ae-score-v2.md, work/dec-ae-no-push-credit.md, work/dec-ae-tenure-norm.md, work/dec-ae-dashboard.md

## Q6
The line ends at bt-xgb-v3, which is in force now. It is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label (the margin-weighted label experiment).
Notes: work/bt-xgb-v3.md, work/bt-xgb-v2.md, work/dec-bt-margin-label.md, work/exp-107-margin-label.md

## Q7
Following ae-score-v1 back, it rests on ds-ae-sessions-daily (via feat-ae-active-days-v1 and feat-ae-depth-v1) and ds-ae-push-log (via feat-ae-push-open-v1).
Notes: work/ds-ae-sessions-daily.md, work/ds-ae-push-log.md

## Q8
Both churn-gbm-2025-v2 and churn-lr-base-2025 build directly on feat-c25-payment-behaviour (payment ratio and late counts) and feat-c25-txn-recency.
Notes: work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md

## Q9
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3 (directly on app-scorecard-v3), dec-app-rebuild-v4 (via find-app-gini-v3-drift), dec-app-no-gbm (via app-gbm-v1 and exp-504-application-scorecard), and dec-app-cutoff-v4 (via find-app-income-lift and exp-506-application-scorecard).
Notes: work/dec-app-cutoff-v3.md, work/dec-app-cutoff-v4.md, work/dec-app-rebuild-v4.md, work/dec-app-no-gbm.md

## Q10
The line ends at cr-lgbm-v3, which is in force now. It is built on cr-lgbm-v2, ds-cr-intent-labels, exp-106-call-center-routing and fnd-cr-threshold (the cost-matrix finding).
Notes: work/cr-lgbm-v3.md, work/cr-lgbm-v2.md, work/ds-cr-intent-labels.md, work/exp-106-call-center-routing.md, work/fnd-cr-threshold.md