## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-suppress-018, dec-aml-ranker-v3 and dec-aml-sample-10, each through aml-xgb-v1, aml-xgb-v2/v3, exp-405/406/407 or aml-find-fp-baseline.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-suppress-018.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md

## Q2
aml-xgb-v3 is in force (aml-xgb-v1 was superseded by aml-xgb-v2, which was superseded by aml-xgb-v3). It is built on aml-xgb-v2, exp-405, exp-407 and ds-aml-oot.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md, aml-alerts/ds-aml-oot.md

## Q3
Only one note of another project is built directly on bt-xgb-v3: pa-bal-forecast-v1 in promo-apr-test.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v2 rests on three dataset notes: ds-aml-alerts (via feat-aml-kyc-band and exp-404), ds-aml-cash-txn (via feat-aml-round-amount, feat-aml-cash-velocity and the v1 features), and ds-aml-dispositions (via aml-xgb-v1).
Notes: aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md, aml-alerts/ds-aml-dispositions.md

## Q5
Both churn-gbm-2025-v2 and churn-lr-base-2025 build directly on feat-c25-txn-recency and feat-c25-payment-behaviour.
Notes: churn-2025/feat-c25-txn-recency.md, churn-2025/feat-c25-payment-behaviour.md

## Q6
bt-logit-baseline is still current and builds directly on feat-bt-util-3m, which was superseded by feat-bt-util-trend-v2.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md

## Q7
Three decision notes rest on feat-ae-push-open-v1: dec-ae-no-push-credit directly (via ae-score-v1 and fnd-ae-push-null), and dec-ae-score-v2 and dec-ae-dashboard through ae-score-v2, which is built on dec-ae-no-push-credit.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-dashboard.md

## Q8
bt-xgb-v1 was superseded by bt-xgb-v2, which was superseded by bt-xgb-v3, the note in force. bt-xgb-v3 is built on bt-xgb-v2, exp-107-margin-label and dec-bt-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/exp-107-margin-label.md, balance-transfer-propensity/dec-bt-margin-label.md

## Q9
Only one note of another project is built directly on feat-bsm-score-map-v2: ds-app-bureau-v10-pull in application-scorecard.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-v8-history (the root of the chain), ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026 and ds-bsm-app-dev-2024.
Notes: bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-app-dev-2024.md