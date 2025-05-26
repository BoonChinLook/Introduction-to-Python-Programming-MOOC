# Write your solution here

def print_sudoku(sudoku: list):
    for row in range(len(sudoku)): #rows 1-9
        for square in range(len(sudoku[row])): # squares in rows
            if sudoku[row][square] == 0:
                print("_", end=" ")
            else:
                print(sudoku[row][square], end=" ")

            if (square + 1) % 3 == 0 and square != len(sudoku[row]) - 1:
                print(" ", end="") # Print extra space after every 3rd column for extra spacings
        print()
        if (row + 1) % 3 == 0:  # Print a blank line after every 3rd row
            print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
#returns copy of orginal grid with new digits.
    copy_sudoku = []
    for row in sudoku:
        copy_sudoku.append(row[:])
    
    copy_sudoku[row_no][column_no] = number #gets the specific row to equal number

    return copy_sudoku

if __name__ == "__main__":
    s = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],]

    res = copy_and_add(s, 1, 1, 5)
    print("Original:")
    print_sudoku(s)
    print()
    print("Copy:")
    print_sudoku(res)