#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .geometry2d import Geometry2D


class Point2D(Geometry2D):
    """
        .. note::
            CAA V5 Visual Basic help

                | Class defining a point in 2D Space.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.point2d = com_object

    def get_coordinates(self, o_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCoordinates
                | o Sub GetCoordinates(    CATSafeArrayVariant    oPoint)
                | 
                | Returns the coordinates of the point
                |
                | Parameters:
                | oPoint[0]
                |               The X Coordinate of the point
                |        
                |  oPoint[1]
                |               The Y Coordinate of the point


        """
        return self.point2d.GetCoordinates(o_point)

    def set_data(self, i_x, i_y):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetData
                | o Sub SetData(    double    iX,
                |                   double    iY)
                | 
                | Modifies the coordinates of the point


                | Parameters:
                | iX
                |                      The X Coordinate of the point
                |        
                |  iY
                |                      The Y Coordinate of the point


        """
        return self.point2d.SetData(i_x, i_y)

    def __repr__(self):
        return f'Point2D(name="{self.name}")'
