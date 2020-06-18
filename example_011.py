#! /usr/bin/python3.6

"""

    Example 11:

    Move the first child in product.

"""

from pycatia import catia
from pycatia.enumeration.enumeration_types import cat_work_mode_type
from pycatia.product_structure_interfaces.product import Product

documents = catia.documents
documents.open(r'cat_files\CF_TopLevelAssy.CATProduct')

document = catia.active_document
product = document.product()

# Change the work mode to Design Mode.
# This is useful for CATIA configurations that work with a cache otherwise methods on children may fail
# due to the document not being loaded.
product.apply_work_mode(cat_work_mode_type.index("DESIGN_MODE"))

# Transformation matrix (45 degrees-rotation around the x axis and a translation).
transformation = (
    1.000,
    0,
    0,
    0,
    0.707,
    0.707,
    0,
    -0.707,
    0.707,
    10.000,
    20.000,
    30.000
)

# activates default shape on all children.
Product.activate_terminal_node(product.get_products())

# move the first child in parent.
product = product.get_products()[0]
move = product.move.apply(transformation)
