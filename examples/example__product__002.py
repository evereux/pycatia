#! /usr/bin/python3.9

"""

    Example - Product - 002

    Description:
        Move the first child in product.

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
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.product_document import ProductDocument

caa = catia()
documents = caa.documents
product_document: ProductDocument = documents.open(Path(os.getcwd(), r"tests\cat_files\product_top.CATProduct"))
product = product_document.product

# Change the work mode to Design Mode.
# This is useful for CATIA configurations that work with a cache otherwise methods on children may fail
# due to the document not being loaded.
product.apply_work_mode(cat_work_mode_type.index("DESIGN_MODE"))

# Transformation matrix (45 degrees-rotation around the x axis and a translation).
transformation = (1.000, 0, 0, 0, 0.707, 0.707, 0, -0.707, 0.707, 10.000, 20.000, 30.000)

# activates default shape on all children.
Product.activate_terminal_node(product.products)

# move the first child in parent.
product = product.products[0]
move = product.move.apply(transformation)
