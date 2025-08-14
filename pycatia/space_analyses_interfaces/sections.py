#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.space_analyses_interfaces.section import Section
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Sections(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Sections
                | 
                | A collection of all Section objects currently managed by the
                | application.
                | 
                | The method GetTechnologicalObject("Sections") on the root product, allows you
                | to retrieve this collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Section)
        self.sections = com_object

    def add(self) -> Section:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Add() As Section
                | 
                |     Creates a Section object which takes all products of the documents into
                |     account and adds it to the Sections collection.
                | 
                |     Returns:
                |         The created Section 
                |     Example:
                | 
                |              This example creates a new Section in the TheSections
                |              collection.
                |
                |             Dim NewSection As Section
                |             Set NewSection = TheSections.Add

        :rtype: Section
        """
        return Section(self.sections.Add())

    def add_from_sel(self) -> Section:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func AddFromSel() As Section
                | 
                |     Creates a Section object which takes all products in the selection into
                |     account and adds it to the Sections collection.
                | 
                |     Returns:
                |         The created Section 
                |     Example:
                | 
                |              This example creates a new Section in the TheSections
                |              collection.
                |
                |             Dim NewSection As Section
                |             Set NewSection = TheSections.AddFromSel

        :rtype: Section
        """
        return Section(self.sections.AddFromSel())

    def item(self, i_index: cat_variant) -> Section:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func Item(CATVariant iIndex) As Section
                | 
                |     Returns a Section object using its index or its name from the Sections
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Section to retrieve from the
                |             collection of Sections. As a numerics, this index is the rank of the Section in
                |             the collection. The index of the first Section in the collection is 1, and the
                |             index of the last Section is Count. As a string, it is the name you assigned to
                |             the Section. 
                | 
                |     Example:
                | 
                |              This example retrieves in ThisSection the ninth
                |              Section,
                |             and in ThatSection the Section named
                |             Section Of MyProduct from the TheSections collection.
                |
                |             Dim ThisSection As Section
                |             Set ThisSection = TheSections.Item(9)
                |             Dim ThatSection As Section
                |             Set ThatSection = TheSections.Item("Section Of MyProduct")

        :param cat_variant i_index:
        :rtype: Section
        """
        return Section(self.sections.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a Section object from the Sections collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Section to remove from the collection
                |             of Sections. As a numerics, this index is the rank of the Section in the
                |             collection. The index of the first Section in the collection is 1, and the
                |             index of the last Section is Count. As a string, it is the name you assigned to
                |             the Section. 
                | 
                |     Example:
                | 
                |              The following example removes the tenth Section and the Section
                |              named
                |             Section Of MyProduct from the TheSections
                |             collection.
                |
                |             TheSections.Remove(10)
                |             TheSections.Remove("Section Of MyProduct")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.sections.Remove(i_index)

    def __getitem__(self, n: int) -> Section:
        if (n + 1) > self.count:
            raise StopIteration

        return Section(self.sections.Item(n + 1))

    def __iter__(self) -> Iterator[Section]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Sections(name="{self.name}")'
