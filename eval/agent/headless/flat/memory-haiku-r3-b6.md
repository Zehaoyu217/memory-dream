## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (through xs-gbm-v2) and dec-xs-retrain-quarterly (through find-xs-drift-2026 and exp-407-oot-2026h1). The tool also flagged 90 other notes that may build on it through unplaced references, so these two are the confirmed chain.
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
The note in force is mrisk-gbm-v3 (AUC 0.91), which replaced mrisk-gbm-v2 and was built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop directly (via feat-cli-util-v1 and feat-cli-pay-behaviour) and ds-cli-outcome-90d (via feat-cli-spend-velocity, itself built on ds-cli-eligible-pop). The tool's automatic chain printed for churn-lr-base-2025, not this note, so I traced it by reading the notes.
Notes: work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
No decision notes rest on ds-clv-holdout-2021h1. Its only dependent is exp-501-customer-lifetime-value, and nothing downstream of that experiment is a decision.
Notes: work/ds-clv-holdout-2021h1.md, work/exp-501-customer-lifetime-value.md

## Q5
The note in force is dec-pbs-gmm-v3-current, the decision adopting pbs-gmm-v3 as the segment table of record. It is built on fnd-pbs-five-segments and pbs-gmm-v3.
Notes: work/dec-pbs-gmm-v3-current.md, work/fnd-pbs-five-segments.md, work/pbs-gmm-v3.md

## Q6
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre (via exp-403-callcentre-naive and feat-xs-call-recent) and ds-xs-offer-log (via q-xs-propensity). Some of its build links are named only in words with no note, so grep would be needed to confirm the full chain.
Notes: work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q7
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst (directly), dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in (through the dispute-triage chain).
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q8
The note in force is rs-xgb-v3, the recovery classifier with a regression head, which replaced rs-xgb-v2. It is built on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q9
clv-bgnbd-v1 rests on two dataset notes: ds-clv-cohort-panel (via feat-clv-tenure) and ds-clv-revenue-monthly (via feat-clv-arpu-v1). Its link to the "bg/nbd versus gbm accuracy test" has no note, so that part is unverified.
Notes: work/ds-clv-cohort-panel.md, work/ds-clv-revenue-monthly.md

## Q10
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 and dec-ed-gbm-for-watchlist, both through the bureau-slope and GBM-vs-logit chain.
Notes: work/dec-ed-promote-v3.md, work/dec-ed-gbm-for-watchlist.md