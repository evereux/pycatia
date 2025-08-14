#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.navigator_interfaces.group import Group
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Groups(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Groups
                | 
                | A collection of all groups currently managed by the
                | application.
                | 
                | The method Product.GetTechnologicalObject ("Groups") on the root product
                | retrieves this collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Group)
        self.groups = com_object

    def add(self) -> Group:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add() As Group
                | 
                |     Creates an empty Group and adds it to the Groups
                |     Collection.
                | 
                |     Returns:
                |         The created group 
                |     Example:
                | 
                |              This example creates a new group in the TheGroups
                |              collection.
                |             
                | 
                |             Dim NewGroup As Group
                |             Set NewGroup = TheGroups.Add

        :rtype: Group
        """
        return Group(self.groups.Add())

    def add_from_sel(self) -> Group:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddFromSel() As Group
                | 
                |     Creates a Group containing all products in the selection and adds it to the
                |     Groups Collection.
                | 
                |     Returns:
                |         The created group 
                |     Example:
                | 
                |              This example creates a new group containing all products in the
                |              selection
                |             in the TheGroups collection.
                |             
                | 
                |             Dim NewGroup As Group
                |             Set NewGroup = TheGroups.AddFromSel

        :rtype: Group
        """
        return Group(self.groups.AddFromSel())

    def all_leaves(self) -> Group:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AllLeaves() As Group
                | 
                |     Returns a group which contains all the terminal nodes of the current root
                |     product.
                | 
                |     Example:
                | 
                |              This example retrieves the group in the TheGroups
                |              collection.
                |             
                | 
                |             Dim AllLeavesGroup As Group
                |             Set AllLeavesGroup = TheGroups.AllLeaves

        :rtype: Group
        """
        return Group(self.groups.AllLeaves())

    def item(self, i_index: cat_variant) -> Group:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Group
                | 
                |     Returns a group using its index or its name from the Groups
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Group to retrieve from the collection
                |             of groups. As a numerics, this index is the rank of the Group in the
                |             collection. The index of the first Group in the collection is 1, and the index
                |             of the last Group is Count. As a string, it is the name you assigned to the
                |             Group. 
                | 
                |     Returns:
                |         The retrieved Group 
                |     Example:
                | 
                |              This example retrieves in ThisGroup the ninth
                |              Group,
                |             and in ThatGroup the Group named
                |             Group3 from the TheGroups collection. 
                |             
                | 
                |             Dim ThisGroup As Group
                |             Set ThisGroup = TheGroups.Item(9)
                |             Dim ThatGroup As Group
                |             Set ThatGroup = TheGroups.Item("Group3")

        :param cat_variant i_index:
        :rtype: Group
        """
        return Group(self.groups.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a group from the Groups collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Group to retrieve from he collection
                |             of groups. As a numerics, this index is the rank of the Group in the
                |             collection. The index of the first Group in the collection is 1, and the index
                |             of the last Group is Count. As a string, it is the name you assigned to the
                |             Group. 
                | 
                |     Example:
                | 
                |              The following example removes the tenth Group and the Group
                |              named
                |             Group2 from the TheGroups collection.
                |             
                | 
                |             TheGroups.Remove(10)
                |             TheGroups.Remove("Group2")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.groups.Remove(i_index)

    def __getitem__(self, n: int) -> Group:
        if (n + 1) > self.count:
            raise StopIteration

        return Group(self.groups.Item(n + 1))

    def __iter__(self) -> Iterator[Group]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Groups(name="{self.name}")'
