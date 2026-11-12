## Q1
They both build directly on three feature notes: the 30-day app sessions feature, the prior-campaign-contact flag, and recency v1 (the version that counts refunds). The response model also uses the 90-day email opens feature, which the T-learner does not.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
The only one is inc-linear-baseline. Nothing has replaced it, though it is not used in production, and it builds directly on feat-inc-payroll-cadence-v1, which feat-inc-payroll-cadence-v2 replaced. inc-gbm-v1 also uses cadence v1, but it was itself replaced by inc-gbm-v2.
Notes: income-estimation/inc-linear-baseline.md

## Q3
Four decisions: dec-cb-metric-24h (built on it directly; since replaced by the 48h definition), dec-cb-metric-48h (through exp-306, fnd-cb-def-sensitivity and fnd-cb-repeat-contact), dec-cb-handoff-v2 (through exp-307 and fnd-cb-repeat-contact), and dec-cb-rollout-60 (through fnd-cb-volume-shift, dec-cb-metric-48h and dec-cb-handoff-v2).
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
The line runs ed-gbm-v1 → ed-gbm-v2 → ed-gbm-v3, and ed-gbm-v3 is in force now (promoted 2026-06-18). It is built on ed-gbm-v2, exp-207 (the bureau slope test) and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only one note in another project builds directly on it: fraud-2026's dec-f26-replace-f25, the decision that fraud26-gbm-v1 replaces the 2025 champion.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 builds on the escalation labels and feat-cb-prior-calls-v1. The labels build on ds-cb-sessions, and the prior-calls feature builds on ds-cb-call-linkage, which also builds on ds-cb-sessions. So it rests on three dataset notes: ds-cb-escalation-labels, ds-cb-call-linkage and ds-cb-sessions.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
They both build directly on the complaint flag, the theme shares and the transaction frequency feature. v2 also adds fee shock v2.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
The only one is mq3-response-gbm-v1. It is no longer used for targeting but nothing has replaced it, and it builds directly on feat-mq3-recency-v1, which feat-mq3-recency-v2 replaced. mq3-uplift-tlearner-v1 also uses recency v1, but mq3-uplift-xl-v2 replaced it.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md

## Q9
In churn-2025, two decisions rest on it: dec-c25-drop-app-sessions (through exp-104, exp-105 and fnd-c25-app-lift-v2) and dec-c25-ship-gbm-v2 (through churn-gbm-2025-v2). Through churn-gbm-2025-v2, three retention-offers-roi decisions also rest on it, via the churn-score feature, ror-uplift-v1 and ror-roi-v1/v2: dec-ror-reallocate-t3 (since replaced by v4), dec-ror-matrix-v4 and dec-ror-value-band-v2.
Notes: churn-2025/dec-c25-drop-app-sessions.md, churn-2025/dec-c25-ship-gbm-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md, retention-offers-roi/dec-ror-value-band-v2.md

## Q10
The line runs fraud25-gbm-v1 → fraud25-gbm-v2 → fraud-2026/fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3, and fraud26-gbm-v3 is in force now. It is built on exp-207 (geo-mismatch and amount z-score), feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/fraud26-gbm-v2.md