#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.plane import Plane
from pycatia.in_interfaces.reference import Reference


class HybridShapePlaneNormal(Plane):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneNormal
                | 
                | Normal plane.
                | Role: Allows to access data of the plane feature normal to a curve at a given
                | point.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_normal = com_object

    @property
    def curve(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Curve() As Reference
                | 
                |     Role: Get the curve to which the plane is to be normal.
                | 
                |     Parameters:
                | 
                |         oCurve
                |             reference curve. 
                | 
                |     See also:
                |         Reference 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Reference
        """

        return Reference(self.hybrid_shape_plane_normal.Curve)

    @curve.setter
    def curve(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_plane_normal.Curve = value

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Point() As Reference
                | 
                |     Role: Get the point where the plane is to be normal.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             point 
                | 
                |     See also:
                |         Reference 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Reference
        """

        return Reference(self.hybrid_shape_plane_normal.Point)

    @point.setter
    def point(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_plane_normal.Point = value

    def __repr__(self):
        return f'HybridShapePlaneNormal(name="{ self.name }")'
