#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.references import References
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.system_interfaces.any_object import AnyObject


class DraftDomain(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DraftDomain
                | 
                | Represents the draft domain.
                | A draft domain is a basic object used by a draft shape. It contains objects
                | such as an angle, a pulling direction, and a collection of faces to be
                | drafted.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.draft_domain = com_object

    @property
    def draft_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DraftAngle() As Angle (Read Only)
                | 
                |     Returns the draft angle.
                | 
                |     Example:
                |         The following example returns in angle the draft angle of the draft
                |         domain firstDraftDomain:
                | 
                |          Set angle = firstDraftDomain.DraftAngle

        :rtype: Angle
        """

        return Angle(self.draft_domain.DraftAngle)

    @property
    def faces_to_draft(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FacesToDraft() As References (Read Only)
                | 
                |     Returns the faces to be drafted. They are returned as a collection of
                |     reference geometric elements.
                | 
                |     Example:
                |         The following example returns the collection of faces to be drafted of
                |         the draft domain firstDraftDomain in list:
                | 
                |          Set list = firstDraftDomain.FacesToDraft

        :rtype: References
        """

        return References(self.draft_domain.FacesToDraft)

    @property
    def multiselection_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MultiselectionMode() As CatDraftMultiselectionMode
                | 
                |     Changes the multiselection mode.
                | 
                |     Parameters:
                | 
                |         iMultiselectionMode.
                |             The elements to be drafted can be selected explicitly
                |             (CATNoneDraftMultiselectionMode) or can implicitly selected as neighbors of the
                |             neutral face (CATMultiselectionByNeutralMode)
                | 
                |             Example:
                |                 The following example returns in MultiselMode the
                |                 multiselection mode of the draft domain firstDraftDomain, and then sets it to
                |                 CATMultiselectionByNeutralMode
                | 
                |                  Set MultiselMode = firstDraftDomain.MultiselectionMode
                |                  firstDraftDomain.MultiselectionMode = CATMultiselectionByNeutralMode

        :return: enum cat_draft_multiselection_mode
        :rtype: int
        """

        return self.draft_domain.MultiselectionMode

    @multiselection_mode.setter
    def multiselection_mode(self, value: int):
        """
        :param int value: enum cat_draft_multiselection_mode
        """

        self.draft_domain.MultiselectionMode = value

    @property
    def neutral_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NeutralElement() As Reference
                | 
                |     Returns or sets the draft neutral element.
                |     To set the property, you can use the following Boundary object:
                |     PlanarFace.
                | 
                |     Example:
                |         The following example returns in neutral the neutral element of the
                |         draft domain firstDraftDomain, and then sets it to
                |         newNeutral:
                | 
                |          Set neutral = firstDraftDomain.NeutralElement
                |          firstDraftDomain.NeutralElement = newNeutral

        :rtype: Reference
        """

        return Reference(self.draft_domain.NeutralElement)

    @neutral_element.setter
    def neutral_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.draft_domain.NeutralElement = value.com_object

    @property
    def neutral_propagation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NeutralPropagationMode() As
                | CatDraftNeutralPropagationMode
                | 
                |     Returns or sets the neutral element propagation mode. This mode is used
                |     when computing the needed neutral elements.
                | 
                |     Example:
                |         The following example returns in propMode the neutral propagation mode
                |         of the draft domain firstDraftDomain, and then sets it to
                |         CATSmoothDraftNeutralPropagationMode so that the neutral propagation will now
                |         be smooth:
                | 
                |          Set propMode = firstDraftDomain.NeutralPropagationMode
                |          firstDraftDomain.NeutralPropagationMode = CATSmoothDraftNeutralPropagationMode

        :return: enum cat_draft_neutral_propagation_mode
        :rtype: int
        """

        return self.draft_domain.NeutralPropagationMode

    @neutral_propagation_mode.setter
    def neutral_propagation_mode(self, value: int):
        """
        :param int value: enum cat_draft_neutral_propagation_mode
        """

        self.draft_domain.NeutralPropagationMode = value

    @property
    def pulling_direction_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PullingDirectionElement() As Reference
                | 
                |     Returns or sets the draft pulling direction element.
                |     To set the property, you can use one of the following Boundary objects:
                |     PlanarFace or RectilinearTriDimFeatEdge.
                | 
                |     Example:
                |         The following example returns in pullingdirection the pulling direction
                |         element of the draft domain firstDraftDomain, and then sets it to
                |         newPullingDirection:
                | 
                |          Set pullingdirection = firstDraftDomain.NeutralElement
                |          firstDraftDomain.PullingDirectionElement = newPullingDirection

        :rtype: Reference
        """

        return Reference(self.draft_domain.PullingDirectionElement)

    @pulling_direction_element.setter
    def pulling_direction_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.draft_domain.PullingDirectionElement = value.com_object

    def add_face_to_draft(self, i_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFaceToDraft(Reference iFace)
                | 
                |     Adds a face to those to be drafted.
                | 
                |     Parameters:
                | 
                |         iFace
                |             The face to add to those to be drafted
                |             The following 
                | 
                |         Boundary object is supported: ScFace. 
                | 
                | Example:
                |     The following example adds the face NewFaceToDraft to the draft domain
                |     CurrentDraftDomain:
                | 
                |      CurrentDraftDomain.AddFaceToDraft(NewFaceToDraft)

        :param Reference i_face:
        :rtype: None
        """
        return self.draft_domain.AddFaceToDraft(i_face.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_face_to_draft'
        # # vba_code = """
        # # Public Function add_face_to_draft(draft_domain)
        # #     Dim iFace (2)
        # #     draft_domain.AddFaceToDraft iFace
        # #     add_face_to_draft = iFace
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_pulling_direction(self, io_pulling_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetPullingDirection(CATSafeArrayVariant
                | ioPullingDirection)
                | 
                |     Returns the draft pulling direction. The pulling direction is returned as
                |     an array containing the pulling direction vector components. Assume this array
                |     is PullDir. It contains:
                | 
                |     PullDir[0],PullDir[1],PullDir[2]
                |         The X, Y, and Z pulling direction vector components 
                | 
                |     Example:
                |         The following example returns in PullDir the pulling direction vector
                |         components of the draft domain firstDraftDomain:
                | 
                |          Set PullDir = firstDraftDomain.PullingDirection
                |          Set x = PullDir[0]
                |          Set y = PullDir[1]
                |          Set z = PullDir[2]

        :param tuple io_pulling_direction:
        :rtype: None
        """
        return self.draft_domain.GetPullingDirection(io_pulling_direction)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_pulling_direction'
        # # vba_code = """
        # # Public Function get_pulling_direction(draft_domain)
        # #     Dim ioPullingDirection (2)
        # #     draft_domain.GetPullingDirection ioPullingDirection
        # #     get_pulling_direction = ioPullingDirection
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_face_to_draft(self, i_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveFaceToDraft(Reference iFace)
                | 
                |     Removes a face from those to be drafted.
                | 
                |     Parameters:
                | 
                |         iFace
                |             The face to be removed from those to be drafted
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example removes the face FaceToRemove from the draft domain
                |     CurrentDraftDomain:
                | 
                |      CurrentDraftDomain.RemoveFaceToDraft(FaceToRemove)

        :param Reference i_face:
        :rtype: None
        """
        return self.draft_domain.RemoveFaceToDraft(i_face.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_face_to_draft'
        # # vba_code = """
        # # Public Function remove_face_to_draft(draft_domain)
        # #     Dim iFace (2)
        # #     draft_domain.RemoveFaceToDraft iFace
        # #     remove_face_to_draft = iFace
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pulling_direction(self, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPullingDirection(double iX,
                | double iY,
                | double iZ)
                | 
                |     Sets the draft pulling direction.
                | 
                |     Parameters:
                | 
                |         iX,iY,iZ
                |             The X, Y, and Z pulling direction vector components
                |             
                | 
                |     Example:
                |         The following example sets the draft pulling direction of the draft
                |         domain firstDraftDomain to the direction with the vector components 10, -5,
                |         10:
                | 
                |          firstDraftDomain.PullingDirection 10, -5, 10

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :rtype: None
        """
        return self.draft_domain.SetPullingDirection(i_x, i_y, i_z)

    def set_volume_support(self, i_volume_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetVolumeSupport(Reference iVolumeSupport)
                | 
                |     Value the support of draft.
                | 
                |     Parameters:
                | 
                |         iVolumeSupport

        :param Reference i_volume_support:
        :rtype: None
        """
        return self.draft_domain.SetVolumeSupport(i_volume_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_volume_support'
        # # vba_code = """
        # # Public Function set_volume_support(draft_domain)
        # #     Dim iVolumeSupport (2)
        # #     draft_domain.SetVolumeSupport iVolumeSupport
        # #     set_volume_support = iVolumeSupport
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DraftDomain(name="{self.name}")'
