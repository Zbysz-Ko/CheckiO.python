#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - Counting tiles
"""

from math import ceil, sqrt, floor

def checkio(radius):
    """count tiles"""
    return [4*sum([floor(sqrt(radius**2-i**2)) for i in range(1, ceil(radius))]), 8*ceil(radius)-4]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
    