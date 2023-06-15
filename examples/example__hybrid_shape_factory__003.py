#! /usr/bin/python3.9

"""

    Example - Hybrid Shape Factory - 003:

    Draw a line between two points.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.part import Part
from pycatia.mec_mod_interfaces.part_document import PartDocument

caa = catia()
documents = caa.documents
documents.add("Part")
document = PartDocument(caa.active_document.com_object)
part = Part(document.part.com_object)
# Note: It's not necessary to explicitly use the PartDocument or the Part class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   part = document.part
# But declaring 'document' and 'part' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688

hybrid_bodies = part.hybrid_bodies
hsf = part.hybrid_shape_factory

# create a new hybrid body.
geom_set = hybrid_bodies.add()
geom_set.name = "Construction_Geometry"

co_ord_1 = (0, 0, 0)
co_ord_2 = (100, 0, 0)
point_1 = hsf.add_new_point_coord(co_ord_1[0], co_ord_1[1], co_ord_1[2])
point_1_reference = Reference(point_1.com_object)
point_2 = hsf.add_new_point_coord(co_ord_2[0], co_ord_2[1], co_ord_2[2])
point_2_reference = Reference(point_2.com_object)

geom_set.append_hybrid_shape(point_1)
geom_set.append_hybrid_shape(point_2)

line = hsf.add_new_line_pt_pt(point_1_reference, point_2_reference)

geom_set.append_hybrid_shape(line)

part.update()
