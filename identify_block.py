#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - Identify Block
"""

def identify_block(n):
    """ Identify letter in grid 4x4 """

    patterns ={"111": "I", "444": "I",
              "114": "J", "134": "J",
              "112": "L", "144": "L",
              "131": "O",
              "121": "S", "414": "S",
              "113": "T", "314": "T",
              "141": "Z", "313": "Z"}
    n = sorted(n)

    if (0, 1) in [(n[i]%4, n[i+1]-n[i]) for i in range(3)]:
        return None

    n = "".join(map(str, [n[i+1]-n[i] for i in range(3)]))
    for i in [n, n[::-1]]:
        if i in patterns:
            return patterns[i]

    return None

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2, 3, 7, 11}) == 'L', 'L'
    assert identify_block({4, 8, 12, 16}) == 'I', 'I'
    assert identify_block({3, 1, 5, 8}) == None, 'None'
    print('"Run" is good. How is "Check"?')
