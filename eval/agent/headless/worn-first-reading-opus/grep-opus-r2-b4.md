## Q1
Four decision notes rest on it. ds-cr-ivr-paths feeds feat-cr-ivr-path-v1, which feeds cr-lgbm-v1 and the logistic baseline. From there the chain reaches dec-cr-lgbm directly, dec-cr-caller-v2 through exp-104 and fnd-cr-leak-corrected, and dec-cr-cost-matrix and dec-cr-pilot through exp-105, cr-lgbm-v2 and cr-lgbm-v3.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v2 replaced cli-xgb-v1, and cli-xgb-v3 (the T-learner uplift model) replaced cli-xgb-v2, so cli-xgb-v3 is in force now. It is built on exp-106 (the out-of-time AUC check for v2), exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only merchant-risk's feat-mrisk-dispute-ratio is built directly on ds-disp-merchant-link. dec-mrisk-dispute-feature mentions the dependency, but it is built on the feature note, not on the dataset.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
Going back through exp-101, the logistic baseline and the caller-history, IVR-path, tenure and TF-IDF features, cr-lgbm-v1 rests on two dataset notes. These are ds-cr-calls (the inbound calls table) and ds-cr-ivr-paths, which itself is built on ds-cr-calls.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both models build directly on four shared features: amount ratio, device age, hour band and velocity v1. v2 also adds feat-f25-mcc-travel.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
The answer is clv-bgnbd-v1. No note replaces it, and it is still kept as marketing's sanity check. It builds directly on the six-month average revenue feature (feat-clv-arpu-v1), which feat-clv-arpu-v2 has replaced. clv-ml-v2 is current too, but it already uses arpu v2.
Notes: customer-lifetime-value/clv-bgnbd-v1.md

## Q7
Three decision notes rest on it. ds-cb-spend-panel feeds the pilot dataset, feat-cb-spend-base and the merchant categories. These lead through cb-elasticity-v1/v2, find-cb-flat-wins and cb-sim-v1/exp-206 to dec-cb-extend-flat-pilot, dec-cb-adopt-banded-tiers and dec-cb-threshold-2500.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v2 replaced disp-lgbm-v1, and disp-lgbm-v3 replaced disp-lgbm-v2, so disp-lgbm-v3 is the current classifier. It is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only model-monitoring's mm-limit-glm-v2 is built directly on feat-fsm-util-ratio, where it takes the place of the legacy utilisation field.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 is built on the pilot dataset and feat-cb-spend-base, and both of those are built on the spend panel. So it rests on ds-cb-pilot-2025q4 and ds-cb-spend-panel.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md