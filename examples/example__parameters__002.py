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
from pycatia.mec_mod_interfaces.part import Part
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product import Product

# from pycatia.knowledge_interfaces import BoolParam

caa = catia()
documents = caa.documents

document = PartDocument(caa.active_document.com_object)
product = Product(document.product.com_object)
part = Part(document.part.com_object)
# Note: It's not necessary to explicitly use the PartDocument or the Part class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   part = document.part
# But declaring 'document' and 'part' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688

# gets the parameters collection
parameters = part.parameters

# get parameter named Thickness
thickness = parameters.get_item_by_name(f"{product.part_number}\\Thickness")
# initialise the length parameter
length = Length(thickness.com_object)

length.value = 80
part.update()
