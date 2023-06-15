#! /usr/bin/python3.9

"""

    Example - Constraints - 001

    Description:
        Fix the first Sub Product in Product using constraints.
        The Sketch examples also show further usage of constraints.

    Requirements:
        - An open product document with at least two parts inside.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.enumeration.enumeration_types import cat_constraint_type
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.product_document import ProductDocument

caa = catia()
document = ProductDocument(caa.active_document.com_object).product
product = Product(document.com_object)
# Note: It's not necessary to explicitly use the ProductDocument or the Product class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   product = document.product
# But declaring 'document' and 'product' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688

products = product.products
constraints = product.constraints()
sub_prod_1 = products.item(1)
ref_sub_prod_1 = sub_prod_1.reference_product

sub_prod_1_name = f"{product.name}/{sub_prod_1.name}/!{product.name}/{sub_prod_1.name}/"
reference = product.create_reference_from_name(sub_prod_1_name)

constraints.add_mono_elt_cst(cat_constraint_type.index("catCstTypeReference"), reference)
