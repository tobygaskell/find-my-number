"""File to run the tests for the Board object."""

from objects.numpad import Board

TEST_WIDTH = 3
TEST_HEIGHT = 2


def test_board():
    """Pytest tests to test the board class object."""
    test_board = Board(TEST_WIDTH, TEST_HEIGHT)

    assert test_board.width == TEST_WIDTH
    assert test_board.height == TEST_HEIGHT

    expected = [["a", "b", "c"], ["-", "1", "-"]]

    assert test_board.board == expected


def test_show_board(capsys):
    """Pytest test to test the board.show_board function."""
    test_board = Board(TEST_WIDTH, TEST_HEIGHT)
    test_board.show_board()
    captured = capsys.readouterr()

    assert "a | b | c" in captured.out
    assert "A | B | C" not in captured.out
    assert "a, b, c" not in captured.out
    assert "- | 1 | -" in captured.out
