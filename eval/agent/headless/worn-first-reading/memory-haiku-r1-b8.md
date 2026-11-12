## Q1
cld-gbm-v3 is the model in force at the end of the line (cld-gbm-v1 was replaced by cld-gbm-v2, which was replaced by cld-gbm-v3). It is built directly on cld-gbm-v2 and feat-cld-payment-shock, and back through them on cld-gbm-v1, feat-cld-risk-band-v1 and v2, ds-cld-decrease-cohort and feat-cli-util-v2.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md, limit-decrease-policy/cld-gbm-v1.md, limit-decrease-policy/feat-cld-risk-band-v1.md, limit-decrease-policy/feat-cld-risk-band-v2.md, limit-decrease-policy/ds-cld-decrease-cohort.md, credit-line-increase/feat-cli-util-v2.md

## Q2
cc-ft-v1 rests on three dataset notes directly or through its inputs: ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and ds-cc-tickets-raw as the root through feat-cc-embed-v1 and ds-cc-qa-labels.
Notes: complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (through xs-gbm-v2) and dec-xs-retrain-quarterly (through find-xs-drift-2026 and exp-407).
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v3 is the model in force (mrisk-gbm-v1 was replaced by mrisk-gbm-v2, which was replaced by mrisk-gbm-v3). It is built directly on exp-507, feat-mrisk-dispute-ratio and mrisk-gbm-v2, and back through them on mrisk-gbm-v1, the merchant-month panel, the chargeback and merchant datasets, and the dispute-triage merchant link.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/mrisk-gbm-v2.md, merchant-risk/mrisk-gbm-v1.md, merchant-risk/ds-mrisk-merchant-month.md, merchant-risk/feat-mrisk-cb-ratio-90d.md, merchant-risk/feat-mrisk-new-merchant.md, merchant-risk/ds-mrisk-chargebacks.md, merchant-risk/ds-mrisk-merchants.md, dispute-triage/ds-disp-merchant-link.md

## Q5
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop and ds-cli-outcome-90d, reached through its feature inputs.
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2, both through exp-501 and the later ML model and feature notes.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-gmm-v3 is the segment model in force (pbs-kmeans-v1 was replaced by pbs-gmm-v2, which was replaced by pbs-gmm-v3). It is built directly on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2, and back through them on pbs-kmeans-v1, the three payment features, exp-402, and the two payment datasets.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/pbs-gmm-v2.md, payment-behavior-segments/exp-402.md, payment-behavior-segments/pbs-kmeans-v1.md, payment-behavior-segments/feat-pbs-cash-share.md, payment-behavior-segments/feat-pbs-minpay-flag.md, payment-behavior-segments/feat-pbs-pay-ratio-v1.md, payment-behavior-segments/ds-pbs-payments-12m.md, payment-behavior-segments/ds-pbs-statement-balances.md

## Q8
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre directly through exp-403-callcentre-naive and feat-xs-call-recent, and ds-xs-offer-log through the propensity question.
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the later models and experiments.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v3 is the model in force (rs-xgb-v1 was replaced by rs-xgb-v2, which was replaced by rs-xgb-v3). It is built directly on exp-308 and rs-xgb-v2, and back through them on exp-306, feat-rs-contact-attempts, find-rs-region-proxy, rs-xgb-v1, the recovery label and charge-off base datasets, and the balance and payment features.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/exp-308.md, recovery-scoring/rs-xgb-v2.md, recovery-scoring/exp-306.md, recovery-scoring/feat-rs-contact-attempts.md, recovery-scoring/find-rs-region-proxy.md, recovery-scoring/rs-xgb-v1.md, recovery-scoring/ds-rs-recovery-labels.md, recovery-scoring/feat-rs-balance-at-co.md, recovery-scoring/feat-rs-pay-before-co.md, recovery-scoring/ds-rs-chargeoff-base.md