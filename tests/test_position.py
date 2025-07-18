"""File to run the tests for the Position object."""

from objects.numpad import Board
from objects.position import Position, check_value


def test_basic_position():
    """Test the init for the position class."""
    test_position = Position(0, 0, "a", True)
    expected_x = 0
    expected_y = 0
    expected_label = "a"
    expected_playable = True
    expected_is_vowel = True

    assert test_position.x == expected_x
    assert test_position.y == expected_y
    assert test_position.label == expected_label
    assert test_position.playable == expected_playable
    assert test_position.is_vowel == expected_is_vowel


def test_is_vowel():
    """Test the is vowel method returns true is label passed is vowel and false otherwise."""
    test_is_vowel = Position(0, 0, "a", True)
    expected_is_vowel = True
    assert test_is_vowel.is_vowel == expected_is_vowel

    test_is_not_vowel = Position(0, 0, "b", True)
    expected_is_not_vowel = False
    assert test_is_not_vowel.is_vowel == expected_is_not_vowel

    test_number = Position(0, 0, "2", True)
    expected_number = False
    assert test_number.is_vowel == expected_number

    test_dash = Position(0, 0, "-", False)
    expected_dash = False
    assert test_dash.is_vowel == expected_dash


def test_check_value():
    """Test the check value function for all evantualities."""
    test_val = 2
    test_limit = 3
    expected = True
    test_valid = check_value(test_val, test_limit)
    assert test_valid == expected

    test_too_high = 20
    test_limit = 3
    expected = False
    test_not_valid = check_value(test_too_high, test_limit)
    assert test_not_valid == expected

    test_negative = -2
    test_limit = 3
    expected = False
    test_not_valid = check_value(test_negative, test_limit)
    assert test_not_valid == expected

    test_same = 3
    test_limit = 3
    expected = True
    test_valid = check_value(test_same, test_limit)
    assert test_valid == expected

    test_zero = 0
    test_limit = 3
    expected = True
    test_valid = check_value(test_zero, test_limit)
    assert test_valid == expected


def test_valid_move():
    """Test the valid move method to ensure that the logic is correct."""
    test_position = Position(1, 0, "a", True)
    test_width = 3
    test_height = 3
    test_valid = test_position.valid_move(test_width, test_height)

    expected = True

    assert test_valid == expected

    test_position = Position(3, 0, "a", True)
    test_width = 3
    test_height = 3
    test_valid = test_position.valid_move(test_width, test_height)

    expected = False

    assert test_valid == expected

    test_position = Position(0, 3, "a", True)
    test_width = 3
    test_height = 3
    test_valid = test_position.valid_move(test_width, test_height)

    expected = False

    assert test_valid == expected

    test_position = Position(-1, 3, "a", True)
    test_width = 3
    test_height = 3
    test_valid = test_position.valid_move(test_width, test_height)

    expected = False

    assert test_valid == expected

    test_position = Position(2, -1, "a", True)
    test_width = 3
    test_height = 3
    test_valid = test_position.valid_move(test_width, test_height)

    expected = False

    assert test_valid == expected

    test_position = Position(1, 0, "-", True)
    test_width = 3
    test_height = 3
    test_valid = test_position.valid_move(test_width, test_height)

    expected = False

    assert test_valid == expected


def test_knight_move():
    """Test the knight move method to ensure that the logic is correct."""
    test_height = 3
    test_width = 3

    test_board = Board(test_width, test_height)

    test_board.show_board()

    test_position = Position(0, 0, "a", True)

    expected_length = 2
    expected_positions = [Position(1, 2, "f", True), Position(2, 1, "1", True)]

    moves = test_position.knight_move(test_board)

    assert len(moves) == expected_length
    assert {move.x for move in moves} == {move.x for move in expected_positions}
    assert {move.y for move in moves} == {move.y for move in expected_positions}
    assert {move.label for move in moves} == {move.label for move in expected_positions}
    assert {move.playable for move in moves} == {move.playable for move in expected_positions}
