#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.sketcher_interfaces.point_2D import Point2D
from pycatia.system_interfaces.system_service import SystemService


class ControlPoint2D(Point2D):
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
                |                             SketcherInterfaces.Point2D
                |                                 ControlPoint2D
                | 
                | Class defining a spline control point in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.control_point_2d = com_object

    @property
    def curvature(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Curvature() As double
                | 
                |     Returns the curvature properties of the spline control
                |     point
                | 
                |     Parameters:
                | 
                |         oCurvature
                |             The curvature of the tangent determined at the control
                |             point

        :rtype: float
        """

        return self.control_point_2d.Curvature

    @curvature.setter
    def curvature(self, value: float):
        """
        :param float value:
        """

        self.control_point_2d.Curvature = value

    def get_tangent(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetTangent(CATSafeArrayVariant oTangent)
                | 
                |     Returns the tangent properties of the spline control point
                | 
                |     Parameters:
                | 
                |         oTangent[0]
                |             The X Coordinate of the tangent determined at the control point
                |             
                |         oTangent[1]
                |             The Y Coordinate of the tangent determined at the control
                |             point

        :rtype: tuple
        """

        vba_function_name = 'get_tangent'
        vba_code = """
        Public Function get_tangent(control_point2_d)
            Dim oTangent (1)
            control_point2_d.GetTangent oTangent
            get_tangent = oTangent
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tangent(self, i_tangent_x: float, i_tangent_y: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTangent(double iTangentX,
                | double iTangentY)
                | 
                |     Imposes the tangent properties of the spline control point
                | 
                |     Parameters:
                | 
                |         iTangentX
                |             The X Coordinate of the tangent determined at the control point
                |             
                |         iTangentY
                |             The Y Coordinate of the tangent determined at the control
                |             point

        :param float i_tangent_x:
        :param float i_tangent_y:
        :rtype: None
        """
        return self.control_point_2d.SetTangent(i_tangent_x, i_tangent_y)

    def unset_curvature(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub UnsetCurvature()
                | 
                |     Unsets the curvature properties of the spline control point

        :rtype: None
        """
        return self.control_point_2d.UnsetCurvature()

    def unset_tangent(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub UnsetTangent()
                | 
                |     Unsets the tangent properties of the spline control point

        :rtype: None
        """
        return self.control_point_2d.UnsetTangent()

    def __repr__(self):
        return f'ControlPoint2D(name="{self.name}")'
