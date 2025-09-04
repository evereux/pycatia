#! /usr/bin/python3.9

"""

    Example - Parameters - 002

    Description:
        Change the Length value of parameter named Thickness.

    Requirements:
        - A CATPart open that contains a length parameter named Thickness.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument

# from pycatia.knowledge_interfaces import BoolParam

application = catia()
part_document: PartDocument = application.active_document
part = part_document.part

product = part_document.product

# gets the parameters collection
parameters = part.parameters

# get parameter named Thickness
thickness = parameters.item("Thickness")
# check it's the expected parameter type
if type(thickness) is Length:
    thickness.value = 80
    part.update()
