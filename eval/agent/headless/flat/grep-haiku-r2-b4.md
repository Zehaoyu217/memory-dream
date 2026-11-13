## Q1
cb-escalate-v1 rests on the escalation label definition (ds-cb-escalation-labels) and on feat-cb-prior-calls-v1. Both trace back to two dataset notes: ds-cb-sessions (`chat.sessions`, 2025) and ds-cb-call-linkage, which joins sessions to calls.
Notes: work/cb-escalate-v1.md, work/ds-cb-escalation-labels.md, work/feat-cb-prior-calls-v1.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
nps-gbm-v1 and nps-gbm-v2 both build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: work/nps-gbm-v1.md, work/nps-gbm-v2.md, work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
Three decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 (directly, via churn-gbm-2025-v2), dec-c25-drop-app-sessions (via exp-105 and exp-104), and dec-ror-value-band-v2 (via ror-roi-v2, exp-407, ror-roi-v1, ror-uplift-v1, feat-ror-churn-score and churn-gbm-2025-v2).
Notes: work/feat-c25-util-v2.md, work/churn-gbm-2025-v2.md, work/exp-104-churn-2025.md, work/exp-105-churn-2025.md, work/dec-c25-drop-app-sessions.md, work/dec-c25-ship-gbm-v2.md, work/feat-ror-churn-score.md, work/ror-uplift-v1.md, work/ror-roi-v1.md, work/exp-407-retention-offers-roi.md, work/ror-roi-v2.md, work/dec-ror-value-band-v2.md

## Q4
fraud26-gbm-v3 is in force at the end of the line (fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3). It builds on the geo-mismatch and amount z-score experiment, feat-f26-amt-zscore, the geo-mismatch feature and fraud26-gbm-v2.
Notes: work/fraud25-gbm-v1.md, work/fraud25-gbm-v2.md, work/dec-f26-replace-f25.md, work/fraud26-gbm-v1.md, work/fraud26-gbm-v2.md, work/fraud26-gbm-v3.md, work/dec-f26-promote-v3.md

## Q5
churn-gbm-2025-v2 traces back to four dataset notes: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-churn-labels and ds-c25-oot-2024h1. The accounts snapshot feeds the util and payment features, app engagement feeds feat-c25-app-sessions (via dec-c25-drop-app-sessions), churn labels feed the 60-day label decision (via fnd-c25-90d-feedback-lag), and the 2024 holdout feeds churn-lr-base-2025 (via exp-106 and fnd-c25-recency-dominates).
Notes: work/churn-gbm-2025-v2.md, work/ds-c25-accounts-snapshot.md, work/ds-c25-app-engagement.md, work/ds-c25-churn-labels.md, work/ds-c25-oot-2024h1.md, work/dec-c25-drop-app-sessions.md, work/exp-106-churn-2025.md, work/fnd-c25-recency-dominates.md, work/churn-lr-base-2025.md, work/dec-c25-label-60d.md, work/fnd-c25-90d-feedback-lag.md

## Q6
rdm-propensity-lr and rdm-uplift-v1 both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: work/rdm-propensity-lr.md, work/rdm-uplift-v1.md, work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md

## Q7
Four decision notes rest on ds-csb-churn-labels. dec-csb-90d-window uses it directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 rest on it indirectly through csb-lr-base and the csb-xgb models.
Notes: work/ds-csb-churn-labels.md, work/dec-csb-90d-window.md, work/exp-201-churn-small-business.md, work/csb-lr-base.md, work/dec-csb-tenure-floor.md, work/exp-202-churn-small-business.md, work/csb-xgb-v1.md, work/csb-xgb-v2.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md

## Q8
find-hp-effect-v2 is in force (the -4.7pp hardship effect). It builds on find-hp-adjusted-effect, which itself replaced find-hp-naive-effect, and on the difference-in-differences hardship experiment and the propensity-matching holdout experiment.
Notes: work/find-hp-naive-effect.md, work/find-hp-adjusted-effect.md, work/find-hp-effect-v2.md

## Q9
csb-lr-base traces back to three dataset notes: ds-csb-churn-labels, ds-csb-oot-2025q1 and ds-csb-biz-accounts. The last is the root population, and both churn labels and the out-of-time holdout build on it.
Notes: work/csb-lr-base.md, work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/ds-csb-biz-accounts.md

## Q10
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: work/trv-ridge-v2.md, work/trv-ridge-v3.md, work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md