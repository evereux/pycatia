#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.product_structure_interfaces.product import Product


class StrObject(Product):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ProductStructureInterfaces.Product
                |                         StrObject
                | 
                | Represents a structure object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_object = com_object

    @property
    def type_(self) -> Parameter:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As Parameter (Read Only)
                | 
                |     Returns the type of the structure object.
                | 
                |     Example:
                |         This example retrieves the type of the StructureMember
                |         object.
                | 
                |          Dim oType As Parameter
                |          Set oType = StructureMember.Type

        :rtype: Parameter
        """

        return Parameter(self.str_object.Type)

    def __repr__(self):
        return f'StrObject(name="{self.name}")'
