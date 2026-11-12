## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. The first is direct through aml-find-fp-baseline and exp-401, and the others run through the aml-xgb-v3 and exp-406/408 chain.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md
## Q2
The note in force at the end of the aml-xgb-v1 line is aml-xgb-v3, which was built directly on aml-xgb-v2 (replaced), exp-405, exp-407 and ds-aml-oot.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md, aml-alerts/ds-aml-oot.md
## Q3
Only one note of another project is built directly on bt-xgb-v3: promo-apr-test/pa-bal-forecast-v1. Other promo-apr-test notes depend on bt-xgb-v3 only through it.
Notes: promo-apr-test/pa-bal-forecast-v1.md
## Q4
aml-xgb-v2 rests on three dataset notes: ds-aml-alerts, ds-aml-cash-txn and ds-aml-dispositions.
Notes: aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md, aml-alerts/ds-aml-dispositions.md
## Q5
Both churn-gbm-2025-v2 and churn-lr-base-2025 build directly on feat-c25-txn-recency and feat-c25-payment-behaviour.
Notes: churn-2025/feat-c25-txn-recency.md, churn-2025/feat-c25-payment-behaviour.md
## Q6
bt-logit-baseline is the only current model that builds directly on a replaced feature or dataset note: it rests on feat-bt-util-3m, which was replaced by feat-bt-util-trend-v2.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md
## Q7
Three decision notes rest on feat-ae-push-open-v1: dec-ae-no-push-credit, dec-ae-score-v2 and dec-ae-dashboard. The first is direct through fnd-ae-push-null, and the other two run through ae-score-v2 and fnd-ae-quintiles.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-dashboard.md
## Q8
The note in force at the end of the bt-xgb-v1 line is bt-xgb-v3, which was built directly on bt-xgb-v2 (replaced), exp-107-margin-label and dec-bt-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/exp-107-margin-label.md, balance-transfer-propensity/dec-bt-margin-label.md
## Q9
Only one note of another project is built directly on feat-bsm-score-map-v2: application-scorecard/ds-app-bureau-v10-pull.
Notes: application-scorecard/ds-app-bureau-v10-pull.md
## Q10
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026, ds-bsm-app-dev-2024 and ds-bsm-v8-history.
Notes: bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md