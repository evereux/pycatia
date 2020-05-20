#! /usr/bin/python3.6

from pycatia.knowledge_interfaces.check import Check
from pycatia.knowledge_interfaces.design_table import DesignTable
from pycatia.knowledge_interfaces.formula import Formula
from pycatia.knowledge_interfaces.law import Law
from pycatia.knowledge_interfaces.relation import Relation
from pycatia.knowledge_interfaces.rule import Rule
from pycatia.knowledge_interfaces.setofequation import SetOfEquation
from pycatia.system_interfaces.collection import Collection


class Relations(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the collection of relations of the part or the product.
                | A relation computes values. A relation can belong to one of the following types:
                | Formula:
                |   It combines parameters to compute the value of one output parameter only. For
                |   example, the mass of a cuboid can be the output parameter of a formula, while
                |   the value is computed using the following parameters:
                |       FormulaBody = (height*width*depth)*density
                |
                | Program:
                | It combines conditions and actions on parameters to compute one or several output
                | parameter values. For example, the following is a program:
                |       ProgramBody = if (mass>2kg) {depth=2mm length=10mm} else {depth=1mm
                |                     length=5mm }
                |
                | Check
                | It only contains conditions on parameter values. For example, the following is a
                | check:
                |       CheckBody = mass<10kg

                | The parameters should be defined previously.

                | Example:
                | The following example shows how to retrieve the collection of relations from a
                | newly created part document:
                |
                | Dim CATDocs As Documents
                | Dim part As Document
                | Dim relations As Relations
                |
                | Set CATDocs = CATIA.Documents
                | Set part  = CATDocs.Add("CATPart")
                | Set relations = part.Relations
    """

    def __init__(self, relations_com_object):
        super().__init__(relations_com_object, child_object=Relation)
        self.relations = relations_com_object

    @property
    def optimizations(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Optimizations
                | o Property Optimizations(    ) As Optimizations
                |
                | Returns the optimization collection.  It can be empty if no
                | optimization is defined in the document. This property is available
                | only when the Product Engineering Optimizer license is available.


                | Parameters:


        """
        return self.relations.Optimizations

    def create_check(self, name, comment, check_formula):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateCheck
                | o Func CreateCheck(    CATBSTR    iName,
                |                        CATBSTR    iComment,
                |                        CATBSTR    iCheckBody) As Check
                |
                | Creates a check relation and adds it to the part's collection of
                | relations.

                | Parameters:
                | iName
                |     The check name
                |
                |  iComment
                |     A description of the check
                |
                |  iCheckBody
                |     The check definition
                |
                |  Returns:
                |   The created check

                | Examples:
                | This example creates the maximummass check relation
                | and adds it to the newly created part:
                |
                | Dim CATDocs As Documents
                | Dim partdoc As Document
                | Dim part As Part
                | Dim massCheck As Check
                |
                | Set CATDocs = CATIA.Documents
                | Set partdoc = CATDocs.Add("CATPart")
                | Set part = partdoc.Part
                | Set massCheck = part.Relations.CreateCheck("maximummass",
                |                                            "Mass is less than 10 kg",
                |                                            "mass<10kg")

            :param str name:
            :param str comment:
            :param str check_formula:
            :return: Check()
        """
        return Check(self.relations.CreateCheck(name, comment, check_formula))

    def create_design_table(self, name, comment, copy_mode, sheet_path):

        """
        .. note::
            CAA V5 Visual Basic help

                | CreateDesignTable
                | o Func CreateDesignTable(    CATBSTR    iName,
                |                              CATBSTR    iComment,
                |                              boolean    iCopyMode,
                |                              CATBSTR    iSheetPath) As DesignTable
                |
                | Creates a design table based on a file organized in an vertical way
                | and adds it to the part's collection of relations.

                | Parameters:
                | iName
                |     The design table name
                |
                |  iComment
                |     A description of the design table
                |
                |  iCopyMode

                |  Returns:
                |   The created design table

                | Examples:
                | This example creates the dt design table
                | and adds it to the newly created part:
                |
                | Dim CATDocs As Documents
                | Set CATDocs = CATIA.Documents
                | Dim partdoc As Document
                | Set partdoc = CATDocs.Add("CATPart")
                | Dim part As Part
                | Set part = partdoc.Part
                | Dim designtable As DesignTable
                | Set designtable = part.Relations.CreateDesignTable("dt",
                |                                                    "Mass is less than 10 kg",
                |                                                    TRUE,
                |                                                    "/users/client/data/sheet.txt")

        :param str name:
        :param str comment:
        :param bool copy_mode:
        :param Path() sheet_path:
        :return: DesignTable
        """
        return DesignTable(self.relations.CreateDesignTable(name, comment, copy_mode, sheet_path))

    def create_formula(self, name, comment, output_parameter, formula_body):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateFormula
                | o Func CreateFormula(    CATBSTR    iName,
                |                          CATBSTR    iComment,
                |                          Parameter  iOutputParameter,
                |                          CATBSTR    iFormulaBody) As Formula
                |
                | Creates a formula relation and adds it to the part's collection of
                | relations.

                | Parameters:
                | iName
                |     The formula name
                |
                |  iComment
                |     A description of the formula
                |
                |  iOutputParameter
                |     The parameter which stores the result of the formula
                |
                |  iFormulaBody
                |     The formula definition

                |  Returns:
                |   The created formula

                | Examples:
                | This example creates the computemass formula relation
                | and adds it to the newly created part:
                |
                | Dim CATDocs As Documents
                | Dim partdoc As Document
                | Dim part As Part
                | Dim massFormula As Formula
                | Set CATDocs = CATIA.Documents
                | Set partdoc = CATDocs.Add("CATPart")
                | Set part = partdoc.Part
                | Set massFormula = part.Relations.CreateFormula("computemass",
                |                                                "Computes the cuboid mass",
                |                                                mass,
                |                                                "(height*width*depth)*density")

        :param str name:
        :param str comment:
        :param Parameter() output_parameter:
        :param formula_body:
        :return: Formula()

        """
        return Formula(self.relations.CreateFormula(name, comment, output_parameter.parameter, formula_body))

    def create_horizontal_design_table(self, name, comment, copy_mode, sheet_path):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateHorizontalDesignTable
                | o Func CreateHorizontalDesignTable(    CATBSTR    iName,
                |                                        CATBSTR    iComment,
                |                                        boolean    iCopyMode,
                |                                        CATBSTR    iSheetPath) As DesignTable
                |
                | Creates a design table based on a file organized in an horizontal way
                | and adds it to the part's collection of relations.

                | Parameters:
                | iName
                |     The design table name
                |
                |  iComment
                |     A description of the design table
                |
                |  iCopyMode

                |  Returns:
                |   The created design table


                | Examples:
                | This example creates the dt design table
                | and adds it to the newly created part:
                |
                | Dim CATDocs As Documents
                | Dim partdoc As Document
                | Dim part As Part
                | Dim designtable As DesignTable
                | Set CATDocs = CATIA.Documents
                | Set partdoc = CATDocs.Add("CATPart")
                | Set part = partdoc.Part
                | Set designtable = part.Relations.CreateHorizontalDesignTable("dt",
                |           "Mass is less than 10 kg",
                |           TRUE,
                |           "/users/client/data/horizontalsheet.txt")

            :param str name:
            :param str comment:
            :param bool copy_mode:
            :param Path() sheet_path:
            :return: DesignTable()
        """
        return DesignTable(self.relations.CreateHorizontalDesignTable(name, comment, copy_mode, sheet_path))

    def create_law(self, name, comment, law_body):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateLaw
                | o Func CreateLaw(    CATBSTR    iName,
                |                      CATBSTR    iComment,
                |                      CATBSTR    iLawBody) As Law
                |
                | Creates a law relation and adds it to the part's collection of
                | relations.

                | Parameters:
                | iName
                |     The law name
                |
                |  iComment
                |     A description of the law
                |
                |  iLawBody
                |     The law definition

                |  Returns:
                |   The created law

            :param str name:
            :param str comment:
            :param str law_body:

            :return: Law()
        """
        return Law(self.relations.CreateLaw(name, comment, law_body))

    def create_program(self, name, comment, program_body):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateProgram
                | o Func CreateProgram(    CATBSTR    iName,
                |                          CATBSTR    iComment,
                |                          CATBSTR    iProgramBody) As Rule
                |
                | Creates a program relation and adds it to the part's collection of
                | relations.

                | Parameters:
                | iName
                |     The program name
                |
                |  iComment
                |     A description of the program
                |
                |  iProgramBody
                |     The program definition
                |
                |
                |  Returns:
                |   The created program

                | Examples:
                | This example creates the selectdepth program relation
                | and adds it to the newly created part:
                |
                | Dim CATDocs As Documents
                | Dim partdoc As Document
                | Dim part As Part
                | Dim depthProgram As Program
                | Set CATDocs = CATIA.Documents
                | Set partdoc = CATDocs.Add("CATPart")
                | Set part = partdoc.Part
                | Set depthProgram = part.Relations.CreateProgram("selectdepth",
                |           "Select depth with respect to mass",
                |           "if (mass>2kg) { depth=2mm } else { depth=1 mm }")

            :param str name:
            :param str comment:
            :param str program_body:
            :return: Relation()

        """
        return Rule(self.relations.CreateProgram(name, comment, program_body))

    def create_rule_base(self, name):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateRuleBase
                | o Func CreateRuleBase(    CATBSTR    iName) As Relation
                |
                | Creates a rulebase.

                | Parameters:
                | iName
                |    The name of the rulebase.

                |  Returns:
                |      The created rulebase.
                |    See also:
                |   activateLinkAnchor('ExpertRuleBase','','ExpertRuleBase')

        :param str name:
        :return: Relation()
        """
        return Relation(self.relations.CreateRuleBase(name))

    def create_set_of_equations(self, name, comment, formula_body):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateSetOfEquations
                | o Func CreateSetOfEquations(    CATBSTR    iName,
                |                                 CATBSTR    iComment,
                |                                 CATBSTR    iFormulaBody) As SetOfEquation
                |
                | Creates a set of equations.

                | Parameters:
                | iName
                |  The name of the set of equation.
                |  iComment
                |  The comment of the set of equation.
                |  iFormulaBody
                |  The body of the set of equation " a==b+4; c ≤ 90".
                |
                |  Returns:
                |     The created set of equations

        :param str name:
        :param str comment:
        :param str formula_body:
        :return: SetOfEquation()
        """
        return SetOfEquation(self.relations.CreateSetOfEquations(name, comment, formula_body))

    def create_set_of_relations(self, parent):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateSetOfRelations
                | o Sub CreateSetOfRelations(    AnyObject    iParent)
                |
                | Creates a set of relations and appends it to a parent object.

                | Parameters:
                | iParent
                |  The object to which the set is appended

        :param parent:
        :return: Relations()
        """
        return Relations(self.relations.CreateSetOfRelations(parent.parent))

    def generate_xml_report_for_checks(self, name):
        """
        .. note::
            CAA V5 Visual Basic help

                | GenerateXMLReportForChecks
                | o Sub GenerateXMLReportForChecks(    CATBSTR    iName)
                |
                | Generates an XML Report on all checks in the current document.

                | Parameters:
                | iName
                |  The name of the XML file
            :param str name:
            :return:
        """
        self.relations.GenerateXMLReportForChecks(name)

    def item(self, index):
        """
        .. warning::

        The index when not a string must be it's python index (indexes in python start from 0).
        collection. The COM interface index starts at 1.


        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item(    CATVariant    iIndex) As Relation
                |
                | Retrieves a relation using its index or its name from the Relations
                | collection.

                | Parameters:
                | iIndex
                |    The index or the name of the relation to retrieve from
                |    the collection of relations.
                |    As a numeric, this index is the rank of the relation
                |    in the collection.
                |    The index of the first relation in the collection is 1, and
                |    the index of the last relation is Count.
                |    As a string, it is the name you assigned to the relation using
                |    the
                |
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property or when creating the relation.
                |    Returns:
                |   The retrieved relation

                | Examples:
                | This example retrieves the last relation in the relations
                | collection.
                |
                | Dim lastRelation As Relation
                | Set lastRelation = relations.Item(relations.Count)

            :param str or int index:
            :return: Relation()
        """

        if isinstance(index, int):
            index += 1

        return Relation(self.relations.Item(index))

    def sub_list(self, feature, recursively):
        """
        .. note::
            CAA V5 Visual Basic help

                | SubList
                | o Func SubList(    AnyObject    iFeature,
                |                    boolean    iRecursively) As Relations
                |
                | Returns a sub-collection of relations aggregated to an object.

                | Parameters:
                | iFeature
                |  The object used to filter the the whole relation collection
                |  to get the resulting sub-collection.
                |
                |  iRecursively
                |  A flag to specify if children parameters are to be searched for in the returned
                |  collection

                |  Returns:
                |   The resulting sub-collection

                | Examples:
                | This example shows how to get a collection of relations that are under a Pad
                |
                | Dim Relations1 As Relations
                | Dim Body0 As AnyObject
                | Dim Pad1 As AnyObject
                | Dim Relations2 As Relations
                | Set Relations1 = CATIA.ActiveDocument.Part.Relations
                | Set Body0 = CATIA.ActiveDocument.Part.Bodies.Item("MechanicalTool.1")
                | Set Pad1 = Body0.Shapes.Item("Pad.1")
                | 'gets the collection of relations that are under the pad Pad.1
                | Set Relations2 = Relations1.SubList(Pad1, TRUE)
        """

        return self.relations.SubList(feature, recursively)

    def remove(self, index):
        """

        .. warning::

            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.

        .. note::
            CAA V5 Visual Basic help

                | Remove
                | o Sub Remove(    CATVariant    iIndex)
                |
                | Removes a relation from the Relations collection.

                | Parameters:
                | iIndex
                |    The index or the name of the relation to remove from
                |    the collection of relations.
                |    As a numeric, this index is the rank of the relation
                |    in the collection.
                |    The index of the first relation in the collection is 1, and
                |    the index of the last relation is Count.
                |    As a string, it is the name you assigned to the relation using
                |    the
                |
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property or when creating the relation.

                | Examples:
                | This example removes the relation named density from
                | the relations collection.
                |
                | relations.Remove("density")

            :param str|int index:
        """

        if isinstance(index, int):
            index += 1

        self.relations.Remove(index)

    def __repr__(self):
        return f'Relations(name="{self.name}")'
