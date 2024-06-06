#! /usr/bin/python3.9
# author: evereux
# contact: evereux@gmail.com

"""

    Creating Bounding Box

    Description
    ===========
    Creates a bounding box around the selected Body using the selected
    AxisSystem to orientate the bounding box.

    The script posted on the following page was used as a reference for this
    script: https://www.eng-tips.com/viewthread.cfm?qid=402813. I have made
    additional changes to the script.

    The resultant output is a bounding box whose offset is parameter driven and
    can be easily modified.

    Requirements
    ============
    python >= 3.9
    pycatia
    CATIA V5 running with a part open that has a Body to be bounded and a
    reference Axis System.

    Documentation
    =============
    https://pycatia.readthedocs.io

    More examples and user scripts can be found at:
    https://github.com/evereux/pycatia/tree/master/examples
    https://github.com/evereux/pycatia/tree/master/user_scripts
"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################


from pycatia import catia
from pycatia.cat_logger import create_logger
from pycatia.enumeration.enumeration_types import cat_constraint_type, cat_vis_property_show, cat_constraint_mode
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.axis_system import AxisSystem
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.sketcher_interfaces.geometry_2D import Geometry2D

logger = create_logger()

caa = catia()
application = caa.application
part_document: PartDocument = application.active_document

if '.CATPart' not in part_document.name:
    logger.critical('There must be an CATPart open and active.')

part = part_document.part
shape_factory = part.shape_factory
hybrid_shape_factory = part.hybrid_shape_factory
bodies = part.bodies
part.update()

mb = caa.message_box(
    'You will be prompted to select a reference Axis System and face of the item to be bounded.',
    buttons=1,
    title='Information.'
)
if mb == 2:
    logger.info('Exiting script.')
    exit()

selection = part_document.selection
selection.clear()
filter_ = ('AxisSystem',)
logger.info('Select the Axis system.')
caa.message_box('Please select the Bounding Box Axis System.', buttons=0, title='Selection Prompt')
output = selection.select_element2(filter_, 'Select bounding box AxisSystem.', False)
if output == 'Cancel':
    logger.info('Exiting script.')
    exit()

axis_bbox = AxisSystem(selection.item(1).value.com_object)
axis_bbox.is_current = 1
origin_coord = axis_bbox.get_origin()
origin_point = hybrid_shape_factory.add_new_point_coord(origin_coord[0], origin_coord[1], origin_coord[2])
ref_origin_pont = part.create_reference_from_object(origin_point)
x_axis_coord = axis_bbox.get_x_axis()
y_axis_coord = axis_bbox.get_y_axis()
z_axis_coord = axis_bbox.get_z_axis()
hs_direction_x = hybrid_shape_factory.add_new_direction_by_coord(x_axis_coord[0], x_axis_coord[1], x_axis_coord[2])
hs_direction_y = hybrid_shape_factory.add_new_direction_by_coord(y_axis_coord[0], y_axis_coord[1], y_axis_coord[2])
hs_direction_z = hybrid_shape_factory.add_new_direction_by_coord(z_axis_coord[0], z_axis_coord[1], z_axis_coord[2])

plane_line_1 = hybrid_shape_factory.add_new_line_pt_dir(ref_origin_pont, hs_direction_x, 0, 0, False)
plane_line_2 = hybrid_shape_factory.add_new_line_pt_dir(ref_origin_pont, hs_direction_y, 0, 0, False)

dot_id = bodies.count
body_bbox = bodies.add()
body_bbox.name = f'Body.BoundingBox.{dot_id}'

hbodies_bbox = body_bbox.hybrid_bodies
gs_bbox = hbodies_bbox.add()
gs_bbox.name = 'points'

selection.clear()
filter_ = ('Face',)
logger.info('Select a face of the body.')
caa.message_box('Please select a face belonging to the body to be bounded.', buttons=0, title='Selection Prompt')
output = selection.select_element2(filter_, 'Select a face of the body to be bounded.', False)
if output == 'Cancel':
    logger.info('Existing Script.')
    exit()

selected_face = selection.item(1).reference
extracted_face = hybrid_shape_factory.add_new_extract(selected_face)
extracted_face.propagation_type = 1
extracted_face.complementary_extract = False
extracted_face.is_federated = False
reference_extracted_face = part.create_reference_from_object(extracted_face)

extrenum_1 = hybrid_shape_factory.add_new_extremum(reference_extracted_face, hs_direction_x, 1)
extrenum_2 = hybrid_shape_factory.add_new_extremum(reference_extracted_face, hs_direction_x, 0)
extrenum_3 = hybrid_shape_factory.add_new_extremum(reference_extracted_face, hs_direction_y, 1)
extrenum_4 = hybrid_shape_factory.add_new_extremum(reference_extracted_face, hs_direction_y, 0)
extrenum_5 = hybrid_shape_factory.add_new_extremum(reference_extracted_face, hs_direction_z, 1)
extrenum_6 = hybrid_shape_factory.add_new_extremum(reference_extracted_face, hs_direction_z, 0)
extrenum_1.name = 'Extrenum.max_X'
extrenum_2.name = 'Extrenum.min_X'
extrenum_3.name = 'Extrenum.max_Y'
extrenum_4.name = 'Extrenum.min_Y'
extrenum_5.name = 'Extrenum.min_Z'
extrenum_6.name = 'Extrenum.min_Z'

part.update()

gs_bbox.append_hybrid_shapes([extrenum_1, extrenum_2, extrenum_3, extrenum_4, extrenum_5, extrenum_6])

part.update()

ref_extrenum_1 = part.create_reference_from_object(extrenum_1)
point_1 = hybrid_shape_factory.add_new_point_coord_with_reference(0, 0, 0, ref_extrenum_1)
point_1.name = 'Point.1'

ref_extrenum_2 = part.create_reference_from_object(extrenum_2)
point_2 = hybrid_shape_factory.add_new_point_coord_with_reference(0, 0, 0, ref_extrenum_2)
point_2.name = 'Point.2'

ref_extrenum_3 = part.create_reference_from_object(extrenum_3)
point_3 = hybrid_shape_factory.add_new_point_coord_with_reference(0, 0, 0, ref_extrenum_3)
point_3.name = 'Point.3'

ref_extrenum_4 = part.create_reference_from_object(extrenum_4)
point_4 = hybrid_shape_factory.add_new_point_coord_with_reference(0, 0, 0, ref_extrenum_4)
point_4.name = 'Point.4'

ref_extrenum_5 = part.create_reference_from_object(extrenum_5)
point_5 = hybrid_shape_factory.add_new_point_coord_with_reference(0, 0, 0, ref_extrenum_5)
point_5.name = 'Point.5'

ref_extrenum_6 = part.create_reference_from_object(extrenum_6)
point_6 = hybrid_shape_factory.add_new_point_coord_with_reference(0, 0, 0, ref_extrenum_6)
point_6.name = 'Point.6'

gs_bbox.append_hybrid_shape(point_1)
gs_bbox.append_hybrid_shape(point_2)
gs_bbox.append_hybrid_shape(point_3)
gs_bbox.append_hybrid_shape(point_4)
gs_bbox.append_hybrid_shape(point_5)
gs_bbox.append_hybrid_shape(point_6)

ref_point_1 = part.create_reference_from_object(point_1)
ref_point_2 = part.create_reference_from_object(point_2)
ref_point_3 = part.create_reference_from_object(point_3)
ref_point_4 = part.create_reference_from_object(point_4)
ref_point_5 = part.create_reference_from_object(point_5)
ref_point_6 = part.create_reference_from_object(point_6)
ref_plane_xy = part.create_reference_from_name(
    f'Selection_RSur:(Face:(Brp:({axis_bbox.name};1);None:());{axis_bbox.name})')

part.update()

# create the sketch
sketches = gs_bbox.hybrid_sketches
sketch_bbox_1 = sketches.add(ref_plane_xy)
factory_2d_1 = sketch_bbox_1.open_edition()
geometric_elements_1 = sketch_bbox_1.geometric_elements
axis_2d = geometric_elements_1.item('AbsoluteAxis')
line_hdirection = Geometry2D(axis_2d.get_item('HDirection').com_object)
line_hdirection.report_name = 1
line_vdirection = Geometry2D(axis_2d.get_item('VDirection').com_object)
line_vdirection.report_name = 2

p = 20000
point_2d_1 = factory_2d_1.create_point(-p, -p)
point_2d_1.report_name = 3

point_2d_2 = factory_2d_1.create_point(p, -p)
point_2d_2.report_name = 4

point_2d_3 = factory_2d_1.create_point(p, p)
point_2d_3.report_name = 5

point_2d_4 = factory_2d_1.create_point(-p, p)
point_2d_4.report_name = 6

line_2d_btm = factory_2d_1.create_line(-p, -p, p, -p)
line_2d_btm.name = "Line.Bottom"
line_2d_btm.report_name = 7
line_2d_btm.start_point = point_2d_1
line_2d_btm.end_point = point_2d_2

line_2d_right = factory_2d_1.create_line(p, -p, p, p)
line_2d_right.name = "Line.Right"
line_2d_right.report_name = 8
line_2d_right.start_point = point_2d_2
line_2d_right.end_point = point_2d_3

line_2d_top = factory_2d_1.create_line(-p, p, p, p)
line_2d_top.name = "Line.Top"
line_2d_top.report_name = 9
line_2d_top.start_point = point_2d_4
line_2d_top.end_point = point_2d_3

line_2d_left = factory_2d_1.create_line(-p, -p, -p, p)
line_2d_left.name = "Line.Left"
line_2d_left.report_name = 10
line_2d_left.start_point = point_2d_1
line_2d_left.end_point = point_2d_4

ref_line_2d_btm = part.create_reference_from_object(line_2d_btm)
ref_line_2d_right = part.create_reference_from_object(line_2d_right)
ref_line_2d_top = part.create_reference_from_object(line_2d_top)
ref_line_2d_left = part.create_reference_from_object(line_2d_left)

constraints_sketch = sketch_bbox_1.constraints

cst_distance = cat_constraint_type.index('catCstTypeDistance')
constraint_btm = constraints_sketch.add_bi_elt_cst(cst_distance, ref_line_2d_btm, ref_point_4)
constraint_top = constraints_sketch.add_bi_elt_cst(cst_distance, ref_point_3, ref_line_2d_top)
constraint_left = constraints_sketch.add_bi_elt_cst(cst_distance, ref_line_2d_left, ref_point_2)
constraint_right = constraints_sketch.add_bi_elt_cst(cst_distance, ref_point_1, ref_line_2d_right)

length_bottom = Length(constraint_btm.dimension.com_object)
length_top = Length(constraint_top.dimension.com_object)
length_left = Length(constraint_left.dimension.com_object)
length_right = Length(constraint_right.dimension.com_object)

# make the bottom line parallel with the zx axis system of selected axis.
ref_plane_zx = part.create_reference_from_b_rep_name(
    f'FSur:(Face:(Brp:({axis_bbox.name};3);None:();Cf11:());WithPermanentBody;WithoutBuildError;WithInitialFeatureSupport;MonoFond;MFBRepVersion_CXR15)',
    axis_bbox)
geometric_elements_zx = factory_2d_1.create_intersections(ref_plane_zx)
geometry_zx = geometric_elements_zx.item('Mark.1')
geometry_2d = Geometry2D(geometric_elements_zx.get_item('Mark.1').com_object)
geometry_2d.construction = True
ref_geometry_zx = part.create_reference_from_object(geometry_zx)
cst_parallel = cat_constraint_type.index('catCstTypeParallelism')
constraint_6 = constraints_sketch.add_bi_elt_cst(cst_parallel, ref_line_2d_btm, ref_geometry_zx)
cst_driving = cat_constraint_mode.index('catCstModeDrivingDimension')
constraint_6.mode = cst_driving
# make the top line parallel with the bottom line.
constraint_7 = constraints_sketch.add_bi_elt_cst(cst_parallel, ref_line_2d_btm, ref_line_2d_top)
constraint_7.mode = cst_driving
# make the left and right lines normal to the bottom line.
cst_normal = cat_constraint_type.index('catCstTypePerpendicularity')
constraint_8 = constraints_sketch.add_bi_elt_cst(cst_normal, ref_line_2d_btm, ref_line_2d_left)
constraint_8.mode = cst_driving
constraint_9 = constraints_sketch.add_bi_elt_cst(cst_normal, ref_line_2d_btm, ref_line_2d_right)
constraint_9.mode = cst_driving

# create the parameters for bounding box offsets
parameters = part.parameters
parameter_bbox_bottom = parameters.create_dimension('BBoxOffset_Bottom', 'Length', 10)
parameter_bbox_top = parameters.create_dimension('BBoxOffset_Top', 'Length', 10)
parameter_bbox_left = parameters.create_dimension('BBoxOffset_Left', 'Length', 10)
parameter_bbox_right = parameters.create_dimension('BBoxOffset_Right', 'Length', 10)

# link the parameters to the lines in sketch
relations = part.relations
relations.create_formula('Formula.Bottom', '', length_bottom, parameter_bbox_bottom.name.split('\\')[1])
relations.create_formula('Formula.Top', '', length_top, parameter_bbox_top.name.split('\\')[1])
relations.create_formula('Formula.Left', '', length_left, parameter_bbox_left.name.split('\\')[1])
relations.create_formula('Formula.Right', '', length_right, parameter_bbox_right.name.split('\\')[1])

sketch_bbox_1.close_edition()

part.update()

# create the min and max Z planes
ref_origin_line_1 = part.create_reference_from_object(line_hdirection)
ref_origin_line_2 = part.create_reference_from_object(line_vdirection)

plane_origin = hybrid_shape_factory.add_new_plane2_lines(ref_origin_line_1, ref_origin_line_2)
ref_plane_origin = part.create_reference_from_object(plane_origin)
plane_origin = hybrid_shape_factory.add_new_plane_offset_pt(ref_plane_origin, ref_point_6)
ref_plane_origin = part.create_reference_from_object(plane_origin)
gs_bbox.append_hybrid_shape(plane_origin)

plane_offset = hybrid_shape_factory.add_new_plane_offset_pt(ref_plane_origin, ref_point_5)
gs_bbox.append_hybrid_shape(plane_offset)

ref_plane_origin = part.create_reference_from_object(plane_origin)
ref_plane_offset = part.create_reference_from_object(plane_offset)

part.update()

# create the line that sweeps around the XY sketch boundary
point_inf = hybrid_shape_factory.add_new_point_coord_with_reference(0, 0, 0, ref_point_6)
point_inf.name = 'Point.Inf'
gs_bbox.append_hybrid_shape(point_inf)
ref_point_inf = part.create_reference_from_object(point_inf)

point_prj_inf = hybrid_shape_factory.add_new_project(ref_point_6, ref_plane_offset)
point_prj_inf.name = 'Point.Prf.Inf'
gs_bbox.append_hybrid_shape(point_prj_inf)
ref_point_prj_inf = part.create_reference_from_object(point_prj_inf)

point_sup = hybrid_shape_factory.add_new_point_coord_with_reference(0, 0, 0, ref_point_prj_inf)
point_sup.name = 'Point.Sup'
gs_bbox.append_hybrid_shape(point_sup)
ref_point_sup = part.create_reference_from_object(point_sup)

line_guide = hybrid_shape_factory.add_new_line_pt_pt(ref_point_sup, ref_point_inf)
gs_bbox.append_hybrid_shape(line_guide)
ref_line_guide = part.create_reference_from_object(line_guide)

line_guide_start = Length(line_guide.begin_offset.com_object)
line_guide_start.value = 1
line_guide_end = Length(line_guide.end_offset.com_object)
line_guide_end.value = 1

contraints_part = part.constraints
cat_cst_type_length = cat_constraint_type.index('catCstTypeLength')
contraint_dz = contraints_part.add_mono_elt_cst(cat_cst_type_length, ref_line_guide)
length_dz = Length(contraint_dz.dimension.com_object)

part.update()

reference_sketch = part.create_reference_from_object(sketch_bbox_1)
sweep = hybrid_shape_factory.add_new_sweep_explicit(reference_sketch, ref_line_guide)
gs_bbox.append_hybrid_shape(sweep)
ref_sweep = part.create_reference_from_object(sweep)

part.update()

sf_close_surface = shape_factory.add_new_close_surface(ref_sweep)
sf_close_surface.name = "CloseSurface.BoundingBox"

part.update()

selection.clear()
selection.add(gs_bbox)
no_show = cat_vis_property_show.index('catVisPropertyNoShowAttr')
selection.vis_properties.set_show(no_show)
selection.clear()
selection.add(body_bbox)
selection.vis_properties.set_real_color(0, 0, 0, 0)
selection.vis_properties.set_real_opacity(150, 1)
selection.vis_properties.set_real_width(2, 1)

part.update()
