---
from: [ds-nps-behaviour-join]
updated: 2025-10-02
---
# Complaint flag: any complaint call in the 90 days before the send date, from `callcenter.calls`
Binary flag, plus a count. Source table owned by cx-analytics; joined on the account key before send_date.
Used in nps-gbm-v1 and nps-gbm-v2.
