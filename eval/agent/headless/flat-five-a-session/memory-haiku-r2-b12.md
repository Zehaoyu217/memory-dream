## Q1
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre (call-centre contacts) and ds-xs-offer-log, both reached through exp-403, feat-xs-call-recent and find-xs-call-overstated. The chain also includes the question q-xs-propensity, which is not a dataset.
Notes: work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q2
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the dispute-triage experiments and models built on the labels.
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q3
rs-xgb-v1 was superseded by rs-xgb-v2, which was superseded by rs-xgb-v3, so rs-xgb-v3 is the one in force. It is built on exp-308-recovery-scoring and rs-xgb-v2 directly, and rs-xgb-v2 in turn rests on exp-306, two bureau and contact features and find-rs-region-proxy.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q4
clv-bgnbd-v1 rests on three dataset notes: ds-clv-cohort-panel and ds-clv-revenue-monthly through feat-clv-arpu-v1 and feat-clv-tenure, and ds-clv-holdout-2021h1 through exp-501, the accuracy test the note names only in words. The last link is inferred from the note's wording, not from a recorded link.
Notes: work/ds-clv-cohort-panel.md, work/ds-clv-revenue-monthly.md, work/ds-clv-holdout-2021h1.md

## Q5
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 and dec-ed-gbm-for-watchlist, both reached through ed-gbm-v3 or feat-ed-bureau-slope-v1 and the early-delinquency experiments.
Notes: work/dec-ed-promote-v3.md, work/dec-ed-gbm-for-watchlist.md