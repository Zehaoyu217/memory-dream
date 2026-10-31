---
from: [ds-xs-offer-log, feat-xs-balance-proxy]
updated: 2025-07-01
supersedes: [feat-xs-balance-proxy]
---
# feat-xs-payroll-flag-v2: recurring payroll-like deposit detected in the last 90 days
Flag set when recurring inflows of at least $800 arrive near-monthly over 90 days, detected from `cards.payments_daily` by pattern matching.
Detected for 61% of eligible accounts under the 2025 descriptors. Payroll-flagged accounts open at 4.8%, against 1.9% for the rest.
Used in xs-gbm-v2.
