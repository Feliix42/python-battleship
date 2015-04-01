''' TODO:
* Play with more ships (costumizable number?)
  -> different sizes?
'''

# Import randint function
from random import randint

# Definitions
def print_board(board):
    print("\n        1 2 3 4 5")
    print("      +-----------+")
    for row in range(len(board)):
        print("     " + str(row + 1) + "| " + " ".join(board[row]) + " |")
    print("      +-----------+\n")

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

max_turns = 15      # number of turns

def generate_ships(board1, board2):
    ships = 5
    ship_row = random_row(board)
    ship_col = random_col(board)
    inv_board[ship_row][ship_col] = "S"

# initialize boards
board = []
inv_board = []

for x in range(5):
    board.append(["O"] * 5)
    inv_board.append([" "] * 5)

generate_ships(inv_board, board)


print("\n             * Let's play Battleship! *")
print_board(board)

turn = 0
for turn in range(max_turns):
    print("           =========== Turn: %s =========== \n" % str(turn + 1))

    while True:
        guess_row = int(input("   Guess a Row: ")) - 1
        guess_col = int(input("   Guess a Column: ")) - 1
        if guess_row in range(5) and guess_col in range(5) and board[guess_row][guess_col] == "O":
            break
        elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or  guess_col > 4):
            print("You picked coordinates outside the ocean! Try again!")
        else:
            print("You guessed that one already, captain!")

    if inv_board[guess_row][guess_col] == "S":
        print("Congratulations! You sunk my battleship!")
        break
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"

        if turn == (max_turns - 1):
            print("Game Over")
    print_board(board)

print("Let me show you my fleet:",)
print_board(inv_board)
