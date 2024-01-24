#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - R-mahjong I: break hand into sets
"""

def riichi_mahjong_sets(hand: list) -> list:
    """ Split tiles to one pair and 4 sets """

    result = []

    def find_sets(ts: list[str], pair: bool = False) -> bool:
        """ Find the matching combination through recursion """
        if ts[0] == ts[1] and not pair and (len(ts)==2 or find_sets(ts[2:], True)):         #pair
            result.append(ts[0]+ts[0][1])
            return True
        if ts[0] == ts[2] and (len(ts)==3 or find_sets(ts[3:], pair)):                      #pona
            result.append(ts[0]+ts[0][1]*2)
            return True
        if ts[0][0] in "pms" and \
            set(temp:=[ts[0][0]+str(int(ts[0][1])+i) for i in range(3)]).issubset(set(ts)): #chi
            for i in temp:
                ts.remove(i)
            if not ts or find_sets(ts, pair):
                result.append(temp[0]+temp[1][1]+temp[2][1])
                return True
        return False

    if find_sets(sorted(hand)):
        return sorted(result)
    return None

print("Example:")
print(
    riichi_mahjong_sets(
        [
            "m2",
            "s9",
            "p9",
            "dg",
            "s3",
            "s2",
            "m1",
            "s8",
            "dg",
            "p9",
            "dg",
            "s7",
            "s1",
            "m3",
        ]
    )
)

# These "asserts" are used for self-checking
assert riichi_mahjong_sets(
    ["m7", "s6", "p2", "m9", "s5", "wn", "s3", "p4", "s4", "p3", "s5", "m8", "s7", "wn"]
) == ["m789", "p234", "s345", "s567", "wnn"]
assert riichi_mahjong_sets(
    ["s7", "p4", "s6", "m8", "m4", "m3", "m8", "m8", "m2", "p6", "m4", "s5", "p5", "m4"]
) == ["m234", "m44", "m888", "p456", "s567"]
assert riichi_mahjong_sets(
    ["s8", "s7", "p2", "s4", "s9", "s3", "s5", "s1", "s6", "m5", "s2", "p2", "m3", "m4"]
) == ["m345", "p22", "s123", "s456", "s789"]
assert riichi_mahjong_sets(
    ["s8", "s9", "m1", "ws", "dr", "s7", "dr", "m9", "ws", "m9", "m2", "dr", "m3", "ws"]
) == ["drrr", "m123", "m99", "s789", "wsss"]

print("Now, what about 'Check solution'?")
