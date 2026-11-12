## Q1
Both build directly on feat-csb-spend-raw and feat-csb-tenure-band (csb-lr-base and csb-xgb-v1 both list these two as direct sources).
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q2
None. The only current churn-2025 model is churn-gbm-2025-v2, and its direct sources (feat-c25-util-v2, feat-c25-txn-recency, feat-c25-payment-behaviour, exp-106, dec-c25-drop-app-sessions) are not marked as replaced.
Notes: churn-2025/churn-gbm-2025-v2.md

## Q3
Three decision notes: dec-bsm-isotonic-map (directly on ds-bsm-v10-cohorts-2026 via exp-303), dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback (both through other notes built on it).
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q4
The line runs cr-lgbm-v1, then cr-lgbm-v2, then cr-lgbm-v3. cr-lgbm-v3 is the one in force (macro F1 0.74 on cr-oot-2026h1). It builds directly on cr-lgbm-v2, fnd-cr-threshold, ds-cr-intent-labels and exp-106.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/fnd-cr-threshold.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md

## Q5
One note: feat-ror-churn-score in retention-offers-roi, built directly on churn-gbm-2025-v2.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through the feature notes.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q7
Three feature notes are shared directly: feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour.
Notes: credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-pay-behaviour.md

## Q8
csb-lr-base, which is still in use as the monitoring challenger (no superseding note). It builds directly on feat-csb-spend-raw, which has been replaced by feat-csb-spend-sa-v2. The current model csb-xgb-v2 builds on no replaced feature or dataset.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md

## Q9
Three decision notes: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. Each rests on ds-cb-spend-panel directly or through other notes.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q10
The line runs dec-cb-extend-flat-pilot, then dec-cb-adopt-banded-tiers, then dec-cb-threshold-2500. dec-cb-threshold-2500 is in force (top tier at $2,500). It builds directly on find-cb-breakeven-lift, exp-206-breakeven-sim and dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/find-cb-breakeven-lift.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/dec-cb-adopt-banded-tiers.md