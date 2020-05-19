#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .curve2d import Curve2D


class Line2D(Curve2D):
    """
        .. note::
            CAA V5 Visual Basic help

                | Class defining a line in 2D Space.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.line2d = com_object

    def get_direction(self, o_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDirection
                | o Sub GetDirection(    CATSafeArrayVariant    oDirection)
                | 
                | Returns the unit-vector pointing in the direction of the       line.
                |
                | Parameters:
                | oDirection[0]
                |   The X Coordinate of the unit vector pointing in the
                |   direction of the line
                |        
                | oDirection[1]
                |   The Y Coordinate of the unit vector pointing in the direction of the line

        """
        return self.line2d.GetDirection(o_direction)

    def get_origin(self, o_origin):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOrigin
                | o Sub GetOrigin(    CATSafeArrayVariant    oOrigin)
                | 
                | Returns a point lying on the line
                |
                | Parameters:
                | oPoint[0]
                |   The X Coordinate of a point lying on the line
                | oPoint[1]
                |   The Y Coordinate of a point lying on the line

        :return: tuple
        """
        return self.line2d.GetOrigin(o_origin)

    def set_data(self, i_x, i_y, i_x_direction, i_y_direction):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetData
                | o Sub SetData( double iX,
                |                double iY,
                |                double iXDirection,
                |                double iYDirection)
                | 
                | Modifies the characteristics of the infinite line
                |
                | Parameters:
                | iX
                |   The X Coordinate of a point lying on the line
                | iY
                |   The Y Coordinate of a point lying on the line
                | iXDirection
                |   The X Coordinate of the unit vector pointing in the direction of the line
                | iYDirection
                |   The Y Coordinate of the unit vector pointing in the direction of the line

        """
        return self.line2d.SetData(i_x, i_y, i_x_direction, i_y_direction)

    def __repr__(self):
        return f'Line2D(name="{self.name}")'
