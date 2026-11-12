## Q1
The note in force at the end of the cld-gbm-v1 line is cld-gbm-v3, which is built on feat-cld-payment-shock and cld-gbm-v2 (and, back through v2, on feat-cld-risk-band-v2 and cld-gbm-v1).
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/feat-cld-payment-shock.md, limit-decrease-policy/cld-gbm-v2.md

## Q2
cc-ft-v1 rests on the dataset notes ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and on ds-cc-tickets-raw through feat-cc-embed-v1 and ds-cc-qa-labels.
Notes: complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (through xs-gbm-v2 and exp-405-top-decile) and dec-xs-retrain-quarterly (through find-xs-drift-2026 and exp-407-oot-2026h1).
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
The note in force at the end of the mrisk-gbm-v1 line is mrisk-gbm-v3, which is built on mrisk-gbm-v2, feat-mrisk-dispute-ratio and exp-507; the dispute ratio itself comes from dispute-triage's ds-disp-merchant-link.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/mrisk-gbm-v2.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/exp-507.md, dispute-triage/ds-disp-merchant-link.md

## Q5
cli-logreg-baseline rests on the dataset notes ds-cli-eligible-pop and ds-cli-outcome-90d, directly through its feature inputs and the question q-cli-utilization-trigger.
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2, both through exp-501 and the ML model chain.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
The note in force at the end of the pbs-kmeans-v1 line is pbs-gmm-v3, which is built on pbs-gmm-v2, feat-pbs-timing-v2 and exp-403; the chain goes back to ds-pbs-payments-12m and ds-pbs-statement-balances.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/pbs-gmm-v2.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/exp-403.md

## Q8
xs-call-uplift-v1 rests on the dataset notes ds-xs-callcentre and ds-xs-offer-log, through exp-403-callcentre-naive, feat-xs-call-recent and find-xs-call-overstated.
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the model and experiment chain.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
The note in force at the end of the rs-xgb-v1 line is rs-xgb-v3, which is built on rs-xgb-v2 and exp-308 (rs-xgb-v2 itself rests on exp-306, find-rs-region-proxy, feat-rs-bureau-postco-v1 and feat-rs-contact-attempts).
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/rs-xgb-v2.md, recovery-scoring/exp-308.md