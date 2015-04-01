''' TODO:
* Stop punish the player for his dumbness
  (no punishment for guessing wrong coordinates)
* Play with more ships (costumizable number?)
  -> work with the inv_board
'''

# Import randint function
from random import randint

# Definitions
def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


# initialize boards
board = []
inv_board = []

for x in range(5):
    board.append(["O"] * 5)
    inv_board.append(["O"] * 5)

ship_row = random_row(board)
ship_col = random_col(board)
inv_board[ship_row][ship_col] = "S"

print("Let's play Battleship!")
print_board(board)
print(ship_row)             # TODO - Debug only!
print(ship_col)             # TODO - Debug only!
print_board(inv_board)      # TODO - Debug only!


turn = 0
for turn in range(4):
    print("Turn: ", turn + 1)
    guess_row = int(input("Guess a Row: "))
    guess_col = int(input("Guess a Column: "))

    if inv_board[guess_row][guess_col] == "S":
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or  guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

        if turn == 3:
            print("Game Over")
    print_board(board)
