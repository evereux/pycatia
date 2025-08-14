#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.in_interfaces.printer import Printer
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Printers(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Printers
                | 
                | A collection of all the Printer objects managed by the
                | application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Printer)
        self.printers = com_object

    def item(self, i_index: cat_variant) -> Printer:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As Printer
                | 
                |     Returns a printer using its index or its device name from the Printers
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the printer to retrieve from the
                |             collection of printers. As a numerics, this index is the rank of the printer in
                |             the collection. The index of the first printer in the collection is 1, and the
                |             index of the last printer is Count. As a string, it is the DeviceName of the
                |             printer. 
                | 
                |     Returns:
                |         The retrieved printer 
                |     Example:
                |         This example returns in ThisPrinter the third printer in the
                |         collection, and in ThatPrinter the printer named
                |         LaserPrinter.
                | 
                |          Dim ThisPrinter As Printer
                |          Set ThisPrinter = CATIA.Printers.Item(3)
                |          Dim ThatPrinter As Printer
                |          Set ThatPrinter = CATIA.Printers.Item("LaserPrinter")

        :param cat_variant i_index:
        :rtype: Printer
        """
        return Printer(self.printers.Item(i_index))

    def __getitem__(self, n: int) -> Printer:
        if (n + 1) > self.count:
            raise StopIteration

        return Printer(self.printers.Item(n + 1))

    def __iter__(self) -> Iterator[Printer]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Printers(name="{self.name}")'
