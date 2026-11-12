## Q1
Both models build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. mq3-response-gbm-v1 also uses the email-open feature, but mq3-uplift-tlearner-v1 does not.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline is the only current model that builds directly on a replaced feature. It uses feat-inc-payroll-cadence-v1, which was superseded by feat-inc-payroll-cadence-v2. The other current model, inc-gbm-v3, builds on inc-gbm-v2 (a model) and no replaced feature or dataset.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md

## Q3
Four decisions rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-handoff-v2, dec-cb-metric-48h and dec-cb-rollout-60 through other notes.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
The line runs ed-gbm-v1, then ed-gbm-v2, then ed-gbm-v3, which is the one in force now. ed-gbm-v3 builds directly on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only one note of another project builds directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25. The other mention is fraud25-gbm-v2, which is in the same project.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests directly on ds-cb-escalation-labels. Through that label note and feat-cb-prior-calls-v1 it reaches ds-cb-sessions and ds-cb-call-linkage.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
nps-gbm-v1 and nps-gbm-v2 both build directly on the complaint-flag, theme-share and transaction-frequency features.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model that builds directly on a replaced feature. It uses feat-mq3-recency-v1, which was superseded by feat-mq3-recency-v2. mq3-channel-rct-v1 and mq3-uplift-xl-v2 use no replaced feature or dataset.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Five decisions rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions in churn-2025, and dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 in retention-offers-roi. All reach it through other notes, not directly.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
The line runs fraud25-gbm-v1, fraud25-gbm-v2, fraud26-gbm-v1, fraud26-gbm-v2, and fraud26-gbm-v3, which is in force now. fraud26-gbm-v3 builds directly on fraud26-gbm-v2, exp-207, feat-f26-amt-zscore and feat-f26-geo-mismatch.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md