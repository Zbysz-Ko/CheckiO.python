#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - Unix Match part 1
"""

def unix_match(filename: str, pattern: str) -> bool:
    """ Match pattern to filename """

    pos, star = 0, False

    for i, char in enumerate(pattern):
        if pos > len(filename):
            return False
        match char:
            case "*":
                star = True
            case "?":
                pos += 1
            case _:
                while star:
                    if char in filename[pos:]:
                        if unix_match(filename[filename.find(char, pos):], pattern[i:]):
                            return True
                        pos += 1
                    else:
                        return False
                if filename[pos] == char:
                    pos += 1
                else:
                    return False
    if not star and filename[pos:]:
        return False
    return True

assert unix_match("somefile1file22.ttxt", "so*me*file??.*t") == True

print("Example:")
print(unix_match("somefile.txt", "*"))

# These "asserts" are used for self-checking
assert unix_match("somefile.txt", "*") == True
assert unix_match("other.exe", "*") == True
assert unix_match("my.exe", "*.txt") == False
assert unix_match("log12.txt", "log?.txt") == False
assert unix_match("log12.txt", "log??.txt") == True
assert unix_match('txt', '????*') == False
assert unix_match('name.txt', 'name.???') == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
