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


class HybridShapePlaneOffsetPt(Plane):
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
                |                             HybridShapePlaneOffsetPt
                | 
                | Offset plane with point reference.
                | Role: Allows to access data of the plane feature parallel to another plane and
                | passing through a Point.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_offset_pt = com_object

    @property
    def ref_plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Plane() As Reference
                | 
                |     Role: Get the reference plane.
                | 
                |     Parameters:
                | 
                |         oPlane
                |             reference Plane. 
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

        return Reference(self.hybrid_shape_plane_offset_pt.Plane)

    @ref_plane.setter
    def ref_plane(self, reference_plane: Reference):
        """
        :param Reference reference_plane:
        """

        self.hybrid_shape_plane_offset_pt.Plane = reference_plane.com_object

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Point() As Reference
                | 
                |     Role: Get the reference point.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             reference point. 
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

        return Reference(self.hybrid_shape_plane_offset_pt.Point)

    @point.setter
    def point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_plane_offset_pt.Point = reference_point.com_object

    def __repr__(self):
        return f'HybridShapePlaneOffsetPt(name="{self.name}")'
