#!/usr/bin/env python3

# Learning Python
#
# Task from Checkio.org - Open Labyrinth
# In my version function 'checkio' is trying to find all ways.
# There is also something for break iteration if in labyrinth
# is too much open spaces.

from typing import List

def checkio(maze_map: List[List[int]]) -> str:
    """Function trying to find path to goal.
    """
    control = {(0,1): "E", (1,0): "S", (0,-1): "W", (-1,0): "N"}
    control2 = {(0,-1): "W", (1,0): "S", (0,1): "E", (-1,0): "N"}
    co = [(1, 1)]
    goal = (10, 10)
    stack = [0]
    result = []
    idx = 0

    def co2path(res: iter) -> str:
        """For convert movement data
        from (y, x) to NESW (North/South, West/East)"""
        
        path = ""
        for i in range(1, len(res)):
            path += control.get( (res[i][0]-res[i-1][0], res[i][1]-res[i-1][1]) )
        return path

    # Do until all ways will found
    while True:

        # If checked all direction from one point,
        # step back and check rest open directions
        while idx == 4:
            co.pop(-1)
            idx = stack.pop(-1)

        # Break if you check all corners
        if len(stack) == 0:
            break

        # Get next direction to check
        i = list(control)[idx]

        # Check if next move is the place, where you have already been
        # If Yes, try next direction
        if len(co)>0 and (co[-1][0]+i[0], co[-1][1]+i[1]) in co:
            idx += 1
            continue

        # Check if next move is path (remember and go next) or wall (try next direction)
        if maze_map[co[-1][0]+i[0]][co[-1][1]+i[1]] == 0:
            stack.append(idx+1)
            co.append((co[-1][0]+i[0], co[-1][1]+i[1]))
            idx = 0
            # If reach goal, remember path, go one step back and try to find another path
            if goal == co[-1]:
                result.append(co.copy())
                co.pop(-1)
                idx = stack.pop(-1)
        else:
            idx += 1

        # Fuse! 55 - longest way in 10x10 matrix (without edges)
        if len(stack)>55:
            if len(result) > 0:
                break
            elif control != control2:
                control = control2
                co = [(1, 1)]
                stack = [0]
                idx = 0


    if result == []:
        raise Exception("There is not way to reach the goal!")

    result.sort(key=len)

    return(co2path(result[0]))

if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
                   [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
