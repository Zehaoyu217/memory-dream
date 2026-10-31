## Q1
Chloe reports lift as a point estimate with its 95% confidence interval, e.g. "+1.8 pts (95% CI +0.6 to +3.0)". She does not show p-values, because business readers take "p = 0.04" as proof. Cost per response in $ goes beside the lift in the same table.
Sources: memory/prefs/chloe-martin-campaign-readout.md
## Q2
She colours the winning campaign orange `#E07B24` and makes every other campaign mid-grey. She avoids brand blue as a highlight because blue series were read as "baseline" in the Q3 2025 campaign readout. Maya Ortiz does the opposite and uses brand blue `#1F4E9A` for her focal cohort; each chart follows its owner's convention. The general style rule allows one orange highlight per chart.
Sources: memory/prefs/chloe-martin-highlight-orange.md, memory/prefs/maya-ortiz-focal-colour.md, memory/reporting/chart-style-colour.md
## Q3
From 2026-06-01, a `cli-` model with PSI above 0.20 on any top-20 feature triggers a drift review. All other model families keep the 0.25 trigger, with 0.10–0.25 as "watch". The rule changed because `cli-glm-v2` drifted to PSI 0.22 on `cli_util_ratio` in 2026-04 and was not reviewed until the next cycle. Separately, the general PSI rule from 2026-06-10 is: above 0.10 starts an investigation, and above 0.25 starts a retrain review with an OOT check (retraining is never automatic).
Sources: memory/reporting/monthly-review-psi-trigger-v2.md (supersedes memory/reporting/monthly-review-psi-trigger.md), memory/corrections/psi-two-tier-thresholds.md
## Q4
Default rates, PD and roll rates in risk tables use 2 decimals in percent, e.g. 3.84%. Retention, share and campaign-response percentages use 1 decimal, e.g. 88.4%. Lena Fischer's risk packs follow the same rule: Gini, KS, PD and default rates to 2 decimals, and exposure in $m to 1 decimal.
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md
## Q5
Offer tiers come from `offers.tier_matrix`. The credit-line and pricing tiers run A to E, with A the highest (best promotional APRs) and E the lowest; this corrects an earlier note that said A was the lowest. For retention, Maya Ortiz owns `offers.tier_matrix` v3 (in force since 2025-09-01): a grid of 10 churn deciles by 3 value bands assigning T0 no offer, T1 fee waiver, T2 2.0% cashback, T3 2.0pp APR cut, T4 $40 statement credit. Matrix v4 applies from the April 2026 cycle: T2 cashback drops to 1.5%, and T3 becomes a $25 statement credit in place of the APR cut.
Sources: memory/glossary/tier.md (superseded), memory/corrections/tier-a-highest.md, memory/retention-offers-roi/ds-ror-tier-matrix.md, memory/retention-offers-roi/dec-ror-matrix-v4.md
## Q6
Use the blended rate of 1.9%, not 2.5%: $100 of purchases earns $1.90. The 2.5% figure was the premium-card rate only; standard cards are about 1.6–1.8%. The Q4 2025 finance pack was restated from 2.5% to 1.9%. Since 2026-01-01 the book itself means open consumer accounts only, excluding commercial cards and charged-off balances.
Sources: memory/corrections/interchange-blended.md (supersedes memory/glossary/interchange.md), memory/corrections/book-excludes-commercial.md
## Q7
No. OOT must be a period after the training window that was never used for training, tuning or feature selection; the last months of training data are in-time validation. That mistake made the fraud model's reported 0.88 AUC an in-time number; its true OOT AUC (2024-10 to 2024-12) was 0.84. The current split method takes the last three observation months as OOT, stops training six months before that window as a gap, and splits on `observation_date`, never on account.
Sources: memory/corrections/oot-not-training-tail.md (supersedes memory/glossary/oot.md), memory/howto/oot-split-by-observation-date.md
## Q8
DPD counts from the minimum payment due date, not the statement close date (rule since 2025-11-01). Day 1 is the day after the due date, and a payment posted on the due date still counts as current (0 DPD). The 2025-11 rule had made the due date itself day 1, one day off; the `cards.payments_daily` pipeline was fixed on 2026-01-15. As a result, Nov–Dec 2025 counts in the 1–29 bucket shift by one day, while the 30+ buckets are unchanged.
Sources: memory/corrections/dpd-due-date-offbyone.md (supersedes memory/corrections/dpd-due-date.md, which superseded memory/glossary/dpd.md)
## Q9
Don't call it uplift: uplift is reported only when treatment and control are randomised holdouts. A non-randomised treated-minus-control difference from `marketing.campaign_responses` is reported as "lift" (observational). For example, Chloe Martin's Oct 2025 CLI report showed a 1.8 pp "uplift" that was observational; the randomised uplift was 0.9 pp. For real uplift, use the random 10% holdout drawn before send (`arm = control`), with at least 3,000 accounts per arm, reported as uplift@20% with Qini support.
Sources: memory/corrections/uplift-randomised-only.md (supersedes memory/glossary/uplift.md), memory/howto/campaign-holdout-design.md, memory/howto/uplift-eval-qini-at-20pct.md
## Q10
`feat_disp_cnt_90d_v1` read 14 days past the observation date, which is leakage; the leak scan (`scripts/leak_scan.py`) flagged it. Limiting it to days on or before observation dropped holdout AUC from 0.79 to 0.72, so the 0.79 was inflated by the leak. The feature was rebuilt as v2, which reads only days on or before observation, and v1 was removed from training.
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md