#! /usr/bin/python3.6

"""

    Example 10:

    Loop through a CATProduct and analyse children if CATPart.
    Only goes two levels deep.

"""

from pycatia.base_interfaces import CATIAApplication

catia = CATIAApplication()

documents = catia.documents()
documents.open(r'tests\CF_TopLevelAssy.CATProduct')

document = catia.document()
top_product = document.product()

# Change the work mode to Design Mode.
# This is useful for CATIA configurations that work with a cache otherwise methods on children may fail
# due to the document not being loaded.
top_product.apply_work_mode("DESIGN_MODE")


def print_properties(product):
    print(f"{product.name}: mass: {product.analyze.mass}, \n"
          f"    volume: {product.analyze.volume}, \n"
          f"    wet_area: {product.analyze.wet_area}, \n"
          f"    gravity_center: {product.analyze.get_gravity_center(catia)}, \n"
          f"    inertia: {product.analyze.get_inertia(catia)}"
          )


# I know, this isn't pretty, but my intent is to keep examples simple.
for sub_product in top_product.get_products():

    if sub_product.is_catproduct():

        for child_product in sub_product.get_products():

            if child_product.is_catpart():
                child_product.activate_default_shape()
                print_properties(child_product)

    else:

        sub_product.activate_default_shape()
        print_properties(sub_product)
