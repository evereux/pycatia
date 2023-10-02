#! /usr/bin/python3.9

"""

    Example - Hybrid Shape Factory - 001

    Description:
        Sequentially rename all points in geometric set (hybrid body) Points in the geometric set MasterGeometry.

    Requirements:
        - An open part document with the following geometric sets:
        
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
from pycatia.in_interfaces.reference import Reference
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

# initialise the hybrid shape factory. this is used to determine the shape type later.
hsf = part.hybrid_shape_factory

tl_hybrid_bodies = part.hybrid_bodies
# get the hybrid body "MasterGeometry"
hb_master_geometry = tl_hybrid_bodies.item("MasterGeometry")
# get the hybrid bodies in "MasterGeometry"
hbs_master_geometry = hb_master_geometry.hybrid_bodies
# get the hybrid body "Points"
hb_points = hbs_master_geometry.item("Points")
# get all the shapes in hybrid body "Points"
hs_shapes = hb_points.hybrid_shapes

# create a list of only points.
points = []
for i in range(1, hs_shapes.count + 1):
    hybrid_shape = hs_shapes.item(i)
    hybrid_shape_reference = Reference(hybrid_shape.com_object)

    # make sure the element is indeed a point.
    if hsf.get_geometrical_feature_type(hybrid_shape_reference) == 1:
        points.append(hs_shapes.item(i))

# sequentially rename the points starting from 1.
point_post_fix = 1
for point in points:
    point.name = f"Point.{point_post_fix}"
    point_post_fix += 1
