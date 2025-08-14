#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.in_interfaces.window import Window
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Windows(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Windows
                | 
                | A collection of all the Window objects currently managed by the
                | application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Window)
        self.windows = com_object

    def arrange(self, i_style: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Arrange(CatArrangeStyle iStyle)
                | 
                |     Arranges all the windows of the collection.
                | 
                |     Parameters:
                | 
                |         iStyle
                |             The arrangement style to take into account to arrange the windows
                |             
                | 
                |     Example:
                |         The following example arranges all the windows in the Windows
                |         collection, according to the catArrangeCascade style.
                | 
                |          CATIA.Windows.Arrange(catArrangeCascade)

        :param int i_style: enum cat_arrange_style
        :rtype: None
        """
        return self.windows.Arrange(i_style)

    def item(self, i_index: cat_variant) -> Window:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Window
                | 
                |     Returns a window using its index or its name from the Windows
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the window to retrieve from the collection
                |             of windows. As a numerics, this index is the rank of the window in the
                |             collection. The index of the first window in the collection is 1, and the index
                |             of the last window is Count. As a string, it is the name you assigned to the
                |             window using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved window 
                |     Example:
                |         This example returns in ThisWindow the third window in the collection,
                |         and in ThatWindow the window named MyWindow.
                | 
                |          Dim ThisWindow As Window
                |          Set ThisWindow = CATIA.Windows.Item(3)
                |          Dim ThatWindow As Window
                |          Set ThatWindow = CATIA.Windows.Item("MyWindow")

        :param cat_variant i_index:
        :rtype: Window
        """
        return Window(self.windows.Item(i_index))

    def __getitem__(self, n: int) -> Window:
        if (n + 1) > self.count:
            raise StopIteration

        return Window(self.windows.Item(n + 1))

    def __iter__(self) -> Iterator[Window]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Windows(name="{self.name}")'
