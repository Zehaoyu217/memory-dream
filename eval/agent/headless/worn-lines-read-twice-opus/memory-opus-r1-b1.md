## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only (through ds-aml-dispositions → aml-xgb-v1 / q-aml-signoff, and exp-401 → aml-find-fp-baseline), and dec-aml-suppress-018, dec-aml-ranker-v3 and dec-aml-sample-10, which build on that one in turn. No notes in other projects rest on aml-alerts.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-suppress-018.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md

## Q2
The line runs aml-xgb-v1 → aml-xgb-v2 → aml-xgb-v3, so aml-xgb-v3 is the one in force now. It is built on aml-xgb-v2 (replaced), ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only one note in another project builds directly on bt-xgb-v3: promo-apr-test/pa-bal-forecast-v1.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three dataset notes. ds-aml-dispositions is a direct input and is itself built on ds-aml-alerts. ds-aml-cash-txn comes in through feat-aml-new-counterparty and feat-aml-structuring-v1.
Notes: aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
The two models share two feature notes as direct inputs: feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
The only one is bt-logit-baseline. It is still current and builds directly on feat-bt-util-3m, which feat-bt-util-trend-v2 has since replaced. The other current model, bt-xgb-v3, does not build directly on a replaced feature or dataset note.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md

## Q7
All four decision notes in app-engagement rest on it. dec-ae-no-push-credit comes through ae-score-v1, and dec-ae-tenure-norm through feat-ae-depth-v1 → exp-504 → feat-ae-depth-v2. dec-ae-score-v2 comes through ae-score-v2 and exp-505, and dec-ae-dashboard through dec-ae-score-v2.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-dashboard.md

## Q8
The line runs bt-xgb-v1 → bt-xgb-v2 → bt-xgb-v3, so bt-xgb-v3 is the one in force now. It is built on bt-xgb-v2 (replaced), dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only one note in another project builds directly on feat-bsm-score-map-v2: application-scorecard/ds-app-bureau-v10-pull.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two dataset notes. ds-ae-sessions-daily comes in through feat-ae-active-days-v1 and feat-ae-depth-v1. ds-ae-push-log comes in through feat-ae-push-open-v1 and is itself built on ds-ae-sessions-daily.
Notes: app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md