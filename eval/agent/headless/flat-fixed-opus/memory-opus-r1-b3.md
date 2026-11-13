## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. All of them reach it through feat-cr-ivr-path-v1 and the routing models and experiments built on that feature.
Notes: work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-cost-matrix.md, work/dec-cr-pilot.md

## Q2
The line runs cli-xgb-v1 → cli-xgb-v2 → cli-xgb-v3, so cli-xgb-v3 is the one in force. It is built on exp-106-credit-line-increase, exp-107-credit-line-increase and find-cli-uplift-wins.
Notes: work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls and ds-cr-ivr-paths. It reaches them through its features, and through exp-101 and cr-logreg-v1.
Notes: work/ds-cr-calls.md, work/ds-cr-ivr-paths.md

## Q4
Both models build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. Only v2 also uses feat-f25-mcc-travel.
Notes: work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500.
Notes: work/dec-cb-adopt-banded-tiers.md, work/dec-cb-extend-flat-pilot.md, work/dec-cb-threshold-2500.md

## Q6
The line runs disp-lgbm-v1 → disp-lgbm-v2 → disp-lgbm-v3, so disp-lgbm-v3 is the one in force. It is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307-dispute-triage and feat-disp-fraud-score.
Notes: work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/disp-lgbm-v2.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q7
cb-elasticity-v1 rests on two dataset notes. It uses ds-cb-pilot-2025q4 directly and reaches ds-cb-spend-panel through feat-cb-spend-base (ds-cb-pilot-2025q4 is also built on it).
Notes: work/ds-cb-pilot-2025q4.md, work/ds-cb-spend-panel.md

## Q8
Both models build directly on three feature notes: feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. feat-mq3-recency-v1 has since been replaced by feat-mq3-recency-v2.
Notes: work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md

## Q9
Four decision notes rest on ds-cb-call-linkage. dec-cb-metric-24h uses it directly. dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h reach it through other notes; dec-cb-metric-48h replaced dec-cb-metric-24h.
Notes: work/dec-cb-metric-24h.md, work/dec-cb-rollout-60.md, work/dec-cb-handoff-v2.md, work/dec-cb-metric-48h.md

## Q10
The line runs ed-gbm-v1 → ed-gbm-v2 → ed-gbm-v3, so ed-gbm-v3 is the one in force. It is built on ed-gbm-v2, exp-207-early-delinquency and feat-ed-bureau-slope-v1.
Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md