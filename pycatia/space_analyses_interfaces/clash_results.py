#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia.space_analyses_interfaces.clash_result import ClashResult
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ClashResults(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ClashResults
                | 
                | A collection of all ClashResult objects currently managed by the
                | application.
                | 
                | The results linked to a specification are not managed thru this collection (see
                | Clashes ).
                | 
                | The method GetTechnologicalObject("ClashResults") on the root product, allows
                | you to retrieve this collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.clash_results = com_object

    def add_from_xml(self, i_path: str, i_type: int) -> ClashResult:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func AddFromXML(CATBSTR iPath,
                | CatClashImportType iType) As ClashResult
                | 
                |     Creates a ClashResult object from a XML file and adds it to the
                |     ClashResults collection.
                | 
                |     Parameters:
                | 
                |         iPath
                |             The path of the XML file. 
                |         iType
                |             The type of import. 
                | 
                |     Returns:
                |         The created ClashResult 
                |     Example:
                | 
                |              This example creates a new ClashResult in the TheClashResults
                |              collection.
                |
                |             Dim NewClashResult As ClashResult
                |             Set NewClashResult = TheClashResults.AddFromXML("c:\\tmp\\sample.xml",
                |                                                              CatClashImportTypeClashOnly)

        :param str i_path:
        :param int i_type: enum cat_clash_import_type
        :rtype: ClashResult
        """
        return ClashResult(self.clash_results.AddFromXML(i_path, i_type))

    def item(self, i_index: cat_variant) -> ClashResult:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As ClashResult
                | 
                |     Returns a ClashResult object using its index or its name from the
                |     ClashResults collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ClashResult to retrieve from the
                |             collection of ClashResults. As a numerics, this index is the rank of the
                |             ClashResult in the collection. The index of the first ClashResult in the
                |             collection is 1, and the index of the last ClashResult is Count. As a string,
                |             it is the name you assigned to the ClashResult. 
                | 
                |     Example:
                | 
                |              This example retrieves in ThisClashResult the ninth
                |              ClashResult,
                |             and in ThatClashResult the ClashResult named
                |             ClashResult Of MyProduct from the TheClashResults collection.
                |
                |             Dim ThisClashResult As ClashResult
                |             Set ThisClashResult = TheClashResults.Item(9)
                |             Dim ThatClashResult As ClashResult
                |             Set ThatClashResult = TheClashResults.Item("ClashResult Of MyProduct")

        :param cat_variant i_index:
        :rtype: ClashResult
        """
        return ClashResult(self.clash_results.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a ClashResult object from the ClashResults
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ClashResult to remove from the
                |             collection of ClashResults. As a numerics, this index is the rank of the
                |             ClashResult in the collection. The index of the first ClashResult in the
                |             collection is 1, and the index of the last ClashResult is Count. As a string,
                |             it is the name you assigned to the ClashResult. 
                | 
                |     Example:
                | 
                |              The following example removes the tenth ClashResult and the
                |              ClashResult named
                |             ClashResult Of MyProduct from the TheClashResults
                |             collection.
                |
                |             TheClashResults.Remove(10)
                |             TheClashResults.Remove("ClashResult Of MyProduct")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.clash_results.Remove(i_index)

    def __getitem__(self, n: int) -> ClashResult:
        if (n + 1) > self.count:
            raise StopIteration

        return ClashResult(self.clash_results.Item(n + 1))

    def __iter__(self) -> Iterator[ClashResult]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'ClashResults(name="{self.name}")'
