## Q1
Both models build directly on three feature notes: feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The response model also uses feat-mq3-email-open-90d, but the T-learner does not.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
None. The only current income model is inc-gbm-v3, and it builds directly on ds-inc-verified-2026 (not replaced), find-inc-log-target-gain, and inc-gbm-v2 (a model, not a feature or dataset).
Notes: income-estimation/inc-gbm-v3.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h and dec-cb-handoff-v2 directly or through other notes, and dec-cb-rollout-60 and dec-cb-metric-48h through other notes.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md, chatbot-deflection/dec-cb-metric-48h.md

## Q4
ed-gbm-v3 is in force now. It is built on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only one note from another project was built directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels directly, and ds-cb-sessions and ds-cb-call-linkage through feat-cb-prior-calls-v1 and the labels.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both models build directly on feat-nps-theme-share-v1, feat-nps-complaint-flag-v1 and feat-nps-txn-freq-v1.
Notes: nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model that builds directly on a replaced feature. It uses feat-mq3-recency-v1, which was replaced by feat-mq3-recency-v2.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Five decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2, dec-c25-drop-app-sessions, dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4. They rest on it directly or through churn-gbm-2025-v2, exp-104 and other notes.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
fraud26-gbm-v3 is in force now, at the end of fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3. It is built on exp-207, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/fraud26-gbm-v2.md