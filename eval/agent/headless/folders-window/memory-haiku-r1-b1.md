## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only and dec-aml-ranker-v3 go through aml-find-fp-baseline and aml-xgb-v3, and dec-aml-suppress-018 and dec-aml-sample-10 go through aml-find-ranker-top40-revised and dec-aml-suppress-018. These are all the decision notes in aml-alerts, and none of the chains reach a decision note in another folder.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-suppress-018.md, aml-alerts/dec-aml-sample-10.md

## Q2
aml-xgb-v3 is the one in force now, after aml-xgb-v1 and then aml-xgb-v2. It is built directly on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v1.md, aml-alerts/aml-xgb-v2.md, aml-alerts/aml-xgb-v3.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only one note of another project is built directly on bt-xgb-v3: promo-apr-test/pa-bal-forecast-v1.
Notes: balance-transfer-propensity/bt-xgb-v3.md, promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three dataset notes: ds-aml-dispositions directly, and ds-aml-alerts and ds-aml-cash-txn through feat-aml-structuring-v1, feat-aml-new-counterparty and ds-aml-dispositions.
Notes: aml-alerts/aml-xgb-v1.md, aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1. cr-lgbm-v1 also builds on three other feature notes that cr-logreg-v1 does not use.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-logreg-v1.md, call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
bt-logit-baseline is the only current model that builds directly on a replaced feature. It builds on feat-bt-util-3m, which was replaced by feat-bt-util-trend-v2.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit and dec-ae-tenure-norm directly or through their feature and score chain, dec-ae-score-v2 through ae-score-v2, and dec-ae-dashboard through dec-ae-score-v2. These are all the decision notes in app-engagement.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/dec-ae-dashboard.md

## Q8
bt-xgb-v3 is the one in force now, after bt-xgb-v1 and then bt-xgb-v2. It is built directly on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v1.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only one note of another project is built directly on feat-bsm-score-map-v2: application-scorecard/ds-app-bureau-v10-pull.
Notes: bureau-score-migration/feat-bsm-score-map-v2.md, application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily and ds-ae-push-log. ds-ae-sessions-daily is reached through the three feature notes it builds on, and ds-ae-push-log through feat-ae-push-open-v1.
Notes: app-engagement/ae-score-v1.md, app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md