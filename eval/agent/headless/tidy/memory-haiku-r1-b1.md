## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018, all in aml-alerts.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md

## Q2
aml-xgb-v3 is in force: aml-xgb-v1 was replaced by aml-xgb-v2, which was replaced by aml-xgb-v3. aml-xgb-v3 is built directly on aml-xgb-v2, exp-405, exp-407 and ds-aml-oot.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md, aml-alerts/ds-aml-oot.md

## Q3
Only one note of another project is built directly on bt-xgb-v3: pa-bal-forecast-v1 in promo-apr-test, which also draws on ds-pa-balance-panel and feat-pa-bt-inflow-v2.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three dataset notes: ds-aml-dispositions directly, and ds-aml-alerts and ds-aml-cash-txn through its feature and dataset inputs.
Notes: aml-alerts/aml-xgb-v1.md, aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both models build directly on feat-cr-transcript-tfidf-v1 and feat-cr-ivr-path-v1.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-logreg-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md, call-center-routing/feat-cr-ivr-path-v1.md

## Q6
bt-logit-baseline is the only current model that builds directly on a replaced feature: it uses feat-bt-util-3m, which was replaced by feat-bt-util-trend-v2. The memory does not mark bt-logit-baseline as superseded.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/feat-bt-util-trend-v2.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-score-v2, dec-ae-tenure-norm and dec-ae-dashboard, all in app-engagement.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/dec-ae-dashboard.md

## Q8
bt-xgb-v3 is in force: bt-xgb-v1 was replaced by bt-xgb-v2, which was replaced by bt-xgb-v3. bt-xgb-v3 is built directly on bt-xgb-v2, exp-107-margin-label and dec-bt-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/exp-107-margin-label.md, balance-transfer-propensity/dec-bt-margin-label.md

## Q9
Only one note of another project is built directly on feat-bsm-score-map-v2: ds-app-bureau-v10-pull in application-scorecard, a dataset.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two dataset notes: ds-ae-push-log through feat-ae-push-open-v1, and ds-ae-sessions-daily through the active-days, depth and push features.
Notes: app-engagement/ae-score-v1.md, app-engagement/ds-ae-push-log.md, app-engagement/ds-ae-sessions-daily.md