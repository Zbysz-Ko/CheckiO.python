#!/usr/bin/env python3

# Learning Python
#
# Task from Checkio.org - Chess Knight

def chess_knight(start: str, moves: int) -> list[str]:
    '''
    Function can find all of the chessboard cells to which the Knight can move 
    at not more than maximum amount of moves
    '''
    # Possible moves of Knight
    movement = ((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2))
    
    # Chessboard
    board = {"h" : "abcdefgh", "v" : "87654321"}
    
    # Convert start position: "a1" = (0, 7); "g8" = (7, 0)
    start = (board["h"].find(start[0]), board["v"].find(start[1]))
    
    # Array of cells to which the Knight can move
    result = []

    # Counter for sequentially checking the next possible moves from the items 
    # stored in the "Result" table.
    counter = 0
    
    # Create array where each index is a counter for the movements left 
    # to be checked for each depth of movement.
    deep = list(0 for _ in range(moves))

    while moves > 0:
        
        # Check all possible moves from current position
        for dm in movement:
            # Sum of the two tuples
            pos = tuple(map(sum, zip(start, dm)))
            # If move is possible and not in result array, add it and increment 
            # counter for current depth of move
            if( -1 < pos[0] < 8 and -1 < pos[1] < 8 and pos not in result):
                result.append(pos)
                deep[moves-1] += 1
        
        # When all the movements of a given depth of movement have been checked, 
        # the next depth of movement is started to count down.
        if counter == 0 or deep[moves] == 0:
            moves -= 1
        # Get next position to check next moves and increment the counter
        # in result / decrement in current depth of moves
        start = result[counter]
        counter += 1
        deep[moves] -= 1

        # The chessboard has 64 squares, so let's not check any more moves 
        # when we've already got them all on the result array.
        if len(result) == 64:
            break
    
    # Convert from (0, 7) to "a1"
    result = sorted([board["h"][i] + board["v"][j] for i, j in result])
    return result


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
