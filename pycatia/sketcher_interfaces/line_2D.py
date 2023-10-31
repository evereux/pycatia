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


class Line2D(Curve2D):
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
                |                                 Line2D
                | 
                | Class defining a line in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.line_2d = com_object

    def get_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetDirection(CATSafeArrayVariant oDirection)
                | 
                |     Returns the unit-vector pointing in the direction of the
                |     line.
                | 
                |     Parameters:
                | 
                |         oDirection[0]
                |             The X Coordinate of the unit vector pointing in the direction of
                |             the line 
                |         oDirection[1]
                |             The Y Coordinate of the unit vector pointing in the direction of
                |             the line

        :rtype: tuple
        """

        vba_function_name = 'get_direction'
        vba_code = """
        Public Function get_direction(line2_d)
            Dim oDirection(2)
            line2_d.GetDirection oDirection
            get_direction = oDirection
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_origin(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetOrigin(CATSafeArrayVariant oOrigin)
                | 
                |     Returns a point lying on the line
                | 
                |     Parameters:
                | 
                |         oPoint[0]
                |             The X Coordinate of a point lying on the line 
                |         oPoint[1]
                |             The Y Coordinate of a point lying on the line

        :rtype: tuple
        """

        vba_function_name = 'get_origin'
        vba_code = """
        Public Function get_origin(line2_d)
            Dim oOrigin(1)
            line2_d.GetOrigin oOrigin
            get_origin = oOrigin
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_data(self, i_x: float, i_y: float, i_x_direction: float, i_y_direction: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetData(double iX,
                | double iY,
                | double iXDirection,
                | double iYDirection)
                | 
                |     Modifies the caracteristics of the infinite line
                | 
                |     Parameters:
                | 
                |         iX
                |             The X Coordinate of a point lying on the line 
                |         iY
                |             The Y Coordinate of a point lying on the line 
                |         iXDirection
                |             The X Coordinate of the unit vector pointing in the direction of
                |             the line 
                |         iYDirection
                |             The Y Coordinate of the unit vector pointing in the direction of
                |             the line

        :param float i_x:
        :param float i_y:
        :param float i_x_direction:
        :param float i_y_direction:
        :rtype: None
        """
        return self.line_2d.SetData(i_x, i_y, i_x_direction, i_y_direction)

    def __repr__(self):
        return f'Line2D(name="{self.name}")'
