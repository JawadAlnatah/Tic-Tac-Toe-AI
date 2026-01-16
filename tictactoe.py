"""
Tic Tac Toe Player
"""

import math

import copy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    O_count = 0
    X_count = 0

    for row in board:
        for cell in row:

            if cell == O:
                O_count += 1

            elif cell == X:
                X_count += 1
    
    
    if O_count == X_count:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row_index, row in enumerate(board):
        for col_index, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((row_index,col_index))
                
    return possible_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    row, col =action

    if row < 0 or row >2 or col < 0 or col >2:
        raise Exception("Invalid action")
    
    if board[row][col] is not EMPTY:
        raise Exception("Invalid action")

    board_copy = copy.deepcopy(board)


    board_copy[row][col] = player(board)

    return board_copy

    
                





def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    """
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)]
    """

    
    for row in range(3):
        #check for row win
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not EMPTY:
            return board[row][0]
        
    for col in range(3):
        #check for column win    
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]
        

    #check for top-right diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    
    #check for bottom left
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not EMPTY:
        return board[2][0]

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board):
        return True
    if not actions(board):
        return True
    else:
        return False

        


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if terminal(board):
        if winner(board) == X:
            return 1
        if winner(board) == O:
            return -1
        else:
            return 0



def max_value(board):
    if terminal(board):
        return utility(board)
    
    best = -math.inf

    for action in actions(board):
        new_board = result(board,action)
        score = min_value(new_board)
        best = max(best,score)
    
    return best



def min_value(board):
    if terminal (board):
        return utility(board)
    
    best = math.inf

    for action in actions(board):
        new_board = result(board,action)
        score = max_value(new_board)
        best = min(best,score)

    return best



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    if player(board) == X:
        best_score = -math.inf
        best_action = None

        for action in actions(board):
            score = min_value(result(board, action))

            if score > best_score:
                best_score = score
                best_action = action
        
        return best_action
    
    if player(board) == O:
        best_score = math.inf
        best_action = None

        for action in actions(board):
            score = max_value(result(board, action))

            if score < best_score:
                best_score = score
                best_action = action

        return best_action

      
    
