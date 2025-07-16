"""Position object for any position on the board."""


class Position:
    """Position object can contain an x a y and a label."""

    def __init__(self, x, y, label, playable) -> None:
        """X, Y and label values initialised."""
        self.x = x
        self.y = y
        self.label = label
        self.playable = playable
        self.is_vowel = self.is_vowel()

    def valid_move(self, board_width, board_height):
        """Check to see if the next move is Valid."""
        valid = True
        if self.x > board_width - 1:
            valid = False
        if self.y > board_height - 1:
            valid = False
        if self.x < 0:
            valid = False
        if self.y < 0:
            valid = False
        if self.label == "-":
            valid = False
        return valid

    def is_vowel(self):
        """Check to see if the position is a vowel or not."""
        is_vowel = False
        if self.label.lower() in ("a", "e", "i", "o", "u"):
            is_vowel = True
        return is_vowel

    def knight_move(self, board):
        """Logic for the knight move criteria."""
        movemenets = [
            {"y": -2, "x": -1},
            {"y": -2, "x": 1},
            {"y": -1, "x": -2},
            {"y": 1, "x": -2},
            {"y": 2, "x": -1},
            {"y": 2, "x": 1},
            {"y": -1, "x": 2},
            {"y": 1, "x": 2},
        ]

        possible_moves = [
            Position(
                self.x + move["x"],
                self.y + move["y"],
                board.board[self.y + move["y"]][self.x + move["x"]],
                True,
            )
            for move in movemenets
            if check_value(self.x + move["x"], board.width - 1)
            and check_value(self.y + move["y"], board.height - 1)
        ]

        return [move for move in possible_moves if move.valid_move(board.width, board.height)]


def check_value(val, limit):
    """See if the value is in the valid bounds."""
    valid = True
    if val > limit:
        valid = False

    if val < 0:
        valid = False

    return valid
