"""Path object for find-my-number problem - will be a combination of positions."""


class Path:
    """Path object for the find-my-number problem."""

    def __init__(self, moves=None) -> None:
        """Init function for the path object."""
        self.moves = moves.copy() if moves else []
        self.length = len(self.moves)
        self.num_of_vowels = len([move for move in self.moves if move.is_vowel])
        self.last_position = None

    def check_move(self, move, cnt, vowels_allowed):
        """Check to see if any of the path criteria is broken."""
        valid_move = True
        moves = self.moves.copy()
        moves.append(move)
        length = len(moves)
        num_of_vowels = len([move for move in moves if move.is_vowel])
        if num_of_vowels > vowels_allowed:
            valid_move = False

        if length > cnt:
            valid_move = False

        return valid_move

    def add_move(self, move):
        """Will add a move to the path."""
        self.moves.append(move)
        self.last_position = move
        self.length = len(self.moves)
        self.num_of_vowels = len([move for move in self.moves if move.is_vowel])
        return self

    def clone(self):
        """Clones the Path."""
        return Path(self.moves)
