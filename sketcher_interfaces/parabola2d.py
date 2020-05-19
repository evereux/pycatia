#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from .curve2d import Curve2D


class Parabola2D(Curve2D):
    """
        .. note::
            CAA V5 Visual Basic help

                | Class defining an parabola in 2D Space.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.parabola2d = com_object

    @property
    def focal_distance(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FocalDistance
                | o Property FocalDistance(    ) As   (Read Only)
                | 
                | Returns the focal distance of the parabola in 2D space
                |
                | Parameters:
                | oFocal
                |   The focal distance of the parabola

        :return:
        """
        return self.parabola2d.FocalDistance

    def get_axis(self, o_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAxis
                | o Sub GetAxis(        oAxis)
                | 
                | Returns the axis vector direction of the parabola in 2D space


                | Parameters:
                | oAxis[0]
                |        The X coordinate of the axis vector direction
                |        
                |  oAxis[1]
                |        The Y coordinate of the axis vector direction

        :return: tuple
        """
        return self.parabola2d.GetAxis(o_axis)

    def get_center(self, o_center):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCenter
                | o Sub GetCenter(        oCenter)
                | 
                | Returns the center of the parabola in 2D space
                |
                | Parameters:
                | oCenter[0]
                |        The X Coordinate of the center point of the parabola
                |        
                |  oCenter[1]
                |        The Y Coordinate of the center point of the parabola

        :return: tuple
        """
        return self.parabola2d.GetCenter(o_center)

    def set_data(self, i_center_x, i_center_y, i_axis_x, i_axis_y, i_focal_distance):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetData
                | o Sub SetData(iCenterX,
                |               iCenterY,
                |               iAxisX,
                |               iAxisY,
                |               iFocalDistance)
                | 
                | Modifies the characteristics of the parabola
                |
                | Parameters:
                | iCenterX
                |   The X Coordinate of the parabola center
                | iCenterY
                |   The Y Coordinate of the parabola center
                | iAxisX
                |   The X coordinate of the axis vector direction
                | iAxisY
                |   The Y coordinate of the axis vector direction
                | iFocalDistance
                |   The focal distance of the parabola

        :param i_center_x:
        :param i_center_y:
        :param i_axis_x:
        :param i_axis_y:
        :param i_focal_distance:
        """
        return self.parabola2d.SetData(i_center_x, i_center_y, i_axis_x, i_axis_y, i_focal_distance)

    def __repr__(self):
        return f'Parabola2D(name="{self.name}")'
