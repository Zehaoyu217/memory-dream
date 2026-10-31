---
from: []
updated: 2025-10-15
---
# feat-fsm-payment-lag-v1: days from statement to payment, mean of last three statements (superseded)
Source `cards.payments_daily`. Difference in days between statement date and payment date, averaged over the last three statements.
Payment timestamps were read in local time, so about 3.1 percent of payments fell on the other side of midnight and changed the day count (exp-101).
Superseded by feat-fsm-payment-lag-v2 after exp-102. Do not use in new models.
