"""Position object for any position on the board."""


class Position:
    """Position object can contain an x a y and a label."""

    def __init__(
        self,
        x: int,
        y: int,
        label: str,
        playable: bool = True,  # noqa: FBT001
    ) -> None:
        """X, Y and label values initialised."""
        self.x = x
        self.y = y
        self.label = label
        self.playable = playable
        self.is_vowel = self.is_vowel()

    def valid_move(self, board_width, board_height):
        """Check to see if the next move is Valid."""
        valid: bool = True

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
        is_vowel: bool = False
        vowels: str = "aeiou"

        if self.label[0].lower() in vowels:
            is_vowel = True
        return is_vowel

    def bishop_move(self, board):
        """Logic for the bishop move criteria."""
        possible_left = self.x
        possible_up = self.y
        possible_down = board.height - (self.y + 1)
        possible_right = board.width - (self.x + 1)

        north_east = min(possible_right, possible_up)
        south_east = min(possible_right, possible_down)
        north_west = min(possible_left, possible_up)
        south_west = min(possible_left, possible_down)

        possible_moves = []
        for place in range(north_east):
            possible_moves.append(
                Position(
                    self.x + (place + 1),
                    self.y - (place + 1),
                    board.board[self.y - (place + 1)][self.x + (place + 1)],
                    True,
                ),
            )
        for place in range(south_east):
            possible_moves.append(
                Position(
                    self.x + (place + 1),
                    self.y + (place + 1),
                    board.board[self.y + (place + 1)][self.x + (place + 1)],
                    True,
                ),
            )
        for place in range(north_west):
            possible_moves.append(
                Position(
                    self.x - (place + 1),
                    self.y - (place + 1),
                    board.board[self.y - (place + 1)][self.x - (place + 1)],
                    True,
                ),
            )
        for place in range(south_west):
            possible_moves.append(
                Position(
                    self.x - (place + 1),
                    self.y + (place + 1),
                    board.board[self.y + (place + 1)][self.x - (place + 1)],
                    True,
                ),
            )
        return [move for move in possible_moves if move.valid_move(board.width, board.height)]

    def knight_move(self, board):
        """Logic for the knight move criteria."""
        right_one_up_two = {"x": -1, "y": -2}
        right_one_down_two = {"x": -1, "y": 2}
        left_one_up_two = {"x": 1, "y": -2}
        left_one_down_two = {"x": 1, "y": 2}
        right_two_up_one = {"x": -2, "y": -1}
        right_two_down_one = {"x": -2, "y": 1}
        left_two_up_one = {"x": 2, "y": -1}
        left_two_down_one = {"x": 2, "y": 1}

        movemenets = [
            right_one_up_two,
            right_one_down_two,
            left_one_up_two,
            left_one_down_two,
            right_two_up_one,
            right_two_down_one,
            left_two_up_one,
            left_two_down_one,
        ]
        new_positions = [
            (
                self.x + move["x"],
                self.y + move["y"],
            )
            for move in movemenets
        ]

        possible_moves = [
            Position(
                pos[0],
                pos[1],
                board.board[pos[1]][pos[0]],
                True,
            )
            for pos in new_positions
            if check_value(pos[0], board.width - 1) and check_value(pos[1], board.height - 1)
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
