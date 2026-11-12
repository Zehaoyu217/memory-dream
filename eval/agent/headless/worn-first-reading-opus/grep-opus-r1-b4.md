I've read every note the questions touch and checked other projects for cross-references; here are the answers.

## Q1
Four decision notes rest on ds-cr-ivr-paths. The chain runs through feat-cr-ivr-path-v1 into cr-logreg-v1 and cr-lgbm-v1, which gives dec-cr-lgbm. From cr-lgbm-v1 it continues through exp-104 and fnd-cr-leak-corrected to dec-cr-caller-v2, and through cr-lgbm-v2 and cr-lgbm-v3 to dec-cr-cost-matrix and dec-cr-pilot. No other project builds on it.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v1 was replaced by cli-xgb-v2, and cli-xgb-v3 replaced that, so cli-xgb-v3 is in force now. It is built on exp-106 (the out-of-time AUC check for v2), exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only one note in another project builds directly on it: merchant-risk's feat-mrisk-dispute-ratio. merchant-risk's dec-mrisk-dispute-feature names the dependency, but it is built on feat-mrisk-dispute-ratio, not on the dataset itself.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
Traced back to the start, cr-lgbm-v1 rests on two dataset notes. One is ds-cr-calls, reached through caller history v1, the transcript TF-IDF feature and the IVR path feature. The other is ds-cr-ivr-paths, reached through feat-cr-ivr-path-v1, which also comes in via exp-101 and cr-logreg-v1. feat-cr-tenure-v1 does not build on any note.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both models build directly on four feature notes: amount ratio, device age, hour band and velocity v1. Only v2 adds the travel flag (feat-f25-mcc-travel).
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
The only such model is clv-bgnbd-v1. It was never replaced and is still kept as the marketing sanity check, but it builds on feat-clv-arpu-v1, which feat-clv-arpu-v2 replaced. clv-ml-v1 also used arpu v1, but it has been superseded itself, and clv-ml-v2 uses arpu v2.
Notes: customer-lifetime-value/clv-bgnbd-v1.md

## Q7
All three decision notes in the project rest on ds-cb-spend-panel. The pilot dataset and feat-cb-spend-base lead through cb-elasticity-v1 and find-cb-flat-wins to dec-cb-extend-flat-pilot. They also lead through cb-elasticity-v2 to dec-cb-adopt-banded-tiers and then dec-cb-threshold-2500. No other project builds on it.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v1 was replaced by disp-lgbm-v2, and disp-lgbm-v3 replaced that, so disp-lgbm-v3 is the current classifier. It is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 (the fraud score lift experiment) and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only one note in another project builds directly on it: model-monitoring's mm-limit-glm-v2, which uses the store util ratio in place of the legacy utilisation field.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 builds on ds-cb-pilot-2025q4 and feat-cb-spend-base, and both of those build on ds-cb-spend-panel. So it rests on two dataset notes: the pilot dataset and the spend panel.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md