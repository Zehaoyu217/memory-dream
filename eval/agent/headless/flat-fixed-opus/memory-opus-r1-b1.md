## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. None is built on it directly; each gets there through the datasets, experiments, models and findings built on it.
Notes: work/dec-aml-queue-only.md, work/dec-aml-ranker-v3.md, work/dec-aml-sample-10.md, work/dec-aml-suppress-018.md

## Q2
The line runs aml-xgb-v1 → aml-xgb-v2 → aml-xgb-v3, and aml-xgb-v3 is the current ranker. It is built on aml-xgb-v2, ds-aml-oot, exp-405-aml-alerts and exp-407-aml-alerts.
Notes: work/aml-xgb-v3.md, work/aml-xgb-v2.md, work/ds-aml-oot.md, work/exp-405-aml-alerts.md, work/exp-407-aml-alerts.md

## Q3
aml-xgb-v1 rests on three datasets. It is built directly on ds-aml-dispositions, which comes from ds-aml-alerts. Its two features, feat-aml-new-counterparty and feat-aml-structuring-v1, both come from ds-aml-cash-txn.
Notes: work/ds-aml-dispositions.md, work/ds-aml-alerts.md, work/ds-aml-cash-txn.md

## Q4
Both models build directly on two feature notes: feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
Four decision notes rest on ds-ae-sessions-daily, all through other notes: dec-ae-no-push-credit, dec-ae-score-v2, dec-ae-tenure-norm and dec-ae-dashboard.
Notes: work/dec-ae-no-push-credit.md, work/dec-ae-score-v2.md, work/dec-ae-tenure-norm.md, work/dec-ae-dashboard.md

## Q6
The line runs bt-xgb-v1 → bt-xgb-v2 → bt-xgb-v3, and bt-xgb-v3 has been the production model since 2026-03-01. It is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: work/bt-xgb-v3.md, work/bt-xgb-v2.md, work/dec-bt-margin-label.md, work/exp-107-margin-label.md

## Q7
ae-score-v1 rests on two datasets: ds-ae-sessions-daily, through feat-ae-active-days-v1 and feat-ae-depth-v1, and ds-ae-push-log, through feat-ae-push-open-v1.
Notes: work/ds-ae-sessions-daily.md, work/ds-ae-push-log.md

## Q8
Both models build directly on two feature notes: feat-c25-payment-behaviour and feat-c25-txn-recency.
Notes: work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md

## Q9
Four decision notes rest on feat-app-util-new, through app-scorecard-v3 and the notes built on it: dec-app-cutoff-v3, dec-app-no-gbm, dec-app-rebuild-v4 and dec-app-cutoff-v4.
Notes: work/dec-app-cutoff-v3.md, work/dec-app-no-gbm.md, work/dec-app-rebuild-v4.md, work/dec-app-cutoff-v4.md

## Q10
The line runs cr-lgbm-v1 → cr-lgbm-v2 → cr-lgbm-v3, and cr-lgbm-v3 is the current router. It is built on cr-lgbm-v2, ds-cr-intent-labels, exp-106-call-center-routing and fnd-cr-threshold.
Notes: work/cr-lgbm-v3.md, work/cr-lgbm-v2.md, work/ds-cr-intent-labels.md, work/exp-106-call-center-routing.md, work/fnd-cr-threshold.md