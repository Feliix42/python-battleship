''' TODO:
* Play with more ships (costumizable number?)
  -> different sizes?
'''

# Import randint function
from random import randint

# initialize boards
board = []
inv_board = []

max_turns = 15      # number of turns
ships = 5       # number of ships to be generated
hits = 0


# Definitions
def print_board(board):
    print("\n        1 2 3 4 5")
    print("      +-----------+")
    for row in range(len(board)):
        print("     {row}| {board} |".format(row=str(row + 1),
                                             board=" ".join(board[row])))
    print("      +-----------+\n")


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


def generate_ships(board1, board2, ships):
    i = 0
    while i < ships:
        ship_row = random_row(board2)
        ship_col = random_col(board2)
        if board1[ship_row][ship_col] != "S":
            board1[ship_row][ship_col] = "S"
            i += 1


def initialize_board():
    for x in range(5):
        board.append(["O"] * 5)
        inv_board.append([" "] * 5)

    generate_ships(inv_board, board, ships)


def main():
    print("\n             * Let's play Battleship! *")
    print("  You have", str(max_turns), "turns to sink my fleet consisting of",
          str(ships), "ships. Good luck!")
    print_board(board)

    for turn in range(max_turns):
        print("           =========== Turn: {tunn} =========== \n\
".format(turn=str(turn + 1)))

        while True:
            guess_row = int(input("   Guess a Row: ")) - 1
            guess_col = int(input("   Guess a Column: ")) - 1
            if (guess_row in range(5) and guess_col in range(5) and
               board[guess_row][guess_col] == "O"):
                break
            elif ((guess_row < 0 or guess_row > 4) or (guess_col < 0 or
                  guess_col > 4)):
                print("You picked coordinates outside the ocean! Try again!")
            else:
                print("You guessed that one already, captain!")

        if inv_board[guess_row][guess_col] == "S":
            print("Congratulations! You sunk my battleship!")
            board[guess_row][guess_col] = "H"
            hits += 1
            if hits == ships:
                break
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

            if turn == (max_turns - 1):
                print("Game Over")
        print_board(board)

    print("Let me show you my fleet:",)
    print_board(inv_board)

if __name__ == '__main__':
    main()
