#! /usr/bin/python3.9

"""

    The catia base object is from which most other functionality derives. See examples for more information.

    >>> from pycatia import catia
    >>> caa = catia()
    >>> documents = caa.documents
    >>> # documents represents the collection of currently open documents.
    >>> document = caa.active_document
    >>> # document is the currently active document.
    >>>
    >>> # open a new CATPart document
    >>> documents.add('Part')

"""

import os

from pycatia.base_interfaces.base_application import catia_application as catia
from pycatia.base_interfaces.context import CATIADocHandler
from .version import version

__author__ = 'Paul Bourne'
__author_email = 'evereux@gmail.com'
__description__ = 'A python module to interface with the CATIA V5 COM object.'
__name__ = "pycatia"
__version__ = version
__url__ = "https://github.com/evereux/pycatia"

name = __name__
