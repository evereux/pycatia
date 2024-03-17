#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
from typing import Iterator

from pycatia.mec_mod_interfaces.axis_system import AxisSystem
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class AxisSystems(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AxisSystems
                | 
                | A collection of all the AxisSystem objects contained in the
                | part.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AxisSystem)
        self.axis_systems = com_object

    def add(self) -> AxisSystem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Add() As AxisSystem
                | 
                |     Creates a new AxisSystem and adds it to the AxisSystems
                |     collection.
                | 
                |     Returns:
                |         The created AxisSystem 
                |     Example:
                |         The following example creates a AxisSystem names NewAxisSystem in the
                |         AxisSystem collection of the rootPart part in the partDoc part
                |         document.
                | 
                |          Set rootPart = partDoc.Part
                |          Set NewAxisSystem = rootPart.AxisSystems.Add()

        :rtype: AxisSystem
        """
        return AxisSystem(self.axis_systems.Add())

    def item(self, i_index: cat_variant) -> AxisSystem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As AxisSystem
                | 
                |     Returns an Axis System using its index or its name from the AxisSystems
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the AxisSystem to retrieve from the
                |             collection of AxisSystems. As a numerics, this index is the rank of the
                |             AxisSystem in the collection. The index of the first AxisSystem in the
                |             collection is 1, and the index of the last AxisSystem is Count. As a string, it
                |             is the name you assigned to the AxisSystem using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved AxisSystem 
                |     Example:
                |         This example retrieves in ThisAxisSystem the fifth AxisSystem in the
                |         collection and in ThatAxisSystem the AxisSystem named MyAxisSystem in the
                |         AxisSystem collection of the partDoc part document.
                | 
                |          Set AxisSystemColl = partDoc.Part.AxisSystems
                |          Set ThisAxisSystem = AxisSystemColl.Item(5)
                |          Set ThatAxisSystem = AxisSystemColl.Item("MyAxisSystem")

        :param cat_variant i_index:
        :rtype: AxisSystem
        """
        return AxisSystem(self.axis_systems.Item(i_index))

    def __getitem__(self, n: int) -> AxisSystem:
        if (n + 1) > self.count:
            raise StopIteration

        return AxisSystem(self.axis_systems.Item(n + 1))

    def __iter__(self) -> Iterator[AxisSystem]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'AxisSystems(name="{self.name}")'
