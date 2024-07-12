"""
This is a tictactoe game
"""


def display_board(board, size=3):
    """
    Prints the Tic Tac Toe board to the terminal in a formatted way.
    """
    for idx in range(0, size):
        print(
            "".join(
                list(
                    map(
                        lambda i: f" {board[i + idx * size]}{' |' if i < size - 1 else ''}",
                        range(0, size),
                    )
                )
            )
        )
        if idx < size - 1:
            print(f"{'---|---|---'}")


def is_valid_move(board, position):
    """
    Checks if a move is valid (position is empty on the board).
    """
    return board[position] == " "


def make_move(board, player_sign, position):
    """
    Updates the board with the player's move at the specified position.
    """
    board[position] = player_sign


def check_has_won(board, player_sign):
    """
    Checks if a player has won the Tic Tac Toe game.
    """
    win_conditions = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    for condition in win_conditions:
        if all(board[i] == player_sign for i in condition):
            return True

    return False


def is_board_full(board):
    """
    Checks if all positions on the board are filled.
    """
    return all(x != " " for x in board)


def get_player_move(board, player):
    """
    Gets a valid move from the player, ensuring it's within the board and empty.
    """
    while True:
        try:
            position = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= position <= 8 and is_valid_move(board, position):
                return position
            print("Invalid move. Please choose an empty position (1-9).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def start_game():
    print("Welcome to our tic tac toe game")
    # Initialize board and players
    board = [" "] * 9
    player1_name = input("Enter Player 1 name: ")
    player2_name = input("Enter Player 2 name: ")
    current_player = player1_name  # Player 1 starts

    player_sign = {player1_name: "X", player2_name: "O"}

    print(f"Welcome, {player1_name} and {player2_name}! Let's play Tic Tac Toe!")

    while True:
        print(f"It's {current_player}'s turn having sign {player_sign[current_player]}")

        # Get player move and update board
        position = get_player_move(board, current_player)
        make_move(board, player_sign[current_player], position)

        print("\n")
        display_board(board)
        print("\n")

        # Check for win or draw
        if check_has_won(board, player_sign[current_player]):
            print(f"Congratulations, {current_player} wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # Switch turns
        current_player = (
            player2_name if current_player == player1_name else player1_name
        )


start_game()
