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
from pycatia.general_knowledge_interfaces.expert_rule_base_component_runtimes import ExpertRuleBaseComponentRuntimes

if TYPE_CHECKING:
    from pycatia.general_knowledge_interfaces.expert_rule_set import ExpertRuleSet


class ExpertRuleSetRuntime(ExpertRuleBaseComponentRuntime):
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
                |                         ExpertRuleSetRuntime
                | 
                | Represents the ExpertRuleSet object in the RelationSet.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.expert_rule_set_runtime = com_object

    @property
    def expert_rule_base_component_runtimes(self) -> ExpertRuleBaseComponentRuntimes:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExpertRuleBaseComponentRuntimes() As
                | ExpertRuleBaseComponentRuntimes (Read Only)
                | 
                |     Returns the list of the RuleBaseComponent.

        :rtype: ExpertRuleBaseComponentRuntimes
        """

        return ExpertRuleBaseComponentRuntimes(self.expert_rule_set_runtime.ExpertRuleBaseComponentRuntimes)

    @property
    def rule_set_edition(self) -> 'ExpertRuleSet':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RuleSetEdition() As ExpertRuleSet (Read Only)
                | 
                |     Returns the editable object corresponding to this ruleset. Be careful that,
                |     according to your licence, or the type of ruleset you're handling, you may not
                |     have the right to edit the ruleset.
                | 
                |     Example:
                | 
                |          Dim aRuleSetEdition As ExpertRuleSet
                |          Set aRuleSetEdition = aRuleSetRuntime.RuleSetEdition
                | 
                |          If not(aRuleSetEdition is Nothing) Then
                |            ' .. some actions
                |          End if

        :rtype: ExpertRuleSet
        """
        
        from pycatia.general_knowledge_interfaces.expert_rule_set import ExpertRuleSet
        return ExpertRuleSet(self.expert_rule_set_runtime.RuleSetEdition)

    def status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Status() As long
                | 
                |     Returns the Status of the ruleset: 1=OK, 0=KO.
                | 
                |     Example:
                | 
                |          Dim RuleSet1 As ExpertRuleSet 
                |          Set RuleSet1 = RuleSet.ExpertGenericRuleBaseComponentRuntimes.Item("RuleSet1")
                |          status = RuleSet1.Status ()
                |          
                | 
                |     Returns:
                |         Status of the ruleset

        :rtype: int
        """
        return self.expert_rule_set_runtime.Status()

    def __repr__(self):
        return f'ExpertRuleSetRuntime(name="{self.name}")'
