## Q1
Both models build directly on feat-c25-txn-recency and feat-c25-payment-behaviour. Those two are the only feature notes in both direct source lists.
Notes: churn-2025/churn-gbm-2025-v2.md, churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-txn-recency.md, churn-2025/feat-c25-payment-behaviour.md

## Q2
cb-uplift-v1 is the only current model that builds directly on a replaced feature. It uses feat-cb-spend-base, which feat-cb-spend-band-v2 superseded.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md, cashback-redesign/feat-cb-spend-band-v2.md

## Q3
Four decision notes rest on feat-app-util-new. dec-app-cutoff-v3 uses it directly through app-scorecard-v3. The other three reach it through app-scorecard-v3 and app-gbm-v1 (via exp-503, exp-504, find-app-gini-v3-drift, app-gbm-v2 and app-scorecard-v4).
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-cutoff-v4.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md

## Q4
cr-lgbm-v3 is the one in force. It was built on cr-lgbm-v2, fnd-cr-threshold, ds-cr-intent-labels and exp-106.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/fnd-cr-threshold.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md

## Q5
Only feat-ror-churn-score in retention-offers-roi is built directly on churn-gbm-2025-v2. ror-uplift-v1 uses it only indirectly.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample. The first feeds the scorecard and feature chain, and the second feeds the reject-inference branch through q-app-reject-inference and exp-501.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md, application-scorecard/app-gbm-v2.md, application-scorecard/app-gbm-v1.md, application-scorecard/app-scorecard-v3.md, application-scorecard/feat-app-util-new.md, application-scorecard/feat-app-thin-file.md, application-scorecard/feat-app-velocity-apps.md, application-scorecard/find-app-reject-inference-gain.md, application-scorecard/exp-501.md, application-scorecard/q-app-reject-inference.md

## Q7
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/csb-xgb-v1.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is the only current churn-2025 model built directly on a replaced feature. It uses feat-c25-util-v1, which feat-c25-util-v2 superseded.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md, churn-2025/feat-c25-util-v2.md

## Q9
Three decision notes rest on ds-bt-offer-log. dec-bt-drop-post-offer-features reaches it through find-bt-limit-leak and exp-104. dec-bt-margin-label and dec-bt-cut-mailer-top30 reach it through bt-xgb-v2, exp-107 and bt-xgb-v3.
Notes: balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/dec-bt-drop-post-offer-features.md

## Q10
dec-cb-threshold-2500 is the one in force. It was built on dec-cb-adopt-banded-tiers, find-cb-breakeven-lift and exp-206-breakeven-sim.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/find-cb-breakeven-lift.md, cashback-redesign/exp-206-breakeven-sim.md