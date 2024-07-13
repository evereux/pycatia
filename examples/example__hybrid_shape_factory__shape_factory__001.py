#! /usr/bin/python3.9

"""

    Example - Hybrid Shape Factory & Shape Factory - 001

    Description:
        3D Points, Spline, Extrusion and Generate Thickness.

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
from pycatia.product_structure_interfaces.product_document import ProductDocument

caa = catia()
documents = caa.documents
part_document: PartDocument = documents.add("Part")

product_document = ProductDocument(caa.active_document.com_object)
product = product_document.product

part = part_document.part

hybrid_shape_factory = part.hybrid_shape_factory
part_shape_factory = part.shape_factory
body = part.main_body

# create the hybrid bodies (Geometrical Set) to add our construction.
hybrid_bodies = part.hybrid_bodies
hybrid_body_points = hybrid_bodies.add()
hybrid_body_splines = hybrid_bodies.add()
hybrid_body_surface = hybrid_bodies.add()
hybrid_body_points.name = "construction_points"
hybrid_body_splines.name = "construction_splines"
hybrid_body_surface.name = "construction_surfaces"

# create the hybrid shape 'points'
point_1 = hybrid_shape_factory.add_new_point_coord(0, 0, 0)
point_1_reference = part.create_reference_from_object(point_1)
point_2 = hybrid_shape_factory.add_new_point_coord(10, 5, 0)
point_2_reference = part.create_reference_from_object(point_2)
point_3 = hybrid_shape_factory.add_new_point_coord(20, 0, 0)
point_3_reference = part.create_reference_from_object(point_3)
point_4 = hybrid_shape_factory.add_new_point_coord(30, 5, 0)
point_4_reference = part.create_reference_from_object(point_4)
point_5 = hybrid_shape_factory.add_new_point_coord(40, 0, 0)
point_5_reference = part.create_reference_from_object(point_5)

# add the points to 'construction_points'
hybrid_body_points.append_hybrid_shape(point_1)
hybrid_body_points.append_hybrid_shape(point_2)
hybrid_body_points.append_hybrid_shape(point_3)
hybrid_body_points.append_hybrid_shape(point_4)
hybrid_body_points.append_hybrid_shape(point_5)

# create the spline
spline = hybrid_shape_factory.add_new_spline()
spline.add_point(point_1_reference)
spline.add_point(point_2_reference)
spline.add_point(point_3_reference)
spline.add_point(point_4_reference)
spline.add_point(point_5_reference)
spline_reference = part.create_reference_from_object(spline)

hybrid_body_splines.append_hybrid_shape(spline)

# create the extrusion
# plane used to define direction
plane = part.origin_elements.plane_xy
plane_reference = part.create_reference_from_object(plane)
# have to create a direction object for extrusion.
direction = hybrid_shape_factory.add_new_direction(plane_reference)
extrusion = hybrid_shape_factory.add_new_extrude(
    spline_reference, i_offset_debut=10, i_offset_fin=10, i_direction=direction
)
extrusion_reference = part.create_reference_from_object(extrusion)
hybrid_body_surface.append_hybrid_shape(extrusion)

main_body = part.main_body
part.in_work_object = main_body
part_shape_factory.add_new_thick_surface(extrusion_reference, 1, 5, 0)

part.update()
