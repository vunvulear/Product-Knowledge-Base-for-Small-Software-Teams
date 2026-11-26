# Business rules

Fictional example only.

| ID | Rule | Evidence for intent | Implementation evidence | Notes |
| --- | --- | --- | --- | --- |
| BRULE-001 | Do not accept two appointments for the same time slot. | `source-sample/business-brief.md`, “Appointment booking” | `source-sample/booking_rules.py`; `source-sample/test_booking_rules.py` | Time-slot equality is the only modeled conflict in this tiny sample. |
| BRULE-002 | Show confirmation after an accepted request. | `source-sample/business-brief.md`, “Appointment booking” | No UI or messaging implementation is included in this example. | Implementation not established. |

Cancellation, payments, opening hours, capacity beyond one booking per slot, and notification channel are open questions, not assumed rules.
