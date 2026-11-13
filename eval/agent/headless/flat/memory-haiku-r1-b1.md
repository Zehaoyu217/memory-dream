## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. They reach it through the AML alert-ranker chain (aml-xgb-v1 → v2 → v3) and the structuring false-positive experiments.
Notes: work/dec-aml-queue-only.md, work/dec-aml-ranker-v3.md, work/dec-aml-sample-10.md, work/dec-aml-suppress-018.md

## Q2
The line ends at aml-xgb-v3, which is in force now (aml-xgb-v1 → aml-xgb-v2 → aml-xgb-v3). aml-xgb-v3 is built on aml-xgb-v2, ds-aml-oot, exp-405-aml-alerts and exp-407-aml-alerts.
Notes: work/aml-xgb-v3.md, work/aml-xgb-v2.md, work/ds-aml-oot.md, work/exp-405-aml-alerts.md, work/exp-407-aml-alerts.md

## Q3
aml-xgb-v1 rests directly on ds-aml-dispositions, feat-aml-new-counterparty and feat-aml-structuring-v1. Going back to the start, the dataset notes are ds-aml-dispositions and ds-aml-cash-txn directly, and ds-aml-alerts through ds-aml-dispositions.
Notes: work/ds-aml-dispositions.md, work/ds-aml-alerts.md, work/ds-aml-cash-txn.md

## Q4
cr-lgbm-v1 and cr-logreg-v1 both build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1. cr-lgbm-v1 also uses caller history, tenure, and the other features, but cr-logreg-v1 does not.
Notes: work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-score-v2, dec-ae-tenure-norm and dec-ae-dashboard. They reach it through the engagement-score chain (ae-score-v1 → v2) and the feature notes built on the sessions table.
Notes: work/dec-ae-no-push-credit.md, work/dec-ae-score-v2.md, work/dec-ae-tenure-norm.md, work/dec-ae-dashboard.md

## Q6
The line ends at bt-xgb-v3, which is in force now (bt-xgb-v1 → bt-xgb-v2 → bt-xgb-v3). bt-xgb-v3 is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: work/bt-xgb-v3.md, work/bt-xgb-v2.md, work/dec-bt-margin-label.md, work/exp-107-margin-label.md

## Q7
ae-score-v1 rests directly on feat-ae-active-days-v1, feat-ae-depth-v1 and feat-ae-push-open-v1. Going back to the start, the dataset notes are ds-ae-sessions-daily and ds-ae-push-log, which feed those features.
Notes: work/ds-ae-sessions-daily.md, work/ds-ae-push-log.md

## Q8
churn-gbm-2025-v2 and churn-lr-base-2025 both build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. The other feature inputs differ: v2 uses util-v2 and churn-lr uses util-v1 and app sessions.
Notes: work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md

## Q9
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3, dec-app-rebuild-v4, dec-app-cutoff-v4 and dec-app-no-gbm. They reach it through app-scorecard-v3 and the scorecard models built on it.
Notes: work/dec-app-cutoff-v3.md, work/dec-app-rebuild-v4.md, work/dec-app-cutoff-v4.md, work/dec-app-no-gbm.md

## Q10
The line ends at cr-lgbm-v3, which is in force now (cr-lgbm-v1 → cr-lgbm-v2 → cr-lgbm-v3). cr-lgbm-v3 is built on cr-lgbm-v2, ds-cr-intent-labels, exp-106-call-center-routing and fnd-cr-threshold.
Notes: work/cr-lgbm-v3.md, work/cr-lgbm-v2.md, work/ds-cr-intent-labels.md, work/exp-106-call-center-routing.md, work/fnd-cr-threshold.md