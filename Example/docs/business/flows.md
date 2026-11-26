# Business flows

## Request a repair appointment

**Example status:** fictional. The source brief confirms the customer selects an available date/time and sees a confirmation after acceptance. [Source: `source-sample/business-brief.md`, “Appointment booking”]

### Main path supported by the brief

1. Customer selects an available date and time.
2. System accepts the request if that slot is not already booked.
3. Customer sees a confirmation after acceptance.

### Alternate path observed in sample implementation

- If the slot already exists in the sample booking set, the function returns `accepted: false` with `slot_unavailable`. [Implementation: `source-sample/booking_rules.py`; test: `source-sample/test_booking_rules.py`]

### Not established

How the customer selects a slot, how service duration is determined, and what happens after a rejected request are not specified by the brief.
