#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.sketcher_interfaces.geometry_2D import Geometry2D
from pycatia.sketcher_interfaces.point_2D import Point2D


class Curve2D(Geometry2D):
    """
        .. note::
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
        self.curve2_d = com_object

    @property
    def continuity(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Continuity() As short (Read Only)
                | 
                |     Returns the highest level of geometric continuity the curve
                |     possesses.
                | 
                |     Parameters:
                | 
                |         oLevel
                |             The maximum geometric continuity level

        :return: enum
        """

        return self.curve2_d.Continuity

    @property
    def end_point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property EndPoint() As Point2D
                | 
                |     Returns the end point of the curve. The end point is decided with respect
                |     to the logical flow imposed on the curve by the object.
                | 
                |     Parameters:
                | 
                |         oEndPoint
                |             The end point of the curve

        :return: Point2D
        """

        return Point2D(self.curve2_d.EndPoint)

    @end_point.setter
    def end_point(self, point_2D):
        """
        :param Point2D point_2D:
        """

        self.curve2_d.EndPoint = point_2D.com_object

    @property
    def period(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Period() As double (Read Only)
                | 
                |     Returns the period of a periodic curve.
                | 
                |     Parameters:
                | 
                |         oPeriod
                |             The period of the curve.

        :return: float
        """

        return self.curve2_d.Period

    @property
    def start_point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
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

        :return: Point2D
        """

        return Point2D(self.curve2_d.StartPoint)

    @start_point.setter
    def start_point(self, point_2D):
        """
        :param Point2D point_2D:
        """

        self.curve2_d.StartPoint = point_2D.com_object

    def get_curvature(self, i_param, o_curvature):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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
        :param tuple o_curvature:
        :return: None
        """
        return self.curve2_d.GetCurvature(i_param, o_curvature)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_curvature'
        # # vba_code = """
        # # Public Function get_curvature(curve2_d)
        # #     Dim iParam (2)
        # #     curve2_d.GetCurvature iParam
        # #     get_curvature = iParam
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_derivatives(self, i_param, o_derivative):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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
        :param tuple o_derivative:
        :return: None
        """
        return self.curve2_d.GetDerivatives(i_param, o_derivative)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_derivatives'
        # # vba_code = """
        # # Public Function get_derivatives(curve2_d)
        # #     Dim iParam (2)
        # #     curve2_d.GetDerivatives iParam
        # #     get_derivatives = iParam
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_end_points(self, o_end_points):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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

        :param tuple o_end_points:
        :return: None
        """
        return self.curve2_d.GetEndPoints(o_end_points)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_end_points'
        # # vba_code = """
        # # Public Function get_end_points(curve2_d)
        # #     Dim oEndPoints (2)
        # #     curve2_d.GetEndPoints oEndPoints
        # #     get_end_points = oEndPoints
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_length_at_param(self, i_from_param, i_to_param):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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
        :return: float
        """
        return self.curve2_d.GetLengthAtParam(i_from_param, i_to_param)

    def get_param_at_length(self, i_from_param, i_length):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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
        :return: float
        """
        return self.curve2_d.GetParamAtLength(i_from_param, i_length)

    def get_param_extents(self, o_params):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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

        :param tuple o_params:
        :return: None
        """
        return self.curve2_d.GetParamExtents(o_params)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_param_extents'
        # # vba_code = """
        # # Public Function get_param_extents(curve2_d)
        # #     Dim oParams (2)
        # #     curve2_d.GetParamExtents oParams
        # #     get_param_extents = oParams
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_point_at_param(self, i_param, o_point):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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
        :param tuple o_point:
        :return: None
        """
        return self.curve2_d.GetPointAtParam(i_param, o_point)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_point_at_param'
        # # vba_code = """
        # # Public Function get_point_at_param(curve2_d)
        # #     Dim iParam (2)
        # #     curve2_d.GetPointAtParam iParam
        # #     get_point_at_param = iParam
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_range_box(self, o_bound_point):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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

        :param tuple o_bound_point:
        :return: None
        """
        return self.curve2_d.GetRangeBox(o_bound_point)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_range_box'
        # # vba_code = """
        # # Public Function get_range_box(curve2_d)
        # #     Dim oBoundPoint (2)
        # #     curve2_d.GetRangeBox oBoundPoint
        # #     get_range_box = oBoundPoint
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_tangent(self, i_param, o_tangency):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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

        :param float i_param:
        :param tuple o_tangency:
        :return: None
        """
        return self.curve2_d.GetTangent(i_param, o_tangency)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_tangent'
        # # vba_code = """
        # # Public Function get_tangent(curve2_d)
        # #     Dim iParam (2)
        # #     curve2_d.GetTangent iParam
        # #     get_tangent = iParam
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def is_periodic(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func IsPeriodic() As boolean
                | 
                |     Specifies whether a curve is periodic or not.
                | 
                |     Parameters:
                | 
                |         oPeriodic
                |             Returns true if the curve is periodic.

        :return: bool
        """
        return self.curve2_d.IsPeriodic()

    def __repr__(self):
        return f'Curve2D(name="{self.name}")'
