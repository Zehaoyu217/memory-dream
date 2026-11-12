## Q1
Both models build directly on two feature notes: feat-c25-payment-behaviour and feat-c25-txn-recency. The other features differ between them: the GBM v2 uses util-v2, while the logistic baseline uses app-sessions and util-v1.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
Two current models do: cb-elasticity-v1 and cb-uplift-v1. Both build on feat-cb-spend-base, which feat-cb-spend-band-v2 has since replaced.
Notes: cashback-redesign/cb-elasticity-v1.md, cashback-redesign/cb-uplift-v1.md

## Q3
Four decision notes do: dec-app-cutoff-v3, dec-app-rebuild-v4, dec-app-no-gbm and dec-app-cutoff-v4. They all come through app-scorecard-v3, the only note built directly on feat-app-util-new.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
cr-lgbm-v3 is in force now; it replaced both cr-lgbm-v1 and cr-lgbm-v2. It is built on cr-lgbm-v2 (now replaced), ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only one note from another project builds directly on churn-gbm-2025-v2: feat-ror-churn-score in retention-offers-roi.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample. The first comes through app-gbm-v1, app-scorecard-v3 and its features. The second comes through find-app-reject-inference-gain, exp-501 and q-app-reject-inference.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both models build directly on feat-csb-spend-raw (now replaced) and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
Only churn-lr-base-2025 does: it is still current and builds on feat-c25-util-v1, which feat-c25-util-v2 has replaced. The other current model, churn-gbm-2025-v2, uses only inputs that are still current.
Notes: churn-2025/churn-lr-base-2025.md

## Q9
Within balance-transfer-propensity, three decisions do: dec-bt-drop-post-offer-features, dec-bt-margin-label and dec-bt-cut-mailer-top30. In promo-apr-test, two more rest on it through other notes: dec-pa-6m-default and dec-pa-no-12m-subprime.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
dec-cb-threshold-2500 is in force now. It replaced dec-cb-adopt-banded-tiers, which had replaced dec-cb-extend-flat-pilot. It is built on dec-cb-adopt-banded-tiers (now replaced), exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md