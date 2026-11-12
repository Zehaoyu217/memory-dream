## Q1
cld-gbm-v3 is in force. It is built directly on cld-gbm-v2 and feat-cld-payment-shock, which go back through cld-gbm-v1 and feat-cld-risk-band-v2 to ds-cld-decrease-cohort and feat-cli-util-v2.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md, limit-decrease-policy/cld-gbm-v1.md, limit-decrease-policy/feat-cld-risk-band-v2.md, limit-decrease-policy/ds-cld-decrease-cohort.md, limit-decrease-policy/feat-cld-risk-band-v1.md, credit-line-increase/feat-cli-util-v2.md

## Q2
Three dataset notes: ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and ds-cc-tickets-raw through feat-cc-embed-v1.
Notes: complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (via xs-gbm-v2) and dec-xs-retrain-quarterly (via find-xs-drift-2026 and exp-407).
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v3 is in force. It is built directly on exp-507, feat-mrisk-dispute-ratio and mrisk-gbm-v2, which go back through exp-504, feat-mrisk-mcc-base and mrisk-gbm-v1 to the merchant-month dataset and the chargeback labels.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/mrisk-gbm-v2.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md

## Q5
Two dataset notes: ds-cli-eligible-pop directly through the features, and ds-cli-outcome-90d through the features and q-cli-utilization-trigger.
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2, reached through exp-501 and then exp-504 and exp-505.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-gmm-v3 is in force. It is built directly on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2, which go back through exp-402, feat-pbs-interest-paid and pbs-kmeans-v1 to the payment and statement-balance datasets.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/pbs-gmm-v2.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md

## Q8
Two dataset notes: ds-xs-offer-log and ds-xs-callcentre, the second through feat-xs-call-recent and exp-403-callcentre-naive.
Notes: cross-sell-savings/ds-xs-offer-log.md, cross-sell-savings/ds-xs-callcentre.md

## Q9
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst, dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v3 is in force. It is built directly on rs-xgb-v2 and exp-308, and rs-xgb-v2 goes back through exp-306, feat-rs-contact-attempts and find-rs-region-proxy to rs-xgb-v1 and the charge-off dataset.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/rs-xgb-v2.md, recovery-scoring/rs-xgb-v1.md