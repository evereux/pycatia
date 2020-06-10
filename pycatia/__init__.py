#! /usr/bin/python3.6

import os

from pycatia.base_interfaces.base_application import catia_application
from pycatia.base_interfaces.context import CATIADocHandler

catia = catia_application()

__author__ = 'Paul Bourne'
__author_email = 'evereux@gmail.com'
__description__ = 'A python module to access the CATIA Measurable object.'
__name__ = "pycatia"
__version__ = "0.3.0a"
__url__ = "https://github.com/evereux/pycatia"

name = __name__

macro_path = os.path.join(os.path.realpath(__file__), r'macros')
