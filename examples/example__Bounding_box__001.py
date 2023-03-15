"""
    Example - Bounding Box version 1 - 001:
    Promt user select axis system and any geometry
    Create Bounding box of selected geometry:
        1.Wireframe bounding box
        2.Surface bounding box
        3.Solid bounding box
    .. warning:
        Catia must be run and document open and active.
        Part document must content any geometry and one axis system
    .. note:
        Need add cylindrical bounding box
"""
from msvcrt import getch
from pycatia.mec_mod_interfaces.axis_system import AxisSystem
from pycatia.mec_mod_interfaces.body import Body
from pycatia.mec_mod_interfaces.part import Part
from pycatia.in_interfaces.reference import Reference
from pycatia.space_analyses_interfaces.spa_workbench import SPAWorkbench
from pycatia import catia

__author__ = "[ptm] by plm-forum.ru"
__status__ = "alpha"

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

"""
    TODO: add user interface with tk
"""
import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box
def getInputBoxValue()->tuple:
    """Get uset input value

    Returns:
        tuple: return tuple offcet value
        (Xmax,Xmin,Ymax,Ymin,Zmax,Zmin)
    """
    result=(Xmax.get(),
            Xmin.get(),
            Ymax.get(),
            Ymin.get(),
            Zmax.get(),
            Zmin.get())
    return result


# this is the function called when the button is clicked
def btnClickFunction():
	print('clicked')



root = Tk()

# This is the section of code which creates the main window
root.geometry('555x180')
root.configure(background='#FFEFDB')
root.title('Input offset')


# This is the section of code which creates a text input box
Xmax=Entry(root)
Xmax.place(x=15, y=40)

Xmin=Entry(root)
Xmin.place(x=15, y=90)

Ymax=Entry(root)
Ymax.place(x=195, y=40)

Ymin=Entry(root)
Ymin.place(x=195, y=90)

Zmax=Entry(root)
Zmax.place(x=375, y=40)

Zmin=Entry(root)
Zmin.place(x=375, y=90)


# This is the section of code which creates a button
Button(root, text='Set offset', bg='#FFEFDB', font=('arial', 12, 'normal'), 
       command=btnClickFunction).place(x=200, y=120)


# This is the section of code which creates the a label
Label(root, text='Xmax', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=25, y=10)
Label(root, text='Xmin', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=25, y=60)

Label(root, text='Ymax', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=195, y=10)
Label(root, text='Ymin', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=195, y=60)

Label(root, text='Zmax', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=375, y=10)
Label(root, text='Zmin', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=375, y=60)


root.mainloop()




def axis_references(input_part: Part, input_axis: AxisSystem) -> tuple:
    """
        Return tuple of references for planes and axis

    Args:
        input_part (Part): current Part() document
        input_axis (AxisSystem): AxisSystem in Part()

    Returns:
        tuple:  (aX,aY,aZ,pXY,pXZ,pYZ)
        where:
            aX:     X-axis Reference()
            aY:     Y-axis Reference()
            aZ:     Z-axis Reference()
            pXY:    XY-plane Reference()
            pXZ:    XZ-plane Reference()
            pYZ:    YZ-Plane Reference()
    """
    s_X_axis = f"REdge:(Edge:(Face:(Brp:({input_axis.name};1);None:();Cf11:());Face:(Brp:({input_axis.name};3);None:();Cf11:());None:(Limits1:();Limits2:());Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MFBRepVersion_CXR14)"
    s_Y_axis = f"REdge:(Edge:(Face:(Brp:({input_axis.name};2);None:();Cf11:());Face:(Brp:({input_axis.name};1);None:();Cf11:());None:(Limits1:();Limits2:());Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MFBRepVersion_CXR14)"
    s_Z_axis = f"REdge:(Edge:(Face:(Brp:({input_axis.name};3);None:();Cf11:());Face:(Brp:({input_axis.name};2);None:();Cf11:());None:(Limits1:();Limits2:());Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MFBRepVersion_CXR14)"

    s_XY_plane = f"RSur:(Face:(Brp:({input_axis.name};1);None:();Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MFBRepVersion_CXR14)"
    s_XZ_plane = f"RSur:(Face:(Brp:({input_axis.name};3);None:();Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MFBRepVersion_CXR14)"
    s_YZ_plane = f"RSur:(Face:(Brp:({input_axis.name};2);None:();Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MFBRepVersion_CXR14)"

    res0 = input_part.create_reference_from_b_rep_name(s_X_axis, Axis_System)
    res1 = input_part.create_reference_from_b_rep_name(s_Y_axis, Axis_System)
    res2 = input_part.create_reference_from_b_rep_name(s_Z_axis, Axis_System)

    res3 = input_part.create_reference_from_b_rep_name(s_XY_plane, Axis_System)
    res4 = input_part.create_reference_from_b_rep_name(s_XZ_plane, Axis_System)
    res5 = input_part.create_reference_from_b_rep_name(s_YZ_plane, Axis_System)
    return (res0, res1, res2, res3, res4, res5)


