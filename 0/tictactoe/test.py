import pytest
from tictactoe import terminal, winner

EMPTY = None
X = "X"
O = "O"


board = [[EMPTY, EMPTY, EMPTY], 
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
    
board2 = [[X, X, X],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]

board3 =    [['O', 'X', 'O'],
            ['X', 'X', 'O'],
            ['X', 'O', 'X']]

board4 =    [[EMPTY, EMPTY, 'X'],
            ['O', 'X', 'O'],
            ['X', 'O', 'X']]

def main():
    test_terminal()
    test_winner()


def test_terminal():
    assert terminal(board) == False
    assert terminal(board2) == True
    assert terminal(board3) == True
    assert terminal(board4) == True


def test_winner():
    assert winner(board) == None
    assert winner(board2) == X
    assert winner(board3) == None
    assert winner(board4) == X