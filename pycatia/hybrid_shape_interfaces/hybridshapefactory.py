#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.factory import Factory
from .hybridshapepointcoord import HybridShapePointCoord
from .hybridshapelineptpt import HybridShapeLinePtPt


class HybridShapeFactory(Factory):
    """
        .. note::
            CAA V5 Visual Basic help

                | Interface to create all kinds of HybridShape objects that may be
                | needed in wireframe and surface design.Note:This interface concern
                | GSD/GSO/DL1 feature creation via VBUse of the creation methods
                | requires to have granted license configuration for feature
                | creationi.e:- Bump, Develop,WrapCurve,WrapSurface require GSO
                | license.- Unfold,  Develop require DL1 license.- Other require GSD
                | license.Note2:For all methods creating datums AddNew*Datum,the object
                | passed as parameter to create the datum has to be in the current
                | container.Otherwise, an error occurs.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_factory = com_object

    def add_new_3d_corner(self, i_element_1, i_element_2, i_direction, i_radius, i_orientation_1, i_orientation_2,
                          i_trim):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNew3DCorner
                | o Func AddNew3DCorner(        iElement1,
                |                               iElement2,
                |                               iDirection,
                |                               iRadius,
                |                               iOrientation1,
                |                               iOrientation2,
                |                               iTrim) As
                | 
                | Creates a new 3D Corner within the current body. Create a 3D
                | corner curve between a point and a curve or 2 curves along a
                | direction.
                |
                | Parameters:
                | iElement1
                |     First reference curve.
                |  
                |  iElement2
                |     Second reference curve.
                |  
                |  iDirection
                |     Direction.
                |  
                |  iRadius
                |     Radius of the corner.
                |  
                |  iOrientation1
                |     Manage the corner center position.
                |    Value can be 1 or -1 
                |  
                |  iOrientation2
                |     Manage the corner center position.
                |    Value can be 1 or -1     
                |  
                |  iTrim
                |     Value can be FALSE or TRUE
                |    if TRUE the 2 curves are trimed and asembled with the corner.
                |  
                |  oCorner
                |     Created corner.


        :param i_element_1:
        :param i_element_2:
        :param i_direction:
        :param i_radius:
        :param i_orientation_1:
        :param i_orientation_2:
        :param i_trim:
        :return:
        """
        return self.hybrid_shape_factory.AddNew3DCorner(i_element_1, i_element_2, i_direction, i_radius,
                                                        i_orientation_1, i_orientation_2, i_trim)

    def add_new_3d_curve_offset(self, i_curve_to_offset, i_direction, i_offset, i_corner_radius, i_corner_tension):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNew3DCurveOffset
                | o Func AddNew3DCurveOffset(        iCurveToOffset,
                |                                    iDirection,
                |                                    iOffset,
                |                                    iCornerRadius,
                |                                    iCornerTension) As
                | 
                | Creates a 3D Curve Offset.
                |
                | Parameters:
                | iCurve
                |       The curve to offset
                |    
                |  iDirection
                |       Offset pulling direction.
                |    
                |  iOffsetValue
                |       Offset Value.
                |    
                |  iCornerRadius
                |       Radius of the 3D corners.
                |    
                |  iCornerTension
                |       Tension of the 3D corners.
                |    
                | 
                |  Returns:
                |   CATIGSM3DCurveOffset_var      created 3DCurveOffset.


        :param i_curve_to_offset:
        :param i_direction:
        :param i_offset:
        :param i_corner_radius:
        :param i_corner_tension:
        :return:
        """
        return self.hybrid_shape_factory.AddNew3DCurveOffset(i_curve_to_offset, i_direction, i_offset, i_corner_radius,
                                                             i_corner_tension)

    def add_new_affinity(self, i_element, i_x_ratio, i_y_ratio, i_z_ratio):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewAffinity
                | o Func AddNewAffinity(        iElement,
                |                               iXRatio,
                |                               iYRatio,
                |                               iZRatio) As
                | 
                | Creates a new Affinity within the current body.
                |
                | Parameters:
                | iElement
                |     point, curve, surface or solid.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                | , 
                |  and 
                | . 
                |      iXRatio
                |     Ratio of affinity in iX direction. 
                |  
                |  iYRatio
                |     Ratio of affinity in iY direction.
                |  
                |  iZRatio
                |     Ratio of affinity in iZ direction.  
                |  
                |  oAffinity
                |     Created affinity


        :param i_element:
        :param i_x_ratio:
        :param i_y_ratio:
        :param i_z_ratio:
        :return:
        """
        return self.hybrid_shape_factory.AddNewAffinity(i_element, i_x_ratio, i_y_ratio, i_z_ratio)

    def add_new_axis_line(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewAxisLine
                | o Func AddNewAxisLine(        iElement) As
                | 
                | Creates a new AxisLine within the current body.
                |
                | Parameters:
                | iElement
                |    Circle, Ellipse, Oblong, Sphere, Revolution surface. Axis is computed for this element
                |  
                |  oAxisLine
                |     Created axis line


        :param i_element:
        :return:
        """
        return self.hybrid_shape_factory.AddNewAxisLine(i_element)

    def add_new_axis_to_axis(self, i_object, i_reference_axis, i_target_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewAxisToAxis
                | o Func AddNewAxisToAxis(        iObject,
                |                                 iReferenceAxis,
                |                                 iTargetAxis) As
                | 
                | Creates a new axis to axis transformation within the current
                | body.
                |
                | Parameters:
                | iObject
                |     Point, curve, surface or solid to transform.
                |  
                |  iReferenceAxis
                |    reference axis system
                |  
                |  iTargetAxis
                |    target axis system
                |  
                |  oAxisToAxis
                |     Created axis to axis transformation.


        :param i_object:
        :param i_reference_axis:
        :param i_target_axis:
        :return:
        """
        return self.hybrid_shape_factory.AddNewAxisToAxis(i_object, i_reference_axis, i_target_axis)

    def add_new_blend(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewBlend
                | o Func AddNewBlend(    ) As
                | 
                | Creates a new blend surface within the current body.
                |
                | Parameters:
                | oBlend
                |    The Blend object if succeded


        :return:
        """
        return self.hybrid_shape_factory.AddNewBlend()

    def add_new_boundary(self, i_initial_element, i_support, i_typede_propagation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewBoundary
                | o Func AddNewBoundary(        iInitialElement,
                |                               iSupport,
                |                               iTypedePropagation) As
                | 
                | Creates a new Boundary within the current body.
                |
                | Parameters:
                | iInitialElement
                |     the element used to initialise the propagation around the surface 
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iSupport
                |     the surface used to compute the boundary around it
                | Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iTypedePropagation
                |    Propagation type the values are:
                |      0  for Boundary for all edges
                |      1  for Boundary propagation for edges on connexe point
                |      2  for Boundary propagation for edges  tangent at point  breaks
                |      3  for Boundary not propagation from the current edge
                |  
                |  oBoundary
                |     The computed element


        :param i_initial_element:
        :param i_support:
        :param i_typede_propagation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewBoundary(i_initial_element, i_support, i_typede_propagation)

    def add_new_boundary_of_surface(self, surface):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewBoundaryOfSurface
                | o Func AddNewBoundaryOfSurface(        Surface) As
                | 
                | Creates a Boundary within the current body.
                |
                | Parameters:
                | iSurface
                |     the feature on which all the boundaries will be computed  
                |  
                |  oBoundary
                |     the whole boundary of the Surface given in first parameter


        :param surface:
        :return:
        """
        return self.hybrid_shape_factory.AddNewBoundaryOfSurface(surface)

    def add_new_bump(self, i_body_to_bump):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewBump
                | o Func AddNewBump(        iBodyToBump) As
                | 
                | Creates a new Bump within the current body. Note: require
                | GSO license.
                |
                | Parameters:
                | :
                |  iBodyToBump    Body to deform witn a Bump  
                |  
                | :
                |  oBump    Bump result


        :param i_body_to_bump:
        :return:
        """
        return self.hybrid_shape_factory.AddNewBump(i_body_to_bump)

    def add_new_circle2_points_rad(self, i_point_1, i_point_2, i_support, i_geodesic, i_radius, i_ori):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircle2PointsRad
                | o Func AddNewCircle2PointsRad(        iPoint1,
                |                                       iPoint2,
                |                                       iSupport,
                |                                       iGeodesic,
                |                                       iRadius,
                |                                       iOri) As
                | 
                | Creates a new Circle passing through 2 points with a radius
                | within the current body.
                |
                | Parameters:
                | iPoint1
                |     first passing point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPoint2
                |     second passing point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iSupport
                |     support surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iGeodesic
                |     Puts the circle on the surface.
                |  
                |  iRadius
                |     Value specified is considered as radius. To use this value as diameter,
                |    set DiameterMode using SetDiameterMode method
                |  
                |  iOri
                |     circle orientation.
                |    Defines the side where circle is computed using the normal direction of line between the 2 passing points.
                |  
                |  oCircle
                |    The Circle object if succeded


        :param i_point_1:
        :param i_point_2:
        :param i_support:
        :param i_geodesic:
        :param i_radius:
        :param i_ori:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircle2PointsRad(i_point_1, i_point_2, i_support, i_geodesic, i_radius,
                                                                i_ori)

    def add_new_circle3_points(self, i_point_1, i_point_2, i_point_3):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircle3Points
                | o Func AddNewCircle3Points(        iPoint1,
                |                                    iPoint2,
                |                                    iPoint3) As
                | 
                | Creates a new circle passing through 3 points within the
                | current body.
                |
                | Parameters:
                | iPoint1
                |     first passing point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPoint2
                |     second passing point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iPoint3
                |     third passing point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      oCircle
                |    Created circle


        :param i_point_1:
        :param i_point_2:
        :param i_point_3:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircle3Points(i_point_1, i_point_2, i_point_3)

    def add_new_circle_bitangent_point(self, i_curve_1, i_curve_2, i_point, i_support, i_ori_1, i_ori_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircleBitangentPoint
                | o Func AddNewCircleBitangentPoint(        iCurve1,
                |                                           iCurve2,
                |                                           iPoint,
                |                                           iSupport,
                |                                           iOri1,
                |                                           iOri2) As
                | 
                | Creates a new circle tangent to 2 curves and passing through
                | one point within the current body.
                |
                | Parameters:
                | iCurve1
                |     first curve to which the circle will be tangent.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iCurve2
                |     second curve to which the circle will be tangent.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | . 
                |      iPoint
                |     passing point. This point must lie on second curve.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iSupport
                |     support surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iOri1
                |     first curve orientation for circle computation.
                |  
                |  iOri2
                |     second curve orientation for circle computation.
                |  
                |  oCircle
                |    Created circle


        :param i_curve_1:
        :param i_curve_2:
        :param i_point:
        :param i_support:
        :param i_ori_1:
        :param i_ori_2:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircleBitangentPoint(i_curve_1, i_curve_2, i_point, i_support, i_ori_1,
                                                                    i_ori_2)

    def add_new_circle_bitangent_radius(self, i_curve_1, i_curve_2, i_support, i_radius, i_ori_1, i_ori_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircleBitangentRadius
                | o Func AddNewCircleBitangentRadius(        iCurve1,
                |                                            iCurve2,
                |                                            iSupport,
                |                                            iRadius,
                |                                            iOri1,
                |                                            iOri2) As
                | 
                | Creates a new circle tangent to 2 curves and with a radius
                | within the current body.
                |
                | Parameters:
                | iCurve1
                |     first curve to which the circle will be tangent.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iCurve2
                |     second curve to which the circle will be tangent.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | . 
                |      iSupport
                |     support surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iRadius
                |     Value specified is considered as radius. To use this value as diameter,
                |    set DiameterMode using SetDiameterMode method
                |  
                |  iOri1
                |     first curve orientation for circle computation.
                |  
                |  iOri2
                |     second curve orientation for circle computation.
                |  
                |  oCircle
                |    Created circle


        :param i_curve_1:
        :param i_curve_2:
        :param i_support:
        :param i_radius:
        :param i_ori_1:
        :param i_ori_2:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircleBitangentRadius(i_curve_1, i_curve_2, i_support, i_radius, i_ori_1,
                                                                     i_ori_2)

    def add_new_circle_center_axis(self, i_axis, i_point, i_value, i_projection):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircleCenterAxis
                | o Func AddNewCircleCenterAxis(        iAxis,
                |                                       iPoint,
                |                                       iValue,
                |                                       iProjection) As
                | 
                | Creates a circle from point and axis.
                |
                | Parameters:
                | iAxis
                |    Axis of plane in which circle is lying
                |  
                |  iPoint
                |     Point used for center computation. It will be the center if ProjectionMode
                |    is False. If ProjectionMode = True, this point will be projected on to axis/line
                |  
                |  iValue
                |     Value specified is considered as radius. To use this value as diameter,
                |    set DiameterMode property
                |  
                |  iProjection
                |     Sets Projection Mode. ProjectionMode = TRUE implies point will be projected on to axis/line,
                |    ProjectionMode = FALSE implies that point will be center of the circle. 
                |  
                |  oCircle
                |    Created circle


        :param i_axis:
        :param i_point:
        :param i_value:
        :param i_projection:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircleCenterAxis(i_axis, i_point, i_value, i_projection)

    def add_new_circle_center_axis_with_angles(self, i_axis, i_point, i_value, i_projection, i_start_angle,
                                               i_end_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircleCenterAxisWithAngles
                | o Func AddNewCircleCenterAxisWithAngles(        iAxis,
                |                                                 iPoint,
                |                                                 iValue,
                |                                                 iProjection,
                |                                                 iStartAngle,
                |                                                 iEndAngle) As
                | 
                | Creates a circle from point and axis.
                |
                | Parameters:
                | iAxis
                |    Axis of plane in which circle is lying
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                |      iPoint
                |     Point used for center computation. It will be the center if ProjectionMode
                |    is False. If ProjectionMode = True, this point will be projected on to axis/line
                |  Sub-element(s) supported (see 
                |  object):  
                |      iValue
                |     Value specified is considered as radius. To use this value as diameter,
                |    set DiameterMode property
                |  
                |  iProjection
                |     Sets Projection Mode. ProjectionMode = TRUE implies point will be projected on to axis/line,
                |    ProjectionMode = FALSE implies that point will be center of the circle. 
                |  
                |  iStartAngle
                |     start angle
                |  
                |  iEndAngle
                |     end angle
                |  
                |  oCircle
                |    Created circle


        :param i_axis:
        :param i_point:
        :param i_value:
        :param i_projection:
        :param i_start_angle:
        :param i_end_angle:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircleCenterAxisWithAngles(i_axis, i_point, i_value, i_projection,
                                                                          i_start_angle, i_end_angle)

    def add_new_circle_center_tangent(self, i_center_elem, i_tangent_curve, i_support, i_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircleCenterTangent
                | o Func AddNewCircleCenterTangent(        iCenterElem,
                |                                          iTangentCurve,
                |                                          iSupport,
                |                                          iRadius) As
                | 
                | Creates a new circle with given center element and tangent
                | curve.
                |
                | Parameters:
                | iCenterElem
                |     Can be either curve or point.
                |  
                |  iTangentCurve
                |     Curve to which the circle will be tangent.
                |  
                |  iSupport
                |     support surface or plane.
                |  
                |  iRadius
                |     circle radius, valid only if center element is curve. Value specified is considered as radius. 
                |    To use this value as diameter, set DiameterMode using SetDiameterMode method
                |  
                |  oCircle
                |    Created circle


        :param i_center_elem:
        :param i_tangent_curve:
        :param i_support:
        :param i_radius:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircleCenterTangent(i_center_elem, i_tangent_curve, i_support, i_radius)

    def add_new_circle_ctr_pt(self, i_center, i_crossing_point, i_support, i_geodesic):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircleCtrPt
                | o Func AddNewCircleCtrPt(        iCenter,
                |                                  iCrossingPoint,
                |                                  iSupport,
                |                                  iGeodesic) As
                | 
                | Creates a new whole circle defined by its center, a passing
                | point within the current body.
                |
                | Parameters:
                | iCenter
                |     circle center.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iCrossingPoint
                |     passing point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iSupport
                |     support surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iGeodesic
                |     Puts the circle on the surface.
                |  
                |  oCircle
                |    CreatedCircle


        :param i_center:
        :param i_crossing_point:
        :param i_support:
        :param i_geodesic:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircleCtrPt(i_center, i_crossing_point, i_support, i_geodesic)

    def add_new_circle_ctr_pt_with_angles(self, i_center, i_crossing_point, i_support, i_geodesic, i_start_angle,
                                          i_end_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircleCtrPtWithAngles
                | o Func AddNewCircleCtrPtWithAngles(        iCenter,
                |                                            iCrossingPoint,
                |                                            iSupport,
                |                                            iGeodesic,
                |                                            iStartAngle,
                |                                            iEndAngle) As
                | 
                | Creates a new circle defined by its center, a passing point
                | and angles within the current body.
                |
                | Parameters:
                | iCenter
                |     circle center.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iCrossingPoint
                |     passing point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iSupport
                |     support surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iGeodesic
                |     Puts the circle on the surface.
                |  
                |  iStartAngle
                |     start angle
                |  
                |  iEndAngle
                |     end angle
                |  
                |  oCircle
                |    Created circle


        :param i_center:
        :param i_crossing_point:
        :param i_support:
        :param i_geodesic:
        :param i_start_angle:
        :param i_end_angle:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircleCtrPtWithAngles(i_center, i_crossing_point, i_support, i_geodesic,
                                                                     i_start_angle, i_end_angle)

    def add_new_circle_ctr_rad(self, i_center, i_support, i_geodesic, i_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircleCtrRad
                | o Func AddNewCircleCtrRad(        iCenter,
                |                                   iSupport,
                |                                   iGeodesic,
                |                                   iRadius) As
                | 
                | Creates a new whole circle defined by its center and a
                | radius within the current body.
                |
                | Parameters:
                | iCenter
                |     circle center.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iSupport
                |     support surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iGeodesic
                |     Puts the circle on the surface.
                |  
                |  iRadius
                |     Value specified is considered as radius. To use this value as diameter,
                |    set DiameterMode using SetDiameterMode method
                |  
                |  oCircle
                |    Created circle


        :param i_center:
        :param i_support:
        :param i_geodesic:
        :param i_radius:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircleCtrRad(i_center, i_support, i_geodesic, i_radius)

    def add_new_circle_ctr_rad_with_angles(self, i_center, i_support, i_geodesic, i_radius, i_start_angle, i_end_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircleCtrRadWithAngles
                | o Func AddNewCircleCtrRadWithAngles(        iCenter,
                |                                             iSupport,
                |                                             iGeodesic,
                |                                             iRadius,
                |                                             iStartAngle,
                |                                             iEndAngle) As
                | 
                | Creates a new circle defined by its center, a radius and
                | angles within the current body.
                |
                | Parameters:
                | iCenter
                |     circle center.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iSupport
                |     support surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iGeodesic
                |     Puts the circle on the surface.
                |  
                |  iRadius
                |     Value specified is considered as radius. To use this value as diameter,
                |    set DiameterMode using SetDiameterMode method
                |  
                |  iStartAngle
                |     start angle
                |  
                |  iEndAngle
                |     end angle
                |  
                |  oCircle
                |    Created circle


        :param i_center:
        :param i_support:
        :param i_geodesic:
        :param i_radius:
        :param i_start_angle:
        :param i_end_angle:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircleCtrRadWithAngles(i_center, i_support, i_geodesic, i_radius,
                                                                      i_start_angle, i_end_angle)

    def add_new_circle_datum(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircleDatum
                | o Func AddNewCircleDatum(        iObject) As
                | 
                | Creates a new datum of circle within the current body.
                |
                | Parameters:
                | iObject
                |     The object whose topological body will be duplicated and put into created datum
                |  
                |  oCircle
                |    Created datum
                |  Note2: the object passed as parameter to create the datum has to be in the current container.
                |  Otherwise, an error occurs.


        :param i_object:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircleDatum(i_object)

    def add_new_circle_tritangent(self, i_curve_1, i_curve_2, i_curve_3, i_support, i_ori_1, i_ori_2, i_ori_3):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCircleTritangent
                | o Func AddNewCircleTritangent(        iCurve1,
                |                                       iCurve2,
                |                                       iCurve3,
                |                                       iSupport,
                |                                       iOri1,
                |                                       iOri2,
                |                                       iOri3) As
                | 
                | Creates a new tritangent circle within the current body.
                |
                | Parameters:
                | iCurve1
                |     first curve to which the circle will be tangent.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iCurve2
                |     second curve to which the circle will be tangent.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | . 
                |      iCurve3
                |     third curve to which the circle will be tangent.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | . 
                |      iSupport
                |     support surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iOri1
                |     first curve orientation for circle computation.
                |  
                |  iOri2
                |     second curve orientation for circle computation.
                |  
                |  iOri3
                |     third curve orientation for circle computation.
                |  
                |  oCircle
                |    Created circle


        :param i_curve_1:
        :param i_curve_2:
        :param i_curve_3:
        :param i_support:
        :param i_ori_1:
        :param i_ori_2:
        :param i_ori_3:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCircleTritangent(i_curve_1, i_curve_2, i_curve_3, i_support, i_ori_1,
                                                                i_ori_2, i_ori_3)

    def add_new_combine(self, i_first_curve, i_second_curve, i_nearest_solutions):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCombine
                | o Func AddNewCombine(        iFirstCurve,
                |                              iSecondCurve,
                |                              iNearestSolutions) As
                | 
                | Creates a new Combine within the current body. By default,
                | the combine direction is the normal of each curve. If you
                | want to change see CATIAHybridShapeCombine interfaces.
                |
                | Parameters:
                | iFirstCurve
                |    First curve to combine
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | .   
                |      iSecondCurve
                |     Second curve to combine
                | Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | .   
                |      iNearestSolution
                |     If more than one solution, to choose the nearest solution of the first curve  
                |  
                |  oCombine
                |    The combine object if succeded


        :param i_first_curve:
        :param i_second_curve:
        :param i_nearest_solutions:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCombine(i_first_curve, i_second_curve, i_nearest_solutions)

    def add_new_conic(self, i_support, i_starting_point, i_end_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewConic
                | o Func AddNewConic(        iSupport,
                |                            iStartingPoint,
                |                            iEndPoint) As
                | 
                | Creates a new conic within the current body.
                |
                | Parameters:
                | iSupport
                |       The conic support (always a plane).
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | .   
                |      iStartingPoint
                |       Starting Point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | .   
                |      iEndPoint
                |       End Point
                | Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      oConic
                |    The Conic object if succeded


        :param i_support:
        :param i_starting_point:
        :param i_end_point:
        :return:
        """
        return self.hybrid_shape_factory.AddNewConic(i_support, i_starting_point, i_end_point)

    def add_new_conical_reflect_line_with_type(self, i_support, i_origin, i_angle, i_orientation_support, i_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewConicalReflectLineWithType
                | o Func AddNewConicalReflectLineWithType(        iSupport,
                |                                                 iOrigin,
                |                                                 iAngle,
                |                                                 iOrientationSupport,
                |                                                 iType) As
                | 
                | Creates a new conical ReflectLine within the current body.
                | Create a conical reflectline curve on a support surface from
                | an origin point with an angle.
                |
                | Parameters:
                | iSupport
                |     Support surface.
                |  
                |  iOrigin
                |     Origin point.
                |  
                |  iAngle
                |     Angle of the reflectline.
                |  
                |  iOrientationSupport
                |     Manage the angle used to compute the reflectline.
                |    Value can be 1 or -1 
                |  
                |  iType
                |     Manage the type used to compute the reflectline.
                |    Value can be 0 or 1
                |    Returns or sets whether the reflectline curve is or should be created with the normal
                |    to the support or the tangent plane to the support.
                |    Role: The TypeSolution indicates whether the created reflectline curve
                |    is compute with the angle between the normale to the support and the direction 
                |    or with the angle between the tangent plane to the support and the direction..
                |    Legal values: 0 for the normal and 1 for the tangent plane.
                |  
                |  oReflectLine
                |     Created conical reflectline.


        :param i_support:
        :param i_origin:
        :param i_angle:
        :param i_orientation_support:
        :param i_type:
        :return:
        """
        return self.hybrid_shape_factory.AddNewConicalReflectLineWithType(i_support, i_origin, i_angle,
                                                                          i_orientation_support, i_type)

    def add_new_connect(self, i_curve_1, i_point_1, i_orient_1, i_continuity_1, i_tension_1, i_curve_2, i_point_2,
                        i_orient_2, i_continuity_2, i_tension_2, trim):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewConnect
                | o Func AddNewConnect(        iCurve1,
                |                              iPoint1,
                |                              iOrient1,
                |                              iContinuity1,
                |                              iTension1,
                |                              iCurve2,
                |                              iPoint2,
                |                              iOrient2,
                |                              iContinuity2,
                |                              iTension2,
                |                              Trim) As
                | 
                | Creates a new Connect within the current body.
                |
                | Parameters:
                | iCurve1
                |     First curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | .   
                |      iPoint1
                |     First point (lying on the first curve)
                | Sub-element(s) supported (see 
                |  object):  see 
                | .   
                |      iOrient1
                |     Orientation on the first curve  
                |  
                |  iContinuity1
                |     Continuity on first curve  
                |  
                |  iTension1
                |     Tension on first curve    
                |  
                |  iCurve2
                |     Second curve.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | .   
                |      iPoint2
                |     Second point (lying on the second curve)
                | Sub-element(s) supported (see 
                |  object):  see 
                | .   
                |      iOrient2
                |     Orientation on the second curve  
                |  
                |  iContinuity2
                |     Continuity on second curve  
                |  
                |  iTension2
                |     Tension on second curve  
                |  
                |  iTrim
                |     Trim the two curves with the connect  
                |  
                |  oConnect
                |     The connect object


        :param i_curve_1:
        :param i_point_1:
        :param i_orient_1:
        :param i_continuity_1:
        :param i_tension_1:
        :param i_curve_2:
        :param i_point_2:
        :param i_orient_2:
        :param i_continuity_2:
        :param i_tension_2:
        :param trim:
        :return:
        """
        return self.hybrid_shape_factory.AddNewConnect(i_curve_1, i_point_1, i_orient_1, i_continuity_1, i_tension_1,
                                                       i_curve_2, i_point_2, i_orient_2, i_continuity_2, i_tension_2,
                                                       trim)

    def add_new_corner(self, i_element_1, i_element_2, i_support, i_radius, i_orientation_1, i_orientation_2, i_trim):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCorner
                | o Func AddNewCorner(        iElement1,
                |                             iElement2,
                |                             iSupport,
                |                             iRadius,
                |                             iOrientation1,
                |                             iOrientation2,
                |                             iTrim) As
                | 
                | Creates a new Corner within the current body. Create a
                | corner curve between a point and a curve or 2 curves on a
                | support surface.
                |
                | Parameters:
                | iElement1
                |     First reference curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      iElement2
                |     Second reference curve.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      iSupport
                |     Support surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iRadius
                |     Radius of the corner.
                |  
                |  iOrientation1
                |     Manage the corner center position.
                |    Value can be 1 or -1 
                |  
                |  iOrientation2
                |     Manage the corner center position.
                |    Value can be 1 or -1     
                |  
                |  iTrim
                |     Value can be FALSE or TRUE
                |    if TRUE the 2 curves are trimed and asembled with the corner.
                |  
                |  oCorner
                |     Created corner.


        :param i_element_1:
        :param i_element_2:
        :param i_support:
        :param i_radius:
        :param i_orientation_1:
        :param i_orientation_2:
        :param i_trim:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCorner(i_element_1, i_element_2, i_support, i_radius, i_orientation_1,
                                                      i_orientation_2, i_trim)

    def add_new_curve_datum(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCurveDatum
                | o Func AddNewCurveDatum(        iObject) As
                | 
                | Creates a new datum of curve within the current body.
                |
                | Parameters:
                | iObject
                |     The object whose topological body will be duplicated and put into created datum
                |  
                |  oCurve
                |    Created curve
                |  Note2: the object passed as parameter to create the datum has to be in the current container.
                |  Otherwise, an error occurs.


        :param i_object:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCurveDatum(i_object)

    def add_new_curve_par(self, curve, support, distance, invert_direction, geodesic):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCurvePar
                | o Func AddNewCurvePar(        Curve,
                |                               Support,
                |                               Distance,
                |                               InvertDirection,
                |                               Geodesic) As
                | 
                | Creates a new CurvePar within the current body.
                |
                | Parameters:
                | iCurve
                |     Reference curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | .   
                |      iSupport
                |     Support on which the curve is lying on
                | Sub-element(s) supported (see 
                |  object):  see 
                | .   
                |      iDistance
                |     Distance value  
                |  
                |  iInvertDirection
                |     Orientation
                |  
                |  iGeodesic
                |     Geodesic mode    
                |  
                |  oCurvePar
                |     Parallel curve


        :param curve:
        :param support:
        :param distance:
        :param invert_direction:
        :param geodesic:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCurvePar(curve, support, distance, invert_direction, geodesic)

    def add_new_curve_smooth(self, ip_ia_curve):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCurveSmooth
                | o Func AddNewCurveSmooth(        ipIACurve) As
                | 
                | Creates a new CurveSmooth within the current body.
                |
                | Parameters:
                | iCurve
                |     Reference curve to be smoothened   
                |  
                |  oCurveSmooth
                |     Smoothened curve


        :param ip_ia_curve:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCurveSmooth(ip_ia_curve)

    def add_new_cylinder(self, i_center, i_radius, i_first_length, i_second_length, i_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewCylinder
                | o Func AddNewCylinder(        iCenter,
                |                               iRadius,
                |                               iFirstLength,
                |                               iSecondLength,
                |                               iDirection) As
                | 
                | Creates a new Cylinder within the current body.
                |
                | Parameters:
                | iCenter
                |     Center of the Cylinder - Can be Point or Vertex.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                |      iRadius
                |     Radius of Cylinder.
                |  
                |  iFirstLength
                |     Length of Cylinder in the given direction.
                |  
                |  iSecondLength
                |     Length of Cylinder in the opposite direction.
                |  
                |  iDirection
                |     Direction of extrusion for Cylinder.
                |  
                |  oCylinderObject
                |    Created CylinderObjct.


        :param i_center:
        :param i_radius:
        :param i_first_length:
        :param i_second_length:
        :param i_direction:
        :return:
        """
        return self.hybrid_shape_factory.AddNewCylinder(i_center, i_radius, i_first_length, i_second_length,
                                                        i_direction)

    def add_new_datums(self, i_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewDatums
                | o Func AddNewDatums(        iElem) As
                | 
                | Creates datums from a multi-domain result feature, one datum
                | is created by object domain. Note; Available only for a
                | shape design feature as input ( not for datum feature ).
                |
                | Parameters:
                | iElem
                |    Reference element 
                |  
                |  oArrayOfDatum
                |    List of datum objects , one datum is created per omain 
                |   Level of availability = V5R14

                | Examples:
                | This example converts a hybrid shape object in as much as
                | datums that the original hybrid shape features contains of
                | domain Dim HShape Set reference =
                | part.CreateReferenceFromObject(hybridShapeObject) ' Convert
                | to Datums HShape = hybridShapeFactory.AddNewDatums reference
                | Num =UBound(HShape) For i = 0 to Num
                | hybridBody1.AppendHybridShape HShape (i) Next
                | part.InWorkObject = HShape(num) part.Update ' Delete
                | original feature hybridShapeFactory.DeleteObjectForDatum
                | reference o Func AddNewDevelop( iMode, iToDevelop, iSupport)
                | As Creates a new Develop within the current body. Note:
                | require either DL1 or GSO license.

        :param i_elem:
        :return:
        """
        return self.hybrid_shape_factory.AddNewDatums(i_elem)

    def add_new_develop(self, i_mode, i_to_develop, i_support):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewDevelop
                | o Func AddNewDevelop(        iMode,
                |                              iToDevelop,
                |                              iSupport) As
                | 
                | Creates a new Develop within the current body. Note: require
                | either DL1 or GSO license.
                |
                | Parameters:
                | iMode
                |     Develop method.
                |  
                |  iToDevelop
                |     Wire to be developed.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iSupport
                |     Revolution support surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      oExt
                |     Created developed wire.


        :param i_mode:
        :param i_to_develop:
        :param i_support:
        :return:
        """
        return self.hybrid_shape_factory.AddNewDevelop(i_mode, i_to_develop, i_support)

    def add_new_direction(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewDirection
                | o Func AddNewDirection(        iElement) As
                | 
                | Creates a new direction specified by an element within the
                | current body.
                |
                | Parameters:
                | iElement
                |    Line or plane specifying the direction.
                |                         In case of plane, the plane normal vector is the direction
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      oDirection
                |     Created direction.


        :param i_element:
        :return:
        """
        return self.hybrid_shape_factory.AddNewDirection(i_element)

    def add_new_direction_by_coord(self, i_x, i_y, i_z):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewDirectionByCoord
                | o Func AddNewDirectionByCoord(        iX,
                |                                       iY,
                |                                       iZ) As
                | 
                | Creates a new Direction specifed by coordinates within the
                | current body.
                |
                | Parameters:
                | iX
                |     X component
                |  
                |  iY
                |     Y component
                |  
                |  iZ
                |     Z component
                |  
                |  oDirection
                |     Created direction


        :param i_x:
        :param i_y:
        :param i_z:
        :return:
        """
        return self.hybrid_shape_factory.AddNewDirectionByCoord(i_x, i_y, i_z)

    def add_new_empty_rotate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewEmptyRotate
                | o Func AddNewEmptyRotate(    ) As
                | 
                | Creates a new empty Rotate within the current body.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_factory.AddNewEmptyRotate()

    def add_new_empty_translate(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewEmptyTranslate
                | o Func AddNewEmptyTranslate(    ) As
                | 
                | Creates a new empty Translate within the current body.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_factory.AddNewEmptyTranslate()

    def add_new_extract(self, element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewExtract
                | o Func AddNewExtract(        Element) As
                | 
                | Creates a new Extract within the current body.
                |
                | Parameters:
                | iElement
                |     Initial element used to start the extraction
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | .  
                |      oExt
                |     The extracted object


        :param element:
        :return:
        """
        return self.hybrid_shape_factory.AddNewExtract(element)

    def add_new_extract_multi(self, element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewExtractMulti
                | o Func AddNewExtractMulti(        Element) As
                | 
                | Creates a new Multiple Extract within the current body.
                |
                | Parameters:
                | iElement
                |     Initial element used to start the extraction
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | .  
                |      oExt
                |     The extracted object


        :param element:
        :return:
        """
        return self.hybrid_shape_factory.AddNewExtractMulti(element)

    def add_new_extrapol_length(self, i_boundary, i_to_extrapol, i_length):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewExtrapolLength
                | o Func AddNewExtrapolLength(        iBoundary,
                |                                     iToExtrapol,
                |                                     iLength) As
                | 
                | Creates a new Extrapol (specified by length) within the
                | current body.
                |
                | Parameters:
                | iBoundary
                |     Boundary point of curve to extrapolate or boundary curve of surface to extrapolate.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iToExtrapol
                |     Curve or surface to extrapolate.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      iLength
                |     Extrapolation length.
                |  
                |  oExtrapol
                |    Created Extrapolation.


        :param i_boundary:
        :param i_to_extrapol:
        :param i_length:
        :return:
        """
        return self.hybrid_shape_factory.AddNewExtrapolLength(i_boundary, i_to_extrapol, i_length)

    def add_new_extrapol_until(self, i_boundary, i_to_extrapol, i_until):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewExtrapolUntil
                | o Func AddNewExtrapolUntil(        iBoundary,
                |                                    iToExtrapol,
                |                                    iUntil) As
                | 
                | Creates a new Extrapol (until an element) within the current
                | body.
                |
                | Parameters:
                | iBoundary
                |     Boundary point of curve to extrapolate or boundary curve of surface to extrapolate.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iToExtrapol
                |     Curve or surface to extrapolate.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      iUntil
                |     Extrapolation limit surface.
                |  
                |  oExtrapol
                |    Created Extrapolation.


        :param i_boundary:
        :param i_to_extrapol:
        :param i_until:
        :return:
        """
        return self.hybrid_shape_factory.AddNewExtrapolUntil(i_boundary, i_to_extrapol, i_until)

    def add_new_extremum(self, i_objet, i_dir, i_min_max):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewExtremum
                | o Func AddNewExtremum(        iObjet,
                |                               iDir,
                |                               iMinMax) As
                | 
                | Creates a new Extremum within the current body.
                |
                | Parameters:
                | iObjet
                |     Element onto extremum is computed
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      iDir
                |     Extremum direction
                |  
                |  iMinMax
                |                          Maximum (GSMMax) or Minimum (GSMMin)
                |  
                |  oExt
                |     The extremum object if succeded


        :param i_objet:
        :param i_dir:
        :param i_min_max:
        :return:
        """
        return self.hybrid_shape_factory.AddNewExtremum(i_objet, i_dir, i_min_max)

    def add_new_extremum_polar(self, i_type, ip_ia_contour):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewExtremumPolar
                | o Func AddNewExtremumPolar(        iType,
                |                                    ipIAContour) As
                | 
                | Creates a new Extremum Polar within the current body.
                |
                | Parameters:
                | iType
                |     Type of extremum polar 0-Min Radius 1-Max Radius 2- Min Angle 3- Maximum Angle
                |  
                |  ipIAContour
                |     Extremum Polar Contour. It should be non convex
                |  
                |  opIAExtPolar
                |     The extremum polar object if succeded


        :param i_type:
        :param ip_ia_contour:
        :return:
        """
        return self.hybrid_shape_factory.AddNewExtremumPolar(i_type, ip_ia_contour)

    def add_new_extrude(self, i_object_to_extrude, i_offset_debut, i_offset_fin, i_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewExtrude
                | o Func AddNewExtrude(        iObjectToExtrude,
                |                              iOffsetDebut,
                |                              iOffsetFin,
                |                              iDirection) As
                | 
                | Creates a new extrude within the current body.
                |
                | Parameters:
                | iObjectToExtrude
                |     Object to be extruded (point, line ,curve,or face)
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | .   
                |      iOffsetDebut
                |     Length value   
                |  
                |  iOffsetFin
                |     Length value 
                |                        ( iOffsetFin has to be larger than iOffsetDebut) 
                |  
                |  iDirection
                |     Extrusion direction  
                |  
                |  oExtrudeObject
                |     Extruded result


        :param i_object_to_extrude:
        :param i_offset_debut:
        :param i_offset_fin:
        :param i_direction:
        :return:
        """
        return self.hybrid_shape_factory.AddNewExtrude(i_object_to_extrude, i_offset_debut, i_offset_fin, i_direction)

    def add_new_fill(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewFill
                | o Func AddNewFill(    ) As
                | 
                | Creates a new Fill within the current body.
                |
                | Parameters:
                | oFill
                |     Fill object


        :return:
        """
        return self.hybrid_shape_factory.AddNewFill()

    def add_new_fillet_bi_tangent(self, i_element_1, i_element_2, i_radius, i_orientation_1, i_orientation_2,
                                  i_supports_trim_mode, i_ribbon_relimitation_mode):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewFilletBiTangent
                | o Func AddNewFilletBiTangent(        iElement1,
                |                                      iElement2,
                |                                      iRadius,
                |                                      iOrientation1,
                |                                      iOrientation2,
                |                                      iSupportsTrimMode,
                |                                      iRibbonRelimitationMode) As
                | 
                | Creates a new a sphere bitangent fillet between two skins.
                |
                | Parameters:
                | iElement1
                |     First support of fillet. 
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | .  
                |      iElement2
                |     Second support of fillet.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iRadius
                |     Radius of the fillet.
                |  
                |  iOrientation1
                |     Manage the fillet center position.
                |  
                |  iOrientation2
                |     Manage the fillet center position. 
                |  
                |  iSupportsTrimMode
                |     The 2 supports can be trimmed and assembled with the fillet.
                |    Value can be 0 (No trim ) or 1 (Trim)
                |  
                |  iRibbonRelimitationMode
                |     Manage the relimition of fillet extremities.
                |    Value can be : 0 (Smooth), 1 (Straight), 2 (Maximum) or 3 (Minimum)
                |  
                |  oFillet
                |    Created fillet.


        :param i_element_1:
        :param i_element_2:
        :param i_radius:
        :param i_orientation_1:
        :param i_orientation_2:
        :param i_supports_trim_mode:
        :param i_ribbon_relimitation_mode:
        :return:
        """
        return self.hybrid_shape_factory.AddNewFilletBiTangent(i_element_1, i_element_2, i_radius, i_orientation_1,
                                                               i_orientation_2, i_supports_trim_mode,
                                                               i_ribbon_relimitation_mode)

    def add_new_fillet_tri_tangent(self, i_element_1, i_element_2, i_remove_elem, i_orientation_1, i_orientation_2,
                                   i_remove_orientation, i_supports_trim_mode, i_ribbon_relimitation_mode):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewFilletTriTangent
                | o Func AddNewFilletTriTangent(        iElement1,
                |                                       iElement2,
                |                                       iRemoveElem,
                |                                       iOrientation1,
                |                                       iOrientation2,
                |                                       iRemoveOrientation,
                |                                       iSupportsTrimMode,
                |                                       iRibbonRelimitationMode) As
                | 
                | Creates a new a tritangent fillet between three skins.
                |
                | Parameters:
                | iElement1
                |     First support of fillet. 
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | .  
                |      iElement2
                |     Second support of fillet.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iRemoveElem
                |     Support to remove of fillet.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iOrientation1
                |     Manage the fillet center position.
                |  
                |  iOrientation2
                |     Manage the fillet center position. 
                |  
                |  iRemoveOrientation
                |     Manage the fillet center position. 
                |  
                |  iSupportsTrimMode
                |     The 2 supports can be trimmed and assembled with the fillet.
                |    Value can be 0 (No trim ) or 1 (Trim)
                |  
                |  iRibbonRelimitationMode
                |     Manage the relimition of fillet extremities.
                |    Value can be : 0 (Smooth), 1 (Straight), 2 (Maximum) or 3 (Minimum)
                |  
                |  oFillet
                |    Created fillet.


        :param i_element_1:
        :param i_element_2:
        :param i_remove_elem:
        :param i_orientation_1:
        :param i_orientation_2:
        :param i_remove_orientation:
        :param i_supports_trim_mode:
        :param i_ribbon_relimitation_mode:
        :return:
        """
        return self.hybrid_shape_factory.AddNewFilletTriTangent(i_element_1, i_element_2, i_remove_elem,
                                                                i_orientation_1, i_orientation_2, i_remove_orientation,
                                                                i_supports_trim_mode, i_ribbon_relimitation_mode)

    def add_new_healing(self, i_body_toheal):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewHealing
                | o Func AddNewHealing(        iBodyToheal) As
                | 
                | Creates a new healing within the current body.
                |
                | Parameters:
                | iBodyToHeal
                |     The body to heal  
                |  
                |  oHealing
                |     The created healing


        :param i_body_toheal:
        :return:
        """
        return self.hybrid_shape_factory.AddNewHealing(i_body_toheal)

    def add_new_helix(self, i_axis, i_invert_axis, i_starting_point, i_pitch, i_height, i_clockwise_revolution,
                      i_starting_angle, i_taper_angle, i_taper_outward):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewHelix
                | o Func AddNewHelix(        iAxis,
                |                            iInvertAxis,
                |                            iStartingPoint,
                |                            iPitch,
                |                            iHeight,
                |                            iClockwiseRevolution,
                |                            iStartingAngle,
                |                            iTaperAngle,
                |                            iTaperOutward) As
                | 
                | Creates a new Helix within the current body.
                |
                | Parameters:
                | iAxis
                |       The helix axis (always a line).
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | .   
                |      iInvertAxis
                |  
                |  iStartingPoint
                |       Starting Point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | .   
                |      iPitch
                |       Pitch.
                |    
                |  iHeight
                |       Helix height.
                |    
                |  iClockwiseRevolution
                |       Revolutions are clockwise if TRUE, counterclockwise if FALSE.
                |    
                |  iStartingAngle
                |       Starting angle from starting point measured on the helix itself.
                |       If no starting angle is wanted, set it to 0.0.
                |    
                |  iTaperAngle
                |       0 <= Taper Angle < Pi/2
                |       If no taper angle is wanted, set it to 0.0 (constant helix radius).
                |    
                |  iTaperOutward
                |       Helix radius increases if TRUE, decreases if FALSE.
                |  
                |  oHelix
                |    The Helix object if succeded


        :param i_axis:
        :param i_invert_axis:
        :param i_starting_point:
        :param i_pitch:
        :param i_height:
        :param i_clockwise_revolution:
        :param i_starting_angle:
        :param i_taper_angle:
        :param i_taper_outward:
        :return:
        """
        return self.hybrid_shape_factory.AddNewHelix(i_axis, i_invert_axis, i_starting_point, i_pitch, i_height,
                                                     i_clockwise_revolution, i_starting_angle, i_taper_angle,
                                                     i_taper_outward)

    def add_new_hybrid_scaling(self, i_elem_to_scale, i_center, i_ratio):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewHybridScaling
                | o Func AddNewHybridScaling(        iElemToScale,
                |                                    iCenter,
                |                                    iRatio) As
                | 
                | Creates a new scaling within the current body.
                |
                | Parameters:
                | iElemToScale
                |     Point, curve, surface or solid to transform.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                | , 
                |  and 
                | . 
                |      iCenter
                |     Reference point or reference plane.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | . 
                |      iRatio
                |     Scaling ratio.
                |  
                |  oScaling
                |     Created scaling.


        :param i_elem_to_scale:
        :param i_center:
        :param i_ratio:
        :return:
        """
        return self.hybrid_shape_factory.AddNewHybridScaling(i_elem_to_scale, i_center, i_ratio)

    def add_new_hybrid_split(self, i_element_1, i_element_2, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewHybridSplit
                | o Func AddNewHybridSplit(        iElement1,
                |                                  iElement2,
                |                                  iOrientation) As
                | 
                | Creates a new Split within the current body.
                |
                | Parameters:
                | iElement1
                |     The feature to cut (curve or surface).
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      iElement2
                |     The cutting feature (point, curve, surface).
                |  Sub-element(s) supported (see 
                |  object):  see 
                | , 
                | , 
                |  and 
                | . 
                |      iOrientation
                |     Manage the kept side of the feature to cut (value can be 1 or -1)
                |  
                |  oSplit
                |     Created split


        :param i_element_1:
        :param i_element_2:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewHybridSplit(i_element_1, i_element_2, i_orientation)

    def add_new_hybrid_trim(self, i_element_1, i_orientation_1, i_element_2, i_orientation_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewHybridTrim
                | o Func AddNewHybridTrim(        iElement1,
                |                                 iOrientation1,
                |                                 iElement2,
                |                                 iOrientation2) As
                | 
                | Creates a new Trim within the current body by cutting and
                | joining two elements. You can trim a surface by a surface or
                | a curve by a curve.
                |
                | Parameters:
                | iElement1
                |     The feature to trim (curve or surface).
                |  
                |  iOrientation1
                |     Manage the kept side of iElement1  (value can be 1 or -1).
                |  
                |  iElement2
                |     The second feature to trim (curve or surface).
                |  
                |  iOrientation2
                |     Manage the kept side of iElement2  (value can be 1 or -1).
                |  
                |  oTrim
                |     Created trim.


        :param i_element_1:
        :param i_orientation_1:
        :param i_element_2:
        :param i_orientation_2:
        :return:
        """
        return self.hybrid_shape_factory.AddNewHybridTrim(i_element_1, i_orientation_1, i_element_2, i_orientation_2)

    def add_new_integrated_law(self, i_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewIntegratedLaw
                | o Func AddNewIntegratedLaw(        iType) As
                | 
                | Creates Integrated Law.
                |
                | Parameters:
                | iType
                |        Type of law = 0 : None
                | 	                 = 1 : Constant
                |                    = 2 : Linear
                |                    = 3 : SType
                |                    = 4 : Advanced
                |                    = 5 : Implicit


        :param i_type:
        :return:
        """
        return self.hybrid_shape_factory.AddNewIntegratedLaw(i_type)

    def add_new_intersection(self, i_object_1, i_object_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewIntersection
                | o Func AddNewIntersection(        iObject1,
                |                                   iObject2) As
                | 
                | Creates a new Intersection within the current body.
                |
                | Parameters:
                | iObject1
                |     First element ( line, curve, plane, surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | ,  
                |  and 
                | .  
                |      iObject2
                |     Second element ( line , curve, plane, surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | ,  
                |  and 
                | . 
                |      oIntersection
                |     Intersection


        :param i_object_1:
        :param i_object_2:
        :return:
        """
        return self.hybrid_shape_factory.AddNewIntersection(i_object_1, i_object_2)

    def add_new_inverse(self, element, inverse):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewInverse
                | o Func AddNewInverse(        Element,
                |                              Inverse) As
                | 
                | Creates a new Inverse within the current body.
                |
                | Parameters:
                | iElement
                |     The objet to inverse
                |  
                |  iInverse
                |     the type of inversion (see CATGSMOrientation.h) 
                |      1  for no inversion 
                |     -1  for inversion
                |  
                |  oInv
                |     The inverted object


        :param element:
        :param inverse:
        :return:
        """
        return self.hybrid_shape_factory.AddNewInverse(element, inverse)

    def add_new_join(self, element_1, element_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewJoin
                | o Func AddNewJoin(        Element1,
                |                           Element2) As
                | 
                | Creates a new Join within the current body.
                |
                | Parameters:
                | iElement1
                |     First element to join ( curve or surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                |  and 
                | .   
                |      iElement2
                |     Second element to join ( same type of the first element)
                | Sub-element(s) supported (see 
                |  object):  see 
                | , 
                |  and 
                | .  
                |      oExt
                |     Join result
                |                        The default value used to join element is 0.001mm


        :param element_1:
        :param element_2:
        :return:
        """
        return self.hybrid_shape_factory.AddNewJoin(element_1, element_2)

    def add_new_law_dist_proj(self, i_reference, i_definition):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLawDistProj
                | o Func AddNewLawDistProj(        iReference,
                |                                  iDefinition) As
                | 
                | Creates a new law within the current body.
                |
                | Parameters:
                | iReference
                |    Reference line of the law.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iDefinition
                |     Definition curve of the law.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | . 
                |      oLaw
                |    The Law object if succeded


        :param i_reference:
        :param i_definition:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLawDistProj(i_reference, i_definition)

    def add_new_line_angle(self, i_curve, i_surface, i_point, i_geodesic, i_begin_offset, i_end_offset, i_angle,
                           i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLineAngle
                | o Func AddNewLineAngle(        iCurve,
                |                                iSurface,
                |                                iPoint,
                |                                iGeodesic,
                |                                iBeginOffset,
                |                                iEndOffset,
                |                                iAngle,
                |                                iOrientation) As
                | 
                | Creates a new angle line within the current body.
                |
                | Parameters:
                | iCurve
                |     Reference curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iSurface
                |     Reference surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iPoint
                |     reference point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iGeodesic
                |     Puts the line on the surface
                |  
                |  iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  iAngle
                |     angle to reference curve
                |  
                |  iOrientation
                |     Orientation allows to reverse the line direction from the reference point.
                |    For a line of L length, it is the same as creating this line with -L length.
                |  
                |  oLine
                |     Created line


        :param i_curve:
        :param i_surface:
        :param i_point:
        :param i_geodesic:
        :param i_begin_offset:
        :param i_end_offset:
        :param i_angle:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLineAngle(i_curve, i_surface, i_point, i_geodesic, i_begin_offset,
                                                         i_end_offset, i_angle, i_orientation)

    def add_new_line_bi_tangent(self, i_curve_1, i_element_2, i_support):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLineBiTangent
                | o Func AddNewLineBiTangent(        iCurve1,
                |                                    iElement2,
                |                                    iSupport) As
                | 
                | Creates a new bitangent line within the current body.
                |
                | Parameters:
                | iCurve1
                |     First tangency curve lying on the support surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iCurve2
                |    Second tangency element (point, curve) lying on the support surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      iSupport
                |    The support surface of the two elements.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      oLine
                |     Created line


        :param i_curve_1:
        :param i_element_2:
        :param i_support:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLineBiTangent(i_curve_1, i_element_2, i_support)

    def add_new_line_bisecting(self, i_line_1, i_line_2, i_begin_offset, i_end_offset, i_orientation, solution_nb):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLineBisecting
                | o Func AddNewLineBisecting(        iLine1,
                |                                    iLine2,
                |                                    iBeginOffset,
                |                                    iEndOffset,
                |                                    iOrientation,
                |                                    SolutionNb) As
                | 
                | Creates a new bisecting line within the current body.
                |
                | Parameters:
                | iLine1
                |     First line.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iLine2
                |     Second line.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | . 
                |      iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  iOrientation
                |     Orientation allows to reverse the line direction from the reference point.
                |    For a line of L length, it is the same as creating this line with -L length.
                |  
                |  oLine
                |     Created line


        :param i_line_1:
        :param i_line_2:
        :param i_begin_offset:
        :param i_end_offset:
        :param i_orientation:
        :param solution_nb:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLineBisecting(i_line_1, i_line_2, i_begin_offset, i_end_offset,
                                                             i_orientation, solution_nb)

    def add_new_line_bisecting_on_support(self, i_line_1, i_line_2, i_surface, i_begin_offset, i_end_offset,
                                          i_orientation, solution_nb):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLineBisectingOnSupport
                | o Func AddNewLineBisectingOnSupport(        iLine1,
                |                                             iLine2,
                |                                             iSurface,
                |                                             iBeginOffset,
                |                                             iEndOffset,
                |                                             iOrientation,
                |                                             SolutionNb) As
                | 
                | Creates a new bisecting line on a support within the current
                | body.
                |
                | Parameters:
                | iLine1
                |     First line.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iLine2
                |     Second line.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | . 
                |      iSurface
                |     Reference surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  iOrientation
                |     Orientation allows to reverse the line direction from the reference point.
                |    For a line of L length, it is the same as creating this line with -L length.
                |  
                |  oLine
                |     Created line


        :param i_line_1:
        :param i_line_2:
        :param i_surface:
        :param i_begin_offset:
        :param i_end_offset:
        :param i_orientation:
        :param solution_nb:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLineBisectingOnSupport(i_line_1, i_line_2, i_surface, i_begin_offset,
                                                                      i_end_offset, i_orientation, solution_nb)

    def add_new_line_bisecting_on_support_with_point(self, i_line_1, i_line_2, i_ref_point, i_surface, i_begin_offset,
                                                     i_end_offset, i_orientation, solution_nb):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLineBisectingOnSupportWithPoint
                | o Func AddNewLineBisectingOnSupportWithPoint(        iLine1,
                |                                                      iLine2,
                |                                                      iRefPoint,
                |                                                      iSurface,
                |                                                      iBeginOffset,
                |                                                      iEndOffset,
                |                                                      iOrientation,
                |                                                      SolutionNb) As
                | 
                | Creates a new bisecting line on a support with a atarting
                | point within the current body.
                |
                | Parameters:
                | iLine1
                |     First line.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iLine2
                |     Second line.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | . 
                |      iRefPoint
                |     Starting point of the bisecting line.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iSurface
                |     Reference surface.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  iOrientation
                |     Orientation allows to reverse the line direction from the reference point.
                |    For a line of L length, it is the same as creating this line with -L length.
                |  
                |  oLine
                |     Created line


        :param i_line_1:
        :param i_line_2:
        :param i_ref_point:
        :param i_surface:
        :param i_begin_offset:
        :param i_end_offset:
        :param i_orientation:
        :param solution_nb:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLineBisectingOnSupportWithPoint(i_line_1, i_line_2, i_ref_point,
                                                                               i_surface, i_begin_offset, i_end_offset,
                                                                               i_orientation, solution_nb)

    def add_new_line_bisecting_with_point(self, i_line_1, i_line_2, i_ref_point, i_begin_offset, i_end_offset,
                                          i_orientation, solution_nb):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLineBisectingWithPoint
                | o Func AddNewLineBisectingWithPoint(        iLine1,
                |                                             iLine2,
                |                                             iRefPoint,
                |                                             iBeginOffset,
                |                                             iEndOffset,
                |                                             iOrientation,
                |                                             SolutionNb) As
                | 
                | Creates a new bisecting line with a starting point within
                | the current body.
                |
                | Parameters:
                | iLine1
                |     First line.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iLine2
                |     Second line.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | . 
                |      iRefPoint
                |     Starting point of the bisecting line.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  iOrientation
                |     Orientation allows to reverse the line direction from the reference point.
                |    For a line of L length, it is the same as creating this line with -L length.
                |  
                |  oLine
                |     Created line


        :param i_line_1:
        :param i_line_2:
        :param i_ref_point:
        :param i_begin_offset:
        :param i_end_offset:
        :param i_orientation:
        :param solution_nb:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLineBisectingWithPoint(i_line_1, i_line_2, i_ref_point, i_begin_offset,
                                                                      i_end_offset, i_orientation, solution_nb)

    def add_new_line_datum(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLineDatum
                | o Func AddNewLineDatum(        iObject) As
                | 
                | Creates a new datum of line within the current body.
                |
                | Parameters:
                | iObject
                |     The object whose topological body will be duplicated and put into created datum
                |  
                |  oLine
                |    Created datum
                |  Note2: the object passed as parameter to create the datum has to be in the current container.
                |  Otherwise, an error occurs.


        :param i_object:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLineDatum(i_object)

    def add_new_line_normal(self, i_surface, i_point, i_begin_offset, i_end_offset, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLineNormal
                | o Func AddNewLineNormal(        iSurface,
                |                                 iPoint,
                |                                 iBeginOffset,
                |                                 iEndOffset,
                |                                 iOrientation) As
                | 
                | Creates a new normal line within the current body.
                |
                | Parameters:
                | iSurface
                |     Reference surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPoint
                |     Reference point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  iOrientation
                |     Orientation allows to reverse the line direction from the reference point.
                |    For a line of L length, it is the same as creating this line with -L length.
                |  
                |  oLine
                |     Created line


        :param i_surface:
        :param i_point:
        :param i_begin_offset:
        :param i_end_offset:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLineNormal(i_surface, i_point, i_begin_offset, i_end_offset,
                                                          i_orientation)

    def add_new_line_pt_dir(self, i_pt, i_direction, i_begin_offset, i_end_offset, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLinePtDir
                | o Func AddNewLinePtDir(        iPt,
                |                                iDirection,
                |                                iBeginOffset,
                |                                iEndOffset,
                |                                iOrientation) As
                | 
                | Creates a new point-direction line within the current body.
                |
                | Parameters:
                | iPt
                |     reference point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iDirection
                |     Direction
                |  
                |  iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  iOrientation
                |     Orientation allows to reverse the line direction from the reference point.
                |    For a line of L length, it is the same as creating this line with -L length.
                |     
                |  
                |  oLine
                |     Created line


        :param i_pt:
        :param i_direction:
        :param i_begin_offset:
        :param i_end_offset:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLinePtDir(i_pt, i_direction, i_begin_offset, i_end_offset, i_orientation)

    def add_new_line_pt_dir_on_support(self, i_pt, i_direction, i_support, i_begin_offset, i_end_offset, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLinePtDirOnSupport
                | o Func AddNewLinePtDirOnSupport(        iPt,
                |                                         iDirection,
                |                                         iSupport,
                |                                         iBeginOffset,
                |                                         iEndOffset,
                |                                         iOrientation) As
                | 
                | Creates a new point-direction line within the current body.
                |
                | Parameters:
                | iPt
                |     reference point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iDirection
                |     Direction
                |  
                |  iSupport
                |    Support element (surface or plane)
                | Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  iOrientation
                |     Orientation allows to reverse the line direction from the reference point.
                |    For a line of L length, it is the same as creating this line with -L length.
                |     
                |  
                |  oLine
                |     Created line


        :param i_pt:
        :param i_direction:
        :param i_support:
        :param i_begin_offset:
        :param i_end_offset:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLinePtDirOnSupport(i_pt, i_direction, i_support, i_begin_offset,
                                                                  i_end_offset, i_orientation)

    def add_new_line_pt_pt(self, i_pt_origine, i_pt_extremite):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLinePtPt
                | o Func AddNewLinePtPt(        iPtOrigine,
                |                               iPtExtremite) As
                | 
                | Creates a new point-point line within the current body.
                |
                | Parameters:
                | iPtOrigine
                |     Origin point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPtExtremite
                |     Extremity point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      oLine
                |     Created line


        :param Reference() i_pt_origine:
        :param Reference() i_pt_extremite:
        :return:
        """
        return HybridShapeLinePtPt(
            self.hybrid_shape_factory.AddNewLinePtPt(i_pt_origine.com_object, i_pt_extremite.com_object))

    def add_new_line_pt_pt_extended(self, i_pt_origine, i_pt_extremite, i_begin_offset, i_end_offset):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLinePtPtExtended
                | o Func AddNewLinePtPtExtended(        iPtOrigine,
                |                                       iPtExtremite,
                |                                       iBeginOffset,
                |                                       iEndOffset) As
                | 
                | Creates a new point-point line with extensions within the
                | current body.
                |
                | Parameters:
                | iPtOrigine
                |     Origin point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPtExtremite
                |     Extremity point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  oLine
                |     Created line


        :param i_pt_origine:
        :param i_pt_extremite:
        :param i_begin_offset:
        :param i_end_offset:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLinePtPtExtended(i_pt_origine, i_pt_extremite, i_begin_offset,
                                                                i_end_offset)

    def add_new_line_pt_pt_on_support(self, i_pt_origine, i_pt_extremite, i_support):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLinePtPtOnSupport
                | o Func AddNewLinePtPtOnSupport(        iPtOrigine,
                |                                        iPtExtremite,
                |                                        iSupport) As
                | 
                | Creates a new point-point line with support within the
                | current body.
                |
                | Parameters:
                | iPtOrigine
                |     Origin point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPtExtremite
                |     Extremity point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iSupport
                |    Support element (surface or plane)
                | Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      oLine
                |     Created line


        :param i_pt_origine:
        :param i_pt_extremite:
        :param i_support:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLinePtPtOnSupport(i_pt_origine, i_pt_extremite, i_support)

    def add_new_line_pt_pt_on_support_extended(self, i_pt_origine, i_pt_extremite, i_support, i_begin_offset,
                                               i_end_offset):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLinePtPtOnSupportExtended
                | o Func AddNewLinePtPtOnSupportExtended(        iPtOrigine,
                |                                                iPtExtremite,
                |                                                iSupport,
                |                                                iBeginOffset,
                |                                                iEndOffset) As
                | 
                | Creates a new point-point line with extensions and with
                | support within the current body.
                |
                | Parameters:
                | iPtOrigine
                |     Origin point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPtExtremite
                |     Extremity point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iSupport
                |    Support element (surface or plane)
                | Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  oLine
                |     Created line


        :param i_pt_origine:
        :param i_pt_extremite:
        :param i_support:
        :param i_begin_offset:
        :param i_end_offset:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLinePtPtOnSupportExtended(i_pt_origine, i_pt_extremite, i_support,
                                                                         i_begin_offset, i_end_offset)

    def add_new_line_tangency(self, i_curve, i_point, i_begin_offset, i_end_offset, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLineTangency
                | o Func AddNewLineTangency(        iCurve,
                |                                   iPoint,
                |                                   iBeginOffset,
                |                                   iEndOffset,
                |                                   iOrientation) As
                | 
                | Creates a new tangent line within the current body.
                |
                | Parameters:
                | iCurve
                |     Reference curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iPoint
                |     Reference point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  iOrientation
                |     Orientation allows to reverse the line direction from the reference point.
                |    For a line of L length, it is the same as creating this line with -L length.
                |     
                |  
                |  oLine
                |     Created line


        :param i_curve:
        :param i_point:
        :param i_begin_offset:
        :param i_end_offset:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLineTangency(i_curve, i_point, i_begin_offset, i_end_offset,
                                                            i_orientation)

    def add_new_line_tangency_on_support(self, i_curve, i_point, i_support, i_begin_offset, i_end_offset,
                                         i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLineTangencyOnSupport
                | o Func AddNewLineTangencyOnSupport(        iCurve,
                |                                            iPoint,
                |                                            iSupport,
                |                                            iBeginOffset,
                |                                            iEndOffset,
                |                                            iOrientation) As
                | 
                | Creates a new tangent line within the current body.
                |
                | Parameters:
                | iCurve
                |     Reference curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iPoint
                |     Reference point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iSupport
                |    Support element (surface or plane)
                | Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iBeginOffset
                |     start offset
                |  
                |  iEndOffset
                |     end offset
                |  
                |  iOrientation
                |     Orientation allows to reverse the line direction from the reference point.
                |    For a line of L length, it is the same as creating this line with -L length.
                |  
                |  oLine
                |     Created line


        :param i_curve:
        :param i_point:
        :param i_support:
        :param i_begin_offset:
        :param i_end_offset:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewLineTangencyOnSupport(i_curve, i_point, i_support, i_begin_offset,
                                                                     i_end_offset, i_orientation)

    def add_new_loft(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewLoft
                | o Func AddNewLoft(    ) As
                | 
                | Creates a new Loft within the current body.
                |
                | Parameters:
                | oExt
                |     CATIAHybridShapeLoft created


        :return:
        """
        return self.hybrid_shape_factory.AddNewLoft()

    def add_new_mid_surface(self, i_support, i_creation_mode, i_threshold):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewMidSurface
                | o Func AddNewMidSurface(        iSupport,
                |                                 iCreationMode,
                |                                 iThreshold) As
                | 
                | Creates a new MidSurface in Automatic Creation Mode Only.
                |
                | Parameters:
                | iSupport
                |     support Body
                |  
                |  iCreationMode
                |     Creation Mode (Only Automatic Accepted)
                |  
                |  iThreshold
                |     Threshold Thickness
                |  
                |  oMidSurface
                |     Created MidSurface


        :param i_support:
        :param i_creation_mode:
        :param i_threshold:
        :return:
        """
        return self.hybrid_shape_factory.AddNewMidSurface(i_support, i_creation_mode, i_threshold)

    def add_new_near(self, multi_element, reference_element):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewNear
                | o Func AddNewNear(        MultiElement,
                |                           ReferenceElement) As
                | 
                | Creates a new Near within the current body.
                |
                | Parameters:
                | iMultiElement
                |     Non connex element (point,curve,surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                | , 
                |  and 
                | . 
                |      iReferenceElement
                |     Reference element
                | Sub-element(s) supported (see 
                |  object):  see 
                | , 
                | , 
                |  and 
                | .   
                |      oNear
                |     The result is the connex component that is the nearest from the reference element


        :param multi_element:
        :param reference_element:
        :return:
        """
        return self.hybrid_shape_factory.AddNewNear(multi_element, reference_element)

    def add_new_offset(self, i_object_to_offset, i_offset, i_orientation, i_precision):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewOffset
                | o Func AddNewOffset(        iObjectToOffset,
                |                             iOffset,
                |                             iOrientation,
                |                             iPrecision) As
                | 
                | Creates a new offset within the current body.
                |
                | Parameters:
                | iObjectToOffset
                |     Surface to offset.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | .   
                |      iOffset
                |     Offset value  
                |  
                |  iOrientation
                |     Offset orientation
                |  
                |  iPrecision
                |     This variable is no longer in use and any change in it's value does not impact the output.
                |  
                |  oOffsetObject
                |     Offset Surface


        :param i_object_to_offset:
        :param i_offset:
        :param i_orientation:
        :param i_precision:
        :return:
        """
        return self.hybrid_shape_factory.AddNewOffset(i_object_to_offset, i_offset, i_orientation, i_precision)

    def add_new_plane1_curve(self, i_planar_curve):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlane1Curve
                | o Func AddNewPlane1Curve(        iPlanarCurve) As
                | 
                | Creates a new plane passing through one planar curve within
                | the current body.
                |
                | Parameters:
                | iPlanarCurve
                |     passing curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      oPlane
                |     Created plane


        :param i_planar_curve:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlane1Curve(i_planar_curve)

    def add_new_plane1_line1_pt(self, i_ln, i_pt):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlane1Line1Pt
                | o Func AddNewPlane1Line1Pt(        iLn,
                |                                    iPt) As
                | 
                | Creates a new plane passing through 1 line and 1 point
                | within the current body.
                |
                | Parameters:
                | iLn
                |     passing line.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      iPt
                |     passing point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      oPlane
                |     Created plane


        :param i_ln:
        :param i_pt:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlane1Line1Pt(i_ln, i_pt)

    def add_new_plane2_lines(self, i_ln_1, i_ln_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlane2Lines
                | o Func AddNewPlane2Lines(        iLn1,
                |                                  iLn2) As
                | 
                | Creates a new plane passing through 2 lines within the
                | current body.
                |
                | Parameters:
                | iLn1
                |     first passing line.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      iLn2
                |     second passing line.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      oPlane
                |     Created line


        :param i_ln_1:
        :param i_ln_2:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlane2Lines(i_ln_1, i_ln_2)

    def add_new_plane3_points(self, i_pt_1, i_pt_2, i_pt_3):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlane3Points
                | o Func AddNewPlane3Points(        iPt1,
                |                                   iPt2,
                |                                   iPt3) As
                | 
                | Creates a new plane passing through 3 points within the
                | current body.
                |
                | Parameters:
                | iPt1
                |     first passing point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPt2
                |     second passing point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iPt3
                |     third passing point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      oPlane
                |     Created plane


        :param i_pt_1:
        :param i_pt_2:
        :param i_pt_3:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlane3Points(i_pt_1, i_pt_2, i_pt_3)

    def add_new_plane_angle(self, i_plane, i_revol_axis, i_angle, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlaneAngle
                | o Func AddNewPlaneAngle(        iPlane,
                |                                 iRevolAxis,
                |                                 iAngle,
                |                                 iOrientation) As
                | 
                | Creates a new angle plane within the current body.
                |
                | Parameters:
                | iPlane
                |     reference plane
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iRevolAxis
                |     rotation axis
                | Sub-element(s) supported (see 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      iAngle
                |     angle
                |  
                |  iOrientation
                |     Orientation to reverse the plane from the reference plane.
                |  
                |  oPlane
                |     Created plane


        :param i_plane:
        :param i_revol_axis:
        :param i_angle:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlaneAngle(i_plane, i_revol_axis, i_angle, i_orientation)

    def add_new_plane_datum(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlaneDatum
                | o Func AddNewPlaneDatum(        iObject) As
                | 
                | Creates a new datum of plane within the current body.
                |
                | Parameters:
                | iObject
                |     The object whose topological body will be duplicated and put into created datum
                |  
                |  oPlane
                |    Created datum
                |  Note2: the object passed as parameter to create the datum has to be in the current container.
                |  Otherwise, an error occurs.


        :param i_object:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlaneDatum(i_object)

    def add_new_plane_equation(self, i_a__coeff, i_b__coeff, i_c__coeff, i_d__coeff):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlaneEquation
                | o Func AddNewPlaneEquation(        iA_Coeff,
                |                                    iB_Coeff,
                |                                    iC_Coeff,
                |                                    iD_Coeff) As
                | 
                | Creates a new equation plane within the current body. Plane
                | equation is Ax+By+Cz = D.
                |
                | Parameters:
                | iA_Coeff
                |     A coefficient
                |  
                |  iB_Coeff
                |     B coefficient
                |  
                |  iC_Coeff
                |     C coefficient
                |  
                |  iD_Coeff
                |     D coefficient
                |  
                |  oPlane
                |     Created plane


        :param i_a__coeff:
        :param i_b__coeff:
        :param i_c__coeff:
        :param i_d__coeff:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlaneEquation(i_a__coeff, i_b__coeff, i_c__coeff, i_d__coeff)

    def add_new_plane_mean(self, i_list_of_points, nb_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlaneMean
                | o Func AddNewPlaneMean(        iListOfPoints,
                |                                NbPoint) As
                | 
                | Creates a new mean through points plane within the current
                | body.
                |
                | Parameters:
                | oIListOfPoints
                |     list of passing points
                |    Warning : Input and Output parameter for CATScript applications, procedural type
                |  
                |  iNbPoint
                |     Number of points
                |  
                |  oPlane
                |     Created plane


        :param i_list_of_points:
        :param nb_point:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlaneMean(i_list_of_points, nb_point)

    def add_new_plane_normal(self, i_curve, i_pt):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlaneNormal
                | o Func AddNewPlaneNormal(        iCurve,
                |                                  iPt) As
                | 
                | Creates a new normal plane within the current body.
                |
                | Parameters:
                | iCurve
                |     Reference curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iPt
                |     Reference point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      oPlane
                |     Created plane


        :param i_curve:
        :param i_pt:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlaneNormal(i_curve, i_pt)

    def add_new_plane_offset(self, i_plane, i_offset, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlaneOffset
                | o Func AddNewPlaneOffset(        iPlane,
                |                                  iOffset,
                |                                  iOrientation) As
                | 
                | Creates a new offset plane within the current body.
                |
                | Parameters:
                | iPlane
                |     reference plane
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iOffset
                |     offset value
                |  
                |  iOrientation
                |     Orientation to reverse the plane from the reference plane. 
                |  
                |  oPlane
                |     Created plane


        :param i_plane:
        :param i_offset:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlaneOffset(i_plane, i_offset, i_orientation)

    def add_new_plane_offset_pt(self, i_plane, i_pt):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlaneOffsetPt
                | o Func AddNewPlaneOffsetPt(        iPlane,
                |                                    iPt) As
                | 
                | Creates a new offset trough point plane within the current
                | body.
                |
                | Parameters:
                | iPlane
                |     reference plane
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPt
                |     Reference point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      oPlane
                |     Created plane


        :param i_plane:
        :param i_pt:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlaneOffsetPt(i_plane, i_pt)

    def add_new_plane_tangent(self, i_surface, i_pt):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPlaneTangent
                | o Func AddNewPlaneTangent(        iSurface,
                |                                   iPt) As
                | 
                | Creates a new tangent plane within the current body.
                |
                | Parameters:
                | iSurface
                |     reference surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPt
                |     reference point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      oPlane
                |     Created plane


        :param i_surface:
        :param i_pt:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPlaneTangent(i_surface, i_pt)

    def add_new_point_between(self, i_point_1, i_point_2, i_ratio, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointBetween
                | o Func AddNewPointBetween(        iPoint1,
                |                                   iPoint2,
                |                                   iRatio,
                |                                   iOrientation) As
                | 
                | Creates a new PointBetween within the current body.
                |
                | Parameters:
                | iPoint1
                |    Reference point to compute the barycenter.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | .   
                |      iPoint2
                |    Second point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | .   
                |      iRatio
                |     barycenter parameter  
                |  
                |  iOrientation
                |     To compute the barycenter of the segment [Pt1 - Pt2]  
                |  
                |  oPoint
                |     PointBetween if succeded


        :param i_point_1:
        :param i_point_2:
        :param i_ratio:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointBetween(i_point_1, i_point_2, i_ratio, i_orientation)

    def add_new_point_center(self, i_curve):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointCenter
                | o Func AddNewPointCenter(        iCurve) As
                | 
                | Creates a new circle center point within the current body.
                |
                | Parameters:
                | iCurve
                |     Reference circle
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      oPoint
                |     Created point


        :param i_curve:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointCenter(i_curve)

    def add_new_point_coord(self, i_x, i_y, i_z):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointCoord
                | o Func AddNewPointCoord(        iX,
                |                                 iY,
                |                                 iZ) As
                | 
                | Creates a new point defined by its cartesian coordinates
                | within the current body.
                |
                | Parameters:
                | iX
                |   X coordinate for the point
                | iY
                |   Y coordinate for the point
                | iZ
                |   Z coordinate for the point
                |  oPoint
                |     Created point


        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: HybridShapePointCoord()
        """

        return HybridShapePointCoord(self.hybrid_shape_factory.AddNewPointCoord(i_x, i_y, i_z))

    def add_new_point_coord_with_reference(self, i_x, i_y, i_z, i_pt):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointCoordWithReference
                | o Func AddNewPointCoordWithReference(        iX,
                |                                              iY,
                |                                              iZ,
                |                                              iPt) As
                | 
                | Creates a new point defined its the cartesian coordinates
                | regarding a reference point.
                |
                | Parameters:
                | iX
                |                         X coordinate for the point
                |  
                |  iY
                |                         Y coordinate for the point
                |  
                |  iZ
                |                         Z coordinate for the point
                |  
                |  iPt
                | 						Reference point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      oPoint
                |     Created point


        :param i_x:
        :param i_y:
        :param i_z:
        :param i_pt:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointCoordWithReference(i_x, i_y, i_z, i_pt)

    def add_new_point_datum(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointDatum
                | o Func AddNewPointDatum(        iObject) As
                | 
                | Creates a new datum of point within the current body.
                |
                | Parameters:
                | iObject
                |     The object whose topological body will be duplicated and put into created datum
                |  
                |  oPoint
                |     Created datum
                |  Note2: the object passed as parameter to create the datum has to be in the current container.
                |  Otherwise, an error occurs.


        :param i_object:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointDatum(i_object)

    def add_new_point_on_curve_along_direction(self, i_crv, i_long, i_orientation, i_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointOnCurveAlongDirection
                | o Func AddNewPointOnCurveAlongDirection(        iCrv,
                |                                                 iLong,
                |                                                 iOrientation,
                |                                                 iDirection) As
                | 
                | Creates a new point on a curve with a deafult origin point
                | and from a distance along direction.
                |
                | Parameters:
                | iCrv
                |     support curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iLong
                |     distance to default origin point.(origin of acurrent axis system)
                |  
                |  iOrientation
                |     Orientation = TRUE means that distance is measured in the other orientation of
                |    the curve.
                |  
                |  iDirection
                |     Direction = The distance at which point is created is measured in this direction.
                |  
                |  oPoint
                |     Created point


        :param i_crv:
        :param i_long:
        :param i_orientation:
        :param i_direction:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointOnCurveAlongDirection(i_crv, i_long, i_orientation, i_direction)

    def add_new_point_on_curve_from_distance(self, i_crv, i_long, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointOnCurveFromDistance
                | o Func AddNewPointOnCurveFromDistance(        iCrv,
                |                                               iLong,
                |                                               iOrientation) As
                | 
                | Creates a new point on a curve from a distance to an
                | extremity within the current body.
                |
                | Parameters:
                | iCrv
                |     support curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iLong
                |     distance to extremity
                |  
                |  iOrientation
                |     Orientation = TRUE means that distance is measured in the other orientation of
                |    the curve and from the other extremity.
                |  
                |  oPoint
                |     Created point


        :param i_crv:
        :param i_long:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointOnCurveFromDistance(i_crv, i_long, i_orientation)

    def add_new_point_on_curve_from_percent(self, i_crv, i_long, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointOnCurveFromPercent
                | o Func AddNewPointOnCurveFromPercent(        iCrv,
                |                                              iLong,
                |                                              iOrientation) As
                | 
                | Creates a new point on a curve from a ratio of distance to
                | an extremity within the current body.
                |
                | Parameters:
                | iCrv
                |     support curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iLong
                |     Ratio of curve length
                |  
                |  iOrientation
                |     Orientation = TRUE means that ratio is measured in the other orientation of
                |    the curve and from the other extremity.
                |  
                |  oPoint
                |     Created point


        :param i_crv:
        :param i_long:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointOnCurveFromPercent(i_crv, i_long, i_orientation)

    def add_new_point_on_curve_with_reference_along_direction(self, i_crv, i_pt, i_long, i_orientation, i_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointOnCurveWithReferenceAlongDirection
                | o Func AddNewPointOnCurveWithReferenceAlongDirection(        iCrv,
                |                                                              iPt,
                |                                                              iLong,
                |                                                              iOrientation,
                |                                                              iDirection) As
                | 
                | Creates a new point on a curve with a reference point and
                | from a distance along direction.
                |
                | Parameters:
                | iCrv
                |     support curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iPt
                |     reference point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iLong
                |     distance (length) to reference point
                |  
                |  iOrientation
                |     Orientation = TRUE means that distance is measured in the other orientation of the curve
                |  
                |  iDirection
                |     Direction = The distance at which point is created is measured in this direction.
                |  
                |  oPoint
                |     Created point


        :param i_crv:
        :param i_pt:
        :param i_long:
        :param i_orientation:
        :param i_direction:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointOnCurveWithReferenceAlongDirection(i_crv, i_pt, i_long,
                                                                                       i_orientation, i_direction)

    def add_new_point_on_curve_with_reference_from_distance(self, i_crv, i_pt, i_long, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointOnCurveWithReferenceFromDistance
                | o Func AddNewPointOnCurveWithReferenceFromDistance(        iCrv,
                |                                                            iPt,
                |                                                            iLong,
                |                                                            iOrientation) As
                | 
                | Creates a new point on a curve with a reference point and
                | from a distance within the current body.
                |
                | Parameters:
                | iCrv
                |     support curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iPt
                |     reference point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iLong
                |     distance (length) to reference point
                |  
                |  iOrientation
                |     Orientation = TRUE means that distance is measured in the other orientation of the curve
                |  
                |  oPoint
                |     Created point


        :param i_crv:
        :param i_pt:
        :param i_long:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointOnCurveWithReferenceFromDistance(i_crv, i_pt, i_long, i_orientation)

    def add_new_point_on_curve_with_reference_from_percent(self, i_crv, i_pt, i_long, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointOnCurveWithReferenceFromPercent
                | o Func AddNewPointOnCurveWithReferenceFromPercent(        iCrv,
                |                                                           iPt,
                |                                                           iLong,
                |                                                           iOrientation) As
                | 
                | Creates a new point on a curve with a reference point and
                | from a ratio of distance within the current body.
                |
                | Parameters:
                | iCrv
                |     Support curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iPt
                |     reference point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iLong
                |     Ratio of curve length
                |  
                |  iOrientation
                |     Orientation = TRUE means that ratio is measured in the other orientation of the curve
                |  
                |  oPoint
                |     Created point


        :param i_crv:
        :param i_pt:
        :param i_long:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointOnCurveWithReferenceFromPercent(i_crv, i_pt, i_long, i_orientation)

    def add_new_point_on_plane(self, i_plane, i_x, i_y):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointOnPlane
                | o Func AddNewPointOnPlane(        iPlane,
                |                                   iX,
                |                                   iY) As
                | 
                | Creates a new point on a plane within the current body.
                |
                | Parameters:
                | iPlane
                |     Support plane 
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iX
                |     X cartesian coordinates in the plane.
                |  
                |  iY
                |     Y cartesian coordinates in the plane.
                |  
                |  oPoint
                |     Created point


        :param i_plane:
        :param i_x:
        :param i_y:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointOnPlane(i_plane, i_x, i_y)

    def add_new_point_on_plane_with_reference(self, i_plane, i_pt, i_x, i_y):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointOnPlaneWithReference
                | o Func AddNewPointOnPlaneWithReference(        iPlane,
                |                                                iPt,
                |                                                iX,
                |                                                iY) As
                | 
                | Creates a new point on a plane with a reference point within
                | the current body.
                |
                | Parameters:
                | iPlane
                |     Support plane
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPt
                |     Reference plane
                | Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iX
                |    X cartesian coordinates in the plane.
                |  
                |  iY
                |     Y cartesian coordinates in the plane.
                |  
                |  oPoint
                |     Created point


        :param i_plane:
        :param i_pt:
        :param i_x:
        :param i_y:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointOnPlaneWithReference(i_plane, i_pt, i_x, i_y)

    def add_new_point_on_surface(self, i_surface, i_direction, i_x):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointOnSurface
                | o Func AddNewPointOnSurface(        iSurface,
                |                                     iDirection,
                |                                     iX) As
                | 
                | Creates a new point on a surface within the current body.
                |
                | Parameters:
                | iSurface
                |     Support surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iDirection
                |     Direction from the reference point in which the point is computed.
                |  
                |  iX
                |     geodesic length to reference point
                |  
                |  oPoint
                |     Created point


        :param i_surface:
        :param i_direction:
        :param i_x:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointOnSurface(i_surface, i_direction, i_x)

    def add_new_point_on_surface_with_reference(self, i_surface, i_pt, i_direction, i_x):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointOnSurfaceWithReference
                | o Func AddNewPointOnSurfaceWithReference(        iSurface,
                |                                                  iPt,
                |                                                  iDirection,
                |                                                  iX) As
                | 
                | Creates a new point on a surface with a reference point
                | within the current body.
                |
                | Parameters:
                | iSurface
                |     Support surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iPt
                |     reference point.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iDirection
                |     Direction from the reference point in which the point is computed.
                |  
                |  iX
                |     geodesic length to reference point
                |  
                |  oPoint
                |     Created point


        :param i_surface:
        :param i_pt:
        :param i_direction:
        :param i_x:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointOnSurfaceWithReference(i_surface, i_pt, i_direction, i_x)

    def add_new_point_tangent(self, i_curve, i_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPointTangent
                | o Func AddNewPointTangent(        iCurve,
                |                                   iDirection) As
                | 
                | Creates a new tangent to curve point within the current
                | body.
                |
                | Parameters:
                | iCurve
                |     Reference curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iDirection
                |     Direction in which tangent points are computed
                |  
                |  oPoint
                |     Created point


        :param i_curve:
        :param i_direction:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPointTangent(i_curve, i_direction)

    def add_new_polyline(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPolyline
                | o Func AddNewPolyline(    ) As
                | 
                | Creates a new Polyline within the current body.
                |
                | Parameters:
                | oPolyline
                |    The Polyline object if succeded


        :return:
        """
        return self.hybrid_shape_factory.AddNewPolyline()

    def add_new_position_transfo(self, i_mode):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewPositionTransfo
                | o Func AddNewPositionTransfo(        iMode) As
                | 
                | Creates a new PositionTransfo within the current body.
                |
                | Parameters:
                | iMode
                |     Positioning mode.
                |  
                |  oExt
                |     Created positioning transformation (i.e. positioned wire / profile).


        :param i_mode:
        :return:
        """
        return self.hybrid_shape_factory.AddNewPositionTransfo(i_mode)

    def add_new_project(self, i_element, i_support):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewProject
                | o Func AddNewProject(        iElement,
                |                              iSupport) As
                | 
                | Creates a new Project within the current body.
                |
                | Parameters:
                | iElement
                |     Element to project (point, curve).
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      iSupport
                |     Curve or surface support for projection.  
                |  Sub-element(s) supported (see 
                |  object):  see 
                | , 
                |  and 
                | .   
                |      oProjection
                |     Created projection


        :param i_element:
        :param i_support:
        :return:
        """
        return self.hybrid_shape_factory.AddNewProject(i_element, i_support)

    def add_new_reflect_line(self, i_support, i_dir, i_angle, i_orientation_support, i_orientation_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewReflectLine
                | o Func AddNewReflectLine(        iSupport,
                |                                  iDir,
                |                                  iAngle,
                |                                  iOrientationSupport,
                |                                  iOrientationDirection) As
                | 
                | Deprecated: V5R17
                | CATIAHybridShapeFactory#AddNewReflectLineWithType Creates a
                | new ReflectLine within the current body. Create a
                | reflectline curve on a support surface along a direction
                | with an angle.
                |
                | Parameters:
                | iSupport
                |     Support surface.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | . 
                |      iAngle
                |     Angle of the reflectline.
                |  
                |  iOrientationSupport
                |     Manage the angle used to compute the reflectline.
                |    Value can be 1 or -1 
                |  
                |  iOrientationDirection
                |     Manage the angle used to compute the reflectline.
                |    Value can be 1 or -1     
                |  
                |  oReflectLine
                |     Created reflectline.


        :param i_support:
        :param i_dir:
        :param i_angle:
        :param i_orientation_support:
        :param i_orientation_direction:
        :return:
        """
        return self.hybrid_shape_factory.AddNewReflectLine(i_support, i_dir, i_angle, i_orientation_support,
                                                           i_orientation_direction)

    def add_new_reflect_line_with_type(self, i_support, i_dir, i_angle, i_orientation_support, i_orientation_direction,
                                       i_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewReflectLineWithType
                | o Func AddNewReflectLineWithType(        iSupport,
                |                                          iDir,
                |                                          iAngle,
                |                                          iOrientationSupport,
                |                                          iOrientationDirection,
                |                                          iType) As
                | 
                | Creates a new ReflectLine within the current body. Create a
                | reflectline curve on a support surface along a direction
                | with an angle.
                |
                | Parameters:
                | iSupport
                |     Support surface.
                |  
                |  iAngle
                |     Angle of the reflectline.
                |  
                |  iOrientationSupport
                |     Manage the angle used to compute the reflectline.
                |    Value can be 1 or -1 
                |  
                |  iOrientationDirection
                |     Manage the angle used to compute the reflectline.
                |    Value can be 1 or -1     
                |  
                |  iType
                |     Manage the type used to compute the reflectline.
                |    Value can be 0 or 1
                |    Returns or sets whether the reflectline curve is or should be created with the normal
                |    to the support or the tangent plane to the support.
                |    Role: The TypeSolution indicates whether the created reflectline curve
                |    is compute with the angle between the normale to the support and the direction 
                |    or with the angle between the tangent plane to the support and the direction..
                |    Legal values: 0 for the normal and 1 for the tangent plane.
                |  
                |  oReflectLine
                |     Created reflectline.


        :param i_support:
        :param i_dir:
        :param i_angle:
        :param i_orientation_support:
        :param i_orientation_direction:
        :param i_type:
        :return:
        """
        return self.hybrid_shape_factory.AddNewReflectLineWithType(i_support, i_dir, i_angle, i_orientation_support,
                                                                   i_orientation_direction, i_type)

    def add_new_revol(self, i_object_to_extrude, i_offset_debut, i_offset_fin, i_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewRevol
                | o Func AddNewRevol(        iObjectToExtrude,
                |                            iOffsetDebut,
                |                            iOffsetFin,
                |                            iAxis) As
                | 
                | Creates a new revolution within the current body.
                |
                | Parameters:
                | iObjectToExtrude
                |     Profile to be revolved
                | Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                | , 
                |  and 
                | .   
                |      iOffsetDebut
                |     Angle value  
                |  
                |  iOffsetFin
                |     Angle value  
                |  
                |  iAxis
                |     Revolution axis ( line that has to be in the profil plane
                | Sub-element(s) supported (see 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      oRevolObject
                |     Revolved result


        :param i_object_to_extrude:
        :param i_offset_debut:
        :param i_offset_fin:
        :param i_axis:
        :return:
        """
        return self.hybrid_shape_factory.AddNewRevol(i_object_to_extrude, i_offset_debut, i_offset_fin, i_axis)

    def add_new_rotate(self, i_to_rotate, i_axis, i_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewRotate
                | o Func AddNewRotate(        iToRotate,
                |                             iAxis,
                |                             iAngle) As
                | 
                | Creates a new Rotate within the current body.
                |
                | Parameters:
                | iToRotate
                |     point, curve, surface or solid to transform.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                | , 
                |  and 
                | . 
                |      iAxis
                |     Rotation axis.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | . 
                |      iAngle
                |     Rotation angle.
                |  
                |  oRotate
                |    Created rotation.


        :param i_to_rotate:
        :param i_axis:
        :param i_angle:
        :return:
        """
        return self.hybrid_shape_factory.AddNewRotate(i_to_rotate, i_axis, i_angle)

    def add_new_section(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewSection
                | o Func AddNewSection(    ) As
                | 
                | Creates a new section.
                |
                | Parameters:
                | oSection
                |      Created Section


        :return:
        """
        return self.hybrid_shape_factory.AddNewSection()

    def add_new_sphere(self, i_center, i_axis, i_radius, i_begin_parallel_angle, i_end_parallel_angle,
                       i_begin_meridian_angle, i_end_meridian_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewSphere
                | o Func AddNewSphere(        iCenter,
                |                             iAxis,
                |                             iRadius,
                |                             iBeginParallelAngle,
                |                             iEndParallelAngle,
                |                             iBeginMeridianAngle,
                |                             iEndMeridianAngle) As
                | 
                | Creates a new Sphere within the current body.
                |
                | Parameters:
                | iCenter
                |     Sphere center.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | .   
                |      iAxis
                |     Sphere axis
                |  
                |  iRadius
                |     Radius
                |  
                |  iBeginParallelAngle
                |     Angle value  
                |  
                |  iEndParallelAngle
                |     Angle value  
                |  
                |  iBeginMeridianAngle
                |     Angle value  
                |  
                |  iEndMeridianAngle
                |     Angle value  
                |  
                |  oSphereObject
                |     Sphere result


        :param i_center:
        :param i_axis:
        :param i_radius:
        :param i_begin_parallel_angle:
        :param i_end_parallel_angle:
        :param i_begin_meridian_angle:
        :param i_end_meridian_angle:
        :return:
        """
        return self.hybrid_shape_factory.AddNewSphere(i_center, i_axis, i_radius, i_begin_parallel_angle,
                                                      i_end_parallel_angle, i_begin_meridian_angle,
                                                      i_end_meridian_angle)

    def add_new_spine(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewSpine
                | o Func AddNewSpine(    ) As
                | 
                | Creates a new spine within the current body.
                |
                | Parameters:
                | oExt
                |     CATIAHybridShapeSpine created


        :return:
        """
        return self.hybrid_shape_factory.AddNewSpine()

    def add_new_spiral(self, i_type, i_support, i_center_point, i_axis, i_starting_radius, i_clockwise_revolution):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewSpiral
                | o Func AddNewSpiral(        iType,
                |                             iSupport,
                |                             iCenterPoint,
                |                             iAxis,
                |                             iStartingRadius,
                |                             iClockwiseRevolution) As
                | 
                | Creates a new Spiral within the current body.
                |
                | Parameters:
                | iType
                |        Spiral is defined by AngleRadius, AnglePitch or PitchRadius.
                |    
                |  iSupport
                |       Spiral planar support.
                |    
                |  iCenterPoint
                |       Center point.
                |    
                |  iAxis
                |       Axis.
                |    
                |  iStartingRadius
                |       Defines the starting point: distance from the center point on the axis.
                |    
                |  iClockwiseRevolution
                |       Revolutions are clockwise if TRUE, counterclockwise if FALSE.
                |  
                |  oSpiral
                |    The Spiral object if succeded


        :param i_type:
        :param i_support:
        :param i_center_point:
        :param i_axis:
        :param i_starting_radius:
        :param i_clockwise_revolution:
        :return:
        """
        return self.hybrid_shape_factory.AddNewSpiral(i_type, i_support, i_center_point, i_axis, i_starting_radius,
                                                      i_clockwise_revolution)

    def add_new_spline(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewSpline
                | o Func AddNewSpline(    ) As
                | 
                | Creates a new Spline within the current body.
                |
                | Parameters:
                | oSpline
                |     Created spline.


        :return:
        """
        return self.hybrid_shape_factory.AddNewSpline()

    def add_new_surface_datum(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewSurfaceDatum
                | o Func AddNewSurfaceDatum(        iObject) As
                | 
                | Creates a new datum of surface within the current body.
                |
                | Parameters:
                | iObject
                |     The object whose topological body will be duplicated and put into created datum
                |  
                |  oSurface
                |    Created surface
                |  Note2: the object passed as parameter to create the datum has to be in the current container.
                |  Otherwise, an error occurs.


        :param i_object:
        :return:
        """
        return self.hybrid_shape_factory.AddNewSurfaceDatum(i_object)

    def add_new_sweep_circle(self, i_guide_1):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewSweepCircle
                | o Func AddNewSweepCircle(        iGuide1) As
                | 
                | Creates a new SweepCircle within the current body.
                |
                | Parameters:
                | iGuide1
                |     First guide or center curve.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      oExt
                |     Created swept surface.


        :param i_guide_1:
        :return:
        """
        return self.hybrid_shape_factory.AddNewSweepCircle(i_guide_1)

    def add_new_sweep_conic(self, ip_ia_guide_1):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewSweepConic
                | o Func AddNewSweepConic(        ipIAGuide1) As
                | 
                | Creates a new SweepConic within the current body.
                |
                | Parameters:
                | iGuide1
                |     First guide curve.
                |  
                |  opIASweepConic
                |     Created swept surface.


        :param ip_ia_guide_1:
        :return:
        """
        return self.hybrid_shape_factory.AddNewSweepConic(ip_ia_guide_1)

    def add_new_sweep_explicit(self, i_profile, i_guide):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewSweepExplicit
                | o Func AddNewSweepExplicit(        iProfile,
                |                                    iGuide) As
                | 
                | Creates a new SweepExplicit within the current body.
                |
                | Parameters:
                | iProfile
                |     Profile.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                |  and 
                | . 
                |      iGuide
                |     First guide curve.
                |  Sub-element(s) supported (see 
                |  object):  see 
                |  and 
                | . 
                |      oExt
                |     Created swept surface.


        :param i_profile:
        :param i_guide:
        :return:
        """
        return self.hybrid_shape_factory.AddNewSweepExplicit(i_profile, i_guide)

    def add_new_sweep_line(self, i_guide_1):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewSweepLine
                | o Func AddNewSweepLine(        iGuide1) As
                | 
                | Creates a new SweepLine within the current body.
                |
                | Parameters:
                | iGuide1
                |     First guide curve.
                |  
                |  oExt
                |     Created swept surface.


        :param i_guide_1:
        :return:
        """
        return self.hybrid_shape_factory.AddNewSweepLine(i_guide_1)

    def add_new_symmetry(self, i_object, i_reference):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewSymmetry
                | o Func AddNewSymmetry(        iObject,
                |                               iReference) As
                | 
                | Creates a new Symmetry within the current body.
                |
                | Parameters:
                | iObject
                |     Point, curve, surface or solid to transform.
                |  Sub-element(s) supported (see 
                | 
                |  object):  see 
                | , 
                | , 
                |  and 
                | . 
                |      iReference
                |     Point, line or reference plane.
                |  Sub-element(s) supported (see 
                |  object):  see 
                | , 
                |  and 
                | . 
                |      oSymmetry
                |     Created symmetry.


        :param i_object:
        :param i_reference:
        :return:
        """
        return self.hybrid_shape_factory.AddNewSymmetry(i_object, i_reference)

    def add_new_transfer(self, i_element_to_transfer, i_type_of_transfer):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewTransfer
                | o Func AddNewTransfer(        iElementToTransfer,
                |                               iTypeOfTransfer) As
                | 
                | Creates a new Transfer within the current body. Note:
                | require DL1 license.
                |
                | Parameters:
                | iElementToTransfer
                | 	The element to transfer
                |  
                |  iTypeOfTransfer
                | 	The type of transfer
                |  
                |  oExt
                |     Created Transfer operation.


        :param i_element_to_transfer:
        :param i_type_of_transfer:
        :return:
        """
        return self.hybrid_shape_factory.AddNewTransfer(i_element_to_transfer, i_type_of_transfer)

    def add_new_translate(self, i_element, i_direction, i_distance):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewTranslate
                | o Func AddNewTranslate(        iElement,
                |                                iDirection,
                |                                iDistance) As
                | 
                | Creates a new Translate within the current body.
                |
                | Parameters:
                | iElement
                |     Point, curve, surface or solid to translate. 
                |  
                |  iDirection
                |     Translation direction.
                |  
                |  iDistance
                |    Translation Distance. 
                |  
                |  oTranslate
                |     Created translation
                |  
                |  oTranslate
                |      Created Translate (Empty feature)
                |   Note: Then translate mode and inputs has to be initialized
                |  
                | 
                |  See also:


        :param i_element:
        :param i_direction:
        :param i_distance:
        :return:
        """
        return self.hybrid_shape_factory.AddNewTranslate(i_element, i_direction, i_distance)

    def add_new_unfold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewUnfold
                | o Func AddNewUnfold(    ) As
                | 
                | Creates a new Unfold within the current body. Note: require
                | DL1 license.
                |
                | Parameters:
                | oExt
                |     Created unfold operation.


        :return:
        """
        return self.hybrid_shape_factory.AddNewUnfold()

    def add_new_volume_datum(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewVolumeDatum
                | o Func AddNewVolumeDatum(        iObject) As
                | 
                | Creates a new datum of volume within the current body. Note:
                | requires GSO License
                |
                | Parameters:
                | iObject
                |     The object whose topological body will be duplicated and put into created datum
                |  
                |  oVolume
                |    Created Volume
                |  Note2: the object passed as parameter to create the datum has to be in the current container.
                |  Otherwise, an error occurs.


        :param i_object:
        :return:
        """
        return self.hybrid_shape_factory.AddNewVolumeDatum(i_object)

    def add_new_wrap_curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewWrapCurve
                | o Func AddNewWrapCurve(    ) As
                | 
                | Creates a new Wrap Curve Surface within the current body.
                | Note: require GSO license.
                |
                | Parameters:
                | oWrapCurve
                |    The Wrap Curve object if succeded


        :return:
        """
        return self.hybrid_shape_factory.AddNewWrapCurve()

    def add_new_wrap_surface(self, i_body_to_deform):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddNewWrapSurface
                | o Func AddNewWrapSurface(        iBodyToDeform) As
                | 
                | Creates a new Wrap Surface within the current body. Note:
                | require GSO license.
                |
                | Parameters:
                | :
                |  iBodyToDeform    Body to deform with a  Wrap Surface
                |  
                |  oWrapSurface
                |    The Wrap Surface object if succeded


        :param i_body_to_deform:
        :return:
        """
        return self.hybrid_shape_factory.AddNewWrapSurface(i_body_to_deform)

    def change_feature_name(self, i_elem, name):
        """
        .. note::
            CAA V5 Visual Basic help

                | ChangeFeatureName
                | o Sub ChangeFeatureName(        iElem,
                |                                 Name)
                | 
                | Set display name for Shape Design Features.
                |
                | Parameters:
                | iElem
                |        Element to rename 
                |    
                |  Name
                |        User name


        :param i_elem:
        :param name:
        :return:
        """
        return self.hybrid_shape_factory.ChangeFeatureName(i_elem, name)

    def delete_object_for_datum(self, i_object):
        """
        .. note::
            CAA V5 Visual Basic help

                | DeleteObjectForDatum
                | o Sub DeleteObjectForDatum(        iObject)
                | 
                | Deletes an object within the current body.
                |
                | Parameters:
                | iObject
                |     Object to delete


        :param i_object:
        :return:
        """
        return self.hybrid_shape_factory.DeleteObjectForDatum(i_object)

    def gsm_visibility(self, i_elem, show):
        """
        .. note::
            CAA V5 Visual Basic help

                | GSMVisibility
                | o Sub GSMVisibility(        iElem,
                |                             Show)
                | 
                | Set Visibility attribut for Shape Design Features.
                |
                | Parameters:
                | iElem
                |        Element to show/NoShow 
                |    
                |  Show
                |        = 0 NoShow , 1= Show


        :param i_elem:
        :param show:
        :return:
        """
        return self.hybrid_shape_factory.GSMVisibility(i_elem, show)

    def get_geometrical_feature_type(self, i_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetGeometricalFeatureType
                | o Func GetGeometricalFeatureType(        iElem) As
                | 
                | Returns type of "geometrical" shape Design feature .
                |
                | Parameters:
                | iElem
                |    Reference element  
                |  
                |  oType
                |      Type of feature 
                |    = 0 , Unknown 
                |    = 1 , Point 
                |    = 2 , Curve 
                |    = 3 , Line 
                |    = 4 , Circle 
                |    = 5 , Surface 
                |    = 6 , Plane 
                |    = 7 , Solid, Volume 
                |   Level of availability = V5R14


        :param i_elem:
        :return:
        """
        return self.hybrid_shape_factory.GetGeometricalFeatureType(i_elem)

    def __repr__(self):
        return f'HybridShapeFactory(name="{self.name}")'
