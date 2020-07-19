#! /usr/bin/python3.6

"""

    Example 10:

    Loop through a CATProduct and analyse children if CATPart.
    Only goes two levels deep.

"""

from pycatia import catia
from pycatia.enumeration.enumeration_types import cat_work_mode_type

documents = catia.documents
documents.open(r'tests\cat_files\product_top.CATProduct')

document = catia.active_document
product = document.product()

# Change the work mode to Design Mode.
# This is useful for CATIA configurations that work with a cache otherwise methods on children may fail
# due to the document not being loaded.
product.apply_work_mode(cat_work_mode_type.index("DESIGN_MODE"))


def print_properties(obj):
    print(f"{obj.name}: mass: {obj.analyze.mass}, \n"
          f"    volume: {obj.analyze.volume}, \n"
          f"    wet_area: {obj.analyze.wet_area}, \n"
          f"    gravity_center: {obj.analyze.get_gravity_center()}, \n"
          f"    inertia: {obj.analyze.get_inertia()}"
          )


# I know, this isn't pretty, but my intent is to keep examples simple.
for sub_product in product.get_products():

    if sub_product.is_catproduct():

        for child_product in sub_product.get_products():

            if child_product.is_catpart():
                child_product.activate_default_shape()
                print_properties(child_product)

    else:

        sub_product.activate_default_shape()
        print_properties(sub_product)
