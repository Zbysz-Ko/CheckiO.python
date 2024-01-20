#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - Blood distribution
"""

def distribute_blood(
    blood_avail: dict[str, int], blood_needs: dict[str, int]
) -> dict[str, dict[str, int]]:
    """ Function distribute available blood of different types 
        to patients requiring transfusions, considering each blood 
        type's compatibility restrictions.
    """
    blood_types = ["A","B","AB","O"]
    result = {i: {j: 0 for j in blood_types} for i in blood_types}
    distribution = [[4, 0, 0], [2, 0, "AB"], [3, "O", 0]]

    def distribute(avail, needs):
        change = min(blood_avail[avail], blood_needs[needs])
        blood_avail[avail] -= change
        blood_needs[needs] -= change
        result[avail][needs] += change

    for i in distribution:
        for blood in blood_types[:i[0]]:
            distribute(i[1] if i[1] else blood, i[2] if i[2] else blood)
    return result


if __name__ == "__main__":
    assert distribute_blood(
        {"A": 150, "B": 100, "AB": 0, "O": 0}, {"A": 100, "B": 100, "AB": 50, "O": 0}
    ) == {
        "A": {"A": 100, "B": 0, "AB": 50, "O": 0},
        "B": {"A": 0, "B": 100, "AB": 0, "O": 0},
        "AB": {"A": 0, "B": 0, "AB": 0, "O": 0},
        "O": {"A": 0, "B": 0, "AB": 0, "O": 0},
    }
    assert distribute_blood(
        {"A": 10, "B": 10, "AB": 20, "O": 20}, {"A": 20, "B": 10, "AB": 30, "O": 0}
    ) == {
        "A": {"A": 10, "B": 0, "AB": 0, "O": 0},
        "B": {"A": 0, "B": 10, "AB": 0, "O": 0},
        "AB": {"A": 0, "B": 0, "AB": 20, "O": 0},
        "O": {"A": 10, "B": 0, "AB": 10, "O": 0},
    }

    print("Coding complete? Click 'Check' to earn cool rewards!")
    