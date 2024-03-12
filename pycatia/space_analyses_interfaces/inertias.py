#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.space_analyses_interfaces.inertia import Inertia
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Inertias(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Inertias
                | 
                | A collection of all inertia objects currently managed by the
                | application.
                | 
                | WARNING: this collection will be DEPRECATED in the next release. It is
                | recommended to use the method GetTechnologicalObject("Inertia") on the product
                | to analyze, to retrieve an Inertia object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Inertia)
        self.inertias = com_object

    def add(self, i_object: AnyObject) -> Inertia:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add(AnyObject iObject) As Inertia
                | 
                |     Creates an Inertia object from an object and adds it to the Inertias
                |     collection.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The Object 
                | 
                |     Returns:
                |         The created Inertia 
                |     Example:
                | 
                |              This example creates a new Inertia from a product
                |              TheProduct
                |             in the TheInertias collection.
                |
                |             Dim NewInertia As Inertia
                |             Set NewInertia = TheInertias.Add(TheProduct)

        :param AnyObject i_object:
        :rtype: Inertia
        """
        return Inertia(self.inertias.Add(i_object.com_object))

    def item(self, i_index: cat_variant) -> Inertia:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Inertia
                | 
                |     Returns an Inertia object using its index or its name from the Inertias
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Inertia to retrieve from the
                |             collection of inertias. As a numerics, this index is the rank of the Inertia in
                |             the collection. The index of the first Inertia in the collection is 1, and the
                |             index of the last Inertia is Count. As a string, it is the name you assigned to
                |             the Inertia. 
                | 
                |     Example:
                | 
                |              This example retrieves in ThisInertia the ninth
                |              Inertia,
                |             and in ThatInertia the Inertia named
                |             Inertia Of MyProduct from the TheInertias collection.
                |
                |             Dim ThisInertia As Inertia
                |             Set ThisInertia = TheInertias.Item(9)
                |             Dim ThatInertia As Inertia
                |             Set ThatInertia = TheInertias.Item("Inertia Of MyProduct")

        :param cat_variant i_index:
        :rtype: Inertia
        """
        return Inertia(self.inertias.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an Inertia object from the Inertias collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Inertia to remove from the collection
                |             of inertias. As a numerics, this index is the rank of the Inertia in the
                |             collection. The index of the first Inertia in the collection is 1, and the
                |             index of the last Inertia is Count. As a string, it is the name you assigned to
                |             the Inertia. 
                | 
                |     Example:
                | 
                |              The following example removes the tenth Inertia and the Inertia
                |              named
                |             Inertia Of MyProduct from the TheInertias
                |             collection.
                |
                |             TheInertias.Remove(10)
                |             TheInertias.Remove("Inertia Of MyProduct")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.inertias.Remove(i_index)

    def __getitem__(self, n: int) -> Inertia:
        if (n + 1) > self.count:
            raise StopIteration

        return Inertia(self.inertias.Item(n + 1))

    def __iter__(self) -> Iterator[Inertia]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Inertias(name="{self.name}")'
