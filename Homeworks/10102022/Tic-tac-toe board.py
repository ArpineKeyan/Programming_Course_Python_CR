#A Tic-tac-toe board can be represented be a 3×3 two-dimensional list,
# where zeroes stand for empty cells, ones stand for X’s and twos stand for O’s.
#(a) Write a function that is given such a list and randomly chooses a spot in which to place a 2.
#The spot chosen must currently be a 0 and a spot must be chosen.
#(b) Write a function that is given such a list and checks to see if someone has won.
#Return True if there is a winner and False otherwise.
import random

board = [0] + 4*[1] + 4*[2]    #[0, 1, 1, 1, 1, 2, 2, 2, 2]
random.shuffle(board)          #smth like [1, 2, 2, 2, 0, 1, 1, 1, 2]
board = [board[i:i+3] for i in range(0, 9, 3)]    #smth like [[1, 2, 2], [2, 0, 1], [1, 1, 2]]

print("The current board is: ", board)

def func1(given_board):
    """

    :param given_board: gets the board
    :return: returns the only empty place on board to fill it with "X"
    """
    for i in range(3):
        for j in range(3):
            if given_board[i][j] == 0:
                print(f"The spot on row {i + 1} and column {j + 1} is empty, you can fill it with 'X'.")
                given_board[i][j] = 2

    return given_board


def func2(given_board):
    """

    :param given_board: gets the board
    :return: returns True id there is winner
    """
    _winX = False                        # X player
    if given_board[0][0] == given_board[1][1] == given_board[2][2] == 2:           # Checking the diagnoal
        _winX = True
    if given_board[2][0] == given_board[1][1] == given_board[0][2] == 2:           # Checking the diagnoal
        _winX = True
    for i in range(3):
        if given_board[0][i] == given_board[1][i] == given_board[2][i] == 2:       #checking column
            _winX = True
            break
    for i in range(3):
        if given_board[i][0] == given_board[i][1] == given_board[i][2] == 2:       #checking row
            _winX = True
            break

    _winO = False              # O player
    if given_board[0][0] == given_board[1][1] == given_board[2][2] == 1:      # Checking the diagnoal
        _winO = True
    if given_board[2][0] == given_board[1][1] == given_board[0][2] == 1:     # Checking the diagnoal
        _winX = True
    for i in range(3):
        if given_board[0][i] == given_board[1][i] == given_board[2][i] == 1:
            _winO = True
            break
    for i in range(3):
        if given_board[i][0] == given_board[i][1] == given_board[i][2] == 1:
            _winO = True
            break
    if _winX:
        print("The X wins.")
    elif _winO:
        print("The 0 wins.")
    else:
        print("No winner.")



print("The final board is: ", func1(board))
new_board = func1(board)
print(func2(new_board))

#The current board is:  [[1, 1, 2], [2, 2, 1], [2, 1, 0]]
#The spot on row 3 and column 3 is empty, you can fill it with 'X'.
#The final board is:  [[1, 1, 2], [2, 2, 1], [2, 1, 2]]
#No winner.