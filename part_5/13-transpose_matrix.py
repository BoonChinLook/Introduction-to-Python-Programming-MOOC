# Write your solution here

def transpose(matrix: list):
#matrix is a 2-d array
    temp = []
    for row in range(len(matrix)):
        for square in range(row, len(matrix)):
           temp = matrix[row][square]
           matrix[row][square] = matrix[square][row]
           matrix[square][row] = temp
        
    print(matrix)
        

if __name__ == "__main__":
    transpose([[1, 2], [1, 2]])
