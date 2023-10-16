#! /usr/bin/python3.9
# author: evereux
# contact: evereux@gmail.com
# date:


"""
    Description
    ===========
    Creates a simple Wing Surface From NACA profile defined in a dat file.


    Requirements
    ============
    python >= 3.9
    pycatia >= 0.6.2
    CATIA V5 running with no existing documents open.


    Methods
    =======
    The following is a brief description of some of the methods used in this script.
    Points on a plane.
    Splines
    Translations (point to point, scaling and rotate)
    Parameters and Relations: These are linked to geometry
    Publications
"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia"))
##########################################################

from pathlib import Path
from pycatia import catia
from pycatia.mec_mod_interfaces.part import Part
from pycatia.product_structure_interfaces.product import Product
from pycatia.scripts.vba import vba_nothing

from naca_profile_support.points import add_points
from naca_profile_support.parameters import create_parameters
from naca_profile_support.read_dat_file import read_dat_file
from naca_profile_support.hide_show import hide_element
from naca_profile_support import constants

# read the contents of the file naca_profile_support/sc20610.dat and import the
# coordinates

part_number = "Wing_Geometry"
naca_dat_file = Path(os.getcwd(), 'user_scripts', 'naca_profile_support/sc20610.dat')

upper_coordinates, lower_coordinates = read_dat_file(naca_dat_file, constants.CHORD_LENGTH_ROOT)

caa = catia()
application = caa.application
documents = application.documents
new_part = documents.add('Part')
document = application.active_document

# todo: check no open documents called part_number, if there are exit the script.

product = Product(document.product.com_object)
product.part_number = part_number

part = Part(document.part.com_object)

parameters = create_parameters(part, product)
relations = part.relations

hybrid_shape_factory = part.hybrid_shape_factory
hybrid_bodies = part.hybrid_bodies

# create new Geometrical Set "ConstructionGeometry
gs_master_geometry = hybrid_bodies.add()
gs_master_geometry.name = "MasterGeometry"

# create new Geometrical Set "ConstructionGeometry
gs_construction_geometry = hybrid_bodies.add()
gs_construction_geometry.name = "ConstructionGeometry"

# create a new Geometrical Set "points" as a child of "ConstructionGeometry"
hbs_construction_geometry = gs_construction_geometry.hybrid_bodies
gs_points = hbs_construction_geometry.add()
gs_points.name = "points"

# create a new Geometrical Set "lower" as a child of "points"
hbs_points_lower = gs_points.hybrid_bodies
gs_points_lower = hbs_points_lower.add()
gs_points_lower.name = "lower"

# create a new Geometrical Set "lower" as a child of "points"
hbs_points_upper = gs_points.hybrid_bodies
gs_points_upper = hbs_points_upper.add()
gs_points_upper.name = "upper"

# create a new Geometrical Set "other" as a child of "points"
hbs_point_other = gs_points.hybrid_bodies
gs_point_other = hbs_points_upper.add()
gs_point_other.name = "other"

# create a new Geometrical Set "lines" as a child of "ConstructionGeometry"
hbs_construction_geometry = gs_construction_geometry.hybrid_bodies
gs_lines = hbs_construction_geometry.add()
gs_lines.name = "lines"

# create a new Geometrical Set "planes" as a child of "ConstructionGeometry"
hbs_construction_geometry = gs_construction_geometry.hybrid_bodies
gs_planes = hbs_construction_geometry.add()
gs_planes.name = "planes"

# create a new Geometrical Set "Spline" as a child of "ConstructionGeometry"
hbs_construction_geometry = gs_construction_geometry.hybrid_bodies
gs_splines = hbs_construction_geometry.add()
gs_splines.name = "splines"

origin_elements = part.origin_elements
plane_xy = origin_elements.plane_xy
plane_yz = origin_elements.plane_yz
plane_zx = origin_elements.plane_zx
ref_plane_xy = part.create_reference_from_object(plane_xy)
ref_plane_yz = part.create_reference_from_object(plane_yz)
ref_plane_zx = part.create_reference_from_object(plane_zx)

add_points(hybrid_shape_factory, ref_plane_xy, gs_points_lower, lower_coordinates)
add_points(hybrid_shape_factory, ref_plane_xy, gs_points_upper, upper_coordinates)
add_points(hybrid_shape_factory, ref_plane_xy, gs_point_other, [(0, 0)])

# initialise the spline object
hs_spline = hybrid_shape_factory.add_new_spline()
hs_spline.set_spline_type(0)
hs_spline.set_closing(0)
hs_spline.set_support(ref_plane_xy)

points_hss_upper = gs_points_upper.hybrid_shapes
points_hss_root = gs_point_other.hybrid_shapes
points_hss_lower = gs_points_lower.hybrid_shapes

# create a list of all the points
points_hss = [p for p in points_hss_upper]
# reverse the upper points as spline creation needs to start from end.
points_hss.reverse()
points_hss.extend([p for p in points_hss_root])
points_hss.extend([p for p in points_hss_lower])

for hs in points_hss:
    ref_point = part.create_reference_from_object(hs)
    hs_spline.add_point_with_constraint_explicit(ref_point, vba_nothing, -1, 1, vba_nothing, 0)
hs_spline.name = "Spline.WingRoot"
gs_splines.append_hybrid_shape(hs_spline)

# add new plane to define wing surface limit
hs_plane_offset = hybrid_shape_factory.add_new_plane_offset(ref_plane_xy, constants.OFFSET_WING_TIP, False)
hs_plane_offset.name = 'Plane.WingTip'
# link to OFFSET_WING_TIP parameter
length_offset = hs_plane_offset.offset
relations.create_formula("Formula.OFFSET_WING_TIP", "", length_offset, "`OFFSET_WING_TIP`")
gs_planes.append_hybrid_shape(hs_plane_offset)
ref_hs_plane_offset = part.create_reference_from_object(hs_plane_offset)

# scale the spline which we'll copy to the offset plane, we need to do this in two directions.
ref_hs_spline = part.create_reference_from_object(hs_spline)
hs_spline_scale_yz = hybrid_shape_factory.add_new_hybrid_scaling(ref_hs_spline, ref_plane_yz, constants.RATIO)
ratio_value = hs_spline_scale_yz.ratio
relations.create_formula("Formula.RATIO.1", "", ratio_value, "`RATIO`")
# link ratio value to parameter
gs_splines.append_hybrid_shape(hs_spline_scale_yz)
ref_hs_spline_yz = part.create_reference_from_object(hs_spline_scale_yz)
hide_element(document, hs_spline_scale_yz)

# second scaling direction
hs_spline_scale_final = hybrid_shape_factory.add_new_hybrid_scaling(ref_hs_spline_yz, ref_plane_zx, constants.RATIO)
# link ratio value to parameter
ratio_value = hs_spline_scale_final.ratio
relations.create_formula("Formula.RATIO.1", "", ratio_value, "`RATIO`")
ref_hs_spline_1 = part.create_reference_from_object(hs_spline_scale_final)
gs_splines.append_hybrid_shape(hs_spline_scale_final)
hide_element(document, ref_hs_spline_1)

# create the translation geometry at the wing tip
point_wingtip_origin = hybrid_shape_factory.add_new_point_on_plane(
    ref_hs_plane_offset,
    constants.WING_TIP_TRANSLATION_X,
    constants.WING_TIP_TRANSLATION_Y
)
gs_point_other.append_hybrid_shape(point_wingtip_origin)
ref_point_wingtip_origin = part.create_reference_from_object(point_wingtip_origin)
point_x = point_wingtip_origin.x_offset
relations.create_formula("Formula.WING_TIP_TRANSLATION_X", "", point_x, "`WING_TIP_TRANSLATION_X`")
point_y = point_wingtip_origin.y_offset
relations.create_formula("Formula.WING_TIP_TRANSLATION_Y", "", point_y, "`WING_TIP_TRANSLATION_Y`")

# create CHORD line of length CHORD_LENGTH_WING_TIP
hs_direction = hybrid_shape_factory.add_new_direction(ref_plane_yz)
line_wingtip_chord = hybrid_shape_factory.add_new_line_pt_dir(
    ref_point_wingtip_origin,
    hs_direction,
    0,
    constants.CHORD_LENGTH_WING_TIP,
    False
)
length_line = line_wingtip_chord.end_offset
relations.create_formula("Formula.CHORD_LENGTH_WING_TIP", "", length_line, "`CHORD_LENGTH_WING_TIP`")

ref_line_wingtip_chord = part.create_reference_from_object(line_wingtip_chord)
gs_lines.append_hybrid_shape(line_wingtip_chord)
# create ANGLE CHORD line of length CHORD_LENGTH_WING_TIP
line_wingtip_chord_angle = hybrid_shape_factory.add_new_line_angle(
    ref_line_wingtip_chord,
    ref_hs_plane_offset,
    ref_point_wingtip_origin,
    False,
    0,
    constants.CHORD_LENGTH_WING_TIP,
    constants.WING_TIP_RELATIVE_ANGLE,
    False
)
length_line = line_wingtip_chord_angle.end_offset
relations.create_formula("Formula.CHORD_LENGTH_WING_TIP", "", length_line, "`CHORD_LENGTH_WING_TIP`")
angle_line = line_wingtip_chord_angle.angle
relations.create_formula("Formula.WING_TIP_RELATIVE_ANGLE", "", angle_line, "`WING_TIP_RELATIVE_ANGLE`")

gs_lines.append_hybrid_shape(line_wingtip_chord_angle)
# create line normal to the wing tip plane to be used for rotation.
line_wingtip_normal = hybrid_shape_factory.add_new_line_normal(
    ref_hs_plane_offset,
    ref_point_wingtip_origin,
    -500,
    500,
    False
)
gs_lines.append_hybrid_shape(line_wingtip_normal)
ref_line_wingtip_normal = part.create_reference_from_object(line_wingtip_normal)

# get the first point in ConstructionGeometry.Points.Other and create reference for translation.
point_0_0 = gs_point_other.hybrid_shapes.item(1)
ref_point_0_0 = part.create_reference_from_object(point_0_0)

# create line from point at wing root and point at wing tip
line_root_tip = hybrid_shape_factory.add_new_line_pt_pt(
    ref_point_0_0,
    ref_point_wingtip_origin
)
gs_lines.append_hybrid_shape(line_root_tip)
ref_line_root_tip = part.create_reference_from_object(line_root_tip)

# copy the scaled spline to the wing tip root using point to point translation
spline_translate = hybrid_shape_factory.add_new_empty_translate()
spline_translate.elem_to_translate = ref_hs_spline_1
spline_translate.vector_type = 1
spline_translate.first_point = ref_point_0_0
spline_translate.second_point = ref_point_wingtip_origin
spline_translate.volume_result = False
gs_splines.append_hybrid_shape(spline_translate)
ref_spline_translate = part.create_reference_from_object(spline_translate)
hide_element(spline_translate)

# rotate the spline
spline_final = hybrid_shape_factory.add_new_empty_rotate()
spline_final.elem_to_rotate = ref_spline_translate
spline_final.volume_result = False
spline_final.rotation_type = 0
spline_final.axis = ref_line_wingtip_normal
spline_final.angle_value = constants.WING_TIP_RELATIVE_ANGLE
spline_final.name = "Spline.WingTip"
# link the angle rotation to parameter WING_TIP_RELATIVE_ANGLE.
spline_angle = spline_final.angle
relations.create_formula("Formala.WING_TIP_RELATIVE_ANGLE", "", spline_angle, "`WING_TIP_RELATIVE_ANGLE`")
gs_splines.append_hybrid_shape(spline_final)
ref_spline_final = part.create_reference_from_object(spline_final)

# create the surface
surface_name = "Surface.WingSurface"
hs_loft = hybrid_shape_factory.add_new_loft()
hs_loft.section_coupling = 1
hs_loft.relimitation = 1
hs_loft.canonical_detection = 2
hs_loft.add_guide(ref_line_root_tip)
hs_loft.add_section_to_loft(ref_hs_spline, 1, vba_nothing)
hs_loft.add_section_to_loft(ref_spline_final, 1, vba_nothing)
gs_master_geometry.append_hybrid_shape(hs_loft)
hs_loft.name = surface_name

# publish the surface.
ref_hs_loft = product.create_reference_from_name(f"{product.part_number}/!{hs_loft.name}")
# ref_hs_loft = part.create_reference_from_object(hs_loft)
publications = product.publications
publication = publications.add(hs_loft.name)
publications.set_direct(hs_loft.name, ref_hs_loft)

part.update_object(gs_construction_geometry)
part.update_object(gs_master_geometry)
part.update()

windows = application.windows
window = windows.get_item_by_name(f"{product.part_number}.CATPart")
active_viewer = window.active_viewer
active_viewer.reframe()
