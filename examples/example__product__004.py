#! /usr/bin/python3.9

"""

    Example - Product - 004:

    Get the position matrix of products (CATPart or CATProduct) in product.

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

caa = catia()
documents = caa.documents
documents.open(r"tests\cat_files\product_top.CATProduct")
document = ProductDocument(caa.active_document.com_object)
product = Product(document.product.com_object)
# Note: It's not necessary to explicitly use the ProductDocument or the Product class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   product = document.product
# But declaring 'document' and 'product' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688

products = product.products

for product in products:
    print(product.position.get_components())
    # print(product.name, position.get_components())

document.close()
