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
from pycatia.knowledge_interfaces.length import Length


class HybridShapePlaneOffset(Plane):

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
    def offset(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Offset() As Length (Read Only)
                | 
                |     Returns the offset value.

        :return: Length
        """

        return Length(self.hybrid_shape_plane_offset.Offset)

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Orientation() As long
                | 
                |     Returns or sets the plane orientation.
                |     Role: The orientation allows you to invert the plane from the reference
                |     plane.
                |     Legal values: the orientation is 1 if the plane orientation is not
                |     inverted, and -1 otherwise.

        :return: int
        """

        return self.hybrid_shape_plane_offset.Orientation

    @orientation.setter
    def orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_plane_offset.Orientation = value

    @property
    def plane(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Plane() As Reference
                | 
                |     Returns or sets the reference plane.
                |     Sub-element(s) supported (see Boundary object): PlanarFace.

        :return: Reference
        """

        return Reference(self.hybrid_shape_plane_offset.Plane)

    @plane.setter
    def plane(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_plane_offset.Plane = value

    def __repr__(self):
        return f'HybridShapePlaneOffset(name="{ self.name }")'
