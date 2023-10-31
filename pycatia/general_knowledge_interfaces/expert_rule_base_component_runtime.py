#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class ExpertRuleBaseComponentRuntime(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ExpertRuleBaseComponentRuntime
                | 
                | Represents a rule base component in a ruleset.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.expert_rule_base_component_runtime = com_object

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Comment() As CATBSTR
                | 
                |     Returns or sets the comment of a rulebase component.

        :rtype: str
        """

        return self.expert_rule_base_component_runtime.Comment

    @comment.setter
    def comment(self, value: str):
        """
        :param str value:
        """

        self.expert_rule_base_component_runtime.Comment = value

    def accurate_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AccurateType() As CATBSTR
                | 
                |     Returns as a string the type of component. Returns a string among
                |     ("ExpertCheck", "ExpertCheckRuntime", "ExpertRule", "ExpertRuleRuntime",
                |     "ExpertRuleSet", "ExpertRuleSetRuntime").
                | 
                |     Returns:
                |         Type name of the rule base component

        :rtype: str
        """
        return self.expert_rule_base_component_runtime.AccurateType()

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Activate()
                | 
                |     Activates the RuleBaseComponent.
                | 
                |     Example:
                |         This example activates the SolidActivity ExpertCheck:
                | 
                |          Dim CATDocs As Document
                |          Set CATDocs   = CATIA.Documents
                |          Dim partdoc As PartDocument
                |          Set partdoc   = CATDocs.Add("CATPart")
                |          Dim part As Part
                |          Set part      = partdoc.Part
                |          part.Relations.Item("RuleBase").RuleSet.ExpertRuleBaseComponentRuntimes.Item("SolidActivity").Activate()

        :rtype: None
        """
        return self.expert_rule_base_component_runtime.Activate()

    def deactivate(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Deactivate()
                | 
                |     Desactivates the RuleBaseComponent.
                | 
                |     Example:
                |         This example Desactivates the SolidActivity
                |         ExpertCheck:
                | 
                |          Dim CATDocs As Document
                |          Set CATDocs   = CATIA.Documents
                |          Dim partdoc As PartDocument
                |          Set partdoc   = CATDocs.Add("CATPart")
                |          Dim part As Part
                |          Set part      = partdoc.Part
                |          part.Relations.Item("RuleBase").RuleSet.ExpertRuleBaseComponentRuntimes.Item("SolidActivity").Deactivate()

        :rtype: None
        """
        return self.expert_rule_base_component_runtime.Deactivate()

    def is_use_only(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsUseOnly() As boolean
                | 
                |     Retrieves the use-only status of the component.
                | 
                |     Returns:
                |         Use only status of the component

        :rtype: bool
        """
        return self.expert_rule_base_component_runtime.IsUseOnly()

    def is_activate(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Isactivate() As boolean
                | 
                |     Tells if the RuleBaseComponent is active.
                | 
                |     Example:
                |         This example tells if the SolidActivity ExpertCheck is active
                |         :
                | 
                |          Dim CATDocs As Document
                |          Set CATDocs   = CATIA.Documents
                |          Dim partdoc As PartDocument
                |          Set partdoc   = CATDocs.Add("CATPart")
                |          Dim part As Part
                |          Set part      = partdoc.Part
                |          status = part.Relations.Item("RuleBase").RuleSet.ExpertRuleBaseComponentRuntimes.Item("SolidActivity").Isactivate()
                |          
                | 
                |     Returns:
                |         Activity of the rule base component

        :rtype: bool
        """
        return self.expert_rule_base_component_runtime.Isactivate()

    def parse(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Parse() As CATBSTR
                | 
                |     Syntactically analyses (ie parses) the component.
                | 
                |     Returns:
                |         Empty string if the parse is correct, otherwise comments on the errors

        :rtype: str
        """
        return self.expert_rule_base_component_runtime.Parse()

    def set_use_only(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUseOnly()
                | 
                |     Prevents any access to the component for reading or deleting.
                |     Be careful : this operation is not reversible.

        :rtype: None
        """
        return self.expert_rule_base_component_runtime.SetUseOnly()

    def __repr__(self):
        return f'ExpertRuleBaseComponentRuntime(name="{self.name}")'
