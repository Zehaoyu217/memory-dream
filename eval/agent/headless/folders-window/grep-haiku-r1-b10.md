## Q1
fsm-churn-xgb-v2 rests on the legacy features dataset (ds-fsm-legacy-features, ml.legacy_feats_v1) through several paths. It builds on fsm-churn-xgb-v1 directly, and on exp-105 → feat-fsm-util-ratio → ds-fsm-legacy-features. It also builds on exp-101 and ds-fsm-parity-sample (via exp-107 and fnd-parity-pre-fix), and on feat-fsm-payment-lag-v2 → exp-102 → exp-101. The lineage of feat-fsm-spend-cv-30d was not traced.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-churn-xgb-v1.md, feature-store-migration/exp-105.md, feature-store-migration/feat-fsm-util-ratio.md, feature-store-migration/exp-107.md, feature-store-migration/fnd-parity-pre-fix.md, feature-store-migration/ds-fsm-parity-sample.md, feature-store-migration/exp-101.md, feature-store-migration/exp-102.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/ds-fsm-legacy-features.md

## Q2
None found in the dependency lines I captured. The current models' inputs that I could check (for example feat-fsm-payment-lag-v2 and feat-velocity-v3) are themselves current, and the feature-level builds-on lines for many current models were not captured, so this is a negative only for the captured lines.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, churn-2025/churn-gbm-2025.md

## Q3
Six fraud-2026 notes rest directly on fraud-2025 notes: fraud26-gbm-v1 (on feat-f25-velocity-v1 and fraud25-gbm-v2), feat-f26-amt-zscore, feat-f26-device-age, feat-f26-velocity-v2, dec-f26-replace-f25 (on dec-f25-champion-v2), and q-f26-travel-rule (on fraud25-find-travel-overflag). dispute-triage's feat-disp-fraud-score, disp-lgbm-v3 and dec-disp-fraud-score-in reach fraud-2025 only through fraud26-gbm-v3, whose own builds-on line I did not capture, so that link is unconfirmed.
Notes: fraud-2026/fraud26-gbm-v1.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/q-f26-travel-rule.md

## Q4
One direct cross-project dependency: retention-offers-roi's feat-ror-churn-score builds on churn-2025's churn-gbm-2025-v2. Earlier notes also flagged ror-uplift-v1 as an indirect dependent, but I did not capture its dependency line, so it is unverified.
Notes: retention-offers-roi/feat-ror-churn-score.md, churn-2025/churn-gbm-2025-v2.md

## Q5
Two revenue-forecast-2026 notes rest directly on spend-forecasting's sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1. I found no further notes that build on those two.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md, spend-forecasting/sfc-hier-v3.md

## Q6
One chain: cashback-redesign's dec-cb-extend-flat-pilot was replaced by dec-cb-adopt-banded-tiers, which was later replaced by dec-cb-threshold-2500. No other decision note chain has a second replacement in the captured lines.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md

## Q7
Thirteen model chains have a second replacement: aml-xgb-v1, bt-xgb-v1, cr-lgbm-v1, inc-gbm-v1, disp-lgbm-v1, mrisk-gbm-v1, pbs-kmeans-v1, rs-xgb-v1, txc-logreg-v1, cu-uplift-v1, cli-xgb-v1, cld-gbm-v1, and fraud26-gbm-v1. fraud25-gbm-v3 may extend the fraud-2025 chain, but its replacement status was not stated in the captured lines, so I left it out.
Notes: aml-alerts/aml-xgb-v1.md, balance-transfer-propensity/bt-xgb-v1.md, call-center-routing/cr-lgbm-v1.md, income-estimation/inc-gbm-v1.md, dispute-triage/disp-lgbm-v1.md, merchant-risk/mrisk-gbm-v1.md, payment-behavior-segments/pbs-kmeans-v1.md, recovery-scoring/rs-xgb-v1.md, txn-categorization/txc-logreg-v1.md, collections-uplift/cu-uplift-v1.md, credit-line-increase/cli-xgb-v1.md, limit-decrease-policy/cld-gbm-v1.md, fraud-2026/fraud26-gbm-v1.md

## Q8
Direct cross-project builds: application-scorecard (feat-app-income-est → income-estimation, ds-app-bureau-v10-pull → bureau-score-migration), collections-channel-mix (find-ch-sms-call-gap → collections-uplift), customer-lifetime-value (exp-506 → reactivation-dormant), dispute-triage (feat-disp-fraud-score → fraud-2026), limit-decrease-policy (feat-cld-risk-band-v2 → credit-line-increase), merchant-risk (two notes → dispute-triage's ds-disp-merchant-link), promo-apr-test (pa-bal-forecast-v1 → balance-transfer-propensity), retention-offers-roi (feat-ror-churn-score → churn-2025), revenue-forecast-2026 (two notes → spend-forecasting), model-monitoring (mm-limit-glm-v2 → feature-store-migration), and fraud-2026 (six notes → fraud-2025). Dependency lines not captured in my reads could add to this list.
Notes: application-scorecard/feat-app-income-est.md, application-scorecard/ds-app-bureau-v10-pull.md, collections-channel-mix/find-ch-sms-call-gap.md, customer-lifetime-value/exp-506.md, dispute-triage/feat-disp-fraud-score.md, limit-decrease-policy/feat-cld-risk-band-v2.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/dec-mrisk-dispute-feature.md, promo-apr-test/pa-bal-forecast-v1.md, retention-offers-roi/feat-ror-churn-score.md, revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md, model-monitoring/mm-limit-glm-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/q-f26-travel-rule.md