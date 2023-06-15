#! /usr/bin/python3.9

"""

    Example - Hybrid Shape Factory & Shape Factory - 001:

    3D Points, Spline, Extrusion and Generate Thickness.

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
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.product_document import ProductDocument

caa = catia()
documents = caa.documents
documents.add("Part")

product_document = ProductDocument(caa.active_document.com_object)
product = Product(product_document.product.com_object)

part_document = PartDocument(caa.active_document.com_object)
part = Part(part_document.part.com_object)
# Note: It's not necessary to explicitly use the PartDocument or the Part class
# with the com_object. It's perfectly fine to write it like this:
#   document = caa.active_document
#   part = document.part
# But declaring 'part_document' and 'part' this way, your linter can't resolve the
# product reference, see https://github.com/evereux/pycatia/issues/107#issuecomment-1336195688

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
point_1_reference = Reference(point_1.com_object)
point_2 = hybrid_shape_factory.add_new_point_coord(10, 5, 0)
point_2_reference = Reference(point_2.com_object)
point_3 = hybrid_shape_factory.add_new_point_coord(20, 0, 0)
point_3_reference = Reference(point_3.com_object)
point_4 = hybrid_shape_factory.add_new_point_coord(30, 5, 0)
point_4_reference = Reference(point_4.com_object)
point_5 = hybrid_shape_factory.add_new_point_coord(40, 0, 0)
point_5_reference = Reference(point_5.com_object)

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
spline_reference = Reference(spline.com_object)

hybrid_body_splines.append_hybrid_shape(spline)

# create the extrusion
# plane used to define direction
plane = part.origin_elements.plane_xy
plane_reference = Reference(plane.com_object)
# have to create a direction object for extrusion.
direction = hybrid_shape_factory.add_new_direction(plane_reference)
extrusion = hybrid_shape_factory.add_new_extrude(
    spline_reference, i_offset_debut=10, i_offset_fin=10, i_direction=direction
)
extrusion_reference = Reference(extrusion.com_object)
hybrid_body_surface.append_hybrid_shape(extrusion)

main_body = part.main_body
part.in_work_object = main_body
part_shape_factory.add_new_thick_surface(extrusion_reference, 1, 5, 0)

part.update()
