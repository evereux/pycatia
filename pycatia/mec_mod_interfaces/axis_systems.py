#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.system_interfaces.collection import Collection
from .axis_system import AxisSystem


class AxisSystems(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | A collection of all the AxisSystem objects contained in the part.

    """

    def __init__(self, collection_com_object):
        super().__init__(collection_com_object, child_object=AxisSystem)
        self.axis_systems = collection_com_object

    def add(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Add
                | o Func Add() As AxisSystem
                | 
                | Creates a new AxisSystem and adds it to the AxisSystems collection.
                | Returns:  The created AxisSystem  Example: The following example
                | creates a AxisSystem names NewAxisSystem in the AxisSystem collection
                | of the rootPart part in the partDoc part document.  Set rootPart =
                | partDoc.Part Set NewAxisSystem = rootPart.AxisSystems.Add()


                | Parameters:


        """
        return self.child_object(self.axis_systems.Add())

    def item(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(    CATVariant    iIndex) As AxisSystem
                | 
                | Returns an Axis System using its index or its name from the
                | AxisSystems collection.


                | Parameters:
                | iIndex
                |    The index or the name of the AxisSystem to retrieve from
                |    the collection of AxisSystems.
                |    As a numeric, this index is the rank of the AxisSystem
                |    in the collection.
                |    The index of the first AxisSystem in the collection is 1, and
                |    the index of the last AxisSystem is Count.
                |    As a string, it is the name you assigned to the AxisSystem using
                |    the 
                | 
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property. 
                |    Returns:
                |   The retrieved AxisSystem


                | Examples:
                | 
                | 
                | This example retrieves in ThisAxisSystem the fifth AxisSystem
                | in the collection and in ThatAxisSystem the AxisSystem
                | named MyAxisSystem in the AxisSystem collection of the partDoc
                | part document.
                | 
                | Set AxisSystemColl = partDoc.Part.AxisSystems
                | Set ThisAxisSystem = AxisSystemColl.Item(5)
                | Set ThatAxisSystem = AxisSystemColl.Item("MyAxisSystem")

        """
        return self.child_object(self.axis_systems.Item(i_index))

    def __repr__(self):
        return f'AxisSystems()'
