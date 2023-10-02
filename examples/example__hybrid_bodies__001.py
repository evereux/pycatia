#! /usr/bin/python3.9

"""

    Example - Hybrid Bodies - 001

    Description:
        You have two bodies named Body.Cube.1 and Body.Cube.2.
        Body.Cube.1 is made the in work object.
        Body.Cube.2 is intersected with Body.Cube.1

    Requirements:
        - An open part document with two bodies:
        
            Part
            |- Body.Cube.1
            |- Body.Cube.2

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.mec_mod_interfaces.body import Body
from pycatia.mec_mod_interfaces.part import Part
from pycatia.mec_mod_interfaces.part_document import PartDocument

caa = catia()
document = PartDocument(caa.active_document.com_object)
part = Part(document.part.com_object)
bodies = part.bodies
# Note: It's not necessary to explicitly use the PartDocument or the Part class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   part = document.part
# But declaring 'document' and 'part' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688

# Warning: if you have several bodies with the same name the first will always be chosen.
body_cube_1_item = bodies.get_item_by_name("Body.Cube.1")
assert isinstance(body_cube_1_item, Body)
body_cube_1 = Body(body_cube_1_item.com_object)

body_cube_2_item = bodies.get_item_by_name("Body.Cube.2")
assert isinstance(body_cube_2_item, Body)
body_cube_2 = Body(body_cube_2_item.com_object)

part.in_work_object = body_cube_1
shapes_body_cube_1 = body_cube_1.shapes
hybrid_bodies_cube_1 = body_cube_1.hybrid_bodies
hybrid_shapes_cube_1 = body_cube_1.hybrid_shapes

shape_factory = part.shape_factory
shape_factory.add_new_add(body_cube_2)
