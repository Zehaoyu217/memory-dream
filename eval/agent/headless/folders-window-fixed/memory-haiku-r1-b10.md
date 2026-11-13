## Q1
The dataset ancestry of `fsm-churn-xgb-v2` is `ds-fsm-legacy-features`, reached through `fsm-churn-xgb-v1` and `feat-fsm-util-ratio`. No other dataset is an ancestor; `ds-fsm-parity-sample` and `ds-fsm-store-registry` are descendants of the legacy dataset, not inputs to v2.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-churn-xgb-v1.md, feature-store-migration/feat-fsm-util-ratio.md, feature-store-migration/ds-fsm-legacy-features.md

## Q2
Ten current model notes build directly on a replaced feature note: `cb-elasticity-v1` and `cb-uplift-v1` (on `feat-cb-spend-base`), `bt-logit-baseline` (on `feat-bt-util-3m`), `churn-lr-base-2025` (on `feat-c25-util-v1`), `csb-lr-base` (on `feat-csb-spend-raw`), `cli-logreg-baseline` (on `feat-cli-util-v1`), `mq3-response-gbm-v1` (on `feat-mq3-recency-v1`), `rdm-propensity-lr` (on `feat-rdm-last-activity-v1`), `ror-uplift-v1` (on `feat-ror-value-band-v1`), and `inc-linear-baseline` (on `feat-inc-payroll-cadence-v1`). None of the replaced inputs is a dataset note.
Notes: cashback-redesign/cb-elasticity-v1.md, cashback-redesign/cb-uplift-v1.md, balance-transfer-propensity/bt-logit-baseline.md, churn-2025/churn-lr-base-2025.md, churn-small-business/csb-lr-base.md, credit-line-increase/cli-logreg-baseline.md, marketing-uplift-q3/mq3-response-gbm-v1.md, reactivation-dormant/rdm-propensity-lr.md, retention-offers-roi/ror-uplift-v1.md, income-estimation/inc-linear-baseline.md

## Q3
28 notes outside `fraud-2025` rest on it, directly or through other notes: 23 in `fraud-2026` and 5 in `dispute-triage`. The direct cross-folder links include `fraud-2026/feat-f26-amt-zscore` (on `feat-f25-amt-ratio`), `fraud-2026/feat-f26-device-age` (on `feat-f25-device-age`), and `fraud-2026/fraud26-gbm-v1` (on `fraud25-gbm-v2`).
Notes: fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/dec-f26-replace-f25.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v3.md, dispute-triage/feat-disp-fraud-score.md

## Q4
16 notes outside `churn-2025` rest on it, all in `retention-offers-roi`. The direct link is `retention-offers-roi/feat-ror-churn-score`, which builds on `churn-2025/churn-gbm-2025-v2`; the other 15 depend on it through that feature or the models built from it.
Notes: retention-offers-roi/feat-ror-churn-score.md, churn-2025/churn-gbm-2025-v2.md, retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/ror-roi-v1.md, retention-offers-roi/ror-roi-v2.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q5
12 notes outside `spend-forecasting` rest on it, all in `revenue-forecast-2026`. The direct links are `revenue-forecast-2026/ds-rev26-spend-volume` and `revenue-forecast-2026/rev26-combined-v1`, which both use `spend-forecasting/sfc-hier-v3`; the other 10 depend on those through their own chains.
Notes: spend-forecasting/sfc-hier-v3.md, revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md, revenue-forecast-2026/feat-rev26-volume-lag.md, revenue-forecast-2026/rev26-interchange-v1.md

## Q6
One decision note qualifies: `cashback-redesign/dec-cb-extend-flat-pilot` was replaced by `dec-cb-adopt-banded-tiers`, which was itself later replaced by `dec-cb-threshold-2500`. Every other decision chain in the list has length two or less.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md

## Q7
Seventeen model notes were replaced by a model that was later replaced: `aml-xgb-v1`, `bt-xgb-v1`, `cr-lgbm-v1`, `cu-uplift-v1`, `cli-xgb-v1`, `disp-lgbm-v1`, `ed-gbm-v1`, `fraud25-gbm-v1`, `fraud25-gbm-v2`, `fraud26-gbm-v1`, `inc-gbm-v1`, `cld-gbm-v1`, `mrisk-gbm-v1`, `pbs-kmeans-v1`, `rs-xgb-v1`, `sfc-ets-v1`, and `txc-logreg-v1`. Each one sits at the start of a chain of three or more model notes.
Notes: aml-alerts/aml-xgb-v1.md, balance-transfer-propensity/bt-xgb-v1.md, call-center-routing/cr-lgbm-v1.md, collections-uplift/cu-uplift-v1.md, credit-line-increase/cli-xgb-v1.md, dispute-triage/disp-lgbm-v1.md, early-delinquency/ed-gbm-v1.md, fraud-2025/fraud25-gbm-v1.md, fraud-2025/fraud25-gbm-v2.md, fraud-2026/fraud26-gbm-v1.md, income-estimation/inc-gbm-v1.md, limit-decrease-policy/cld-gbm-v1.md, merchant-risk/mrisk-gbm-v1.md, payment-behavior-segments/pbs-kmeans-v1.md, recovery-scoring/rs-xgb-v1.md, spend-forecasting/sfc-ets-v1.md, txn-categorization/txc-logreg-v1.md

## Q8
These are the direct cross-folder built-on links I could verify, excluding general folders: `fraud-2026` notes on `fraud-2025` notes; `dispute-triage/feat-disp-fraud-score` on `fraud-2026/fraud26-gbm-v3`; `retention-offers-roi/feat-ror-churn-score` on `churn-2025/churn-gbm-2025-v2`; `revenue-forecast-2026` notes on `spend-forecasting/sfc-hier-v3`; `model-monitoring/mm-limit-glm-v2` on `feature-store-migration/feat-fsm-util-ratio`; `application-scorecard/feat-app-income-est` on `income-estimation/inc-gbm-v3`; `promo-apr-test/pa-bal-forecast-v1` on `balance-transfer-propensity/bt-xgb-v3`; and `customer-lifetime-value/exp-506` on `reactivation-dormant/rdm-uplift-v1`. I did not scan every feature and experiment note in every folder, so this list may be incomplete.
Notes: fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/q-f26-travel-rule.md, dispute-triage/feat-disp-fraud-score.md, retention-offers-roi/feat-ror-churn-score.md, revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md, model-monitoring/mm-limit-glm-v2.md, application-scorecard/feat-app-income-est.md, promo-apr-test/pa-bal-forecast-v1.md, customer-lifetime-value/exp-506.md