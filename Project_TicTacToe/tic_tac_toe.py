### Course: Zero to Mastery Academy | Prompt Engineering
### Section 5: Challenge - Build Your Second Game (Tic-Tac-Toe with AI opponent)

### imports
import sys
from typing import List

########################################################################################################################
# Game Board Class                                                                                                     #
########################################################################################################################

class GameBoard:
    """
    Represents and handles the Tic-Tac-Toe game board.
    
    Attributes:
    - _board : List[List[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "|"@"
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
        2. Each item of _board must be a list of size 3.
        3. Each item of the sublists must be "X"|"O"|" " (space).

        Returns:
        - bool: True = valid game board | False = invalid game board
        """
        
        ### method main logic ------------------------------------------------------------------------------------------

        # _board is not list of size 3 > returning false
        if not isinstance(self._board, list) or len(self._board) != 3: return False
        # _board items are not lists of size 3 > returning false
        if not all(isinstance(row, list) and len(row) == 3 for row in self._board): return False
        # _board sublist items are not "X"|"O"|" " > returning false
        if not all(item in ["X","O"," "] for row in self._board for item in row): return False
        # all checks passed > returning true
        return True
    
    ### method for displaying game board ###############################################################################
    def display(self) -> bool:
        """
        Prints the current Tic-Tac-Toe game board to the console.
        
        Returns:
        - bool: True = print success | False = print failure
        """

        ### verifying game board ---------------------------------------------------------------------------------------

        # invalid game board > returning false
        if not self._verify(): return False

        ### method main logic ------------------------------------------------------------------------------------------

        # clearing screen >> printing column numbers
        print("\033[H\033[J", end="")
        print("\n   | 1 | 2 | 3 ")
        # looping through rows of game board
        for index,row in enumerate(self._board):
            # printing divider >> printing row number and row
            print("---|---|---|---")
            print(f" {index+1} | {row[0]} | {row[1]} | {row[2]} ")
        # print success > returning true
        return True
    
    ### method for returning game board ################################################################################
    def get(self) -> List[List[str]]:
        """
        Returns the current state of the Tic-Tac-Toe game board.

        Returns:
        - List[List[str]], current state of game board, 3x3 list of strings, elements "X"|"O"|" "|"@"
        """

        ### method main logic ------------------------------------------------------------------------------------------

        # invalid game board > creating error board >> returning game board
        self._board[0][0] = "@" if not self._verify() else self._board[0][0]
        return self._board
    
    ### method for updating game board #################################################################################
    def update(self, aRow=int(), aColumn=int(), aMark=str()) -> int:
        """
        Updates the Tic-Tac-Toe game board with the player move.
        
        Args:
        - aRow: int, 0-2, row index of player move
        - aColumn: int, 0-2, column index of player move
        - aMark: str, player mark "X"|"O"
        
        Returns:
        - int: 1 = update success | 0 = invalid move | -5 = update failure
        """

        ### verifying inputs -------------------------------------------------------------------------------------------

        # invalid game board > returning -5
        if not self._verify(): return -5
        # invalid input type > returning -5
        if not isinstance(aRow, int) or not isinstance(aColumn, int) or aMark not in ["X","O"," "]: return -5
        # invalid index > returning 0
        if aRow < 0 or 2 < aRow or aColumn < 0 or 2 < aColumn: return 0
        # position already occupied > returning 0
        if aMark in ["X","O"] and self._board[aRow][aColumn] != " ": return 0

        ### method main logic ------------------------------------------------------------------------------------------
        
        # placing player mark on game board >> returning 1
        self._board[aRow][aColumn] = aMark
        return 1
    
    ### method for checking terminal conditions ########################################################################
    def check(self) -> str:
        """Checks the Tic-Tac-Toe game board for a winner or draw.

        Returns:
        - str: "X" = human wins | "O" = AI wins | "=" = draw | "" = no terminal condition | "@" = check failure
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
        # human wins > returning "X"
        if any(line == ["X"] * 3 for line in win_conditions): return "X"
        # AI wins > returning "O"
        if any(line == ["O"] * 3 for line in win_conditions): return "O"
        # draw > returning "="
        if all(item in ["X","O"] for row in self._board for item in row): return "="
        # no terminal condition > returning empty string
        return ""

########################################################################################################################
# Move Input Module                                                                                                    #
########################################################################################################################

### function for obtaining human move ##################################################################################
def human_move(aBoard=GameBoard()) -> bool:
    """
    Obtains, validates, and places a move on the Tic-Tac-Toe game board from the human player.

    Args:
    - aBoard: GameBoard() object, handles the game board

    Returns:
    - bool: True = move success | False = move failure
    """
    
    ### verifying input  -----------------------------------------------------------------------------------------------

    # invalid aBoard type > returning false
    if not isinstance(aBoard, GameBoard): return False

    ### function main logic --------------------------------------------------------------------------------------------

    # printing separator line
    print()
    # looping until valid move is entered
    while True:
        # prompting for move > splitting input >> stripping leading and trailing spaces
        player_move: List[str] = input("Enter your move (row,column): ").split(",")
        player_move = [item.strip() for item in player_move]
        # invalid input >> deleting prompt > restarting loop
        if len(player_move) != 2 or not all(item.isdecimal() for item in player_move):
            print("\033[1A", end="\x1b[2K"); continue
        # converting input to game board position indices >> placing move on game board
        row,column = map(lambda x: int(x)-1, player_move)
        return_code: int = aBoard.update(aRow=row, aColumn=column, aMark="X")
        # update success > returning true >> update failure > returning false
        if return_code == 1: return True
        if return_code == -5: return False
        # invalid move > deleting prompt > restarting loop
        print("\033[1A", end="\x1b[2K")

### minimax algorithm ##################################################################################################
def minimax(aBoard=GameBoard(), aMaximizing=True) -> int:
    """
    Implements the Minimax Algorithm for determining the next AI move.
    Attempts to maximize the chances of winning for the AI player.
    Attempts to minimize the chances of winning for the human player.
    
    Args:
    - aBoard: GameBoard() object, handles the game board
    - aMaximizing: bool, True = maximizing score | False = minimizing score
    
    Returns:
    - int: 1 = AI wins | 0 = draw | -1 = human wins | -5 = minimax failure
    """

    ### verifying inputs -----------------------------------------------------------------------------------------------

    # invalid aBoard type | invalid game board | invalid aMaximizing type > returning -5
    if not isinstance(aBoard, GameBoard) or aBoard.get()[0][0] == "@" or not isinstance(aMaximizing, bool): return -5

    ### checking for terminal conditions -------------------------------------------------------------------------------

    # retrieving condition code
    condition: str = aBoard.check()
    # AI wins > returning 1
    if condition == "O": return 1
    # draw > returning 0
    if condition == "=": return 0
    # human wins > returning -1
    if condition == "X": return -1
    # check failure > returning -5
    if condition == "@": return -5

    ### minimax logic --------------------------------------------------------------------------------------------------
    
    # initializing best score
    best_score: float = -float("inf") if aMaximizing else float("inf")
    # looping through available moves
    for row,column in [(i,j) for i in range(3) for j in range(3) if aBoard.get()[i][j] == " "]:
        # determining player mark >> placing move > update failure > returning -5
        player_mark: str = "O" if aMaximizing else "X"
        if aBoard.update(aRow=row, aColumn=column, aMark=player_mark) == -5: return -5
        # determining minimax flag >> calling minimax for opponent move >> minimax failure > returning -5
        minimax_flag: bool = False if aMaximizing else True
        last_score = minimax(aBoard=aBoard, aMaximizing=minimax_flag)
        if last_score == -5: return -5
        # undoing move > update failure > returning -5
        if aBoard.update(aRow=row, aColumn=column, aMark=" ") == -5: return -5
        # updating best score
        best_score = max(last_score, best_score) if aMaximizing else min(last_score, best_score)
    # returning best score
    return best_score

### function for figuring ai move ######################################################################################
def ai_move(aBoard=GameBoard()) -> bool:
    """
    Determines the next AI move using the Minimax Algorithm.
    
    Args:
    - aBoard: GameBoard() object, handles the game board
    
    Returns:
    - bool: True = move success | False = move failure
    """

    ### function init --------------------------------------------------------------------------------------------------

    # invalid aBoard type | invalid game board > returning false
    if not isinstance(aBoard, GameBoard) or aBoard.get()[0][0] == "@": return False
    # best row, column, score inits
    best_row, best_column, best_score = -1, -1, -float("inf")

    ### figuring best move ---------------------------------------------------------------------------------------------
    
    # looping through available moves
    for row,column in [(i,j) for i in range(3) for j in range(3) if aBoard.get()[i][j] == " "]:
        # placing AI move > update failure > returning false
        if aBoard.update(aRow=row, aColumn=column, aMark="O") == -5: return False
        # calling minimax for human move >> minimax failure > returning false
        last_score = minimax(aBoard=aBoard, aMaximizing=False)
        if last_score == -5: return False
        # undoing AI move > update failure > returning false
        if aBoard.update(aRow=row, aColumn=column, aMark=" ") == -5: return False
        # better move found > updating best stuff
        if best_score < last_score: best_row, best_column, best_score = row, column, last_score
    
    ### taking best move -----------------------------------------------------------------------------------------------

    # placing best move > update failure > returning false >> move success > returning true
    if aBoard.update(aRow=best_row, aColumn=best_column, aMark="O") == -5: return False
    return True

########################################################################################################################
# Game Control Module                                                                                                  #
########################################################################################################################

### game loop function #################################################################################################
def game_loop() -> bool:
    """
    Runs the main game loop for Tic-Tac-Toe.
    
    Returns:
    - bool: True = game loop success | False = game loop failure
    """

    ### function init --------------------------------------------------------------------------------------------------

    ### initializing game board and starting player
    board: GameBoard = GameBoard(); player: str = "X"

    ### game loop init -------------------------------------------------------------------------------------------------

    # looping while terminal condition occurs
    while True:

        ### placing and displaying moves -------------------------------------------------------------------------------

        # displaying game board > print failure > returning false
        if not board.display(): return False
        # human turn >> placing human move > move failure > returning false
        if player == "X":
            if not human_move(aBoard=board): return False
        # AI turn >> placing AI move > move failure > returning false
        else:
            if not ai_move(aBoard=board): return False
        
        ### checking for terminal condition (win | lose | draw | failure) ----------------------------------------------

        # reading condition code
        condition: str = board.check()
        # check failure > returning false
        if condition == "@": return False
        # no terminal condition > switching turns > restarting loop
        elif not condition: player = "O" if player == "X" else "X"; continue
        # terminal condition
        else:
            # displaying final game board > print failure > returning false
            if not board.display(): return False
            # displaying separator line >> displaying result >> returning true
            print()
            print("You won!" if condition == "X" else "AI won!" if condition == "O" else "It is a draw!")
            return True

### main loop function for ending | restarting game ####################################################################
def main_loop() -> None:
    """
    Restarts or ends the Tic-Tac-Toe game.
    """

    ### function main logic --------------------------------------------------------------------------------------------

    ### looping until user decides to quit
    while True:

        ### running game
        # starting game loop
        return_code: bool = game_loop()
        # game loop success > printing game over message >> game loop failure > printing error message
        if return_code: print("\nGame Over!")
        else: print ("\nSomething went wrong. (Gremlins in the code...:)")

        ### input loop
        # printing separator line
        print()
        # continuous looping until valid choice is entered
        while True:
            # prompting user > parsing input
            user_choice: str = input("Enter 'r' to restart game or 'q' to quit: ").strip().lower()
            # valid choice > breaking loop >> invalid choice > deleting prompt
            if user_choice in ["r","q"]: break
            else: print("\033[1A", end="\x1b[2K")

        ### quitting game
        # choice is quit > terminating loop
        if user_choice == 'q': break

    ### terminating function -------------------------------------------------------------------------------------------

    # printing parting message >> returning
    print("\nSee you soon!\n")
    return

### executing script
# main program > starting main loop >> import module > printing error message
if __name__ == "__main__": main_loop()
else: print("\nError: This is not an import module.\n")
# terminating execution
sys.exit()
