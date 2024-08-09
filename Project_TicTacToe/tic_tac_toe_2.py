### Course: Zero to Mastery Academy | Prompt Engineering
### Section 5: Building Tic-Tac-Toe Game
### Game code, docstrings, and comments were all created by ChatGPT.

### function displaying the current board ------------------------------------------------------------------------------
def display_board(board=list()) -> None:
    """
    Displays the current state of the Tic-Tac-Toe board.
    
    Args:
        board (list[str]): List of 9 elements representing the current board. Elements are 'X' | 'O' | ' '.
    """

    ### function main logic
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

    ### returning
    return

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

def minimax(board, is_maximizing, ai_player, human_player):
    if check_win(board, ai_player):
        return 1
    elif check_win(board, human_player):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai_player
                score = minimax(board, False, ai_player, human_player)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = human_player
                score = minimax(board, True, ai_player, human_player)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move(board, ai_player):
    best_score = -float('inf')
    best_move = None
    human_player = 'X' if ai_player == 'O' else 'O'

    for i in range(9):
        if board[i] == ' ':
            board[i] = ai_player
            score = minimax(board, False, ai_player, human_player)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = ai_player

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    human_player = 'X'
    ai_player = 'O'
    current_player = 'X'

    while True:
        display_board(board)
        if current_player == human_player:
            player_move(board, human_player)
        else:
            ai_move(board, ai_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = ai_player if current_player == human_player else human_player

tic_tac_toe()
