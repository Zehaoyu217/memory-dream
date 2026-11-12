## Q1
feat-rs-region-rate is an out-of-fold, smoothed recovery rate by postcode region. Adding it lifted recovery-scoring Gini from 0.41 to 0.44 on recovery-scoring-holdout-2023h2 (exp-303), but compliance flagged it as a proxy for neighbourhood demographics: a 2.9x recovery spread across region deciles at equal balance and payment history (exp-304, find-rs-region-proxy). The decision on 2025-05-22 was to drop it from all recovery-scoring models, at a cost of 0.02 Gini (0.44 to 0.42).
Sources: memory/recovery-scoring/feat-rs-region-rate.md, memory/recovery-scoring/exp-303.md, memory/recovery-scoring/exp-304.md, memory/recovery-scoring/find-rs-region-proxy.md, memory/recovery-scoring/dec-rs-drop-region.md

## Q2
The naive comparison showed a call in the prior 90 days adds +1.8 points of open rate (4.9% against 3.1%). After matching on propensity and tenure the effect fell to +0.6 points, not significant, so the naive figure was mostly selection (find-xs-call-overstated). A causal forest (xs-call-uplift-v1) then found +1.2 points in deciles 1-2, and the decision of 2025-11-10 limits call-centre savings outreach to deciles 1-2 (confirmed in exp-406).
Sources: memory/cross-sell-savings/exp-403-callcentre-naive.md, memory/cross-sell-savings/find-xs-call-overstated.md, memory/cross-sell-savings/xs-call-uplift-v1.md, memory/cross-sell-savings/dec-xs-call-low-deciles.md, memory/cross-sell-savings/exp-406-call-uplift.md

## Q3
sfc-hier-v3 is the current segment spend forecast (total MAPE 2.3% on sfc-oot-2025h2). Its direct inputs are sfc-lgbm-v2, feat-sfc-active-accounts (an active-account regressor), fnd-sfc-q4-reconciled and exp-207 (MinT reconciliation). Further back it rests on 17 notes, including the lag, seasonality and CPI-lag features, the segment monthly dataset and the macro and holiday calendars.
Sources: memory/spend-forecasting/sfc-hier-v3.md, memory/spend-forecasting/exp-207.md, memory/spend-forecasting/feat-sfc-active-accounts.md, memory/spend-forecasting/fnd-sfc-q4-reconciled.md, memory/spend-forecasting/dec-sfc-ship-hier-v3.md

## Q4
The fraud-2026 model now uses an alert threshold of 0.66, set by the 2026-08-26 decision to promote fraud26-gbm-v3 (replacing v2, which used 0.62). At 0.66 the v3 candidate gives 21.5% precision at a 0.6% alert rate with recall 0.61 (exp-208).
Sources: memory/fraud-2026/dec-f26-promote-v3.md, memory/fraud-2026/exp-208.md, memory/fraud-2026/fraud26-gbm-v3.md, memory/fraud-2026/dec-f26-promote-v2.md

## Q5
mrisk-gbm-v2 reached AUC 0.86 and precision@100 of 0.43 on mrisk-oot-2026h1 (exp-505, 2026-07-06, re-confirmed as the reference in exp-507). It has since been superseded by mrisk-gbm-v3, which reached AUC 0.91 and precision@100 0.58 on the same holdout.
Sources: memory/merchant-risk/exp-505.md, memory/merchant-risk/mrisk-gbm-v2.md, memory/merchant-risk/exp-507.md, memory/merchant-risk/mrisk-gbm-v3.md

## Q6
The new-account scorecard was rebuilt as v4 (dec-app-rebuild-v4, 2026-06-26) because app-scorecard-v3's out-of-time Gini fell from 0.41 to 0.33 on the 2026-Q1 holdout as bureau scores drifted (find-app-gini-v3-drift). The rebuild keeps the explainable points-based form but moves to v10 bureau bands, reject-inference weights and an income estimate. On application-scorecard-oot-2026h1 it reached Gini 0.42 against 0.35 for v3 (exp-507), and the cutoff was set at 592 from 2026-11-01 (dec-app-cutoff-v4).
Sources: memory/application-scorecard/dec-app-rebuild-v4.md, memory/application-scorecard/find-app-gini-v3-drift.md, memory/application-scorecard/app-scorecard-v4.md, memory/application-scorecard/exp-507.md, memory/application-scorecard/q-app-gini-target.md, memory/application-scorecard/dec-app-cutoff-v4.md

## Q7
feat-txc-normalise-v2 strips store numbers, hash codes and city suffixes from transaction descriptors (2025-09-22). Its rule list is versioned in the repo, and new suffixes are added by pull request rather than by the model. It lifted txc-gbm-v2 macro-F1 from 0.78 to 0.81 on holdout-2025q2 (exp-104), and it is an input to txc-gbm-v3, the shipped model (macro-F1 0.83 on txc-oot-2026h1, decision of 2026-03-10).
Sources: memory/txn-categorization/feat-txc-normalise-v2.md, memory/txn-categorization/exp-104.md, memory/txn-categorization/txc-gbm-v3.md, memory/txn-categorization/dec-txc-ship-gbm-v3.md, memory/txn-categorization/feat-txc-descriptor-tokens-v2.md

## Q8
exp-205 added the payment-to-minimum ratio (feat-ed-minpay-v2) to ed-gbm-v1, lifting AUC from 0.781 to 0.803 on early-delinquency-holdout-2024q4 (n=402,000), with no leakage (find-ed-minpay). That led to ed-gbm-v2 (2025-09-10), which was in turn superseded by ed-gbm-v3 (2026-06-15). ed-gbm-v3 reached AUC 0.809 on early-delinquency-oot-2026h1 with score PSI 0.07, after exp-207 added the bureau slope.
Sources: memory/early-delinquency/exp-205.md, memory/early-delinquency/find-ed-minpay.md, memory/early-delinquency/ed-gbm-v2.md, memory/early-delinquency/ed-gbm-v3.md, memory/early-delinquency/feat-ed-minpay-v2.md

## Q9
fsm-churn-xgb-v2 reads 41 features from the feature store: v1's 40 features, with feat-fsm-payment-lag-v2 (payment lag in UTC) and feat-fsm-util-ratio (balance over limit at month-end) taken from the store, plus feat-fsm-spend-cv-30d (30-day coefficient of variation of approved spend). The model reads payment lag v2 only, not v1.
Sources: memory/feature-store-migration/fsm-churn-xgb-v2.md, memory/feature-store-migration/exp-105.md, memory/feature-store-migration/feat-fsm-payment-lag-v2.md, memory/feature-store-migration/feat-fsm-util-ratio.md, memory/feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
The approval cutoff for application decisions on the v10 scale is 652, set by dec-bsm-cutover-2026q3 (2026-08-25) for the cutover on 2026-09-01. It replaces the v8 cutoff of 640 and holds the 58% approval rate with a 4.1% bad rate (exp-305). The v8 fallback stays in place.
Sources: memory/bureau-score-migration/dec-bsm-cutover-2026q3.md, memory/bureau-score-migration/exp-305.md, memory/bureau-score-migration/bsm-cutoff-logit.md, memory/bureau-score-migration/q-bsm-psi-shift.md