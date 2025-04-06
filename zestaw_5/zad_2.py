#Create the function print_working_days(date1, date2), where 'date1' and 'date2' are strings of the form 'YYYY-MM-DD'.
#The function prints dates of working days (from Monday to Friday) in the given range, 'date2' is excluded.
from datetime import datetime,date, timedelta
from enum import Enum


class Holiday(Enum):
    SATURDAY = 5
    SUNDAY = 6


def print_working_days(date1, date2):
    assert_date_format(date1)
    assert_date_format(date2)
    date_start = date.fromisoformat(date1)
    date_end = date.fromisoformat(date2)

    current = date_start
    while current <= date_end:
        if current.weekday() not in (Holiday.SATURDAY.value, Holiday.SUNDAY.value):
            print(current)
        current += timedelta(days=1)


# generator
def working_days_generator(date1, date2):
    assert_date_format(date1)
    assert_date_format(date2)
    d_start = date.fromisoformat(date1)
    d_end = date.fromisoformat(date2)
    d_delta = d_end - d_start
    working_days = (d
                    for d in (d_start + timedelta(days=i) for i in range(d_delta.days + 1))
                    if d.weekday() not in (Holiday.SATURDAY, Holiday.SUNDAY))
    return working_days

def assert_date_format(date_str: str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        assert False, f"Invalid date format for '{date_str}', expected YYYY-MM-DD"

if __name__ == "__main__":
    date1 = '2025-04-01'
    date2 = '2025-04-06'
    print_working_days(date1, date2)






