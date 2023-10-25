#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.general_knowledge_interfaces.expert_rule_set import ExpertRuleSet
from pycatia.knowledge_interfaces.relation import Relation
from pycatia.system_interfaces.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia.general_knowledge_interfaces.expert_rule_base import ExpertRuleBase


class ExpertRuleBaseRuntime(Relation):
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
                |                                 ExpertRuleBaseRuntime
                | 
                | Represents the Runtime part of the RuleBase.
                | The following example shows how to create the Rule Base RB1 from a newly
                | created part document:
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
                |  Set RuleBase  = relations.CreateRuleBase("RB1")
                |
                | See also:
                |     Relations
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.expert_rule_base_runtime = com_object

    @property
    def report_description_length(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReportDescriptionLength() As
                | CatDescriptionLengthType
                | 
                |     Returns or sets the Report Description Length (For Text option
                |     only).
                | 
                |     0
                |         ShortText 
                |     1
                |         LongText

        :return: enum cat_description_length_type
        :rtype: int
        """

        return self.expert_rule_base_runtime.ReportDescriptionLength

    @report_description_length.setter
    def report_description_length(self, value: int):
        """
        :param int value: enum cat_description_length_type
        """

        self.expert_rule_base_runtime.ReportDescriptionLength = value

    @property
    def report_output_format(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReportOutPutFormat() As CatOutPutFormatType
                | 
                |     Returns or sets the Report OutPut Format.
                | 
                |     0
                |         Html 
                |     1
                |         Text 
                |     2
                |         Print 
                |     3
                |         Email

        :return: enum cat_out_put_format_type
        :rtype: int
        """

        return self.expert_rule_base_runtime.ReportOutPutFormat

    @report_output_format.setter
    def report_output_format(self, value: int):
        """
        :param int value: enum cat_out_put_format_type
        """

        self.expert_rule_base_runtime.ReportOutPutFormat = value

    @property
    def report_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReportPath() As CATBSTR
                | 
                |     Returns or sets the Report output path.

        :rtype: str
        """

        return self.expert_rule_base_runtime.ReportPath

    @report_path.setter
    def report_path(self, value: str):
        """
        :param str value:
        """

        self.expert_rule_base_runtime.ReportPath = value

    @property
    def report_show_result(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReportShowResult() As CatShowResultType
                | 
                |     Returns or sets the option for sorting the report.
                | 
                |     0
                |         ByRule 
                |     1
                |         ByObject 
                |     2
                |         ByState

        :return: enum cat_show_result_type
        :rtype: int
        """

        return self.expert_rule_base_runtime.ReportShowResult

    @report_show_result.setter
    def report_show_result(self, value: int):
        """
        :param int value: enum cat_show_result_type
        """

        self.expert_rule_base_runtime.ReportShowResult = value

    @property
    def rule_base_edition(self) -> 'ExpertRuleBase':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RuleBaseEdition() As ExpertRuleBase (Read Only)
                | 
                |     Returns the editable object corresponding to this rulebase. Be careful
                |     that, according to your licence, or the type of rulebase you're handling, you
                |     may not have the right to edit the rulebase. 
                | Example:
                | 
                |      Dim aRBEdition As CATIAExpertRuleBase
                |      Set aRBEdition = aRBRuntime.RuleBaseEdition
                | 
                |      If not(aRBEdition is Nothing) Then
                |        ' .. action on the editable rulebase
                |      End if

        :rtype: ExpertRuleBase
        """

        from pycatia.general_knowledge_interfaces.expert_rule_base import ExpertRuleBase
        return ExpertRuleBase(self.expert_rule_base_runtime.RuleBaseEdition)

    @property
    def rule_set(self) -> ExpertRuleSet:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RuleSet() As ExpertRuleSet (Read Only)
                | 
                |     Returns the Set linked to the RuleBase. This is the main RuleSet that
                |     contains all the RuleBase components.

        :rtype: ExpertRuleSet
        """

        return ExpertRuleSet(self.expert_rule_base_runtime.RuleSet)

    @property
    def solve_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SolveType() As CatSolveType
                | 
                |     Returns or sets the solve option.

        :return: enum cat_solve_type
        :rtype: int
        """

        return self.expert_rule_base_runtime.SolveType

    @solve_type.setter
    def solve_type(self, value: int):
        """
        :param int value: enum cat_solve_type
        """

        self.expert_rule_base_runtime.SolveType = value

    @property
    def text_visualization(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TextVisualization() As CatVisualizationType
                | 
                |     Returns or sets the Report option for visualization.
                | 
                |     0
                |         Passed 
                |     1
                |         Failed 
                |     2
                |         Both

        :return: enum cat_visualization_type
        :rtype: int
        """

        return self.expert_rule_base_runtime.TextVisualization

    @text_visualization.setter
    def text_visualization(self, value: int):
        """
        :param int value: enum cat_visualization_type
        """

        self.expert_rule_base_runtime.TextVisualization = value

    def accurate_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AccurateType() As CATBSTR
                | 
                |     Returns as a string the type of component.
                | 
                |     Returns:
                |         A string among ("ExpertRuleBase", "ExpertRuleBaseRuntime")

        :rtype: str
        """
        return self.expert_rule_base_runtime.AccurateType()

    def add_fact(self, i_fact: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddFact(AnyObject iFact)
                | 
                |     Adds new fact to the rule base resolution.
                | 
                |     Parameters:
                | 
                |         iFact
                |             Fact to be added 
                | 
                |     Example:
                | 
                |           Dim pad3 as Shape
                |           Dim rulebase as ExpertRuleBase
                | 
                |           Set pad3 = part.MainBody.Shapes.Item("Pad3")
                |           Set rulebase = part.Relations.Item("RuleBase")
                |           rulebase.AddFact (pad3)

        :param AnyObject i_fact:
        :rtype: None
        """
        return self.expert_rule_base_runtime.AddFact(i_fact.com_object)

    def add_root_of_facts(self, i_root_facts: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddRootOfFacts(AnyObject iRootFacts)
                | 
                |     Adds a new root of facts to the rule base.
                | 
                |     Parameters:
                | 
                |         iRootFacts
                |             root of facts to be added.

        :param AnyObject i_root_facts:
        :rtype: None
        """
        return self.expert_rule_base_runtime.AddRootOfFacts(i_root_facts.com_object)

    def deduce(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Deduce()
                | 
                |     Launch a Forward chaining Solve on the current RuleBase. 
                | Example:
                | 
                |       Dim rulebase as ExpertRuleBase
                | 
                |       Set rulebase = part.Relations.Item("RuleBase")
                |       rulebase.Deduce ()

        :rtype: None
        """
        return self.expert_rule_base_runtime.Deduce()

    def fingerprint(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Fingerprint() As boolean
                | 
                |     Returns the Fingerprint information. The fingerprint indicates
                |     if the last result of the rulebase is relevant regarding to the
                |     objects the rule base has checked. In other words, if the part
                |     has evolved since last Deduce, the fingerprint is false.
                |     Be careful : on volatile rulebases ( ExpertRuleBase.VolatileCopy ), it raises an error.
                | 
                |     Example:
                | 
                |           on error resume next
                |           part.Relations.Item("RuleBase").Fingerprint ()
                |           on error goto 0
                |          
                | 
                |     Returns:
                |         Fingerprint information

        :rtype: bool
        """
        return self.expert_rule_base_runtime.Fingerprint()

    def get_number_of_roots_of_facts(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNumberOfRootsOfFacts() As long
                | 
                |     Retrieves the number of roots of facts of the rule base.
                | 
                |     Returns:
                |         Number of roots of facts.

        :rtype: int
        """
        return self.expert_rule_base_runtime.GetNumberOfRootsOfFacts()

    def get_roots_of_facts(self, o_roots_of_facts: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetRootsOfFacts(CATSafeArrayVariant oRootsOfFacts)
                | 
                |     Retrieves all the roots of facts from the rule base.
                | 
                |     Parameters:
                | 
                |         oRootsOfFacts
                |             array of roots of facts.

        :param tuple o_roots_of_facts:
        :rtype: None
        """
        return self.expert_rule_base_runtime.GetRootsOfFacts(o_roots_of_facts)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_roots_of_facts'
        # # vba_code = """
        # # Public Function get_roots_of_facts(expert_rule_base_runtime)
        # #     Dim oRootsOfFacts (2)
        # #     expert_rule_base_runtime.GetRootsOfFacts oRootsOfFacts
        # #     get_roots_of_facts = oRootsOfFacts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def import_(self, i_rule_set: ExpertRuleSet, i_force: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Import(ExpertRuleSet iRuleSet,
                | boolean iForce)
                | 
                |     Import from RuleSet.
                | 
                |     Parameters:
                | 
                |         iRuleSet
                |             CATIAExpertRuleSet : the RuleSet user want to import. 
                |         iForce
                |             Boolean : if True (= 1), then if imported rules allready exist in target document, rules of target document are replaced. 
                | 
                |     Example:
                | 
                |          Dim CATDocs As Documents
                |          Set CATDocs   = CATIA.Documents
                |          Dim partdoc As Document
                |          Set partdoc = CATDocs.Open("e:/TargetDocument.CATPart")
                |          Dim part As Part
                |          Set part      = partdoc.Part
                |          Dim productdoc As Document
                |          Set productdoc = CATDocs.Open("e:/ImportedDocument.CATProduct")
                |          Dim product As Product
                |          Set product      = productdoc.Product
                |          Dim ruleset As ExpertRuleSet
                |          Set ruleset    = product.Relations.Item("RuleBase").RuleSet.ExpertRuleBaseComponentRuntimes.ShallowItem(1)
                |          part.Relations.Item("RuleBase").Import (ruleset,0)

        :param ExpertRuleSet i_rule_set:
        :param bool i_force:
        :rtype: None
        """
        return self.expert_rule_base_runtime.Import(i_rule_set.com_object, i_force)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'import'
        # # vba_code = """
        # # Public Function import(expert_rule_base_runtime)
        # #     Dim iRuleSet (2)
        # #     expert_rule_base_runtime.Import iRuleSet
        # #     import = iRuleSet
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def import_from_file(self, i_path: str, i_force: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ImportFromFile(CATBSTR iPath,
                | boolean iForce)
                | 
                |     Import from file.
                | 
                |     Parameters:
                | 
                |         iPath
                |             CATBSTR : the path of the document user want to import. 
                |         iForce
                |             Boolean : if True (= 1), then if imported rules allready
                |             exist in target document, rules of target document are
                |             replaced. if False (= 0), then if imported rules allready
                |             exist in target document, rules of imported document are ignored.*
                |
                |     Example:
                | 
                |           part.Relations.Item("RuleBase").ImportFromFile
                |           ("e:/importeddocument.CATProduct",0)

        :param str i_path:
        :param bool i_force:
        :rtype: None
        """
        return self.expert_rule_base_runtime.ImportFromFile(i_path, i_force)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'import_from_file'
        # # vba_code = """
        # # Public Function import_from_file(expert_rule_base_runtime)
        # #     Dim iPath (2)
        # #     expert_rule_base_runtime.ImportFromFile iPath
        # #     import_from_file = iPath
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def import_with_link(self, i_root: AnyObject, i_force: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ImportWithLink(AnyObject iRoot,
                | boolean iForce)
                | 
                |     Import with link to a document.
                | 
                |     Parameters:
                | 
                |         iRoot
                |             CATIABase : the root user want to import into. 
                |         iForce
                |             Boolean : if True (= 1), then if imported rules allready exist
                |             in target document, rules of target document are replaced.
                |             if False (= 0), then if imported rules allready exist in
                |             target document, rules of imported document are ignored.*
                | 
                |     Example:
                | 
                |           part.Relations.Item("RuleBase").ImportWithLink
                |           (root,0)

        :param AnyObject i_root:
        :param bool i_force:
        :rtype: None
        """
        return self.expert_rule_base_runtime.ImportWithLink(i_root.com_object, i_force)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'import_with_link'
        # # vba_code = """
        # # Public Function import_with_link(expert_rule_base_runtime)
        # #     Dim iRoot (2)
        # #     expert_rule_base_runtime.ImportWithLink iRoot
        # #     import_with_link = iRoot
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_root_of_facts(self, i_root_facts: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveRootOfFacts(AnyObject iRootFacts)
                | 
                |     Removes a root of facts from the rule base.
                | 
                |     Parameters:
                | 
                |         iRootFacts
                |             root of facts to be removed.

        :param AnyObject i_root_facts:
        :rtype: None
        """
        return self.expert_rule_base_runtime.RemoveRootOfFacts(i_root_facts.com_object)

    def report(self, really_start_browser: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Report(boolean reallyStartBrowser)
                | 
                |     Launch a Report. The default output format is HTML
                | 
                |     Parameters:
                | 
                |         reallyStartBrowser
                |             Boolean : if True (= 1), then the browser is started on the report 
                | 
                |     Example:
                | 
                |           part.Relations.Item("RuleBase").Report (0)

        :param bool really_start_browser:
        :rtype: None
        """
        return self.expert_rule_base_runtime.Report(really_start_browser)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'report'
        # # vba_code = """
        # # Public Function report(expert_rule_base_runtime)
        # #     Dim reallyStartBrowser (2)
        # #     expert_rule_base_runtime.Report reallyStartBrowser
        # #     report = reallyStartBrowser
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def synchronize_status(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func SynchronizeStatus() As boolean
                | 
                |     Returns the Synchronize information. The synchronize status indicates
                |     for a linked rule base if the rulebase is synchronized.
                |     Be careful : on volatile rulebases ( ExpertRuleBase.VolatileCopy ), it raises an error.
                | 
                |     Example:
                | 
                |           on error resume next
                |           part.Relations.Item("RuleBase").SynchronizeStatus ()
                |           on error goto 0
                |
                |     Returns:
                |         Synchronize status

        :rtype: bool
        """
        return self.expert_rule_base_runtime.SynchronizeStatus()

    def __repr__(self):
        return f'ExpertRuleBaseRuntime(name="{self.name}")'
