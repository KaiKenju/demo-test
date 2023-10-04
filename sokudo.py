""" Algorithms for sokudo
 1. Find the next empty(puzzle)
 2. Check it is valid or not
 3. Solve the sokudo by guessing

"""
#----------------------------------------------------------------
"""
1. Find the next empty(puzzle)
- Interate through each row r in the puzzle
- Interate through each column  c in the puzzle
==> Ìf puzzle[r][c] = -1: (mean the value does solve)
        return the coordinates (r,c)
==> if no empty cell is found :
        return (None, None)

Check if guess exits in the current row: puzzle[row]
    return false
Check if guess exits in the current column: puzzle[column]
    return false
If no empty cell is found:
    return (None, None)

2. is_valid

Check if guess exits in puzzle[row]:
    return false
Check if guess exits in puzzle[i][column]: (for each row i in the puzzle)
    return false

=> 3x3 Square based on the current row and col
Iterate through each cell (r,c) in 3x3 square (matrix)

- if puzzle[r][c] = guess  (duplicate results ==> false)
    return false
- if guess is valid
    return true

3. Solve sudoku
Find the next empty cell (from the number (1) above)
- if no empty cells left (i.e row is None)
        return true  ==> the puzzle is solved
- if 
"""

from pprint import pprint
def find_next_empty(puzzle):
    #find the next col, row that's not filled yet ==> mean -1 (-1 = hidden value)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
            
    return None, None

def is_valid(puzzle, guess, row, col):
    #let's start with row
    row_val = puzzle[row]
    if guess in row_val:
        return False
    
    #The col_vals contains value of column
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False
    
    # -----Check guess in square or not ---
    row_start = (row // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    col_start = (col // 3) * 3
    
    # Load each element in square to chẹck
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True
    # -----Check guess in square or not --------------------------

def solve_sudoku(puzzle):
    
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    if row is None:  # this is true if our find_next_empty function returns None, None
        return True 
    
    for guess in range(1, 10): 
        # step 2: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            # step 4: then we recursively call our solver!
            if solve_sudoku(puzzle):
                return True
        
        # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
