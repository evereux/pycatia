#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_mesh_parts import AnalysisMeshParts
from pycatia.analysis_interfaces.analysis_set import AnalysisSet


class AnalysisMeshManager(AnalysisSet):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATAnalysisInterfaces.AnalysisSet
                |                         AnalysisMeshManager
                | 
                | The interface to access a CATIAAnalysisMeshManager.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_mesh_manager = com_object

    @property
    def analysis_mesh_parts(self) -> AnalysisMeshParts:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisMeshParts() As AnalysisMeshParts (Read
                | Only)
                | 
                |     Returns the meshpart collection from the current analysis mesh manager.

        :rtype: AnalysisMeshParts
        """

        return AnalysisMeshParts(self.analysis_mesh_manager.AnalysisMeshParts)

    def __repr__(self):
        return f'AnalysisMeshManager(name="{self.name}")'
