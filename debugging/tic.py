#!/usr/bin/python3
def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.

    Parameters:
    board (list of list of str): A 3x3 list representing the current game board.

    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner in the current board state.

    Parameters:
    board (list of list of str): A 3x3 list representing the current game board.

    Returns:
    bool: True if a winning condition is met, otherwise False.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Checks if the board is completely filled.

    Parameters:
    board (list of list of str): A 3x3 list representing the current game board.

    Returns:
    bool: True if the board is full, otherwise False.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play the Tic-Tac-Toe game. Manages game flow, input handling, 
    and win/tie conditions.

    Parameters:
    None

    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize empty board
    player = "X"  # Start with player X

    while True:
        print_board(board)
        
        # Get input from the current player
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")
            continue

        # Check if the inputs are within the valid range
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid coordinates! Please enter numbers between 0 and 2.")
            continue

        # Check if the chosen cell is empty
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place the player's mark on the board
        board[row][col] = player

        # Check if the current player wins
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie! The board is full.")
            break

        # Switch to the next player
        player = "O" if player == "X" else "X"

# Run the game
tic_tac_toe()
