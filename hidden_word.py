#!/usr/bin/env python3

"""Learning Python

Task from Checkio.org - Hidden word
"""

def checkio(text, word):
    """ Find start and end position
        (horizontally or vertically)
        of 'word' in 'text'"""
    text = text.replace(" ", "").lower().splitlines()
    for row, t in enumerate(text):
        for col in [i for i, _ in enumerate(t) if _ == word[0]]:            # Find occurrences of the first letter in a line
            if len(t) >= col+len(word) and t[col:col+len(word)] == word:    # Check "word" horizontally
                return [row+1, col+1, row+1, col+len(word)]
            if len(text) >= row+len(word) \
                and "".join([text[row+_][col] for _ in range(len(word)) \
                             if len(text[row+_]) > col]) == word:           # Check "word" vertically
                return [row+1, col+1, row+len(word), col+1]
    return None


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert (
        checkio(
            """DREAMING of apples on a wall,
And amidreng often, dear,
I dreamed that, if I counted all,
-How many would appear?""",
            "ten",
        )
        == [2, 14, 2, 16]
    )
    assert (
        checkio(
            """He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""",
            "noir",
        )
        == [4, 16, 7, 16]
    )
print("Coding complete? Click 'Check' to earn cool rewards!")
