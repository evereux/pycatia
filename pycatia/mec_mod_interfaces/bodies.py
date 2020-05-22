#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.collection import Collection
from .body import Body


class Bodies(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | A collection of all the Body objects contained in the part.

    """

    def __init__(self, collection_com_object):
        super().__init__(collection_com_object, child_object=Body)
        self.bodies = collection_com_object

    def add(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Add
                | o Func Add(    ) As Body
                | 
                | Creates a new body and adds it to the Bodies collection. This body
                | becomes the current one  Returns:  The created body
                |
                | Example:
                | The following example creates a body names NewBody in the body collection
                | of the rootPart part in the partDoc part document. NewBody becomes the
                | current body in partDoc.
                | Set rootPart = partDoc.Part
                | Set NewBody = rootPart.Bodies.Add()

        """
        return self.child_object(self.bodies.Add())

    def item(self, i_index):
        """

        .. warning::

            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.

        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(    CATVariant    iIndex) As Body
                | 
                | Returns a body using its index or its name from the Bodies collection.


                | Parameters:
                | iIndex
                |    The index or the name of the body to retrieve from
                |    the collection of bodies.
                |    As a numeric, this index is the rank of the body
                |    in the collection.
                |    The index of the first body in the collection is 1, and
                |    the index of the last body is Count.
                |    As a string, it is the name you assigned to the body using
                |    the 
                | 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property. 
                |    Returns:
                |   The retrieved body
                |
                | Examples:
                | This example retrieves in ThisBody the fifth body
                | in the collection and in ThatBody the body
                | named MyBody in the body collection of the partDoc
                | part document.
                | 
                | Set BodyColl = partDoc.Part.Bodies
                | Set ThisBody = BodyColl.Item(5)
                | Set ThatBody = BodyColl.Item("MyBody")

        :return: Body()
        """

        if isinstance(i_index, int):
            i_index += 1
        return self.child_object(self.bodies.Item(i_index))

    def __repr__(self):
        return f'Bodies(name="{self.name}")'
