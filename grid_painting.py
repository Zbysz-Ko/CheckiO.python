#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - Grid Painting
"""

def grid_painting(cells: str) -> int:
    """ Calculate minimum steps of painting """
    grid = "".join([chr(i) if chr(i) in cells else " " for i in range(65,90)])
    strokes = []
    temp = set()
    result = 0

    # Colleting all possible brush strokes
    for pos in cells:
        y, x = divmod(ord(pos)-65, 5)
        end = grid.find(" ", x+y*5, 5+y*5) - y*5
        if end < 0:
            end = 5
        for i in range(x+1,end+1):
            strokes.append(set(grid[x+y*5:i+y*5]))
            for j in range(y+1,5):
                if " " in grid[x+j*5:i+j*5]:
                    break
                else:
                    strokes[-1].update(set(grid[x+j*5:i+j*5]))
    
    strokes.sort(reverse=True, key=len)

    # Count only the necessary strokes
    while strokes:
        stroke = strokes.pop()
        stroke_copy = stroke.copy()
        for st in strokes:
            stroke.difference_update(st)
            if not stroke:
                break
        else:
            if not stroke.issubset(temp):
                result += 1
                temp.update(stroke_copy)

    return result


print("Example:")
print(grid_painting('ABCFGHMRX'), 3)
print(grid_painting('GHLMNRS'), 2)
print(grid_painting('GHILNQRS'), 4)
print(grid_painting('ABCDEFGHIJKLMNOPQRSTUVWXY'), 1)
print(grid_painting('ACEGIKMOQSUWY'), 13)
print(grid_painting('ABDEFGHIJLMNPQRSTUVXY'), 5)
print(grid_painting('ABCDEFHJKLMNOPRTUVWXY'), 6)
print(grid_painting('BCDFGHIJKLMNOPQRSTVWX'), 2)

# These "asserts" are used for self-checking
assert grid_painting("ABCFGHMRX") == 3
assert grid_painting("GHLMNRS") == 2
assert grid_painting("GHILNQRS") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
