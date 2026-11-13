## Q1
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels (its target), ds-cb-call-linkage (through feat-cb-prior-calls-v1), and ds-cb-sessions, which is the root of both of the others.
Notes: work/cb-escalate-v1.md, work/ds-cb-escalation-labels.md, work/feat-cb-prior-calls-v1.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
nps-gbm-v1 and nps-gbm-v2 both build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1. The complaint-flag match is by description ("the complaint call flag feature"), not by id.
Notes: work/nps-gbm-v1.md, work/nps-gbm-v2.md, work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
dec-c25-drop-app-sessions and dec-c25-ship-gbm-v2 rest on feat-c25-util-v2 directly or through exp-104, exp-105 and churn-gbm-2025-v2. dec-ror-value-band-v2 also rests on it, but only through ror-roi-v2, whose link to ror-uplift-v1 and the 60-day churn score is inferred from body text and descriptive phrases rather than an explicit id.
Notes: work/dec-c25-drop-app-sessions.md, work/dec-c25-ship-gbm-v2.md, work/dec-ror-value-band-v2.md, work/feat-c25-util-v2.md

## Q4
The line ends with fraud26-gbm-v3, which is in force (promoted live 2026-08-26) and has no later replacement. It builds on exp-207-fraud-2026, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: work/fraud26-gbm-v3.md, work/fraud26-gbm-v2.md

## Q5
churn-gbm-2025-v2 rests on two dataset roots: ds-c25-accounts-snapshot (through feat-c25-util-v2 and the payment and recency features) and ds-c25-app-engagement (through the app-session decision and feat-c25-app-sessions). The 2024 holdout is not on this chain, since it enters only through churn-lr-base-2025.
Notes: work/churn-gbm-2025-v2.md, work/feat-c25-util-v2.md, work/ds-c25-accounts-snapshot.md, work/dec-c25-drop-app-sessions.md, work/feat-c25-app-sessions.md, work/ds-c25-app-engagement.md

## Q6
rdm-propensity-lr and rdm-uplift-v1 both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: work/rdm-propensity-lr.md, work/rdm-uplift-v1.md, work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md

## Q7
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor (via fnd-csb-tenure-cut). dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 rest on it through csb-xgb-v1 and csb-xgb-v2, which both build on dec-csb-tenure-floor.
Notes: work/dec-csb-90d-window.md, work/dec-csb-tenure-floor.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md, work/ds-csb-churn-labels.md, work/fnd-csb-tenure-cut.md, work/csb-xgb-v1.md, work/csb-xgb-v2.md

## Q8
The line ends with find-hp-effect-v2, which is in force: hardship enrolment reduces the 30-to-60 roll by 4.7pp. It builds on exp-404-hardship-programs (the difference-in-differences check), exp-408-hardship-programs (the propensity matching holdout) and find-hp-adjusted-effect, which replaced the naive find-hp-naive-effect.
Notes: work/find-hp-effect-v2.md, work/find-hp-adjusted-effect.md, work/exp-404-hardship-programs.md, work/exp-408-hardship-programs.md

## Q9
csb-lr-base rests on ds-csb-biz-accounts. It reaches that root directly and also through ds-csb-churn-labels, ds-csb-oot-2025q1, feat-csb-spend-raw and feat-csb-tenure-band.
Notes: work/csb-lr-base.md, work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md, work/ds-csb-biz-accounts.md

## Q10
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: work/trv-ridge-v2.md, work/trv-ridge-v3.md, work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md