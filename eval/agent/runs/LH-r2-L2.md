## Q1
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q2
None. The only current churn-2025 model is churn-gbm-2025-v2, and its direct inputs (exp-106, feat-c25-util-v2, feat-c25-txn-recency, feat-c25-payment-behaviour, dec-c25-drop-app-sessions) are not marked superseded.
Notes: churn-2025/churn-gbm-2025-v2.md

## Q3
Three decisions rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (via exp-303 and find-bsm-psi-after-map), dec-bsm-cutover-2026q3, and dec-bsm-keep-v8-fallback.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q4
The note in force is cr-lgbm-v3 (LightGBM v3, macro F1 0.74 on cr-oot-2026h1). It is built directly on cr-lgbm-v2, fnd-cr-threshold, ds-cr-intent-labels and exp-106.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/fnd-cr-threshold.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md

## Q5
Only one note from another project is built directly on churn-gbm-2025-v2: feat-ror-churn-score in retention-offers-roi.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q7
Both build directly on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour.
Notes: credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-pay-behaviour.md

## Q8
csb-lr-base, which is still current as the monitoring challenger, builds directly on feat-csb-spend-raw, and that feature has been superseded by feat-csb-spend-sa-v2. The current scoring model csb-xgb-v2 has no replaced inputs.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md

## Q9
Three decisions rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q10
The note in force is dec-cb-threshold-2500 (top tier at $2,500 for Q3 2026). It is built directly on find-cb-breakeven-lift, exp-206-breakeven-sim and dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/find-cb-breakeven-lift.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/dec-cb-adopt-banded-tiers.md