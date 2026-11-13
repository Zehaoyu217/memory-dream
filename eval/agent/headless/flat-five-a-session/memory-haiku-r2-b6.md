## Q1
disp-lgbm-v1 was replaced by disp-lgbm-v2, which was then replaced by disp-lgbm-v3, the note in force now. disp-lgbm-v3 builds directly on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307-dispute-triage and feat-disp-fraud-score, and through disp-lgbm-v2 on the v1 chain.
Notes: work/disp-lgbm-v3.md, work/disp-lgbm-v2.md, work/disp-lgbm-v1.md, work/dec-disp-fraud-score-in.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q2
cb-elasticity-v1 rests directly on the dataset ds-cb-pilot-2025q4 and on feat-cb-spend-base, which in turn rests on the dataset ds-cb-spend-panel. So its dataset notes are ds-cb-pilot-2025q4 (direct) and ds-cb-spend-panel (through feat-cb-spend-base).
Notes: work/cb-elasticity-v1.md, work/ds-cb-pilot-2025q4.md, work/feat-cb-spend-base.md, work/ds-cb-spend-panel.md

## Q3
Both mq3-response-gbm-v1 and mq3-uplift-tlearner-v1 build directly on feat-mq3-app-sessions-30d (30-day app sessions) and feat-mq3-prior-treat (prior-30-day campaign contact).
Notes: work/mq3-response-gbm-v1.md, work/mq3-uplift-tlearner-v1.md, work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md

## Q4
Directly, dec-cb-metric-24h rests on ds-cb-call-linkage. Through it, dec-cb-metric-48h (which replaced the 24h decision), dec-cb-rollout-60 and dec-cb-handoff-v2 also rest on ds-cb-call-linkage. The tool named the last two only by slug, so their file paths are inferred from the folder's naming pattern, not confirmed.
Notes: work/dec-cb-metric-24h.md, work/dec-cb-metric-48h.md, work/dec-cb-rollout-60.md, work/dec-cb-handoff-v2.md

## Q5
ed-gbm-v1 was replaced by ed-gbm-v2, which was replaced by ed-gbm-v3, the note in force now. ed-gbm-v3 builds directly on ed-gbm-v2, exp-207-early-delinquency and feat-ed-bureau-slope-v1, and through ed-gbm-v2 on the v1 chain and its features (feat-ed-util-trend-v1, feat-ed-cashadv-v1, feat-ed-minpay-v2).
Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/ed-gbm-v1.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md