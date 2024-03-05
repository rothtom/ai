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


class Frontier():
    def __init__(self):
        self.frontier = []

    def empty(self):
        return self.frontier == []
    
    def remove(self):
        item = self.frontier[-1]
        self.frontier.remove(item)
        return item

    def add(self, item):
        self.frontier.append(item)

    
frontier = Frontier()


class List():
    def add(self, item):
        if item not in self:
            self.append(item)


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

    top_state = Node(state=board, parent=None, action=None)    
    frontier.add(top_state)
    top_state = load_every_state()

    top_state = MAX(top_state)

    best_state = Node(state=None, action=None, parent=top_state)

    if player(board) == X:
        best_state.util = -2
        for state in top_state.children:
            if state.util > best_state.util:
                best_state = state
    
    else:
        best_state.util = 2
        for state in top_state.children:
            if state.util < best_state.util:
                best_state = state

    return best_state.action


def load_every_state():
    while frontier.empty() == False:
        state = frontier.remove()
        for action in actions(state.state):
            new_state = Node(state=result(state.state, action), action=action, parent=state)
            state.children.append(new_state)
            frontier.add(new_state)
    top_state = state
    while top_state.parent != None:
        top_state = top_state.parent
    return top_state
        

def MAX(state):
    if terminal(state.state):
        state.util = utility(state.state)
        return state

    state.util = -2
    for child in state.children:
        if child.util == None:
            child.util = MIN(child).util
        if child.util > state.util:
            state.util = child.util
    
    return state


def MIN(state):
    if terminal(state.state):
        state.util = utility(state.state)
        return state

    state.util = 2
    for child in state.children:
        if child.util == None:
            child.util = MAX(child).util
        if child.util < state.util:
            state.util = child.util
    
    return state
        
