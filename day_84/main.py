from random import choice

board = [' ' for _ in range(9)]


def game_board():
    # Print the board in a 3x3 grid format
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_win():
    # Create board
    game_board()

    # Define all possible winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    # Check if any winning combination is found
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            print(f"Player {board[combination[0]]} wins!")
            return False

    # Check if the board is full (no spaces left)
    if ' ' not in board:
        print("It's a draw!")
        return False

    return True


def add_position(position, player):
    if board[position] == ' ':
        board[position] = player
    else:
        print("Position occupied, please try again")


def ai_move_position():
    # AI chooses a random position from the available ones
    available_positions = [i for i, spot in enumerate(board) if spot == ' ']
    return choice(available_positions) if available_positions else None


def start_game():
    print("Starting game")
    input("Press enter to play")
    print("Player 1: X")
    print("Player 2: O")
    print("0 to 8 represents the position in the game board starting from top to bottom, left to right")
    print("e.g. 0 is the top left, 5 is the middle right, 6 is the bottom left")
    print("""
     0 | 1 | 2 
     --+---+--
     3 | 4 | 5 
     --+---+--
     6 | 7 | 8
    """)

    game_mode = int(input("Type 0 to play with AI, type 1 to play with human player then press enter: "))
    current_player = 'X'  # Player X always starts
    game_on = True

    while game_on:
        # Player X or O's turn
        if game_mode == 0:  # AI game mode
            if current_player == 'X':
                # Player X chooses a position
                p1_position = int(input("Player X type in a number from 0 to 8 then press enter: "))
                if 0 <= p1_position <= 8:
                    add_position(position=p1_position, player='X')
                    game_on = check_win()
                    current_player = 'O'  # Switch to AI
                else:
                    print("Invalid input, please try again")
                    continue
            else:
                # AI (Player O) turn
                ai_position = ai_move_position()
                if ai_position is not None:
                    print(f"AI chooses position {ai_position}")
                    add_position(position=ai_position, player='O')
                    game_on = check_win()
                    current_player = 'X'  # Switch back to Player X
                else:
                    print("No available positions left.")
                    game_on = False

        elif game_mode == 1:  # Human vs Human
            if current_player == 'X':
                # Player X's turn
                p1_position = int(input("Player X type in a number from 0 to 8 then press enter: "))
                if 0 <= p1_position <= 8:
                    add_position(position=p1_position, player='X')
                    game_on = check_win()
                    current_player = 'O'  # Switch to Player O
                else:
                    print("Invalid input, please try again")
                    continue
            else:
                # Player O's turn
                p2_position = int(input("Player O type in a number from 0 to 8 then press enter: "))
                if 0 <= p2_position <= 8:
                    add_position(position=p2_position, player='O')
                    game_on = check_win()
                    current_player = 'X'  # Switch back to Player X
                else:
                    print("Invalid input, please try again")
                    continue


start_game()
