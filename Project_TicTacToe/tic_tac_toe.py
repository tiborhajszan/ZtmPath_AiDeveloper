### Course: Zero to Mastery Academy | Prompt Engineering
### Section 5: Challenge - Build Your Second Game (Tic-Tac-Toe with AI opponent)

### imports
import sys
from typing import List, Tuple

### function initializing game board -----------------------------------------------------------------------------------
def initialize_board() -> List[List[str]]:
    """
    Initializes an empty 3x3 Tic-Tac-Toe board.

    Returns:
        list[list[str]]: empty game board, 3x3 list of strings, elements " "
    """

    ### creating and returning 3x3 matrix filled with spaces
    return [[" " for _ in range(3)] for _ in range(3)]

### function updating game board ---------------------------------------------------------------------------------------
def update_board(board:List[List[str]], position:Tuple[int,int], player:str='X') -> bool:
    """
    Updates the Tic-Tac-Toe board with the player's move.
    
    Args:
        board: list[list[str]], current state of game board, 3x3 list of strings, elements "X" | "O" | ""
        position: tuple[int,int], row and column indices of player move
        player: str, player mark ("X" | "O", default = "X")
    
    Returns:
        bool: True = successful move, False = invalid move
    """
    
    ### unpacking position tuple into row and column
    row,col = position

    ### checking whether position is within board
    if 0 <= row < 3 and 0 <= col < 3: # valid position
        pass
    else: # invalid position
        return False
    
    ### checking whether position is available (not already marked with 'X' or 'O')
    if board[row][col] == " ": # available position
        board[row][col] = player # placing player mark on board
        return True
    else: # occupied position
        return False

### function displaying game board -------------------------------------------------------------------------------------
def display_board(aBoard=list()) -> None:
    """
    Displays the current state of the Tic-Tac-Toe board.
    
    Args:
        aBoard: list[list[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "
    
    Returns:
        None: prints game board to console
    """

    ### asserting argument types and values
    if type(aBoard) is not list or len(aBoard) != 3 \
    or any(type(row) is not list or len(row) != 3 for row in aBoard) \
    or any(any(item not in ["X","O"," "] for item in row) for row in aBoard):
        print("\nInvalid game board: Restarting game...")
        aBoard = [[" " for _ in range(3)] for _ in range(3)]

    ### function main logic
    print() # printing separator line to console
    for index,row in enumerate(aBoard): # looping through each row of board
        print(f" {row[0]} | {row[1]} | {row[2]} ") # printing row to console
        if index < 2: print("---|---|---") # printing row divider to console
    
    ### returning
    return

board = initialize_board()
display_board(aBoard=board)
update_board(board=board, position=(1,1), player="X")
display_board(aBoard=board)
sys.exit()


def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move >= 0 and move < 9 and board[move] == ' ':
                board[move] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return ' ' not in board

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    current_player = 'X'

    while True:
        display_board(board)
        player_move(board, current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()
