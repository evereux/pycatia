#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.sketcher_interfaces.geometric_element import GeometricElement


class Geometry2D(GeometricElement):
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
                |                         Geometry2D
                | 
                | 2D wireframe geometric element.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.geometry_2d = com_object

    @property
    def construction(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Construction() As boolean
                | 
                |     Returns the construction mode of the 2D geometry

        :rtype: bool
        """

        return self.geometry_2d.Construction

    @construction.setter
    def construction(self, value: bool):
        """
        :param bool value:
        """

        self.geometry_2d.Construction = value

    @property
    def report_name(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReportName() As long
                | 
                |     Returns the report name of the 2D geometry
                | 
                |     Parameters:
                | 
                |         oReportName
                |             The integer value of the report name

        :rtype: int
        """

        return self.geometry_2d.ReportName

    @report_name.setter
    def report_name(self, value: int):
        """
        :param int value:
        """

        self.geometry_2d.ReportName = value

    def __repr__(self):
        return f'Geometry2D(name="{self.name}")'
