"""Entry point for find-my-number."""

import logging
import random
import time

from objects.find_my_number import NumberFinder

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)

HEIGHT: int = 4
WIDTH: int = 5
CNT: int = 10
VOWELS: int = 2


def main():
    """Run find-my-number (optimized, preserves logic)."""
    logger.info("Starting find-my-number")
    method = input("Bishop or Knight moves? (b/k): ").strip().lower()
    start_time = time.time()
    find = NumberFinder(WIDTH, HEIGHT, CNT, VOWELS, method)
    if method not in ["b", "bishop", "k", "knight"]:
        logger.error("Invalid method selected. Please choose 'b' for Bishop or 'k' for Knight.")
    find.board.show_board()
    find.find_paths()
    logger.info("Total paths found: %d", find.path_cnt)
    logger.info(
        "Example path: %s",
        [move.label for move in find.final_paths[random.choice(range(find.path_cnt))].moves],  # noqa: S311
    )
    end_time = time.time()
    logger.info("Elapsed time: %.2f seconds", end_time - start_time)


if __name__ == "__main__":
    main()
