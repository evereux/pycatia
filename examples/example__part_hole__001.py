#! /usr/bin/python3.9

"""

    Example - Part Hole 001

    Description:
        Find all the Hole(s) in the active CATPart document and report it's origin
        and direction (relative to origin).

    Requirements:
        - CATIA running.
        - A CATPart open that contains a PartBody with Hole(s).

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
from pycatia.part_interfaces.hole import Hole

caa = catia()
application = caa.application
part_document: PartDocument = application.active_document
part = part_document.part
selection = part_document.selection
selection.clear()
# search the entire CATPart for all Holes belonging to the Part Design workbench.
selection.search("'Part Design'.Hole,all")

# collect the co-ordinates into a list so we can draw the points afterwards
# to visually check results.
points = []

for feature in range(selection.count):
    n = feature + 1
    auto_object = selection.item2(n).value
    reference = part.create_reference_from_object(auto_object)

    hole = Hole(auto_object.com_object)
    origin = hole.get_origin()
    direction = hole.get_direction()
    print(f"Name: {selection.item2(n).value.name}")
    print("Hole origin: \n"
          f"x = {origin[0]}\n"
          f"y = {origin[1]}\n"
          f"z = {origin[2]}")
    print("Direction: \n"
          f"x = {direction[0]}\n"
          f"y = {direction[1]}\n"
          f"z = {direction[2]}\n")

    points.append((origin, direction))

selection.clear()

# create a new Geometrical Set called "Points" to which the origin and direction
# points will be added.
hybrid_bodies = part.hybrid_bodies
hb_points = hybrid_bodies.add()
hb_points.name = "Points"

hsf = part.hybrid_shape_factory

for p in points:
    origin = p[0]
    direction = p[1]

    point_origin = hsf.add_new_point_coord(origin[0], origin[1], origin[2])
    point_origin_reference = part.create_reference_from_object(point_origin)
    hb_points.append_hybrid_shape(point_origin)

    point_direction = hsf.add_new_point_coord_with_reference(
        direction[0],
        direction[1],
        direction[2],
        point_origin_reference
    )

    hb_points.append_hybrid_shape(point_direction)

part.update()
