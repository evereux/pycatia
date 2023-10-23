#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.sketcher_interfaces.curve_2D import Curve2D
from pycatia.system_interfaces.system_service import SystemService


class Hyperbola2D(Curve2D):
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
                |                                 Hyperbola2D
                | 
                | Class defining an hyperbola in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hyperbola_2d = com_object

    @property
    def imaginary_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ImaginaryRadius() As double (Read Only)
                | 
                |     Returns the minor radius of the hyperbola in 2D space
                | 
                |     Parameters:
                | 
                |         oMinorRadius
                |             The minor radius of the hyperbola

        :rtype: float
        """

        return self.hyperbola_2d.ImaginaryRadius

    @property
    def radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Radius() As double (Read Only)
                | 
                |     Returns the major radius of the hyperbola in 2D space
                | 
                |     Parameters:
                | 
                |         oMajorRadius
                |             The major radius of the hyperbola

        :rtype: float
        """

        return self.hyperbola_2d.Radius

    def get_axis(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetAxis(CATSafeArrayVariant oAxis)
                | 
                |     Returns the axis vector direction of the hyperbola in 2D
                |     space
                | 
                |     Parameters:
                | 
                |         oAxis[0]
                |             The X coordinate of the axis vector direction 
                |         oAxis[1]
                |             The Y coordinate of the axis vector direction

        :rtype: tuple
        """

        vba_function_name = 'get_axis'
        vba_code = """
        Public Function get_axis(hyperbola_2d)
            Dim oAxis (1)
            hyperbola_2d.GetAxis oAxis
            get_axis = oAxis
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_center(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetCenter(CATSafeArrayVariant oCenter)
                | 
                |     Returns the center point of the hyperbola in 2D space
                | 
                |     Parameters:
                | 
                |         oCenter[0]
                |             The X Coordinate of the center point of the hyperbola
                |             
                |         oCenter[1]
                |             The Y Coordinate of the center point of the
                |             hyperbola

        :rtype: tuple
        """

        vba_function_name = 'get_center'
        vba_code = """
        Public Function get_center(hyperbola_2d)
            Dim oCenter (1)
            hyperbola_2d.GetCenter oCenter
            get_center = oCenter
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_data(self, i_center_x: float, i_center_y: float, i_axis_x: float, i_axis_y: float, i_major_radius: float,
                 i_minor_radius: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetData(double iCenterX,
                | double iCenterY,
                | double iAxisX,
                | double iAxisY,
                | double iMajorRadius,
                | double iMinorRadius)
                | 
                |     Modifies the caracteristics of the hyperbola
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X Coordinate of the hyperbola center 
                |         iCenterY
                |             The Y Coordinate of the hyperbola center 
                |         iAxisX
                |             The X coordinate of the axis vector direction 
                |         iAxisY
                |             The Y coordinate of the axis vector direction 
                |         iMajorRadius
                |             The length of the major radius 
                |         iMinorRadius
                |             The length of the minor radius

        :param float i_center_x:
        :param float i_center_y:
        :param float i_axis_x:
        :param float i_axis_y:
        :param float i_major_radius:
        :param float i_minor_radius:
        :rtype: None
        """
        return self.hyperbola_2d.SetData(i_center_x, i_center_y, i_axis_x, i_axis_y, i_major_radius, i_minor_radius)

    def __repr__(self):
        return f'Hyperbola2D(name="{self.name}")'
