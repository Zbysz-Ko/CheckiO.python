#!/usr/bin/env python3

# Learning Python
#
# Task from Checkio.org - Ugly Numbers
# Version "one by one" (with cache)

def prime_factor(num: int) -> bool:
    while num % 2 == 0:
        num = num / 2
    while num % 3 == 0:
        num = num / 3
    while num % 5 == 0:
        num = num / 5
    return True if num == 1 else False

def ugly_number(n: int, ugly: iter = []) -> int:
    if len(ugly) >= n:
        return ugly[n-1]
    num = 0
    if len(ugly) > 0:
        num = ugly[-1]
    while len(ugly) < n:
        num += 1
        if prime_factor(num):
            ugly.append(num)
    return ugly[n-1]

if __name__ == "__main__":
    print("Example:")
    print(ugly_number(10))
    print(ugly_number(15))
    print(ugly_number(5))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert ugly_number(4) == 4
    assert ugly_number(6) == 6
    assert ugly_number(11) == 15
    print("Ugly Numbers coding complete? Click 'Check' to earn cool rewards!")
    