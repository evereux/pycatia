#! /usr/bin/python3.6

"""

    Example - Hybrid Bodies - 001:

    You have two bodies named Body.Cube.1 and Body.Cube.2.

    Body.Cube.1 is made the in work object.

    Body.Cube.2 is intersected with Body.Cube.1

    Part
       |- Body.Cube.1
       |- Body.Cube.2

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pycatia import catia

caa = catia()
documents = caa.documents

document = caa.active_document
part = document.part
bodies = part.bodies

# warning, if you have several bodies with the same name the first will always be chosen.
body_cube_1 = bodies.get_item_by_name('Body.Cube.1')
body_cube_2 = bodies.get_item_by_name('Body.Cube.2')

part.in_work_object = body_cube_1

shapes_body_cube_1 = body_cube_1.shapes
hybrid_bodies_cube_1 = body_cube_1.hybrid_bodies
hybrid_shapes_cube_1 = body_cube_1.hybrid_shapes

shape_factory = part.shape_factory

shape_factory.add_new_add(body_cube_2)
