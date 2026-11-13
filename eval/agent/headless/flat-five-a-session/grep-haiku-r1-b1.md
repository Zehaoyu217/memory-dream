## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only (via aml-find-fp-baseline and the aml-xgb-v1 ranker), dec-aml-suppress-018 (via exp-406, aml-find-ranker-top40-revised and ds-aml-oot), dec-aml-sample-10 (via dec-aml-suppress-018), and dec-aml-ranker-v3 (via dec-aml-suppress-018 and aml-xgb-v3).
Notes: work/dec-aml-queue-only.md, work/dec-aml-suppress-018.md, work/dec-aml-sample-10.md, work/dec-aml-ranker-v3.md

## Q2
aml-xgb-v1 was replaced by aml-xgb-v2, which was replaced by aml-xgb-v3. aml-xgb-v3 is the one in force (promoted 2026-07-08). It is built on aml-xgb-v2, ds-aml-oot, exp-405-aml-alerts and exp-407-aml-alerts.
Notes: work/aml-xgb-v3.md, work/aml-xgb-v2.md, work/ds-aml-oot.md, work/exp-405-aml-alerts.md, work/exp-407-aml-alerts.md

## Q3
aml-xgb-v1 rests on three direct inputs: the AML analyst dispositions dataset, feat-aml-new-counterparty and feat-aml-structuring-v1. Following those back gives ds-aml-dispositions, which builds on ds-aml-alerts, and ds-aml-cash-txn, which the two features read from.
Notes: work/ds-aml-dispositions.md, work/ds-aml-alerts.md, work/ds-aml-cash-txn.md

## Q4
Both cr-lgbm-v1 and cr-logreg-v1 build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
Four decision notes rest on ds-aml-sessions-daily: dec-ae-score-v2 and dec-ae-dashboard (via ae-score-v2 and the active-days and depth features built on it), dec-ae-no-push-credit (via ae-score-v1) and dec-ae-tenure-norm (via feat-ae-depth-v2 and feat-ae-depth-v1).
Notes: work/dec-ae-dashboard.md, work/dec-ae-no-push-credit.md, work/dec-ae-score-v2.md, work/dec-ae-tenure-norm.md