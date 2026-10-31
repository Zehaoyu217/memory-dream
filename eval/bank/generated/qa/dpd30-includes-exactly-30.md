---
updated: 2025-04-15
from: [howto/dpd-bucket-labelling]
---
# Q: Does the 30+ label include accounts at exactly 30 days past due? A: Yes, 30+ means DPD of 30 or more.
Raj Patel's team confirmed this against `cards.payments_daily` on 2025-04-15. An account at 30 DPD sits in the 30 to 59 bucket and counts toward 30+.
The strictly-greater-than version was dropped.
