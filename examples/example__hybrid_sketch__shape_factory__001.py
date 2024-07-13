#! /usr/bin/python3.9

"""

    Example - Hybrid Sketch & Shape Factory - 001

    Description:
        Creates a square in a sketch and fully constrains it. Sketch then used to pad.

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
from pycatia.enumeration.enumeration_types import cat_constraint_type
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.sketcher_interfaces.geometry_2D import Geometry2D

caa = catia()
documents = caa.documents
part_document: PartDocument = documents.add("Part")
part = part_document.part

hsf = part.hybrid_shape_factory

hbs = part.hybrid_bodies
geom_set = hbs.add()
geom_set.name = "Construction Geometry"

# create a point at 0, 0, 0. This will be used to position square inside sketch.
co_ord = (0, 0, 0)
point_1_3D = hsf.add_new_point_coord(co_ord[0], co_ord[1], co_ord[2])
geom_set.append_hybrid_shape(point_1_3D)
# update the part otherwise point can't be referenced in sketch.
part.update()

# plane for sketch positioning
xy_plane = part.origin_elements.plane_xy
xy_plane_reference = part.create_reference_from_object(xy_plane)
# add the sketch.
sketch = geom_set.hybrid_sketches.add(xy_plane_reference)
# open the sketch for editing.
factory_2D = sketch.open_edition()

# get the h_direction used for constraining the line.
geom_elements = sketch.geometric_elements
abs_axis = geom_elements.item("AbsoluteAxis")

h_direction = Geometry2D(abs_axis.get_item("HDirection").com_object)
h_direction.report_name = 1

v_direction = Geometry2D(abs_axis.get_item("VDirection").com_object)
v_direction.report_name = 2

# create the points for the line.
point_1 = factory_2D.create_point(0, 0)
point_2 = factory_2D.create_point(0, 10)
point_3 = factory_2D.create_point(10, 10)
point_4 = factory_2D.create_point(10, 0)
point_1.report_name = 3
point_2.report_name = 4
point_3.report_name = 5
point_4.report_name = 6

# as the lines start and end points will be set to the points above.
line_1 = factory_2D.create_line(0, 0, 0, 10)
line_2 = factory_2D.create_line(0, 10, 10, 10)
line_3 = factory_2D.create_line(10, 10, 10, 0)
line_4 = factory_2D.create_line(10, 0, 0, 0)
line_1.report_name = 7
line_2.report_name = 8
line_3.report_name = 9
line_4.report_name = 10

line_1.start_point, line_1.end_point = point_1, point_2
line_2.start_point, line_2.end_point = point_2, point_3
line_3.start_point, line_3.end_point = point_3, point_4
line_4.start_point, line_4.end_point = point_4, point_1

# lets start constraining the square.
constraints = sketch.constraints

# create the length constraint.
# left vertical line.
constraint_length_1 = constraints.add_mono_elt_cst(cat_constraint_type.index("catCstTypeLength"), part.create_reference_from_object(line_1))
# horizontal line.
constraint_length_4 = constraints.add_mono_elt_cst(cat_constraint_type.index("catCstTypeLength"), part.create_reference_from_object(line_4))

# make the constraint reference.
# constraint_length_1.mode = cat_constraint_mode.index("catCstModeDrivenDimension")

# # this is how you would change the length of the line via it's constraint.
# length = constraint_length_1.dimension
# length.value = 20

# constrain the bottom line to h_direction
constraint_horizontal = constraints.add_bi_elt_cst(
    cat_constraint_type.index("catCstTypeOn"), part.create_reference_from_object(line_4), part.create_reference_from_object(h_direction)
)

# constrain left vertical as angle to bottom line.
constraint_angle = constraints.add_bi_elt_cst(
    cat_constraint_type.index("catCstTypeAngle"), part.create_reference_from_object(line_1), part.create_reference_from_object(line_4)
)

# make the two horizontal lines parallel.
constraint_p_h = constraints.add_bi_elt_cst(
    cat_constraint_type.index("catCstTypeParallelism"), part.create_reference_from_object(line_1), part.create_reference_from_object(line_3)
)
# make the two vertical lines parallel.
constraint_p_v = constraints.add_bi_elt_cst(
    cat_constraint_type.index("catCstTypeParallelism"), part.create_reference_from_object(line_2), part.create_reference_from_object(line_4)
)

# create projection of 3D point used and constrain to 2d point.
geometric_elements1 = factory_2D.create_projections(part.create_reference_from_object(point_1_3D))
projected_point = Geometry2D(geometric_elements1.item(1).com_object)
projected_point.construction = True
point_ref = part.create_reference_from_object(projected_point)

constraint_mid = constraints.add_bi_elt_cst(cat_constraint_type.index("catCstTypeOn"), part.create_reference_from_object(point_1), point_ref)

sketch.close_edition()

part.update()

# create the pad from sketch
main_body = part.main_body
part.in_work_object = main_body
part_shape_factory = part.shape_factory
part_shape_factory.add_new_pad(sketch, 5)

part.update()
