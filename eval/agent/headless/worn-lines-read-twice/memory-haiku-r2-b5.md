## Q1
The two models share three direct feature inputs: feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The response model also uses feat-mq3-email-open-90d, and the T-learner also uses ds-mq3-q2-rct.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline is still current and builds directly on feat-inc-payroll-cadence-v1, which was replaced by feat-inc-payroll-cadence-v2. The other current model, inc-gbm-v3, builds on ds-inc-verified-2026 and find-inc-log-target-gain, neither of which has been replaced.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h and dec-cb-metric-48h, dec-cb-handoff-v2, and dec-cb-rollout-60, the last reached through cb-escalate-v1 and fnd-cb-volume-shift.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
ed-gbm-v3 is in force at the end of the line (ed-gbm-v1, then ed-gbm-v2, then ed-gbm-v3). It is built directly on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only one note of another project is built directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25, the decision that replaces the 2025 champion from 2026-02-10.
Notes: fraud-2026/dec-f26-replace-f25.md, fraud-2025/dec-f25-champion-v2.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels directly, and ds-cb-call-linkage and ds-cb-sessions through feat-cb-prior-calls-v1 and the labels. ds-cb-sessions is the start of the chain.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both models build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1. nps-gbm-v2 also uses feat-nps-fee-shock-v2.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model that builds directly on a replaced input: feat-mq3-recency-v1, which was replaced by feat-mq3-recency-v2. The other current models, mq3-uplift-xl-v2 and mq3-channel-rct-v1, use no replaced feature or dataset.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Five decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions in churn-2025, and dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 in retention-offers-roi.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
fraud26-gbm-v3 is in force at the end of the line (fraud25-gbm-v1, then fraud25-gbm-v2, then fraud26-gbm-v1, fraud26-gbm-v2, fraud26-gbm-v3). It is built directly on fraud26-gbm-v2, exp-207, feat-f26-amt-zscore and feat-f26-geo-mismatch.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md