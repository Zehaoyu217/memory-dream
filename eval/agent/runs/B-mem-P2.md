## Q1
Chloe Martin reports campaign lift as a point estimate with its 95% confidence interval, e.g. "+1.8 pts (95% CI +0.6 to +3.0)". She does not show p-values, because business readers take "p = 0.04" as proof. Cost per response in $ goes in the same table, next to the lift.
Sources: memory/prefs/chloe-martin-campaign-readout.md
## Q2
She marks the winning campaign in orange `#E07B24` and shows all other campaigns in mid-grey. She avoids brand blue for highlights because readers took blue series as the "baseline" in the Q3 2025 campaign readout. Maya Ortiz does the opposite and uses brand blue `#1F4E9A` for her focal cohort; each chart follows its owner's convention. The general chart rule allows one orange highlight per chart.
Sources: memory/prefs/chloe-martin-highlight-orange.md, memory/prefs/maya-ortiz-focal-colour.md, memory/reporting/chart-style-colour.md
## Q3
Since 2026-06-01, a `cli-` model triggers a drift review when PSI goes above 0.20 on any of its top-20 features. All other model families keep the 0.25 trigger, with 0.10–0.25 counted as "watch". The rule changed because `cli-glm-v2` drifted to PSI 0.22 on `cli_util_ratio` in 2026-04 and was not reviewed until the next cycle. It replaces the earlier 0.25 trigger for all models.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md, memory/reporting/monthly-review-psi-trigger.md
## Q4
Default rates, PD and roll rates in risk tables use 2 decimals, e.g. 3.84%. Retention, share and campaign-response percentages use 1 decimal, e.g. 88.4%. Lena Fischer's risk packs follow the same rule: PD and default rates to 2 decimals in percent, and Gini and KS to 2 decimals.
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md
## Q5
Offer tiers are assigned from the `offers.tier_matrix` table and run A to E. A correction made in 2025-05 says A is the highest tier (best promotional APRs) and E the lowest, reversing the old glossary note. On the retention side, the same table holds Maya Ortiz's matrix: v3 has tiers T0–T4 on a grid of 10 churn deciles by 3 value bands, and v4 takes effect from the April 2026 cycle. Churn risk-tier cuts are also written to this table each night.
Sources: memory/glossary/tier.md, memory/corrections/tier-a-highest.md, memory/retention-offers-roi/ds-ror-tier-matrix.md, memory/churn-2026/dec-risk-tiers.md
## Q6
Use the blended rate of 1.9%, not 2.5%: $100 of purchases earns $1.90. 2.5% is the premium-card rate only, and standard cards sit around 1.6–1.8%. The Q4 2025 finance pack used 2.5% and was restated to 1.9%.
Sources: memory/corrections/interchange-blended.md (supersedes memory/glossary/interchange.md)
## Q7
No. OOT must be a period after the training window that was never used for training, tuning or feature selection; the last months of the training data are only in-time validation. The fraud model's 0.88 AUC was in-time, and its true OOT AUC (2024-10 to 2024-12) was 0.84. The split rule takes the last three observation months as OOT and leaves a six-month gap after training ends (e.g. train through 2024-12, gap 2025-01 to 2025-06, OOT 2025-07 to 2025-09).
Sources: memory/corrections/oot-not-training-tail.md, memory/howto/oot-split-by-observation-date.md
## Q8
DPD counts from the minimum payment due date (since 2025-11-01), no longer from the statement close date. Day 1 is the day after the due date: a payment posted on the due date still counts as current (0 DPD). This fixed an off-by-one in the 2025-11 rule, which counted the due date itself as day 1. The fix went into the `cards.payments_daily` pipeline on 2026-01-15; it shifted Nov–Dec 2025 counts in the 1–29 bucket and left the 30+ buckets unchanged.
Sources: memory/corrections/dpd-due-date-offbyone.md, memory/corrections/dpd-due-date.md
## Q9
Don't call it uplift. Uplift is reported only when treatment and control are randomised holdouts; an observational difference from `marketing.campaign_responses` is reported as "lift". For example, Chloe Martin's Oct 2025 CLI report showed a 1.8 pp "uplift" that was observational, while the randomised uplift was 0.9 pp. In her readouts, report the lift with its 95% CI and no p-value.
Sources: memory/corrections/uplift-randomised-only.md (supersedes memory/glossary/uplift.md), memory/prefs/chloe-martin-campaign-readout.md
## Q10
The leak scan (`scripts/leak_scan.py`) flagged `feat_disp_cnt_90d_v1` because it read data 14 days past the observation date. That leak inflated holdout AUC from 0.72 to 0.79. The rebuilt v2 reads only days on or before the observation date, and v1 was removed from training.
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md