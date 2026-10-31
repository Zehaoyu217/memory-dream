---
from: [ds-hp-enrolled]
updated: 2025-08-05
---
# feat-hp-txn-drop-v1 is the spend drop in the 3 months before enrolment against the prior 6-month average
Feature: spend in the three months before enrolment as a share of the prior six-month average, plus a flag for a drop of 30% or more.
Source: `cards.txn_daily` aggregated to account-month.
Enrolled accounts show a 30%-plus spend drop in 41% of cases, against 12% of matched controls. This is a selection signal.
