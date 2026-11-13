## Q1
Four decision notes rest on ds-aml-alerts. dec-aml-queue-only gets there through aml-find-fp-baseline, exp-401 and the dispositions dataset. dec-aml-suppress-018 builds on queue-only. dec-aml-ranker-v3 and dec-aml-sample-10 both build on suppress-018.
Notes: work/dec-aml-queue-only.md, work/dec-aml-suppress-018.md, work/dec-aml-ranker-v3.md, work/dec-aml-sample-10.md

## Q2
aml-xgb-v1 was replaced by aml-xgb-v2, and v2 by aml-xgb-v3, which is the current ranker. aml-xgb-v3 is built on aml-xgb-v2, ds-aml-oot, exp-405-aml-alerts and exp-407-aml-alerts (the note calls exp-407 "the experiment on recalibrated v3 top-40% capture").
Notes: work/aml-xgb-v3.md, work/aml-xgb-v2.md, work/ds-aml-oot.md, work/exp-405-aml-alerts.md, work/exp-407-aml-alerts.md

## Q3
aml-xgb-v1 rests on three datasets. It uses ds-aml-dispositions directly, and that note builds on ds-aml-alerts. It reaches ds-aml-cash-txn through feat-aml-new-counterparty and feat-aml-structuring-v1.
Notes: work/ds-aml-dispositions.md, work/ds-aml-alerts.md, work/ds-aml-cash-txn.md

## Q4
Both models build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
All four engagement decisions rest on ds-ae-sessions-daily. dec-ae-no-push-credit gets there through ae-score-v1, and dec-ae-score-v2 through ae-score-v2. dec-ae-tenure-norm goes through depth v2 and depth v1. dec-ae-dashboard builds on dec-ae-score-v2.
Notes: work/dec-ae-no-push-credit.md, work/dec-ae-score-v2.md, work/dec-ae-tenure-norm.md, work/dec-ae-dashboard.md

## Q6
bt-xgb-v1 was replaced by bt-xgb-v2, and v2 by bt-xgb-v3, which has been the production model since 2026-03-01. bt-xgb-v3 is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: work/bt-xgb-v3.md, work/bt-xgb-v2.md, work/dec-bt-margin-label.md, work/exp-107-margin-label.md

## Q7
ae-score-v1 rests on two datasets. Active days v1 and depth v1 build on ds-ae-sessions-daily. Push open v1 builds on ds-ae-push-log, which itself builds on ds-ae-sessions-daily.
Notes: work/ds-ae-sessions-daily.md, work/ds-ae-push-log.md

## Q8
Both models build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. They differ on utilisation: the GBM uses util-v2 and the logistic baseline uses util-v1.
Notes: work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md

## Q9
Four decision notes rest on feat-app-util-new, all through app-scorecard-v3: dec-app-cutoff-v3 directly, and dec-app-no-gbm through exp-503 and exp-504. dec-app-rebuild-v4 goes through app-gbm-v2 and find-app-gini-v3-drift, and dec-app-cutoff-v4 through app-scorecard-v4.
Notes: work/dec-app-cutoff-v3.md, work/dec-app-no-gbm.md, work/dec-app-rebuild-v4.md, work/dec-app-cutoff-v4.md

## Q10
cr-lgbm-v1 was replaced by cr-lgbm-v2, and v2 by cr-lgbm-v3, which is the current router. cr-lgbm-v3 is built on cr-lgbm-v2, ds-cr-intent-labels, exp-106-call-center-routing and fnd-cr-threshold (the note calls it "the cost matrix misroute finding").
Notes: work/cr-lgbm-v3.md, work/cr-lgbm-v2.md, work/ds-cr-intent-labels.md, work/exp-106-call-center-routing.md, work/fnd-cr-threshold.md