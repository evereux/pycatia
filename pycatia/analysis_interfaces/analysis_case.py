#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_set import AnalysisSet
from pycatia.analysis_interfaces.analysis_sets import AnalysisSets
from pycatia.system_interfaces.any_object import AnyObject


class AnalysisCase(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnalysisCase
                | 
                | Represent the analysis case object.
                | Role: Interface designed to manage Analysis Case behavior.
                | In the Analysis document, an Analysis Case is the object dedicated to define
                | and manage the environment data necessary to run a computation. This
                | environment is made of sets.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_case = com_object

    @property
    def analysis_sets(self) -> AnalysisSets:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisSets() As AnalysisSets (Read Only)
                | 
                |     Returns the analysis sets collection associated to the analysis
                |     case.
                | 
                |     Returns:
                |         The collection of analysis sets. 
                |     Example:
                |         The following example retrieves the analysis sets collection
                |         ListSets
                | 
                |          Dim MyCase As AnalysisCase
                |          Dim ListSets As AnalysisSets
                |          Set ListSets = MyCase.AnalysisSets

        :rtype: AnalysisSets
        """

        return AnalysisSets(self.analysis_case.AnalysisSets)

    def add_solution(self, i_solution_type: str) -> AnalysisSet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AddSolution(CATBSTR iSolutionType) As AnalysisSet
                | 
                |     Creates a Solution set defined by its type in the Case.
                | 
                |     Parameters:
                | 
                |         iSolutionType
                |             The feature type of the solution set.
                |             This is a user defined type corresponding to the kind of
                |             computation. For example "StaticSet" 
                | 
                |     Returns:
                |         oSolution The analysis set created. 
                |     Example:
                |         The following example create a solution set ListSets
                | 
                |          Dim MyCase As AnalysisCase
                |          Dim Newsol As AnalysisSet
                |          Set Newsol = MyCase.AddSolution("StaticSet")

        :param str i_solution_type:
        :rtype: AnalysisSet
        """
        return AnalysisSet(self.analysis_case.AddSolution(i_solution_type))

    def compute(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Compute()
                | 
                |     Launch the computation (Update) of an analysis case. This step corresponds
                |     to the "Case Solution" option of the interactive command. 
                | Example:
                |     The following example launches the update of MyCase
                | 
                |      Dim MyCase As AnalysisCase
                |      MyCase.Compute

        :rtype: None
        """
        return self.analysis_case.Compute()

    def compute_mesh_only(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ComputeMeshOnly()
                | 
                |     Launch the computation (Update) of an analysis case. This method
                |     corresponds to the "Mesh Only" option of the interactive command.
                |     
                | Example:
                |     The following example launches the update of MyCase
                | 
                |      Dim MyCase As AnalysisCase
                |      MyCase.ComputeMeshOnly

        :rtype: None
        """
        return self.analysis_case.ComputeMeshOnly()

    def __repr__(self):
        return f'AnalysisCase(name="{self.name}")'
