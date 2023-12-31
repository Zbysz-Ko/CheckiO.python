#!/usr/bin/env python3

"""Learning Python

Task from Checkio.org - Chess Knight
"""

def chess_knight(start: str, moves: int) -> list[str]:
    ''' Function can find all of the chessboard cells 
        to which the Knight can move 
        at not more than maximum amount of moves
    '''
    movement = ((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2))
    board = {"h" : "abcdefgh",
             "v" : "87654321"}
    start = (board["h"].find(start[0]), board["v"].find(start[1]))
    result = []
    counter = 0
    deep = list(0 for _ in range(moves))

    while moves > 0:
        for dm in movement:
            pos = tuple(map(sum, zip(start, dm)))
            if( -1 < pos[0] < 8 and -1 < pos[1] < 8 and pos not in result):
                result.append(pos)
                deep[moves-1] += 1
        if counter == 0 or deep[moves] == 0:
            moves -= 1
        start = result[counter]
        counter += 1
        deep[moves] -= 1
        if len(result) == 64:
            break

    return sorted([board["h"][i] + board["v"][j] for i, j in result])


if __name__ == "__main__":
    print("Example:")
    print(chess_knight("a1", 1))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight("a1", 1) == ["b3", "c2"]
    assert chess_knight("h8", 2) == [
        "d6",
        "d8",
        "e5",
        "e7",
        "f4",
        "f7",
        "f8",
        "g5",
        "g6",
        "h4",
        "h6",
        "h8",
    ]
