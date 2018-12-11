#! /usr/bin/python3.6


class PYCATIABaseException(Exception):
    """
    PYCATIABaseException class.
    """
    pass


class CATIAApplicationException(PYCATIABaseException):
    """

    """

    def __init__(self, message):
        """

        :param message:
        """

        self.message = message
