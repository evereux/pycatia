#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.part_interfaces.fillet import Fillet


class TritangentFillet(Fillet):

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
                |                                 TritangentFillet
                | 
                | The Tritangent Fillet feature : a fillet is built between 3 faces,
                | 2 faces will be relimited, the third one ("face to remove")
                | will
                | be used for fillet tangency ; this face will disappear within the resulting
                | shape.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tritangent_fillet = com_object

    @property
    def face_to_remove(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FaceToRemove() As Reference
                | 
                |     Returns the face to be removed by the tritangent fillet.
                | 
                |     Returns:
                |         oFaceToRemove The face to be removed by the fillet (@see CATIAReference
                |         for more information)
                | 
                |         Example:
                |             The following example returns in removedFace the face to be removed
                |             of
                |             tritangent fillet firstTritangentFillet:
                | 
                |              Set removedFace = firstTritangentFillet.FaceToRemove

        :rtype: Reference
        """

        return Reference(self.tritangent_fillet.FaceToRemove)

    @face_to_remove.setter
    def face_to_remove(self, value: Reference):
        """
        :param Reference value:
        """

        self.tritangent_fillet.FaceToRemove = value.com_object

    @property
    def first_face(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstFace() As Reference
                | 
                |     Returns the first face limiting the tritangent fillet.
                | 
                |     Returns:
                |         oFirstFace The limiting face (@see CATIAReference for more
                |         information)
                | 
                |         Example:
                |             The following example returns in face1 the first limiting face
                |             of
                |             tritangent fillet firstTritangentFillet:
                | 
                |              Set face1 = firstTritangentFillet.FirstFace

        :rtype: Reference
        """

        return Reference(self.tritangent_fillet.FirstFace)

    @first_face.setter
    def first_face(self, value: Reference):
        """
        :param Reference value:
        """

        self.tritangent_fillet.FirstFace = value.com_object

    @property
    def second_face(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondFace() As Reference
                | 
                |     Returns the second face limiting the tritangent fillet.
                | 
                |     Returns:
                |         oSecondFace The limiting face (@see CATIAReference for more
                |         information)
                | 
                |         Example:
                |             The following example returns in face2 the second limiting face
                |             of
                |             tritangent fillet firstTritangentFillet:
                | 
                |              Set face2 = firstTritangentFillet.SecondFace

        :rtype: Reference
        """

        return Reference(self.tritangent_fillet.SecondFace)

    @second_face.setter
    def second_face(self, value: Reference):
        """
        :param Reference value:
        """

        self.tritangent_fillet.SecondFace = value.com_object

    def __repr__(self):
        return f'TritangentFillet(name="{ self.name }")'
