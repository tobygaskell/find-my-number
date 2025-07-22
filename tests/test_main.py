"""File to run the tests for the main python file."""

from main import main


def test_main(caplog):
    """Test the main function of find-my-number."""
    with caplog.at_level("INFO"):
        main()

    assert "Starting find-my-number" in caplog.text
    assert "Total paths found:" in caplog.text
    assert "a | b | c | d | e" in caplog.text
    assert "- | 1 | 2 | 3 | -" in caplog.text
    assert "Elapsed time: " in caplog.text
    assert "seconds" in caplog.text
