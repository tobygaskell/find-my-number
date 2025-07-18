"""Board object for find-my-number problem."""

from objects.position import Position


class Board:
    """Board object."""

    def __init__(self, width: int, height: int) -> None:
        """Board can have a width, a height and a list of positions."""
        self.width = width
        self.height = height
        self.board = self.init_positions()
        self.positions = [
            Position(x, y, label, True)
            for y, row in enumerate(self.board)
            for x, label in enumerate(row)
            if label != "-"
        ]

    def show_board(self):
        """Display the board to standard out with aligned columns."""
        max_len = max(len(cell) for row in self.board for cell in row)

        for row in self.board:
            formatted_row = [cell.ljust(max_len) for cell in row]
            print(" | ".join(formatted_row))  # noqa: T201

    def init_positions(self):
        """Set up the board with the positions given."""
        numpad = [["-" for position in range(self.width)] for position in range(self.height)]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        itter: int = 0
        letter_index: int = 0
        for i in range(self.height - 1):
            for j in range(self.width):
                numpad[i][j] = alphabet[letter_index] * (itter + 1)

                letter_index += 1

                if letter_index == len(alphabet):
                    itter += 1
                    letter_index = 0

        for j in range(self.width - 2):
            numpad[self.height - 1][j + 1] = str(j + 1)
        return numpad
