#!/usr/bin/env python3

# Learning Python
#
# Task from Checkio.org - Life Counter

def life_counter(state: tuple, tick_n: int) -> int:
    '''Function implements "The Game of Life"
    
    state - initial pattern
    tick_n - number of steps in time
    result - number of live cell for the Nth steps
    '''

    # Array of adjacent cell positions
    movement = ((-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1))
    
    # Change input tuples to lists
    if isinstance(state, tuple):
        state = list(state)
    else:
        state = [[state]]
    if isinstance(state[0], tuple):
        for _ in range(len(state)):
            state[_] = list(state[_])
    else:
        state = [state]
    
    def check_state(state_check):
        '''
        If there are live cells in the first or last horizontal or vertical 
        line, the function adds a line of dead cells in that direction.
        If there are redundant lines of dead cells (more than one) in a given 
        direction, the function reduces the number lines with dead cells to one.
        '''

        # Checking first horizontal line
        if 1 in state_check[0]:
            state_check.insert(0, list(0 for _ in range(len(state_check[0]))))
        else:
            # Fuse if there aren't live cells
            if len(state_check) == 1:
                return [[[0]]]
            while 1 not in state_check[1]:
                state_check.pop(0)
                # Fuse if there aren't live cells
                if len(state_check) == 1:
                    return [[[0]]]
       
        # Checking last horizontal line
        if 1 in state_check[-1]:
            state_check.append(list(0 for _ in range(len(state_check[0]))))
        else:
            while 1 not in state_check[-2]:
                state_check.pop(-1)

        # Checking first vertical line
        if 1 in [state_check[_][0] for _ in range(len(state_check))]:
            for i in range(len(state_check)):
                state_check[i].insert(0, 0)
        else:
            while 1 not in [state_check[_][1] for _ in range(len(state_check))]:
                for i in range(len(state_check)):
                    state_check[i].pop(0)

        # Checking last vertical line
        if 1 in [state_check[_][-1] for _ in range(len(state_check))]:
            for i in range(len(state_check)):
                state_check[i].append(0)
        else:
            while 1 not in [state_check[_][-2] for _ in range(len(state_check))]:
                for i in range(len(state_check)):
                    state_check[i].pop(-1)
 
        return state_check
    
    def life(state_in):
        '''
        Function implements life transitions to the pattern

        Live cells: <2 or >3 live adjacent cells = cell die
        Dead cells: =3 live adjacent cells = cell reborn
        '''
        
        # Reducing or increasing the pattern
        state_in = check_state(state_in)

        # Getting size of the pattern
        len_x = len(state_in[0])
        len_y = len(state_in)

        # Init pattern for the step
        state_out = []

        # Iterate through each cell in the pattern and check whether or not its state is changed.
        for y in range(len_y):
            state_out.append([])
            for x in range(len_x):
                counter = 0
                for m in movement:
                    dx = x + m[0]
                    dy = y + m[1]
                    if dx < 0 or dy < 0 or dx == len_x or dy == len_y or state_in[dy][dx] == 0:
                        continue
                    counter += 1
                if (state_in[y][x] and counter in (2, 3)) or (not state_in[y][x] and counter == 3):
                    state_out[y].append(1)
                else:
                    state_out[y].append(0)
        
        return state_out

    # Perform a set number of steps
    for i in range(tick_n):
        state = life(state)
        # Check if life ends earlier
        if state == [[0]]:
            break
    state = check_state(state)

    # Calculate number of life cells
    result = 0
    for i in state:
        result += i.count(1)

    return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 4) == 15, "Example"
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 15) == 14, "Little later"
    assert life_counter(((0, 1, 0),
                         (0, 0, 1),
                         (1, 1, 1)), 50) == 5, "Glider"
    assert life_counter(((1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1),
                         (0, 0, 0, 0, 0),
                         (1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1)), 100) == 16, "Stones"
