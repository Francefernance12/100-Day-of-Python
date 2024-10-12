from random import choice

board = [' ' for _ in range(9)]


def game_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_win():
    game_board()
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            print(f"Player {board[combination[0]]} wins!")
            return False

    if ' ' not in board:
        print("It's a draw!")
        return False

    return True


def add_position(position, player):
    if board[position] == ' ':
        board[position] = player
    else:
        print("Position occupied, please try again")
        return False
    return True


def ai_move_position():
    available_positions = [i for i, spot in enumerate(board) if spot == ' ']
    return choice(available_positions) if available_positions else None


def start_game():
    print("Starting game")
    input("Press enter to play")
    print("Player 1: X")
    print("Player 2: O")
    print("0 to 8 represents the position in the game board starting from top to bottom, left to right")
    print("""
     0 | 1 | 2 
     --+---+--
     3 | 4 | 5 
     --+---+--
     6 | 7 | 8
    """)

    try:
        game_mode = int(input("Type 0 to play with AI, type 1 to play with human player: "))
    except ValueError:
        print("Invalid input. Game mode should be 0 or 1.")
        return

    current_player = 'X'
    game_on = True

    while game_on:
        try:
            if game_mode == 0:  # AI game mode
                if current_player == 'X':
                    p1_position = int(input("Player X, type in a number from 0 to 8: "))
                    if 0 <= p1_position <= 8:
                        if add_position(p1_position, 'X'):
                            game_on = check_win()
                            current_player = 'O'
                    else:
                        print("Invalid input. Please enter a number between 0 and 8.")
                        continue
                else:
                    ai_position = ai_move_position()
                    if ai_position is not None:
                        print(f"AI chooses position {ai_position}")
                        add_position(ai_position, 'O')
                        game_on = check_win()
                        current_player = 'X'
                    else:
                        print("No available positions left.")
                        game_on = False

            elif game_mode == 1:  # Human vs Human
                if current_player == 'X':
                    p1_position = int(input("Player X, type in a number from 0 to 8: "))
                    if 0 <= p1_position <= 8:
                        if add_position(p1_position, 'X'):
                            game_on = check_win()
                            current_player = 'O'
                    else:
                        print("Invalid input. Please enter a number between 0 and 8.")
                        continue
                else:
                    p2_position = int(input("Player O, type in a number from 0 to 8: "))
                    if 0 <= p2_position <= 8:
                        if add_position(p2_position, 'O'):
                            game_on = check_win()
                            current_player = 'X'
                    else:
                        print("Invalid input. Please enter a number between 0 and 8.")
                        continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")


start_game()
