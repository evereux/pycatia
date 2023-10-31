#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.knowledge_interfaces.parameters import Parameters
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.funct_system_interfaces.functional_document import FunctionalDocument


class FunctionalElement(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FunctionalElement
                | 
                | Represents a Functional Element.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.functional_element = com_object

    @property
    def document(self) -> 'FunctionalDocument':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Document() As FunctionalDocument (Read Only)
                | 
                |     Returns the Document.

        :rtype: FunctionalDocument
        """

        return FunctionalDocument(self.functional_element.Document)

    @property
    def parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Parameters() As Parameters (Read Only)
                | 
                |     Returns the parameters collection.

        :rtype: Parameters
        """

        return Parameters(self.functional_element.Parameters)

    def __repr__(self):
        return f'FunctionalElement(name="{self.name}")'
