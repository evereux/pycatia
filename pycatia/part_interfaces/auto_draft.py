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
from pycatia.part_interfaces.dress_up_shape import DressUpShape


class AutoDraft(DressUpShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             AutoDraft
                | 
                | Represents the AutoDraft shape.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.auto_draft = com_object

    @property
    def functional_face(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FunctionalFace(Reference iFace) (Write Only)

        :rtype: Reference
        """

        return Reference(self.auto_draft.FunctionalFace)

    @functional_face.setter
    def functional_face(self, reference: Reference):
        """
        :param Reference reference:
        """

        self.auto_draft.FunctionalFace = reference.com_object

    @property
    def functional_faces(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FunctionalFaces() As References (Read Only)
                | 
                |     Returns or sets the functional faces.
                | 
                |     Example:
                |         The following example returns in FunctionalFaces the list functional
                |         faces of the AutoDraft AutoDraft, and then sets NewFunctionalFace as a
                |         functional face:
                | 
                |          Set FunctionalFaces = AutoDraft.FunctionalFace
                |          AutoDraft.FunctionalFace = NewFunctionalFace

        :rtype: References
        """

        return References(self.auto_draft.FunctionalFaces)

    @property
    def main_draft_angle(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MainDraftAngle() As Reference
                | 
                |     Returns or sets the main draft angle.
                | 
                |     Example:
                |         The following example returns in MainDraftAngle the main draft angle of
                |         the AutoDraft AutoDraft, and then sets it to
                |         NewMainDraftAngle.:
                | 
                |          Set MainDraftAngle = AutoDraft.MainDraftAngle
                |          AutoDraft.MainDraftAngle = NewMainDraftAngle

        :rtype: Reference
        """

        return Reference(self.auto_draft.MainDraftAngle)

    @main_draft_angle.setter
    def main_draft_angle(self, value: Reference):
        """
        :param Reference value:
        """

        self.auto_draft.MainDraftAngle = value.com_object

    @property
    def mode(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Mode() As Reference
                | 
                |     Returns or sets the draft mode.
                | 
                |     Example:
                |         The following example returns in Mode the mode of the draft AutoDraft
                |         AutoDraft, and then sets it to NewMode:
                | 
                |          Set Mode = AutoDraft.Mode
                |          AutoDraft.Mode = NewMode

        :rtype: Reference
        """

        return Reference(self.auto_draft.Mode)

    @mode.setter
    def mode(self, value: Reference):
        """
        :param Reference value:
        """

        self.auto_draft.Mode = value.com_object

    @property
    def parting_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PartingElement() As Reference
                | 
                |     Returns or sets the parting element.
                | 
                |     Example:
                |         The following example returns in PartingElement the parting element of
                |         the AutoDraft AutoDraft, and then sets it to
                |         NewpartingElement:
                | 
                |          Set PartingElement = AutoDraft.PartingElement
                |          AutoDraft.PartingElement = NewPartingElement

        :rtype: Reference
        """

        return Reference(self.auto_draft.PartingElement)

    @parting_element.setter
    def parting_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.auto_draft.PartingElement = value.com_object

    @property
    def pulling_direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PullingDirection() As Reference
                | 
                |     Returns or sets the pulling direction.
                | 
                |     Example:
                |         The following example returns in PullingDirection the pulling direction
                |         of the AutoDraft AutoDraft, and then sets it to
                |         NewPullingDirection.:
                | 
                |          Set PullingDirection = AutoDraft.PullingDirection
                |          AutoDraft.PullingDirection = NewPullingDirection

        :rtype: Reference
        """

        return Reference(self.auto_draft.PullingDirection)

    @pulling_direction.setter
    def pulling_direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.auto_draft.PullingDirection = value.com_object

    def __repr__(self):
        return f'AutoDraft(name="{self.name}")'
