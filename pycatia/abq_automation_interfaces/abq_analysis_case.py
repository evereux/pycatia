#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_display_groups import ABQDisplayGroups
from pycatia.abq_automation_interfaces.abq_global_element_assignment import ABQGlobalElementAssignment
from pycatia.abq_automation_interfaces.abq_jobs import ABQJobs
from pycatia.abq_automation_interfaces.abq_solution_case import ABQSolutionCase
from pycatia.abq_automation_interfaces.abq_steps import ABQSteps
from pycatia.system_interfaces.any_object import AnyObject


class ABQAnalysisCase(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAnalysisCase
                | 
                | Represents an Abaqus analysis case (ABQAnalysisCase) object.
                | 
                | Role: Access an Abaqus analysis case object or determine its properties. An
                | ABQAnalysisCase object contains the collection of Abaqus steps (ABQSteps ) and
                | Abaqus jobs ( ABQJobs ). An Abaqus analysis case object contains the data
                | required to manage and run an Abaqus finite element analysis.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_analysis_case = com_object

    @property
    def display_groups(self) -> ABQDisplayGroups:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DisplayGroups() As ABQDisplayGroups (Read Only)
                | 
                |     Returns the Abaqus display groups associated with this analysis
                |     case.
                | 
                |     Returns:
                |         The collection of display groups. 
                |     Example:
                |         The following example retrieves the Abaqus display group collection
                |         DisplayGroups in ListDisplayGroups.
                | 
                |          Dim MyCase As ABQAnalysisCase
                |          Dim ListDisplayGroups As ABQDisplayGroups
                |          Set ListDisplayGroups = MyCase.DisplayGroups

        :rtype: ABQDisplayGroups
        """

        return ABQDisplayGroups(self.abq_analysis_case.DisplayGroups)

    @property
    def global_elem_assignment(self) -> ABQGlobalElementAssignment:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlobalElemAssignment() As ABQGlobalElementAssignment (Read
                | Only)
                | 
                |     Returns the Global Element Assignement feature associated with this
                |     analysis case.
                | 
                |     Returns:
                |         The associated Global Element Assignement feature . 
                |     Example:
                |         The following example retrieves the Global Element Assignement feature
                |         collection GlobalElemAssignment in
                |         oGlobalElementAssignment.
                | 
                |          Dim MyCase As ABQAnalysisCase
                |          Dim GlobalElementAssignment As
                |          ABQGlobalElementAssignment
                |          Set GlobalElementAssignment = MyCase.GlobalElemAssignment

        :rtype: ABQGlobalElementAssignment
        """

        return ABQGlobalElementAssignment(self.abq_analysis_case.GlobalElemAssignment)

    @property
    def jobs(self) -> ABQJobs:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Jobs() As ABQJobs (Read Only)
                | 
                |     Returns the Abaqus jobs associated with this analysis
                |     case.
                | 
                |     Returns:
                |         The collection of jobs. 
                |     Example:
                |         The following example retrieves the Abaqus job collection Jobs in
                |         ListJobs.
                | 
                |          Dim MyCase As ABQAnalysisCase
                |          Dim ListJobs As ABQJobs
                |          Set ListJobs = MyCase.Jobs

        :rtype: ABQJobs
        """

        return ABQJobs(self.abq_analysis_case.Jobs)

    @property
    def solution_case(self) -> ABQSolutionCase:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SolutionCase() As ABQSolutionCase (Read Only)
                | 
                |     Returns the Abaqus solution case associated with this analysis
                |     case.
                | 
                |     Returns:
                |         The associated Abaqus solution case. 
                |     Example:
                |         The following example retrieves the Abaqus solution case collection
                |         SolutionCase in SolutionCase.
                | 
                |          Dim MyCase As ABQAnalysisCase
                |          Dim SolutionCase As ABQSolutionCase
                |          Set SolutionCase = MyCase.SolutionCase

        :rtype: ABQSolutionCase
        """

        return ABQSolutionCase(self.abq_analysis_case.SolutionCase)

    @property
    def steps(self) -> ABQSteps:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Steps() As ABQSteps (Read Only)
                | 
                |     Returns the Abaqus analysis steps associated with this analysis
                |     case.
                | 
                |     Returns:
                |         The collection of analysis steps. 
                |     Example:
                |         The following example retrieves the Abaqus analysis step collection
                |         Steps in ListSteps.
                | 
                |          Dim MyCase As ABQAnalysisCase
                |          Dim ListSteps As ABQSteps
                |          Set ListSteps = MyCase.Steps

        :rtype: ABQSteps
        """

        return ABQSteps(self.abq_analysis_case.Steps)

    def __repr__(self):
        return f'ABQAnalysisCase(name="{self.name}")'
