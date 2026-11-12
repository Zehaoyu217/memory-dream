## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only and dec-aml-suppress-018 directly or through the chain, and dec-aml-ranker-v3 and dec-aml-sample-10 through dec-aml-suppress-018. The full project map confirms no other decision notes in aml-alerts.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-suppress-018.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md

## Q2
aml-xgb-v3 is the one in force, since it has no supersession marker. It is built directly on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only promo-apr-test/pa-bal-forecast-v1 is built directly on bt-xgb-v3. The other promo-apr-test notes rest on the balance-transfer-propensity folder only through other notes.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three datasets: ds-aml-dispositions directly, and ds-aml-cash-txn (through feat-aml-new-counterparty and feat-aml-structuring-v1) and ds-aml-alerts (through ds-aml-dispositions) further back.
Notes: aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-cash-txn.md, aml-alerts/ds-aml-alerts.md

## Q5
cr-lgbm-v1 and cr-logreg-v1 both build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
bt-logit-baseline is the only current balance-transfer-propensity model built directly on a replaced feature: feat-bt-util-3m, which was superseded by feat-bt-util-trend-v2. bt-xgb-v3 is current but builds on no replaced feature directly.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-tenure-norm, dec-ae-score-v2 and dec-ae-dashboard, the last through dec-ae-score-v2.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-dashboard.md

## Q8
bt-xgb-v3 is in force, since it has no supersession marker. It is built directly on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only application-scorecard/ds-app-bureau-v10-pull is built directly on feat-bsm-score-map-v2 from another project.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two datasets: ds-ae-sessions-daily, and ds-ae-push-log through ds-ae-push-log's own dependency on ds-ae-sessions-daily. Both are reached through its direct features.
Notes: app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md