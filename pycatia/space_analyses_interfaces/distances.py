#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.space_analyses_interfaces.distance import Distance
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Distances(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Distances
                | 
                | A collection of all Distance objects currently managed by the
                | application.
                | 
                | The method GetTechnologicalObject("Distances") on the root product, allows you
                | to retrieve this collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Distance)
        self.distances = com_object

    def add(self) -> Distance:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add() As Distance
                | 
                |     Creates a Distance object which takes all products of the document into
                |     account and adds it to the Distances collection.
                | 
                |     Returns:
                |         The created Distance 
                |     Example:
                | 
                |              This example creates a new Distance in the TheDistances
                |              collection.
                |
                |             Dim NewDistance As Distance
                |             Set NewDistance = TheDistances.Add

        :rtype: Distance
        """
        return Distance(self.distances.Add())

    def add_from_sel(self) -> Distance:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func AddFromSel() As Distance
                | 
                |     Creates a Distance object which takes all products in the selection into
                |     account and adds it to the Distances collection.
                | 
                |     Returns:
                |         The created Distance 
                |     Example:
                | 
                |              This example creates a new Distance in the TheDistances
                |              collection.
                |
                |             Dim NewDistance As Distance
                |             Set NewDistance = TheDistances.AddFromSel

        :rtype: Distance
        """
        return Distance(self.distances.AddFromSel())

    def item(self, i_index: cat_variant) -> Distance:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As Distance
                | 
                |     Returns a Distance object using its index or its name from the Distances
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Distance to retrieve from the
                |             collection of Distances. As a numerics, this index is the rank of the Distance
                |             in the collection. The index of the first Distance in the collection is 1, and
                |             the index of the last Distance is Count. As a string, it is the name you
                |             assigned to the Distance. 
                | 
                |     Example:
                | 
                |              This example retrieves in ThisDistance the ninth
                |              Distance,
                |             and in ThatDistance the Distance named
                |             Distance Of MyProduct from the TheDistances collection.
                |
                |             Dim ThisDistance As Distance
                |             Set ThisDistance = TheDistances.Item(9)
                |             Dim ThatDistance As Distance
                |             Set ThatDistance = TheDistances.Item("Distance Of MyProduct")

        :param cat_variant i_index:
        :rtype: Distance
        """
        return Distance(self.distances.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a Distance object from the Distances collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Distance to remove from the collection
                |             of Distances. As a numerics, this index is the rank of the Distance in the
                |             collection. The index of the first Distance in the collection is 1, and the
                |             index of the last Distance is Count. As a string, it is the name you assigned
                |             to the Distance. 
                | 
                |     Example:
                | 
                |              The following example removes the tenth Distance and the Distance
                |              named
                |             Distance Of MyProduct from the TheDistances
                |             collection.
                |
                |             TheDistances.Remove(10)
                |             TheDistances.Remove("Distance Of MyProduct")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.distances.Remove(i_index)

    def __getitem__(self, n: int) -> Distance:
        if (n + 1) > self.count:
            raise StopIteration

        return Distance(self.distances.Item(n + 1))

    def __iter__(self) -> Iterator[Distance]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Distances(name="{self.name}")'
