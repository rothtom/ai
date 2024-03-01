"""
Tic Tac Toe Player
"""

import math
import sys
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

sys.setrecursionlimit(100000)


class Node():
    def __init__(self, state, action, parent):
        self.state = state
        self.action = action
        self.parent = parent
        self.children = []
        self.util = None
        self.possibilities = actions(self.state)
    
    def remove(self):
        possibilities = self.possibilities
        possibility = possibilities[0]
        possibilities.remove(possibilities[0])
        self.possibilities = possibilities
        return possibility
    
    def empty(self):
        return len(self.possibilities) == 0
    








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
    moves = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                moves += 1
    if (moves % 2) == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = tuple()
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action = (i, j)
                actions.append(action)
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    action = list(action)
    if board[action[0]][action[1]] != EMPTY:
        raise ProcessLookupError
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]

    if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])) and board[1][1] != EMPTY:
        return board[1][1]

    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) == 0 or winner(board) != None:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    state = Node(state=board, action=None, parent=None)
    moves = []
    p = player(state.state)
    for action in actions(state.state):
        state = Node(state=result(state.state, action), action=action, parent=state)
        if p == O:
            state.util = MIN(state).util
        else:
            state.util = MAX(state).util
        moves.append({"action": state.action,
                      "util": state.util})
    
    if p == O:
        util = 2
        for move in moves:
            if move["util"] < util:
                optimal_move = move["action"]

    elif p == X:
        util = -2
        for move in moves:
            if move["util"] > util:
                optimal_move = move["action"]



    return optimal_move



def MIN(state):
    while state.possibilities != None:    
        if state.empty():
            state = state.parent
            
        action = state.remove()
        state = Node(state=result(state.state, action), action=action, parent=state)
        state.parent.children.append(state)
        print(state.state, state.parent.state, state.children)
        util = MAX(state).util
        state.util = 2
        if util < state.util:
            state.util = util
        
        if terminal(state.state) == True:
            state.util = utility(state.state)
            return state
        
        if state.possibilities == None:
            return state


    state.util = utility(state.state) 
    return state
    
    

    
    





def MAX(state):
    while state.possibilities != None:
        if state.empty():
            state = state.parent
        action = state.remove()
        state = Node(state=result(state.state, action), action=action, parent=state)
        state.parent.children.append(state)
        print(state.state, state.parent.state, state.children)
        util = MIN(state).util
        state.util = -2
        if util > state.util:
            state.util = util
        
        if terminal(state.state) == True:
            state.util = utility(state.state)
            return state
        
        if state.possibilities == None:
            return state


    state.util = utility(state.state) 
    return state
    
    
    
