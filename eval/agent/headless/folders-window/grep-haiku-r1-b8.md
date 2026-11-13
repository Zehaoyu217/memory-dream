## Q1
cld-gbm-v3 is in force. It builds on cld-gbm-v2 (which replaced v1) and feat-cld-payment-shock.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md

## Q2
cc-ft-v1 rests on three dataset notes: the raw ticket table, the QA labels built on it, and the taxonomy v3 dataset, which has no upstream.
Notes: complaint-classification/cc-ft-v1.md, complaint-classification/ds-cc-tickets-raw.md, complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md

## Q3
Two decisions rest on feat-xs-balance-proxy: dec-xs-top-decile-offer, through exp-405 and xs-gbm-v2 (which builds on xs-gbm-v1), and dec-xs-retrain-quarterly, through exp-407. The call decisions do not chain to the balance proxy.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md, cross-sell-savings/exp-405.md, cross-sell-savings/xs-gbm-v2.md, cross-sell-savings/xs-gbm-v1.md, cross-sell-savings/feat-xs-balance-proxy.md

## Q4
mrisk-gbm-v3 is in force, replacing v2 (which replaced v1). It builds on exp-507, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/mrisk-gbm-v2.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md

## Q5
cli-logreg-baseline rests on two dataset notes: the eligible population and the 90-day outcome, which is built on that population.
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decisions rest on ds-clv-holdout-2021h1 through the model chain: dec-clv-ship-ml-v1, via clv-bgnbd-v1, exp-501 and fnd-clv-bgnbd-bias, and clv-ml-v1; and dec-clv-ship-ml-v2, via clv-ml-v2 and clv-ml-v1. Both models report their MAPE on that holdout. No decision cites the holdout directly.
Notes: customer-lifetime-value/ds-clv-holdout-2021h1.md, customer-lifetime-value/exp-501.md, customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/fnd-clv-bgnbd-bias.md, customer-lifetime-value/clv-ml-v1.md, customer-lifetime-value/clv-ml-v2.md, customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-gmm-v3 is in force. It replaces pbs-gmm-v2, which replaced pbs-kmeans-v1, and it builds on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/pbs-gmm-v2.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md

## Q8
xs-call-uplift-v1 rests on two dataset notes: the call-centre dataset and the offer log, which the call-centre dataset is built on.
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decisions rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the model chain (disp-lgbm-v1 and disp-lgbm-v2, then disp-lgbm-v3).
Notes: dispute-triage/ds-disp-analyst-labels.md, dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/disp-lgbm-v1.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v3 is in force. It replaces rs-xgb-v2, which replaced rs-xgb-v1, and it builds on exp-308 and rs-xgb-v2.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/rs-xgb-v2.md, recovery-scoring/exp-308.md