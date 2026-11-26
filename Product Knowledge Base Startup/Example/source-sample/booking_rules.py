"""Tiny fictional implementation used only to demonstrate source references."""


def create_booking(slot, bookings):
    """Accept a requested slot if no existing booking uses it."""
    if slot in bookings:
        return {"accepted": False, "reason": "slot_unavailable"}
    bookings.add(slot)
    return {"accepted": True, "slot": slot}
