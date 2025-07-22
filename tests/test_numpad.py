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
    expected_position: int = 4

    assert test_board.board == expected
    assert len(test_board.positions) == expected_position


def test_show_board(caplog):
    """Pytest test to test the board.show_board function."""
    test_board = Board(TEST_WIDTH, TEST_HEIGHT)
    with caplog.at_level("INFO"):
        test_board.show_board()

    assert "a | b | c" in caplog.text
    assert "A | B | C" not in caplog.text
    assert "a, b, c" not in caplog.text
    assert "- | 1 | -" in caplog.text


def test_show_board_large(caplog):
    """Pytest test to test the board.show_board function."""
    test_width: int = 10
    test_height: int = 5
    test_board = Board(test_width, test_height)
    with caplog.at_level("INFO"):
        test_board.show_board()

    assert "aa | bb | cc" in caplog.text
    assert "AA | BB | CC" not in caplog.text
    assert "aa, bb, cc" not in caplog.text
    assert "-  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | - " in caplog.text
