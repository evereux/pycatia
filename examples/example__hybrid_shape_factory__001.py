#! /usr/bin/python3.9

"""

    Example - Hybrid Shape Factory - 001:

    Sequentially rename all points in geometric set (hybrid body) Points in the geometric set MasterGeometry.

    Part
       |- MasterGeometry
         |- Points

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
document = caa.active_document
part = document.part

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

    # make sure the element is indeed a point.
    if hsf.get_geometrical_feature_type(hybrid_shape) == 1:
        points.append(hs_shapes.item(i))

# sequentially rename the points starting from 1.
point_post_fix = 1
for point in points:
    point.name = f"Point.{point_post_fix}"
    point_post_fix += 1
