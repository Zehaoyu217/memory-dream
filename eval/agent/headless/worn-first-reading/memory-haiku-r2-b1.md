## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. They reach it through the dataset, feature and model notes built on it.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md

## Q2
aml-xgb-v1 was replaced by aml-xgb-v2, which was replaced by aml-xgb-v3, the note in force now. aml-xgb-v3 is built on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
One note in another project is built directly on bt-xgb-v3: promo-apr-test/pa-bal-forecast-v1, which uses it as a BT propensity score.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three datasets: ds-aml-dispositions directly, and ds-aml-alerts and ds-aml-cash-txn through its feature notes.
Notes: aml-alerts/aml-xgb-v1.md, aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both models build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-logreg-v1.md, call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
bt-logit-baseline is the only current model that builds directly on a replaced feature: feat-bt-util-3m, which was superseded by feat-bt-util-trend-v2. The other BT models either are superseded or build on models and decisions, not on replaced features or datasets.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-score-v2, dec-ae-tenure-norm and dec-ae-dashboard.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/dec-ae-dashboard.md

## Q8
bt-xgb-v1 was replaced by bt-xgb-v2, which was replaced by bt-xgb-v3, the note in force now. bt-xgb-v3 is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
One note in another project is built directly on feat-bsm-score-map-v2: application-scorecard/ds-app-bureau-v10-pull, which re-scores applications on the mapped v10 score.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two datasets: ds-ae-sessions-daily through feat-ae-active-days-v1 and feat-ae-depth-v1, and ds-ae-push-log through feat-ae-push-open-v1.
Notes: app-engagement/ae-score-v1.md, app-engagement/feat-ae-active-days-v1.md, app-engagement/feat-ae-depth-v1.md, app-engagement/feat-ae-push-open-v1.md, app-engagement/ds-ae-push-log.md, app-engagement/ds-ae-sessions-daily.md