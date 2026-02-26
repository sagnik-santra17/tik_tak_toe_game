print()
print("------------------------")
print("Welcome to Tick-Tack-Toe")
print("------------------------")
print()

def player_pick():
    while True:
        pick = input("Choose your pick 'X' or 'O': ").upper()

        if pick in ("X", "O"):
            print(f"Player 1 chose {pick}")
            print(f"Player 2 chose {'O' if pick == 'X' else 'X'}")
            return pick
        
        else:
            print("Please choose between 'X' or 'O'")

player1_mark = player_pick()
player2_mark = "O" if player1_mark == "X" else "X"

def start_game(board):

    print(board[7] + " " + "|" + " " + board[8] + " " + "|" + " " + board[9])
    print("---------")
    print(board[4] + " " + "|" + " " + board[5] + " " + "|" + " " + board[6])
    print("---------")
    print(board[1] + " " + "|" + " " + board[2] + " " + "|" + " " + board[3])

print()

def win_check(board, mark):
    return(
        #Rows
        board[1] == board[2] == board[3] == mark or
        board[4] == board[5] == board[6] == mark or
        board[7] == board[8] == board[9] == mark or

        #Columns
        board[1] == board[4] == board[7] == mark or
        board[2] == board[5] == board[8] == mark or
        board[3] == board[6] == board[9] == mark or

        #Diagonals
        board[3] == board[5] == board[7] == mark or
        board[1] == board[5] == board[9] == mark
    )

def choose_position():
    index = [" "] + ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    start_game(index)
    current_player = player1_mark

    for _ in range(9):
        while True:
            print()
            position = input(f"{current_player}: Choose your index between 1-9: ")
            print()
            if not position.isdigit():
                print(f"{current_player}: Please choose an index between 1-9")
                continue

            position = int(position)

            if position not in range(1,10):
                print(f"{current_player}: Your index is out of range! Please choose an index between 1-9")
                continue

            if index[position] in ("X", "O"):
                print(f"{current_player}: This index is already taken! Please pick another one.")
                continue
            else:
                index[position] = current_player
                break

        start_game(index)

        if win_check(index, current_player):
            print()
            print(f"{current_player} has own the game!!!")
            print()
            return

        current_player = player2_mark if current_player == player1_mark else player1_mark

    print("It's a draw")
        
def replay():
    while True:
        choice = input("Do you want to replay? Choose 'Y'/'N': ").upper()
        print()

        if choice in ("Y", "N"):
            return choice == "Y"
        else:
            print("Please choose between: 'Y'/'N'")

while True:
    choose_position()
    
    if not replay():
        print("Thanks for playing!!!") 
        break