## Q1
Both models build directly on three feature notes: feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The email-opens feature is used only by the response model, and the RCT dataset only by the T-learner.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
Only inc-linear-baseline. It is still current and builds directly on feat-inc-payroll-cadence-v1, which feat-inc-payroll-cadence-v2 replaced. inc-gbm-v3 is also current, but the only replaced note it builds on is a model (inc-gbm-v2), not a feature or dataset.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md

## Q3
Four decisions rest on ds-cb-call-linkage. dec-cb-metric-24h builds on it directly. dec-cb-metric-48h comes through fnd-cb-def-sensitivity and fnd-cb-repeat-contact, dec-cb-handoff-v2 through fnd-cb-repeat-contact, and dec-cb-rollout-60 through fnd-cb-volume-shift and the other decisions.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
The line runs ed-gbm-v1 → ed-gbm-v2 → ed-gbm-v3, so ed-gbm-v3 is in force now. It builds directly on ed-gbm-v2, exp-207 (the bureau-slope experiment) and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
One note from another project builds directly on it: the decision dec-f26-replace-f25 in project fraud-2026.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three datasets. ds-cb-escalation-labels is a direct input. ds-cb-call-linkage comes through feat-cb-prior-calls-v1, and ds-cb-sessions sits under both of those.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both versions build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1. v2 also adds feat-nps-fee-shock-v2.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
Only mq3-response-gbm-v1. It has not been replaced and builds directly on feat-mq3-recency-v1, which feat-mq3-recency-v2 replaced. mq3-uplift-xl-v2's only replaced input is a model, and mq3-channel-rct-v1's inputs have not been replaced.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Five decisions rest on it. In churn-2025 they are dec-c25-drop-app-sessions (through exp-104 and exp-105) and dec-c25-ship-gbm-v2 (through churn-gbm-2025-v2). Through churn-gbm-2025-v2 and retention-offers-roi/feat-ror-churn-score, three decisions in retention-offers-roi also rest on it: dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4.
Notes: churn-2025/dec-c25-drop-app-sessions.md, churn-2025/dec-c25-ship-gbm-v2.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
The line runs fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3, so fraud26-gbm-v3 (in project fraud-2026) is in force now. It builds directly on exp-207, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/fraud26-gbm-v2.md