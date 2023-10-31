#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.structure_interfaces.str_foundation import StrFoundation
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class StrFoundations(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrFoundations
                | 
                | A collection of the Foundation objects contained in a given Product object of a
                | ProductDocument object.
                | A Product object aggregates zero or one Foundations collection. This collection
                | is retrieved using the Product.GetTechnologicalObject method of the
                | product.
                | 
                | Example:
                | 
                |       The following example retrieves the Foundation collection from
                |       the
                |      oProduct Product.
                |      
                | 
                |      Dim oFoundations as AnyObject
                |      Set oFoundations = oProduct.GetTechnologicalObject("StructureFoundations")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=StrFoundation)
        self.str_foundations = com_object

    def item(self, i_index: cat_variant) -> StrFoundation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As StrFoundation
                | 
                |     Returns a Foundation from its index in the Foundations
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Foundation to retrieve in the collection of
                |             Foundations. This index can either be the rank of the Foundation in the
                |             collection or the name you assign to the Foundation. As a numerics, this index
                |             is the rank of the Foundation in the collection. The index of the first
                |             Foundation in the collection is 1, and the index of the last Foundation is
                |             Count. As a string, it is the name you assigned to the Foundation using the
                |             
                | 
                |         AnyObject.Name property 
                |     Returns:
                |         The retrieved Foundation 
                |     Example:
                | 
                |           The following example returns in ThisFoundation the third
                |           Foundation,
                |          and in ThatFoundation the Foundation named
                |          Column_1 in the Assembly_1 Foundation collection.
                |          
                | 
                |          Dim ThisFoundation As Foundation
                |          Set ThisFoundation = Assembly_1.Item(3)
                |          Dim ThatFoundation As Foundation
                |          Set ThatFoundation = Assembly.Item("Column_1")

        :param cat_variant i_index:
        :rtype: StrFoundation
        """
        return StrFoundation(self.str_foundations.Item(i_index))

    def __repr__(self):
        return f'StrFoundations(name="{self.name}")'
