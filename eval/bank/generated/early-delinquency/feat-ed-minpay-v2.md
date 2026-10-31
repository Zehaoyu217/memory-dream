---
from: [ds-ed-label-30p3m]
updated: 2025-04-08
---
# feat-ed-minpay-v2 is the 6-month payment-to-minimum ratio from payments_daily, using posting date
Version 2: the ratio uses payment posting date. Version 1 used value date and mis-assigned payments made after the due date.
Feature: mean of payment divided by minimum due over six months, plus the count of cycles with a ratio below 1.
Source: `cards.payments_daily`.
