#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.general_knowledge_interfaces.expert_rule_base_component_runtime import ExpertRuleBaseComponentRuntime

if TYPE_CHECKING:
    from pycatia.general_knowledge_interfaces.expert_rule import ExpertRule


class ExpertRuleRuntime(ExpertRuleBaseComponentRuntime):
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
                |                         ExpertRuleRuntime
                | 
                | Represents the ExpertRuleRuntime object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.expert_rule_runtime = com_object

    @property
    def priority(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Priority() As double
                | 
                |     Returns or sets the priority of the rule. The priority of expert rules
                |     indicates the order in which the rules are evaluated. Rules with the same
                |     priority are evaluated in the order of their creation.

        :rtype: float
        """

        return self.expert_rule_runtime.Priority

    @priority.setter
    def priority(self, value: float):
        """
        :param float value:
        """

        self.expert_rule_runtime.Priority = value

    @property
    def rule_edition(self) -> 'ExpertRule':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RuleEdition() As ExpertRule (Read Only)
                | 
                |     Returns the editable object corresponding to this rule. Be careful that, according to your licence, or the type of rule you're handling, you may not have the right to edit the rule. Dim aRuleEdition As ExpertRule Set aRuleEdition = aRuleRuntime.RuleEdition If not(aRuleEdition is Nothing) Then CATIA.SystemService.Print aRuleEdition.Body End if

        :rtype: ExpertRule
        """
        
        from pycatia.general_knowledge_interfaces.expert_rule import ExpertRule
        return ExpertRule(self.expert_rule_runtime.RuleEdition)

    def __repr__(self):
        return f'ExpertRuleRuntime(name="{self.name}")'
