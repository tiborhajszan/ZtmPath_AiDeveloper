### Course: Zero to Mastery Academy | Prompt Engineering
### Section 5: Challenge - Build Your Second Game (Tic-Tac-Toe with AI opponent)

### imports
import os, sys
from typing import List, Tuple

########################################################################################################################
# Game Board Class                                                                                                     #
########################################################################################################################

class GameBoard:
    """
    Represents the Tic-Tac-Toe game board.
    
    Attributes:
    - _board : List[List[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "
    """
    
    ### constructor method #############################################################################################
    def __init__(self) -> None:
        """Initializes an empty 3x3 Tic-Tac-Toe game board."""

        ### creating 3x3 list of strings filled with spaces
        self._board: List[List[str]] = [[" " for _ in range(3)] for _ in range(3)]

    ### method for verifying game board ################################################################################
    def _verify(self) -> bool:
        """
        Verifies the integrity of the Tic-Tac-Toe game board by checking the following conditions:
        1. _board must be a list of size 3.
        2. Each element of _board must be a list of size 3.
        3. Each element of the sublists must be one of "X", "O", or " " (space).

        Returns:
        - bool: True = valid board, False = invalid board
        """
        
        ### method main logic ------------------------------------------------------------------------------------------

        # _board is not list of size 3 > returning false
        if not isinstance(self._board, list) or len(self._board) != 3: return False
        # _board elements are not lists of size 3 > returning false
        if not all(isinstance(row, list) and len(row) == 3 for row in self._board): return False
        # _board sublist elements are not "X"|"O"|" " > returning false
        if not all(item in ["X","O"," "] for row in self._board for item in row): return False
        # all checks passed > returning true
        return True

### function for verifying player move ---------------------------------------------------------------------------------
def verify_move(aBoard=list(), aMove=int()) -> bool:
    """
    Checks if player move is valid on the current Tic-Tac-Toe board.
    
    Args:
    - aBoard: List[List[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "
    - aMove: Tuple[int,int], row and column indexes of player move

    Returns:
    - bool: True = valid move, False = invalid move
    """

    ### invalid game board > returning false
    if not verify_board(aBoard=aBoard): return False
    
    ### aMove is not tuple of size 2 > returning false
    if not isinstance(aMove, tuple) or len(aMove) != 2: return False
    
    ### aMove elements are not int or outside range 0-2 > returning false
    if not all(isinstance(item, int) and 0 <= item < 3 for item in aMove): return False
    
    ### unpacking aMove tuple
    row,column = aMove
    
    ### selected cell is not available > returnin false
    if aBoard[row][column] != " ": return False

    ### all checks passed > returning true
    return True

### function for updating game board -----------------------------------------------------------------------------------
def update_board(aBoard=list(), aMove=tuple(), aMark=str()) -> bool:
    """
    Updates the Tic-Tac-Toe board with the player move.
    
    Args:
    - aBoard: List[List[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "
    - aMove: Tuple[int,int], row and column indices of player move
    - aMark: str, player mark "X"|"O"
    
    Returns:
    - bool: True = successful move, False = failed move
    """

    ### invalid game board and/or move > returning false
    if not verify_move(aBoard=aBoard, aMove=aMove): return False

    ### invalid mark > returning false
    if aMark not in ["X","O"]: return False
    
    ### unpacking move tuple > placing mark on game board > returning true
    row,column = aMove
    aBoard[row][column] = aMark
    return True

### function for displaying game board ---------------------------------------------------------------------------------
def display_board(aBoard=list()) -> bool:
    """
    Prints the current state of the Tic-Tac-Toe board to the console.
    
    Args:
    - aBoard: List[List[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "
    
    Returns:
    - bool: True = printing successful, False = printing failed
    """

    ### invalid game board > returning false
    if not verify_board(aBoard=aBoard): return False

    ### printing column numbers
    print("\n   | 1 | 2 | 3 ")

    ### printing rows and dividers
    for index,row in enumerate(aBoard):
        print("---|---|---|---")
        print(f" {index+1} | {row[0]} | {row[1]} | {row[2]} ")
    
    ### successful printing > returning true
    return True

board = initialize_board()
display_board(aBoard=board)
print(update_board(aBoard=board, aMove=(2,2), aMark="O"))
display_board(aBoard=board)
sys.exit()


########################################################################################################################
# Game Logic Module                                                                                                    #
########################################################################################################################

### function for finding winner ----------------------------------------------------------------------------------------
def check_winner(aBoard=list()) -> str:
    """Checks the Tic-Tac-Toe board for a winner.

    Args:
    - aBoard: List[List[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "

    Returns:
    - str: "X"|"O"|"" (no winner)
    """

    ### invalid game board > returning no winner
    if not verify_board(aBoard=aBoard): return ""

    ### defining win conditions
    win_conditions: List[List[str]] = [aBoard[row] for row in range(3)] # rows
    win_conditions.extend([list(column) for column in zip(*aBoard)]) # columns
    win_conditions.append([aBoard[index][index] for index in range(3)]) # backslash diagonal
    win_conditions.append([aBoard[index][2 - index] for index in range(3)]) # slash diagonal

    ### checking for and returning winner
    return next((line[0] for line in win_conditions if line[0] in ["X","O"] and line.count(line[0]) == 3), "")

### function for determining draw --------------------------------------------------------------------------------------
def is_draw(aBoard=list()) -> bool:
    """
    Determines if the current Tic-Tac-Toe game is a draw.
    The game is a draw if the board is full and no winner exists.

    Args:
    - aBoard: List[List[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "

    Returns:
    - bool: True = full board, False = moves available
    """

    ### invalid game board > returning false
    if not verify_board(aBoard=aBoard): return False
    
    ### full board > returning true | cells available > returning false
    return all(cell != " " for row in aBoard for cell in row)

