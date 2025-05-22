# Write your solution here
#"sudoku" list takes in a 2-D array
#row_no represents single value
#Question asks function to return True or False for rows
#filled correctly ; numbers 1-9

def row_correct(sudoku: list, row_no: int):
    checker = []
    for square in sudoku[row_no]:
        if square > 0:
            checker.append(square)
    for item in checker:
        if checker.count(item) > 1:
            return False
    return True

            
if __name__ == "__main__":
    
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0], #row 0 in test case
  [2, 0, 0, 2, 5, 0, 7, 0, 0], # row 1 in test case
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))


        
