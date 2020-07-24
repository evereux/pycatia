#! /usr/bin/python3.6

"""

    Example 23:

    Fix the first Sub Product in Product using constraints. The Sketch examples
    also show further usage of constraints.

"""

from pycatia import catia
from pycatia.enumeration.enumeration_types import cat_constraint_type

document = catia.active_document

product = document.product()
constraints = product.constraints()

products = product.products
sub_prod_1 = products.item(1)
ref_sub_prod_1 = sub_prod_1.reference_product

sub_prod_1_name = f"{product.name}/{sub_prod_1.name}/!{product.name}/{sub_prod_1.name}/"
reference = product.create_reference_from_name(sub_prod_1_name)

constraints.add_mono_elt_cst(cat_constraint_type.index("catCstTypeReference"), reference)
