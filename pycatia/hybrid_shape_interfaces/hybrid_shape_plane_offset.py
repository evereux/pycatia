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
from pycatia.knowledge_interfaces.length import Length


class HybridShapePlaneOffset(Plane):
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
                |                             HybridShapePlaneOffset
                | 
                | Offset plane.
                | Role: Allows to access data of the plane feature created with an offset to
                | another plane.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_plane_offset = com_object

    @property
    def offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Offset() As Length (Read Only)
                | 
                |     Returns the offset value.

        :rtype: Length
        """

        return Length(self.hybrid_shape_plane_offset.Offset)

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation() As long
                | 
                |     Returns or sets the plane orientation.
                |     Role: The orientation allows you to invert the plane from the reference
                |     plane.
                |     Legal values: the orientation is 1 if the plane orientation is not
                |     inverted, and -1 otherwise.

        :rtype: int
        """

        return self.hybrid_shape_plane_offset.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_plane_offset.Orientation = value

    @property
    def ref_plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Plane() As Reference
                | 
                |     Returns or sets the reference plane.
                |     Sub-element(s) supported (see Boundary object): PlanarFace.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_plane_offset.Plane)

    @ref_plane.setter
    def ref_plane(self, reference_plane: Reference):
        """
        :param Reference reference_plane:
        """

        self.hybrid_shape_plane_offset.Plane = reference_plane.com_object

    def __repr__(self):
        return f'HybridShapePlaneOffset(name="{self.name}")'
