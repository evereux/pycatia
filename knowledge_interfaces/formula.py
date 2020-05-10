#! /usr/bin/python3.7
from pycatia.knowledge_interfaces.relation import Relation


class Formula(Relation):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the formula relation.T
                | Examples:
                | The following example shows how to
                | create a formula that computes the mass of a cuboid, given its
                | geometric dimensions and the density of the material it is made of:
                |
                | Dim CATDocs As Documents
                | Dim part1 As Document
                | Dim width As RealParam
                | Dim height As RealParam
                | Dim depth As RealParam
                | Dim density As RealParam
                | Dim mass As RealParam
                | Dim computemass As RealParam
                | Dim formel As String
                |
                | Set CATDocs = CATIA.Documents
                | Set part1 = CATDocs.Add("CATPart")
                | Set width = part1.Part.Parameters.CreateReal("width", 1.)
                | Set height = part1.Part.Parameters.CreateReal("height", 2.)
                | Set depth = part1.Part.Parameters.CreateReal("depth", 3.)
                | Set density = part1.Part.Parameters.CreateReal("density", 1.5)
                | Set mass = part1.Part.Parameters.CreateReal("mass", 0.)
                |
                | formel = "(width*height*depth)*density"
                | Set computemass = part1.Part.Relations.CreateFormula("computemass",
                |                                                      "Computes the cuboid mass",
                |                                                      mass,
                |                                                      formel)
    """

    # def __init__(self, formula):
    #     self.formula = formula

    def __init__(self, name=None, comment=None, output_parameter=None, formula_body=None,
                 parent=None):

        if formula_body and not isinstance(formula_body, str):
            raise ValueError(f'Parameter formula_body [{formula_body}] has to be str()')

        self.relations = self.set_relations(parent)
        self.formula = Relation(self.relations.CreateFormula(
            name, comment, output_parameter, formula_body))

    def set_relations(self, parent):
        try:
            # if parent is <class "Relations">
            return parent.relations
        except AttributeError:
            # if parent is something like Catia.ActiveDocument.Part.Relations
            return parent
