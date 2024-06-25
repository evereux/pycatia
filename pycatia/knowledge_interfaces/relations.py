#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator
from pathlib import Path

from pycatia.exception_handling.exceptions import CATIAApplicationException
from pycatia.knowledge_interfaces.check import Check
from pycatia.knowledge_interfaces.design_table import DesignTable
from pycatia.knowledge_interfaces.formula import Formula
from pycatia.knowledge_interfaces.law import Law
from pycatia.knowledge_interfaces.optimizations import Optimizations
from pycatia.knowledge_interfaces.relation import Relation
from pycatia.knowledge_interfaces.rule import Rule
from pycatia.knowledge_interfaces.set_of_equation import SetOfEquation
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class Relations(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Relations
                | 
                | Represents the collection of relations of the part or the
                | product.
                | 
                | A relation computes values. A relation can belong to one of the following
                | types:
                | 
                | Formula
                |     It combines parameters to compute the value of one output parameter only.
                |     For example, the mass of a cuboid can be the output parameter of a formula,
                |     while the value is computed using the following
                |     parameters:
                | 
                |      
                |      FormulaBody = (height*width*depth)*density
                |      
                | 
                | Program
                |     It combines conditions and actions on parameters to compute one or several
                |     output parameter values. For example, the following is a
                |     program:
                | 
                |      ProgramBody = if (mass>2kg) { depth=2mm length=10mm } else { depth=1mm length=5mm }  
                |      
                | 
                | Check
                |     It only contains conditions on parameter values. For example, the following
                |     is a check:
                | 
                |      CheckBody = mass<10kg
                |      
                | 
                | The parameters should be defined previously.
                | 
                | The following example shows how to retrieve the collection of relations from a
                | newly created part document:
                | 
                |  Dim CATDocs As Documents
                |  Set CATDocs = CATIA.Documents
                |  Dim part As Document
                |  Set part  = CATDocs.Add("CATPart")
                |  Dim relations As Relations
                |  Set relations = part.Relations
                |  
                | 
                | See also:
                |     Formula, Rule, Check, DesignTable
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Relation)
        self.relations = com_object

    @property
    def optimizations(self) -> Optimizations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Optimizations() As Optimizations (Read Only)
                | 
                |     Returns the optimization collection.
                |     It can be empty if no optimization is defined in the
                |     document.
                |     This property is available only when the Product Engineering Optimizer
                |     license is available.

        :rtype: Optimizations
        """

        return Optimizations(self.relations.Optimizations)

    def create_check(self, i_name: str, i_comment: str, i_check_body: str) -> Check:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateCheck(CATBSTR iName,
                | CATBSTR iComment,
                | CATBSTR iCheckBody) As Check
                | 
                |     Creates a check relation and adds it to the part's collection of
                |     relations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The check name 
                |         iComment
                |             A description of the check 
                |         iCheckBody
                |             The check definition 
                | 
                |     Returns:
                |         The created check 
                |     Example:
                |         This example creates the maximummass check relation and adds it to the
                |         newly created part:
                | 
                |          Dim CATDocs As Documents
                |          Set CATDocs = CATIA.Documents
                |          Dim partdoc As Document
                |          Set partdoc  = CATDocs.Add("CATPart")
                |          Dim part As Part
                |          Set part    = partdoc.Part 
                |          Dim massCheck As Check 
                |          Set massCheck    = part.Relations.CreateCheck
                |                             ("maximummass",
                |                              "Ensures that the mass is less than 10
                |                              kg",
                |                              "mass<10kg")

        :param str i_name:
        :param str i_comment:
        :param str i_check_body:
        :rtype: Check
        """
        return Check(self.relations.CreateCheck(i_name, i_comment, i_check_body))

    def create_design_table(self, i_name: str, i_comment: str, i_copy_mode: bool, i_sheet_path: Path) -> DesignTable:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateDesignTable(CATBSTR iName,
                | CATBSTR iComment,
                | boolean iCopyMode,
                | CATBSTR iSheetPath) As DesignTable
                | 
                |     Creates a design table based on a file organized in an vertical way and
                |     adds it to the part's collection of relations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The design table name 
                |         iComment
                |             A description of the design table 
                |         iCopyMode
                | 
                |     Returns:
                |         The created design table 
                |     Example:
                |         This example creates the dt design table and adds it to the newly
                |         created part:
                | 
                |          Dim CATDocs As Documents
                |          Set CATDocs = CATIA.Documents
                |          Dim partdoc As Document
                |          Set partdoc  = CATDocs.Add("CATPart")
                |          Dim part As Part
                |          Set part    = partdoc.Part 
                |          Dim designtable As DesignTable
                |          Set designtable    = part.Relations.CreateDesignTable
                |                              ("dt",
                |                               "Ensures that the mass is less than 10
                |                               kg",
                |                               TRUE,
                |                              
                |                              "/u/users/client/data/sheet.txt")

        :param str i_name:
        :param str i_comment:
        :param bool i_copy_mode:
        :param Path i_sheet_path:
        :rtype: DesignTable
        """
        if not i_sheet_path.exists():
            raise CATIAApplicationException(f'Could not find design table "{i_sheet_path}".')

        return DesignTable(self.relations.CreateDesignTable(i_name, i_comment, i_copy_mode, i_sheet_path))

    def create_formula(
            self,
            i_name: str,
            i_comment: str,
            i_output_parameter: 'Parameter',
            i_formula_body: str
    ):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateFormula(CATBSTR iName,
                | CATBSTR iComment,
                | Parameter iOutputParameter,
                | CATBSTR iFormulaBody) As Formula
                | 
                |     Creates a formula relation and adds it to the part's collection of
                |     relations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The formula name 
                |         iComment
                |             A description of the formula 
                |         iOutputParameter
                |             The parameter which stores the result of the formula
                |             
                |         iFormulaBody
                |             The formula definition 
                | 
                |     Returns:
                |         The created formula 
                |     Example:
                |         This example creates the computemass formula relation and adds it to
                |         the newly created part:
                | 
                |          Dim CATDocs As Documents
                |          Set CATDocs = CATIA.Documents
                |          Dim partdoc As Document
                |          Set partdoc  = CATDocs.Add("CATPart")
                |          Dim part As Part
                |          Set part    = partdoc.Part 
                |          Dim massFormula As Formula
                |          Set massFormula = part.Relations.CreateFormula
                |                            ("computemass",
                |                            "Computes the cuboid mass",
                |                             mass,
                |                            "(height*width*depth)*density")

        :param str i_name:
        :param str i_comment:
        :param Parameter i_output_parameter:
        :param str i_formula_body:
        :rtype: Formula
        """
        return Formula(self.relations.CreateFormula(i_name, i_comment, i_output_parameter.com_object, i_formula_body))

    def create_horizontal_design_table(self,
                                       i_name: str,
                                       i_comment: str,
                                       i_copy_mode: bool,
                                       i_sheet_path: str) -> DesignTable:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateHorizontalDesignTable(CATBSTR iName,
                | CATBSTR iComment,
                | boolean iCopyMode,
                | CATBSTR iSheetPath) As DesignTable
                | 
                |     Creates a design table based on a file organized in an horizontal way and
                |     adds it to the part's collection of relations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The design table name 
                |         iComment
                |             A description of the design table 
                |         iCopyMode
                | 
                |     Returns:
                |         The created design table 
                |     Example:
                |         This example creates the dt design table and adds it to the newly
                |         created part:
                | 
                |          Dim CATDocs As Documents
                |          Set CATDocs = CATIA.Documents
                |          Dim partdoc As Document
                |          Set partdoc  = CATDocs.Add("CATPart")
                |          Dim part As Part
                |          Set part    = partdoc.Part 
                |          Dim designtable As DesignTable
                |          Set designtable    = part.Relations.CreateHorizontalDesignTable
                |                             ("dt",
                |                              "Ensures that the mass is less than 10
                |                              kg",
                |                              TRUE,
                |                             "/u/users/client/data/horizontalsheet.txt")

        :param str i_name:
        :param str i_comment:
        :param bool i_copy_mode:
        :param str i_sheet_path:
        :rtype: DesignTable
        """
        return DesignTable(self.relations.CreateHorizontalDesignTable(i_name, i_comment, i_copy_mode, i_sheet_path))

    def create_law(self, i_name: str, i_comment: str, i_law_body: str) -> Law:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateLaw(CATBSTR iName,
                | CATBSTR iComment,
                | CATBSTR iLawBody) As Law
                | 
                |     Creates a law relation and adds it to the part's collection of
                |     relations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The law name 
                |         iComment
                |             A description of the law 
                |         iLawBody
                |             The law definition 
                | 
                |     Returns:
                |         The created law

        :param str i_name:
        :param str i_comment:
        :param str i_law_body:
        :rtype: Law
        """
        return Law(self.relations.CreateLaw(i_name, i_comment, i_law_body))

    def create_program(self, i_name: str, i_comment: str, i_program_body: str) -> Rule:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateProgram(CATBSTR iName,
                | CATBSTR iComment,
                | CATBSTR iProgramBody) As Rule
                | 
                |     Creates a program relation and adds it to the part's collection of
                |     relations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The program name 
                |         iComment
                |             A description of the program 
                |         iProgramBody
                |             The program definition 
                | 
                |     Returns:
                |         The created program 
                |     Example:
                |         This example creates the selectdepth program relation and adds it to
                |         the newly created part:
                | 
                |          Dim CATDocs As Documents
                |          Set CATDocs = CATIA.Documents
                |          Dim partdoc As Document
                |          Set partdoc  = CATDocs.Add("CATPart")
                |          Dim part As Part
                |          Set part    = partdoc.Part 
                |          Dim depthProgram As Program
                |          Set depthProgram = part.Relations.CreateProgram
                |                             ("selectdepth",
                |                             "Select depth with respect to
                |                             mass",
                |                             "if (mass>2kg) { depth=2mm } else { depth=1 mm
                |                             }")

        :param str i_name:
        :param str i_comment:
        :param str i_program_body:
        :rtype: Rule
        """
        return Rule(self.relations.CreateProgram(i_name, i_comment, i_program_body))

    def create_rule_base(self, i_name: str) -> Relation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateRuleBase(CATBSTR iName) As Relation
                | 
                |     Creates a rulebase.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the rulebase. 
                | 
                |     Returns:
                |         The created rulebase. 
                |     See also:
                |         ExpertRuleBase

        :param str i_name:
        :rtype: Relation
        """
        return Relation(self.relations.CreateRuleBase(i_name))

    def create_set_of_equations(self, i_name: str, i_comment: str, i_formula_body: str) -> SetOfEquation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func CreateSetOfEquations(CATBSTR iName,
                | CATBSTR iComment,
                | CATBSTR iFormulaBody) As SetOfEquation
                | 
                |     Creates a set of equations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the set of equation. 
                |         iComment
                |             The comment of the set of equation. 
                |         iFormulaBody
                |             The body of the set of equation " a==b+4; c ≤ 90".
                |             
                | 
                |     Returns:
                |         The created set of equations

        :param str i_name:
        :param str i_comment:
        :param str i_formula_body:
        :rtype: SetOfEquation
        """
        return SetOfEquation(self.relations.CreateSetOfEquations(i_name, i_comment, i_formula_body))

    def create_set_of_relations(self, i_parent: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub CreateSetOfRelations(AnyObject iParent)
                | 
                |     Creates a set of relations and appends it to a parent
                |     object.
                | 
                |     Parameters:
                | 
                |         iParent
                |             The object to which the set is appended

        :param AnyObject i_parent:
        :rtype: None
        """
        return self.relations.CreateSetOfRelations(i_parent.com_object)

    def generate_xml_report_for_checks(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GenerateXMLReportForChecks(CATBSTR iName)
                | 
                |     Generates an XML Report on all checks in the current
                |     document.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the XML file

        :param str i_name:
        :rtype: None
        """
        return self.relations.GenerateXMLReportForChecks(i_name)

    def item(self, i_index: cat_variant) -> Relation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func Item(CATVariant iIndex) As Relation
                | 
                |     Retrieves a relation using its index or its name from the Relations
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the relation to retrieve from the
                |             collection of relations. As a numerics, this index is the rank of the relation
                |             in the collection. The index of the first relation in the collection is 1, and
                |             the index of the last relation is Count. As a string, it is the name you
                |             assigned to the relation using the 
                | 
                |         AnyObject.Name property or when creating the relation.
                |         
                |     Returns:
                |         The retrieved relation 
                |     Example:
                |         This example retrieves the last relation in the relations
                |         collection.
                | 
                |          Dim lastRelation As Relation
                |          Set lastRelation = relations.Item(relations.Count)

        :param cat_variant i_index:
        :rtype: Relation
        """
        return Relation(self.relations.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a relation from the Relations collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the relation to remove from the collection
                |             of relations. As a numerics, this index is the rank of the relation in the
                |             collection. The index of the first relation in the collection is 1, and the
                |             index of the last relation is Count. As a string, it is the name you assigned
                |             to the relation using the 
                | 
                |         AnyObject.Name property or when creating the relation.
                |         
                | 
                | Example:
                |     This example removes the relation named density from the relations
                |     collection.
                | 
                |      relations.Remove("density")

        :param cat_variant i_index:
        :rtype: None
        """
        return self.relations.Remove(i_index)

    def sub_list(self, i_feature: AnyObject, i_recursively: bool) -> 'Relations':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func SubList(AnyObject iFeature,
                | boolean iRecursively) As Relations
                | 
                |     Returns a sub-collection of relations aggregated to an
                |     object.
                | 
                |     Parameters:
                | 
                |         iFeature
                |             The object used to filter the the whole relation collection to get
                |             the resulting sub-collection. 
                |         iRecursively
                |             A flag to specify if children parameters are to be searched for in
                |             the returned collection 
                | 
                |     Returns:
                |         The resulting sub-collection 
                |     Example:
                |         This example shows how to get a collection of relations that are under
                |         a Pad
                | 
                |          Dim Relations1 As Relations
                |          Set Relations1 = CATIA.ActiveDocument.Part.Relations' gets the collection of relations in the
                |              part
                |          Dim Body0 As AnyObject
                |          Set Body0 = CATIA.ActiveDocument.Part.Bodies.Item  ( "MechanicalTool.1" ) 
                |          Dim Pad1 As AnyObject
                |          Set Pad1 = Body0.Shapes.Item  ( "Pad.1" ) ' gets the pad Pad.1
                |          Dim Relations2 As Relations
                |          Set Relations2 = Relations1.SubList(Pad1, TRUE) ' gets the collection of relations that are 
                |              under the pad Pad.1

        :param AnyObject i_feature:
        :param bool i_recursively:
        :rtype: Relations
        """
        return Relations(self.relations.SubList(i_feature.com_object, i_recursively))

    def __getitem__(self, n: int) -> Relation:
        if (n + 1) > self.count:
            raise StopIteration

        return Relation(self.relations.Item(n + 1))

    def __iter__(self) -> Iterator[Relation]:
        for i in range(self.count):
            yield self.child_object(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Relations(name="{self.name}")'
