# Data model

Fictional example. The sample uses an in-memory Python set of slot values; no persistent database schema is included. [Source: `source-sample/booking_rules.py`]

| Data shape | Observed fields / behavior | Evidence |
| --- | --- | --- |
| Slot | A string used for membership comparison in the booking set. | `source-sample/booking_rules.py`; `source-sample/test_booking_rules.py` |
| Booking result | A dictionary with `accepted`; rejected result also includes `reason`, accepted result includes `slot`. | `source-sample/booking_rules.py` |
