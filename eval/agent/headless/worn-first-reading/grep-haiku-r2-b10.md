## Q1
The only dataset note in its chain is `ds-fsm-legacy-features` (ml.legacy_feats_v1). It reaches fsm-churn-xgb-v2 directly through feat-fsm-util-ratio and through the legacy churn model fsm-churn-xgb-v1, which exp-105 builds on. The other inputs are features with no dataset note behind them.
Notes: feature-store-migration/ds-fsm-legacy-features.md, feature-store-migration/feat-fsm-util-ratio.md, feature-store-migration/fsm-churn-xgb-v1.md, feature-store-migration/exp-105.md, feature-store-migration/fsm-churn-xgb-v2.md

## Q2
Ten current models build on a feature that has since been replaced: bt-logit-baseline, cb-uplift-v1, csb-lr-base, cli-logreg-baseline, rdm-propensity-lr, mq3-response-gbm-v1, churn-lr-base-2025, ror-uplift-v1, inc-linear-baseline and clv-bgnbd-v1. The last four name the replaced feature by description, not by id. Several of these are baselines retired from production, but no later note replaces them.
Notes: balance-transfer-propensity/bt-logit-baseline.md, cashback-redesign/cb-uplift-v1.md, churn-small-business/csb-lr-base.md, credit-line-increase/cli-logreg-baseline.md, reactivation-dormant/rdm-propensity-lr.md, marketing-uplift-q3/mq3-response-gbm-v1.md, churn-2025/churn-lr-base-2025.md, retention-offers-roi/ror-uplift-v1.md, income-estimation/inc-linear-baseline.md, customer-lifetime-value/clv-bgnbd-v1.md

## Q3
28 notes outside fraud-2025 rest on it: five in dispute-triage (through feat-disp-fraud-score, which builds on fraud26-gbm-v3) and 23 in fraud-2026. Four of the fraud-2026 notes are linked by description only (exp-206, exp-208, fraud26-find-geo-drift, dec-f26-maturity-60d).
Notes: dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v3.md, dispute-triage/exp-307.md, dispute-triage/exp-308.md, dispute-triage/feat-disp-fraud-score.md, fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-promote-v3.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/exp-201.md, fraud-2026/exp-202.md, fraud-2026/exp-203.md, fraud-2026/exp-204.md, fraud-2026/exp-205.md, fraud-2026/exp-206.md, fraud-2026/exp-207.md, fraud-2026/exp-208.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/fraud26-find-geo-drift.md, fraud-2026/fraud26-find-label-bias.md, fraud-2026/fraud26-find-velocity-clean.md, fraud-2026/fraud26-find-velocity-leak.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/fraud26-gbm-v3.md, fraud-2026/q-f26-travel-rule.md

## Q4
Three notes outside churn-2025 rest on it: feat-ror-churn-score builds directly on churn-gbm-2025-v2, exp-403 uses it through "the 60-day churn score feature", and ror-uplift-v1 builds on both.
Notes: retention-offers-roi/feat-ror-churn-score.md, retention-offers-roi/exp-403.md, retention-offers-roi/ror-uplift-v1.md

## Q5
Twelve revenue-forecast-2026 notes rest on spend-forecasting, all through sfc-hier-v3 (directly via ds-rev26-spend-volume and rev26-combined-v1, and through the notes built on those).
Notes: revenue-forecast-2026/dec-rev26-cap-scenario-separate.md, revenue-forecast-2026/dec-rev26-p10-p90-bands.md, revenue-forecast-2026/dec-rev26-v2-for-board.md, revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/exp-301.md, revenue-forecast-2026/exp-305.md, revenue-forecast-2026/exp-307.md, revenue-forecast-2026/feat-rev26-volume-lag.md, revenue-forecast-2026/fnd-rev26-apr-sensitivity.md, revenue-forecast-2026/fnd-rev26-volume-driven.md, revenue-forecast-2026/rev26-combined-v1.md, revenue-forecast-2026/rev26-interchange-v1.md

## Q6
One line: dec-cb-extend-flat-pilot was replaced by dec-cb-adopt-banded-tiers, which dec-cb-threshold-2500 replaced later. No other decision line has a replacement that was itself replaced.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md

## Q7
Fifteen replacement lines qualify, each starting at the first model note shown. The churn-gbm-2025 line is included on the strength of churn-gbm-2025-v2's own statement that churn-2026 later replaced it, not on a churn-2026 note.
Notes: aml-alerts/aml-xgb-v1.md, balance-transfer-propensity/bt-xgb-v1.md, call-center-routing/cr-lgbm-v1.md, churn-2025/churn-gbm-2025.md, collections-uplift/cu-uplift-v1.md, credit-line-increase/cli-xgb-v1.md, dispute-triage/disp-lgbm-v1.md, early-delinquency/ed-gbm-v1.md, fraud-2025/fraud25-gbm-v1.md, income-estimation/inc-gbm-v1.md, limit-decrease-policy/cld-gbm-v1.md, merchant-risk/mrisk-gbm-v1.md, payment-behavior-segments/pbs-kmeans-v1.md, recovery-scoring/rs-xgb-v1.md, spend-forecasting/sfc-ets-v1.md, txn-categorization/txc-logreg-v1.md

## Q8
Eighteen notes are built directly on a note of another project. Examples: fraud-2026/feat-f26-amt-zscore.md builds on fraud-2025/feat-f25-amt-ratio.md, and revenue-forecast-2026/rev26-combined-v1.md builds on spend-forecasting/sfc-hier-v3.md.
Notes: application-scorecard/ds-app-bureau-v10-pull.md, application-scorecard/feat-app-income-est.md, collections-channel-mix/find-ch-sms-call-gap.md, customer-lifetime-value/exp-506.md, dispute-triage/feat-disp-fraud-score.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/q-f26-travel-rule.md, limit-decrease-policy/feat-cld-risk-band-v2.md, merchant-risk/feat-mrisk-dispute-ratio.md, model-monitoring/mm-limit-glm-v2.md, promo-apr-test/pa-bal-forecast-v1.md, retention-offers-roi/feat-ror-churn-score.md, revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md