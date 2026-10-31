---
from: []
updated: 2025-06-10
---
# `survey.nps_wave` holds one row per respondent per quarterly NPS wave, about 46,000 per wave
Owner Chloe Martin (marketing). Waves 2025Q1 (n = 45,800) and 2025Q2 (n = 46,120) at this extract.
Fields: respondent_key, wave, send_date, nps_score (0 to 10), open_text, response_ts.
Respondents are sampled from active accounts; the send date is the cut for all behaviour features.
