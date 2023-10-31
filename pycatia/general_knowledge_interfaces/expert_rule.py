#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.general_knowledge_interfaces.expert_rule_runtime import ExpertRuleRuntime


class ExpertRule(ExpertRuleRuntime):
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
                |                        GenKnowledgeInterfaces.ExpertRuleRuntime
                |                             ExpertRule
                | 
                | Represents the edition part of a rule.
                | The following example shows how access the Rule Rule1 from an existing RuleSet
                | RS1 of the RuleBase RB1
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
                |  Set RuleSet	 = RuleBase.ExpertRuleBaseComponentRuntimes.Item("RS1")
                |  Dim Rule1 As ExpertRuleRuntime
                |  Set Rule1	 = RuleSet.ExpertRuleBaseComponentRuntimes.Item("Rule1")
                |
                | See also:
                |     Relations, ExpertRuleBase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.expert_rule = com_object

    @property
    def body(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Body() As CATBSTR
                | 
                |     Returns or sets the string that defines the body of a Rule.
                |     For instance: "if ( H\\Diameter > 20mm ) H\\Activity = FALSE"

        :rtype: str
        """

        return self.expert_rule.Body

    @body.setter
    def body(self, value: str):
        """
        :param str value:
        """

        self.expert_rule.Body = value

    @property
    def language(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Language() As long
                | 
                |     Returns or sets the language of a rule.

        :rtype: int
        """

        return self.expert_rule.Language

    @language.setter
    def language(self, value: int):
        """
        :param int value:
        """

        self.expert_rule.Language = value

    @property
    def variables(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Variables() As CATBSTR
                | 
                |     Returns or sets the variables scope of the a Rule. For instance: "H:Hole;
                |     P: Pad"

        :rtype: str
        """

        return self.expert_rule.Variables

    @variables.setter
    def variables(self, value: str):
        """
        :param str value:
        """

        self.expert_rule.Variables = value

    def __repr__(self):
        return f'ExpertRule(name="{self.name}")'
