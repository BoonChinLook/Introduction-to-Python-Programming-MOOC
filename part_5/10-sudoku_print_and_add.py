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
       
    

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    for row in sudoku: # goes through rows
        for square in row: # goes through items in rows
            sudoku[row_no][column_no] = number #gets the specific row to equal number



if __name__ == "__main__":

    s = [
  [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
  [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
  [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
  [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
  [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
  [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
  [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
  [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],]
    print_sudoku(s)