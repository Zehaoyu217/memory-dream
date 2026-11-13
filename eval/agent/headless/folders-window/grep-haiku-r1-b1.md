## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-suppress-018, dec-aml-sample-10 and dec-aml-ranker-v3. Each reaches it through the chain of ranker, experiment and disposition notes that were built on the alerts table.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-suppress-018.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-ranker-v3.md

## Q2
aml-xgb-v3 is in force; it replaced aml-xgb-v2, which had replaced aml-xgb-v1. It is built on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v1.md, aml-alerts/aml-xgb-v2.md, aml-alerts/aml-xgb-v3.md

## Q3
Only one note from another project builds directly on bt-xgb-v3: pa-bal-forecast-v1 in promo-apr-test.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on the dispositions dataset (ds-aml-dispositions) directly, and on the cash-transaction dataset (ds-aml-cash-txn) through its two feature notes. Its dispositions dataset in turn rests on the alerts dataset (ds-aml-alerts). The dataset notes are therefore ds-aml-dispositions, ds-aml-alerts and ds-aml-cash-txn.
Notes: aml-alerts/aml-xgb-v1.md, aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md, aml-alerts/feat-aml-new-counterparty.md, aml-alerts/feat-aml-structuring-v1.md

## Q5
Both cr-lgbm-v1 and cr-logreg-v1 build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-logreg-v1.md, call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
None. The only current model, bt-xgb-v3, builds directly on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label, none of which is a feature or dataset note. The replaced feature feat-bt-util-3m is used only by retired models.
Notes: balance-transfer-propensity/bt-xgb-v3.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-dashboard, dec-ae-no-push-credit, dec-ae-score-v2 and dec-ae-tenure-norm. Each reaches it directly or through the holdout, label, push-log, feature or experiment notes built on the sessions table.
Notes: app-engagement/dec-ae-dashboard.md, app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md

## Q8
bt-xgb-v3 is in force; it replaced bt-xgb-v2, which had replaced bt-xgb-v1. It is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v1.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/bt-xgb-v3.md

## Q9
Only one note from another project builds directly on feat-bsm-score-map-v2: ds-app-bureau-v10-pull in application-scorecard.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on the sessions dataset (ds-ae-sessions-daily) directly, and on the push-log dataset (ds-ae-push-log) through the push-open feature. The dataset notes are ds-ae-sessions-daily and ds-ae-push-log.
Notes: app-engagement/ae-score-v1.md, app-engagement/feat-ae-active-days-v1.md, app-engagement/feat-ae-depth-v1.md, app-engagement/feat-ae-push-open-v1.md, app-engagement/ds-ae-push-log.md, app-engagement/ds-ae-sessions-daily.md