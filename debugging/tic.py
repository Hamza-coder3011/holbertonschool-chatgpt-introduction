#!/usr/bin/python3

def print_board(board):
    """Display the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """Check if the board is full (for draw)."""
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(player):
    """Prompt the user until valid coordinates are entered."""
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Coordinates must be 0, 1, or 2. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def tic_tac_toe():
    """Main game loop for Tic Tac Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_valid_input(current_player)

        if board[row][col] == " ":
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken. Try again.")

tic_tac_toe()
