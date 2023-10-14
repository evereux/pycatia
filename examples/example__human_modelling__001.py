#! /usr/bin/python3.9

"""
    Example - Human Modelling 001

    Description:
        Add a female manikin to the product in the sitting position.

    Requirements:
        - An open product document.
"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.enumeration.enumeration_types import swk_anthro_sex
from pycatia.enumeration.enumeration_types import swk_posture_spec
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.product_document import ProductDocument
from pycatia.dnb_human_modeling_interfaces.swk_hmi_workbench import SWKHmiWorkbench

caa = catia()
document = ProductDocument(caa.active_document.com_object)
product = Product(document.product.com_object)
# Note: It's not necessary to explicitly use the ProductDocument or the Product class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   product = document.product
# But declaring 'document' and 'product' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688


human_work_bench = SWKHmiWorkbench(product.get_technological_object("HumanWorkbench"))
gender = swk_anthro_sex.index("Female")
manikin = human_work_bench.create_manikin("Manikin1", gender, 50, 1)
sit = swk_posture_spec.index("SWKPostureSpecSit")
manikin.body.set_posture(sit, True)

print(manikin.anthro.gender)
