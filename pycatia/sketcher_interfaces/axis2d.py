#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .geometricelement import GeometricElement
from .line2d import Line2D
from .point2d import Point2D


class Axis2D(GeometricElement):
    """
        .. note::
            CAA V5 Visual Basic help

                | Interface defining a coordinate system in the 2D Space.

    """

    def __init__(self, catia, com_object):
        super().__init__(com_object)
        self.axis2d = catia.Axis2D

    @property
    def horizontal_reference(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HorizontalReference
                | o Property HorizontalReference(    ) As Line2D
                | 
                | Returns the 2D coordinate system horizontal axis.

        :return: Line2D()
        """
        return Line2D(self.axis2d.HorizontalReference)

    @property
    def origin(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Origin
                | o Property Origin(    ) As Point2D
                | 
                | Returns the 2D coordinate system origin.

        :return: Point2D()
        """
        return Point2D(self.axis2d.Origin)

    @property
    def vertical_reference(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | VerticalReference
                | o Property VerticalReference(    ) As Line2D
                | 
                | Returns the 2D coordinate system vertical axis.

        :return: Line2D
        """
        return Line2D(self.axis2d.VerticalReference)

    def __repr__(self):
        return f'Axis2D(name="{self.name}")'
