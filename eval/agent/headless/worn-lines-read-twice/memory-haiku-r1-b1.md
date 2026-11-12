## Q1
Four decisions rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. The folder has four decision notes in total, so these are all of them.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md

## Q2
aml-xgb-v3 is the note in force. It is built on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only promo-apr-test/pa-bal-forecast-v1 is built directly on bt-xgb-v3.
Notes: promo-apr-test/pa-bal-forecast-v1.md, balance-transfer-propensity/bt-xgb-v3.md

## Q4
aml-xgb-v1 rests on two dataset notes: ds-aml-dispositions directly, and ds-aml-alerts and ds-aml-cash-txn through its feature and experiment notes.
Notes: aml-alerts/aml-xgb-v1.md, aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
cr-lgbm-v1 and cr-logreg-v1 both build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-logreg-v1.md, call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
Only bt-logit-baseline, which is still current, builds directly on a replaced note: feat-bt-util-3m, which was replaced by feat-bt-util-trend-v2.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/feat-bt-util-trend-v2.md

## Q7
Four decisions rest on ds-ae-sessions-daily: dec-ae-dashboard, dec-ae-no-push-credit, dec-ae-score-v2 and dec-ae-tenure-norm. The folder has four decision notes in total, so these are all of them.
Notes: app-engagement/dec-ae-dashboard.md, app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md

## Q8
bt-xgb-v3 is the note in force. It is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only application-scorecard/ds-app-bureau-v10-pull, a dataset, is built directly on feat-bsm-score-map-v2.
Notes: application-scorecard/ds-app-bureau-v10-pull.md, bureau-score-migration/feat-bsm-score-map-v2.md

## Q10
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily and ds-ae-push-log, reached through its feature notes.
Notes: app-engagement/ae-score-v1.md, app-engagement/feat-ae-active-days-v1.md, app-engagement/feat-ae-depth-v1.md, app-engagement/feat-ae-push-open-v1.md, app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md