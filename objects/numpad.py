"""Board object for find-my-number problem."""


class Board:
    """Board object."""

    def __init__(self, width, height, positions) -> None:
        """Board can have a width, a height and a list of positions."""
        self.width = width
        self.height = height
        self.positions = positions
        self.board = self.init_positions()

    def show_board(self):
        """Display the board to standard out."""
        for row in self.board:
            print(" | ".join(row))  # noqa: T201
        return True

    def init_positions(self):
        """Set up the board with the positions given."""
        numpad = [["-" for position in range(self.width)] for position in range(self.height)]
        for pos in self.positions:
            numpad[pos.y][pos.x] = pos.label
        return numpad
