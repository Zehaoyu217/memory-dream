## Q1
Both models build directly on three feature notes: the 30-day app sessions feature, the prior-campaign-contact feature, and the recency feature (v1). mq3-response-gbm-v1 also uses the 90-day email-opens feature, which the T-learner does not.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
None of the current models in income-estimation has a feature or dataset note that was replaced. inc-linear-baseline builds directly on feat-inc-payroll-cadence-v1, which has since been replaced by v2. inc-gbm-v3 is current, but it builds on the replaced model inc-gbm-v2, not on a feature or dataset.
Notes: income-estimation/inc-linear-baseline.md

## Q3
Four decision notes rest on ds-cb-call-linkage. dec-cb-metric-24h rests on it directly. dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h rest on it through other notes.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-rollout-60.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-metric-48h.md

## Q4
ed-gbm-v3 is the one in force. It builds on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1. Its body also names the utilisation-trend, cash-advance and min-pay features.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only one note in another project builds directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25, which is the decision that replaces the 2025 champion.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels directly, and ds-cb-call-linkage and ds-cb-sessions through the feature and label chain. The fourth note it rests on, feat-cb-prior-calls-v1, is a feature, not a dataset.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Three feature notes are built on directly by both nps-gbm-v1 and nps-gbm-v2: the complaint-flag feature, the theme-share feature, and the transaction-frequency feature.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model in marketing-uplift-q3 that builds directly on a replaced feature, namely feat-mq3-recency-v1, which was superseded by v2. mq3-channel-rct-v1 and mq3-uplift-xl-v2 do not rest on any replaced feature or dataset.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md

## Q9
Five decision notes rest on feat-c25-util-v2. Two are in churn-2025 (dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions, the latter through exp-105 and exp-104). Three are in retention-offers-roi (dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4).
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
fraud26-gbm-v3 is the one in force. It builds on fraud26-gbm-v2, exp-207, feat-f26-amt-zscore and feat-f26-geo-mismatch.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md