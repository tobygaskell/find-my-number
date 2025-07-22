"""File to run the test for the find_my_number object."""

from objects.find_my_number import NumberFinder


def test_number_finder():
    """Pytest test to test the number finder class object."""
    test_width: int = 3
    test_height: int = 2
    test_cnt: int = 3
    test_vowels: int = 1
    expected_paths: list = []
    expected_path_cnt: int = 0
    finder = NumberFinder(
        test_width,
        test_height,
        test_cnt,
        test_vowels,
    )

    assert finder.width == test_width
    assert finder.height == test_height
    assert finder.cnt == test_cnt
    assert finder.vowels == test_vowels
    assert finder.board.width == test_width
    assert finder.board.height == test_height
    assert finder.total_paths == expected_paths
    assert finder.path_cnt == expected_path_cnt
    assert isinstance(finder.knight_moves_cache, dict)


def test_find_paths():
    """Pytest test to test the find_paths function."""
    test_width: int = 3
    test_height: int = 2
    test_cnt: int = 3
    test_vowels: int = 1
    finder = NumberFinder(
        test_width,
        test_height,
        test_cnt,
        test_vowels,
    )
    finder.find_paths()

    expected_path_cnt: int = 0

    assert isinstance(finder.total_paths, list)
    assert finder.path_cnt == expected_path_cnt
    assert all(isinstance(path, list) for path in finder.total_paths)


def test_find_paths_with_results():
    """Ensure path_cnt is correctly updated when valid paths are found."""
    test_width: int = 4
    test_height: int = 3
    test_cnt: int = 3
    test_vowels: int = 0
    finder = NumberFinder(
        width=test_width,
        height=test_height,
        cnt=test_cnt,
        vowels=test_vowels,
    )

    finder.find_paths()

    assert finder.path_cnt > 0
