## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only (via aml-find-fp-baseline and exp-401), dec-aml-ranker-v3 (via aml-xgb-v3, v2, exp-404 and feat-aml-kyc-band), dec-aml-suppress-018 (via exp-406 and ds-aml-oot), and dec-aml-sample-10 (via dec-aml-suppress-018).
Notes: work/dec-aml-queue-only.md, work/dec-aml-ranker-v3.md, work/dec-aml-suppress-018.md, work/dec-aml-sample-10.md

## Q2
aml-xgb-v3 is the note in force: aml-xgb-v1 was replaced by aml-xgb-v2, which was replaced by v3 on 2026-07-08. aml-xgb-v3 is built on aml-xgb-v2, ds-aml-oot, exp-405-aml-alerts and exp-407-aml-alerts.
Notes: work/aml-xgb-v3.md, work/aml-xgb-v2.md, work/ds-aml-oot.md, work/exp-405-aml-alerts.md, work/exp-407-aml-alerts.md

## Q3
aml-xgb-v1 rests on three dataset notes: ds-aml-dispositions and, through it, ds-aml-alerts (its direct inputs are the analyst dispositions and the structuring and new-counterparty features), and ds-aml-cash-txn through feat-aml-structuring-v1 and feat-aml-new-counterparty.
Notes: work/ds-aml-alerts.md, work/ds-aml-dispositions.md, work/ds-aml-cash-txn.md

## Q4
cr-lgbm-v1 and cr-logreg-v1 both build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
Four decision notes rest on ds-ae-sessions-daily: dec-ae-score-v2 (via ae-score-v2 and feat-ae-depth-v2), dec-ae-tenure-norm (via feat-ae-depth-v2), dec-ae-no-push-credit (via ae-score-v1), and dec-ae-dashboard (via dec-ae-score-v2).
Notes: work/dec-ae-score-v2.md, work/dec-ae-tenure-norm.md, work/dec-ae-no-push-credit.md, work/dec-ae-dashboard.md