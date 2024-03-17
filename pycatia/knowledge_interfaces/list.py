#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class List(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     List
                | 
                | Represents a CATIAList.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.list = com_object

    def add(self, i_item_value: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Add(AnyObject iItemValue)
                | 
                |     Adds an item at the end of the list. Does an AddRef on the item. Returns
                |     E_FAIL if the object type is not correct. Will return E_FAIL if trying to set
                |     an already existing element while IsDuplicateElementsAllowed is false.

        :param AnyObject i_item_value:
        :rtype: None
        """
        return self.list.Add(i_item_value.com_object)

    def item(self, i_index: cat_variant) -> AnyObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As AnyObject
                | 
                |     Retrieves a Feature using its index or its name from the Features
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Feature to retrieve from the
                |             collection of Features. As a numerics, this index is the rank of the Feature in
                |             the collection. The index of the first Feature in the collection is 1, and the
                |             index of the last Feature is Count. As a string, it is the name you assigned to
                |             the Feature using the 
                | 
                |         AnyObject.Name property or when creating the Feature. 
                |     Returns:
                |         The retrieved Feature 
                |     Example:
                |         This example retrieves the last Feature in the Features
                |         collection.
                | 
                |          Dim lastFeature As CATIABase
                |          Set lastFeature = Features.Item(Features.Count)

        :param cat_variant i_index:
        :rtype: AnyObject
        """
        return AnyObject(self.list.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a Feature from the Features collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Feature to retrieve from the
                |             collection of Features. As a numerics, this index is the rank of the Feature in
                |             the collection. The index of the first Feature in the collection is 1, and the
                |             index of the last Feature is Count. As a string, it is the name you assigned to
                |             the Feature using the 
                | 
                |         AnyObject.Name property or when creating the Feature. 
                | 
                | Example:
                |     This example removes the Feature named density from the Features
                |     collection.
                | 
                |      Features.Remove("density")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.list.Remove(i_index)

    def reorder(self, i_index_current: cat_variant, i_index_target: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Reorder(CATVariant iIndexCurrent,
                | CATVariant iIndexTarget)
                | 
                |     Reorders an element by moving it from the current position to the target
                |     position. Doesn't change the list if either position is out of the list. Return
                |     E_FAIL if cannot reorder.

        :param cat_variant i_index_current:
        :param cat_variant i_index_target:
        :rtype: None
        """
        return self.list.Reorder(i_index_current, i_index_target)

    def replace(self, i_index: cat_variant, i_item_value: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Replace(CATVariant iIndex,
                | AnyObject iItemValue)
                | 
                |     Sets an item in the list at a position. Does an AddRef on the item. Returns
                |     E_FAIL if the object type is not correct or the index is out of bounds. Returns
                |     E_FAIL if trying to set an already existing element while
                |     IsDuplicateElementsAllowed is false.

        :param cat_variant i_index:
        :param AnyObject i_item_value:
        :rtype: None
        """
        return self.list.Replace(i_index, i_item_value.com_object)

    def __getitem__(self, n: int) -> AnyObject:
        if (n + 1) > self.count:
            raise StopIteration

        return AnyObject(self.list.Item(n + 1))

    def __iter__(self) -> Iterator[AnyObject]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'List(name="{self.name}")'
