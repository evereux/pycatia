#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.funct_system_interfaces.functional_element import FunctionalElement
from pycatia.system_interfaces.any_object import AnyObject


class FunctionalFacet(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FunctionalFacet
                | 
                | The interface to access a Functional Facet.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.functional_facet = com_object

    @property
    def functional_element(self) -> FunctionalElement:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FunctionalElement() As FunctionalElement (Read
                | Only)
                | 
                |     Get the Functional Element owning the Facet.

        :rtype: FunctionalElement
        """

        return FunctionalElement(self.functional_facet.FunctionalElement)

    def free(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Free()
                | 
                |     Free the resources allocated by the Facet.

        :rtype: None
        """
        return self.functional_facet.Free()

    def init(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Init()
                | 
                |     Init resources for the Facet.

        :rtype: None
        """
        return self.functional_facet.Init()

    def __repr__(self):
        return f'FunctionalFacet(name="{self.name}")'
