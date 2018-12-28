#! /usr/bin/python3.6

from .catiaapplication import CATIAApplication
from .csv_tools import create_points
from .document import Document
from .document import Documents
from .general_functions import create_measurable
from .general_functions import run_system_service
from .hybridshapefactory import HybridShapeFactory
from .measurable import CATIAMeasurable
from .part import Part
from .product import Product
from .reference import create_reference
from .workbenches import create_spa_workbench


__author__ = 'Paul Bourne'
__author_email = 'evereux@gmail.com'
__description__ = 'A python module to access the CATIA Measurable object.'
__name__ = "pycatia"
__version__ = "0.0.3"
__url__ = "https://github.com/evereux/pycatia"

name = __name__
