## Q1
Four decision notes rest on ds-cr-ivr-paths, all through feat-cr-ivr-path-v1. dec-cr-lgbm comes through cr-lgbm-v1 and cr-logreg-v1. dec-cr-caller-v2 comes through exp-104 and fnd-cr-leak-corrected. dec-cr-cost-matrix and dec-cr-pilot come through cr-lgbm-v2 and cr-lgbm-v3.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
The line runs cli-xgb-v1 → cli-xgb-v2 → cli-xgb-v3, and cli-xgb-v3 is in force now. It builds on exp-106 (its note calls it "the out-of-time auc check for v2"), exp-107 and find-cli-uplift-wins. It also replaces cli-xgb-v2 and reuses the v2 feature set.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only merchant-risk/feat-mrisk-dispute-ratio builds directly on ds-disp-merchant-link. merchant-risk/dec-mrisk-dispute-feature mentions the dependency, but it builds on feat-mrisk-dispute-ratio, not on the dataset itself.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes. ds-cr-ivr-paths comes through feat-cr-ivr-path-v1. ds-cr-calls comes through ds-cr-ivr-paths, feat-cr-caller-history-v1 and feat-cr-transcript-tfidf-v1, and through exp-101 → cr-logreg-v1. feat-cr-tenure-v1 is built on no note.
Notes: call-center-routing/ds-cr-ivr-paths.md, call-center-routing/ds-cr-calls.md

## Q5
Both models build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. Only v2 adds feat-f25-mcc-travel.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. The only current model is clv-ml-v2, and it builds directly on feat-clv-arpu-v2 and feat-clv-hazard, which are both still current. The model that used the replaced feat-clv-arpu-v1, clv-bgnbd-v1, has itself been replaced by clv-ml-v2.
Notes: customer-lifetime-value/clv-ml-v2.md

## Q7
Three decision notes rest on ds-cb-spend-panel. dec-cb-extend-flat-pilot comes through ds-cb-pilot-2025q4 → cb-elasticity-v1 → find-cb-flat-wins. dec-cb-adopt-banded-tiers comes through cb-elasticity-v2. dec-cb-threshold-2500 comes through dec-cb-adopt-banded-tiers and exp-206-breakeven-sim (cb-sim-v1).
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
The line runs disp-lgbm-v1 → disp-lgbm-v2 → disp-lgbm-v3, and disp-lgbm-v3 is the current classifier. It builds on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only model-monitoring/mm-limit-glm-v2 builds directly on feat-fsm-util-ratio. It uses the feature in place of the legacy utilisation field.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel through both the pilot and feat-cb-spend-base. The chain ends at ds-cb-spend-panel, which names cb_spend_panel.sql and cards.txn_daily as its sources, but neither has a note in the memory.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md