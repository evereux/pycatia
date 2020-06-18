#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.space_analyses_interfaces.clash_result import ClashResult
from pycatia.system_interfaces.collection import Collection


class ClashResults(Collection):

    """
        .. note::
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

    def add_from_xml(self, i_path=None, i_type=None):
        """
        .. note::
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
                | 
                |             Dim NewClashResult As ClashResult
                |             Set NewClashResult = TheClashResults.AddFromXML("c:\\tmp\\sample.xml",
                |                                                              CatClashImportTypeClashOnly)

        :param str i_path:
        :param CatClashImportType i_type:
        :return: ClashResult
        """
        return ClashResult(self.clash_results.AddFromXML(i_path, i_type.com_object))

    def item(self, i_index=None):
        """
        .. note::
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
                |             
                | 
                |             Dim ThisClashResult As ClashResult
                |             Set ThisClashResult = TheClashResults.Item(9)
                |             Dim ThatClashResult As ClashResult
                |             Set ThatClashResult = TheClashResults.Item("ClashResult Of MyProduct")

        :param CATVariant i_index:
        :return: ClashResult
        """
        return ClashResult(self.clash_results.Item(i_index.com_object))

    def remove(self, i_index=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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
                | 
                |             TheClashResults.Remove(10)
                |             TheClashResults.Remove("ClashResult Of MyProduct")

        :param CATVariant i_index:
        :return: None
        """
        return self.clash_results.Remove(i_index.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(clash_results)
        # #     Dim iIndex (2)
        # #     clash_results.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ClashResults(name="{ self.name }")'
