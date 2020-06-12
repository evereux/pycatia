#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.part_interfaces.draft_domains import DraftDomains
from pycatia.part_interfaces.dress_up_shape import DressUpShape


class Draft(DressUpShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Draft
                | 
                | Represents the draft shape.
                | A draft shape is made up of draft domains (at least one) and of a parting
                | element.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.draft = com_object

    @property
    def draft_domains(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DraftDomains() As DraftDomains (Read Only)
                | 
                |     Returns the collection of draft domains.
                | 
                |     Example:
                |         The following example returns in list the collection of draft domains
                |         of the firstDraft draft:
                | 
                |          Set list = firstDraft.DraftDomains

        :return: DraftDomains
        """

        return DraftDomains(self.draft.DraftDomains)

    @property
    def mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Mode() As CatDraftMode
                | 
                |     Returns or sets the draft mode.
                | 
                |     Example:
                |         The following example returns in mode the draft mode of the firstDraft
                |         draft, and then sets it to
                |         CatReflectKeepFaceDraftMode:
                | 
                |          Set mode = firstDraft.Mode
                |          Set firstDraft.Mode = CatReflectKeepFaceDraftMode

        :return: enum cat_draft_mode
        """

        return self.draft.Mode

    @mode.setter
    def mode(self, value):
        """
        :param enum cat_draft_mode value:
        """

        self.draft.Mode = value

    @property
    def parting_element(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PartingElement() As Reference
                | 
                |     Returns or sets the draft parting element.
                |     To set the property, you can use the following Boundary object:
                |     PlanarFace.
                | 
                |     Example:
                |         The following example returns in element the parting element of the
                |         firstDraft draft, and then sets it to the element2 geometrical
                |         element:
                | 
                |          Set element = firstDraft.PartingElement
                |          Set firstDraft.PartingElement = element2

        :return: Reference
        """

        return Reference(self.draft.PartingElement)

    @parting_element.setter
    def parting_element(self, value):
        """
        :param Reference value:
        """

        self.draft.PartingElement = value

    def __repr__(self):
        return f'Draft(name="{ self.name }")'
