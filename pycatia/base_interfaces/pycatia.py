#! /usr/bin/python3.6

import logging

from pycatia.cat_logger import create_logger


class PyCATIA:
    """
    Base class for the catia application.
    """

    def __init__(self):
        pass

    @property
    def logger(self) -> logging.Logger:
        """
        :return: logging.Logger
        :rtype: logging.Logger
        """
        return create_logger()

    def __repr__(self):
        return 'PyCATIA()'
