#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .curve2d import Curve2D
from .point2d import Point2D


class Circle2D(Curve2D):
    """
        .. note::
            CAA V5 Visual Basic help

                | Class defining a circle in 2D Space.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.circle2d = com_object

    @property
    def center_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CenterPoint
                | o Property CenterPoint(    ) As Point2D
                | 
                | Returns the center point of the circle.
                |
                | Parameters:
                | oCenterPoint
                |   The center point of the circle


        """
        return Point2D(self.circle2d.CenterPoint)

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Radius
                | o Property Radius(    ) As double
                | 
                | Returns the radius of the circle
                |
                | Parameters:
                | oRadius
                |   The radius of the circle

        :return: float
        """
        return self.circle2d.Radius

    def get_center(self, o_data):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCenter
                | o Sub GetCenter(    CATSafeArrayVariant    oData)
                | 
                | Returns the center of the circle
                |
                | Parameters:
                | oData[0]
                |   The X Coordinate of the circle center point
                | oData[1]
                |   The Y Coordinate of the circle center point
                |
                | Examples:
                | 
                | The following example reads the coordinates of the center
                | of the circle myCircle:
                | double center(1)
                | myCircle.GetCenter center

        :return: tuple
        """
        return self.circle2d.GetCenter(o_data)

    def set_data(self, i_center_x, i_center_y, i_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetData
                | o Sub SetData(    double    iCenterX,
                |                   double    iCenterY,
                |                   double    iRadius)
                | 
                | Modifies the characteristics of the circle
                |
                | Parameters:
                | iCenterX
                |   The X Coordinate of the circle center
                | iCenterY
                |   The Y Coordinate of the circle center
                | iRadius
                |   The radius of the circle

        :param float i_center_x:
        :param float i_center_y:
        :param float i_radius:
        """
        return self.circle2d.SetData(i_center_x, i_center_y, i_radius)

    def __repr__(self):
        return 'Circle2D()'
