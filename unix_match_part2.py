#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - Unix Match part 2
"""

def unix_match(filename: str, pattern: str) -> bool:
    """ Match pattern to filename """
    pos, bra, check, seq = 0, False, True, []
    for i in pattern:
        if len(filename) < pos:
            return False
        if bra:
            if i == "]":
                if not seq and filename[pos:pos+2+int(not check)] == ("[]" if check else "[!]"):
                    pos += 2+int(not check)
                elif (filename[pos] in seq) == check:
                    pos += 1
                else:
                    return False
                bra, check, seq = False, True, []
            elif i == "!":
                check = False
            else:
                seq.append(i)
        elif i == "[":
            bra = True
        else:
            if i == filename[pos]:
                pos += 1
            else:
                return False
    if bra or filename[pos:]:
        return False
    return True

assert unix_match('[!]check.txt', '[!]check.txt') == True
print("Example:")
print(unix_match("log1.txt", "log[1234567890].txt"))

# These "asserts" are used for self-checking
assert unix_match("log1.txt", "log[1234567890].txt") == True
assert unix_match("log1.txt", "log[!1].txt") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
