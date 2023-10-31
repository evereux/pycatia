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


class HybridShapePlane1Curve(Plane):
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
                |                             HybridShapePlane1Curve
                | 
                | plane through a curve.
                | Role: Allows to access data of the plane feature passing though a planar
                | curve.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane1_curve = com_object

    @property
    def curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Curve() As Reference
                | 
                |     Role: Get the planar curve.
                | 
                |     Parameters:
                | 
                |         oCurve
                |             Curve. 
                | 
                |     See also:
                |         Reference 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_plane1_curve.Curve)

    @curve.setter
    def curve(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_plane1_curve.Curve = reference_curve.com_object

    def __repr__(self):
        return f'HybridShapePlane1Curve(name="{self.name}")'
