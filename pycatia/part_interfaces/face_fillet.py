#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.part_interfaces.fillet import Fillet


class FaceFillet(Fillet):

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
                |                         PartInterfaces.DressUpShape
                |                             PartInterfaces.Fillet
                |                                 FaceFillet
                | 
                | Represents the face fillet shape.
                | A face fillet shape is built between two faces with a fillet
                | radius.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.face_fillet = com_object

    @property
    def first_face(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstFace() As Reference
                | 
                |     Returns or sets the first limiting face.
                |     To set the property, you can use the following Boundary object:
                |     Face.
                | 
                |     Example:
                |         The following example returns in face1 the first limiting face of the
                |         face fillet firstFaceFillet, and then sets it to
                |         NewFace1:
                | 
                |          Set face1 = firstFaceFillet.FirstFace
                |          firstFaceFillet.FirstFace = NewFace1

        :rtype: Reference
        """

        return Reference(self.face_fillet.FirstFace)

    @first_face.setter
    def first_face(self, value: Reference):
        """
        :param Reference value:
        """

        self.face_fillet.FirstFace = value.com_object

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Radius() As Length (Read Only)
                | 
                |     Returns the face fillet radius.
                | 
                |     Example:
                |         The following example returns in radius the fillet radius of the face
                |         fillet firstFaceFillet:
                | 
                |          Set radius = firstFaceFillet.Radius

        :rtype: Length
        """

        return Length(self.face_fillet.Radius)

    @property
    def second_face(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondFace() As Reference
                | 
                |     Returns or sets the second limiting face.
                |     To set the property, you can use the following Boundary object:
                |     Face.
                | 
                |     Example:
                |         The following example returns in face2 the second limiting face of the
                |         face fillet firstFaceFillet, and then sets it to
                |         NewFace2:
                | 
                |          Set face2 = firstFaceFillet.SecondFace
                |          firstFaceFillet.SecondFace = NewFace2

        :rtype: Reference
        """

        return Reference(self.face_fillet.SecondFace)

    @second_face.setter
    def second_face(self, value: Reference):
        """
        :param Reference value:
        """

        self.face_fillet.SecondFace = value.com_object

    def __repr__(self):
        return f'FaceFillet(name="{ self.name }")'
