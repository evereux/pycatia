#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .curve2d import Curve2D
from .point2d import Point2D


class Ellipse2D(Curve2D):
    """
        .. note::
            CAA V5 Visual Basic help

                | Class defining an ellipse in 2D Space.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ellipse2d = com_object

    @property
    def center_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CenterPoint
                | o Property CenterPoint(    ) As Point2D
                | 
                | Returns the center point of the ellipse.
                |
                | Parameters:
                | iCenterPoint
                |   The center point of the ellipse

        :return: Point2D()
        """
        return Point2D(self.ellipse2d.CenterPoint)

    @property
    def major_radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MajorRadius
                | o Property MajorRadius(    ) As double
                | 
                | Returns the radius of the ellipse major axis
                |
                | Parameters:
                | oMajorRadius
                |   The radius of the major axis

        :return: float
        """
        return self.ellipse2d.MajorRadius

    @property
    def minor_radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MinorRadius
                | o Property MinorRadius(    ) As double
                | 
                | Returns the radius of the ellipse minor axis
                |
                | Parameters:
                | oMinorRadius
                |   The radius of the minor axis

        :return: float
        """
        return self.ellipse2d.MinorRadius

    def get_center(self, o_center):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCenter
                | o Sub GetCenter(    CATSafeArrayVariant    oCenter)
                | 
                | Returns the center of the ellipse in 2D space
                |
                | Parameters:
                | oCenter[0]
                |   The X Coordinate of the center point of the ellipse
                | oCenter[1]
                |   The Y Coordinate of the center point of the ellipse

        :return: float
        """
        return self.ellipse2d.GetCenter(o_center)

    def get_major_axis(self, o_major_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetMajorAxis
                | o Sub GetMajorAxis(    CATSafeArrayVariant    oMajorAxis)
                | 
                | Returns the unit vector of the major axis of the ellipse in 2D
                | space
                |
                | Parameters:
                | oMajorAxis[0]
                |   The length of the major axis
                | oMajorAxis[1]
                |   The length of the major axis

        :return: tuple
        """
        return self.ellipse2d.GetMajorAxis(o_major_axis)

    def get_minor_axis(self, o_major_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetMinorAxis
                | o Sub GetMinorAxis(    CATSafeArrayVariant    oMajorAxis)
                | 
                | Returns the unit vector of the minor axis of the ellipse in 2D
                | space
                |
                | Parameters:
                | oMinorAxis[0]
                |   The length of the major axis
                | oMinorAxis[1]
                |   The length of the major axis

        :return: tuple
        """
        return self.ellipse2d.GetMinorAxis(o_major_axis)

    def set_data(self, i_center_x, i_center_y, i_major_x, i_major_y, i_major_radius, i_minor_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetData
                | o Sub SetData(double iCenterX,
                |               double iCenterY,
                |               double iMajorX,
                |               double iMajorY,
                |               double iMajorRadius,
                |               double iMinorRadius)
                | 
                | Modifies the characteristics of the ellipse
                |
                | Parameters:
                | iCenterX
                |   The X Coordinate of the ellipse center
                | iCenterY
                |   The Y Coordinate of the ellipse center
                | iMajorX
                |   The X coordinate of the Major axis direction
                | iMajorY
                |   The Y coordinate of the Major axis direction
                | iMajorRadius
                |   The length of the major axis
                | iMinorRadius
                |   The length of the minor axis

        :param float i_center_x:
        :param float i_center_y:
        :param float i_major_x:
        :param float i_major_y:
        :param float i_major_radius:
        :param float i_minor_radius:
        """
        self.ellipse2d.SetData(i_center_x, i_center_y, i_major_x, i_major_y, i_major_radius, i_minor_radius)

    def __repr__(self):
        return f'Ellipse2D({self.name})'
