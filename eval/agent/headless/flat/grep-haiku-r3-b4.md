## Q1
cb-escalate-v1 builds on the escalation label definition (ds-cb-escalation-labels) and feat-cb-prior-calls-v1. That feature builds on ds-cb-call-linkage, which builds on the root dataset ds-cb-sessions.
Notes: work/cb-escalate-v1.md, work/ds-cb-escalation-labels.md, work/feat-cb-prior-calls-v1.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
nps-gbm-v1 and nps-gbm-v2 share three direct features: the complaint call flag (feat-nps-complaint-flag-v1), the theme share feature (feat-nps-theme-share-v1), and the transaction frequency feature (feat-nps-txn-freq-v1). v2 also adds the fee shock feature (feat-nps-fee-shock-v2).
Notes: work/nps-gbm-v1.md, work/nps-gbm-v2.md, work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
Direct dependents of feat-c25-util-v2 are churn-gbm-2025-v2 and exp-104-churn-2025. Decisions that rest on it are dec-c25-ship-gbm-v2 (via churn-gbm-2025-v2 and exp-107) and dec-c25-drop-app-sessions (via exp-104, then exp-105). The ROR chain also starts from churn-gbm-2025-v2 (via feat-ror-churn-score), and it reaches dec-ror-reallocate-t3, dec-ror-matrix-v4 and dec-ror-value-band-v2. One link in that chain is weak: ror-roi-v1 mentions ror-uplift-v1 in its text but does not list it under Builds on.
Notes: work/feat-c25-util-v2.md, work/churn-gbm-2025-v2.md, work/exp-104-churn-2025.md, work/exp-105-churn-2025.md, work/dec-c25-drop-app-sessions.md, work/dec-c25-ship-gbm-v2.md, work/exp-107-churn-2025.md, work/feat-ror-churn-score.md, work/ror-uplift-v1.md, work/ror-roi-v1.md, work/exp-404-retention-offers-roi.md, work/fnd-ror-realloc-gain.md, work/dec-ror-reallocate-t3.md, work/dec-ror-matrix-v4.md, work/dec-ror-value-band-v2.md

## Q4
The replacement line is fraud25-gbm-v1, replaced by fraud25-gbm-v2 on 2025-06-18. v2 is the current champion. fraud25-gbm-v3 is a challenger that was not promoted, so it does not continue the line. v2 builds on the fraud label arrival lag, the amount-to-median ratio, the device age feature, the authorisation hour band, feat-f25-mcc-travel, feat-f25-velocity-v1 and fraud25-gbm-v1.
Notes: work/fraud25-gbm-v1.md, work/fraud25-gbm-v2.md, work/fraud25-gbm-v3.md

## Q5
churn-gbm-2025-v2 builds on feat-c25-util-v2, which builds on ds-c25-accounts-snapshot. That is the only dataset lineage I verified for this model. It also builds on the payment behaviour feature (feat-c25-payment-behaviour) and the card transaction recency feature (feat-c25-txn-recency), but I did not read those notes, so their dataset parents are unverified. I also did not confirm a path to ds-c25-oot-2024h1, so I am leaving it out.
Notes: work/churn-gbm-2025-v2.md, work/feat-c25-util-v2.md

## Q6
rdm-propensity-lr and rdm-uplift-v1 share two direct features: feat-rdm-app-installed and feat-rdm-last-activity-v1. rdm-uplift-v1 also builds on rdm-propensity-lr itself.
Notes: work/rdm-propensity-lr.md, work/rdm-uplift-v1.md, work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md

## Q7
Decisions that rest on ds-csb-churn-labels are dec-csb-90d-window (direct), and, through the csb-lr-base chain, dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2. The chain runs csb-lr-base → exp-202 → dec-csb-tenure-floor → csb-xgb-v1/v2 → dec-csb-ship-xgb-v1/v2, and csb-lr-base → exp-203 → fnd-csb-volatility-lift → dec-csb-ship-xgb-v1. I did not enumerate every input to csb-xgb-v2, so there may be more decisions downstream.
Notes: work/ds-csb-churn-labels.md, work/csb-lr-base.md, work/exp-201-churn-small-business.md, work/exp-202-churn-small-business.md, work/exp-203-churn-small-business.md, work/fnd-csb-volatility-lift.md, work/dec-csb-tenure-floor.md, work/csb-xgb-v1.md, work/csb-xgb-v2.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md, work/dec-csb-90d-window.md

## Q8
The replacement line is find-hp-naive-effect, superseded by find-hp-adjusted-effect, which is superseded by find-hp-effect-v2. The current note is find-hp-effect-v2, dated 2026-01-22, which reports a -4.7pp effect. It builds on the difference-in-differences hardship experiment (exp-404-hardship-programs), the propensity matching holdout experiment (exp-408-hardship-programs), and find-hp-adjusted-effect.
Notes: work/find-hp-naive-effect.md, work/find-hp-adjusted-effect.md, work/find-hp-effect-v2.md

## Q9
csb-lr-base builds on the churn labels dataset (ds-csb-churn-labels) and the 2025 Q1 out-of-time dataset (ds-csb-oot-2025q1). It also builds on the raw spend feature (feat-csb-spend-raw) and the tenure bands feature (feat-csb-tenure-band). All of these trace back to the root dataset ds-csb-biz-accounts.
Notes: work/csb-lr-base.md, work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q10
trv-ridge-v2 and trv-ridge-v3 share two direct inputs: feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: work/trv-ridge-v2.md, work/trv-ridge-v3.md, work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md