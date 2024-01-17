#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - Count Chains
"""

from typing import List, Tuple
from math import hypot

def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    """ Count groups of circles in chain """
    groups = 0

    def is_intersect(c1, c2):
        """ Check if 2 circles are intersected"""
        return True if c1[2]+c2[2] > hypot(c1[0]-c2[0], c1[1]-c2[1]) > abs(c1[2]-c2[2]) else False

    while circles:
        counter = 0
        chain = [circles.pop()]
        while counter < len(chain):
            for circle in circles.copy():
                if is_intersect(chain[counter], circle):
                    chain.append(circle)
                    circles.remove(circle)
            counter += 1
        groups += 1

    return groups

if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    assert count_chains([(1, 3, 1), (2, 2, 1), (4, 2, 1), (5, 3, 1), (3, 3, 1)]) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
