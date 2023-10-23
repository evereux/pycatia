#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class AnalysisLinkedDocuments(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AnalysisLinkedDocuments
                | 
                | The collection of Documents linked by Analysis.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_linked_documents = com_object

    def item(self, i_index: cat_variant) -> Document:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As Document
                | 
                |     Returns a Document by its index or its name from the linked Documents
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the linked Document to retrieve from the
                |             collection of linked Documents. As a numerics, this index is the rank of the
                |             linked Document in the collection. The index of the first linked Document in
                |             the collection is 1, and the index of the last linked Document is Count. As a
                |             string, it is the name you assigned to the collection by using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved linked Document

        :param cat_variant i_index:
        :rtype: Document
        """
        return Document(self.analysis_linked_documents.Item(i_index))

    def __repr__(self):
        return f'AnalysisLinkedDocuments(name="{self.name}")'
