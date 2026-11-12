## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018, directly or through the aml-xgb and aml-find notes built on it.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md
## Q2
The note in force at the end of the aml-xgb-v1 line is aml-xgb-v3 (aml-xgb-v1 was superseded by aml-xgb-v2, which was superseded by aml-xgb-v3). aml-xgb-v3 is built directly on aml-xgb-v2, exp-405, exp-407 and ds-aml-oot.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md, aml-alerts/ds-aml-oot.md
## Q3
One note of another project is built directly on bt-xgb-v3: promo-apr-test/pa-bal-forecast-v1, which lists it in its from-line alongside ds-pa-balance-panel and feat-pa-bt-inflow-v2. The only other direct dependent, dec-bt-cut-mailer-top30, is in the same project.
Notes: promo-apr-test/pa-bal-forecast-v1.md
## Q4
aml-xgb-v2 rests, back to the start, on three dataset notes: ds-aml-alerts, ds-aml-cash-txn and ds-aml-dispositions.
Notes: aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md, aml-alerts/ds-aml-dispositions.md, aml-alerts/aml-xgb-v2.md
## Q5
Both churn-gbm-2025-v2 and churn-lr-base-2025 build directly on feat-c25-txn-recency and feat-c25-payment-behaviour.
Notes: churn-2025/feat-c25-txn-recency.md, churn-2025/feat-c25-payment-behaviour.md, churn-2025/churn-gbm-2025-v2.md, churn-2025/churn-lr-base-2025.md
## Q6
bt-logit-baseline is the only current model that builds directly on a replaced feature or dataset note: it rests on feat-bt-util-3m, which was replaced by feat-bt-util-trend-v2. bt-xgb-v3 is current but builds directly only on models, experiments and a decision, not on any replaced feature or dataset.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md
## Q7
Three decision notes rest on feat-ae-push-open-v1: dec-ae-no-push-credit, dec-ae-score-v2 and dec-ae-dashboard, directly or through ae-score-v1 and the other notes built on it.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-dashboard.md
## Q8
The note in force at the end of the bt-xgb-v1 line is bt-xgb-v3 (bt-xgb-v1 was superseded by bt-xgb-v2, which was superseded by bt-xgb-v3). bt-xgb-v3 is built directly on bt-xgb-v2, exp-107-margin-label and dec-bt-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/exp-107-margin-label.md, balance-transfer-propensity/dec-bt-margin-label.md
## Q9
One note of another project is built directly on feat-bsm-score-map-v2: application-scorecard/ds-app-bureau-v10-pull, which re-scores the 2024 and 2025 applications on the mapped v10 bureau score.
Notes: application-scorecard/ds-app-bureau-v10-pull.md
## Q10
bsm-app-gbm-v10b rests, back to the start, on four dataset notes: ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026, ds-bsm-app-dev-2024 and ds-bsm-v8-history.
Notes: bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/bsm-app-gbm-v10b.md