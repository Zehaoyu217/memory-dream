## Q1
Decisions resting on ds-cu-call-outcomes are dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3. Each reaches the dataset through cu-resp-v1, feat-cu-call-tod-v1 or cu-uplift-v3. The collections-channel-mix decisions that cite dec-cu-promote-v3 are references, not builds, so they are excluded.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/cu-resp-v1.md, collections-uplift/feat-cu-call-tod-v1.md, collections-uplift/exp-103.md, collections-uplift/find-cu-tod-leak.md, collections-uplift/find-cu-tod-gain.md, collections-uplift/dec-cu-drop-tod.md, collections-uplift/exp-105.md, collections-uplift/find-cu-response-misranks.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/cu-uplift-v3.md, collections-uplift/dec-cu-promote-v3.md

## Q2
inc-gbm-v3 is the note in force. It builds on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2, which it replaces.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md, income-estimation/inc-gbm-v1.md

## Q3
Only one note in another project builds directly on rdm-uplift-v1: customer-lifetime-value/exp-506, which builds on clv-ml-v2 and rdm-uplift-v1.
Notes: customer-lifetime-value/exp-506.md, reactivation-dormant/rdm-uplift-v1.md

## Q4
ch-bandit-v1 rests on the dataset notes ds-ch-contact-costs, ds-ch-ab-wave1 and ds-ch-ab-wave2. ds-ch-contact-costs feeds the feature notes and ds-ch-ab-wave1; ds-ch-ab-wave1 feeds ds-ch-ab-wave2 and the SMS-versus-call findings.
Notes: collections-channel-mix/ch-bandit-v1.md, collections-channel-mix/ch-propensity-v2.md, collections-channel-mix/exp-507.md, collections-channel-mix/ch-propensity-v1.md, collections-channel-mix/exp-506.md, collections-channel-mix/feat-ch-prefer-channel-v1.md, collections-channel-mix/feat-ch-send-window-v1.md, collections-channel-mix/feat-ch-prior-contact-v1.md, collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md, collections-channel-mix/find-ch-sms-matches-call.md, collections-channel-mix/exp-501.md, collections-channel-mix/exp-502.md, collections-channel-mix/q-ch-sms-vs-call.md

## Q5
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 (char 3–5 gram TF-IDF on raw descriptors) and feat-txc-mcc-prior (per-merchant MCC prior).
Notes: txn-categorization/txc-gbm-v2.md, txn-categorization/txc-logreg-v1.md, txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Decisions resting on ds-cc-holdout are dec-cc-ft-v1 and dec-cc-drop-dispute-v1. Both reach it through cc-logreg-v1, the direct dependent, via exp-201 (dec-cc-ft-v1) and the dispute-link chain exp-202 → exp-204 (dec-cc-drop-dispute-v1).
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/exp-201.md, complaint-classification/cc-logreg-v1.md, complaint-classification/ds-cc-holdout.md, complaint-classification/dec-cc-drop-dispute-v1.md, complaint-classification/feat-cc-dispute-link-v2.md, complaint-classification/fnd-cc-dispute-link-leak.md, complaint-classification/exp-204.md, complaint-classification/fnd-cc-dispute-link-helps.md, complaint-classification/exp-202.md

## Q7
feat-lbl-churn-flag-closure is in force. It builds on dec-lbl-churn-closure and feat-lbl-churn-flag-90d, which replaced feat-lbl-churn-flag-60d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md, label-pipeline-rebuild/feat-lbl-churn-flag-60d.md

## Q8
Two notes in revenue-forecast-2026 build directly on spend-forecasting's sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1. rev26-interchange-v1 uses it as a volume source, but its builds-on line does not name it.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md, spend-forecasting/sfc-hier-v3.md

## Q9
cu-resp-v1 rests on the dataset notes ds-cu-call-outcomes and ds-cu-cases-dpd. ds-cu-call-outcomes supplies the label and the contact-history feature, and ds-cu-cases-dpd supplies the base population for the DPD-roll and payment-behaviour features.
Notes: collections-uplift/cu-resp-v1.md, collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md, collections-uplift/feat-cu-dpd-roll-v1.md, collections-uplift/feat-cu-pay-behaviour.md, collections-uplift/feat-cu-contact-hist-v2.md

## Q10
Only dec-cli-uplift-targeting rests on ds-cli-holdout-2025q4, through cli-xgb-v1 (which it reaches via cli-xgb-v2, exp-102 and exp-106). The other decisions in the folder do not.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/cli-xgb-v2.md, credit-line-increase/find-cli-uplift-wins.md, credit-line-increase/exp-102.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/ds-cli-holdout-2025q4.md