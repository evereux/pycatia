#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from .geometricelement import GeometricElement


class Geometry2D(GeometricElement):
    """
        .. note::
            CAA V5 Visual Basic help

                | 2D wireframe geometric element.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.geometry2d = com_object

    @property
    def construction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Construction
                | o Property Construction(    ) As boolean
                | 
                | Returns the construction mode of the 2D geometry

                | Parameters:

        :return: bool
        """
        return self.geometry2d.Construction

    @property
    def report_name(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReportName
                | o Property ReportName(    ) As long
                | 
                | Returns the report name of the 2D geometry
                |
                | Parameters:
                | oReportName
                |        The integer value of the report name

        :return: int
        """
        return self.geometry2d.ReportName

    def __repr__(self):
        return f'Geometry2D(name="{self.name}")'

