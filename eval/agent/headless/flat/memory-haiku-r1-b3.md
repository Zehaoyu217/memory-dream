## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. They reach it through feat-cr-ivr-path-v1, cr-lgbm-v1 and related notes.
Notes: work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-cost-matrix.md, work/dec-cr-pilot.md

## Q2
cli-xgb-v3 is the note in force at the end of the cli-xgb-v1 → v2 → v3 line. It was built on exp-106-credit-line-increase, exp-107-credit-line-increase and find-cli-uplift-wins. One further link, the out-of-time AUC check for v2, is named only in words and matches no note.
Notes: work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls and ds-cr-ivr-paths. It reaches ds-cr-calls through feat-cr-caller-history-v1, feat-cr-tenure-v1 and feat-cr-transcript-tfidf-v1, and reaches ds-cr-ivr-paths through feat-cr-ivr-path-v1.
Notes: work/ds-cr-calls.md, work/ds-cr-ivr-paths.md

## Q4
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. Version 2 adds feat-f25-mcc-travel on top.
Notes: work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. They reach it through the cb-elasticity, exp-20x and find-cb notes built on the panel.
Notes: work/dec-cb-adopt-banded-tiers.md, work/dec-cb-extend-flat-pilot.md, work/dec-cb-threshold-2500.md

## Q6
disp-lgbm-v3 is the note in force at the end of the disp-lgbm-v1 → v2 → v3 line. It was built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307-dispute-triage and feat-disp-fraud-score.
Notes: work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/disp-lgbm-v2.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q7
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel through feat-cb-spend-base.
Notes: work/ds-cb-pilot-2025q4.md, work/ds-cb-spend-panel.md

## Q8
Both mq3-response-gbm-v1 and mq3-uplift-tlearner-v1 build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The response model also uses feat-mq3-email-open-90d.
Notes: work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md

## Q9
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h through the chatbot experiments and findings.
Notes: work/dec-cb-metric-24h.md, work/dec-cb-rollout-60.md, work/dec-cb-handoff-v2.md, work/dec-cb-metric-48h.md

## Q10
ed-gbm-v3 is the note in force at the end of the ed-gbm-v1 → v2 → v3 line. It was built on ed-gbm-v2, exp-207-early-delinquency and feat-ed-bureau-slope-v1, and uses the features feat-ed-util-trend-v1, feat-ed-cashadv-v1 and feat-ed-minpay-v2.
Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md, work/feat-ed-util-trend-v1.md, work/feat-ed-cashadv-v1.md, work/feat-ed-minpay-v2.md