## Q1
Both models build on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. mq3-response-gbm-v1 also uses feat-mq3-email-open-90d, and mq3-uplift-tlearner-v1 uses the ds-mq3-q2-rct dataset.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/mq3-uplift-tlearner-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline builds directly on feat-inc-payroll-cadence-v1, which has been replaced by v2. It has no superseded marker, so it is treated as current; inc-gbm-v3, the live model, builds on no replaced feature or dataset.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h and dec-cb-handoff-v2 directly, and dec-cb-rollout-60 and dec-cb-metric-48h through other notes.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/ds-cb-call-linkage.md

## Q4
The note in force is ed-gbm-v3, which is built on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1. Its feature inputs are also feat-ed-util-trend-v1, feat-ed-cashadv-v1 and feat-ed-minpay-v2.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only one note from another project builds directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25, which is built on fraud-2025/dec-f25-champion-v2 and fraud26-gbm-v1.
Notes: fraud-2026/dec-f26-replace-f25.md, fraud-2025/dec-f25-champion-v2.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels directly, and ds-cb-call-linkage and ds-cb-sessions through feat-cb-prior-calls-v1 and the labels note.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
nps-gbm-v1 and nps-gbm-v2 both build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: nps-drivers/nps-gbm-v1.md, nps-drivers/nps-gbm-v2.md, nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model that builds directly on a replaced feature: feat-mq3-recency-v1, now replaced by feat-mq3-recency-v2. mq3-uplift-xl-v2 and mq3-channel-rct-v1 build on no replaced feature or dataset.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-recency-v2.md

## Q9
Five decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions in churn-2025, and three retention-offers-roi decisions (dec-ror-value-band-v2, dec-ror-reallocate-t3, dec-ror-matrix-v4) reached through them.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md, churn-2025/feat-c25-util-v2.md

## Q10
The note in force is fraud26-gbm-v3, which is built on fraud26-gbm-v2, exp-207, feat-f26-amt-zscore and feat-f26-geo-mismatch.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md