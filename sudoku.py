def find_next_empty(puzzle):
    # find next empty square --> represent with 0
    # return coordinates
    # (None, None) is if the board is fully filled
    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    
    return None, None

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row, col of the puzzle is a valid guess
    # returns False if it's not
    
    # check the rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # check the columns
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # check the 3x3 square matrix
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    # if we haven't returned False, it's a valid guess
    return True

def solve_sudoku(puzzle):
    # our puzzle is a list of lists where the inner lists are rows
    # return if there is a solution
    # mutate puzzle to be the solution if solvable
    
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)
    
    # step 1.1: if there's nowhere left, we're done because we only allowed valid input
    if row is None:
        return True
    
    # step 2: if there's a place to put a number, then make a guess 1-9
    for guess in range(1, 10):
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place the guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
            
        # step 5: if not valid OR if our guess doesn't solve the puzzle
        # backtrack and try a new number
        puzzle[row][col] = 0 # reset guess
            
    # step 6: if none of the numbers that we try work, then this puzzle is unsolvable
    return False

puzzle = [ # create an empty puzzle board to fill
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print() # gives a one line margin from the text at the top
for r in range(9): # fill the board with numbers
    # gets and stores rows as 9-digit numbers
    row_num = input("Enter a 9-digit number for the row (0 is empty): ")
    for i in range(9): # iterates through the number and stores it in the puzzle
        puzzle[r] = [int(x) for x in str(row_num)] # turns the variable row_num into an array
            
    print("------------------------------------------------------------") # indicates row end

solve_sudoku(puzzle)

print() # seperates it from the input area
for r in range(9): # prints the puzzle nicely
    for c in range(9):
        print(puzzle[r][c], end=' ') # prints the numbers
        if (c + 1) % 3 == 0 and c != 8: # adds a space every 3 numbers in a row for neatness
            print('  ', end='')
    print() # adds a space between rows
    if (r + 1) % 3 == 0 and r != 8:
        print() # adds a space ever 3 rows to make 3x3 grids visible
print() # adds a margin between end and start of program
input() # adds a space from the end of program and stops from closing