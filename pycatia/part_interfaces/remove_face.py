#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.references import References
from pycatia.part_interfaces.dress_up_shape import DressUpShape


class RemoveFace(DressUpShape):
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
                |                             RemoveFace
                | 
                | Represents the Remove Face operation.
                | It removes a face or a set of faces.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.remove_face = com_object

    @property
    def keep_face(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property KeepFace(Reference iKeepFace) (Write Only)
                | 
                |     Adds a new face to be Kept.
                | 
                |     Parameters:
                | 
                |         iKeepFace
                |             The new face to process
                |             The following 
                | 
                |         Boundary object is supported: Face.

        """

        return self.remove_face.KeepFace

    @keep_face.setter
    def keep_face(self, reference_face: Reference):
        """
        :param Reference reference_face:
        """

        self.remove_face.KeepFace = reference_face.com_object

    @property
    def keep_faces(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property KeepFaces() As References (Read Only)
                | 
                |     Get the specified faces to be kept.

        :return: References
        :rtype: References
        """

        return References(self.remove_face.KeepFaces)

    @property
    def propagation(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Propagation() As References (Read Only)
                | 
                |     Get the faces that will be removed.

        :return: References
        :rtype: References
        """

        return References(self.remove_face.Propagation)

    @property
    def remove_face(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RemoveFace(Reference iRemoveFace) (Write Only)
                | 
                |     Adds a new face to be removed.
                | 
                |     Parameters:
                | 
                |         iRemoveFace
                |             The new face to process
                |             The following 
                | 
                |         Boundary object is supported: Face.

        """

        return self.remove_face.RemoveFace

    @remove_face.setter
    def remove_face(self, reference_face: Reference):
        """
        :param Reference reference_face:
        """

        self.remove_face.RemoveFace = reference_face.com_object

    @property
    def remove_faces(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RemoveFaces() As References (Read Only)
                | 
                |     Get the specified faces to be removed.

        :return: References
        :rtype: References
        """

        return References(self.remove_face.RemoveFaces)

    def remove_keep_face(self, i_keep_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub remove_KeepFace(Reference iKeepFace)
                | 
                |     Removes a face to be Kept.
                | 
                |     Parameters:
                | 
                |         iKeepFace
                |             The new face to process
                |             The following 
                | 
                |         Boundary object is supported: Face.

        :param Reference i_keep_face:
        :return: None
        :rtype: None
        """
        return self.remove_face.remove_KeepFace(i_keep_face.com_object)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_keep_face'
        # # vba_code = """
        # # Public Function remove_keep_face(remove_face)
        # #     Dim iKeepFace (2)
        # #     remove_face.remove_KeepFace iKeepFace
        # #     remove_keep_face = iKeepFace
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_remove_face(self, i_remove_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub remove_RemoveFace(Reference iRemoveFace)
                | 
                |     Removes a face to be removed.
                | 
                |     Parameters:
                | 
                |         iRemoveFace
                |             The new face to process
                |             The following 
                | 
                |         Boundary object is supported: Face.

        :param Reference i_remove_face:
        :return: None
        :rtype: None
        """
        return self.remove_face.remove_RemoveFace(i_remove_face.com_object)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_remove_face'
        # # vba_code = """
        # # Public Function remove_remove_face(remove_face)
        # #     Dim iRemoveFace (2)
        # #     remove_face.remove_RemoveFace iRemoveFace
        # #     remove_remove_face = iRemoveFace
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'RemoveFace(name="{self.name}")'
