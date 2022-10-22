# Write a function that is given a 9 × 9 potentially solved Sudoku and returns True if it is solved correctly and False
# if there is a mistake. The Sudoku is correctly solved if there are no repeated numbers in any row or any column
# or in any of the nine “blocks.”

"""
In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row,
and each of the nine 3 × 3 subgrids that compose the grid contain all of the digits from 1 to 9.
"""
import random

sudoku_random_board = [[random.randint(1, 9) for row in range(9)] for column in range(9)]
sudoku_solved_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7],
                       [8, 5, 9, 7, 6, 1, 4, 2, 3], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6],
                       [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9]]


# row values check
def row_check(matrix):
    flag = True
    for item in matrix:
        for i in item:
            if item.count(i) > 1:
                flag = False
    return flag


# transpose of matrix will help with column check
def matrix_transpose(matrix):
    new_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[i][j] = matrix[j][i]
    return new_matrix


# column values check
def col_check(matrix):
    transposed_matrix = matrix_transpose(matrix)
    return row_check(transposed_matrix)


# block values check
def block_check(matrix):
    flag = True
    for c in range(0, 9, 3):
        for k in range(0, 9, 3):
            minor = [[matrix[n][m] for m in range(k, k + 3)] for n in range(c, c + 3)]
            for item in minor:
                for i in item:
                    if item.count(i) > 1:
                        flag = False
    return flag

matrix = sudoku_solved_board
#matrix = sudoku_random_board
if col_check(matrix) and row_check(matrix) and block_check(matrix):
    print(f"Sudoku { matrix } \n is solved.")
else:
    print("Not solved")


#print("Column check solved_board: ", col_check(matrix))
#print("Row check solved_board: ", row_check(matrix))
#print("Block check solved_board: ", block_check(matrix))
#print("Column check random_board: ", col_check(sudoku_random_board))
#print("Row check random_board: ", row_check(sudoku_random_board))
#print("Block check random_board: ", block_check(sudoku_random_board))
