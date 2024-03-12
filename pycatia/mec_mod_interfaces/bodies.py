#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.mec_mod_interfaces.body import Body
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Bodies(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Bodies
                |
                | A collection of all the Body objects contained in the part.

    """

    def __init__(self, collection_com_object):
        super().__init__(collection_com_object, child_object=Body)
        self.bodies = collection_com_object

    def add(self) -> Body:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add() As Body
                | 
                |     Creates a new body and adds it to the Bodies collection. This body becomes
                |     the current one
                | 
                |     Returns:
                |         The created body 
                |     Example:
                |         The following example creates a body names NewBody in the body
                |         collection of the rootPart part in the partDoc part document. NewBody becomes
                |         the current body in partDoc.
                | 
                |          Set rootPart = partDoc.Part
                |          Set NewBody = rootPart.Bodies.Add()

        :rtype: Body
        """
        return Body(self.bodies.Add())

    def item(self, i_index: cat_variant) -> Body:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Body
                | 
                |     Returns a body using its index or its name from the Bodies
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the body to retrieve from the collection
                |             of bodies. As a numerics, this index is the rank of the body in the collection.
                |             The index of the first body in the collection is 1, and the index of the last
                |             body is Count. As a string, it is the name you assigned to the body using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved body 
                |     Example:
                |         This example retrieves in ThisBody the fifth body in the collection and
                |         in ThatBody the body named MyBody in the body collection of the partDoc part
                |         document.
                | 
                |          Set BodyColl = partDoc.Part.Bodies
                |          Set ThisBody = BodyColl.Item(5)
                |          Set ThatBody = BodyColl.Item("MyBody")

        :param cat_variant i_index:
        :rtype: Body
        """
        return Body(self.bodies.Item(i_index))

    def __getitem__(self, n: int) -> Body:
        if (n + 1) > self.count:
            raise StopIteration

        return Body(self.bodies.Item(n + 1))

    def __iter__(self) -> Iterator[Body]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Bodies(name="{self.name}")'
