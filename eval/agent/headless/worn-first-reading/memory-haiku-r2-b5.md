## Q1
Both models build on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The response model also uses feat-mq3-email-open-90d, which the T-learner does not.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline is the only current income model that builds directly on a replaced feature: it uses feat-inc-payroll-cadence-v1, which was superseded by feat-inc-payroll-cadence-v2. The current model inc-gbm-v3 builds on no replaced feature or dataset.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h and dec-cb-handoff-v2 directly or via fnd-cb-repeat-contact, dec-cb-metric-48h via fnd-cb-def-sensitivity or fnd-cb-repeat-contact, and dec-cb-rollout-60 via fnd-cb-volume-shift and dec-cb-metric-48h.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
ed-gbm-v3 is in force at the end of the line (ed-gbm-v1 → ed-gbm-v2 → ed-gbm-v3). It builds directly on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1, and through them on ed-gbm-v1, feat-ed-util-trend-v1, feat-ed-cashadv-v1, ds-ed-current-base and ds-ed-bureau-join; its body also names feat-ed-minpay-v2 as a feature, which the link graph does not count.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md, early-delinquency/ed-gbm-v1.md, early-delinquency/feat-ed-util-trend-v1.md, early-delinquency/feat-ed-cashadv-v1.md, early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-bureau-join.md, early-delinquency/feat-ed-minpay-v2.md

## Q5
Only one note from another project builds directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25.md.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels and ds-cb-call-linkage directly or through feat-cb-prior-calls-v1, and ds-cb-sessions at the root of the chain.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1. nps-gbm-v2 also uses feat-nps-fee-shock-v2, which v1 does not.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
Only mq3-response-gbm-v1 is a current model that builds directly on a replaced feature, feat-mq3-recency-v1, which was superseded by feat-mq3-recency-v2. The other current models, mq3-uplift-xl-v2 and mq3-channel-rct-v1, use no replaced feature or dataset.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Five decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions in churn-2025, and three retention-offers-roi decisions (dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4), all through the chain from churn-gbm-2025-v2.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
fraud26-gbm-v3 is in force at the end of the line, which is longer than two steps (fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3). It rests directly on exp-207, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2, and through them on 27 further notes, reaching back to the fraud-2025 labels, features and models.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/fraud26-gbm-v2.md, fraud-2025/feat-f25-amt-ratio.md, fraud-2026/dec-f26-maturity-60d.md, fraud-2026/ds-f26-cnp-txn.md, fraud-2026/ds-f26-labels-2026.md, fraud-2026/ds-f26-oot-2026h1.md, fraud-2026/exp-206.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-mcc-risk.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2025/ds-f25-txn-2024-2025.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-velocity-v1.md, fraud-2025/fraud25-gbm-v2.md, fraud-2026/exp-202.md, fraud-2026/exp-205.md, fraud-2026/fraud26-find-label-bias.md, fraud-2026/q-f26-label-lag.md, fraud-2025/ds-f25-labels.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-mcc-travel.md, fraud-2025/fraud25-gbm-v1.md, fraud-2026/exp-201.md, fraud-2026/fraud26-find-velocity-leak.md, fraud-2025/ds-f25-travel-tags.md, fraud-2026/exp-203.md, fraud-2026/exp-204.md