#! /usr/bin/python3.9

"""

    Example - Product - 005

    Description:
        Loop through a CATProduct and find if sub component is a CATPart or CATProduct.

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
from pycatia.enumeration.enumeration_types import cat_work_mode_type
from pycatia.product_structure_interfaces.product_document import ProductDocument

caa = catia()
documents = caa.documents
product_document: ProductDocument = documents.open(Path(os.getcwd(), r"tests/cat_files/product_top.CATProduct"))
product = product_document.product
# Change the work mode to Design Mode.
# This is useful for CATIA configurations that work with a cache otherwise
# methods on children may fail due to the document not being loaded.
product.apply_work_mode(cat_work_mode_type.index("DESIGN_MODE"))

products = product.products

if len(products) == 0:
    print("Active document has no children or is not a CATProduct.")

for item in products:
    if item.is_catpart():
        print(f'This is a part: "{item}"')
        print("")

    if item.is_catproduct():
        product = item
        print(f'This is a product: "{item}"')

        if item.has_children():
            print("This product has children.")
            children = item.get_children()
            print(children)
        print("")
