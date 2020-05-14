#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.collection import Collection


class List(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents a CATIAList.

    """

    def __init__(self, collection_com_object):
        super().__init__(collection_com_object)
        self.list = collection_com_object

    def add(self, i_item_value):
        """
        .. note::
            CAA V5 Visual Basic help

                | Add
                | o Sub Add(    AnyObject    iItemValue)
                | 
                | Adds an item at the end of the list. Does an AddRef on the item.
                | Returns E_FAIL if the object type is not correct. Will return E_FAIL
                | if trying to set an already existing element while
                | IsDuplicateElementsAllowed is false.


                | Parameters:


        """
        return self.list.Add(i_item_value)

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(    CATVariant    iIndex) As AnyObject
                | 
                | Retrieves a Feature using its index or its name from the Features
                | collection.


                | Parameters:
                | iIndex
                |    The index or the name of the Feature to retrieve from
                |    the collection of Features.
                |    As a numerics, this index is the rank of the Feature
                |    in the collection.
                |    The index of the first Feature in the collection is 1, and
                |    the index of the last Feature is Count.
                |    As a string, it is the name you assigned to the Feature using
                |    the 
                | 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property or when creating the Feature. 
                |    Returns:
                |   The retrieved Feature


                | Examples:
                | 
                | 
                | This example retrieves the last Feature in the Features
                | collection.
                | 
                | Dim lastFeature As CATIABase
                | Set lastFeature = Features.Item(Features.Count)
                | 
                | 
                | 
        """
        return self.list.Item(i_index)

    def remove(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Remove
                | o Sub Remove(    CATVariant    iIndex)
                | 
                | Removes a Feature from the Features collection.


                | Parameters:
                | iIndex
                |    The index or the name of the Feature to retrieve from
                |    the collection of Features.
                |    As a numerics, this index is the rank of the Feature
                |    in the collection.
                |    The index of the first Feature in the collection is 1, and
                |    the index of the last Feature is Count.
                |    As a string, it is the name you assigned to the Feature using
                |    the 
                | 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property or when creating the Feature.


                | Examples:
                | 
                | 
                | This example removes the Feature named density from
                | the Features collection.
                | 
                | Features.Remove("density")
                | 
                | 
        """
        return self.list.Remove(i_index)

    def reorder(self, i_index_current, i_index_target):
        """
        .. note::
            CAA V5 Visual Basic help

                | Reorder
                | o Sub Reorder(    CATVariant    iIndexCurrent,
                |                   CATVariant    iIndexTarget)
                | 
                | Reorders an element by moving it from the current position to the
                | target position. Doesn't change the list if either position is out of
                | the list. Return E_FAIL if cannot reorder.


                | Parameters:


        """
        return self.list.Reorder(i_index_current, i_index_target)

    def replace(self, i_index, i_item_value):
        """
        .. note::
            CAA V5 Visual Basic help

                | Replace
                | o Sub Replace(    CATVariant    iIndex,
                |                   AnyObject    iItemValue)
                | 
                | Sets an item in the list at a position. Does an AddRef on the item.
                | Returns E_FAIL if the object type is not correct or the index is out
                | of bounds. Returns E_FAIL if trying to set an already existing element
                | while IsDuplicateElementsAllowed is false.


                | Parameters:


        """
        return self.list.Replace(i_index, i_item_value)
