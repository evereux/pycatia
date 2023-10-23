#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_manager import AnalysisManager
from pycatia.in_interfaces.document import Document


class AnalysisDocument(Document):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Document
                |                         AnalysisDocument
                | 
                | Represents the document object for analysis.
                | This objects is used for all CAE applications to defines specifications and
                | managed associated results.
                | The document for analysis data is typed as ".CATAnalysis".
                | When an analysis document object is created, an analysis manager is also
                | created.
                | This analysis manager is the root object at the top of the structure of the
                | Analysis document.
                | 
                | See also:
                |     Document
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_document = com_object

    @property
    def analysis(self) -> AnalysisManager:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Analysis() As AnalysisManager (Read Only)
                | 
                |     Returns the root analysis object from the current analysis
                |     document.
                | 
                |     Example:
                |         The following example returns in RootAnalysis the root analysis object
                |         of the active document, assumed to be an analysis
                |         document:
                | 
                |          Dim AnalysisDocument As Document
                |          Set AnalysisDocument = CATIA.ActiveDocument
                |          Dim RootAnalysis As AnalysisManager
                |          Set RootAnalysis = AnalysisDocument.Analysis

        :rtype: AnalysisManager
        """

        return AnalysisManager(self.analysis_document.Analysis)

    def __repr__(self):
        return f'AnalysisDocument(name="{self.name}")'
