## Q1
Four decision notes rest on ds-aml-alerts, directly or through other notes: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md

## Q2
The line runs aml-xgb-v1 → aml-xgb-v2 → aml-xgb-v3, so aml-xgb-v3 is in force now. It is built on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
One note of another project is built directly on bt-xgb-v3: promo-apr-test/pa-bal-forecast-v1, which uses it as a BT propensity score.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three dataset notes: ds-aml-dispositions and ds-aml-cash-txn, plus ds-aml-alerts through the two features feat-aml-structuring-v1 and feat-aml-new-counterparty. The ds-aml-alerts link comes via the feature notes, not directly.
Notes: aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both cr-lgbm-v1 and cr-logreg-v1 build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
Only bt-logit-baseline fits: it is current (not superseded) and builds directly on feat-bt-util-3m, which has been replaced by feat-bt-util-trend-v2. The other current BT model, bt-xgb-v3, builds on models and notes, not on a replaced feature or dataset.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/feat-bt-util-trend-v2.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-score-v2, dec-ae-tenure-norm and dec-ae-dashboard.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/dec-ae-dashboard.md

## Q8
The line runs bt-xgb-v1 → bt-xgb-v2 → bt-xgb-v3, so bt-xgb-v3 is in force now. It is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label; dec-bt-margin-label also cites a rule that no note was placed for, so its link back to bt-xgb-v1 is unconfirmed.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
One note of another project is built directly on feat-bsm-score-map-v2: application-scorecard/ds-app-bureau-v10-pull, which re-scores applications on the mapped v10 bureau score.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily and ds-ae-push-log, reached through the features feat-ae-active-days-v1, feat-ae-depth-v1 and feat-ae-push-open-v1.
Notes: app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md