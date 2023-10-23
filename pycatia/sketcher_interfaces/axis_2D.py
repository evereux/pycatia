#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.sketcher_interfaces.geometry_2D import Geometry2D
from pycatia.sketcher_interfaces.line_2D import Line2D
from pycatia.sketcher_interfaces.point_2D import Point2D


class Axis2D(Geometry2D):
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
                |                             Axis2D
                | 
                | Interface defining a coordinate system in the 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.axis_2d = com_object

    @property
    def horizontal_reference(self) -> Line2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HorizontalReference() As Line2D (Read Only)
                | 
                |     Returns the 2D coordinate system horizontal axis.

        :rtype: Line2D
        """

        return Line2D(self.axis_2d.HorizontalReference)

    @property
    def origin(self) -> Point2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Origin() As Point2D (Read Only)
                | 
                |     Returns the 2D coordinate system origin.

        :rtype: Point2D
        """

        return Point2D(self.axis_2d.Origin)

    @property
    def vertical_reference(self) -> Line2D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property VerticalReference() As Line2D (Read Only)
                | 
                |     Returns the 2D coordinate system vertical axis.

        :rtype: Line2D
        """

        return Line2D(self.axis_2d.VerticalReference)

    def __repr__(self):
        return f'Axis2D(name="{self.name}")'
