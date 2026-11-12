## Q1
All four aml-alerts decisions trace back to ds-aml-alerts. dec-aml-queue-only gets there through aml-find-fp-baseline → exp-401 and through q-aml-signoff → ds-aml-dispositions. dec-aml-suppress-018, dec-aml-ranker-v3 and dec-aml-sample-10 rest on the ranker, OOT-set and suppression chain built on top of those. No note in another project builds on these.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-suppress-018.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md

## Q2
The line runs aml-xgb-v1 → aml-xgb-v2 → aml-xgb-v3, and aml-xgb-v3 is the current ranker. It builds on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407 (the experiment on recalibrated v3 top-40% capture).
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only one note in another project builds directly on bt-xgb-v3: promo-apr-test's balance forecast model pa-bal-forecast-v1.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 builds on ds-aml-dispositions, feat-aml-new-counterparty and feat-aml-structuring-v1. Both features build on ds-aml-cash-txn, and ds-aml-dispositions builds on ds-aml-alerts. So it rests on three datasets: ds-aml-dispositions, ds-aml-cash-txn and ds-aml-alerts.
Notes: aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-cash-txn.md, aml-alerts/ds-aml-alerts.md

## Q5
Both models build directly on two feature notes: feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
The one match is bt-logit-baseline. No note replaces it, but it is kept only as a reference model and no longer scored in production. It builds directly on feat-bt-util-3m, which feat-bt-util-trend-v2 has since replaced. bt-xgb-v3, the other current model, builds directly only on bt-xgb-v2, a decision and an experiment.
Notes: balance-transfer-propensity/bt-logit-baseline.md

## Q7
All four app-engagement decisions trace back to ds-ae-sessions-daily, through the features, push log, attrition labels and holdout built on it. dec-ae-no-push-credit goes through ae-score-v1, dec-ae-score-v2 and dec-ae-dashboard through ae-score-v2, and dec-ae-tenure-norm through feat-ae-depth-v2.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-dashboard.md, app-engagement/dec-ae-tenure-norm.md

## Q8
The line runs bt-xgb-v1 → bt-xgb-v2 → bt-xgb-v3, and bt-xgb-v3 has been the production model since 2026-03-01. It builds on bt-xgb-v2 (the depth-5 xgboost model), dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only one note in another project builds directly on feat-bsm-score-map-v2: application-scorecard's dataset ds-app-bureau-v10-pull.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 builds on feat-ae-active-days-v1, feat-ae-depth-v1 and feat-ae-push-open-v1. The first two come from ds-ae-sessions-daily, and the push feature comes from ds-ae-push-log, which itself builds on ds-ae-sessions-daily. So it rests on two datasets: ds-ae-sessions-daily and ds-ae-push-log.
Notes: app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md