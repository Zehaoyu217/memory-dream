I've read the memory and have everything I need. Here are the answers.

## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-suppress-018, dec-aml-ranker-v3 and dec-aml-sample-10. They all reach it through other notes, not directly. Examples are aml-xgb-v1, q-aml-signoff, aml-find-fp-baseline and exp-407.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-suppress-018.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md

## Q2
aml-xgb-v1 was replaced by aml-xgb-v2, which was replaced by aml-xgb-v3. aml-xgb-v3 is the one in force now. It is built on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only one note in another project is built directly on bt-xgb-v3: the model pa-bal-forecast-v1 in promo-apr-test. Other promo-apr-test notes, such as pa-margin-v1 and v2, rest on it only through pa-bal-forecast-v1.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three datasets. It uses ds-aml-dispositions directly. It reaches ds-aml-alerts through ds-aml-dispositions, and ds-aml-cash-txn through feat-aml-structuring-v1 and feat-aml-new-counterparty.
Notes: aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both models build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
Only bt-logit-baseline fits. It is still current and builds directly on feat-bt-util-3m, which feat-bt-util-trend-v2 replaced. bt-xgb-v3 is current too, but the replaced note it builds on is a model (bt-xgb-v2), not a feature or dataset.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-tenure-norm, dec-ae-score-v2 and dec-ae-dashboard. They all reach it through other notes, such as ae-score-v1, feat-ae-depth-v2 and ae-score-v2.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-dashboard.md

## Q8
bt-xgb-v1 was replaced by bt-xgb-v2, which was replaced by bt-xgb-v3. bt-xgb-v3 is the one in force now. It is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only one note in another project is built directly on feat-bsm-score-map-v2: the dataset ds-app-bureau-v10-pull in application-scorecard. Other application-scorecard notes, such as feat-app-bureau-v10-band and app-scorecard-v4, reach it only through that dataset.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two datasets. It reaches ds-ae-push-log through feat-ae-push-open-v1. It reaches ds-ae-sessions-daily through feat-ae-active-days-v1 and feat-ae-depth-v1, and also through ds-ae-push-log, which is built on it.
Notes: app-engagement/ds-ae-push-log.md, app-engagement/ds-ae-sessions-daily.md