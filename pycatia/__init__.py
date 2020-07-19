#! /usr/bin/python3.6

"""

    The base object from which most other functionality derives. See examples for more information.

    >>> from pycatia import catia
    >>> documents = catia.documents
    >>> # documents represents the collection of currently open documents.
    >>> document = catia.active_document
    >>> # document is the currently active document.
    >>>
    >>> # open a new CATPart document
    >>> documents.add('Part')

"""

import os

from pycatia.base_interfaces.base_application import catia_application
from pycatia.base_interfaces.context import CATIADocHandler

catia = catia_application()

__author__ = 'Paul Bourne'
__author_email = 'evereux@gmail.com'
__description__ = 'A python module to access the CATIA Measurable object.'
__name__ = "pycatia"
__version__ = "0.3.7"
__url__ = "https://github.com/evereux/pycatia"

name = __name__
