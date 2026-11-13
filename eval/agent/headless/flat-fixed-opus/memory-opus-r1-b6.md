## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (through xs-gbm-v2) and dec-xs-retrain-quarterly (through exp-407-oot-2026h1 and find-xs-drift-2026).
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
The line runs mrisk-gbm-v1 → mrisk-gbm-v2 → mrisk-gbm-v3, so mrisk-gbm-v3 is the one in force now. It is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline rests on two dataset notes. ds-cli-eligible-pop comes through feat-cli-util-v1, feat-cli-pay-behaviour and q-cli-utilization-trigger, and ds-cli-outcome-90d comes through feat-cli-spend-velocity (ds-cli-outcome-90d itself is built on ds-cli-eligible-pop).
Notes: work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and the decision that replaced it, dec-clv-ship-ml-v2. Both come through the chain exp-501 → clv-bgnbd-v1 → clv-ml-v1/v2.
Notes: work/dec-clv-ship-ml-v1.md, work/dec-clv-ship-ml-v2.md

## Q5
The line runs pbs-kmeans-v1 → pbs-gmm-v2 → pbs-gmm-v3, so pbs-gmm-v3 is the one in force now. It is built on exp-403-payment-behavior-segments, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: work/pbs-gmm-v3.md, work/exp-403-payment-behavior-segments.md, work/feat-pbs-timing-v2.md, work/pbs-gmm-v2.md

## Q6
xs-call-uplift-v1 rests on two dataset notes. ds-xs-callcentre comes through exp-403-callcentre-naive and feat-xs-call-recent, and ds-xs-offer-log is what ds-xs-callcentre is built on. The memory flagged some links stated only in words, but they describe the same notes already in the chain.
Notes: work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q7
Four decision notes rest on ds-disp-analyst-labels. dec-disp-labels-two-analyst is built on it directly. dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in rest on it through other notes.
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q8
The line runs rs-xgb-v1 → rs-xgb-v2 → rs-xgb-v3, so rs-xgb-v3 is the one in force now. It is built on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q9
clv-bgnbd-v1 rests on three dataset notes. ds-clv-holdout-2021h1 comes through exp-501-customer-lifetime-value, and ds-clv-revenue-monthly comes through feat-clv-arpu-v1. ds-clv-cohort-panel comes through feat-clv-tenure and is also what the other two datasets are built on.
Notes: work/ds-clv-holdout-2021h1.md, work/ds-clv-revenue-monthly.md, work/ds-clv-cohort-panel.md

## Q10
Two decision notes rest on ds-ed-bureau-join: dec-ed-gbm-for-watchlist (through ed-logit-v1, the experiments and find-ed-gbm-vs-logit) and dec-ed-promote-v3, which replaced it (through feat-ed-bureau-slope-v1 and ed-gbm-v3).
Notes: work/dec-ed-gbm-for-watchlist.md, work/dec-ed-promote-v3.md