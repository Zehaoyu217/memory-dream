I have all eight answers. In the notes, links to other projects are written as full paths, so links described only in words were matched to notes in the same project.

## Q1
fsm-churn-xgb-v2 rests on two dataset notes. The legacy features dataset reaches it directly through fsm-churn-xgb-v1, feat-fsm-util-ratio and the payment-lag features. The frozen parity sample reaches it through exp-107, fnd-parity-pre-fix and exp-101.
Notes: feature-store-migration/ds-fsm-legacy-features.md, feature-store-migration/ds-fsm-parity-sample.md

## Q2
Ten current models, mostly baselines, still read a feature that has since been replaced (for example util-v1, the raw spend feature, payroll-cadence-v1, value-band-v1 and last-activity-v1). None of them was itself replaced.
Notes: churn-2025/churn-lr-base-2025.md, cashback-redesign/cb-uplift-v1.md, churn-small-business/csb-lr-base.md, marketing-uplift-q3/mq3-response-gbm-v1.md, income-estimation/inc-linear-baseline.md, credit-line-increase/cli-logreg-baseline.md, balance-transfer-propensity/bt-logit-baseline.md, reactivation-dormant/rdm-propensity-lr.md, customer-lifetime-value/clv-bgnbd-v1.md, retention-offers-roi/ror-uplift-v1.md

## Q3
Most of fraud-2026 rests on fraud-2025, through its velocity, device-age and amount-ratio features, the fraud25-gbm-v2 model and the champion decision. The dispute-triage v3 line also rests on it, through the fraud26-gbm-v3 score feature.
Notes: fraud-2026/dec-f26-replace-f25.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/fraud26-gbm-v3.md, fraud-2026/q-f26-travel-rule.md, fraud-2026/exp-201.md, fraud-2026/exp-202.md, fraud-2026/exp-203.md, fraud-2026/exp-204.md, fraud-2026/exp-205.md, fraud-2026/exp-206.md, fraud-2026/exp-207.md, fraud-2026/exp-208.md, fraud-2026/fraud26-find-label-bias.md, fraud-2026/fraud26-find-velocity-leak.md, fraud-2026/fraud26-find-velocity-clean.md, fraud-2026/fraud26-find-geo-drift.md, fraud-2026/dec-f26-maturity-60d.md, fraud-2026/dec-f26-promote-v2.md, fraud-2026/dec-f26-promote-v3.md, dispute-triage/feat-disp-fraud-score.md, dispute-triage/exp-307.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v3.md, dispute-triage/exp-308.md

## Q4
retention-offers-roi rests on churn-2025 through feat-ror-churn-score, which uses churn-gbm-2025-v2. From there it spreads to the uplift and ROI models, the findings built on them, value band v2 and the matrix decisions.
Notes: retention-offers-roi/feat-ror-churn-score.md, retention-offers-roi/exp-403.md, retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/ror-roi-v1.md, retention-offers-roi/exp-404.md, retention-offers-roi/exp-407.md, retention-offers-roi/fnd-ror-realloc-gain.md, retention-offers-roi/fnd-ror-cashback-roi.md, retention-offers-roi/ror-roi-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/exp-405.md, retention-offers-roi/fnd-ror-cashback-roi-v2.md, retention-offers-roi/feat-ror-value-band-v2.md, retention-offers-roi/exp-406.md, retention-offers-roi/dec-ror-matrix-v4.md, retention-offers-roi/dec-ror-value-band-v2.md

## Q5
revenue-forecast-2026 rests on spend-forecasting through sfc-hier-v3. That model feeds the spend-volume dataset and rev26-combined-v1, and from there the interchange model, the cap and band analyses, and the board decisions.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/feat-rev26-volume-lag.md, revenue-forecast-2026/rev26-interchange-v1.md, revenue-forecast-2026/exp-301.md, revenue-forecast-2026/exp-305.md, revenue-forecast-2026/fnd-rev26-volume-driven.md, revenue-forecast-2026/rev26-combined-v1.md, revenue-forecast-2026/exp-307.md, revenue-forecast-2026/fnd-rev26-apr-sensitivity.md, revenue-forecast-2026/dec-rev26-cap-scenario-separate.md, revenue-forecast-2026/dec-rev26-p10-p90-bands.md, revenue-forecast-2026/dec-rev26-v2-for-board.md

## Q6
Only one decision line has more than one replacement: the flat-pilot extension was replaced by the banded-tiers decision, which dec-cb-threshold-2500 then replaced. Every other decision was replaced only once.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md

## Q7
Fifteen model lines were replaced at least twice. The longest starts at fraud25-gbm-v1 and runs through fraud25-gbm-v2 into fraud26-gbm-v1, v2 and v3.
Notes: aml-alerts/aml-xgb-v1.md, balance-transfer-propensity/bt-xgb-v1.md, call-center-routing/cr-lgbm-v1.md, collections-uplift/cu-uplift-v1.md, credit-line-increase/cli-xgb-v1.md, dispute-triage/disp-lgbm-v1.md, early-delinquency/ed-gbm-v1.md, fraud-2025/fraud25-gbm-v1.md, income-estimation/inc-gbm-v1.md, limit-decrease-policy/cld-gbm-v1.md, merchant-risk/mrisk-gbm-v1.md, payment-behavior-segments/pbs-kmeans-v1.md, recovery-scoring/rs-xgb-v1.md, spend-forecasting/sfc-ets-v1.md, txn-categorization/txc-logreg-v1.md

## Q8
Eighteen notes are built directly on a note from another project. Six are in fraud-2026 (all on fraud-2025), and the rest each link to one other project, such as income-estimation, bureau-score-migration, churn-2025 or spend-forecasting.
Notes: application-scorecard/ds-app-bureau-v10-pull.md, application-scorecard/feat-app-income-est.md, collections-channel-mix/find-ch-sms-call-gap.md, customer-lifetime-value/exp-506.md, dispute-triage/feat-disp-fraud-score.md, fraud-2026/dec-f26-replace-f25.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/q-f26-travel-rule.md, limit-decrease-policy/feat-cld-risk-band-v2.md, merchant-risk/feat-mrisk-dispute-ratio.md, model-monitoring/mm-limit-glm-v2.md, promo-apr-test/pa-bal-forecast-v1.md, retention-offers-roi/feat-ror-churn-score.md, revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md