########################################################################################################################
# Move Input Module                                                                                                    #
########################################################################################################################

### function for obtaining player move ---------------------------------------------------------------------------------
def get_player_move(aBoard=list()) -> Tuple[int,int]:
    """
    Obtains, validates, and returns a move from the player.

    Args:
    - aBoard: List[List[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "

    Returns:
    - Tuple[int,int]: row and column of player move
    """
    
    ### invalid game board > returning invalid player move
    if not verify_board(aBoard=aBoard): return -1,-1

    ### looping until valid player move is entered
    while True:
        # trying: prompting for move > parsing input > validating and returning move
        try:
            player_move = input("Enter your move (row,col): ").strip()
            row,column = map(lambda x: int(x)-1, player_move.split(","))
            if 0 <= row < 3 and 0 <= column < 3 and aBoard[row][column] == " ": return row,column
        # error: continuing loop
        except:
            pass

### minimax algorithm --------------------------------------------------------------------------------------------------
def minimax(aBoard=list(), aMaximizing=True) -> int:
    """
    Implements the Minimax Algorithm to determine the next AI move.
    
    Args:
    - aBoard: List[List[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "
    - aMaximizing: bool, True = maximizing score, False = minimizing score
    
    Returns:
    - int: score for the given board state
    """

    ### invalid game board > error handling
    if not verify_board(aBoard=aBoard): pass

    ### invalid maximizing flag > error handling
    if not isinstance(aMaximizing, bool): pass

    ### terminal conditions > returning score
    winner = check_winner(aBoard=aBoard) # looking for winner
    if winner == "O": return 1 # AI wins
    elif winner == "X": return -1 # player wins
    elif is_draw(aBoard=aBoard): return 0 # draw
    
    ### maximizing score
    if aMaximizing:
        best_score = -float("inf") # starting from minus infinity
        # looping through available moves
        for row,column in [(i,j) for i in range(3) for j in range(3) if aBoard[i][j] == " "]:
            aBoard[row][column] = "O" # pretending AI move
            last_score = minimax(aBoard=aBoard, aMaximizing=False) # calling minimax for player move
            aBoard[row][column] = " " # undoing AI move
            best_score = max(last_score, best_score) # updating best score
        return best_score # returning best score
    
    ### minimizing score
    best_score = float("inf") # starting from plus infinity
    # looping through available moves
    for row,column in [(i,j) for i in range(3) for j in range(3) if aBoard[i][j] == " "]:
        aBoard[row][column] = "X" # pretending player move
        last_score = minimax(aBoard=aBoard, aMaximizing=True) # calling minimax for AI move
        aBoard[row][column] = " " # undoing player move
        best_score = min(last_score, best_score) # updating best score
    return best_score # returning best score

### get ai move function -----------------------------------------------------------------------------------------------
from typing import List, Tuple

def get_ai_move(aBoard: List[List[str]]) -> Tuple[int, int]:
    """
    Determines the AI's next move using the Minimax algorithm.
    
    This function first verifies the board's integrity using `verify_board()`.
    Then, it computes the optimal move for the AI ("O") based on the current board state.
    The AI will attempt to minimize the player's chances of winning while maximizing its own.
    
    Args:
    - aBoard (List[List[str]]): The current state of the Tic-Tac-Toe board.
    
    Returns:
    - Tuple[int, int]: The (row, col) of the optimal move for the AI.
    """

    def available_moves(board: List[List[str]]) -> List[Tuple[int, int]]:
        """Returns a list of available moves as (row, col) tuples."""
        return 

    # Ensure the board is valid
    if not verify_board(aBoard):
        raise ValueError("Invalid board provided")

    # Initialize best variables
    best_move = (-1, -1)
    best_score = -float('inf')
    
    # Loop through available moves and apply Minimax
    for row, col in available_moves(aBoard):
        aBoard[row][col] = "O"
        score = minimax(aBoard, False)
        aBoard[row][col] = " "  # Undo move
        if score > best_score:
            best_score = score
            best_move = (row, col)
    
    return best_move

########################################################################################################################
# Game Utility Module                                                                                                  #
########################################################################################################################

### function for ending | restarting game ------------------------------------------------------------------------------
def restart_game(aMessage=str()) -> None:
    """
    Handles errors, and restarts or ends the Tic-Tac-Toe game.

    Args:
    - aMessage: str, optional error message to display
    """

    #>>> verifying and printing error message
    # aMessage not string > aMessage empty string
    if not isinstance(aMessage, str): aMessage = str()
    # aMessage valid string > adding separator lines
    if 0 < len(aMessage): aMessage = "\n" + aMessage + "\n"
    # printing to console
    print(aMessage)

    #>>> input loop
    # continuous looping until valid choice is entered
    while True:
        # prompting user and parsing input
        user_choice = input("Enter 'r' to restart game or 'q' to quit: ").strip().lower()
        # valid user choice > breaking loop
        if user_choice in ["r","q"]: break
        # invalid user choice > deleting prompt, continuing loop
        print("\033[1A", end="\x1b[2K")

    #>>> restarting game
    # user choice is restart
    if user_choice == 'r':
        # printing confirmation
        print("\nRestarting Game...")
        # restarting script
        os.system("cls")
        os.execl(sys.executable, "python", __file__)
        sys.exit()

    #>>> quitting game
    # terminating script, printing confirmation
    sys.exit("\nGame Over!")



########################################################################################################################

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
