#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_adaptivity_manager import AnalysisAdaptivityManager
from pycatia.analysis_interfaces.analysis_cases import AnalysisCases
from pycatia.analysis_interfaces.analysis_mesh_manager import AnalysisMeshManager
from pycatia.analysis_interfaces.analysis_post_manager import AnalysisPostManager
from pycatia.analysis_interfaces.analysis_sets import AnalysisSets
from pycatia.system_interfaces.any_object import AnyObject


class AnalysisModel(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnalysisModel
                | 
                | Represent the analysis model object.
                | Role: In the analysis document, an analysis model is the object dedicated to
                | set and manage all the required data for the discretization and idealization of
                | a Finite Element model.
                | This object gives access to:
                | 
                |     A collection of AnalysisCase.
                |     A collection of AnalysisSets (All the input sets like properties,
                |     groups).
                |     A AnalysisPostManager object for reporting.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_model = com_object

    @property
    def adaptivity_manager(self) -> AnalysisAdaptivityManager:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AdaptivityManager() As AnalysisAdaptivityManager (Read
                | Only)
                | 
                |     Returns the AdaptivityManager defined on the analysis
                |     model.
                | 
                |     Returns:
                |         a CATIAAnalysisAdaptivityManager.

        :rtype: AnalysisAdaptivityManager
        """

        return AnalysisAdaptivityManager(self.analysis_model.AdaptivityManager)

    @property
    def analysis_cases(self) -> AnalysisCases:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisCases() As AnalysisCases (Read Only)
                | 
                |     Returns the collection of analysis cases defined on the analysis
                |     model.
                | 
                |     Returns:
                |         oAnalysisCases Collection of cases.

        :rtype: AnalysisCases
        """

        return AnalysisCases(self.analysis_model.AnalysisCases)

    @property
    def analysis_sets(self) -> AnalysisSets:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisSets() As AnalysisSets (Read Only)
                | 
                |     Returns the analysis sets collection associated with a analysis
                |     model.
                | 
                |     Returns:
                |         a collection of CATIAAnalysisSets.

        :rtype: AnalysisSets
        """

        return AnalysisSets(self.analysis_model.AnalysisSets)

    @property
    def mesh_manager(self) -> AnalysisMeshManager:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MeshManager() As AnalysisMeshManager (Read Only)
                | 
                |     Returns the MeshManager defined on the analysis model.
                | 
                |     Returns:
                |         a CATIAAnalysisMeshManager.

        :rtype: AnalysisMeshManager
        """

        return AnalysisMeshManager(self.analysis_model.MeshManager)

    @property
    def post_manager(self) -> AnalysisPostManager:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PostManager() As AnalysisPostManager (Read Only)
                | 
                |     Returns the Postprocessing manager defined on the analysis
                |     model.
                | 
                |     Returns:
                |         oPostManager the AnalysisPostManager Object.

        :rtype: AnalysisPostManager
        """

        return AnalysisPostManager(self.analysis_model.PostManager)

    def run_transition(self, i_transition_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RunTransition(CATBSTR iTransitionName)
                | 
                |     Apply a transition to the analysis model.
                | 
                |     Parameters:
                | 
                |         Transition
                |             name.

        :param str i_transition_name:
        :rtype: None
        """
        return self.analysis_model.RunTransition(i_transition_name)

    def __repr__(self):
        return f'AnalysisModel(name="{self.name}")'
