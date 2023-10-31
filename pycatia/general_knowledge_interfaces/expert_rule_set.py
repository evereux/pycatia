#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.general_knowledge_interfaces.expert_check import ExpertCheck
from pycatia.general_knowledge_interfaces.expert_rule import ExpertRule
from pycatia.general_knowledge_interfaces.expert_rule_set_runtime import ExpertRuleSetRuntime


class ExpertRuleSet(ExpertRuleSetRuntime):
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
                |                        GenKnowledgeInterfaces.ExpertRuleSetRuntime
                |                             ExpertRuleSet
                | 
                | Represents the ExpertRuleSet object which is the editable part of a RuleSet or
                | a RuleBase.
                | The following example shows how to access the RuleSet of the rule Base
                | RB1
                | 
                |  Dim CATDocs As Documents 
                |  Set CATDocs   = CATIA.Documents
                |  Dim partdoc As Document
                |  Set partdoc   = CATDocs.Add("CATPart")
                |  Dim part as Part
                |  Set part      = partdoc.Part
                |  Dim relations as Relations
                |  Set relations = part.Relations
                |  Dim RuleBase as ExpertRuleBaseRuntime
                |  Set RuleBase  = relations.Item("RB1")
                |  Dim RuleSet as ExpertRuleSet
                |  Set RuleSet	 = RuleBase.RuleSet
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.expert_rule_set = com_object

    def create_check(self, i_name: str, i_check_variables: str, i_check_body: str, i_rule_set: str) -> ExpertCheck:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateCheck(CATBSTR iName,
                | CATBSTR iCheckVariables,
                | CATBSTR iCheckBody,
                | CATBSTR iRuleSet) As ExpertCheck
                | 
                |     Creates a check and adds it to the RuleSet.
                | 
                |     Parameters:
                | 
                |         iName
                |             The check name 
                |         iCheckVariables
                |             define variables of the check. 
                |         iCheckBody
                |             The check definition 
                |         iRuleSet
                |             The ruleset name where the check is to be aggregated.
                |             If this macro is used from the RuleSet where we
                |             want to create the check, the param must be equal to value : "".
                | 
                |     Returns:
                |         The created check 
                |     Example:
                |         This example creates the SolidActivity check and adds it to the newly
                |         created RuleSet.1 RuleSet then creates the HoleActivity check and adds it to
                |         the newly created RuleSet.2 RuleSet
                | 
                |           Dim CATDocs As Documents 
                |           Set CATDocs   = CATIA.Documents
                |           Dim partdoc As Document
                |           Dim part as Part
                |           Dim CheckSolid as ExpertCheck
                |           Dim ruleset as ExpertRuleSet
                |           Dim CheckHole as ExpertCheck
                | 
                |           Set partdoc      = CATDocs.Add("CATPart")
                |           Set part         = partdoc.Part 
                |           Set CheckSolid   = part.Relations.Item("RuleBase").RuleSet.CreateCheck
                |                              ("SolidActivity",
                |                               "Sol : Solid",
                |                               "Sol.Activity == True",
                |                               "RuleSet.1")
                |           Set ruleset      = part.Relations.Item("RuleBase").RuleSet.CreateRuleSet
                |                              ("RuleSet.2",
                |                               "")
                |           Set CheckHole    = ruleset.CreateCheck
                |                              ("HoleActivity",
                |                               "H : Hole",
                |                               "H.Activity == True",
                |                               "")

        :param str i_name:
        :param str i_check_variables:
        :param str i_check_body:
        :param str i_rule_set:
        :rtype: ExpertCheck
        """
        return ExpertCheck(self.expert_rule_set.CreateCheck(i_name, i_check_variables, i_check_body, i_rule_set))

    def create_rule(self, i_name: str, i_rule_variables: str, i_rule_body: str, i_rule_set: str) -> ExpertRule:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateRule(CATBSTR iName,
                | CATBSTR iRuleVariables,
                | CATBSTR iRuleBody,
                | CATBSTR iRuleSet) As ExpertRule
                | 
                |     Creates a rule and adds it to the RuleSet.
                | 
                |     Parameters:
                | 
                |         iName
                |             The rule name 
                |         iRuleVariables
                |             define variables of the rule. 
                |         iRuleBody
                |             The check definition 
                |         iRuleSet
                |             The RuleSet name where this rule aggregated. If this macro is used from the ruleset where
                |             we want to aggregate the rule, the param must be equal to value : "".
                | 
                |     Returns:
                |         The created rule 
                |     Example:
                |         This example creates the DesactivateIfActivatedOnSolid rule and adds it
                |         to the newly created RuleSet.1 RuleSet then creates the
                |         DesactivateIfActivatedOnHole rule and adds it to the newly created RuleSet.2
                |         RuleSet
                | 
                |           Dim CATDocs As Documents 
                |           Set CATDocs   = CATIA.Documents
                | 
                |           Dim partdoc As Document
                |           Set partdoc   = CATDocs.Add("CATPart")
                | 
                |           Dim part as Part
                |           Set part         = partdoc.Part
                | 
                |           Dim rulesolid as ExpertRule
                |           Set rulesolid    = part.Relations.Item("RuleBase").RuleSet.CreateRule
                |                              ("DesactivateIfActivatedOnSolid",
                |                               "Sol : Solid",
                |                               "Sol.Activity == True then Sol.Activity = False",
                |         "RuleSet.1")
                |           Dim ruleset as ExpertRuleSet
                |           Set ruleset      = part.Relations.Item("RuleBase").RuleSet.CreateRuleSet
                |                              ("RuleSet.2",
                |                               "")
                |           Dim rulehole as ExpertRule
                |           Set rulehole     = ruleset.CreateRule
                |                              ("DesactivateIfActivatedOnHole",
                |                               "H : Hole",
                |                               "H.Activity == True then H.Activity = False",
                |                               "")

        :param str i_name:
        :param str i_rule_variables:
        :param str i_rule_body:
        :param str i_rule_set:
        :rtype: ExpertRule
        """
        return ExpertRule(self.expert_rule_set.CreateRule(i_name, i_rule_variables, i_rule_body, i_rule_set))

    def create_rule_set(self, i_name: str, i_rule_set: str) -> 'ExpertRuleSet':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateRuleSet(CATBSTR iName,
                | CATBSTR iRuleSet) As ExpertRuleSet
                | 
                |     Creates a RuleSet and adds it to the RuleSet.
                | 
                |     Parameters:
                | 
                |         iName
                |             The ruleset name 
                |         iRuleSet
                |             The ruleset name where this ruleset is to be aggregated. If this macro is used from the
                |             ruleset or the rulebase where we want to aggregate the ruleset, the param must be equal
                |             to value : "".
                | 
                |     Returns:
                |         The created ruleset 
                |     Example:
                |         This example, firstly, creates the RuleSet.1 RuleSet and adds it to the
                |         newly created RuleBase. Secondly, it creates RuleSet.2 RuleSet and adds it to
                |         the ruleset RuleSet.1
                | 
                |           Dim CATDocs As Documents 
                |           Set CATDocs   = CATIA.Documents
                |           Dim partdoc As Document
                |           Set partdoc   = CATDocs.Add("CATPart")
                |           Dim part as Part
                |           Set part         = partdoc.Part
                |           Dim RS1 as ExpertRuleSet
                |           RS1 = part.Relations.Item("RuleBase").RuleSet.CreateRuleSet
                |                              ("RuleSet.1",
                |                               "")
                |           Dim RS2 as ExpertRuleSet
                |           RS2 = part.Relations.Item("RuleBase").RuleSet.CreateRuleSet
                |                              ("RuleSet.2",
                |                               "RuleSet.1")

        :param str i_name:
        :param str i_rule_set:
        :rtype: ExpertRuleSet
        """
        return ExpertRuleSet(self.expert_rule_set.CreateRuleSet(i_name, i_rule_set))

    def __repr__(self):
        return f'ExpertRuleSet(name="{self.name}")'
