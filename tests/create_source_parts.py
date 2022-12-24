import os
from pathlib import Path

from pycatia.enumeration.enumeration_types import cat_constraint_mode
from pycatia.enumeration.enumeration_types import cat_constraint_type
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument
from tests.common_vars import caa
from tests.common_vars import test_files

source_cat_part_measurable = Path(os.getcwd(), test_files, "part_measurable.CATPart")

geom_set_arcs = "construction_arcs"
geom_set_cylinders = "construction_cylinders"
geom_set_lines = "construction_lines"
geom_set_planes = "construction_planes"
geom_set_points = "construction_points"
geom_set_sketches = "construction_sketches"
geom_set_splines = "construction_splines"
geom_set_surfaces = "construction_surfaces"


def create_cat_part_measurable(file_name):
    documents = caa.documents
    documents.add("Part")

    document = caa.active_document
    document.save_as(file_name)
    product = ProductDocument(document.com_object).product
    product.part_number = "cat_part_measurable"
    product.revision = "A.1"
    product.nomenclature = "pycatia part for testing"
    product.definition = "pycatia part for testing"
    part = PartDocument(document.com_object).part

    pad_width = 100
    pad_height = 100
    pad_depth = 50

    # ######################## #
    # initialise the factories #
    # ######################## #
    hybrid_shape_factory = part.hybrid_shape_factory
    hybrid_bodies = part.hybrid_bodies
    part_shape_factory = part.shape_factory
    part_parameters = part.parameters

    # ######################### #
    # initialise the parameters #
    # ######################### #

    part_parameters.create_boolean("Activate", True)
    dim_pad_width = part_parameters.create_dimension("pad_width", "LENGTH", pad_width)
    dim_pad_height = part_parameters.create_dimension("pad_height", "LENGTH", pad_height)
    dim_pad_depth = part_parameters.create_dimension("pad_depth", "LENGTH", pad_depth)

    main_body = part.main_body

    # ######################## #
    # create the hybrid bodies #
    # ######################## #
    hybrid_body_arcs = hybrid_bodies.add()
    hybrid_body_arcs.name = geom_set_arcs

    hybrid_body_cylinders = hybrid_bodies.add()
    hybrid_body_cylinders.name = geom_set_cylinders

    hybrid_body_lines = hybrid_bodies.add()
    hybrid_body_lines.name = geom_set_lines

    hybrid_body_planes = hybrid_bodies.add()
    hybrid_body_planes.name = geom_set_planes

    hybrid_body_points = hybrid_bodies.add()
    hybrid_body_points.name = geom_set_points

    hybrid_body_sketches = hybrid_bodies.add()
    hybrid_body_sketches.name = geom_set_sketches

    hybrid_body_splines = hybrid_bodies.add()
    hybrid_body_splines.name = geom_set_splines

    hybrid_body_surfaces = hybrid_bodies.add()
    hybrid_body_surfaces.name = geom_set_surfaces

    # #################### #
    # create the 3D points #
    # #################### #

    # create the hybrid shape 'points'
    point_1 = hybrid_shape_factory.add_new_point_coord(0, 0, 0)
    point_2 = hybrid_shape_factory.add_new_point_coord(pad_width, 0, 0)
    point_3 = hybrid_shape_factory.add_new_point_coord(pad_width, pad_height, 0)
    point_4 = hybrid_shape_factory.add_new_point_coord(0, pad_height, 0)

    ref_point_1 = Reference(point_1.com_object)
    ref_point_2 = Reference(point_2.com_object)
    ref_point_3 = Reference(point_3.com_object)
    ref_point_4 = Reference(point_4.com_object)

    # add the points to 'construction_points'
    hybrid_body_points.append_hybrid_shape(point_1)
    hybrid_body_points.append_hybrid_shape(point_2)
    hybrid_body_points.append_hybrid_shape(point_3)
    hybrid_body_points.append_hybrid_shape(point_4)

    part.update()

    relations = part.relations
    # the dim name here would typically be 'Part1\dim_width'. the com interfaces does not expect the 'Part1' part.
    p_w_name = "\\".join(dim_pad_width.name.split("\\")[1:])
    p_h_name = "\\".join(dim_pad_height.name.split("\\")[1:])
    formula_1 = relations.create_formula("formula_1", "", point_2.x, p_w_name)
    formula_2 = relations.create_formula("formula_2", "", point_3.x, p_w_name)
    formula_3 = relations.create_formula("formula_3", "", point_3.y, p_h_name)
    formula_5 = relations.create_formula("formula_5", "", point_4.y, p_h_name)

    # #############################
    # create the sketch for the pad
    # #############################
    xy_plane = part.origin_elements.plane_xy
    ref_xy_plane = Reference(xy_plane.com_object)
    sketch = hybrid_body_sketches.hybrid_sketches.add(ref_xy_plane)
    factory_2d = sketch.open_edition()

    # create the points for the lines.
    # the co-ordinates aren't import as the line will be constrained
    # to the 3d points.
    point_1_2d = factory_2d.create_point(0, 0)
    point_2_2d = factory_2d.create_point(pad_width, 0)
    point_3_2d = factory_2d.create_point(pad_width, pad_height)
    point_4_2d = factory_2d.create_point(0, pad_height)
    point_1_2d.report_name = 1
    point_2_2d.report_name = 1
    point_3_2d.report_name = 1
    point_4_2d.report_name = 1

    line_1_2d = factory_2d.create_line(0, 0, pad_width, 0)
    line_2_2d = factory_2d.create_line(pad_width, 0, pad_width, pad_height)
    line_3_2d = factory_2d.create_line(pad_width, pad_height, 0, pad_height)
    line_4_2d = factory_2d.create_line(0, pad_height, 0, 0)

    line_1_2d.start_point, line_1_2d.end_point = point_1_2d, point_2_2d
    line_2_2d.start_point, line_2_2d.end_point = point_2_2d, point_3_2d
    line_3_2d.start_point, line_3_2d.end_point = point_3_2d, point_4_2d
    line_4_2d.start_point, line_4_2d.end_point = point_4_2d, point_1_2d

    constraints = sketch.constraints

    con_line_1_start = constraints.add_bi_elt_cst(
        cat_constraint_type.index("catCstTypeOn"),
        Reference(line_1_2d.start_point.com_object),
        ref_point_1,
    )
    con_line_1_start.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
    con_line_1_end = constraints.add_bi_elt_cst(
        cat_constraint_type.index("catCstTypeOn"),
        Reference(line_1_2d.end_point.com_object),
        ref_point_2,
    )
    con_line_1_end.mode = cat_constraint_mode.index("catCstModeDrivingDimension")

    con_line_2_start = constraints.add_bi_elt_cst(
        cat_constraint_type.index("catCstTypeOn"),
        Reference(line_2_2d.start_point.com_object),
        ref_point_2,
    )
    con_line_2_start.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
    con_line_2_end = constraints.add_bi_elt_cst(
        cat_constraint_type.index("catCstTypeOn"),
        Reference(line_2_2d.end_point.com_object),
        ref_point_3,
    )
    con_line_2_end.mode = cat_constraint_mode.index("catCstModeDrivingDimension")

    con_line_3_start = constraints.add_bi_elt_cst(
        cat_constraint_type.index("catCstTypeOn"),
        Reference(line_3_2d.start_point.com_object),
        ref_point_3,
    )
    con_line_3_start.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
    con_line_3_end = constraints.add_bi_elt_cst(
        cat_constraint_type.index("catCstTypeOn"),
        Reference(line_3_2d.end_point.com_object),
        ref_point_4,
    )
    con_line_3_end.mode = cat_constraint_mode.index("catCstModeDrivingDimension")

    con_line_4_start = constraints.add_bi_elt_cst(
        cat_constraint_type.index("catCstTypeOn"),
        Reference(line_4_2d.start_point.com_object),
        ref_point_4,
    )
    con_line_4_start.mode = cat_constraint_mode.index("catCstModeDrivingDimension")
    con_line_4_end = constraints.add_bi_elt_cst(
        cat_constraint_type.index("catCstTypeOn"),
        Reference(line_4_2d.end_point.com_object),
        ref_point_1,
    )
    con_line_4_end.mode = cat_constraint_mode.index("catCstModeDrivingDimension")

    sketch.close_edition()

    # ##############
    # create the pad
    # ##############

    part.in_work_object = main_body
    pad = part_shape_factory.add_new_pad(sketch, pad_depth)

    part.update()

    # ##############
    # create lines
    # ##############

    line_1 = hybrid_shape_factory.add_new_line_pt_pt(ref_point_1, ref_point_3)
    hybrid_body_lines.append_hybrid_shape(line_1)

    line_2 = hybrid_shape_factory.add_new_line_pt_pt(ref_point_1, ref_point_4)
    hybrid_body_lines.append_hybrid_shape(line_2)

    # ###################################### #
    # create a surface by filling the sketch #
    # ###################################### #
    fill = hybrid_shape_factory.add_new_fill()
    sketch_reference = part.create_reference_from_object(sketch)
    fill.add_bound(sketch_reference)
    hybrid_body_surfaces.append_hybrid_shape(fill)

    # ################ #
    # create a circle  #
    # ################ #
    circle = hybrid_shape_factory.add_new_circle_ctr_rad(ref_point_4, ref_xy_plane, True, 25)
    hybrid_body_arcs.append_hybrid_shape(circle)

    part.update()

    # ############## #
    # create an axis #
    # ############## #
    axis_systems = part.axis_systems
    axis = axis_systems.add()
    axis.name = "Axis.1"

    part.update()

    # ############### #
    # create a spline #
    # ############### #
    point_5 = hybrid_shape_factory.add_new_point_coord(-54, 47, 0)
    point_6 = hybrid_shape_factory.add_new_point_coord(-70, 108, 0)
    point_7 = hybrid_shape_factory.add_new_point_coord(-54, 155, 0)
    point_8 = hybrid_shape_factory.add_new_point_coord(-70, 200, 0)

    # add the points to 'construction_points'
    hybrid_body_points.append_hybrid_shape(point_5)
    hybrid_body_points.append_hybrid_shape(point_6)
    hybrid_body_points.append_hybrid_shape(point_7)
    hybrid_body_points.append_hybrid_shape(point_8)

    spline = hybrid_shape_factory.add_new_spline()
    spline.add_point(Reference(point_5.com_object))
    spline.add_point(Reference(point_6.com_object))
    spline.add_point(Reference(point_7.com_object))
    spline.add_point(Reference(point_8.com_object))

    hybrid_body_splines.append_hybrid_shape(spline)

    part.update()

    # ############## #
    # create a plane #
    # ############## #
    plane = hybrid_shape_factory.add_new_plane_offset(ref_xy_plane, 200, True)
    hybrid_body_planes.append_hybrid_shape(plane)

    part.update()

    # ################# #
    # create a cylinder #
    # ################# #
    direction = hybrid_shape_factory.add_new_direction(ref_xy_plane)
    cylinder = hybrid_shape_factory.add_new_cylinder(ref_point_3, 33, 100, 0, direction)
    hybrid_body_cylinders.append_hybrid_shape(cylinder)

    part.update()

    document.save()
    document.close()


def get_cat_part_measurable():
    if not source_cat_part_measurable.exists():
        caa.logger.info(f"Creating {source_cat_part_measurable}")
        create_cat_part_measurable(source_cat_part_measurable)
    return source_cat_part_measurable
