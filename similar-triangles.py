#!/usr/bin/env python3

# Learning Python
#
# Task from Checkio.org - Similar Triangles

from typing import List, Tuple
Coords = List[Tuple[int, int]]

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    def leng(p) -> List:
        [p1, p2, p3] = p
        return sorted([ ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2), ((p1[0]-p3[0])**2 + (p1[1]-p3[1])**2), ((p2[0]-p3[0])**2 + (p2[1]-p3[1])**2) ])

    l1 = leng(coords_1)
    l2 = leng(coords_2)
    if l1[0]/l2[0] == l1[1]/l2[1] and l1[2]/l2[2] == l1[1]/l2[1]:
        return True

    return False


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
