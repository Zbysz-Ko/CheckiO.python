#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - Weekend counter
"""

from datetime import date

def checkio(from_date, to_date):
    """ Count the days of rest """
    days = (to_date-from_date).days + 1
    if secret := from_date.weekday() - 6:
        secret += days%7
    return days//7 * 2 + 1 + ( (secret > 0) - (secret < 0) )

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
