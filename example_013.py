#! /usr/bin/python3.6

"""

    Example 13:

    3D Points, Spline, Extrusion and Generate Thickness.

"""
from pycatia import catia

# create a new part and rename.
documents = catia.documents
documents.add('Part')
document = catia.active_document

part = catia.active_document.part()
product = catia.active_document.product()
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
point_2 = hybrid_shape_factory.add_new_point_coord(10, 5, 0)
point_3 = hybrid_shape_factory.add_new_point_coord(20, 0, 0)
point_4 = hybrid_shape_factory.add_new_point_coord(30, 5, 0)
point_5 = hybrid_shape_factory.add_new_point_coord(40, 0, 0)

# add the points to 'construction_points'
hybrid_body_points.append_hybrid_shape(point_1)
hybrid_body_points.append_hybrid_shape(point_2)
hybrid_body_points.append_hybrid_shape(point_3)
hybrid_body_points.append_hybrid_shape(point_4)
hybrid_body_points.append_hybrid_shape(point_5)

# create the spline
spline = hybrid_shape_factory.add_new_spline()
spline.add_point(point_1)
spline.add_point(point_2)
spline.add_point(point_3)
spline.add_point(point_4)
spline.add_point(point_5)

hybrid_body_splines.append_hybrid_shape(spline)

# create the extrusion
# plane used to define direction
plane = part.origin_elements.plane_xy
# have to create a direction object for extrusion.
direction = hybrid_shape_factory.add_new_direction(plane)
extrusion = hybrid_shape_factory.add_new_extrude(spline, i_offset_debut=10, i_offset_fin=10, i_direction=direction)
hybrid_body_surface.append_hybrid_shape(extrusion)

main_body = part.main_body
part.in_work_object = main_body
part_shape_factory.add_new_thick_surface(extrusion, 1, 5, 0)

part.update()
