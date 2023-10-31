#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.document import Document
from pycatia.funct_system_interfaces.funct_facet_managers import FunctFacetManagers
from pycatia.funct_system_interfaces.functional_description import FunctionalDescription


class FunctionalDocument(Document):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Document
                |                         FunctionalDocument
                | 
                | Represents a Functional Document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.functional_document = com_object

    @property
    def current_description(self) -> FunctionalDescription:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CurrentDescription() As FunctionalDescription (Read
                | Only)
                | 
                |     Returns the Current Description.

        :rtype: FunctionalDescription
        """

        return FunctionalDescription(self.functional_document.CurrentDescription)

    @property
    def facet_managers(self) -> FunctFacetManagers:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FacetManagers() As FunctFacetManagers (Read Only)
                | 
                |     Returns the Facet Managers.

        :rtype: FunctFacetManagers
        """

        return FunctFacetManagers(self.functional_document.FacetManagers)

    @property
    def original_description(self) -> FunctionalDescription:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OriginalDescription() As FunctionalDescription (Read
                | Only)
                | 
                |     Returns the Original Description.

        :rtype: FunctionalDescription
        """

        return FunctionalDescription(self.functional_document.OriginalDescription)

    def __repr__(self):
        return f'FunctionalDocument(name="{self.name}")'
