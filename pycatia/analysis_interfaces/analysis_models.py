#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_model import AnalysisModel
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class AnalysisModels(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AnalysisModels
                | 
                | The collection of analysis models making an analysis document.
                | As of today this collection is made of a single analysis
                | model.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AnalysisModel)
        self.analysis_models = com_object

    def item(self, i_index: cat_variant) -> AnalysisModel:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As AnalysisModel
                | 
                |     Returns an analysis model using its index or its name from the analysis
                |     model collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the analysis model to retrieve from the
                |             collection of analysis model. As a numerics, this index is the rank of the
                |             analysis model in the collection. The index of the first analysis model in the
                |             collection is 1, and the index of the last analysis model is Count. As a
                |             string, it is the name you assigned to the analysis model using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved analysis model 
                |     Example:
                |         The following example retrieves the first analysis model in the
                |         analysis model collection of the AnalysisManager
                |         object.
                | 
                |          Dim AnalysisDocument As Document
                |          Set AnalysisDocument = CATIA.ActiveDocument
                |          Dim RootAnalysis As AnalysisManager
                |          Set RootAnalysis = AnalysisDocument.Analysis
                |          Dim analysisModels As AnalysisModels
                |          Set analysisModels = RootAnalysis.AnalysisModels
                |          Dim analysisModel As AnalysisModel
                |          Set AnalysisModel = analysisModel.Item(1)

        :param cat_variant i_index:
        :rtype: AnalysisModel
        """
        return AnalysisModel(self.analysis_models.Item(i_index))

    def __repr__(self):
        return f'AnalysisModels(name="{self.name}")'
