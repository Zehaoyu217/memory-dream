## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only (via aml-find-fp-baseline and exp-401), dec-aml-suppress-018 and dec-aml-sample-10 (both via dec-aml-queue-only), and dec-aml-ranker-v3 (via aml-xgb-v3, which builds on ds-aml-oot). About 90 other work notes name a source that no note matched, so this list may be incomplete.
Notes: work/dec-aml-queue-only.md, work/dec-aml-suppress-018.md, work/dec-aml-ranker-v3.md, work/dec-aml-sample-10.md

## Q2
The note in force at the end of the aml-xgb-v1 → v2 → v3 line is aml-xgb-v3, which is current and not superseded. It builds on aml-xgb-v2, ds-aml-oot, exp-405-aml-alerts and the experiment on recalibrated v3 top-40% capture.
Notes: work/aml-xgb-v3.md

## Q3
aml-xgb-v1 rests on three dataset notes. ds-aml-dispositions is direct, and ds-aml-cash-txn (via feat-aml-structuring-v1) and ds-aml-alerts (via ds-aml-dispositions and exp-401) are reached through other notes.
Notes: work/ds-aml-dispositions.md, work/ds-aml-cash-txn.md, work/ds-aml-alerts.md

## Q4
Both cr-lgbm-v1 and cr-logreg-v1 build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit (via ae-score-v1), dec-ae-tenure-norm (via feat-ae-depth-v2 and feat-ae-depth-v1), dec-ae-score-v2 (via ae-score-v2 and the exp-505 chain), and dec-ae-dashboard (via dec-ae-score-v2). About 90 other work notes name a source that no note matched, so this list may be incomplete.
Notes: work/dec-ae-no-push-credit.md, work/dec-ae-tenure-norm.md, work/dec-ae-score-v2.md, work/dec-ae-dashboard.md