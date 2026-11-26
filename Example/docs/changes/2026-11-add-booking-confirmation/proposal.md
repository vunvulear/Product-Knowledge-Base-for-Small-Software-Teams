# Change proposal: Add a customer confirmation after booking

**Example status:** fictional proposal, not implemented in sample code.

- Issue: Not applicable; this is a demonstration record.
- Related requirement: [BR-003](../../business/requirements.md)

## Why

The fictional business brief says the customer sees a confirmation after an appointment request is accepted. The sample implementation only returns an `accepted` result and includes no customer interface or notification channel. [Sources: `source-sample/business-brief.md`; `source-sample/booking_rules.py`]

## Intended business change

Provide a customer-visible confirmation after acceptance. The delivery method is not specified and needs a business decision before implementation.

## Open question

Should confirmation appear only on screen, be sent by email/SMS, or use another agreed channel? No choice is assumed here.
