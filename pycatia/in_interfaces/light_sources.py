#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.in_interfaces.light_source import LightSource
from pycatia.system_interfaces.collection import Collection


class LightSources(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     LightSources
                | 
                | A collection of all the LightSource objects.
                | This collection is currently managed by a Viewer3D object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=LightSource)
        self.light_sources = com_object

    def add(self) -> LightSource:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add() As LightSource
                | 
                |     Adds a new light source to the LightSources collection. 
                | 
                | Example:
                |     The following adds a light source to the collection attached to the active
                |     viewer. This viewer must be a @see Viewer3D object.
                | 
                |      Dim MyViewer As Viewer
                |      Set MyViewer = CATIA.ActiveWindow.ActiveViewer
                |      Dim MyLightSource As LightSource
                |      Set MyLightSource = MyViewer.LightSources.Add

        :rtype: LightSource
        """
        return LightSource(self.light_sources.Add())

    def item(self, i_index: int) -> LightSource:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(long iIndex) As LightSource
                | 
                |     Returns a light source from its index in the LightSources
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the light source to retrieve in the collection of
                |             light sources. Compared with other collections, you cannot use the name of the
                |             light source as argument. 
                | 
                |     Returns:
                |         The retrieved light source 
                | 
                | Example:
                |     The following example returns in MyLightSource the sixth light source in
                |     the collection.
                | 
                |      Dim MyLightSource As LightSource
                |      Set MyLightSource = LightSources.Item(6)

        :param int i_index:
        :rtype: LightSource
        """
        return LightSource(self.light_sources.Item(i_index))

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(long iIndex)
                | 
                |     Removes a light source from the LightSources collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the light source to remove. Compared with other
                |             collections, you cannot use the name of the light source as argument.
                |             
                | 
                |     Example:
                |         The following example removes the second light source in the collection
                |         attached to the active viewer. This viewer must be a 
                | 
                |     Viewer3D object.
                | 
                |      Dim MyViewer As Viewer
                |      Set MyViewer = CATIA.ActiveWindow.ActiveViewer
                |      MyViewer.LightSources.Remove(2)

        :param int i_index:
        :rtype: None
        """
        return self.light_sources.Remove(i_index)

    def __getitem__(self, n: int) -> LightSource:
        if (n + 1) > self.count:
            raise StopIteration

        return LightSource(self.light_sources.Item(n + 1))

    def __iter__(self) -> Iterator[LightSource]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'LightSources(name="{self.name}")'
