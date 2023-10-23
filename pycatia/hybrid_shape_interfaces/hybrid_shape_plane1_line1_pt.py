#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.plane import Plane
from pycatia.in_interfaces.reference import Reference


class HybridShapePlane1Line1Pt(Plane):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlane1Line1Pt
                | 
                | Represents plane feature defined by a line and a point.
                | Role: Allows to access data of the plane feature passing though one line and
                | one point
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane1_line1_pt = com_object

    @property
    def line(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Line() As Reference
                | 
                |     Returns or sets the passing line.
                | 
                |     Parameters:
                | 
                |         oLine
                |             Line. 
                | 
                |     See also:
                |         Reference 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_plane1_line1_pt.Line)

    @line.setter
    def line(self, reference_line: Reference):
        """
        :param Reference reference_line:
        """

        self.hybrid_shape_plane1_line1_pt.Line = reference_line

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Point() As Reference
                | 
                |     Return or sets the passing point.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             Point. 
                | 
                |     See also:
                |         Reference 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_plane1_line1_pt.Point)

    @point.setter
    def point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_plane1_line1_pt.Point = reference_point.com_object

    def __repr__(self):
        return f'HybridShapePlane1Line1Pt(name="{self.name}")'
