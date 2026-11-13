## Q1
Four decisions depend on ds-cr-ivr-paths. It feeds feat-cr-ivr-path-v1, which feeds cr-logreg-v1 and cr-lgbm-v1. That makes dec-cr-lgbm depend on it. Through exp-104 → fnd-cr-leak-corrected it reaches dec-cr-caller-v2, and through cr-lgbm-v2/v3 and fnd-cr-threshold it reaches dec-cr-cost-matrix and dec-cr-pilot.
Notes: work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-cost-matrix.md, work/dec-cr-pilot.md

## Q2
The line runs cli-xgb-v1 → cli-xgb-v2 → cli-xgb-v3, and cli-xgb-v3 is the one in force now. It is built on exp-106-credit-line-increase (the out-of-time AUC check for v2), exp-107-credit-line-increase and find-cli-uplift-wins.
Notes: work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls and ds-cr-ivr-paths. ds-cr-ivr-paths comes in through feat-cr-ivr-path-v1 (directly and via exp-101 → cr-logreg-v1). ds-cr-calls comes in through the caller-history and TF-IDF features, and ds-cr-ivr-paths is itself built on it.
Notes: work/ds-cr-calls.md, work/ds-cr-ivr-paths.md

## Q4
Both models build directly on the same four feature notes: amount ratio, device age, hour band and velocity v1. Only v2 adds the travel flag (feat-f25-mcc-travel), and the shared label-lag note is a dataset, not a feature.
Notes: work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decisions depend on ds-cb-spend-panel. The path runs through ds-cb-pilot-2025q4 and feat-cb-spend-base into cb-elasticity-v1. From there find-cb-flat-wins leads to dec-cb-extend-flat-pilot, and cb-elasticity-v2 leads to dec-cb-adopt-banded-tiers and then dec-cb-threshold-2500.
Notes: work/dec-cb-extend-flat-pilot.md, work/dec-cb-adopt-banded-tiers.md, work/dec-cb-threshold-2500.md

## Q6
The line runs disp-lgbm-v1 → disp-lgbm-v2 → disp-lgbm-v3, and disp-lgbm-v3 is the one in force now. It is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307-dispute-triage (the fraud-score lift experiment) and feat-disp-fraud-score.
Notes: work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/disp-lgbm-v2.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q7
cb-elasticity-v1 rests on ds-cb-pilot-2025q4 directly. It also rests on ds-cb-spend-panel, both through the pilot dataset and through feat-cb-spend-base.
Notes: work/ds-cb-pilot-2025q4.md, work/ds-cb-spend-panel.md

## Q8
Both models build directly on the 30-day app sessions feature, the prior campaign contact feature and recency v1. The 90-day email opens feature is used only by the response model.
Notes: work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md

## Q9
Four decisions depend on ds-cb-call-linkage. dec-cb-metric-24h builds on it directly. dec-cb-metric-48h comes through exp-306 → fnd-cb-def-sensitivity and exp-307 → fnd-cb-repeat-contact, and dec-cb-handoff-v2 comes through fnd-cb-repeat-contact. dec-cb-rollout-60 comes through fnd-cb-volume-shift and the 48h decision.
Notes: work/dec-cb-metric-24h.md, work/dec-cb-metric-48h.md, work/dec-cb-handoff-v2.md, work/dec-cb-rollout-60.md

## Q10
The line runs ed-gbm-v1 → ed-gbm-v2 → ed-gbm-v3, and ed-gbm-v3 is the one in force now. It is built on ed-gbm-v2, exp-207-early-delinquency (the bureau slope lift experiment) and feat-ed-bureau-slope-v1.
Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md