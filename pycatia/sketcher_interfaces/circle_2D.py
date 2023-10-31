#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.sketcher_interfaces.curve_2D import Curve2D
from pycatia.sketcher_interfaces.point_2D import Point2D
from pycatia.system_interfaces.system_service import SystemService


class Circle2D(Curve2D):
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
                |                             SketcherInterfaces.Curve2D
                |                                 Circle2D
                | 
                | Class defining a circle in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.circle_2d = com_object

    @property
    def center_point(self) -> Point2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CenterPoint() As Point2D
                | 
                |     Returns the center point of the circle.
                | 
                |     Parameters:
                | 
                |         oCenterPoint
                |             The center point of the circle

        :rtype: Point2D
        """

        return Point2D(self.circle_2d.CenterPoint)

    @center_point.setter
    def center_point(self, value: Point2D):
        """
        :param Point2D value:
        """

        self.circle_2d.CenterPoint = value

    @property
    def radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Radius() As double (Read Only)
                | 
                |     Returns the radius of the circle
                | 
                |     Parameters:
                | 
                |         oRadius
                |             The radius of the circle

        :rtype: float
        """

        return self.circle_2d.Radius

    def get_center(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetCenter(CATSafeArrayVariant oData)
                | 
                |     Returns the center of the circle
                | 
                |     Parameters:
                | 
                |         oData[0]
                |             The X Coordinate of the circle center point 
                |         oData[1]
                |             The Y Coordinate of the circle center point 
                |         Example:
                |             The following example reads the coordinates of the
                |             center
                |             of the circle myCircle: double center(1) myCircle.GetCenter
                |             center

        :rtype: tuple
        """

        vba_function_name = 'get_center'
        vba_code = """
        Public Function get_center(circle2_d)
            Dim oData (2)
            circle2_d.GetCenter oData
            get_center = oData
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_data(self, i_center_x: float, i_center_y: float, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetData(double iCenterX,
                | double iCenterY,
                | double iRadius)
                | 
                |     Modifies the caracteristics of the circle
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X Coordinate of the circle center 
                |         iCenterY
                |             The Y Coordinate of the circle center 
                |         iRadius
                |             The radius of the circle

        :param float i_center_x:
        :param float i_center_y:
        :param float i_radius:
        :rtype: None
        """
        return self.circle_2d.SetData(i_center_x, i_center_y, i_radius)

    def __repr__(self):
        return f'Circle2D(name="{self.name}")'
