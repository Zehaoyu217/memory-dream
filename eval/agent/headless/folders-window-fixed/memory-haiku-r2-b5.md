## Q1
Both models build directly on three feature notes: the 30-day app sessions feature, the prior-campaign-contact feature and the recency feature (v1). The response model also uses the 90-day email-opens feature, which the T-learner does not.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/mq3-uplift-tlearner-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
None. The only current model in income-estimation is inc-gbm-v3, and it builds directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2. inc-gbm-v2 is a replaced model, not a feature or dataset.
Notes: income-estimation/inc-gbm-v3.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h and dec-cb-metric-48h directly, and dec-cb-handoff-v2 and dec-cb-rollout-60 through other notes built on it.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
The note in force is ed-gbm-v3, which was built directly on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1. Its body also names feat-ed-util-trend-v1, feat-ed-cashadv-v1 and feat-ed-minpay-v2 as features.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only one note from another project was built directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25, which replaces the fraud-2025 champion.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels directly, and ds-cb-call-linkage and ds-cb-sessions through the chain.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both nps-gbm-v1 and nps-gbm-v2 build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: nps-drivers/nps-gbm-v1.md, nps-drivers/nps-gbm-v2.md, nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model that builds directly on a replaced feature or dataset: it uses feat-mq3-recency-v1, which was replaced by feat-mq3-recency-v2.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Five decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions through the churn models, and dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 through the retention-offers-roi chain.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
The note in force is fraud26-gbm-v3, which was built directly on exp-207, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/fraud26-gbm-v2.md