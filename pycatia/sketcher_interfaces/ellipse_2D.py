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


class Ellipse2D(Curve2D):
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
                |                                 Ellipse2D
                | 
                | Class defining an ellipse in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ellipse_2d = com_object

    @property
    def center_point(self) -> Point2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CenterPoint() As Point2D
                | 
                |     Returns the center point of the ellipse.
                | 
                |     Parameters:
                | 
                |         iCenterPoint
                |             The center point of the ellipse

        :rtype: Point2D
        """

        return Point2D(self.ellipse_2d.CenterPoint)

    @center_point.setter
    def center_point(self, value: Point2D):
        """
        :param Point2D value:
        """

        self.ellipse_2d.CenterPoint = value

    @property
    def major_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MajorRadius() As double (Read Only)
                | 
                |     Returns the radius of the ellipse major axis
                | 
                |     Parameters:
                | 
                |         oMajorRadius
                |             The radius of the major axis

        :rtype: float
        """

        return self.ellipse_2d.MajorRadius

    @property
    def minor_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MinorRadius() As double (Read Only)
                | 
                |     Returns the radius of the ellipse minor axis
                | 
                |     Parameters:
                | 
                |         oMinorRadius
                |             The radius of the minor axis

        :rtype: float
        """

        return self.ellipse_2d.MinorRadius

    def get_center(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetCenter(CATSafeArrayVariant oCenter)
                | 
                |     Returns the center of the ellipse in 2D space
                | 
                |     Parameters:
                | 
                |         oCenter[0]
                |             The X Coordinate of the center point of the ellipse
                |             
                |         oCenter[1]
                |             The Y Coordinate of the center point of the
                |             ellipse

        :rtype: tuple
        """

        vba_function_name = 'get_center'
        vba_code = """
        Public Function get_center(ellipse2_d)
            Dim oCenter (1)
            ellipse2_d.GetCenter oCenter
            get_center = oCenter
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_major_axis(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetMajorAxis(CATSafeArrayVariant oMajorAxis)
                | 
                |     Returns the unit vector of the major axis of the ellipse in 2D
                |     space
                | 
                |     Parameters:
                | 
                |         oMajorAxis[0]
                |             The length of the major axis 
                |         oMajorAxis[1]
                |             The length of the major axis

        :rtype: tuple
        """

        vba_function_name = 'get_major_axis'
        vba_code = """
        Public Function get_major_axis(ellipse2_d)
            Dim oMajorAxis (1)
            ellipse2_d.GetMajorAxis oMajorAxis
            get_major_axis = oMajorAxis
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_minor_axis(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetMinorAxis(CATSafeArrayVariant oMajorAxis)
                | 
                |     Returns the unit vector of the minor axis of the ellipse in 2D
                |     space
                | 
                |     Parameters:
                | 
                |         oMinorAxis[0]
                |             The length of the major axis 
                |         oMinorAxis[1]
                |             The length of the major axis

        :rtype: tuple
        """

        vba_function_name = 'get_minor_axis'
        vba_code = """
        Public Function get_minor_axis(ellipse2_d)
            Dim oMajorAxis (1)
            ellipse2_d.GetMinorAxis oMajorAxis
            get_minor_axis = oMajorAxis
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_data(self,
                 i_center_x: float,
                 i_center_y: float,
                 i_major_x: float,
                 i_major_y: float,
                 i_major_radius: float,
                 i_minor_radius: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetData(double iCenterX,
                | double iCenterY,
                | double iMajorX,
                | double iMajorY,
                | double iMajorRadius,
                | double iMinorRadius)
                | 
                |     Modifies the caracteristics of the ellipse
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X Coordinate of the ellipse center 
                |         iCenterY
                |             The Y Coordinate of the ellipse center 
                |         iMajorX
                |             The X coordinate of the Major axis direction 
                |         iMajorY
                |             The Y coordinate of the Major axis direction 
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
        :rtype: None
        """
        return self.ellipse_2d.SetData(i_center_x, i_center_y, i_major_x, i_major_y, i_major_radius, i_minor_radius)

    def __repr__(self):
        return f'Ellipse2D(name="{self.name}")'
