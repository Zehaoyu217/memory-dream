## Q1
Chloe Martin reports campaign lift as a point estimate with its 95% confidence interval, for example "+1.8 pts (95% CI +0.6 to +3.0)". She does not show p-values, because business readers take "p = 0.04" as proof. Cost per response in $ goes beside the lift in the same table.
Sources: memory/prefs/chloe-martin-campaign-readout.md
## Q2
She highlights the winning campaign in orange `#E07B24` and puts all other campaigns in mid-grey. She avoids brand blue because readers took blue series to mean "baseline" in the Q3 2025 campaign readout. Maya Ortiz does the opposite and uses brand blue `#1F4E9A` for her focal cohort; each chart follows its owner's convention, and the house rule allows one orange highlight per chart.
Sources: memory/prefs/chloe-martin-highlight-orange.md, memory/reporting/chart-style-colour.md, memory/prefs/maya-ortiz-focal-colour.md
## Q3
Since 2026-06-01, any `cli-` model with PSI above 0.20 on a top-20 feature triggers a drift review. All other model families keep the 0.25 trigger, with 0.10–0.25 as "watch". The change was made because `cli-glm-v2` drifted to PSI 0.22 on `cli_util_ratio` in 2026-04 and was not reviewed until the next cycle. The old rule (above 0.25 for every model) is superseded.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md (supersedes memory/reporting/monthly-review-psi-trigger.md)
## Q4
Default rates, PD and roll rates in risk tables use 2 decimals, for example 3.84%. Retention, share and campaign-response percentages use 1 decimal, for example 88.4%. Lena Fischer's risk packs follow the same rule: PD, default rates and Gini/KS to 2 decimals, and exposure in $m to 1 decimal.
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md
## Q5
Offer tiers are the credit-line and pricing bands assigned to each account from `offers.tier_matrix`, running from A to E. A correction made A the highest tier (best promotional APRs) and E the lowest. About 18% of active accounts are tier A.
Sources: memory/glossary/tier.md (superseded), memory/corrections/tier-a-highest.md
## Q6
Use the blended rate of 1.9%, not 2.5%. The 2.5% figure was the premium-card rate only; standard cards sit around 1.6–1.8%. The Q4 2025 finance pack used 2.5% and was restated to 1.9%. Also note that from 2026-01-01 the book means consumer receivables only, excluding commercial cards and charged-off balances.
Sources: memory/corrections/interchange-blended.md (supersedes memory/glossary/interchange.md), memory/corrections/book-excludes-commercial.md
## Q7
No. OOT must be a period after the training window that was never used for training, tuning or feature selection. The last months of the training data are in-time validation. The fraud model's 0.88 AUC was in-time; its true OOT AUC (2024-10 to 2024-12) was 0.84. The current split runs on `observation_date`, leaves a 6-month unused gap after training, then takes 3 months of OOT.
Sources: memory/corrections/oot-not-training-tail.md (supersedes memory/glossary/oot.md), memory/howto/oot-split-by-observation-date.md
## Q8
DPD counts from the minimum payment due date (since 2025-11-01; previously from the statement close date). Day 1 is the day after the due date, and a payment posted on the due date still counts as current (0 DPD). This corrected the 2025-11 rule, which was off by one day and was fixed in the `cards.payments_daily` pipeline on 2026-01-15. The Nov–Dec 2025 1–29 bucket counts shifted by one day; the 30+ buckets did not change.
Sources: memory/corrections/dpd-due-date-offbyone.md (supersedes memory/corrections/dpd-due-date.md, which superseded memory/glossary/dpd.md)
## Q9
Don't call it uplift. Uplift is reported only when treatment and control are randomised holdouts. An observational treated-minus-control difference from `marketing.campaign_responses` is called "lift". For example, Chloe Martin's Oct 2025 CLI report showed a 1.8 pp "uplift" that was observational; the randomised uplift was 0.9 pp.
Sources: memory/corrections/uplift-randomised-only.md (supersedes memory/glossary/uplift.md)
## Q10
`feat_disp_cnt_90d_v1` read 14 days past the observation date, which is leakage, and the leak scan (`scripts/leak_scan.py`) flagged it. Restricted to days on or before observation, holdout AUC fell from 0.79 to 0.72. It was rebuilt as v2 and v1 was removed from training.
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md