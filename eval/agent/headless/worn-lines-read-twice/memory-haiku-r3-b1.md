## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. Three of them reach it through the aml-xgb models and findings.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md

## Q2
The line ends at aml-xgb-v3, which is in force now. It is built on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v1.md, aml-alerts/aml-xgb-v2.md, aml-alerts/aml-xgb-v3.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
One note of another project is built directly on bt-xgb-v3: promo-apr-test/pa-bal-forecast-v1. It builds on bt-xgb-v3, ds-pa-balance-panel and feat-pa-bt-inflow-v2.
Notes: promo-apr-test/pa-bal-forecast-v1.md, balance-transfer-propensity/bt-xgb-v3.md

## Q4
aml-xgb-v1 rests on three datasets: ds-aml-dispositions (direct), and ds-aml-alerts and ds-aml-cash-txn (through feat-aml-structuring-v1 and feat-aml-new-counterparty).
Notes: aml-alerts/aml-xgb-v1.md, aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both build on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1. cr-lgbm-v1 also uses caller history, tenure, and exp-101, but cr-logreg-v1 does not.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-logreg-v1.md, call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
Only bt-logit-baseline fits. It is still current and builds directly on feat-bt-util-3m, which was replaced by feat-bt-util-trend-v2. The other current model, bt-xgb-v3, builds on no replaced feature or dataset.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/feat-bt-util-trend-v2.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-score-v2, dec-ae-tenure-norm and dec-ae-dashboard. They reach it through the feature, score and finding notes built on it.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/dec-ae-dashboard.md

## Q8
The line ends at bt-xgb-v3, which is in force now. It is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v1.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
One note of another project is built directly on feat-bsm-score-map-v2: application-scorecard/ds-app-bureau-v10-pull, which re-scores the 2024 and 2025 applications on the mapped v10 bureau score.
Notes: application-scorecard/ds-app-bureau-v10-pull.md, bureau-score-migration/feat-bsm-score-map-v2.md

## Q10
ae-score-v1 rests on two datasets: ds-ae-sessions-daily and ds-ae-push-log. It reaches them through its three features: feat-ae-active-days-v1, feat-ae-depth-v1 and feat-ae-push-open-v1.
Notes: app-engagement/ae-score-v1.md, app-engagement/feat-ae-active-days-v1.md, app-engagement/feat-ae-depth-v1.md, app-engagement/feat-ae-push-open-v1.md, app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md