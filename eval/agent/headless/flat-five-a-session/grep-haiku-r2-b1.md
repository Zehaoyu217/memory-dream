## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only (through aml-xgb-v1 and aml-find-fp-baseline, both built on the AML alert data), dec-aml-suppress-018, dec-aml-sample-10 and dec-aml-ranker-v3.
Notes: work/dec-aml-queue-only.md, work/dec-aml-suppress-018.md, work/dec-aml-sample-10.md, work/dec-aml-ranker-v3.md

## Q2
aml-xgb-v1 was replaced by aml-xgb-v2, which was in turn replaced by aml-xgb-v3, the ranker in force since 2026-07-08 (dec-aml-ranker-v3). aml-xgb-v3 builds on aml-xgb-v2, ds-aml-oot, exp-405-aml-alerts and exp-407-aml-alerts.
Notes: work/aml-xgb-v1.md, work/aml-xgb-v2.md, work/aml-xgb-v3.md, work/ds-aml-oot.md, work/exp-405-aml-alerts.md, work/exp-407-aml-alerts.md

## Q3
The dataset notes are ds-aml-dispositions and ds-aml-alerts (through the analyst dispositions link), and ds-aml-cash-txn (through feat-aml-new-counterparty and feat-aml-structuring-v1).
Notes: work/aml-xgb-v1.md, work/ds-aml-dispositions.md, work/ds-aml-alerts.md, work/feat-aml-new-counterparty.md, work/feat-aml-structuring-v1.md, work/ds-aml-cash-txn.md

## Q4
Both build on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1. cr-lgbm-v1 also uses caller history, tenure and experiment inputs, but cr-logreg-v1 does not.
Notes: work/cr-lgbm-v1.md, work/cr-logreg-v1.md, work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
Four decisions rest on ds-ae-sessions-daily: dec-ae-score-v2 and dec-ae-dashboard (through ae-score-v2 and feat-ae-active-days-v1), dec-ae-no-push-credit (through ae-score-v1), and dec-ae-tenure-norm (through feat-ae-depth-v2 and feat-ae-depth-v1).
Notes: work/dec-ae-score-v2.md, work/dec-ae-dashboard.md, work/dec-ae-no-push-credit.md, work/dec-ae-tenure-norm.md