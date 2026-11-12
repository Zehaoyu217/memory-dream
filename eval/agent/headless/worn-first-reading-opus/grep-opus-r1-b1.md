## Q1
All four aml-alerts decisions rest on ds-aml-alerts. dec-aml-queue-only gets there through aml-find-fp-baseline → exp-401. dec-aml-suppress-018 gets there through the ranker findings and dec-aml-queue-only. dec-aml-ranker-v3 gets there through aml-xgb-v3 → ds-aml-oot. dec-aml-sample-10 gets there through dec-aml-suppress-018. No note in another project builds on it.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-suppress-018.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md

## Q2
aml-xgb-v1 was replaced by aml-xgb-v2, and aml-xgb-v2 by aml-xgb-v3, which is the current ranker. aml-xgb-v3 builds on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407 (the recalibrated v3 top-40% capture experiment).
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only one note in another project builds directly on bt-xgb-v3: the promo-apr-test balance forecast pa-bal-forecast-v1.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three dataset notes. ds-aml-dispositions is direct, and it builds on ds-aml-alerts. ds-aml-cash-txn comes through feat-aml-new-counterparty and feat-aml-structuring-v1.
Notes: aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both models build directly on the IVR path feature and the 30-second transcript TF-IDF feature.
Notes: call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
Only bt-logit-baseline. No note replaces it, though it is now just a reference model and no longer scored in production. It builds directly on feat-bt-util-3m, which feat-bt-util-trend-v2 replaced.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md

## Q7
All four app-engagement decisions rest on ds-ae-sessions-daily. dec-ae-no-push-credit gets there through ae-score-v1. dec-ae-score-v2 and dec-ae-dashboard get there through ae-score-v2 → feat-ae-active-days-v1. dec-ae-tenure-norm gets there through feat-ae-depth-v2 → feat-ae-depth-v1. Notes in other projects use the `app.sessions_daily` table but do not cite this note.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-dashboard.md, app-engagement/dec-ae-tenure-norm.md

## Q8
bt-xgb-v1 was replaced by bt-xgb-v2, and bt-xgb-v2 by bt-xgb-v3, which has been the production model since 2026-03-01. bt-xgb-v3 builds on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only one note in another project builds directly on feat-bsm-score-map-v2: the application-scorecard bureau v10 pull dataset.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two dataset notes. ds-ae-sessions-daily comes through the active-days and depth v1 features. ds-ae-push-log comes through feat-ae-push-open-v1, and ds-ae-push-log itself builds on ds-ae-sessions-daily.
Notes: app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md