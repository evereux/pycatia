#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.general_knowledge_interfaces.expert_report_objects import ExpertReportObjects
from pycatia.general_knowledge_interfaces.expert_rule_base_component_runtime import ExpertRuleBaseComponentRuntime

if TYPE_CHECKING:
    from pycatia.general_knowledge_interfaces.expert_check import ExpertCheck


class ExpertCheckRuntime(ExpertRuleBaseComponentRuntime):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    GenKnowledgeInterfaces.ExpertRuleBaseComponentRuntime
                |                         ExpertCheckRuntime
                | 
                | Runtime part of a check.
                | The following example shows how to access the Check check1 from an existing
                | RuleSet RS1 of the RuleBase RB1.
                | 
                |  Dim CATDocs As Document
                |  Set CATDocs   = CATIA.Documents
                |  Dim partdoc As PartDocument
                |  Set partdoc   = CATDocs.Add("CATPart")
                |  Dim part As Part
                |  Set part      = partdoc.Part
                |  Dim relations As Relations
                |  Set relations = part.Relations
                |  Dim Rulebase As ExpertRuleBaseRuntime
                |  Set RuleBase  = relations.Item("RB1")
                |  Dim Ruleset As ExpertRuleSetRuntime
                |  Set RuleSet	 = RuleBase.RuleSet.ExpertRuleBaseComponentRuntimes.Item("RS1")
                |  Dim Check1 As ExpertCheckRuntime
                |  Set Check1	 = RuleSet.ExpertRuleBaseComponentRuntimes.Item("Check1")
                |  
                | 
                | See also:
                |     Relations, ExpertRuleBase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.expert_check_runtime = com_object

    @property
    def automatic_correct(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutomaticCorrect() As boolean
                | 
                |     Returns or sets the status of the automatic correction facility. When set
                |     to TRUE, the check automatically calls the user function defined by
                |     put_CorrectFunction when it fails.

        :rtype: bool
        """

        return self.expert_check_runtime.AutomaticCorrect

    @automatic_correct.setter
    def automatic_correct(self, value: bool):
        """
        :param bool value:
        """

        self.expert_check_runtime.AutomaticCorrect = value

    @property
    def check_edition(self) -> 'ExpertCheck':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CheckEdition() As ExpertCheck (Read Only)
                | 
                |     Returns the editable object corresponding to this check. Be careful that,
                |     according to your licence, or the type of check you're handling, you may not
                |     have the right to edit the check.
                | 
                |     Example:
                | 
                |          Dim aCheckEdition As ExpertCheck
                |          Set aCheckEdition = aCheckRuntime.CheckEdition
                | 
                |          If not(aCheckEdition is Nothing) Then
                |            CATIA.SystemService.Print aCheckEdition.Body
                |          End if

        :rtype: ExpertCheck
        """
        
        from pycatia.general_knowledge_interfaces.expert_check import ExpertCheck
        return ExpertCheck(self.expert_check_runtime.CheckEdition)

    @property
    def correct_function(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CorrectFunction() As CATBSTR
                | 
                |     Returns or sets the body to be called in order to correct the check.

        :rtype: str
        """

        return self.expert_check_runtime.CorrectFunction

    @correct_function.setter
    def correct_function(self, value: str):
        """
        :param str value:
        """

        self.expert_check_runtime.CorrectFunction = value

    @property
    def correct_function_comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CorrectFunctionComment() As CATBSTR
                | 
                |     Returns or sets the comment of the correct function of the check.

        :rtype: str
        """

        return self.expert_check_runtime.CorrectFunctionComment

    @correct_function_comment.setter
    def correct_function_comment(self, value: str):
        """
        :param str value:
        """

        self.expert_check_runtime.CorrectFunctionComment = value

    @property
    def correct_function_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CorrectFunctionType() As long
                | 
                |     Returns or sets the type of the body to be called in order to correct the
                |     check.
                | 
                |     1
                |         Visual Basic 
                |     2
                |         Comment 
                |     3
                |         Http 
                |     4
                |         User Function

        :rtype: int
        """

        return self.expert_check_runtime.CorrectFunctionType

    @correct_function_type.setter
    def correct_function_type(self, value: int):
        """
        :param int value:
        """

        self.expert_check_runtime.CorrectFunctionType = value

    @property
    def failures(self) -> ExpertReportObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Failures() As ExpertReportObjects (Read Only)
                | 
                |     Returns the list of the tuples that don't satisfy this check.

        :rtype: ExpertReportObjects
        """

        return ExpertReportObjects(self.expert_check_runtime.Failures)

    @property
    def help(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Help() As CATBSTR
                | 
                |     Returns or sets the contextual help of the check object.

        :rtype: str
        """

        return self.expert_check_runtime.Help

    @help.setter
    def help(self, value: str):
        """
        :param str value:
        """

        self.expert_check_runtime.Help = value

    @property
    def justification(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Justification() As CATBSTR
                | 
                |     Returns or sets the reason why the check was overridden.

        :rtype: str
        """

        return self.expert_check_runtime.Justification

    @justification.setter
    def justification(self, value: str):
        """
        :param str value:
        """

        self.expert_check_runtime.Justification = value

    @property
    def priority(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Priority() As double
                | 
                |     Returns or sets the priority of the check. The priority of expert checks
                |     indicates the order in which the checks are evaluated. Checks with the same
                |     priority are evaluated in the order of their creation.

        :rtype: float
        """

        return self.expert_check_runtime.Priority

    @priority.setter
    def priority(self, value: float):
        """
        :param float value:
        """

        self.expert_check_runtime.Priority = value

    @property
    def succeeds(self) -> ExpertReportObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Succeeds() As ExpertReportObjects (Read Only)
                | 
                |     Returns the list of the tuples that satisfy this check.

        :rtype: ExpertReportObjects
        """

        return ExpertReportObjects(self.expert_check_runtime.Succeeds)

    def correct(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Correct()
                | 
                |     Applies the "correction" function on failed elements.

        :rtype: None
        """
        return self.expert_check_runtime.Correct()

    def highlight(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Highlight()
                | 
                |     Highlights the Failures on the check.

        :rtype: None
        """
        return self.expert_check_runtime.Highlight()

    def status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Status() As long
                | 
                |     Returns the Status of the check.
                | 
                |     Example:
                | 
                |          Dim Check1 As ExpertCheck 
                |          Set Check1 = RuleSet.ExpertRuleBaseComponentRuntimes.Item("Check1")
                |          status = Check1.Status ()
                |          
                | 
                |     Returns:
                |         1=OK, 0=KO.

        :rtype: int
        """
        return self.expert_check_runtime.Status()

    def __repr__(self):
        return f'ExpertCheckRuntime(name="{self.name}")'
