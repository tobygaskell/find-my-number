"""File to run the tests for the Path object."""

from objects.path import Path
from objects.position import Position


def test_path():
    """Test basic path object."""
    test_path = Path()

    assert test_path.moves == []
    assert test_path.length == 0
    assert test_path.num_of_vowels == 0
    assert test_path.last_position is None


def test_path_filled():
    """Test basic path object."""
    test_positions = [
        {"label": "a", "x": 0, "y": 0, "playable": True},
        {"label": "i", "x": 1, "y": 0, "playable": True},
    ]
    expected_moves = [Position(p["x"], p["y"], p["label"], p["playable"]) for p in test_positions]
    expected_length = 2
    expected_num_of_vowels = 2
    test_path = Path(expected_moves)

    assert test_path.moves == expected_moves
    assert test_path.length == expected_length
    assert test_path.num_of_vowels == expected_num_of_vowels
    assert test_path.last_position is None


def test_add_move():
    """Test add move method."""
    initial_position = Position(0, 0, "a", True)
    added_position = Position(0, 1, "i", True)

    expected_moves = [initial_position, added_position]
    expected_length = 2
    expected_num_of_vowels = 2

    test_path = Path([initial_position])

    test_path.add_move(added_position)

    assert test_path.moves == expected_moves
    assert test_path.length == expected_length
    assert test_path.num_of_vowels == expected_num_of_vowels
    assert test_path.last_position is added_position


def test_check_move():
    """Test the check move method."""
    initial_position = Position(0, 0, "a", True)
    added_position = Position(0, 1, "i", True)

    test_path = Path([initial_position])

    test_too_many_vowel = test_path.check_move(added_position, 2, 1)

    assert not test_too_many_vowel

    test_too_long = test_path.check_move(added_position, 1, 2)

    assert not test_too_long

    test_both = test_path.check_move(added_position, 1, 1)

    assert not test_both

    test_valid = test_path.check_move(added_position, 2, 2)

    assert test_valid


def test_clone():
    """Test the clone method and ensure that all the values are the same after clone."""
    initial_position = Position(0, 0, "a", True)
    test_path = Path([initial_position])
    new_path = test_path.clone()

    assert test_path.moves == new_path.moves
    assert test_path.length == new_path.length
    assert test_path.num_of_vowels == new_path.num_of_vowels
    assert test_path.last_position is new_path.last_position
