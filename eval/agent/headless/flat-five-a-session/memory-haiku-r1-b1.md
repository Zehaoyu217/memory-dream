## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. None depend on it directly; each reaches it through an aml-xgb model or a finding.
Notes: work/dec-aml-queue-only.md, work/dec-aml-ranker-v3.md, work/dec-aml-sample-10.md, work/dec-aml-suppress-018.md

## Q2
aml-xgb-v3 is the one in force: aml-xgb-v1 was replaced by aml-xgb-v2, which was replaced by aml-xgb-v3. aml-xgb-v3 is built on aml-xgb-v2, ds-aml-oot, exp-405-aml-alerts and the experiment that measured its top-40% capture (exp-407-aml-alerts).
Notes: work/aml-xgb-v3.md, work/aml-xgb-v2.md, work/ds-aml-oot.md, work/exp-405-aml-alerts.md, work/exp-407-aml-alerts.md

## Q3
aml-xgb-v1 rests on three dataset notes: ds-aml-dispositions directly, and ds-aml-cash-txn and ds-aml-alerts through its feature and dataset notes. ds-aml-alerts and ds-aml-cash-txn are the starting points; neither is built on anything else.
Notes: work/ds-aml-dispositions.md, work/ds-aml-cash-txn.md, work/ds-aml-alerts.md

## Q4
feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1 are the two feature notes that both cr-lgbm-v1 and cr-logreg-v1 build on directly.
Notes: work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md, work/cr-lgbm-v1.md, work/cr-logreg-v1.md

## Q5
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-score-v2, dec-ae-tenure-norm and dec-ae-dashboard. They reach it through the engagement features, models and experiments built on that dataset.
Notes: work/dec-ae-no-push-credit.md, work/dec-ae-score-v2.md, work/dec-ae-tenure-norm.md, work/dec-ae-dashboard.md