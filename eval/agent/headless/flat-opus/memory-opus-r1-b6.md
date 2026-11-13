## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer and dec-xs-retrain-quarterly. Both come through xs-gbm-v1 → xs-gbm-v2 and the experiments built on them (exp-405, exp-407, find-xs-drift-2026). The proxy itself was later replaced by feat-xs-payroll-flag-v2.
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md, work/feat-xs-balance-proxy.md, work/xs-gbm-v1.md, work/xs-gbm-v2.md

## Q2
The line runs mrisk-gbm-v1 → mrisk-gbm-v2 → mrisk-gbm-v3, and mrisk-gbm-v3 is the model in force now. It is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md, work/mrisk-gbm-v1.md

## Q3
cli-logreg-baseline is built on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour. Through those it rests on two dataset notes: ds-cli-eligible-pop (the "cli-eligible population counts" in the feature notes' wording) and ds-cli-outcome-90d, which itself is built on ds-cli-eligible-pop.
Notes: work/cli-logreg-baseline.md, work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md, work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
Two decision notes rest on it: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2, which replaced it. The chain runs ds-clv-holdout-2021h1 → exp-501 (the "bg/nbd versus gbm accuracy test") → clv-bgnbd-v1, exp-503 and fnd-clv-bgnbd-bias → clv-ml-v1 → those decisions. The two links from exp-501 are named only in words in the notes, which is why the tool's chain stopped at exp-501.
Notes: work/dec-clv-ship-ml-v1.md, work/dec-clv-ship-ml-v2.md, work/ds-clv-holdout-2021h1.md, work/exp-501-customer-lifetime-value.md, work/clv-bgnbd-v1.md, work/clv-ml-v1.md

## Q5
The line runs pbs-kmeans-v1 → pbs-gmm-v2 → pbs-gmm-v3, and the last step is dec-pbs-gmm-v3-current, which is now in force. That decision is built on fnd-pbs-five-segments and pbs-gmm-v3.
Notes: work/dec-pbs-gmm-v3-current.md, work/fnd-pbs-five-segments.md, work/pbs-gmm-v3.md, work/pbs-gmm-v2.md, work/pbs-kmeans-v1.md

## Q6
xs-call-uplift-v1 is built on exp-403-callcentre-naive, feat-xs-call-recent and find-xs-call-overstated. Through those it rests on two dataset notes: ds-xs-callcentre and, under that, ds-xs-offer-log, which goes back to q-xs-propensity.
Notes: work/xs-call-uplift-v1.md, work/exp-403-callcentre-naive.md, work/feat-xs-call-recent.md, work/find-xs-call-overstated.md, work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q7
Four decision notes rest on ds-disp-analyst-labels. dec-disp-labels-two-analyst rests on it directly; dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in come through the dispute-triage experiments and the disp-lgbm models.
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md, work/ds-disp-analyst-labels.md

## Q8
The line runs rs-xgb-v1 → rs-xgb-v2 → rs-xgb-v3, and rs-xgb-v3 is the model in force now. It is built on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md, work/rs-xgb-v1.md

## Q9
clv-bgnbd-v1 is built on feat-clv-arpu-v1, feat-clv-tenure and exp-501, the accuracy test (named only in words in the note). Through those it rests on three dataset notes: ds-clv-revenue-monthly, ds-clv-cohort-panel and ds-clv-holdout-2021h1. The chain goes back to the churn glossary term and q-clv-model-choice.
Notes: work/clv-bgnbd-v1.md, work/feat-clv-arpu-v1.md, work/feat-clv-tenure.md, work/exp-501-customer-lifetime-value.md, work/ds-clv-revenue-monthly.md, work/ds-clv-cohort-panel.md, work/ds-clv-holdout-2021h1.md

## Q10
Two decision notes rest on ds-ed-bureau-join: dec-ed-gbm-for-watchlist (through ed-logit-v1 → exp-201 → find-ed-gbm-vs-logit) and dec-ed-promote-v3, which replaced it (through feat-ed-bureau-slope-v1 → exp-207, find-ed-bureau-slope and ed-gbm-v3).
Notes: work/dec-ed-gbm-for-watchlist.md, work/dec-ed-promote-v3.md, work/ds-ed-bureau-join.md, work/ed-logit-v1.md, work/feat-ed-bureau-slope-v1.md