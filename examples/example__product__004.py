#! /usr/bin/python3.9

"""

    Example - Product - 004

    Description:
        Get the position matrix of products (CATPart or CATProduct) in product.

    Requirements:
        - CATIA running.
        - Tests already setup.
    
"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################
from pathlib import Path

from pycatia import catia
from pycatia.product_structure_interfaces.product_document import ProductDocument

caa = catia()
documents = caa.documents
product_document: ProductDocument = documents.open(Path(os.getcwd(), r"tests\cat_files\product_top.CATProduct"))
product = product_document.product

products = product.products

for product in products:
    print(product.position.get_components())
    # print(product.name, position.get_components())

product_document.close()
