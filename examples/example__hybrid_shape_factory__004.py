#! /usr/bin/python3.9

"""

    Example - Hybrid Shape Factory - 004

    Description:
        Loops through the items in hybrid body "ConstructionGeometry" and determine the object type using selection.
        Once determined create an object from it and find it's parent(s).

    Requirements:
        - An active part document open with a geometrical set called "ConstructionGeometry" containing points
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
from pycatia.mec_mod_interfaces.part_document import PartDocument

caa = catia()
# if the active document is a CATPart this will return a PartDocument
part_document: PartDocument = caa.active_document
part = part_document.part

hbs = part.hybrid_bodies
hb_construction_lines = hbs.item("ConstructionGeometry")
gs_construction_geometry = hb_construction_lines.hybrid_shapes

for i in range(len(gs_construction_geometry)):

    shape_index = i + 1

    hs = gs_construction_geometry.item(shape_index)

    # clear the selection on each loop.
    part_document.selection.clear()
    # add the shape to the selection.
    part_document.selection.add(hs)
    # create the selected element by getting the first item in the document selection.
    selected_elem = part_document.selection.item(1)

    # test part only has HybridShapeLinePtPt
    if selected_elem.type == "HybridShapeLinePtPt":
        # to create the HybridShapeLinePtPt object we need to use the hybrid_shape com_object.
        hs_line_pt_pt = HybridShapeLinePtPt(hs.com_object)

        ref_start_point = hs_line_pt_pt.pt_origin
        ref_end_point = hs_line_pt_pt.pt_extremity

        start_point = HybridShapePointCoord(gs_construction_geometry.item(ref_start_point.display_name).com_object)
        end_point = HybridShapePointCoord(gs_construction_geometry.item(ref_end_point.display_name).com_object)

        print(f'Line: {hs_line_pt_pt.name}')
        print(f'\tStart point: {start_point.name, start_point.get_coordinates()}')
        print(f'\tEnd point: end_point.name, end_point.get_coordinates()')
