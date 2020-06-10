#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.collection import Collection
from .hybrid_body import HybridBody


class HybridBodies(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | A collection of the HybridBody objects.

    """

    def __init__(self, collection_com_object):
        super().__init__(collection_com_object, child_object=HybridBody)
        self.hybrid_bodies = collection_com_object

    def add(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Add
                | o Func Add() As HybridBody
                | 
                | Creates a new hybrid body and adds it to the HybridBodies collection.
                | This body becomes the current one
                | Returns:  The created body
                |
                | Example: The following example creates a body named newHybridBody in
                | the hybrid body collection of the rootPart part in the partDoc part
                | document. NewPartBody becomes the current body in partDoc.
                |
                | Set NewPartBody = rootPart.Bodies.AddPartBody()


        :return: HybridBody()
        """
        return self.child_object(self.hybrid_bodies.Add())

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(    CATVariant    iIndex) As HybridBody
                | 
                | Returns a body using its index or its name from the Bodies collection.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the hybrid body to retrieve from
                |    the collection of hybrid bodies.
                |    As a numeric, this index is the rank of the hybrid body
                |    in the collection.
                |    The index of the first hybrid body in the collection is 1, and
                |    the index of the last hybrid body is Count.
                |    As a string, it is the name you assigned to the hybrid body using
                |    the 
                | 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property. 
                |    Returns:
                |   The retrieved hybrid body
                |
                | Examples:
                | 
                | 
                | This example retrieves in ThisHybridBody the fifth hybrid body
                | in the collection and in ThatHybridBody the hybrid body
                | named MyHybridBody in the hybrid body collection of the partDoc
                | part document.
                | 
                | Set hybridBodyColl = partDoc.Part.HybridBodies
                | Set ThisHybridBody = hybridBodyColl.Item(5)
                | Set ThatHybridBody = hybridBodyColl.Item("MyHybridBody")


        """
        return HybridBody(self.hybrid_bodies.Item(i_index))

    def __repr__(self):
        return f'HybridBodies(name="{self.name}")'
