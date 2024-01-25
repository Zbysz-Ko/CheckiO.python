#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - Long repeat
"""

from re import findall

def long_repeat(line: str) -> int:
    """
    length the longest substring that consists of the same char
    """
    return max(map(len, findall("+|".join(set(line))+"+", line))) if line else 0


print("Example:")
print(long_repeat(""))

assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
