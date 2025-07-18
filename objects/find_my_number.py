"""Main Logic for the Find My Number game."""

import logging

from objects.numpad import Board
from objects.path import Path

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)


class NumberFinder:
    """Class to encapsulate the logic for finding paths in the number grid."""

    def __init__(self, width, height, cnt, vowels) -> None:
        """Initialize the game with board dimensions and path requirements."""
        self.width = width
        self.height = height
        self.cnt = cnt
        self.vowels = vowels
        self.board = Board(self.width, self.height)
        self.knight_moves_cache = {
            (pos.x, pos.y, pos.label): pos.knight_move(self.board) for pos in self.board.positions
        }
        self.total_paths = []
        self.path_cnt = 0

    def find_paths(self):
        """Find all valid paths based on knight moves."""
        for position in self.board.positions:
            starting_path = Path()
            paths = [starting_path.add_move(position)]
            for _ in range(self.cnt - 1):
                new_paths = []
                for path in paths:
                    moves = self.knight_moves_cache[
                        (
                            path.last_position.x,
                            path.last_position.y,
                            path.last_position.label,
                        )
                    ]
                    for move in moves:
                        if path.check_move(move, self.cnt, self.vowels):
                            new_paths.append(path.clone().add_move(move))
                paths = new_paths

            self.total_paths.append([path for path in paths if path.length == self.cnt])

        self.path_cnt = len([item for sublist in self.total_paths for item in sublist])
