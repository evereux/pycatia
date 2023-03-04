#! /usr/bin/python3.9

"""

    Example - Prodcut - 006:

    Get the Inertia of a product using product.get_technical object and print
    it's mass.

    See Inertia class for full list of properties and methods available.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pycatia import catia
from pycatia.product_structure_interfaces.product import Product
from pycatia.space_analyses_interfaces.inertia import Inertia

caa = catia()
document = caa.active_document
product = Product(document.product.com_object)
inertia_com = product.get_technological_object("Inertia")
inertia = Inertia(inertia_com)

print(inertia.mass)
