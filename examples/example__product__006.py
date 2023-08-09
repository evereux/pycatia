#! /usr/bin/python3.9

"""

    Example - Product - 006

    Description:
        Get the Inertia of a product using product.get_technical object and print it's mass.
        See Inertia class for full list of properties and methods available.

    Requirements:
        - An open part document.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.product_document import ProductDocument
from pycatia.space_analyses_interfaces.inertia import Inertia

caa = catia()
document = ProductDocument(caa.active_document.com_object)
product = Product(document.product.com_object)
# Note: It's not necessary to explicitly use the ProductDocument or the Product class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   product = document.product
# But declaring 'document' and 'product' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688

inertia_com = product.get_technological_object("Inertia")
inertia = Inertia(inertia_com)

print(inertia.mass)
