#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.knowledge_interfaces.unit import Unit
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Units(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Units
                | 
                | Represents the collection of Units.
                | This collection can be retrieved via any collection of parameters (method
                | Units).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Unit)
        self.units = com_object

    def item(self, i_index: cat_variant) -> Unit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As Unit
                | 
                |     Returns a unit using its index or its name from the from the Parameters
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the unit to retrieve from the collection
                |             of parameters. As a numerics, this index is the rank of the unit in the
                |             collection. The index of the first unit in the collection is 1, and the index
                |             of the last parameter is Count. As a string, it is the name you assigned to the
                |             parameter using the 
                | 
                |         AnyObject.Name property or when creating the parameter.
                |         
                |     Example:
                |         This example retrieves the millimeter unit in the units
                |         collection:
                | 
                |          Set unitmm = units.Item("mm")

        :param cat_variant i_index:
        :rtype: Unit
        """
        return Unit(self.units.Item(i_index))

    def __getitem__(self, n: int) -> Unit:
        if (n + 1) > self.count:
            raise StopIteration

        return Unit(self.units.Item(n + 1))

    def __iter__(self) -> Iterator[Unit]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Units(name="{self.name}")'
