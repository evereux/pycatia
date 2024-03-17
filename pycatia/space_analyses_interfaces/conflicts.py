#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.space_analyses_interfaces.conflict import Conflict
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Conflicts(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Conflicts
                | 
                | A collection of all Conflict objects currently detected by a Clash
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.conflicts = com_object

    def item(self, i_index: cat_variant) -> Conflict:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Conflict
                | 
                |     Returns a Conflict object using its index from the Conflicts
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Conflict object to retrieve from the collection of
                |             Conflicts. As a numerics, this index is the rank of the Conflict in the
                |             collection. The index of the first Conflict in the collection is 1, and the
                |             index of the last Conflict is Count. 
                | 
                |     Example:
                | 
                |              This example retrieves in ThisConflict the ninth
                |              Conflict
                |             from the TheConflicts collection. 
                |
                |             Dim ThisConflict As Conflict
                |             Set ThisConflict = TheConflicts.Item(9)

        :param cat_variant i_index:
        :rtype: Conflict
        """
        return Conflict(self.conflicts.Item(i_index))

    def __getitem__(self, n: int) -> Conflict:
        if (n + 1) > self.count:
            raise StopIteration

        return Conflict(self.conflicts.Item(n + 1))

    def __iter__(self) -> Iterator[Conflict]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Conflicts(name="{self.name}")'
