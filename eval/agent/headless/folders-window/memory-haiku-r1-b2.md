## Q1
Both churn-gbm-2025-v2 and churn-lr-base-2025 build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. churn-gbm-2025-v2 also builds on feat-c25-util-v2, and churn-lr-base-2025 builds on the replaced feat-c25-util-v1 and feat-c25-app-sessions instead.
Notes: churn-2025/churn-gbm-2025-v2.md, churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
cb-uplift-v1 is still current and builds directly on feat-cb-spend-base, which was replaced by feat-cb-spend-band-v2. cb-elasticity-v1 also builds on feat-cb-spend-base, but cb-elasticity-v2's text says it replaces that 0.21 estimate, so it is effectively superseded even though the index does not mark it.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md, cashback-redesign/feat-cb-spend-band-v2.md, cashback-redesign/cb-elasticity-v1.md

## Q3
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3 and dec-app-no-gbm (through app-scorecard-v3 and app-gbm-v1 respectively), plus dec-app-rebuild-v4 and dec-app-cutoff-v4 (through app-gbm-v2, app-scorecard-v4 and exp-507). The decision-to-model links are from the chain output, not from reading each decision note.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
The line ends at cr-lgbm-v3, which is in force. It builds on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only one note of another project is built directly on churn-gbm-2025-v2: retention-offers-roi/feat-ror-churn-score. Other retention-offers-roi notes rest on churn-2025 only through that feature.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 directly, and ds-app-reject-sample through exp-501 and the reject-inference chain.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw and feat-csb-tenure-band. csb-xgb-v1 also builds on feat-csb-deposit-volatility.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
The only current churn-2025 model that builds directly on a replaced feature is churn-lr-base-2025, which uses feat-c25-util-v1, now replaced by feat-c25-util-v2. churn-gbm-2025-v2 uses only current features, and churn-gbm-2025 is superseded.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md, churn-2025/feat-c25-util-v2.md

## Q9
Five decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30 and dec-bt-margin-label in balance-transfer-propensity, plus dec-pa-6m-default and dec-pa-no-12m-subprime in promo-apr-test. The chain output also hints that one more note may be affected through words it names but that have no note, and I did not resolve that.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
The line ends at dec-cb-threshold-2500, which is in force. It builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md