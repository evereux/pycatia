#! /usr/bin/python3.9

"""

    Example - Hybrid Shape Factory - 004

    Description:
        Loops through the items in hybrid body "Lines" and determine the object type using selection.
        Once determined create an object from it and find it's parent(s).

    Requirements:
        - An active part document open with a geometrical set called "construction_geometry" containing points
          generated using HybridShapePtCoord and line generated using HybridShapeLinePtPt:

            Part
            |- MasterGeometry
                |- Points

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pycatia import catia
from pycatia.hybrid_shape_interfaces.hybrid_shape_line_pt_pt import HybridShapeLinePtPt
from pycatia.hybrid_shape_interfaces.hybrid_shape_point_coord import (
    HybridShapePointCoord,
)
from pycatia.mec_mod_interfaces.part import Part
from pycatia.mec_mod_interfaces.part_document import PartDocument

caa = catia()
document = PartDocument(caa.active_document.com_object)
part = Part(document.part.com_object)
# Note: It's not necessary to explicitly use the PartDocument or the Part class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   part = document.part
# But declaring 'document' and 'part' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688

hbs = part.hybrid_bodies
hb_construction_lines = hbs.item("construction_geometry")
hss = hb_construction_lines.hybrid_shapes

for shape_index in range(1, hss.count + 1):
    hs = hss.item(shape_index)

    # clear the selection on each loop.
    document.selection.clear()
    # add the shape to the selection.
    document.selection.add(hs)
    # create the selected element by getting the first item in the document selection.
    selected_elem = document.selection.item(1)

    # test part only has HybridShapeLinePtPt
    if selected_elem.type == "HybridShapeLinePtPt":
        # to create the HybridShapeLinePtPt object we need to use the hybrid_shape com_object.
        hs_line_pt_pt = HybridShapeLinePtPt(hs.com_object)

        ref_start_point = hs_line_pt_pt.pt_origin
        ref_end_point = hs_line_pt_pt.pt_extremity

        start_point = HybridShapePointCoord(hss.item(ref_start_point.display_name).com_object)
        end_point = HybridShapePointCoord(hss.item(ref_end_point.display_name).com_object)

        print(hs_line_pt_pt.name)
        print(start_point.name, start_point.get_coordinates())
        print(end_point.name, end_point.get_coordinates())
