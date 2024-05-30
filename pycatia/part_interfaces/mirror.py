#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.part_interfaces.transformation_shape import TransformationShape
from pycatia.system_interfaces.any_object import AnyObject


class Mirror(TransformationShape):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.TransformationShape
                |                             Mirror
                | 
                | Represents the mirror shape.
                | It duplicates a shape with respect to a planar mirroring element, such as a
                | planar face or a plane.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.mirror = com_object

    @property
    def mirroring_object(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MirroringObject() As AnyObject (Read Only)
                | 
                |     Returns the mirroring Object.

        :rtype: AnyObject
        """

        return AnyObject(self.mirror.MirroringObject)

    @property
    def mirroring_plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MirroringPlane() As Reference
                | 
                |     Returns or sets the mirroring reference plane. It can be a plane, or a
                |     plane face.
                |     To set the property, you can use the following Boundary object:
                |     PlanarFace.
                | 
                |     Example:
                |         The following example returns in ref the mirroring reference plane of
                |         the mirroring firstMirroring, and then sets it to the created
                |         MyRef:
                | 
                |          Set ref = firstMirroring.MirroringPlane
                |          Set MyRef = part.CreateReferenceFromGeometry (plane)
                |          firstMirroring.MirroringPlane = MyRef

        :rtype: Reference
        """

        return Reference(self.mirror.MirroringPlane)

    @mirroring_plane.setter
    def mirroring_plane(self, value: Reference):
        """
        :param Reference value:
        """

        self.mirror.MirroringPlane = value.com_object

    def __repr__(self):
        return f'Mirror(name="{ self.name }")'
