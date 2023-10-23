#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.general_knowledge_interfaces.expert_check_runtime import ExpertCheckRuntime


class ExpertCheck(ExpertCheckRuntime):
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
                |                        GenKnowledgeInterfaces.ExpertCheckRuntime
                |                             ExpertCheck
                | 
                | Represents the edition part of a check.
                | The following example shows how to access the Check check1 from an existing
                | RuleSet RS1 of the RuleBase RB1
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
        self.expert_check = com_object

    @property
    def body(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Body() As CATBSTR
                | 
                |     Returns or sets the body of a Check.
                | 
                |     Example:
                | 
                |          Check1.Body = "H.Diameter > 20mm AND GetSubString(P.Name, 1, 6) == "myPad."

        :rtype: str
        """

        return self.expert_check.Body

    @body.setter
    def body(self, value: str):
        """
        :param str value:
        """

        self.expert_check.Body = value

    @property
    def language(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Language() As long
                | 
                |     Returns or sets the language of a check.
                | 
                |     1
                |         KWE language 
                |     2
                |         VB Script

        :rtype: int
        """

        return self.expert_check.Language

    @language.setter
    def language(self, value: int):
        """
        :param int value:
        """

        self.expert_check.Language = value

    @property
    def variables(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Variables() As CATBSTR
                | 
                |     Returns or sets the variable scope of an Expert Check.
                | 
                |     Example:
                | 
                |          Check1.Variables = "H:Hole; P: Pad"

        :rtype: str
        """

        return self.expert_check.Variables

    @variables.setter
    def variables(self, value: str):
        """
        :param str value:
        """

        self.expert_check.Variables = value

    def __repr__(self):
        return f'ExpertCheck(name="{self.name}")'
