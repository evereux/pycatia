#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.sketcher_interfaces.geometry_2D import Geometry2D
from pycatia.sketcher_interfaces.point_2D import Point2D
from pycatia.system_interfaces.system_service import SystemService


class Curve2D(Geometry2D):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             Curve2D
                | 
                | Class defining a curve in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.curve_2d = com_object

    @property
    def continuity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Continuity() As short (Read Only)
                | 
                |     Returns the highest level of geometric continuity the curve
                |     possesses.
                | 
                |     Parameters:
                | 
                |         oLevel
                |             The maximum geometric continuity level

        :rtype: int
        """

        return self.curve_2d.Continuity

    @property
    def end_point(self) -> Point2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndPoint() As Point2D
                | 
                |     Returns the end point of the curve. The end point is decided with respect
                |     to the logical flow imposed on the curve by the object.
                | 
                |     Parameters:
                | 
                |         oEndPoint
                |             The end point of the curve

        :rtype: Point2D
        """

        return Point2D(self.curve_2d.EndPoint)

    @end_point.setter
    def end_point(self, end_point: Point2D):
        """
        :param Point2D end_point:
        """

        self.curve_2d.EndPoint = end_point.com_object

    @property
    def period(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Period() As double (Read Only)
                | 
                |     Returns the period of a periodic curve.
                | 
                |     Parameters:
                | 
                |         oPeriod
                |             The period of the curve.

        :rtype: float
        """

        return self.curve_2d.Period

    @property
    def start_point(self) -> Point2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StartPoint() As Point2D
                | 
                |     Returns the start point of the curve. The start point is decided with
                |     respect to the logical flow imposed on the curve by the
                |     object.
                | 
                |     Parameters:
                | 
                |         oStartPoint
                |             The start point of the curve

        :rtype: Point2D
        """

        return Point2D(self.curve_2d.StartPoint)

    @start_point.setter
    def start_point(self, start_point: Point2D):
        """
        :param Point2D start_point:
        """

        self.curve_2d.StartPoint = start_point.com_object

    def get_curvature(self, i_param: float) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetCurvature(double iParam,
                | CATSafeArrayVariant oCurvature)
                | 
                |     Returns the curvature and curvature direction at the parameter
                |     specified.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The parameter of the chosen point on the curve. 
                |         oCurvature[0]
                |             The curvature at the specified parameter. 
                |         oCurvature[1;2]
                |             The unit-vector of curvature direction at the specified
                |             parameter.

        :param float i_param:
        :rtype: tuple
        """

        vba_function_name = 'get_curvature'
        vba_code = """
        Public Function get_curvature(curve2_d, i_param)
            Dim oCurvature (2)
            curve2_d.GetCurvature i_param, oCurvature
            get_curvature = oCurvature
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object, i_param])

    def get_derivatives(self, i_param: float) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetDerivatives(double iParam,
                | CATSafeArrayVariant oDerivative)
                | 
                |     Returns the first, second and third derivatives at the parameter
                |     specified.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The parameter of the chosen point on the curve. 
                |         oDerivative[0]
                |             First degree derivative. 
                |         oDerivative[1]
                |             Second degree derivative. 
                |         oDerivative[2]
                |             Third degree derivative.

        :param float i_param:
        :rtype: tuple
        """

        vba_function_name = 'get_derivatives'
        vba_code = """
        Public Function get_derivatives(curve2_d, i_param)
            Dim oDerivative(2)
            curve2_d.GetDerivatives iParam, oDerivative
            get_derivatives = oDerivative
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object, i_param])

    def get_end_points(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetEndPoints(CATSafeArrayVariant oEndPoints)
                | 
                |     Returns the end-points of the curve. The start point and the end point are
                |     decided with respect to the logical flow imposed on the curve by the
                |     object.
                | 
                |     Parameters:
                | 
                |         oEndPoints[0]
                |             The x coordinate of the start point 
                |         oEndPoints[1]
                |             The y coordinate of the start point 
                |         oEndPoints[2]
                |             The x coordinate of the end point 
                |         oEndPoints[3]
                |             The y coordinate of the end point

        :rtype: tuple
        """

        vba_function_name = 'get_end_points'
        vba_code = """
        Public Function get_end_points(curve2_d)
            Dim oEndPoints (3)
            curve2_d.GetEndPoints oEndPoints
            get_end_points = oEndPoints
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_length_at_param(self, i_from_param: float, i_to_param: float) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLengthAtParam(double iFromParam,
                | double iToParam) As double
                | 
                |     Returns the length, measured along the curve, from a given parameter to a
                |     given parameter.
                | 
                |     Parameters:
                | 
                |         iFromParam
                |             The parameter from which the length is to be measured.
                |             
                |         iToParam
                |             The parameter to which the length is to be measured.
                |             
                |         oLength
                |             The length between the parameters

        :param float i_from_param:
        :param float i_to_param:
        :rtype: float
        """
        return self.curve_2d.GetLengthAtParam(i_from_param, i_to_param)

    def get_param_at_length(self, i_from_param: float, i_length: float) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetParamAtLength(double iFromParam,
                | double iLength) As double
                | 
                |     Returns the parameter at a given length, measured along the curve, starting
                |     from a given parameter. The direction of measurement is always in the direction
                |     of the logical flow of the curve. If no inherent logical flow can be assigned
                |     the direction is the direction of increasing
                |     parameterization.
                | 
                |     Parameters:
                | 
                |         iFromParam
                |             The parameter from which the length needs to be measured.
                |             
                |         iLength
                |             The length of the curve to be measured from iFromParam in the
                |             logical flow direction of the curve. 
                |         oParam
                |             The computed parameter.

        :param float i_from_param:
        :param float i_length:
        :rtype: float
        """
        return self.curve_2d.GetParamAtLength(i_from_param, i_length)

    def get_param_extents(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetParamExtents(CATSafeArrayVariant oParams)
                | 
                |     Returns the parametric extents of the curve. This is the parametric
                |     equivalent of the end-points.
                | 
                |     Parameters:
                | 
                |         oParams[0]
                |             The parameter associated with the start point of the curve
                |             
                |         oParams[1]
                |             The parameter associated with the end point of the
                |             curve

        :rtype: tuple
        """

        vba_function_name = 'get_param_extents'
        vba_code = """
        Public Function get_param_extents(curve2_d)
            Dim oParams(1)
            curve2_d.GetParamExtents oParams
            get_param_extents = oParams
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_point_at_param(self, i_param: float) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetPointAtParam(double iParam,
                | CATSafeArrayVariant oPoint)
                | 
                |     Returns a point on the curve computed from an input
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The parameter 
                |         oPoint
                |             The X and Y coordinates of the computed 2D space
                |             point.

        :param float i_param:
        :rtype: tuple
        """

        vba_function_name = 'get_point_at_param'
        vba_code = """
        Public Function get_point_at_param(curve2_d, i_param)
            Dim oPoint (1)
            curve2_d.GetPointAtParam i_param, oPoint
            get_point_at_param = oPoint
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object, i_param])

    def get_range_box(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetRangeBox(CATSafeArrayVariant oBoundPoint)
                | 
                |     Returns the range box (or bounding box) of the object
                |     The box is axially aligned within the local coordinate system of the
                |     server.
                | 
                |     Parameters:
                | 
                |         oBoundPoint[0]
                |             The minimum x point of the box 
                |         oBoundPoint[1]
                |             The minimum y point of the box 
                |         oBoundPoint[2]
                |             The maximum x point of the box 
                |         oBoundPoint[3]
                |             The maximum y point of the box

        :rtype: tuple
        """

        vba_function_name = 'get_range_box'
        vba_code = """
        Public Function get_range_box(curve2_d)
            Dim oBoundPoint(3)
            curve2_d.GetRangeBox oBoundPoint
            get_range_box = oBoundPoint
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_tangent(self, i_param: float) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetTangent(double iParam,
                | CATSafeArrayVariant oTangency)
                | 
                |     Returns the unit-vector tangent at the parameter
                |     specified.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The parameter of the chosen point on the curve. 
                |         oTangency
                |             The X and Y coordinates of the unit-vector tangent at the specified
                |             parameter.

        :i_param: float
        :rtype: None
        """

        vba_function_name = 'get_tangent'
        vba_code = """
        Public Function get_tangent(curve2_d, i_param)
            Dim oTangency(1)
            curve2_d.GetTangent i_param, oTangency
            get_tangent = oTangency
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object, i_param])

    def is_periodic(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func IsPeriodic() As boolean
                | 
                |     Specifies whether a curve is periodic or not.
                | 
                |     Parameters:
                | 
                |         oPeriodic
                |             Returns true if the curve is periodic.

        :rtype: bool
        """
        return self.curve_2d.IsPeriodic()

    def __repr__(self):
        return f'Curve2D(name="{self.name}")'
