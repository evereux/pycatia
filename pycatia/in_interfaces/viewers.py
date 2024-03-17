#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.in_interfaces.viewer import Viewer
from pycatia.system_interfaces.collection import Collection


class Viewers(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Viewers
                | 
                | A collection of all the Viewer objects currently attached to a
                | window.
                | For a SpecsAndGeomWindow object, the viewer containing the geometry is the
                | first viewer, and the viewer containing the specification tree is the second
                | viewer.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Viewer)
        self.viewers = com_object

    def item(self, i_index: int) -> Viewer:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(long iIndex) As Viewer
                | 
                |     Returns a viewer using its index from the Viewers collection. The first
                |     item has the rank 1 in the collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the viewer to retrieve from the collection
                |             of viewers. As a numerics, this index is the rank of the viewer in the
                |             collection. The index of the first viewer in the collection is 1, and the index
                |             of the last viewer is Count. As a string, it is the name you assigned to the
                |             viewer using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved viewer 
                | 
                | Example:
                |     This example returns in MyViewer the second viewer in the
                |     collection.
                | 
                |      Dim MyViewer As Viewer
                |      Set MyViewer = Viewer.Item(2)

        :param int i_index:
        :rtype: Viewer
        """
        return Viewer(self.viewers.Item(i_index))

    def __getitem__(self, n: int) -> Viewer:
        if (n + 1) > self.count:
            raise StopIteration

        return Viewer(self.viewers.Item(n + 1))

    def __iter__(self) -> Iterator[Viewer]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Viewers(name="{self.name}")'
