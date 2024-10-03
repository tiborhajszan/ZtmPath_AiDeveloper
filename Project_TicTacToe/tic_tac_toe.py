### Course: Zero to Mastery Academy | Prompt Engineering
### Section 5: Challenge - Build Your Second Game (Tic-Tac-Toe with AI opponent)

### imports
import sys
from typing import List, Tuple

########################################################################################################################
# Game Board Module                                                                                                    #
########################################################################################################################

### function for initializing game board -------------------------------------------------------------------------------
def initialize_board() -> List[List[str]]:
    """
    Initializes an empty 3x3 Tic-Tac-Toe board.

    Returns:
    - List[List[str]]: empty game board, 3x3 list of strings, all elements " "
    """

    ### creating and returning 3x3 list matrix filled with spaces
    return [[" " for _ in range(3)] for _ in range(3)]

### function for verifying game board ----------------------------------------------------------------------------------
def verify_board(aBoard=list()) -> bool:
    """
    Verifies the integrity of the Tic-Tac-Toe board by checking the following conditions:
    1. The input "aBoard" must be a list of size 3.
    2. Each element of "aBoard" must be a list of size 3.
    3. Each element of the sublists must be one of "X", "O", or " " (space).

    Args:
    - aBoard: List[List[str]], game board to verify, 3x3 list of strings, elements "X"|"O"|" "

    Returns:
    - bool: True = valid board, False = invalid board
    """
    
    ### aBoard is not list of size 3 > returning false
    if not isinstance(aBoard, list) or len(aBoard) != 3: return False
    
    ### aBoard elements are not lists of size 3 > returning false
    if not all(isinstance(row, list) and len(row) == 3 for row in aBoard): return False
        
    ### aBoard sublist elements are not "X"|"O"|" " > returning false
    if not all(all(item in ["X","O"," "] for item in row) for row in aBoard): return False
    
    ### all checks passed > returning true
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
def update_board(aBoard=initialize_board(), aMove=(-1,-1), aMark="X") -> bool:
    """
    Updates the Tic-Tac-Toe board with the player move.
    
    Args:
        board: list[list[str]], current state of game board, 3x3 list of strings, elements "X" | "O" | ""
        position: tuple[int,int], row and column indices of player move
        player: str, player mark ("X" | "O", default = "X")
    
    Returns:
        bool: True = successful move, False = invalid move
    """
    
    ### unpacking position tuple into row and column
    row,col = aMove

    ### checking whether position is within board
    if 0 <= row < 3 and 0 <= col < 3: # valid position
        pass
    else: # invalid position
        return False
    
    ### checking whether position is available (not already marked with 'X' or 'O')
    if aBoard[row][col] == " ": # available position
        aBoard[row][col] = aMark # placing player mark on board
        return True
    else: # occupied position
        return False

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
    - bool: True = full board, False otherwise
    """

    ### invalid game board > returning false
    if not verify_board(aBoard=aBoard): return False
    
    ### full board > returning true | cells available > returning false
    return all(cell != " " for row in aBoard for cell in row)

board = [["H" for _ in range(3)] for _ in range(3)]
# board[0][0] = "O"
# board[1][1] = "O"
# board[2][2] = "O"
# board.append([" ", " ", " "])
display_board(aBoard=board)
print([is_draw(aBoard=board)])
sys.exit()

########################################################################################################################
# Player Input Module                                                                                                  #
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
    
    def minimax(board: List[List[str]], is_maximizing: bool) -> int:
        """
        Implements the Minimax algorithm to evaluate board states.
        
        Args:
        - board (List[List[str]]): The current game board.
        - is_maximizing (bool): Whether the current turn is maximizing or minimizing (AI or player).
        
        Returns:
        - int: The score for the given board state.
        """
        winner = check_winner(board)
        if winner == "O":  # AI wins
            return 1
        elif winner == "X":  # Player wins
            return -1
        elif is_draw(board):  # Draw
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for row, col in available_moves(board):
                board[row][col] = "O"
                score = minimax(board, False)
                board[row][col] = " "  # Undo move
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row, col in available_moves(board):
                board[row][col] = "X"
                score = minimax(board, True)
                board[row][col] = " "  # Undo move
                best_score = min(score, best_score)
            return best_score

    def available_moves(board: List[List[str]]) -> List[Tuple[int, int]]:
        """Returns a list of available moves as (row, col) tuples."""
        return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

    def is_draw(board: List[List[str]]) -> bool:
        """Returns True if the board is full (no available moves) and there's no winner."""
        return all(cell != " " for row in board for cell in row)

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
