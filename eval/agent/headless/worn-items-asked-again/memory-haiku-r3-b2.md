## Q1
Both build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. Those are the only two feature notes they share as direct inputs.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
cb-uplift-v1 is the only current model that builds directly on a replaced input: it takes feat-cb-spend-base, which feat-cb-spend-band-v2 replaced. cb-elasticity-v1 has the same input but is itself replaced by cb-elasticity-v2, so it does not count.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md

## Q3
Four decisions rest on feat-app-util-new: dec-app-cutoff-v3, dec-app-cutoff-v4, dec-app-no-gbm and dec-app-rebuild-v4. The first two rest on it through app-scorecard-v3 and app-scorecard-v4, and the other two through the GBM and v4 chain.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-cutoff-v4.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md

## Q4
The note in force is cr-lgbm-v3 (cr-lgbm-v1 was replaced by v2, and v2 by v3). It builds directly on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only one note from another project is built directly on churn-gbm-2025-v2: feat-ror-churn-score in retention-offers-roi.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two datasets: ds-app-applications-2024 and ds-app-reject-sample. The first comes in through feat-app-util-new and the velocity and thin-file features, the second through the reject-inference question and exp-501.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
Only churn-lr-base-2025 is current and builds directly on a replaced feature: feat-c25-util-v1, which feat-c25-util-v2 replaced. churn-gbm-2025-v2 builds only on current inputs.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md

## Q9
Five decisions rest on ds-bt-offer-log: dec-bt-cut-mailer-top30, dec-bt-drop-post-offer-features and dec-bt-margin-label in balance-transfer-propensity, plus dec-pa-6m-default and dec-pa-no-12m-subprime in promo-apr-test. The last two come through the promo-apr-test models that build on the balance-transfer work.
Notes: balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
The note in force is dec-cb-threshold-2500 (dec-cb-extend-flat-pilot was replaced by dec-cb-adopt-banded-tiers, which was replaced by dec-cb-threshold-2500). It builds directly on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md