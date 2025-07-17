"""Entery point for find-my-number."""

import logging
import random

from objects.numpad import Board
from objects.path import Path
from objects.position import Position

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)

POSITIONS = [
    {"label": "a", "x": 0, "y": 0, "playable": True},
    {"label": "b", "x": 1, "y": 0, "playable": True},
    {"label": "c", "x": 2, "y": 0, "playable": True},
    {"label": "d", "x": 3, "y": 0, "playable": True},
    {"label": "e", "x": 4, "y": 0, "playable": True},
    {"label": "f", "x": 0, "y": 1, "playable": True},
    {"label": "g", "x": 1, "y": 1, "playable": True},
    {"label": "h", "x": 2, "y": 1, "playable": True},
    {"label": "i", "x": 3, "y": 1, "playable": True},
    {"label": "j", "x": 4, "y": 1, "playable": True},
    {"label": "k", "x": 0, "y": 2, "playable": True},
    {"label": "l", "x": 1, "y": 2, "playable": True},
    {"label": "m", "x": 2, "y": 2, "playable": True},
    {"label": "n", "x": 3, "y": 2, "playable": True},
    {"label": "o", "x": 4, "y": 2, "playable": True},
    {"label": "-", "x": 0, "y": 3, "playable": False},
    {"label": "1", "x": 1, "y": 3, "playable": True},
    {"label": "2", "x": 2, "y": 3, "playable": True},
    {"label": "3", "x": 3, "y": 3, "playable": True},
    {"label": "-", "x": 4, "y": 3, "playable": False},
]

HEIGHT = 4
WIDTH = 5
CNT = 10
VOWELS = 2


def main():
    """Run find-my-number."""
    data = []
    for pos in POSITIONS:
        p = Position(pos["x"], pos["y"], pos["label"], pos["playable"])
        data.append(p)
    my_board = Board(WIDTH, HEIGHT, data)
    my_board.show_board()

    total_paths = []
    for p in [pos for pos in data if pos.playable]:
        starting_position = p
        logger.info("Starting Position: %s", starting_position.label)
        moves = starting_position.knight_move(my_board)
        starting_path = Path()
        paths = [starting_path.add_move(starting_position)]

        for _ in range(CNT - 1):
            new_paths = []
            for path in paths:
                moves = path.last_position.knight_move(my_board)

                for move in moves:
                    valid_new_path = path.check_move(move, CNT, VOWELS)
                    if valid_new_path:
                        new_paths.append(path.clone().add_move(move))

            paths = new_paths

        total_paths.append([path for path in paths if path.length == CNT])

    final_paths = [item for sublist in total_paths for item in sublist]

    logger.info("Total Number of valid Paths: %s", len(final_paths))

    index = random.choice(range(len(final_paths)))  # noqa: S311

    logger.info("Example Path: %s", [move.label for move in final_paths[index].moves])


if __name__ == "__main__":
    main()
