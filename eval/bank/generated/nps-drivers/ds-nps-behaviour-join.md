---
from: [ds-nps-waves]
updated: 2025-09-15
---
# Behaviour features join to `cards.txn_daily` and `callcenter.calls` over the 90 days before each send date
Joins on respondent_key to the account key. Window is 90 days before send_date only. Built by Tomás Rivera (data engineering).
Covers transactions (`cards.txn_daily`), fee charges, and complaint calls (`callcenter.calls`). No post-send data is joined.
