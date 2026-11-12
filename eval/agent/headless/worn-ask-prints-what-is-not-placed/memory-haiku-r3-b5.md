## Q1
Both models build directly on three feature notes: feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. mq3-response-gbm-v1 also uses feat-mq3-email-open-90d, and mq3-uplift-tlearner-v1 also uses ds-mq3-q2-rct.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
None. The only current income-estimation model is inc-gbm-v3, and it builds directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2, none of which is a replaced feature or dataset.
Notes: income-estimation/inc-gbm-v3.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h through other notes.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-rollout-60.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-metric-48h.md

## Q4
The line ends at ed-gbm-v3, which is in force. It builds directly on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1, and through them on ed-gbm-v1, feat-ed-util-trend-v1, feat-ed-cashadv-v1, ds-ed-bureau-join, ds-ed-oot-2026h1, ds-ed-current-base and ds-ed-label-30p3m. The note's own feature list also names feat-ed-minpay-v2, which its Builds-on line does not link.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md, early-delinquency/ed-gbm-v1.md, early-delinquency/feat-ed-util-trend-v1.md, early-delinquency/feat-ed-cashadv-v1.md, early-delinquency/ds-ed-bureau-join.md, early-delinquency/ds-ed-oot-2026h1.md, early-delinquency/ds-ed-current-base.md, early-delinquency/ds-ed-label-30p3m.md

## Q5
Only one note of another project builds directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25.md.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels and ds-cb-sessions directly or through the chain, and ds-cb-call-linkage through feat-cb-prior-calls-v1.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both models build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model that builds directly on a replaced feature. It uses feat-mq3-recency-v1, which was replaced by feat-mq3-recency-v2.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Five decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions in churn-2025, and dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 in retention-offers-roi.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
The line runs fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3, and fraud26-gbm-v3 is in force. It rests on 31 notes: directly on exp-207, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2, and through those on the rest of the chain back to the 2025 datasets.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/dec-f26-maturity-60d.md, fraud-2026/ds-f26-cnp-txn.md, fraud-2026/ds-f26-labels-2026.md, fraud-2026/ds-f26-oot-2026h1.md, fraud-2026/exp-206.md, fraud-2026/feat-f26-device-age.md, fraud-2026/feat-f26-mcc-risk.md, fraud-2026/feat-f26-velocity-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/fraud26-find-label-bias.md, fraud-2026/q-f26-label-lag.md, fraud-2026/exp-201.md, fraud-2026/exp-202.md, fraud-2026/exp-203.md, fraud-2026/exp-204.md, fraud-2026/exp-205.md, fraud-2026/fraud26-find-velocity-leak.md, fraud-2025/fraud25-gbm-v2.md, fraud-2025/fraud25-gbm-v1.md, fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-velocity-v1.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-mcc-travel.md, fraud-2025/ds-f25-txn-2024-2025.md, fraud-2025/ds-f25-labels.md, fraud-2025/ds-f25-travel-tags.md