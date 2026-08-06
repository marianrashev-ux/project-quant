from datetime import date
from project_quant.central_bank_schedule import (CentralBankSchedule)


def test_number_of_meetings():

    schedule = CentralBankSchedule([
        date(2026,9,11),
        date(2026,10,23),
        date(2026,12,11),
    ])

    assert schedule.number_of_meetings(
        date(2026,8,5),
        date(2026,11,1),
    ) == 2

def test_meetings_between():

    schedule = CentralBankSchedule([
        date(2026,9,11),
        date(2026,10,23),
        date(2026,12,11),
    ])

    assert schedule.meetings_between(
        date(2026,8,5),
        date(2026,11,1),
    ) == [
        date(2026,9,11),
        date(2026,10,23),
    ]