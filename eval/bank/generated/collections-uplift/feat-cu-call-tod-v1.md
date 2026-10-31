---
from: [ds-cu-call-outcomes]
updated: 2025-06-02
---
# feat-cu-call-tod-v1 is the hour-of-day answer rate per account, computed from callcenter.calls
Feature: share of past calls answered in each of four day-parts (morning, midday, afternoon, evening), per account.
Built from `callcenter.calls`. Intended to place calls at the hour the customer is likely to pick up.
Status: adds AUC in exp-103 on holdout-2025q2, but do not use before reading find-cu-tod-leak.
