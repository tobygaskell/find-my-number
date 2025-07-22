"""Entry point for find-my-number."""

import logging
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
    find = NumberFinder(WIDTH, HEIGHT, CNT, VOWELS)
    find.find_paths()
    logger.info("Total paths found: %d", find.path_cnt)


if __name__ == "__main__":
    logger.info("Starting find-my-number")
    start_time = time.time()
    main()
    end_time = time.time()
    logger.info("Elapsed time: %.2f seconds", end_time - start_time)
