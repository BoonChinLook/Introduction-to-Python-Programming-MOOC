# Write your solution here
def row_correct(sudoku: list, row_no: int):
    checker = []
    for square in sudoku[row_no]:
        if square > 0:
            checker.append(square)
    for item in checker:
        if checker.count(item) > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    checker = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in checker:
            return False
        checker.append(row[column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    checker = []
    row_no = row_no - 1
    for rows in range(3): 
        row_no += 1
        for cols in range(3):
            if sudoku[row_no][column_no] in checker and sudoku[row_no][column_no] > 0:
                return False
            checker.append(sudoku[row_no][column_no])
            column_no += 1
        column_no -= 3
    return True

def sudoku_grid_correct(sudoku:list):
    for row_index in range(0, len(sudoku), 3):
        for column_no in range(0, len(sudoku), 3):
            if block_correct(sudoku, row_index, column_no) == False:
                return False

    for column_no in range(len(sudoku)):
        if column_correct(sudoku, column_no) == False:
            return False
       
    for row_index in range(len(sudoku)):
        if  row_correct(sudoku, row_index) == False:
            return False
  
    return True
            


if __name__ == "__main__":
    sudoku = [
  [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
  [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
  [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
  [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
  [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
  [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
  [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
  [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
  [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],]
    
    print(sudoku_grid_correct(sudoku))