#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.sketcher_interfaces.geometry_2D import Geometry2D
from pycatia.system_interfaces.system_service import SystemService


class Point2D(Geometry2D):
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
                |                             Point2D
                | 
                | Class defining a point in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.point_2d = com_object

    def get_coordinates(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetCoordinates(CATSafeArrayVariant oPoint)
                | 
                |     Returns the coordinates of the point
                | 
                |     Parameters:
                | 
                |         oPoint[0]
                |             The X Coordinate of the point 
                |         oPoint[1]
                |             The Y Coordinate of the point

        :rtype: tuple
        """

        vba_function_name = 'get_coordinates'
        vba_code = """
        Public Function get_coordinates(point2_d)
            Dim oPoint(1)
            point2_d.GetCoordinates oPoint
            get_coordinates = oPoint
        End Function
        """

        system_service = self.application.system_service
        return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_data(self, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetData(double iX,
                | double iY)
                | 
                |     Modifies the coordinates of the point
                | 
                |     Parameters:
                | 
                |         iX
                |             The X Coordinate of the point 
                |         iY
                |             The Y Coordinate of the point

        :param float i_x:
        :param float i_y:
        :rtype: None
        """
        return self.point_2d.SetData(i_x, i_y)

    def __repr__(self):
        return f'Point2D(name="{self.name}")'
