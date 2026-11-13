## Q1
cb-escalate-v1 rests on two datasets directly, ds-cb-escalation-labels and ds-cb-sessions is not direct; it rests on ds-cb-escalation-labels (dataset) and ds-cb-call-linkage (dataset) directly or through feat-cb-prior-calls-v1, with ds-cb-sessions (dataset) at the root.
Notes: work/cb-escalate-v1.md, work/ds-cb-escalation-labels.md, work/feat-cb-prior-calls-v1.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
Both nps-gbm-v1 and nps-gbm-v2 build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
Five decision notes rest on feat-c25-util-v2: dec-c25-drop-app-sessions, dec-c25-ship-gbm-v2, dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4, all directly or through churn-gbm-2025-v2 and the other notes built on it.
Notes: work/dec-c25-drop-app-sessions.md, work/dec-c25-ship-gbm-v2.md, work/dec-ror-value-band-v2.md, work/dec-ror-reallocate-t3.md, work/dec-ror-matrix-v4.md

## Q4
The line is fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3. fraud26-gbm-v3 is the one in force, and it is built on exp-207-fraud-2026, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: work/fraud26-gbm-v3.md, work/exp-207-fraud-2026.md, work/feat-f26-amt-zscore.md, work/feat-f26-geo-mismatch.md, work/fraud26-gbm-v2.md

## Q5
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-oot-2024h1 and ds-c25-churn-labels, reached directly or through its feature, experiment and model parents.
Notes: work/churn-gbm-2025-v2.md, work/ds-c25-accounts-snapshot.md, work/ds-c25-app-engagement.md, work/ds-c25-oot-2024h1.md, work/ds-c25-churn-labels.md

## Q6
rdm-propensity-lr and rdm-uplift-v1 both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md

## Q7
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through other notes.
Notes: work/dec-csb-90d-window.md, work/dec-csb-tenure-floor.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md

## Q8
The line is find-hp-naive-effect → find-hp-adjusted-effect → find-hp-effect-v2. find-hp-effect-v2 is in force, and it is built on exp-404-hardship-programs, exp-402-hardship-programs and find-hp-adjusted-effect.
Notes: work/find-hp-effect-v2.md, work/exp-404-hardship-programs.md, work/exp-402-hardship-programs.md, work/find-hp-adjusted-effect.md

## Q9
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through them.
Notes: work/csb-lr-base.md, work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/ds-csb-biz-accounts.md

## Q10
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md