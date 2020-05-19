#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25

from .curve2d import Curve2D


class Hyperbola2D(Curve2D):
    """
        .. note::
            CAA V5 Visual Basic help

                | Class defining an hyperbola in 2D Space.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hyperbola2d = com_object

    @property
    def imaginary_radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ImaginaryRadius
                | o Property ImaginaryRadius(    ) As   (Read Only)
                | 
                | Returns the minor radius of the hyperbola in 2D space


                | Parameters:
                | oMinorRadius
                |        The minor radius of the hyperbola

        :return: float
        """
        return self.hyperbola2d.ImaginaryRadius

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Radius
                | o Property Radius(    ) As   (Read Only)
                | 
                | Returns the major radius of the hyperbola in 2D space


                | Parameters:
                | oMajorRadius
                |        The major radius of the hyperbola

        :return: float
        """
        return self.hyperbola2d.Radius

    def get_axis(self, o_axis):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAxis
                | o Sub GetAxis(        oAxis)
                | 
                | Returns the axis vector direction of the hyperbola in 2D space


                | Parameters:
                | oAxis[0]
                |        The X coordinate of the axis vector direction
                |        
                |  oAxis[1]
                |        The Y coordinate of the axis vector direction

        :return: float
        """
        return self.hyperbola2d.GetAxis(o_axis)

    def get_center(self, o_center):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetCenter
                | o Sub GetCenter(        oCenter)
                | 
                | Returns the center point of the hyperbola in 2D space


                | Parameters:
                | oCenter[0]
                |        The X Coordinate of the center point of the hyperbola
                |        
                |  oCenter[1]
                |        The Y Coordinate of the center point of the hyperbola

        :return: tuple
        """
        return self.hyperbola2d.GetCenter(o_center)

    def set_data(self, i_center_x, i_center_y, i_axis_x, i_axis_y, i_major_radius, i_minor_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetData
                | o Sub SetData(        iCenterX,
                |                       iCenterY,
                |                       iAxisX,
                |                       iAxisY,
                |                       iMajorRadius,
                |                       iMinorRadius)
                | 
                | Modifies the caracteristics of the hyperbola


                | Parameters:
                | iCenterX
                |        The X Coordinate of the hyperbola center
                |        
                |  iCenterY
                |        The Y Coordinate of the hyperbola center
                |        
                |  iAxisX
                |        The X coordinate of the axis vector direction
                |        
                |  iAxisY
                |        The Y coordinate of the axis vector direction
                |        
                |  iMajorRadius
                |        The length of the major radius
                |        
                |  iMinorRadius
                |        The length of the minor radius

        :param float i_center_x:
        :param float i_center_y:
        :param float i_axis_x:
        :param float i_axis_y:
        :param float i_major_radius:
        :param float i_minor_radius:
        """
        self.hyperbola2d.SetData(i_center_x, i_center_y, i_axis_x, i_axis_y, i_major_radius, i_minor_radius)

    def __repr__(self):
        return f'Hyperbola2D(name="{self.name}")'