def measure_between_planes(
        plane_1: Reference, plane_2: Reference, spa: SPAWorkbench) -> float:
    """
        Return minimum distance between 2 planes
        All planes must bu updated!!!
    Args:
        plane_1 (Reference): first plane
        plane_2 (Reference): second plane
        spa (SPAWorkbench): document SPAWorkbench

    Returns:
        float: result
    """

    mes_plane1 = spa.get_measurable(plane_1)
    min_distance = mes_plane1.get_minimum_distance(plane_2)
    return min_distance


# import headers
try:
    caa = catia()
    documents = caa.documents
    document = caa.active_document
except Exception:
    print("CATIA not started or document not " +
          "opened or started several CATIA sessions")
    print("Press any key to exit...")
    getch()
    exit()


# Input offset to bounding box

Offset_X_min = 10
Offset_X_max = 10

Offset_Y_min = 10
Offset_Y_max = 10

Offset_Z_min = 10
Offset_Z_max = 10

message_promt = (f"Creating Bounding box with offset:\n" +
                 f"Xmin={Offset_X_min}\nXmax={Offset_X_max}\n" +
                 f"Ymin={Offset_Y_min}\nXmax={Offset_Y_max}\n" +
                 f"Zmin={Offset_Z_min}\nXmax={Offset_Z_max}")

return_value = caa.message_box(message_promt, 4, title="Warring")
if (return_value == 7):
    print("Canceled by user")
    exit()

