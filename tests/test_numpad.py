"""File to run the tests for the Board object."""

from objects.numpad import Board
from objects.position import Position

TEST_POSITIONS = [
    {"label": "a", "x": 0, "y": 0, "playable": True},
    {"label": "b", "x": 1, "y": 0, "playable": True},
]
TEST_WIDTH = 2
TEST_HEIGHT = 1


def test_board():
    """Pytest tests to test the board class object."""
    data = [Position(p["x"], p["y"], p["label"], p["playable"]) for p in TEST_POSITIONS]
    test_board = Board(TEST_WIDTH, TEST_HEIGHT, data)

    assert test_board.width == TEST_WIDTH
    assert test_board.height == TEST_HEIGHT
    assert test_board.positions == data

    expected = [["a", "b"]]

    assert test_board.board == expected


def test_show_board(capsys):
    """Pytest test to test the board.show_board function."""
    data = [Position(p["x"], p["y"], p["label"], p["playable"]) for p in TEST_POSITIONS]
    test_board = Board(TEST_WIDTH, TEST_HEIGHT, data)
    test_board.show_board()
    captured = capsys.readouterr()

    assert "a | b" in captured.out
    assert "A | B" not in captured.out
    assert "a, b" not in captured.out
