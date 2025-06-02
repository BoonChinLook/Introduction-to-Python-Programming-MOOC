# Write your solution here
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

    
    print(checker)

if __name__ == "__main__":
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))