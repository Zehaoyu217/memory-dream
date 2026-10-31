---
from: []
updated: 2025-02-17
---
# 2.1M transaction descriptors sampled from cards.txn_daily, Jan-Jun 2025
Sample pulled from `cards.txn_daily` for January to June 2025: 2.1M rows, one row per transaction, descriptor string plus MCC.
A spot-check of masking on 500 rows found no unmasked card or account numbers.
Descriptors are raw bank strings: store numbers, '#' codes and city suffixes appear in about 38% of rows.
Source for feat-txc-descriptor-tokens-v1 and feat-txc-normalise-v2.
