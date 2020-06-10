#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

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
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

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
    def line(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Reference
        """

        return Reference(self.hybrid_shape_plane1_line1_pt.Line)

    @line.setter
    def line(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_plane1_line1_pt.Line = value

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
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

        :return: Reference
        """

        return Reference(self.hybrid_shape_plane1_line1_pt.Point)

    @point.setter
    def point(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_plane1_line1_pt.Point = value

    def __repr__(self):
        return f'HybridShapePlane1Line1Pt(name="{ self.name }")'
