def find_next_index(i, j, square):
    if (j+1 < len(square)) and (square[i][j+1] == 0):
        j += 1
        # print 'right'
    elif (i-1 >= 0) and (square[i-1][j] == 0):
        i -= 1
        # print 'up'
    elif (j-1 >= 0) and (square[i][j-1] == 0):
        j -= 1
        # print 'left'
    else:
        i += 1
        #  print 'down'
    return i, j


def sum_of_adjacent_cells(i, j, square):
    adjacent_cells = square[max(i-1,0):min(i+1,len(square)-1)+1, max(j-1,0):min(j+1,len(square)-1)+1]
    # print adjacent_cells
    return adjacent_cells.sum()


input = 361527
k = 1
i = j = 0
current_value = 1
square_size = 1
square = [[current_value]]

import numpy as np

while input >= current_value:
    k += 1
    if k > square_size*square_size:
        # increase matrix
        square_size += 2
        old_square = square
        square = np.zeros(shape=(square_size, square_size),  dtype=np.int)
        square[1:square_size-1,1:square_size-1] = old_square
        j += 1
        i += 1
    i, j = find_next_index(i, j, square)
    square[i][j] = sum_of_adjacent_cells(i, j, square)
    current_value = square[i][j]
    # print current_value
    # print square

print current_value