#!/usr/bin/env python3

"""Learning Python

Task from Checkio.org - Lightbulb End Watching
"""

from datetime import datetime
from typing import List, Optional


def sum_light(
        els: List[datetime],
        start_watching: Optional[datetime] = None,
        end_watching: Optional[datetime] = None,
    ) -> int:
    """How long the light bulb has been turned on"""
    seconds = 0
    while els:
        if end_watching is not None:
            if len(els) == 1:
                els.append(end_watching)
            if end_watching < els[0]:
                return seconds
            elif end_watching >= els[0] and end_watching <= els[1]:
                els[1] = end_watching
        if start_watching is not None:
            if start_watching >= els[0] and start_watching <= els[1]:
                els[0] = start_watching
            elif start_watching > els[1]:
                els = els[2:]
                continue
            else:
                start_watching = None
        seconds += (els.pop(1)-els.pop(0)).total_seconds()
    return seconds

if __name__ == "__main__":
    print("Example:")
    print(
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
    )

    assert (
        sum_light(
            els=[
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            start_watching=datetime(2015, 1, 12, 10, 0, 0),
            end_watching=datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 0),
            datetime(2015, 1, 12, 10, 0, 7),
        )
        == 7
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 3),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 7
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 0, 10),
            ],
            datetime(2015, 1, 12, 10, 0, 10),
            datetime(2015, 1, 12, 10, 0, 20),
        )
        == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 30, 0),
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 0),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 20
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 9, 50, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 9, 0, 0),
            datetime(2015, 1, 12, 10, 5, 0),
        )
        == 300
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
                datetime(2015, 1, 12, 11, 10, 10),
            ],
            datetime(2015, 1, 12, 11, 5, 0),
            datetime(2015, 1, 12, 12, 0, 0),
        )
        == 310
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 11, 5, 0),
            datetime(2015, 1, 12, 11, 10, 0),
        )
        == 300
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 10, 10, 0),
            datetime(2015, 1, 12, 11, 0, 10),
        )
        == 20
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
                datetime(2015, 1, 12, 10, 10, 10),
                datetime(2015, 1, 12, 11, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 10, 0),
            datetime(2015, 1, 12, 10, 20, 20),
        )
        == 610
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 10, 0),
            datetime(2015, 1, 12, 10, 20, 20),
        )
        == 1220
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 9, 0),
            datetime(2015, 1, 12, 10, 0, 0),
        )
        == 0
    )

    assert (
        sum_light(
            [
                datetime(2015, 1, 12, 10, 0, 0),
            ],
            datetime(2015, 1, 12, 9, 9, 0),
            datetime(2015, 1, 12, 10, 0, 10),
        )
        == 10
    )

    print(
        "The third mission in series is completed? Click 'Check' to earn cool rewards!"
    )
