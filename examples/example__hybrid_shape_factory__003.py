#! /usr/bin/python3.9

"""

    Example - Hybrid Shape Factory - 003

    Description:
        Draws a line between two points.

    Requirements:
        - CATIA running.

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
documents = caa.documents
part_document: PartDocument = documents.add("Part")
part = part_document.part

hybrid_bodies = part.hybrid_bodies
hsf = part.hybrid_shape_factory

# create a new hybrid body.
geom_set = hybrid_bodies.add()
geom_set.name = "Construction_Geometry"

co_ord_1 = (0, 0, 0)
co_ord_2 = (100, 0, 0)
point_1 = hsf.add_new_point_coord(co_ord_1[0], co_ord_1[1], co_ord_1[2])
point_1_reference = part.create_reference_from_object(point_1)

point_2 = hsf.add_new_point_coord(co_ord_2[0], co_ord_2[1], co_ord_2[2])
point_2_reference = part.create_reference_from_object(point_2)

geom_set.append_hybrid_shape(point_1)
geom_set.append_hybrid_shape(point_2)

line = hsf.add_new_line_pt_pt(point_1_reference, point_2_reference)

geom_set.append_hybrid_shape(line)

part.update()
