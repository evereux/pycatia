import logging
import sys

from typing import Optional

# the following code was shamefully pilfered from Flask's logging.


def has_level_handler(logger: Optional[logging.Logger]):
    """

    Check if there is a handler in the logging chain that will handle the
    given logger's :meth:`effective level <~logging.Logger.getEffectiveLevel>`

    :param logger: logging.Logger
    :return:
    """
    """
        Check if there is a handler in the logging chain that will handle the
        given logger's :meth:`effective level <~logging.Logger.getEffectiveLevel>`.
    
    """
    level = logger.getEffectiveLevel()
    current = logger

    while current:
        if any(handler.level <= level for handler in current.handlers):
            return True

        if not current.propagate:
            break

        current = current.parent

    return False


def create_logger() -> logging.Logger:
    """

    :return: Logger
    :rtype: logging.Logger
    """

    #: ``[%(asctime)s] %(levelname)s in %(module)s: %(message)s``.
    default_handler = logging.StreamHandler(sys.stderr)
    default_handler.setFormatter(
        logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
    )

    logger = logging.getLogger('pycatia')

    logger.setLevel(logging.INFO)
    
    # clear existed Handlers
    logger.handlers.clear()
    
    logger.addHandler(default_handler)

    return logger
