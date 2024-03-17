#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.drafting_interfaces.drawing_thread import DrawingThread
from pycatia.system_interfaces.collection import Collection


class DrawingThreads(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingThreads
                | 
                | A collection of all the drawing threads currently managed by a drawing view of
                | drawing sheet in a drawing document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingThread)
        self.drawing_threads = com_object

    # todo: ascertain the correct type for i_geom_elem
    def add(self, i_geom_elem) -> DrawingThread:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add(CATBaseDispatch iGeomElem) As DrawingThread
                | 
                |     Creates a drawing thread and adds it to the DrawingThreads
                |     collection.
                | 
                |     Parameters:
                | 
                |         iGeomElem
                |             Geometry to create the thread on. Be careful, this geometry must be
                |             a 2D geometry 
                | 
                |     Returns:
                |         The created drawing thread 
                | 
                | Example:
                |     The following example creates a drawing thread and retrieved in MyThread in
                |     the drawing view collection of the MyView drawing view. This view belongs to
                |     the drawing view collection of the drawing sheet
                | 
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim MyThread As DrawingThread
                |      Set MyThread = MyView.Threads.Add(iGeomElem)

        :param i_geom_elem:
        :rtype: DrawingThread
        """
        return DrawingThread(self.drawing_threads.Add(i_geom_elem.com_object))

    def item(self, i_index: int) -> DrawingThread:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(long iIndex) As DrawingThread
                | 
                |     Returns a drawing thread using its index from the DrawingThreads
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing thread to retrieve from the collection of
                |             drawing threads. As a numerics, this index is the rank of the drawing thread in
                |             the collection. The index of the first drawing thread in the collection is 1,
                |             and the index of the last drawing thread is Count.
                |             
                | 
                |     Returns:
                |         The retrieved drawing thread 
                |     Example:
                |         This example retrieves in ThisDrawingThread the second drawing thread,
                |         in the drawing view collection of the active view in the active sheet, in the
                |         active document supposed to be a drawing document.
                | 
                |          Dim MyView  As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          Dim ThisDrawingThread As DrawingThread
                |          Set ThisDrawingThread = MyView.Threads.Item(2)

        :param int i_index:
        :rtype: DrawingThread
        """
        return DrawingThread(self.drawing_threads.Item(i_index))

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(long iIndex)
                | 
                |     Removes a drawing thread from the DrawingThreads
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing thread to remove from the collection of
                |             drawing threads. As a numerics, this index is the rank of the drawing thread in
                |             the collection. The index of the first drawing thread in the collection is 1,
                |             and the index of the last drawing thread is Count.
                |             
                | 
                |     Example:
                |         The following example removes the third drawing thread in the drawing
                |         thread collection of the active view of the active document, supposed to be a
                |         drawing document.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.DrawingThreads.Remove(3)

        :param int i_index:
        :rtype: None
        """
        return self.drawing_threads.Remove(i_index)

    def __getitem__(self, n: int) -> DrawingThread:
        if (n + 1) > self.count:
            raise StopIteration

        return DrawingThread(self.drawing_threads.Item(n + 1))

    def __iter__(self) -> Iterator[DrawingThread]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'DrawingThreads(name="{self.name}")'
