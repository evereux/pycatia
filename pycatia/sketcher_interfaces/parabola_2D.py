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


class Parabola2D(Curve2D):
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
                |                                 Parabola2D
                | 
                | Class defining an parabola in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.parabola_2d = com_object

    @property
    def focal_distance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FocalDistance() As double (Read Only)
                | 
                |     Returns the focal distance of the parabola in 2D space
                | 
                |     Parameters:
                | 
                |         oFocal
                |             The focal distance of the parabola

        :rtype: float
        """

        return self.parabola_2d.FocalDistance

    def get_axis(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetAxis(CATSafeArrayVariant oAxis)
                | 
                |     Returns the axis vector direction of the parabola in 2D
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
        Public Function get_axis(parabola2_d)
            Dim oAxis (1)
            parabola2_d.GetAxis oAxis
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
                |     Returns the center of the parabola in 2D space
                | 
                |     Parameters:
                | 
                |         oCenter[0]
                |             The X Coordinate of the center point of the parabola
                |             
                |         oCenter[1]
                |             The Y Coordinate of the center point of the
                |             parabola

        :rtype: tuple
        """

        vba_function_name = 'get_center'
        vba_code = """
        Public Function get_center(parabola2_d)
            Dim oCenter(1)
            parabola2_d.GetCenter oCenter
            get_center = oCenter
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_data(self, i_center_x: float, i_center_y: float, i_axis_x: float, i_axis_y: float,
                 i_focal_distance: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetData(double iCenterX,
                | double iCenterY,
                | double iAxisX,
                | double iAxisY,
                | double iFocalDistance)
                | 
                |     Modifies the caracteristics of the parabola
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X Coordinate of the parabola center 
                |         iCenterY
                |             The Y Coordinate of the parabola center 
                |         iAxisX
                |             The X coordinate of the axis vector direction 
                |         iAxisY
                |             The Y coordinate of the axis vector direction 
                |         iFocalDistance
                |             The focal distance of the parabola

        :param float i_center_x:
        :param float i_center_y:
        :param float i_axis_x:
        :param float i_axis_y:
        :param float i_focal_distance:
        :rtype: None
        """
        return self.parabola_2d.SetData(i_center_x, i_center_y, i_axis_x, i_axis_y, i_focal_distance)

    def __repr__(self):
        return f'Parabola2D(name="{self.name}")'
