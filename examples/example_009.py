#! /usr/bin/python3.6

"""

    Example 9:

    Get the position matrix of products (CATPart or CATProduct) in product.

"""

##########################################################
# insert syspath to project folder so examples can be run.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))

##########################################################

from pycatia import catia

caa = catia()
documents = caa.documents
documents.open(r'tests\cat_files\product_top.CATProduct')
document = caa.active_document

product = document.product()
products = product.products

for product in products:
    print(product.position.get_components())
    # print(product.name, position.get_components())

document.close()
