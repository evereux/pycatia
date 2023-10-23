#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.general_knowledge_interfaces.expert_rule_base_runtime import ExpertRuleBaseRuntime


class ExpertRuleBase(ExpertRuleBaseRuntime):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.KnowledgeObject
                |                        KnowledgeInterfaces.KnowledgeActivateObject
                |                             KnowledgeInterfaces.Relation
                |                                GenKnowledgeInterfaces.ExpertRuleBaseRuntime
                |                                     ExpertRuleBase
                | 
                | Represents the RuleBase object that can be edited.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.expert_rule_base = com_object

    def volatile_copy(self) -> ExpertRuleBaseRuntime:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func VolatileCopy() As ExpertRuleBaseRuntime
                | 
                |     Copy the persistent rulebase in a unpersistent unchangeable
                |     rulebase.
                | 
                |     Returns:
                |         A volatile copy of the rulebase

        :rtype: ExpertRuleBaseRuntime
        """
        return ExpertRuleBaseRuntime(self.expert_rule_base.VolatileCopy())

    def __repr__(self):
        return f'ExpertRuleBase(name="{self.name}")'
