# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

"""Module docstring."""

import logging
from sys import stdout


def main():  # noqa: ANN201 (missing-return-type-undocumented-public-function)
    """Run the main script."""
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        stream=stdout,
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s [[%(pathname)s:%(lineno)d]] %(message)s",
    )
    logger.info("Hello, world!")
    logger.warning("Bye, world!")


if __name__ == "__main__":  # pragma: no cover
    main()