if (document.is_part):
    # need to autocomplete
    part_document = Part(document.part.com_object)
    selection = document.selection

    try:
        part_document.update()
    except Exception:
        print("Part document must be without errors!")
        print("Press any key to exit...")
        getch()
        exit()

    hsf = part_document.hybrid_shape_factory
    caa.message_box('Select a Axis System', 0, title='Selection promt')
    sFilter = ("AxisSystem",)
    sStatus = selection.select_element2(sFilter, "select a  local axis", True)
    if sStatus == "Cancel":
        caa.message_box(
            "Wrong selection! Application will closed!", 16, title="Warring")
        exit()
    Axis_System = AxisSystem(selection.item(1).value.com_object)
    selection.clear()

    ref_axis = axis_references(part_document, Axis_System)

    Hybrid_Shape_D1 = hsf.add_new_direction(ref_axis[0])
    Hybrid_Shape_D2 = hsf.add_new_direction(ref_axis[1])
    Hybrid_Shape_D3 = hsf.add_new_direction(ref_axis[2])

    ref_XY = ref_axis[3]
    ref_XZ = ref_axis[4]
    ref_YZ = ref_axis[5]

    # Create structure for geometry
    #   |-Bounding_box.X            :solid Body
    #   |-GSD Bounding Box.X        :geometrical sets main
    #   |---|-Extreme Points.X
    #   |---|-Planes.X
    #   |---|-Base Lines.X
    #   |---|-Points.X
    #   |---|-Edge.X
    #   |---|-Surfaces.X
    #   |-Profile_Pad.X             :output profile for solid Body
    #   |-Wireframe_Bounding_Box.X  :output edge
    #   |-Surface_Bounding_box.X    :output surfase

    oBodies = part_document.bodies
    j = oBodies.count
    body1 = oBodies.add()
    body1.name = f"Bounding_Box.{j}"

    hybridBodies1 = part_document.hybrid_bodies
    hybridBody_main = hybridBodies1.add()
    hybridBody_main.name = f"GSD Bounding Box.{j}"
    part_document.in_work_object = hybridBody_main.hybrid_bodies
    hybridBody_Extreme_Points = hybridBody_main.hybrid_bodies.add()
    hybridBody_Extreme_Points.name = f"Extreme Points.{j}"
    hybridBody_Planes = hybridBody_main.hybrid_bodies.add()
    hybridBody_Planes.name = f"Planes.{j}"
    hybridBody_Base_Lines = hybridBody_main.hybrid_bodies.add()
    hybridBody_Base_Lines.name = f"Base Lines.{j}"
    hybridBody_Points = hybridBody_main.hybrid_bodies.add()
    hybridBody_Points.name = f"Points.{j}"
    hybridBody_Edge = hybridBody_main.hybrid_bodies.add()
    hybridBody_Edge.name = f"Edge.{j}"
    hybridBody_Surfaces = hybridBody_main.hybrid_bodies.add()
    hybridBody_Surfaces.name = f"Surfaces.{j}"

    part_document.update()
    selection.add(hybridBody_Extreme_Points)
    selection.add(hybridBody_Planes)
    selection.add(hybridBody_Base_Lines)
    selection.add(hybridBody_Points)
    selection.add(hybridBody_Edge)
    selection.add(hybridBody_Surfaces)
    selection.vis_properties.set_show(1)
    selection.clear()

    # promt user select face
    caa.message_box('Select a HybridBodies', 0, title='Selection promt')

    # TODO
    # need test Face

    sFilter = ("Body", "HybridShape", "Face")
    sStatus = selection.select_element2(sFilter, "select a HybridBody", False)
    if (sStatus == "Cancel"):
        caa.message_box('HybridBodies not select', 16, title='Warning')
        exit()

    hb = Body(selection.item(1).value.com_object)
    reference1 = part_document.create_reference_from_object(hb)
    selection.clear()
    
    # create 6 extremum points

    HybridShapeExtremum1 = hsf.add_new_extremum(reference1, Hybrid_Shape_D1, 1)
    HybridShapeExtremum1.direction = Hybrid_Shape_D1
    HybridShapeExtremum1.direction2 = Hybrid_Shape_D2
    HybridShapeExtremum1.direction3 = Hybrid_Shape_D3
    HybridShapeExtremum1.extremum_type = 1
    HybridShapeExtremum1.extremum_type2 = 1
    HybridShapeExtremum1.extremum_type3 = 1
    HybridShapeExtremum1.name = "max_X"

    HybridShapeExtremum2 = hsf.add_new_extremum(reference1, Hybrid_Shape_D1, 0)
    HybridShapeExtremum2.direction = Hybrid_Shape_D1
    HybridShapeExtremum2.direction2 = Hybrid_Shape_D2
    HybridShapeExtremum2.direction3 = Hybrid_Shape_D3
    HybridShapeExtremum2.extremum_type = 0
    HybridShapeExtremum2.extremum_type2 = 0
    HybridShapeExtremum2.extremum_type3 = 0
    HybridShapeExtremum2.name = "min_X"

    HybridShapeExtremum3 = hsf.add_new_extremum(reference1, Hybrid_Shape_D2, 1)
    HybridShapeExtremum3.direction = Hybrid_Shape_D2
    HybridShapeExtremum3.direction2 = Hybrid_Shape_D1
    HybridShapeExtremum3.direction3 = Hybrid_Shape_D3
    HybridShapeExtremum3.extremum_type = 1
    HybridShapeExtremum3.extremum_type2 = 1
    HybridShapeExtremum3.extremum_type3 = 1
    HybridShapeExtremum3.name = "max_Y"

    HybridShapeExtremum4 = hsf.add_new_extremum(reference1, Hybrid_Shape_D2, 0)
    HybridShapeExtremum4.direction = Hybrid_Shape_D2
    HybridShapeExtremum4.direction2 = Hybrid_Shape_D1
    HybridShapeExtremum4.direction3 = Hybrid_Shape_D3
    HybridShapeExtremum4.extremum_type = 0
    HybridShapeExtremum4.extremum_type2 = 0
    HybridShapeExtremum4.extremum_type3 = 0
    HybridShapeExtremum4.name = "min_Y"

    HybridShapeExtremum5 = hsf.add_new_extremum(reference1, Hybrid_Shape_D3, 1)
    HybridShapeExtremum5.direction = Hybrid_Shape_D3
    HybridShapeExtremum5.direction2 = Hybrid_Shape_D1
    HybridShapeExtremum5.direction3 = Hybrid_Shape_D2
    HybridShapeExtremum5.extremum_type = 1
    HybridShapeExtremum5.extremum_type2 = 1
    HybridShapeExtremum5.extremum_type3 = 1
    HybridShapeExtremum5.name = "max_Z"

    HybridShapeExtremum6 = hsf.add_new_extremum(reference1, Hybrid_Shape_D3, 0)
    HybridShapeExtremum6.direction = Hybrid_Shape_D3
    HybridShapeExtremum6.direction2 = Hybrid_Shape_D1
    HybridShapeExtremum6.direction3 = Hybrid_Shape_D2
    HybridShapeExtremum6.extremum_type = 0
    HybridShapeExtremum6.extremum_type2 = 0
    HybridShapeExtremum6.extremum_type3 = 0
    HybridShapeExtremum6.name = "min_Z"

    # append points to Geometrical Set

    hybridBody_Extreme_Points.append_hybrid_shape(HybridShapeExtremum1)
    hybridBody_Extreme_Points.append_hybrid_shape(HybridShapeExtremum2)
    hybridBody_Extreme_Points.append_hybrid_shape(HybridShapeExtremum3)
    hybridBody_Extreme_Points.append_hybrid_shape(HybridShapeExtremum4)
    hybridBody_Extreme_Points.append_hybrid_shape(HybridShapeExtremum5)
    hybridBody_Extreme_Points.append_hybrid_shape(HybridShapeExtremum6)

    # create 12 planes
    # 6 extremum planes

    Plane_Xmax = hsf.add_new_plane_offset_pt(ref_YZ, HybridShapeExtremum1)
    Plane_Xmax.name = "Plane_X_max"
    Plane_Xmin = hsf.add_new_plane_offset_pt(ref_YZ, HybridShapeExtremum2)
    Plane_Xmin.name = "Plane_X_min"

    Plane_Ymax = hsf.add_new_plane_offset_pt(ref_XZ, HybridShapeExtremum3)
    Plane_Ymax.name = "Plane_Y_max"
    Plane_Ymin = hsf.add_new_plane_offset_pt(ref_XZ, HybridShapeExtremum4)
    Plane_Ymin.name = "Plane_Y_min"

    Plane_Zmax = hsf.add_new_plane_offset_pt(ref_XY, HybridShapeExtremum5)
    Plane_Zmax.name = "Plane_Z_max"
    Plane_Zmin = hsf.add_new_plane_offset_pt(ref_XY, HybridShapeExtremum6)
    Plane_Zmin.name = "Plane_Z_min"

    hybridBody_Planes.append_hybrid_shape(Plane_Xmax)
    hybridBody_Planes.append_hybrid_shape(Plane_Xmin)
    hybridBody_Planes.append_hybrid_shape(Plane_Ymax)
    hybridBody_Planes.append_hybrid_shape(Plane_Ymin)
    hybridBody_Planes.append_hybrid_shape(Plane_Zmax)
    hybridBody_Planes.append_hybrid_shape(Plane_Zmin)

    part_document.update_object(Plane_Xmax)
    part_document.update_object(Plane_Xmin)

    # and 6 offset planes
    Plane_Xmax_offset = hsf.add_new_plane_offset(
        Plane_Xmax, Offset_X_max, False)
    Plane_Xmax_offset.name = "Plane_X_max_offset"
    Plane_Xmin_offset = hsf.add_new_plane_offset(
        Plane_Xmin, Offset_X_min, True)
    Plane_Xmin_offset.name = "Plane_X_min_offset"

    Plane_Ymax_offset = hsf.add_new_plane_offset(
        Plane_Ymax, Offset_Y_max, False)
    Plane_Ymax_offset.name = "Plane_Y_max_offset"
    Plane_Ymin_offset = hsf.add_new_plane_offset(
        Plane_Ymin, Offset_Y_min, True)
    Plane_Ymin_offset.name = "Plane_Y_min_offset"

    Plane_Zmax_offset = hsf.add_new_plane_offset(
        Plane_Zmax, Offset_Z_max, False)
    Plane_Zmax_offset.name = "Plane_Z_max_offset"
    Plane_Zmin_offset = hsf.add_new_plane_offset(
        Plane_Zmin, Offset_Z_min, True)
    Plane_Zmin_offset.name = "Plane_Z_min_offset"

    hybridBody_Planes.append_hybrid_shape(Plane_Xmax_offset)
    hybridBody_Planes.append_hybrid_shape(Plane_Xmin_offset)
    hybridBody_Planes.append_hybrid_shape(Plane_Ymax_offset)
    hybridBody_Planes.append_hybrid_shape(Plane_Ymin_offset)
    hybridBody_Planes.append_hybrid_shape(Plane_Zmax_offset)
    hybridBody_Planes.append_hybrid_shape(Plane_Zmin_offset)

    # get bounding box measure
    part_document.update()
    x_length = measure_between_planes(
        part_document.create_reference_from_object(Plane_Xmax),
        part_document.create_reference_from_object(Plane_Xmin),
        document.spa_workbench())
    y_length = measure_between_planes(
        part_document.create_reference_from_object(Plane_Ymax),
        part_document.create_reference_from_object(Plane_Ymin),
        document.spa_workbench())
    z_length = measure_between_planes(
        part_document.create_reference_from_object(Plane_Zmax),
        part_document.create_reference_from_object(Plane_Zmin),
        document.spa_workbench())

    hybridBody_main.name = (
        f"GSD Bounding Box{x_length}x{y_length}[{z_length}].{j}")

    # create intersections offset planes

    # Zmin->Xmax,Xmin,Ymax,Ymin. its enough for bounding box
    # for example
    # fill= hsf.add_new_fill()
    # fill.add_bound(line1,line2,line3,line4)
    # bounding box = pad (fill) up to Zmax plane
    #
    #  Point_H0V1         Line_H1
    #            *-------------------------------*  Point_H1V1
    #            |                               |
    #            |                               |
    #            |                               |
    #            |                               |
    #            | <----- Line_V0                | <---Line_V1
    #            |                               |
    #            |                               |
    #            |                               |
    #            *-------------------------------*
    #  Point_H0V0         Line_H0                   Point_H1V0
    #
    #   Y
    #   ^
    #   |
    #   |
    #   |
    #   |
    #   0-------------> X

    Line_V1 = hsf.add_new_intersection(Plane_Xmax_offset, Plane_Zmin_offset)
    Line_V0 = hsf.add_new_intersection(Plane_Xmin_offset, Plane_Zmin_offset)
    Line_H1 = hsf.add_new_intersection(Plane_Ymax_offset, Plane_Zmin_offset)
    Line_H0 = hsf.add_new_intersection(Plane_Ymin_offset, Plane_Zmin_offset)
    Line_V1.name = "Line_V1"
    Line_V0.name = "Line_V0"
    Line_H1.name = "Line_H1"
    Line_H0.name = "Line_H0"

    # but u can use translate
    # do not intersection directly
    # its not working with cylindrycal object
    # Line_Xmax_Zmax_offset=hsf.add_new_translate(Line_Xmax_Zmin_offset,)
    # Line_Xmin_Zmax_offset=hsf.add_new_translate(Line_Xmin_Zmin_offset,)
    # Line_Ymax_Zmax_offset=hsf.add_new_translate(Line_Ymax_Zmin_offset,)
    # Line_Ymin_Zmax_offset=hsf.add_new_translate(Line_Ymin_Zmin_offset,)

    # append all in wireframe
    hybridBody_Base_Lines.append_hybrid_shape(Line_V1)
    hybridBody_Base_Lines.append_hybrid_shape(Line_V0)
    hybridBody_Base_Lines.append_hybrid_shape(Line_H1)
    hybridBody_Base_Lines.append_hybrid_shape(Line_H0)

    Point_H1V1 = hsf.add_new_intersection(Line_V1, Line_H1)
    Point_H0V1 = hsf.add_new_intersection(Line_V1, Line_H0)
    Point_H1V0 = hsf.add_new_intersection(Line_V0, Line_H1)
    Point_H0V0 = hsf.add_new_intersection(Line_V0, Line_H0)

    Point_H1V1.name = "Point_H1V1"
    Point_H0V1.name = "Point_H0V1"
    Point_H1V0.name = "Point_H1V0"
    Point_H0V0.name = "Point_H0V0"

    hybridBody_Points.append_hybrid_shape(Point_H1V1)
    hybridBody_Points.append_hybrid_shape(Point_H0V1)
    hybridBody_Points.append_hybrid_shape(Point_H1V0)
    hybridBody_Points.append_hybrid_shape(Point_H0V0)

    Point_H1V1_max = hsf.add_new_project(Point_H1V1, Plane_Zmax_offset)
    Point_H1V1_max.direction = Hybrid_Shape_D3
    Point_H0V1_max = hsf.add_new_project(Point_H0V1, Plane_Zmax_offset)
    Point_H0V1_max.direction = Hybrid_Shape_D3
    Point_H1V0_max = hsf.add_new_project(Point_H1V0, Plane_Zmax_offset)
    Point_H1V0_max.direction = Hybrid_Shape_D3
    Point_H0V0_max = hsf.add_new_project(Point_H0V0, Plane_Zmax_offset)
    Point_H0V0_max.direction = Hybrid_Shape_D3

    Point_H1V1_max.name = "Point_H1V1_max"
    Point_H0V1_max.name = "Point_H0V1_max"
    Point_H1V0_max.name = "Point_H1V0_max"
    Point_H0V0_max.name = "Point_H0V0_max"

    # For visual properties
    Point_tuple = (Point_H1V1,
                   Point_H0V1,
                   Point_H1V0,
                   Point_H0V0,
                   Point_H1V1_max,
                   Point_H0V1_max,
                   Point_H1V0_max,
                   Point_H0V0_max)

    hybridBody_Points.append_hybrid_shape(Point_H1V1_max)
    hybridBody_Points.append_hybrid_shape(Point_H0V1_max)
    hybridBody_Points.append_hybrid_shape(Point_H1V0_max)
    hybridBody_Points.append_hybrid_shape(Point_H0V0_max)

   # Create 8 lines for bounding box
   # To Line H0V0->H0V1->H1V1->H1V0->H0V0

    Line_H0V0_H0V1 = hsf.add_new_line_pt_pt(Point_H0V0, Point_H0V1)
    Line_H0V1_H1V1 = hsf.add_new_line_pt_pt(Point_H0V1, Point_H1V1)
    Line_H1V1_H1V0 = hsf.add_new_line_pt_pt(Point_H1V1, Point_H1V0)
    Line_H1V0_H0V0 = hsf.add_new_line_pt_pt(Point_H1V0, Point_H0V0)

    Line_H0V0_H0V1.name = "Line_H0V0_H0V1"
    Line_H0V1_H1V1.name = "Line_H0V1_H1V1"
    Line_H1V1_H1V0.name = "Line_H1V1_H1V0"
    Line_H1V0_H0V0.name = "Line_H1V0_H0V0"

    Line_H0V0_H0V1_Zmax = hsf.add_new_line_pt_pt(
        Point_H0V0_max, Point_H0V1_max)
    Line_H0V1_H1V1_Zmax = hsf.add_new_line_pt_pt(
        Point_H0V1_max, Point_H1V1_max)
    Line_H1V1_H1V0_Zmax = hsf.add_new_line_pt_pt(
        Point_H1V1_max, Point_H1V0_max)
    Line_H1V0_H0V0_Zmax = hsf.add_new_line_pt_pt(
        Point_H1V0_max, Point_H0V0_max)

    Line_H0V0_H0V1_Zmax.name = "Line_H0V0_H0V1_Zmax"
    Line_H0V1_H1V1_Zmax.name = "Line_H0V1_H1V1_Zmax"
    Line_H1V1_H1V0_Zmax.name = "Line_H1V1_H1V0_Zmax"
    Line_H1V0_H0V0_Zmax.name = "Line_H1V0_H0V0_Zmax"

    Line_H1V1_H1V1_max = hsf.add_new_line_pt_pt(Point_H1V1, Point_H1V1_max)
    Line_H0V1_H0V1_max = hsf.add_new_line_pt_pt(Point_H0V1, Point_H0V1_max)
    Line_H1V0_H1V0_max = hsf.add_new_line_pt_pt(Point_H1V0, Point_H1V0_max)
    Line_H0V0_H0V0_max = hsf.add_new_line_pt_pt(Point_H0V0, Point_H0V0_max)

    Line_H1V1_H1V1_max.name = "Line_H1V1_H1V1_max"
    Line_H0V1_H0V1_max.name = "Line_H0V1_H0V1_max"
    Line_H1V0_H1V0_max.name = "Line_H1V0_H1V0_max"
    Line_H0V0_H0V0_max.name = "Line_H0V0_H0V0_max"

    hybridBody_Edge.append_hybrid_shape(Line_H0V0_H0V1)
    hybridBody_Edge.append_hybrid_shape(Line_H0V1_H1V1)
    hybridBody_Edge.append_hybrid_shape(Line_H1V1_H1V0)
    hybridBody_Edge.append_hybrid_shape(Line_H1V0_H0V0)

    hybridBody_Edge.append_hybrid_shape(Line_H0V0_H0V1_Zmax)
    hybridBody_Edge.append_hybrid_shape(Line_H0V1_H1V1_Zmax)
    hybridBody_Edge.append_hybrid_shape(Line_H1V1_H1V0_Zmax)
    hybridBody_Edge.append_hybrid_shape(Line_H1V0_H0V0_Zmax)

    hybridBody_Edge.append_hybrid_shape(Line_H1V1_H1V1_max)
    hybridBody_Edge.append_hybrid_shape(Line_H0V1_H0V1_max)
    hybridBody_Edge.append_hybrid_shape(Line_H1V0_H1V0_max)
    hybridBody_Edge.append_hybrid_shape(Line_H0V0_H0V0_max)

    # Profile for pad
    Profile_Pad = hsf.add_new_join(Line_H0V0_H0V1, Line_H0V1_H1V1)
    Profile_Pad.add_element(Line_H1V1_H1V0)
    Profile_Pad.add_element(Line_H1V0_H0V0)
    Profile_Pad.set_manifold(True)
    Profile_Pad.set_connex(True)
    Profile_Pad.name = f"Profile_Pad.{j}"
    hybridBody_main.append_hybrid_shape(Profile_Pad)

    Wireframe_Bounding_Box = hsf.add_new_join(Line_H0V0_H0V1, Line_H0V1_H1V1)
    Wireframe_Bounding_Box.add_element(Line_H1V1_H1V0)
    Wireframe_Bounding_Box.add_element(Line_H1V0_H0V0)
    Wireframe_Bounding_Box.add_element(Line_H0V0_H0V1_Zmax)
    Wireframe_Bounding_Box.add_element(Line_H0V1_H1V1_Zmax)
    Wireframe_Bounding_Box.add_element(Line_H1V1_H1V0_Zmax)
    Wireframe_Bounding_Box.add_element(Line_H1V0_H0V0_Zmax)
    Wireframe_Bounding_Box.add_element(Line_H1V1_H1V1_max)
    Wireframe_Bounding_Box.add_element(Line_H0V1_H0V1_max)
    Wireframe_Bounding_Box.add_element(Line_H1V0_H1V0_max)
    Wireframe_Bounding_Box.add_element(Line_H0V0_H0V0_max)

    Wireframe_Bounding_Box.name = f"Wireframe_Bounding_Box.{j}"

    # non mainfold
    Wireframe_Bounding_Box.set_manifold(False)

    hybridBody_main.append_hybrid_shape(Wireframe_Bounding_Box)

    # Surface Bounding box
    Fill_Zmin = hsf.add_new_fill()
    Fill_Zmin.add_bound(Line_H0V0_H0V1)
    Fill_Zmin.add_bound(Line_H0V1_H1V1)
    Fill_Zmin.add_bound(Line_H1V1_H1V0)
    Fill_Zmin.add_bound(Line_H1V0_H0V0)

    hybridBody_Surfaces.append_hybrid_shape(Fill_Zmin)

    Fill_Zmax = hsf.add_new_fill()
    Fill_Zmax.add_bound(Line_H0V0_H0V1_Zmax)
    Fill_Zmax.add_bound(Line_H0V1_H1V1_Zmax)
    Fill_Zmax.add_bound(Line_H1V1_H1V0_Zmax)
    Fill_Zmax.add_bound(Line_H1V0_H0V0_Zmax)
    hybridBody_Surfaces.append_hybrid_shape(Fill_Zmax)
    part_document.update()

    """This is error code
    
    Wall_E=hsf.add_new_extrude(part_document.create_reference_from_object(Profile_Pad),20,0,Hybrid_Shape_D3)
    Wall_E.first_limit_type=2
    Wall_E.second_limit_type=2
    Wall_E.compute()
    Wall_E.first_upto_element(part_document.create_reference_from_object(Plane_Zmin_offset))
    Wall_E.second_upto_element(part_document.create_reference_from_object(Plane_Zmax_offset))
    Wall_E.name="Wall_e"
    hybridBody_main.append_hybrid_shape(Wall_E)
    """

    Wall = hsf.add_new_sweep_line(Profile_Pad)
    Wall.mode = 6
    Wall.solution_no = 0
    Wall.smooth_activity = False
    Wall.guide_deviation_activity = False
    Wall.draft_computation_mode = 0
    Wall.draft_direction = Hybrid_Shape_D3
    wall_lim1_ref = part_document.create_reference_from_object(
        Plane_Zmax_offset)
    wall_lim2_ref = part_document.create_reference_from_object(
        Plane_Zmin_offset)
    Wall.set_first_length_definition_type(3, wall_lim1_ref)
    Wall.set_second_length_definition_type(3, wall_lim2_ref)

    """
    for test nothing
    import pythoncom
    vba_nothing = pythoncom.Empty
    ref=part_document.create_reference_from_name("")
    Wall.set_second_length_definition_type(3,ref)
    """

    Wall.setback_value = 0.02
    Wall.fill_twisted_areas = 1
    Wall.c0_vertices_mode = True
    Wall.append_hybrid_shape(Profile_Pad)
    Wall.canonical_detection = 2
    Wall.name = "Wall_sweep"
    hybridBody_Surfaces.append_hybrid_shape(Wall)

    Surface_Bounding_box = hsf.add_new_join(Fill_Zmin, Wall)
    Surface_Bounding_box.add_element(Fill_Zmax)
    Surface_Bounding_box.set_manifold(True)
    Surface_Bounding_box.set_connex(True)
    Surface_Bounding_box.name = f"Surface_Bounding_box.{j}"

    hybridBody_main.append_hybrid_shape(Surface_Bounding_box)

    # solid
    part_document.update_object(Profile_Pad)
    part_document.update_object(Plane_Zmax_offset)

    sf = part_document.shape_factory
    part_document.in_work_object = body1
    ref = part_document.create_reference_from_object(Profile_Pad)
    pad = sf.add_new_pad_from_ref(ref, 50)
    pad.set_direction(ref_axis[2])
    part_document.update()
    pad_1_limit = pad.first_limit
    pad_1_limit.limit_mode = 3
    pad_1_limit.limiting_element = part_document.create_reference_from_object(
        Plane_Zmax_offset).com_object
    part_document.update()

    for pt in Point_tuple:
        selection.add(pt)
    # add vis property to point
    # part must bu updated
    part_document.update()
    selection.vis_properties.set_show(0)
    selection.vis_properties.set_symbol_type(12)
    selection.vis_properties.set_real_color(0, 255, 0, 0)
    selection.clear()
    selection.add(hybridBody_Points)
    selection.vis_properties.set_show(0)
    selection.clear()

    # add vis property to wireframe bounding box
    selection.add(Wireframe_Bounding_Box)
    selection.vis_properties.set_real_width(2, 0)
    selection.vis_properties.set_real_color(255, 255, 8, 0)
    selection.vis_properties.set_real_opacity(180, 0)
    selection.clear()

    # add vis property to Bounding_box Body
    selection.add(Surface_Bounding_box)
    selection.vis_properties.set_real_color(255, 128, 255, 0)
    selection.vis_properties.set_real_opacity(55, 0)
    selection.clear()

    # add vis property to surface bounding box
    part_document.in_work_object = body1
    selection.add(pad)
    selection.vis_properties.set_real_color(128, 0, 255, 0)
    selection.vis_properties.set_real_opacity(55, 0)
    selection.clear()

else:
    print("must be a part")
    caa.message_box("Wrong selection! Application will closed!",
                    16, title="Warring")
    exit()
