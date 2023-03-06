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
##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath('..\\pycatia'))
##########################################################

from pycatia import catia
from pycatia.mec_mod_interfaces.part import Part
from pycatia.mec_mod_interfaces.body import Body
from pycatia.mec_mod_interfaces.axis_system import AxisSystem
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape

from pycatia.hybrid_shape_interfaces.point import Point
from pycatia.hybrid_shape_interfaces.hybrid_shape_point_coord import HybridShapePointCoord
from pycatia.hybrid_shape_interfaces.hybrid_shape_project import HybridShapeProject
#from pycatia.in_interfaces import vis_property_set




caa = catia()

# import headers
caa = catia()
documents = caa.documents
# active document 
document = caa.active_document

#Input offset to bounding box
Offset_X_min=10
Offset_X_max=10

Offset_Y_min=10
Offset_Y_max=10

Offset_Z_min=10
Offset_Z_max=10



if (document.is_part):
    # need to autocomplete
    part_document=Part(document.part.com_object)

    selection=document.selection
    part_document.update()

    hsf=part_document.hybrid_shape_factory

    sFilter=("AxisSystem",)
    sStatus = selection.select_element2(sFilter, "select a  local axis", True)
    Axis_System=AxisSystem(selection.item(1).value.com_object)

    #TODO Need to structurize it    
    Axis_Ref=AxisSystem(selection.item(1).value.com_object)
    Axis_Ref_name=Axis_System.name
    Axis_name=Axis_System.name
    Axis_System.is_current=True
    Axis_System.name ="Create by [PTM].plm-forum.ru and ema3.com"
    Axis_name=Axis_System.name
    Origin_coord=Axis_System.get_origin()
    Origin_Point=HybridShapePointCoord(hsf.add_new_point_coord(Origin_coord[0] ,Origin_coord[1] ,Origin_coord[2] ))
    
    Axis_Ref=part_document.create_reference_from_object(Origin_Point.com_object)
    
    Axis_Coord=Axis_System.get_x_axis()
    Hybrid_Shape_D1=hsf.add_new_direction_by_coord(Axis_Coord[0], Axis_Coord[1], Axis_Coord[2])
    
    Axis_Coord=Axis_System.get_y_axis()
    Hybrid_Shape_D2=hsf.add_new_direction_by_coord(Axis_Coord[0], Axis_Coord[1], Axis_Coord[2])
    
    Axis_Coord=Axis_System.get_z_axis()
    Hybrid_Shape_D3=hsf.add_new_direction_by_coord(Axis_Coord[0], Axis_Coord[1], Axis_Coord[2])

    selection.clear()


    # TODO
    # to end file

    oBodies=part_document.bodies
    j=oBodies.count
    body1=oBodies.add()
    body1.name=f"Bounding_Box.{j}"

    # TODO need structurize Geom sets

    hybridBodies1 = part_document.hybrid_bodies
    hybridBody_BB_element = hybridBodies1.add()
    hybridBody_BB_element.name = "Bounding Box Elements"
    part_document.in_work_object=hybridBody_BB_element
    hybridBody_Extreme_Points=hybridBodies1.add()
    hybridBody_Extreme_Points.name= "Bounding Box Extreme Points"


    # promt user select face
    # caa.message_box('Select a HybridBodies', 0 ,title='Selection promt')
    
    # TODO
    # need test Face

    sFilter=("Body","HybridShape","Face")
    sStatus = selection.select_element2(sFilter, "select a HybridBody", False)
    if (sStatus == "Cancel"):
        caa.message_box('HybridBodies not select', 16 ,title='Warning')
        exit()
    
    hb=Body(selection.item(1).value.com_object)
    reference1=part_document.create_reference_from_object(hb)
    selection.clear()  
    # create 6 extremum points
    
    HybridShapeExtremum1 =hsf.add_new_extremum(reference1, Hybrid_Shape_D1, 1)
    HybridShapeExtremum1.direction=Hybrid_Shape_D1
    HybridShapeExtremum1.direction2=Hybrid_Shape_D2
    HybridShapeExtremum1.direction3=Hybrid_Shape_D3
    HybridShapeExtremum1.extremum_type=1
    HybridShapeExtremum1.extremum_type2=1
    HybridShapeExtremum1.extremum_type3=1
    HybridShapeExtremum1.name="max_X"
    

    HybridShapeExtremum2 = hsf.add_new_extremum(reference1, Hybrid_Shape_D1, 0)
    HybridShapeExtremum2.direction=Hybrid_Shape_D1
    HybridShapeExtremum2.direction2=Hybrid_Shape_D2
    HybridShapeExtremum2.direction3=Hybrid_Shape_D3
    HybridShapeExtremum2.extremum_type=0
    HybridShapeExtremum2.extremum_type2=0
    HybridShapeExtremum2.extremum_type3=0
    HybridShapeExtremum2.name="min_X"


    HybridShapeExtremum3 = hsf.add_new_extremum(reference1, Hybrid_Shape_D2, 1)
    HybridShapeExtremum3.direction=Hybrid_Shape_D2
    HybridShapeExtremum3.direction2=Hybrid_Shape_D1
    HybridShapeExtremum3.direction3=Hybrid_Shape_D3
    HybridShapeExtremum3.extremum_type=1
    HybridShapeExtremum3.extremum_type2=1
    HybridShapeExtremum3.extremum_type3=1
    HybridShapeExtremum3.name="max_Y"
   
    HybridShapeExtremum4 = hsf.add_new_extremum(reference1, Hybrid_Shape_D2, 0)
    HybridShapeExtremum4.direction=Hybrid_Shape_D2
    HybridShapeExtremum4.direction2=Hybrid_Shape_D1
    HybridShapeExtremum4.direction3=Hybrid_Shape_D3
    HybridShapeExtremum4.extremum_type=0
    HybridShapeExtremum4.extremum_type2=0
    HybridShapeExtremum4.extremum_type3=0
    HybridShapeExtremum4.name="min_Y"

    HybridShapeExtremum5 = hsf.add_new_extremum(reference1, Hybrid_Shape_D3, 1)
    HybridShapeExtremum5.direction=Hybrid_Shape_D3
    HybridShapeExtremum5.direction2=Hybrid_Shape_D1
    HybridShapeExtremum5.direction3=Hybrid_Shape_D2
    HybridShapeExtremum5.extremum_type=1
    HybridShapeExtremum5.extremum_type2=1
    HybridShapeExtremum5.extremum_type3=1
    HybridShapeExtremum5.name="max_Z"

    HybridShapeExtremum6 = hsf.add_new_extremum(reference1, Hybrid_Shape_D3, 0)
    HybridShapeExtremum6.direction=Hybrid_Shape_D3
    HybridShapeExtremum6.direction2=Hybrid_Shape_D1
    HybridShapeExtremum6.direction3=Hybrid_Shape_D2
    HybridShapeExtremum6.extremum_type=0
    HybridShapeExtremum6.extremum_type2=0
    HybridShapeExtremum6.extremum_type3=0
    HybridShapeExtremum6.name="min_Z"

    #go to definition append points
    hybridBody2 = hybridBodies1.item("Bounding Box Extreme Points")
    hybridBody2.append_hybrid_shape(HybridShapeExtremum1)
    hybridBody2.append_hybrid_shape(HybridShapeExtremum2)
    hybridBody2.append_hybrid_shape(HybridShapeExtremum3)
    hybridBody2.append_hybrid_shape(HybridShapeExtremum4)
    hybridBody2.append_hybrid_shape(HybridShapeExtremum5)
    hybridBody2.append_hybrid_shape(HybridShapeExtremum6)
      
    # TODO need to send it to end for speedup
    #add vis property to point
    # part must bu updated
    part_document.update()
    # u can search or add
    #selection.search("CatPrtSearch.Point,All")
    selection.add(HybridShapeExtremum1)
    selection.add(HybridShapeExtremum3)
    selection.add(HybridShapeExtremum5)
    selection.vis_properties.set_show(0)
    selection.vis_properties.set_symbol_type(5)
    selection.vis_properties.set_real_color(0,255,0,0)
    selection.clear()

    selection.add(HybridShapeExtremum2)
    selection.add(HybridShapeExtremum4)
    selection.add(HybridShapeExtremum6)
    selection.vis_properties.set_show(0)
    selection.vis_properties.set_symbol_type(5)
    selection.vis_properties.set_real_color(255,0,0,0)
    selection.clear()

    # create 12 planes
    # 6 max planes
    # mb try affinity but this works well)



    selection_XY_plane=f"RSur:(Face:(Brp:({Axis_System.name};1);None:();Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MFBRepVersion_CXR14)"
    selection_XZ_plane=f"RSur:(Face:(Brp:({Axis_System.name};3);None:();Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MFBRepVersion_CXR14)"
    selection_YZ_plane=f"RSur:(Face:(Brp:({Axis_System.name};2);None:();Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MFBRepVersion_CXR14)"
    
    ref_XY=part_document.create_reference_from_b_rep_name(selection_XY_plane,Axis_System)
    ref_XZ=part_document.create_reference_from_b_rep_name(selection_XZ_plane,Axis_System)
    ref_YZ=part_document.create_reference_from_b_rep_name(selection_YZ_plane,Axis_System)

    Plane_Xmax=hsf.add_new_plane_offset_pt(ref_YZ,HybridShapeExtremum1)
    Plane_Xmax.name="Plane_X_max"
    Plane_Xmin=hsf.add_new_plane_offset_pt(ref_YZ,HybridShapeExtremum2)
    Plane_Xmin.name="Plane_X_min"

    Plane_Ymax=hsf.add_new_plane_offset_pt(ref_XZ,HybridShapeExtremum3)
    Plane_Ymax.name="Plane_Y_max"
    Plane_Ymin=hsf.add_new_plane_offset_pt(ref_XZ,HybridShapeExtremum4)
    Plane_Ymin.name="Plane_Y_min"

    Plane_Zmax=hsf.add_new_plane_offset_pt(ref_XY,HybridShapeExtremum5)
    Plane_Zmax.name="Plane_Z_max"
    Plane_Zmin=hsf.add_new_plane_offset_pt(ref_XY,HybridShapeExtremum6)
    Plane_Zmin.name="Plane_Z_min"

    hybridBody2.append_hybrid_shape(Plane_Xmax)
    hybridBody2.append_hybrid_shape(Plane_Xmin)
    hybridBody2.append_hybrid_shape(Plane_Ymax)
    hybridBody2.append_hybrid_shape(Plane_Ymin)
    hybridBody2.append_hybrid_shape(Plane_Zmax)
    hybridBody2.append_hybrid_shape(Plane_Zmin)

    # 6 offset planes
    Plane_Xmax_offset=hsf.add_new_plane_offset(Plane_Xmax,Offset_X_max,False)
    Plane_Xmax_offset.name="Plane_X_max_offset"
    Plane_Xmin_offset=hsf.add_new_plane_offset(Plane_Xmin,Offset_X_min,True)
    Plane_Xmin_offset.name="Plane_X_min_offset"

    Plane_Ymax_offset=hsf.add_new_plane_offset(Plane_Ymax,Offset_Y_max,False)
    Plane_Ymax_offset.name="Plane_Y_max_offset"
    Plane_Ymin_offset=hsf.add_new_plane_offset(Plane_Ymin,Offset_Y_min,True)
    Plane_Ymin_offset.name="Plane_Y_min_offset"

    Plane_Zmax_offset=hsf.add_new_plane_offset(Plane_Zmax,Offset_Z_max,False)
    Plane_Zmax_offset.name="Plane_Z_max_offset"
    Plane_Zmin_offset=hsf.add_new_plane_offset(Plane_Zmin,Offset_Z_min,True)
    Plane_Zmin_offset.name="Plane_Z_min_offset"

    hybridBody2.append_hybrid_shape(Plane_Xmax_offset)
    hybridBody2.append_hybrid_shape(Plane_Xmin_offset)
    hybridBody2.append_hybrid_shape(Plane_Ymax_offset)
    hybridBody2.append_hybrid_shape(Plane_Ymin_offset)
    hybridBody2.append_hybrid_shape(Plane_Zmax_offset)
    hybridBody2.append_hybrid_shape(Plane_Zmin_offset)

    # TODO
    # Measure rough stock




    #create intersections offset planes

    # Zmin->Xmax,Xmin,Ymax,Ymin. its enough for bounding box
    # for example
    # fill= hsf.add_new_fill()
    # fill.add_bound(line1,line2,line3,line4)
    # bounding box = pad (fill) up to Zmax plane
    #
    #  Point_H0V1         Line_H1
    #    *  -------------------------   * Point_H1V1
    #   |                               |
    #   |                               |
    #   |                               |
    #   |                               |
    #   | Line_V0                       |Line_V1
    #   |                               |
    #   |                               |
    #   |               xdirection      |
    #    *  -------------------------> *     Point_H1V0
    #  Point_H0V0             Line_H0


    Line_V1=hsf.add_new_intersection(Plane_Xmax_offset,Plane_Zmin_offset)
    Line_V0=hsf.add_new_intersection(Plane_Xmin_offset,Plane_Zmin_offset)
    Line_H1=hsf.add_new_intersection(Plane_Ymax_offset,Plane_Zmin_offset)
    Line_H0=hsf.add_new_intersection(Plane_Ymin_offset,Plane_Zmin_offset)
    Line_V1.name="Line_V1"
    Line_V0.name="Line_V0"
    Line_H1.name="Line_H1"
    Line_H0.name="Line_H0"

    # but u can use translate and intersect or projection
    # do not intersection directly
    # its not working with cylindrycal object
    # Line_Xmax_Zmax_offset=hsf.add_new_translate(Line_Xmax_Zmin_offset,)
    # Line_Xmin_Zmax_offset=hsf.add_new_translate(Line_Xmin_Zmin_offset,)
    # Line_Ymax_Zmax_offset=hsf.add_new_translate(Line_Ymax_Zmin_offset,)
    # Line_Ymin_Zmax_offset=hsf.add_new_translate(Line_Ymin_Zmin_offset,)

    # append all in wireframe
    hybridBody2.append_hybrid_shape(Line_V1)
    hybridBody2.append_hybrid_shape(Line_V0)
    hybridBody2.append_hybrid_shape(Line_H1)
    hybridBody2.append_hybrid_shape(Line_H0)

    Point_H1V1=hsf.add_new_intersection(Line_V1,Line_H1)
    Point_H0V1=hsf.add_new_intersection(Line_V1,Line_H0)
    Point_H1V0=hsf.add_new_intersection(Line_V0,Line_H1)
    Point_H0V0=hsf.add_new_intersection(Line_V0,Line_H0)

    Point_H1V1.name="Point_H1V1"
    Point_H0V1.name="Point_H0V1"
    Point_H1V0.name="Point_H1V0"
    Point_H0V0.name="Point_H0V0"

    hybridBody2.append_hybrid_shape(Point_H1V1)
    hybridBody2.append_hybrid_shape(Point_H0V1)
    hybridBody2.append_hybrid_shape(Point_H1V0)
    hybridBody2.append_hybrid_shape(Point_H0V0)

    # Oo need to refact

    Point_H1V1_max=hsf.add_new_project(Point_H1V1,Plane_Zmax_offset)
    Point_H1V1_max.direction=Hybrid_Shape_D3
    Point_H0V1_max=hsf.add_new_project(Point_H0V1,Plane_Zmax_offset)
    Point_H0V1_max.direction=Hybrid_Shape_D3
    Point_H1V0_max=hsf.add_new_project(Point_H1V0,Plane_Zmax_offset)
    Point_H1V0_max.direction=Hybrid_Shape_D3
    Point_H0V0_max=hsf.add_new_project(Point_H0V0,Plane_Zmax_offset)
    Point_H0V0_max.direction=Hybrid_Shape_D3

    Point_H1V1_max.name="Point_H1V1_max"
    Point_H0V1_max.name="Point_H0V1_max"
    Point_H1V0_max.name="Point_H1V0_max"
    Point_H0V0_max.name="Point_H0V0_max"


    hybridBody2.append_hybrid_shape(Point_H1V1_max)
    hybridBody2.append_hybrid_shape(Point_H0V1_max)
    hybridBody2.append_hybrid_shape(Point_H1V0_max)
    hybridBody2.append_hybrid_shape(Point_H0V0_max)

   # Create 8 lines for bounding box
   # TODO need to create geom set
    Line_H1V1_H1V1_max=hsf.add_new_line_pt_pt(Point_H1V1,Point_H1V1_max)
    Line_H0V1_H0V1_max=hsf.add_new_line_pt_pt(Point_H0V1,Point_H0V1_max)
    Line_H1V0_H1V0_max=hsf.add_new_line_pt_pt(Point_H1V0,Point_H1V0_max)
    Line_H0V0_H0V0_max=hsf.add_new_line_pt_pt(Point_H0V0,Point_H0V0_max)
    
    # Wireframe_Bounding_box=hsf.add_new_join()


    
    hybridBody2.append_hybrid_shape(Line_H1V1_H1V1_max)
    hybridBody2.append_hybrid_shape(Line_H0V1_H0V1_max)
    hybridBody2.append_hybrid_shape(Line_H1V0_H1V0_max)
    hybridBody2.append_hybrid_shape(Line_H0V0_H0V0_max)




    #pad
    #update





    """
    Hybrid_Shape_D1 = hsf.AddNewDirectionByCoord(AxisCoord(0), AxisCoord(1), AxisCoord(2))
				axissyst.GetYAxis AxisCoord
				Set hybridShapeD2 = hybridShapeFactory1.AddNewDirectionByCoord(AxisCoord(0), AxisCoord(1), AxisCoord(2))
				axissyst.GetZAxis AxisCoord
				Set hybridShapeD3 = hybridShapeFactory1.AddNewDirectionByCoord(AxisCoord(0), AxisCoord(1), AxisCoord(2))
    """
else:
    print("must be a part")

"""
# update part.
part.update()
"""