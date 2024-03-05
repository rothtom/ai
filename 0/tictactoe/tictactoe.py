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
        self.util = None




explored = []







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

    state = Node(state=board, parent=None, action=None)    
    MAX(state)
    relevant = []
    for exploration in explored:
        if exploration.parent != None:
            if exploration.parent.state == board:
                print(exploration.parent.state)
                relevant.append(exploration)
    
    if relevant == []:
        print("No relevant moves!")
        return actions(board)[0]
    
    

    best_option = relevant[0] 

    p = player(board)
    if p == O:
        for state in relevant:   
            if state.util > best_option.util:
                best_option = state
    
    else:
        for state in relevant:
            if state.util < best_option.util:
                best_option = state

    print(state.state)
    return state.action
            




def MAX(state):
    possible_actions = actions(state.state)
    for possible_action in possible_actions:
        new_state = Node(state=result(state.state, possible_action), parent=state, action=possible_action)
        if terminal(new_state.state):
            new_state.util = utility(new_state.state)
            explored.append(new_state)
            return new_state
        
        temp_util = MIN(new_state).util
        if new_state.util == None:
            new_state.util = -2

        if temp_util < new_state.util:
            new_state.util = temp_util


    
    for possible_action in possible_actions:
        new_state = Node(state=result(state.state, possible_action), parent=state, action=possible_action)
        if new_state.util == None:
            new_state.util = MIN(new_state).util
    
        if state.util == None:
            state.util = -2
        
        if state.util < new_state.util:
            state.util = new_state.util
    
    explored.append(state)
    return state

def MIN(state):
    possible_actions = actions(state.state)
    for possible_action in possible_actions:
        new_state = Node(state=result(state.state, possible_action), parent=state, action=possible_action)
        if terminal(new_state.state):
            new_state.util = utility(new_state.state)
            explored.append(new_state)
            return new_state
        
        temp_util = MIN(new_state).util
        if new_state.util == None:
            new_state.util = 2

        if temp_util > new_state.util:
            new_state.util = temp_util


    
    for possible_action in possible_actions:
        new_state = Node(state=result(state.state, possible_action), parent=state, action=possible_action)
        if new_state.util == None:
            new_state.util = MIN(new_state).util
    
        if state.util == None:
            state.util = 2
        
        if state.util > new_state.util:
            state.util = new_state.util
    
    explored.append(state)
    return state
