## Q1
Both models build on three shared feature notes: feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The response model also uses the email-open feature, and the T-learner also uses the Q2 RCT dataset.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline is the current model that builds directly on feat-inc-payroll-cadence-v1, which has been superseded by feat-inc-payroll-cadence-v2. The other current model, inc-gbm-v3, rests only on current inputs and on the replaced model inc-gbm-v2.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md

## Q3
Four decisions rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h through other notes.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-rollout-60.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-metric-48h.md

## Q4
The line ends at ed-gbm-v3, which is in force now (ed-gbm-v1 was replaced by v2, and v2 by v3). ed-gbm-v3 is built directly on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1, and its body also names feat-ed-util-trend-v1, feat-ed-cashadv-v1 and feat-ed-minpay-v2 as inputs.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only one note from another project builds directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25.md.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels and ds-cb-sessions directly or via ds-cb-call-linkage, and ds-cb-call-linkage itself through feat-cb-prior-calls-v1. ds-cb-sessions is the root of the chain.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
nps-gbm-v1 and nps-gbm-v2 both build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model that builds directly on a replaced feature or dataset: feat-mq3-recency-v1, which was superseded by feat-mq3-recency-v2.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Five decisions rest on feat-c25-util-v2: dec-c25-ship-gbm-v2, dec-c25-drop-app-sessions (via exp-105 and exp-104), dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 (the last three in retention-offers-roi).
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
The line ends at fraud26-gbm-v3, which is in force now (fraud25-gbm-v1 was replaced by v2, then by fraud26-gbm-v1, v2 and v3). fraud26-gbm-v3 is built directly on fraud26-gbm-v2, exp-207, feat-f26-amt-zscore and feat-f26-geo-mismatch.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md