"""The hello world cli app."""

import logging
from sys import stdout


def main() -> None:
    """Run the main script.

    Examples:
    >>> main()

    """
    logger: logging.Logger = logging.getLogger(__name__)
    logging.basicConfig(
        stream=stdout,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(pathname)s:%(lineno)d] %(message)s",
    )
    logger.info("Hello, world!")
    logger.warning("Bye, world!")


if __name__ == "__main__":  # pragma: no cover
    main()
