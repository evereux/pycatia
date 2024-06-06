#! /usr/bin/python3.9

"""

    Example - Product - 003

    Description:
        Loop through a CATProduct and analyse children if CATPart.
        Only goes two levels deep.

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


def print_properties(obj: Product):
    print(
        f"{obj.name}: mass: {obj.analyze.mass}, \n"
        f"    volume: {obj.analyze.volume}, \n"
        f"    wet_area: {obj.analyze.wet_area}, \n"
        f"    gravity_center: {obj.analyze.get_gravity_center()}, \n"
        f"    inertia: {obj.analyze.get_inertia()}"
    )


# I know, this isn't pretty, but my intent is to keep examples simple.
for sub_product in product.products:
    if sub_product.is_catproduct():
        for child_product in sub_product.products:
            if child_product.is_catpart():
                child_product.activate_default_shape()
                print_properties(child_product)

    else:
        sub_product.activate_default_shape()
        print_properties(sub_product)
