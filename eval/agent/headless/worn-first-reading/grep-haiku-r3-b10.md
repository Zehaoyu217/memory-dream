## Q1
The dataset notes behind fsm-churn-xgb-v2 are ds-fsm-legacy-features (via fsm-churn-xgb-v1, feat-fsm-util-ratio and exp-101) and ds-fsm-parity-sample (via exp-101, exp-102 and exp-107).
Notes: feature-store-migration/ds-fsm-legacy-features.md, feature-store-migration/ds-fsm-parity-sample.md

## Q2
Nine model notes with no replacement build on a replaced feature: bt-logit-baseline, cb-uplift-v1, churn-lr-base-2025, csb-lr-base, cli-logreg-baseline, clv-bgnbd-v1, inc-linear-baseline, rdm-propensity-lr and ror-uplift-v1. bt-logit-baseline and clv-bgnbd-v1 are no longer used in production but have no replacement note, and churn-lr-base-2025, inc-linear-baseline and ror-uplift-v1 reach their replaced feature through a descriptive reference rather than an id.
Notes: balance-transfer-propensity/bt-logit-baseline.md, cashback-redesign/cb-uplift-v1.md, churn-2025/churn-lr-base-2025.md, churn-small-business/csb-lr-base.md, credit-line-increase/cli-logreg-baseline.md, customer-lifetime-value/clv-bgnbd-v1.md, income-estimation/inc-linear-baseline.md, reactivation-dormant/rdm-propensity-lr.md, retention-offers-roi/ror-uplift-v1.md

## Q3
Twenty-eight notes outside fraud-2025 rest on it: 23 in fraud-2026 and 5 in dispute-triage. They reach it through feat-f25-amt-ratio, feat-f25-device-age, feat-f25-velocity-v1, fraud25-gbm-v2, dec-f25-champion-v2 and fraud25-find-travel-overflag.
Notes: dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v3.md, dispute-triage/exp-307.md, dispute-triage/exp-308.md, dispute-triage/feat-disp-fraud-score.md, fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-promote-v3.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/exp-201.md, fraud-2026/exp-202.md, fraud-2026/exp-203.md, fraud-2026/exp-204.md, fraud-2026/exp-205.md, fraud-2026/exp-206.md, fraud-2026/exp-207.md, fraud-2026/exp-208.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/fraud26-find-geo-drift.md, fraud-2026/fraud26-find-label-bias.md, fraud-2026/fraud26-find-velocity-clean.md, fraud-2026/fraud26-find-velocity-leak.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/fraud26-gbm-v3.md, fraud-2026/q-f26-travel-rule.md

## Q4
Sixteen retention-offers-roi notes rest on churn-2025, through feat-ror-churn-score (built on churn-gbm-2025-v2) and the notes built on it. Several of these links are descriptive rather than by id, such as "the t-learner uplift model" for ror-uplift-v1.
Notes: retention-offers-roi/feat-ror-churn-score.md, retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/exp-403.md, retention-offers-roi/ror-roi-v1.md, retention-offers-roi/exp-404.md, retention-offers-roi/fnd-ror-realloc-gain.md, retention-offers-roi/fnd-ror-cashback-roi.md, retention-offers-roi/exp-405.md, retention-offers-roi/fnd-ror-cashback-roi-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md, retention-offers-roi/exp-406.md, retention-offers-roi/exp-407.md, retention-offers-roi/ror-roi-v2.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/feat-ror-value-band-v2.md

## Q5
Twelve revenue-forecast-2026 notes rest on spend-forecasting, all through sfc-hier-v3 via ds-rev26-spend-volume and rev26-combined-v1.
Notes: revenue-forecast-2026/dec-rev26-cap-scenario-separate.md, revenue-forecast-2026/dec-rev26-p10-p90-bands.md, revenue-forecast-2026/dec-rev26-v2-for-board.md, revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/exp-301.md, revenue-forecast-2026/exp-305.md, revenue-forecast-2026/exp-307.md, revenue-forecast-2026/feat-rev26-volume-lag.md, revenue-forecast-2026/fnd-rev26-apr-sensitivity.md, revenue-forecast-2026/fnd-rev26-volume-driven.md, revenue-forecast-2026/rev26-combined-v1.md, revenue-forecast-2026/rev26-interchange-v1.md

## Q6
Only one line qualifies: dec-cb-extend-flat-pilot was replaced by dec-cb-adopt-banded-tiers, which was itself replaced by dec-cb-threshold-2500.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md

## Q7
Sixteen lines of model replacements qualify, and each is listed by its first note. churn-2025/churn-gbm-2025 is the one line whose link is descriptive: churn-gbm-2025-v2 says the churn-2026 project "replaced this line" with its churn-xgb models.
Notes: aml-alerts/aml-xgb-v1.md, balance-transfer-propensity/bt-xgb-v1.md, call-center-routing/cr-lgbm-v1.md, churn-2025/churn-gbm-2025.md, collections-uplift/cu-uplift-v1.md, credit-line-increase/cli-xgb-v1.md, dispute-triage/disp-lgbm-v1.md, early-delinquency/ed-gbm-v1.md, fraud-2025/fraud25-gbm-v1.md, income-estimation/inc-gbm-v1.md, limit-decrease-policy/cld-gbm-v1.md, merchant-risk/mrisk-gbm-v1.md, payment-behavior-segments/pbs-kmeans-v1.md, recovery-scoring/rs-xgb-v1.md, spend-forecasting/sfc-ets-v1.md, txn-categorization/txc-logreg-v1.md

## Q8
Eighteen notes are built directly on a note of another project, all listed below. Edges to general folders are excluded.
Notes: application-scorecard/ds-app-bureau-v10-pull.md, application-scorecard/feat-app-income-est.md, collections-channel-mix/find-ch-sms-call-gap.md, customer-lifetime-value/exp-506.md, dispute-triage/feat-disp-fraud-score.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/q-f26-travel-rule.md, limit-decrease-policy/feat-cld-risk-band-v2.md, merchant-risk/feat-mrisk-dispute-ratio.md, model-monitoring/mm-limit-glm-v2.md, promo-apr-test/pa-bal-forecast-v1.md, retention-offers-roi/feat-ror-churn-score.md, revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md