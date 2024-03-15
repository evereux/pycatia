#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.geometric_elements import GeometricElements
from pycatia.sketcher_interfaces.circle_2D import Circle2D
from pycatia.sketcher_interfaces.control_point_2D import ControlPoint2D
from pycatia.sketcher_interfaces.ellipse_2D import Ellipse2D
from pycatia.sketcher_interfaces.geometry_2D import Geometry2D
from pycatia.sketcher_interfaces.hyperbola_2D import Hyperbola2D
from pycatia.sketcher_interfaces.line_2D import Line2D
from pycatia.sketcher_interfaces.parabola_2D import Parabola2D
from pycatia.sketcher_interfaces.point_2D import Point2D
from pycatia.sketcher_interfaces.spline_2D import Spline2D
from pycatia.system_interfaces.any_object import AnyObject


class Factory2D(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Factory2D
                | 
                | Interface to the factory for 2D objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.factory_2d = com_object

    def create_circle(self, i_center_x: float, i_center_y: float, i_radius: float, i_start_param: float,
                      i_end_param: float) -> Circle2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateCircle(double iCenterX,
                | double iCenterY,
                | double iRadius,
                | double iStartParam,
                | double iEndParam) As Circle2D
                | 
                |     Creates and returns a 2D circle arc.
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X coordinate of the circle center 
                |         iCenterY
                |             The Y coordinate of the circle center 
                |         iRadius
                |             The radius of the circle 
                |         iStartParam
                |             The beginning parameter of the circle.
                |             This parameter is an angle value between 0 included and 2PI
                |             excluded. Parameter values are computed from the axis horizontal direction in
                |             the trigonometrical direction. 
                |         iEndParam
                |             The end parameter of the circle.
                |             This parameter may take any value between iStartParam excluded and
                |             4PI included.

        :param float i_center_x:
        :param float i_center_y:
        :param float i_radius:
        :param float i_start_param:
        :param float i_end_param:
        :rtype: Circle2D
        """
        return Circle2D(self.factory_2d.CreateCircle(i_center_x, i_center_y, i_radius, i_start_param, i_end_param))

    def create_closed_circle(self, i_center_x: float, i_center_y: float, i_radius: float) -> Circle2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateClosedCircle(double iCenterX,
                | double iCenterY,
                | double iRadius) As Circle2D
                | 
                |     Creates and returns a closed 2D circle.
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X coordinate of the circle center 
                |         iCenterY
                |             The Y coordinate of the circle center 
                |         iRadius
                |             The radius of the circle

        :param float i_center_x:
        :param float i_center_y:
        :param float i_radius:
        :rtype: Circle2D
        """
        return Circle2D(self.factory_2d.CreateClosedCircle(i_center_x, i_center_y, i_radius))

    def create_closed_ellipse(self, i_center_x: float, i_center_y: float, i_major_x: float, i_major_y: float,
                              i_major_radius: float, i_minor_radius: float) -> Ellipse2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateClosedEllipse(double iCenterX,
                | double iCenterY,
                | double iMajorX,
                | double iMajorY,
                | double iMajorRadius,
                | double iMinorRadius) As Ellipse2D
                | 
                |     Creates and returns a closed 2D ellipse.
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X coordinate of the ellipse center 
                |         iCenterY
                |             The Y coordinate of the ellipse center 
                |         iMajorX
                |             The X component of the major axis direction 
                |         iMajorY
                |             The Y component of the Major axis direction 
                |         iMajorRadius
                |             The length of the major axis 
                |         iMinorRadius
                |             The length of the minor axis

        :param float i_center_x:
        :param float i_center_y:
        :param float i_major_x:
        :param float i_major_y:
        :param float i_major_radius:
        :param float i_minor_radius:
        :rtype: Ellipse2D
        """
        return Ellipse2D(
            self.factory_2d.CreateClosedEllipse(i_center_x, i_center_y, i_major_x, i_major_y, i_major_radius,
                                                i_minor_radius))

    def create_control_point(self, i_x: float, i_y: float) -> ControlPoint2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateControlPoint(double iX,
                | double iY) As ControlPoint2D
                | 
                |     Creates and returns a 2D spline control point.
                | 
                |     Parameters:
                | 
                |         iX
                |             The X coordinate of point to create 
                |         iY
                |             The Y coordinate of point to create

        :param float i_x:
        :param float i_y:
        :rtype: ControlPoint2D
        """
        return ControlPoint2D(self.factory_2d.CreateControlPoint(i_x, i_y))

    def create_ellipse(self, i_center_x: float, i_center_y: float, i_major_x: float, i_major_y: float,
                       i_major_radius: float, i_minor_radius: float, i_start_param: float,
                       i_end_param: float) -> Ellipse2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateEllipse(double iCenterX,
                | double iCenterY,
                | double iMajorX,
                | double iMajorY,
                | double iMajorRadius,
                | double iMinorRadius,
                | double iStartParam,
                | double iEndParam) As Ellipse2D
                | 
                |     Creates and returns a 2D ellipse arc.
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X coordinate of the ellipse center 
                |         iCenterY
                |             The Y coordinate of the ellipse center 
                |         iMajorX
                |             The X component of the major axis direction 
                |         iMajorY
                |             The Y component of the major axis direction 
                |         iMajorRadius
                |             The length of the major axis 
                |         iMinorRadius
                |             The length of the minor axis 
                |         iStartParam
                |             The beginning parameter of the ellipse.
                |             This parameter is an angle value between 0 included and 2PI
                |             excluded. Parameter values are computed from the major axis direction in the
                |             trigonometrical direction. 
                |         iEndParam
                |             The end parameter of the ellipse.
                |             This parameter may take any value between iStartParam excluded and
                |             4PI included.

        :param float i_center_x:
        :param float i_center_y:
        :param float i_major_x:
        :param float i_major_y:
        :param float i_major_radius:
        :param float i_minor_radius:
        :param float i_start_param:
        :param float i_end_param:
        :rtype: Ellipse2D
        """
        return Ellipse2D(
            self.factory_2d.CreateEllipse(i_center_x, i_center_y, i_major_x, i_major_y, i_major_radius, i_minor_radius,
                                          i_start_param, i_end_param))

    def create_hyperbola(self, i_center_x: float, i_center_y: float, i_axis_x: float, i_axis_y: float,
                         i_major_radius: float, i_minor_radius: float) -> Hyperbola2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateHyperbola(double iCenterX,
                | double iCenterY,
                | double iAxisX,
                | double iAxisY,
                | double iMajorRadius,
                | double iMinorRadius) As Hyperbola2D
                | 
                |     Creates and returns a hyperbola.
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X coordinate of the hyperbola center 
                |         iCenterY
                |             The Y coordinate of the hyperbola center 
                |         iAxisX
                |             The X coordinate of the major axis direction 
                |         iAxisY
                |             The Y coordinate of the major axis direction 
                |         iMajorRadius
                |             The length of the major axis 
                |         iMinorRadius
                |             The length of the minor axis

        :param float i_center_x:
        :param float i_center_y:
        :param float i_axis_x:
        :param float i_axis_y:
        :param float i_major_radius:
        :param float i_minor_radius:
        :rtype: Hyperbola2D
        """
        return Hyperbola2D(
            self.factory_2d.CreateHyperbola(i_center_x, i_center_y, i_axis_x, i_axis_y, i_major_radius, i_minor_radius))

    def create_intersection(self, i_geometry: Reference) -> Geometry2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateIntersection(Reference iGeometry) As Geometry2D
                | 
                |     Creates and returns the intersection of an object with the
                |     sketch.
                | 
                |     Parameters:
                | 
                |         iGeometry
                |             The object to intersect with the sketch

        :param Reference i_geometry:
        :rtype: Geometry2D
        """
        return Geometry2D(self.factory_2d.CreateIntersection(i_geometry.com_object))

    def create_intersections(self, i_geometry: Reference) -> GeometricElements:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateIntersections(Reference iGeometry) As
                | GeometricElements
                | 
                |     Creates and returns the possible intersections of an object with the
                |     sketch.
                | 
                |     Parameters:
                | 
                |         iGeometry
                |             The object to intersect with the sketch

        :param Reference i_geometry:
        :rtype: GeometricElements
        """
        return GeometricElements(self.factory_2d.CreateIntersections(i_geometry.com_object))

    def create_line(self, i_x1: float, i_y1: float, i_x2: float, i_y2: float) -> Line2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateLine(double iX1,
                | double iY1,
                | double iX2,
                | double iY2) As Line2D
                | 
                |     Creates and returns a 2D line.
                | 
                |     Parameters:
                | 
                |         iX1
                |             The X coordinate of line first extremity 
                |         iY1
                |             The Y coordinate of line first extremity 
                |         iX2
                |             The X coordinate of line second extremity 
                |         iY2
                |             The Y coordinate of line second extremity

        :param float i_x1:
        :param float i_y1:
        :param float i_x2:
        :param float i_y2:
        :rtype: Line2D
        """
        return Line2D(self.factory_2d.CreateLine(i_x1, i_y1, i_x2, i_y2))

    def create_line_from_vector(self, i_x1: float, i_y1: float, i_ux: float, i_uy: float) -> Line2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateLineFromVector(double iX1,
                | double iY1,
                | double iUX,
                | double iUY) As Line2D
                | 
                |     Creates and returns a 2D line.
                | 
                |     Parameters:
                | 
                |         iX1
                |             The X coordinate of the line origin 
                |         iY1
                |             The Y coordinate of the line origin 
                |         iUX
                |             The X component of the line vector 
                |         iUY
                |             The Y component of the line vector

        :param float i_x1:
        :param float i_y1:
        :param float i_ux:
        :param float i_uy:
        :rtype: Line2D
        """
        return Line2D(self.factory_2d.CreateLineFromVector(i_x1, i_y1, i_ux, i_uy))

    def create_parabola(self, i_center_x: float, i_center_y: float, i_axis_x: float, i_axis_y: float,
                        i_focal_distance: float) -> Parabola2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateParabola(double iCenterX,
                | double iCenterY,
                | double iAxisX,
                | double iAxisY,
                | double iFocalDistance) As Parabola2D
                | 
                |     Creates and returns a parabola.
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X coordinate of the parabola center 
                |         iCenterY
                |             The Y coordinate of the parabola center 
                |         iAxisX
                |             The X coordinate of the major axis direction 
                |         iAxisY
                |             The Y coordinate of the major axis direction 
                |         iFocalDistance
                |             The parabola focal distance

        :param float i_center_x:
        :param float i_center_y:
        :param float i_axis_x:
        :param float i_axis_y:
        :param float i_focal_distance:
        :rtype: Parabola2D
        """
        return Parabola2D(self.factory_2d.CreateParabola(i_center_x, i_center_y, i_axis_x, i_axis_y, i_focal_distance))

    def create_point(self, i_x: float, i_y: float) -> Point2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreatePoint(double iX,
                | double iY) As Point2D
                | 
                |     Creates and returns a 2D point.
                | 
                |     Parameters:
                | 
                |         iX
                |             The X coordinate of point to create 
                |         iY
                |             The Y coordinate of point to create

        :param float i_x:
        :param float i_y:
        :rtype: Point2D
        """
        return Point2D(self.factory_2d.CreatePoint(i_x, i_y))

    def create_projection(self, i_geometry: Reference) -> Geometry2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateProjection(Reference iGeometry) As Geometry2D
                | 
                |     Creates and returns the projection of an object on the
                |     sketch.
                | 
                |     Parameters:
                | 
                |         iGeometry
                |             The object to project on the sketch

        :param Reference i_geometry:
        :rtype: Geometry2D
        """
        return Geometry2D(self.factory_2d.CreateProjection(i_geometry.com_object))

    def create_projections(self, i_geometry: Reference) -> GeometricElements:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateProjections(Reference iGeometry) As
                | GeometricElements
                | 
                |     Creates and returns the possible projections of an object on the
                |     sketch.
                | 
                |     Parameters:
                | 
                |         iGeometry
                |             The object to project on the sketch

        :param Reference i_geometry:
        :rtype: GeometricElements
        """
        return GeometricElements(self.factory_2d.CreateProjections(i_geometry.com_object))

    def create_spline(self, i_poles: tuple) -> Spline2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func CreateSpline(CATSafeArrayVariant iPoles) As Spline2D
                | 
                |     Creates and returns a 2D b-spline.
                | 
                |     Parameters:
                | 
                |         iPoles
                |             An array of CATIAPoint2D forming the poles of the
                |             b-spline.

        :param tuple i_poles:
        :rtype: Spline2D
        """
        return Spline2D(self.factory_2d.CreateSpline(tuple(p2d.com_object for p2d in i_poles)))

    def __repr__(self):
        return f'Factory2D(name="{self.name}")'
