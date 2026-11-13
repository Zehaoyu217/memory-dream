## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. They reach it through cr-lgbm-v1, cr-lgbm-v2 and feat-cr-caller-history-v2 (via feat-cr-ivr-path-v1 and exp-101/103 to 106).
Notes: work/ds-cr-ivr-paths.md, work/dec-cr-lgbm.md, work/dec-cr-caller-v2.md, work/dec-cr-cost-matrix.md, work/dec-cr-pilot.md

## Q2
cli-xgb-v1 was replaced by cli-xgb-v2, which was replaced by cli-xgb-v3, the note in force now. cli-xgb-v3 is built on exp-106-credit-line-increase, exp-107-credit-line-increase and find-cli-uplift-wins. The v2 out-of-time AUC check it names in words is not placed as a note, so that link is not in the chain.
Notes: work/cli-xgb-v3.md, work/cli-xgb-v2.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls directly through the caller-history and tenure features, and ds-cr-ivr-paths through feat-cr-ivr-path-v1. Both are reached through the feature and experiment notes it was built on.
Notes: work/cr-lgbm-v1.md, work/ds-cr-calls.md, work/ds-cr-ivr-paths.md

## Q4
fraud25-gbm-v1 and fraud25-gbm-v2 both build directly on feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. Note that feat-f25-amt-ratio is itself superseded by feat-f26-amt-zscore.
Notes: work/fraud25-gbm-v1.md, work/fraud25-gbm-v2.md, work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md

## Q5
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. They reach it through cb-elasticity-v1 and v2, exp-201 to 207, and the spend-band and grocery-share features.
Notes: work/ds-cb-spend-panel.md, work/dec-cb-adopt-banded-tiers.md, work/dec-cb-extend-flat-pilot.md, work/dec-cb-threshold-2500.md

## Q6
disp-lgbm-v1 was replaced by disp-lgbm-v2, which was replaced by disp-lgbm-v3, the note in force now. disp-lgbm-v3 is built directly on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307-dispute-triage and feat-disp-fraud-score. Those rest on the v1 chain (dec-disp-labels-two-analyst, ds-disp-analyst-labels, feat-disp-reason-text), the amount-band, txn-match and merchant-chargeback features, and fraud26-gbm-v3.
Notes: work/disp-lgbm-v3.md, work/disp-lgbm-v2.md, work/dec-disp-fraud-score-in.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md, work/disp-lgbm-v1.md, work/dec-disp-labels-two-analyst.md, work/ds-disp-analyst-labels.md, work/feat-disp-reason-text.md

## Q7
cb-elasticity-v1 rests on ds-cb-pilot-2025q4 directly and on ds-cb-spend-panel through feat-cb-spend-base.
Notes: work/cb-elasticity-v1.md, work/ds-cb-pilot-2025q4.md, work/ds-cb-spend-panel.md

## Q8
mq3-response-gbm-v1 and mq3-uplift-tlearner-v1 both build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1.
Notes: work/mq3-response-gbm-v1.md, work/mq3-uplift-tlearner-v1.md, work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md

## Q9
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h through the chatbot experiments and findings. dec-cb-metric-24h is superseded by dec-cb-metric-48h but still rests on the linkage dataset.
Notes: work/ds-cb-call-linkage.md, work/dec-cb-metric-24h.md, work/dec-cb-rollout-60.md, work/dec-cb-handoff-v2.md, work/dec-cb-metric-48h.md

## Q10
ed-gbm-v1 was replaced by ed-gbm-v2, which was replaced by ed-gbm-v3, the note in force now. ed-gbm-v3 is built on ed-gbm-v2, exp-207-early-delinquency and feat-ed-bureau-slope-v1, plus the utilisation-trend, cash-advance and min-pay features. Those features rest on ds-ed-current-base, and the bureau slope on ds-ed-bureau-join. The feat-ed-cashadv-v1 link to the scoring population is named only in words.
Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/exp-207-early-delinquency.md, work/feat-ed-util-trend-v1.md, work/feat-ed-cashadv-v1.md, work/feat-ed-minpay-v2.md, work/feat-ed-bureau-slope-v1.md