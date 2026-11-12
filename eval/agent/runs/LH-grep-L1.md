## Q1
Four decision notes rest on aml-alerts/ds-aml-alerts, directly or through built notes: dec-aml-queue-only (via aml-xgb-v1), dec-aml-ranker-v3 (via aml-xgb-v3), dec-aml-sample-10, and dec-aml-suppress-018 (via aml-xgb-v3).
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md

## Q2
aml-xgb-v3 is in force: aml-xgb-v1 was superseded by aml-xgb-v2, which was superseded by aml-xgb-v3. aml-xgb-v3 is built on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only one note of another project is built directly on balance-transfer-propensity/bt-xgb-v3: promo-apr-test/pa-bal-forecast-v1.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
Following aml-xgb-v2 back to the start, it rests on three dataset notes: ds-aml-alerts (directly and via the exp, feature and v1 chain), ds-aml-dispositions (via aml-xgb-v1) and ds-aml-cash-txn.
Notes: aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both churn-gbm-2025-v2 and churn-lr-base-2025 build directly on feat-c25-payment-behaviour and feat-c25-txn-recency.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q6
Only bt-logit-baseline is a current model that builds directly on a replaced feature: it is built on feat-bt-util-3m, which feat-bt-util-trend-v2 has superseded. The other current model, bt-xgb-v3, builds only on models, experiments and decisions.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/feat-bt-util-trend-v2.md

## Q7
Three decision notes rest on app-engagement/feat-ae-push-open-v1: dec-ae-score-v2, dec-ae-no-push-credit and dec-ae-dashboard, all through the ae-score and exp chain.
Notes: app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-dashboard.md

## Q8
bt-xgb-v3 is in force: bt-xgb-v1 was superseded by bt-xgb-v2, which was superseded by bt-xgb-v3. bt-xgb-v3 is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only application-scorecard/ds-app-bureau-v10-pull is built directly on bureau-score-migration/feat-bsm-score-map-v2 from another project.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-app-dev-2024, ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026 and ds-bsm-v8-history.
Notes: bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md