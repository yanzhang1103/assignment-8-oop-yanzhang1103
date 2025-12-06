import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from models.board import Board


def test_row_win():
    b = Board()
    b.grid = [
        ["X", "X", "X"],
        [" ", "O", " "],
        ["O", " ", " "]
    ]
    assert b.check_winner() == "X"


def test_column_win():
    b = Board()
    b.grid = [
        ["O", "X", " "],
        ["O", "X", " "],
        ["O", " ", "X"]
    ]
    assert b.check_winner() == "O"


def test_diagonal_win():
    b = Board()
    b.grid = [
        ["X", "O", " "],
        ["O", "X", "O"],
        [" ", " ", "X"]
    ]
    assert b.check_winner() == "X"


def test_no_winner():
    b = Board()
    b.grid = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"]
    ]
    assert b.check_winner() == ""
