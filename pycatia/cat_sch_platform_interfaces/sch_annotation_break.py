#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchAnnotationBreak(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAnnotationBreak
                | 
                | Manage an annotation break operations.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_annotation_break = com_object

    def flip_over_line(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub FlipOverLine()
                | 
                |     Mirror the symbol over the route segment line that ends in the connector on
                |     which the symbol is placed.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAnnotationBreak
                |           ...
                |          objThisIntf.FlipOverLine

        :rtype: None
        """
        return self.sch_annotation_break.FlipOverLine()

    def flip_over_orthogonal_line(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub FlipOverOrthogonalLine()
                | 
                |     Mirror the symbol over the line orthogonal to the route segment line that
                |     ends in the connector on which the symbol is placed and going through the
                |     connector's position.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAnnotationBreak
                |           ...
                |          objThisIntf.FlipOverOrthogonalLine

        :rtype: None
        """
        return self.sch_annotation_break.FlipOverOrthogonalLine()

    def scale(self, i_db_scale_factor: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Scale(double iDbScaleFactor)
                | 
                |     Scale the symbol.
                | 
                |     Parameters:
                | 
                |         iDbScaleFactor
                |             The scale factor to scale the symbol by. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAnnotationBreak
                |          Dim dbVar1 As Double
                |           ...
                |          objThisIntf.ScaledbVar1

        :param float i_db_scale_factor:
        :rtype: None
        """
        return self.sch_annotation_break.Scale(i_db_scale_factor)

    def __repr__(self):
        return f'SchAnnotationBreak(name="{self.name}")'
