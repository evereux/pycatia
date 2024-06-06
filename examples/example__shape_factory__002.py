#! /usr/bin/python3.9

"""

    Example - Shape Factory - 002

    Description:
        Mirror the main body of the part.

    Requirements:
        - CATIA running with an open part with an non-empty main body.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.mec_mod_interfaces.part_document import PartDocument

caa = catia()
# if the active document is a CATPart this will return a PartDocument
part_document: PartDocument = caa.active_document
part = part_document.part
part.in_work_object = part.main_body

mirror_reference = part.create_reference_from_object(part.origin_elements.plane_zx)
shape_factory = part.shape_factory
mirror_symmetry = shape_factory.add_new_symmetry_2(mirror_reference)
mirror_symmetry.hybrid_shape

part.in_work_object = part.main_body
part.update_object(part.main_body)
