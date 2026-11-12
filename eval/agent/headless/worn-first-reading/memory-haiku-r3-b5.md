## Q1
Both models build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. mq3-response-gbm-v1 also uses feat-mq3-email-open-90d, and mq3-uplift-tlearner-v1 also uses ds-mq3-q2-rct.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/mq3-uplift-tlearner-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline is still current and builds directly on feat-inc-payroll-cadence-v1, which was superseded by feat-inc-payroll-cadence-v2. inc-gbm-v3 is also current, but its only replaced input is the model inc-gbm-v2, not a feature or dataset.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h through other notes.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-rollout-60.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-metric-48h.md

## Q4
ed-gbm-v3 is in force now. It builds directly on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1. Through those it rests on ed-gbm-v1, ds-ed-current-base, feat-ed-cashadv-v1, feat-ed-util-trend-v1 and ds-ed-bureau-join.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md, early-delinquency/ed-gbm-v1.md, early-delinquency/ds-ed-current-base.md, early-delinquency/feat-ed-cashadv-v1.md, early-delinquency/feat-ed-util-trend-v1.md, early-delinquency/ds-ed-bureau-join.md

## Q5
Only one note in another project builds directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25.md.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-sessions at the root, ds-cb-call-linkage built on it, and ds-cb-escalation-labels built directly on it.
Notes: chatbot-deflection/ds-cb-sessions.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-escalation-labels.md

## Q7
nps-gbm-v1 and nps-gbm-v2 both build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model that builds directly on a replaced feature or dataset: feat-mq3-recency-v1, which was superseded by feat-mq3-recency-v2. mq3-uplift-xl-v2 and mq3-channel-rct-v1 are current but use no replaced inputs.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Five decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions in churn-2025, and dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 in retention-offers-roi.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
fraud26-gbm-v3 is in force at the end of the line (fraud25-gbm-v1, then fraud25-gbm-v2, then fraud26-gbm-v1, then fraud26-gbm-v2). It builds directly on fraud26-gbm-v2, exp-207, feat-f26-amt-zscore and feat-f26-geo-mismatch.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md