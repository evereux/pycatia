#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.space_analyses_interfaces.clash import Clash
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Clashes(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Clashes
                | 
                | A collection of all Clash objects currently managed by the
                | application.
                | 
                | The method GetTechnologicalObject("Clashes") on the root product, allows you to
                | retrieve this collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.clashes = com_object

    def add(self) -> Clash:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add() As Clash
                | 
                |     Creates a Clash object which takes all products into account and adds it to
                |     the Clashes collection.
                | 
                |     Returns:
                |         The created Clash 
                |     Example:
                | 
                |              This example creates a new Clash in the TheClashes
                |              collection.
                |
                |             Dim NewClash As Clash
                |             Set NewClash = TheClashes.Add

        :rtype: Clash
        """
        return Clash(self.clashes.Add())

    def add_from_sel(self) -> Clash:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddFromSel() As Clash
                | 
                |     Creates a Clash object which takes all products in the selection into
                |     account and adds it to the Clashes collection.
                | 
                |     Returns:
                |         The created Clash 
                |     Example:
                | 
                |              This example creates a new Clash in the TheClashes
                |              collection.
                |
                |             Dim NewClash As Clash
                |             Set NewClash = TheClashes.AddFromSel

        :rtype: Clash
        """
        return Clash(self.clashes.AddFromSel())

    def item(self, i_index: cat_variant) -> Clash:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Clash
                | 
                |     Returns a Clash object using its index or its name from the Clashes
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Clash to retrieve from the collection
                |             of Clashes. As a numerics, this index is the rank of the Clash in the
                |             collection. The index of the first Clash in the collection is 1, and the index
                |             of the last Clash is Count. As a string, it is the name you assigned to the
                |             Clash. 
                | 
                |     Example:
                | 
                |              This example retrieves in ThisClash the ninth
                |              Clash,
                |             and in ThatClash the Clash named
                |             Clash Of MyProduct from the TheClashes collection.
                |
                |             Dim ThisClash As Clash
                |             Set ThisClash = TheClashes.Item(9)
                |             Dim ThatClash As Clash
                |             Set ThatClash = TheClashes.Item("Clash Of MyProduct")

        :param cat_variant i_index:
        :rtype: Clash
        """
        return Clash(self.clashes.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a Clash object from the Clashes collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Clash to remove from the collection of
                |             Clashes. As a numerics, this index is the rank of the Clash in the collection.
                |             The index of the first Clash in the collection is 1, and the index of the last
                |             Clash is Count. As a string, it is the name you assigned to the Clash.
                |
                |     Example:
                | 
                |              The following example removes the tenth Clash and the Clash
                |              named
                |             Clash Of MyProduct from the TheClashes collection.
                |
                |             TheClashes.Remove(10)
                |             TheClashes.Remove("Clash Of MyProduct")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.clashes.Remove(i_index)

    def __getitem__(self, n: int) -> Clash:
        if (n + 1) > self.count:
            raise StopIteration

        return Clash(self.clashes.Item(n + 1))

    def __iter__(self) -> Iterator[Clash]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Clashes(name="{self.name}")'
