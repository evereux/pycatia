#! /usr/bin/python3.6

from .base_object import BaseKnowledge


class Relation(BaseKnowledge):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the relation object.It is an abstract object which is not
                | intended to be created as such, but from which the check, design
                | table, formula, rule, objects derive.
    """

    def __init__(self, relation):
        super().__init__(relation)
        self.relation = relation

    @property
    def context(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Context
                | o Property Context(    ) As AnyObject
                |
                | Returns the context of the parameter. The context of a parameter can
                | be a part, a product, a drafting, or a process document, depending
                | where the parameter is.  Returns:   The context    See also:
                | activateLinkAnchor('Part','','Part') ,
                | activateLinkAnchor('Product','','Product') , CATIADrawing,
                | CATIAProcess
        """
        return self.relation.Context

    @property
    def nb_in_parameters(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NbInParameters
                | o Property NbInParameters(    ) As long
                |
                | Returns the number of input parameters of the relation.
        """
        return self.relation.NbInParameters

    @property
    def nb_out_parameters(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NbOutParameters
                | o Property NbOutParameters(    ) As long
                |
                | Returns the number of output parameters of the relation. The output
                | parameters of the relation are those constrained by the relation.
        """
        return self.relation.NbOutParameters

    @property
    def value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Value
                | o Property Value(    ) As CATBSTR
                |
                | Returns the definition of the relation.  It returns an empty string if
                | the relation is not an expressional one (for example for a design
                | table). The definition is the body to be executed to compute one or
                | several parameters. It is passed as the last input argument of the
                | relation creation methods of the
                | activateLinkAnchor('Relations','','Relations')  collection.

                | Example:
                | This example retrieves the maximummass relation definition and
                | displays it in a message box:
                | reldef = maximummass.Value
                | MsgBox "maximummass relation is defined as " & reldef
        """
        return self.relation.Value

    @value.setter
    def value(self, value):
        self.relation.Value = value

    def get_in_parameter(self, index):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetInParameter
                | o Func GetInParameter(    long    iIndex) As AnyObject
                |
                | Returns an input parameter of the relation. This method can return an
                | object that is not a parameter, that is, you cannot handle it as a
                | Parameter object.
                | For example, in a relation like Area.1 = area(PartBody\\Pad.1\\Sketch.1) the
                | object PartBody\\Pad.1\\Sketch.1 is a sketch and not a parameter. To use such an
                | object, call the Visual Basic TypeName function to retrieve its real type.
                | Dim objectType objectType = TypeName(oParameter)
                | If objectType = "Parameter" Then ...

                | Parameters:
                | iIndex
                |  The searched input parameter index in the relation.
                |  Legal values: 1 ≤ iIndex ≤
                |
                |  activateLinkAnchor('','NbInParameters','NbInParameters')
        """
        return self.relation.GetInParameter(index)

    def get_out_parameter(self, index):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOutParameter
                | o Func GetOutParameter(    long    iIndex) As Parameter
                |
                | Returns an output parameter of the relation.  Use TypeName method on
                | the returned parameter to get the real type of the parameter.

                | Parameters:
                | iIndex
                |  The searched input parameter index in the relation.
                |  Legal values: 1 ≤ iIndex ≤
                |
                |  activateLinkAnchor('','NbOutParameters','NbOutParameters')
        """
        return self.relation.GetOutParameter(index)

    def modify(self, value):
        """
        .. note::
            CAA V5 Visual Basic help

                | Modify
                | o Sub Modify(    CATBSTR    iValue)
                |
                | Modifies the relation.

                | Parameters:
                | iValue
                |    The new relation value
        """
        return self.relation.Modify(value)

    def rename(self, name):
        """
        .. note::
            CAA V5 Visual Basic help

                | Rename
                | o Sub Rename(    CATBSTR    iName)
                |
                | Renames the relation.

                | Parameters:
                | iName
                |    The new relation name
        """
        return self.relation.Rename(name)

    def __repr__(self):
        return f'Relation(value="{self.value}")'
