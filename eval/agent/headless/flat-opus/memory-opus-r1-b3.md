## Q1
Four decision notes rest on ds-cr-ivr-paths, all reached through feat-cr-ivr-path-v1. dec-cr-lgbm comes via cr-lgbm-v1 and cr-logreg-v1. dec-cr-caller-v2 comes via exp-104 → fnd-cr-leak-corrected → feat-cr-caller-history-v2. dec-cr-cost-matrix and dec-cr-pilot come via cr-lgbm-v3.
Notes: work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-cost-matrix.md, work/dec-cr-pilot.md

## Q2
The line runs cli-xgb-v1 → cli-xgb-v2 → cli-xgb-v3, so cli-xgb-v3 is the one in force now. It is built on exp-106-credit-line-increase (the out-of-time AUC check for v2), exp-107-credit-line-increase and find-cli-uplift-wins, and it replaces cli-xgb-v2.
Notes: work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md, work/cli-xgb-v2.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-ivr-paths, through feat-cr-ivr-path-v1 and cr-logreg-v1, and ds-cr-calls, through the caller-history, TF-IDF and IVR-path chains. feat-cr-tenure-v1 cites `cards.accounts_monthly` and the onboarding team's account spec, but neither has a note of its own.
Notes: work/ds-cr-ivr-paths.md, work/ds-cr-calls.md

## Q4
Both models build directly on the same four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. Only v2 adds feat-f25-mcc-travel.
Notes: work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decision notes rest on ds-cb-spend-panel. dec-cb-extend-flat-pilot comes via find-cb-flat-wins and cb-elasticity-v1. dec-cb-adopt-banded-tiers comes via cb-elasticity-v2. dec-cb-threshold-2500 comes via dec-cb-adopt-banded-tiers and exp-206-breakeven-sim.
Notes: work/dec-cb-extend-flat-pilot.md, work/dec-cb-adopt-banded-tiers.md, work/dec-cb-threshold-2500.md

## Q6
The line runs disp-lgbm-v1 → disp-lgbm-v2 → disp-lgbm-v3, so disp-lgbm-v3 is the one in force now. It is built on dec-disp-fraud-score-in, disp-lgbm-v2 (which it replaces), exp-307-dispute-triage (the fraud-score lift test) and feat-disp-fraud-score.
Notes: work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/disp-lgbm-v2.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q7
cb-elasticity-v1 rests on two dataset notes. ds-cb-pilot-2025q4 is direct. ds-cb-spend-panel comes through both ds-cb-pilot-2025q4 and feat-cb-spend-base.
Notes: work/ds-cb-pilot-2025q4.md, work/ds-cb-spend-panel.md

## Q8
Both models build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. Only the response model also uses feat-mq3-email-open-90d.
Notes: work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md

## Q9
Four decision notes rest on ds-cb-call-linkage. dec-cb-metric-24h is direct. dec-cb-metric-48h comes via exp-306 → fnd-cb-def-sensitivity, and also via fnd-cb-repeat-contact. dec-cb-handoff-v2 comes via exp-307 → fnd-cb-repeat-contact. dec-cb-rollout-60 comes via fnd-cb-volume-shift, dec-cb-handoff-v2 and dec-cb-metric-48h.
Notes: work/dec-cb-metric-24h.md, work/dec-cb-metric-48h.md, work/dec-cb-handoff-v2.md, work/dec-cb-rollout-60.md

## Q10
The line runs ed-gbm-v1 → ed-gbm-v2 → ed-gbm-v3, so ed-gbm-v3 is the one in force now. It is built on ed-gbm-v2 (which it replaces), exp-207-early-delinquency (the bureau slope lift test) and feat-ed-bureau-slope-v1.
Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md