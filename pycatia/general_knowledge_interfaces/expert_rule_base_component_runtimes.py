#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.general_knowledge_interfaces.expert_rule_base_component_runtime import ExpertRuleBaseComponentRuntime
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ExpertRuleBaseComponentRuntimes(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ExpertRuleBaseComponentRuntimes
                | 
                | Represents the collection of ExpertRuleBase (ExpertChecks, ExpertRules, and
                | ExpertRuleSets) components.
                | This collection can be seen flattened (with Item/Count) or hierarchised (with
                | ShallowItem/ShallowCount).
                | 
                | Be careful : the flattened view can be misleading. For instance, if there are
                | two ExpertChecks with the same name, you will be able to access only one of
                | them (with the methods ExpertRuleBaseComponentRuntimes.Item and
                | ExpertRuleBaseComponentRuntimes.Remove )
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ExpertRuleBaseComponentRuntime)
        self.expert_rule_base_component_runtimes = com_object

    def item(self, i_index: cat_variant) -> ExpertRuleBaseComponentRuntime:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As
                | ExpertRuleBaseComponentRuntime
                | 
                |     Returns a RuleBase component using its index or its name from the entire
                |     RuleBase collection.
                | 
                |     If several Expert components have the same name, the use of name is
                |     unpredicted.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Rule Base component to retrieve from
                |             the collection of Rule Base Components. As a numerics, this index is the rank
                |             of the Rule Base Component in the collection. The index of the first component
                |             in the collection is 1, and the index of the last component is Count. As a
                |             string, it is the name you assigned to the component using the
                |
                |         AnyObject.Name property or when creating the component.
                |         
                |     Returns:
                |         The retrieved Rule base component. 
                | 
                | Example:
                |     This example retrieves the last component in a RuleSet
                |     collection.
                | 
                |       Dim lastRuleBaseComponent as
                |       ExpertRuleBaseComponentRuntime
                |       Set lastRuleBaseComponent = RuleSet.Item(RuleCollection.Count)

        :param cat_variant i_index:
        :rtype: ExpertRuleBaseComponentRuntime
        """
        return ExpertRuleBaseComponentRuntime(self.expert_rule_base_component_runtimes.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes an Expert component from the Rule Base collection. If the expert
                |     component is a RuleSet all the rules, checks and rulesets embedded in the
                |     Ruleset will be also removed.
                | 
                |     If several Expert components have the same name, the use of name is
                |     unpredicted.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the component to retrieve from the
                |             collection. As a numerics, this index is the rank of the expert component in
                |             the collection. The index of the first component in the collection is 1, and
                |             the index of the last component is Count. As a string, it is the name you
                |             assigned to the component using the 
                | 
                |         AnyObject.Name property or when creating the Expert component.
                |         
                | 
                | Example:
                |     This example removes the Expert component named density from the relations
                |     collection.
                | 
                |      Dim CATDocs As Document
                |      Set CATDocs   = CATIA.Documents
                |      Dim partdoc As PartDocument
                |      Set partdoc   = CATDocs.Add("CATPart")
                |      Dim part As Part
                |      Set part      = partdoc.Part
                |      Set massCheck    = part.Relations.Item("RuleBase").RuleSet.ExpertRuleBaseComponentRuntimes.Remove("density")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.expert_rule_base_component_runtimes.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(expert_rule_base_component_runtimes)
        # #     Dim iIndex (2)
        # #     expert_rule_base_component_runtimes.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def shallow_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ShallowCount() As long
                | 
                |     Returns the number of first-level-depth objects in the collection. This is
                |     handy to scan the objects in a collection.
                | 
                |     Example:
                |         This example retrieves in ObjectNumber the number of objects currently
                |         gathered in MyCollection.
                | 
                |          ObjectNumber = MyCollection.ShallowCount

        :rtype: int
        """
        return self.expert_rule_base_component_runtimes.ShallowCount()

    def shallow_item(self, i_index: cat_variant) -> ExpertRuleBaseComponentRuntime:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ShallowItem(CATVariant iIndex) As
                | ExpertRuleBaseComponentRuntime
                | 
                |     Returns a first-level-depth RuleBase component using its index or its name
                |     from the RuleBase collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Rule Base component to retrieve from
                |             the collection of Rule Base Components. As a numerics, this index is the rank
                |             of the Rule Base Component in the collection. The index of the first component
                |             in the collection is 1, and the index of the last component is ShallowCount. As
                |             a string, it is the name you assigned to the component using the
                |             
                | 
                |         AnyObject.Name property or when creating the component.
                |         
                |     Returns:
                |         The retrieved Rule base component. 
                | 
                | Example:
                |     This example retrieves the last component in a RuleSet
                |     collection.
                | 
                |       Dim lastRuleBaseComponent as
                |       ExpertRuleBaseComponentRuntime
                |       Set lastRuleBaseComponent = RuleSet.ShallowItem(RuleCollection.ShallowCount)

        :param cat_variant i_index:
        :rtype: ExpertRuleBaseComponentRuntime
        """
        return ExpertRuleBaseComponentRuntime(self.expert_rule_base_component_runtimes.ShallowItem(i_index))

    def shallow_remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ShallowRemove(CATVariant iIndex)
                | 
                |     Removes an first-level-depth Expert component from the Rule Base
                |     collection. If the expert component is a RuleSet all the rules, checks and
                |     rulesets embedded in the Ruleset will be also removed.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the component to retrieve from the
                |             collection. As a numerics, this index is the rank of the expert component in
                |             the collection. The index of the first component in the collection is 1, and
                |             the index of the last component is ShallowCount. As a string, it is the name
                |             you assigned to the component using the 
                | 
                |         AnyObject.Name property or when creating the Expert component.
                |         
                | 
                | Example:
                |     This example removes the Expert component named density from the relations
                |     collection.
                | 
                |      Dim CATDocs As Document
                |      Set CATDocs   = CATIA.Documents
                |      Dim partdoc As PartDocument
                |      Set partdoc   = CATDocs.Add("CATPart")
                |      Dim part As Part
                |      Set part      = partdoc.Part
                |      Set massCheck    = part.Relations.Item("RuleBase").RuleSet.ExpertRuleBaseComponentRuntimes.ShallowRemove("density")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.expert_rule_base_component_runtimes.ShallowRemove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'shallow_remove'
        # # vba_code = """
        # # Public Function shallow_remove(expert_rule_base_component_runtimes)
        # #     Dim iIndex (2)
        # #     expert_rule_base_component_runtimes.ShallowRemove iIndex
        # #     shallow_remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ExpertRuleBaseComponentRuntimes(name="{self.name}")'
