from booking_rules import create_booking


def test_accepts_an_available_slot():
    assert create_booking("2026-12-01T10:00", set())["accepted"] is True


def test_rejects_a_slot_already_booked():
    assert create_booking("2026-12-01T10:00", {"2026-12-01T10:00"}) == {
        "accepted": False,
        "reason": "slot_unavailable",
    }
