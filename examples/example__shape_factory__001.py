#! /usr/bin/python3.9

"""

    Example - Shape Factory - 001:

    Add new bodies to part.
    Create a cylinder in an added body.
    Do Intersection operations between two bodies.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.mec_mod_interfaces.part import Part


caa = catia()
documents = caa.documents
documents.add("Part")
document = caa.active_document
part = document.part
# not neccessary but will provide autocompletion in IDEs.
part = Part(part.com_object)
shape_factory = part.shape_factory

# add new bodies
bodies = part.bodies
body_1 = bodies.add()
body_1.name = "Body.Cylinder.1"
body_2 = bodies.add()
body_2.name = "Body.Cylinder.2"
body_3 = bodies.add()
body_3.name = "Body.Empty"

# create a cylinder in body_1
sketches_body_1 = body_1.sketches
origin_elements = part.origin_elements
reference_xy = origin_elements.plane_xy
sketch_body_1 = sketches_body_1.add(reference_xy)

part.in_work_object = sketch_body_1
factory_2d = sketch_body_1.open_edition()
circle = factory_2d.create_closed_circle(0, 0, 5)
sketch_body_1.close_edition()

length = 5
shape_factory.add_new_pad(sketch_body_1, length)
part.update()

# create a cylinder in body_2
sketches_body_2 = body_2.sketches
origin_elements = part.origin_elements
reference_xy = origin_elements.plane_xy
sketch_body_2 = sketches_body_2.add(reference_xy)

part.in_work_object = sketch_body_2
factory_2d = sketch_body_2.open_edition()
circle = factory_2d.create_closed_circle(3, 0, 5)
sketch_body_2.close_edition()

length = 5
shape_factory.add_new_pad(sketch_body_2, length)
part.update()

# warning, if you have several bodies with the same name the first will always be chosen.
body_cylinder_1 = bodies.get_item_by_name("Body.Cylinder.1")
body_cylinder_2 = bodies.get_item_by_name("Body.Cylinder.2")

# Noting, the VBA example uses
# ‘CATIA.ActiveDocument.Part.CurrentShape = Pad1‘
# to make Pad1 the current shape,
# while there is no current_shape attribute in pycatia.mec_mod_interfaces.part.
# Using the in_work_object attribute can get the same effect.
part.in_work_object = body_cylinder_1

# intersect body_cylinder_1 with body_cylinder_2
shape_factory.add_new_intersect(body_cylinder_2)

part.update()
