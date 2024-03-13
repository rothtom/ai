import pytest
import minesweeper as ms


def main():
    test_neighbours()


def test_neighbours():
    assert ms.neighbours((0, 0)) == {(0, 1), (1, 0), (1, 1)}
    assert ms.neighbours((1, 1)) == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}
