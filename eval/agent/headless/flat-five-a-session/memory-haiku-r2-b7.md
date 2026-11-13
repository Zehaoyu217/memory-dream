## Q1
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels (directly), and ds-cb-call-linkage and ds-cb-sessions (through ds-cb-escalation-labels and feat-cb-prior-calls-v1).
Notes: work/cb-escalate-v1.md, work/ds-cb-escalation-labels.md, work/feat-cb-prior-calls-v1.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
Both nps-gbm-v1 and nps-gbm-v2 build directly on three feature notes: feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: work/nps-gbm-v1.md, work/nps-gbm-v2.md, work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
Five decision notes rest on feat-c25-util-v2: dec-c25-drop-app-sessions and dec-c25-ship-gbm-v2 (through churn-gbm-2025-v2 and exp-106-churn-2025), and dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 (through the retention-offer ROI chain). The chain has one unplaced link, "the util-v2 swap experiment" in exp-106-churn-2025; it matches exp-104-churn-2025 by title, which is already in the chain.
Notes: work/feat-c25-util-v2.md, work/dec-c25-drop-app-sessions.md, work/dec-c25-ship-gbm-v2.md, work/dec-ror-value-band-v2.md, work/dec-ror-reallocate-t3.md, work/dec-ror-matrix-v4.md

## Q4
The note in force at the end of the fraud25-gbm-v1 line is fraud26-gbm-v3 (fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3). It builds on exp-207-fraud-2026, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: work/fraud26-gbm-v3.md, work/exp-207-fraud-2026.md, work/feat-f26-amt-zscore.md, work/feat-f26-geo-mismatch.md, work/fraud26-gbm-v2.md

## Q5
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-oot-2024h1 and ds-c25-churn-labels, reached directly or through its feature, experiment and model parents. The unplaced "util-v2 swap experiment" link in exp-106-churn-2025 matches exp-104-churn-2025, which is already in the chain, so no dataset is missing.
Notes: work/churn-gbm-2025-v2.md, work/ds-c25-accounts-snapshot.md, work/ds-c25-app-engagement.md, work/ds-c25-oot-2024h1.md, work/ds-c25-churn-labels.md