#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.list import List
from pycatia.knowledge_interfaces.parameter import Parameter


class ListParameter(Parameter):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.Parameter
                |                         ListParameter
                | 
                | Represents a CATIAListParameter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.list_parameter = com_object

    @property
    def value_list(self) -> List:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ValueList() As List (Read Only)
                | 
                |     Returns or sets the value of the List object.

        :rtype: List
        """

        return List(self.list_parameter.ValueList)

    def __repr__(self):
        return f'ListParameter(name="{ self.name }")'
