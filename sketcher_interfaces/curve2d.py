#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .geometry2d import Geometry2D
from .point2d import Point2D


class Curve2D(Geometry2D):
    """
        .. note::
            CAA V5 Visual Basic help

                | Class defining a curve in 2D Space.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.curve2d = com_object

    @property
    def continuity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Continuity
                | o Property Continuity(    ) As short
                | 
                | Returns the highest level of geometric continuity the curve
                | possesses.
                |
                | Parameters:
                | oLevel
                |   The maximum geometric continuity level

        :return: int
        """
        return self.curve2d.Continuity

    @property
    def end_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndPoint
                | o Property EndPoint(    ) As Point2D
                | 
                | Returns the end point of the curve. The end point is decided
                | with respect to the logical flow imposed on the curve by
                | the object.
                |
                | Parameters:
                | oEndPoint
                |   The end point of the curve


        """
        return Point2D(self.curve2d.EndPoint)

    @property
    def period(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Period
                | o Property Period(    ) As double
                | 
                | Returns the period of a periodic curve.
                |
                | Parameters:
                | oPeriod
                |   The period of the curve.

        :return: float
        """
        return self.curve2d.Period

    @property
    def start_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartPoint
                | o Property StartPoint(    ) As Point2D
                | 
                | Returns the start point of the curve. The start point is
                | decided with respect to the logical flow imposed on the
                | curve by the object.
                |
                | Parameters:
                | oStartPoint
                |   The start point of the curve

        :return: Point2D()
        """
        return Point2D(self.curve2d.StartPoint)

    def get_curvature(self, i_param, o_curvature):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCurvature
                | o Sub GetCurvature(    double    iParam,
                |                        CATSafeArrayVariant    oCurvature)
                | 
                | Returns the curvature and curvature direction at the        parameter
                | specified.
                |
                | Parameters:
                | iParam
                |   The parameter of the chosen point on the curve.
                | oCurvature[0]
                |   The curvature at the specified parameter.
                | oCurvature[1;2]
                |   The unit-vector of curvature direction at the specified
                |   parameter.

        :return: float
        """
        return self.curve2d.GetCurvature(i_param, o_curvature)

    def get_derivatives(self, i_param, o_derivative):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDerivatives
                | o Sub GetDerivatives(double iParam,
                |                      CATSafeArrayVariant oDerivative)
                | 
                | Returns the first, second and third derivatives at the
                | parameter specified.
                |
                | Parameters:
                | iParam
                |   The parameter of the chosen point on the curve.
                | oDerivative[0]
                |   First degree derivative.
                | oDerivative[1]
                |   Second degree derivative.
                | oDerivative[2]
                |   Third degree derivative.

        :return: tuple
        """
        return self.curve2d.GetDerivatives(i_param, o_derivative)

    def get_end_points(self, o_end_points):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetEndPoints
                | o Sub GetEndPoints(    CATSafeArrayVariant    oEndPoints)
                | 
                | Returns the end-points of the curve. The start point and the end
                | point are decided with respect to the logical flow imposed
                | on the curve by the object.
                |
                | Parameters:
                | oEndPoints[0]
                |   The x coordinate of the start point
                | oEndPoints[1]
                |   The y coordinate of the start point
                | oEndPoints[2]
                |   The x coordinate of the end point
                | oEndPoints[3]
                |   The y coordinate of the end point

        :return: float
        """
        return self.curve2d.GetEndPoints(o_end_points)

    def get_length_at_param(self, i_from_param, i_to_param):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLengthAtParam
                | o Func GetLengthAtParam(    double    iFromParam,
                |                             double    iToParam) As double
                | 
                | Returns the length, measured along the curve, from a given
                | parameter to a given parameter.
                |
                | Parameters:
                | iFromParam
                |   The parameter from which the length is to be measured.
                | iToParam
                |   The parameter to which the length is to be measured.
                | oLength
                |   The length between the parameters

        :return: float
        """
        return self.curve2d.GetLengthAtParam(i_from_param, i_to_param)

    def get_param_at_length(self, i_from_param, i_length):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetParamAtLength
                | o Func GetParamAtLength(    double    iFromParam,
                |                             double    iLength) As double
                | 
                | Returns the parameter at a given length, measured along the
                | curve, starting from a given parameter.  The direction of
                | measurement is always in the direction of the logicalflow of
                | the curve.  If no inherent logical flow can be assigned the
                | direction is the direction of increasing parameterization.
                |
                | Parameters:
                | iFromParam
                |   The parameter from which the length needs to be measured.
                | iLength
                |   The length of the curve to be measured from iFromParam in
                |   the logical flow direction of the curve.
                | oParam
                |   The computed parameter.

        :return: float
        """
        return self.curve2d.GetParamAtLength(i_from_param, i_length)

    def get_param_extents(self, o_params):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetParamExtents
                | o Sub GetParamExtents(    CATSafeArrayVariant    oParams)
                | 
                | Returns the parametric extents of the curve. This is the
                | parametric equivalent of the end-points.
                |
                | Parameters:
                | oParams[0]
                |   The parameter associated with the start point of the curve
                | oParams[1]
                |   The parameter associated with the end point of the curve

        """
        return self.curve2d.GetParamExtents(o_params)

    def get_point_at_param(self, i_param, o_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPointAtParam
                | o Sub GetPointAtParam(double iParam,
                |                       CATSafeArrayVariant oPoint)
                | 
                | Returns a point on the curve computed from an       input parameter.
                |
                | Parameters:
                | iParam
                |   The parameter
                | oPoint
                |   The X and Y coordinates of the computed 2D space point.


        """
        return self.curve2d.GetPointAtParam(i_param, o_point)

    def get_range_box(self, o_bound_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetRangeBox
                | o Sub GetRangeBox(    CATSafeArrayVariant    oBoundPoint)
                | 
                | Returns the range box (or bounding box) of the object       The box is
                | axially aligned within the local coordinate       system of the
                | server.
                |
                | Parameters:
                | oBoundPoint[0]
                |   The minimum x point of the box
                | oBoundPoint[1]
                |   The minimum y point of the box
                | oBoundPoint[2]
                |   The maximum x point of the box
                | oBoundPoint[3]
                |   The maximum y point of the box

        :return: tuple
        """
        return self.curve2d.GetRangeBox(o_bound_point)

    def get_tangent(self, i_param, o_tangency):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetTangent
                | o Sub GetTangent(    double    iParam,
                |                      CATSafeArrayVariant    oTangency)
                | 
                | Returns the unit-vector tangent at the parameter specified.
                |
                | Parameters:
                | iParam
                |   The parameter of the chosen point on the curve.
                | oTangency
                |   The X and Y coordinates of the unit-vector tangent at the
                |   specified parameter.

        :return: tuple
        """
        return self.curve2d.GetTangent(i_param, o_tangency)

    def is_periodic(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsPeriodic
                | o Func IsPeriodic(    ) As boolean
                | 
                | Specifies whether a curve is periodic or not.
                |
                | Parameters:
                | oPeriodic
                |   Returns true if the curve is periodic.

        :return: bool
        """
        return self.curve2d.IsPeriodic()

    def __repr__(self):
        return f'Curve2d(name="{self.name}")'

