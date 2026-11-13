## Q1
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels (its target), ds-cb-call-linkage (behind feat-cb-prior-calls-v1), and ds-cb-sessions at the root, which both of those build on.
Notes: work/ds-cb-escalation-labels.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
Both nps-gbm-v1 and nps-gbm-v2 build directly on the complaint flag, the theme shares and the transaction frequency feature.
Notes: work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
Three decision notes rest on feat-c25-util-v2: dec-c25-drop-app-sessions (via exp-105 and exp-104), dec-c25-ship-gbm-v2 (via churn-gbm-2025-v2), and dec-ror-value-band-v2 (via ror-roi-v2, exp-407, ror-roi-v1, ror-uplift-v1, feat-ror-churn-score and churn-gbm-2025-v2). The last link depends on ror-roi-v1 and ror-uplift-v1, which the notes tie together in their text rather than in a formal "built on" line.
Notes: work/dec-c25-drop-app-sessions.md, work/dec-c25-ship-gbm-v2.md, work/dec-ror-value-band-v2.md

## Q4
fraud25-gbm-v1 was superseded by fraud25-gbm-v2, which was replaced by fraud26-gbm-v1, then fraud26-gbm-v2 and fraud26-gbm-v3. fraud26-gbm-v3 (promoted 2026-08-26) is the one in force, and it is built on exp-207-fraud-2026, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: work/fraud26-gbm-v3.md, work/exp-207-fraud-2026.md, work/feat-f26-amt-zscore.md, work/feat-f26-geo-mismatch.md, work/fraud26-gbm-v2.md

## Q5
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot (the base population, under the util-v2 and payment features), ds-c25-churn-labels (via the label-window decision and exp-101), ds-c25-app-engagement (via feat-c25-app-sessions), and ds-c25-oot-2024h1 (the 2024 holdout that churn-lr-base-2025 builds on, through the v1 model chain). The holdout link is inferred from the chain rather than stated in churn-gbm-2025-v2's own "built on" line.
Notes: work/ds-c25-accounts-snapshot.md, work/ds-c25-churn-labels.md, work/ds-c25-app-engagement.md, work/ds-c25-oot-2024h1.md