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

caa = catia()
part_document: PartDocument = caa.active_document
part = part_document.part
product_document: ProductDocument = ProductDocument(caa.active_document.com_object)
product = product_document.product

# gets the parameters collection
parameters = part.parameters

# get parameter named Thickness
thickness = parameters.get_item_by_name(f"{product.part_number}\\Thickness")
# initialise the length parameter
length = Length(thickness.com_object)

length.value = 80
part.update()
