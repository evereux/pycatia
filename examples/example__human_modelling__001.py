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
from pycatia.product_structure_interfaces.product_document import ProductDocument
from pycatia.dnb_human_modeling_interfaces.swk_hmi_workbench import SWKHmiWorkbench

caa = catia()
# if the active document is a CATProduct this will return a ProductDocument
product_document: ProductDocument = caa.active_document
product = product_document.product

human_work_bench = SWKHmiWorkbench(product.get_technological_object("HumanWorkbench"))
gender = swk_anthro_sex.index("Female")
manikin = human_work_bench.create_manikin("Manikin1", gender, 50, 1)
sit = swk_posture_spec.index("SWKPostureSpecSit")
manikin.body.set_posture(sit, True)

print(manikin.anthro.gender)
