---
from: [ds-cu-cases-dpd]
updated: 2025-03-10
---
# feat-cu-pay-behaviour is the 6-month payment-to-minimum ratio and partial-payment share from payments_daily
Features: mean ratio of payment to minimum due over 6 months, share of cycles with a partial payment, median days from due date to payment, autopay flag.
Source: `cards.payments_daily`, using posting date rather than value date.
Adds +0.018 AUC to cu-resp-v1 on holdout-2025q1 (n=24,860). Co-linearity with feat-cu-dpd-roll-v1 on partial-payment share is 0.61; both kept.
