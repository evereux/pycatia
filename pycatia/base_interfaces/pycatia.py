#! /usr/bin/python3.6

from pycatia.cat_logger import create_logger


class PyCATIA:

    def __init__(self):
        pass

    @property
    def logger(self):
        return create_logger(self)

    def __repr__(self):
        return 'PyCATIA()'
