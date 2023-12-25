#!/usr/bin/env python3

# Learning Python
#
# Task from Checkio.org - Ugly Numbers
# Version with improved performance and with cache in memory

def ugly_number(n: int, ugly: list = [1], c: list = [0, 0, 0, 2, 3, 5]) -> int:

    if len(ugly) >= n:
        return ugly[n-1]

    while len(ugly) < n:
        ugly.append( min(c[3], c[4], c[5]) )
        
        if ugly[-1] == c[3]:
            c[0] += 1
            c[3] = ugly[c[0]] * 2
        if ugly[-1] == c[4]:
            c[1] += 1
            c[4] = ugly[c[1]] * 3
        if ugly[-1] == c[5]:
            c[2] += 1
            c[5] = ugly[c[2]] * 5
    
    return ugly[n-1]

if __name__ == "__main__":
    print("Example:")
    print(ugly_number(4))
    print(ugly_number(6))
    print(ugly_number(11))
    print(ugly_number(1))
    print(ugly_number(29))
    print(ugly_number(84))
    print(ugly_number(313))
    print(ugly_number(171))
    print(ugly_number(593))
    print(ugly_number(899))
    print(ugly_number(978))
    print(ugly_number(1173))
    print(ugly_number(1398))
    print(ugly_number(1407))
    print(ugly_number(1500))
    print(ugly_number(9999))
    print(ugly_number(345987))
    print(ugly_number(567890))
    print(ugly_number(777777))
    print(ugly_number(1000000))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert ugly_number(4) == 4
    assert ugly_number(6) == 6
    assert ugly_number(11) == 15
    print("Ugly Numbers coding complete? Click 'Check' to earn cool rewards!")
    