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

        ### method main logic ------------------------------------------------------------------------------------------

        # creating empty game board as 3x3 list of strings filled with spaces
        self._board: List[List[str]] = [[" " for _ in range(3)] for _ in range(3)]

    ### private method for verifying game board ########################################################################
    def _verify(self) -> bool:
        """
        Verifies the integrity of the Tic-Tac-Toe game board by checking the following conditions:
        1. _board must be a list of size 3.
        2. Each element of _board must be a list of size 3.
        3. Each element of the sublists must be one of "X", "O", or " " (space).

        Returns:
        - bool: True = valid game board | False = invalid game board
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
    
    ### method for displaying game board ###############################################################################
    def display(self) -> bool:
        """
        Prints the current Tic-Tac-Toe game board to the console.
        
        Returns:
        - bool: True = printing successful | False = invalid game board
        """

        ### verifying game board ---------------------------------------------------------------------------------------

        # invalid game board > returning false
        if not self._verify(): return False

        ### method main logic ------------------------------------------------------------------------------------------

        # printing column numbers
        print("\n   | 1 | 2 | 3 ")
        # looping through rows of game board
        for index,row in enumerate(self._board):
            # printing divider
            print("---|---|---|---")
            # printing row number and row
            print(f" {index+1} | {row[0]} | {row[1]} | {row[2]} ")
        # printing successful > returning true
        return True
    
    ### method for returning game board ################################################################################
    def get(self) -> List[List[str]]:
        """
        Returns the current state of the Tic-Tac-Toe game board.

        Returns:
        - List[List[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "
        """

        ### method main logic ------------------------------------------------------------------------------------------

        # invalid game board > returning error board
        if not self._verify(): return [["@" for _ in range(3)] for _ in range(3)]
        # valid game board > returning game board
        else: return self._board
    
    ### method for updating game board #################################################################################
    def update(self, aRow=int(), aColumn=int(), aMark=str()) -> int:
        """
        Updates the Tic-Tac-Toe game board with the player move.
        
        Args:
        - aRow: int, 0-2, row index of player move
        - aColumn: int, 0-2, column index of player move
        - aMark: str, player mark "X"|"O"
        
        Returns:
        - int: 1 = update successful | 0 = update failed | -1 = invalid input
        """

        ### verifying inputs -------------------------------------------------------------------------------------------

        # invalid input > returning -1
        if not self._verify() or not isinstance(aRow, int) \
        or not isinstance(aColumn, int) or aMark not in ["X","O"," "]:
            return -1
        # incorrect index | position occupied > returning 0
        if aRow < 0 or 2 < aRow or aColumn < 0 or 2 < aColumn or self._board[aRow][aColumn] != " ": return 0

        ### method main logic ------------------------------------------------------------------------------------------
        
        # placing player mark on game board
        self._board[aRow][aColumn] = aMark
        # update successful > returning 1
        return 1
    
    ### method for checking terminal conditions ########################################################################
    def check(self) -> str:
        """Checks the Tic-Tac-Toe game board for a winner or draw.

        Returns:
        - str: "X" = player wins | "O" = AI wins | "=" = draw | "" = no terminal condition | "@" = invalid game board
        """

        ### verifying game board ---------------------------------------------------------------------------------------

        # invalid game board > returning "@"
        if not self._verify(): return "@"

        ### method main logic ------------------------------------------------------------------------------------------

        ### defining win conditions
        win_conditions: List[List[str]] = [self._board[row] for row in range(3)] # rows
        win_conditions.extend([list(column) for column in zip(*self._board)]) # columns
        win_conditions.append([self._board[index][index] for index in range(3)]) # backslash diagonal
        win_conditions.append([self._board[index][2 - index] for index in range(3)]) # slash diagonal

        ### checking for terminal conditions
        # player wins > returning "X"
        if any(line == ["X"] * 3 for line in win_conditions): return "X"
        # AI wins > returning "O"
        if any(line == ["O"] * 3 for line in win_conditions): return "O"
        # draw > returning "="
        if all(item in ["X","O"] for row in self._board for item in row): return "="
        # no terminal condition > returning ""
        return ""

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

### minimax algorithm ##################################################################################################
def minimax(aBoard=GameBoard(), aMaximizing=True) -> int:
    """
    Implements the Minimax Algorithm for determining the next AI move.
    
    Args:
    - aBoard: GameBoard() object, handles the game board
    - aMaximizing: bool, True = maximizing score, False = minimizing score
    
    Returns:
    - int: 1 = AI wins | 0 = draw | -1 = player wins | -2 = minimax failure
    """

    ### verifying inputs -----------------------------------------------------------------------------------------------

    # invalid aBoard type | invalid aMaximizing type > returning -2
    if not isinstance(aBoard, GameBoard) or not isinstance(aMaximizing, bool): return -2
    # retrieving game board
    board: List[List[str]] = aBoard.get()
    # invalid game board > returning -2
    if board[0][0] == "@": return -2

    ### checking for terminal conditions -------------------------------------------------------------------------------

    # retrieving condition code
    condition: str = aBoard.check()
    # AI wins > returning 1
    if condition == "O": return 1
    # draw > returning 0
    if condition == "=": return 0
    # player wins > returning -1
    if condition == "X": return -1
    # error code > returning -2
    if condition == "@": return -2

    ### minimaxing logic -----------------------------------------------------------------------------------------------
    
    # initializing best score
    best_score: float = -float("inf") if aMaximizing else float("inf")
    # looping through available moves
    for row,column in [(i,j) for i in range(3) for j in range(3) if board[i][j] == " "]:
        # determining player mark
        player: str = "O" if aMaximizing else "X"
        # placing move > update failure > returning -2
        if aBoard.update(aRow=row, aColumn=column, aMark=player) == -1: return -2
        # determining minimax flag
        minimax_flag: bool = False if aMaximizing else True
        # calling minimax for opponent move
        last_score = minimax(aBoard=aBoard, aMaximizing=minimax_flag)
        # minimax failure > returning -2
        if last_score == -2: return -2
        # undoing move > update failure > returning -2
        if aBoard.update(aRow=row, aColumn=column, aMark=" ") == -1: return -2
        # updating best score
        best_score = max(last_score, best_score) if aMaximizing else min(last_score, best_score)
    # returning best score
    return best_score

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
