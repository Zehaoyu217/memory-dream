## Q1
Four decision notes rest on ds-aml-alerts, all through intermediate notes: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. None of them builds on it directly.
Notes: work/dec-aml-queue-only.md, work/dec-aml-ranker-v3.md, work/dec-aml-sample-10.md, work/dec-aml-suppress-018.md

## Q2
The note in force is aml-xgb-v3, since aml-xgb-v1 was replaced by aml-xgb-v2 and v2 was replaced by v3. aml-xgb-v3 builds on aml-xgb-v2, ds-aml-oot and exp-405-aml-alerts, plus the recalibrated top-40% capture experiment (exp-407-aml-alerts).
Notes: work/aml-xgb-v3.md, work/aml-xgb-v2.md, work/ds-aml-oot.md, work/exp-405-aml-alerts.md, work/exp-407-aml-alerts.md

## Q3
aml-xgb-v1 rests on three dataset notes: ds-aml-dispositions directly, and ds-aml-alerts and ds-aml-cash-txn through the feature notes and the dispositions dataset.
Notes: work/ds-aml-dispositions.md, work/ds-aml-alerts.md, work/ds-aml-cash-txn.md

## Q4
cr-lgbm-v1 and cr-logreg-v1 both build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
Four decision notes rest on ds-ae-sessions-daily, all through intermediate notes: dec-ae-dashboard, dec-ae-no-push-credit, dec-ae-score-v2 and dec-ae-tenure-norm. None of them builds on it directly.
Notes: work/dec-ae-dashboard.md, work/dec-ae-no-push-credit.md, work/dec-ae-score-v2.md, work/dec-ae-tenure-norm.md