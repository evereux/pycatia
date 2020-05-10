#! /usr/bin/python3.7
from pycatia.knowledge_interfaces.relation import Relation


class Parameter:
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the parameter.It can be computed from a relation: formula,
                | program, or check. It is an abstract object which is not intended to
                | be created as such, but from which the integer, bolean, real, and
                | string parameters derive.
                |
                | Here is an example to create one:
                | Dim CATDocs As Documents
                | Set CATDocs = CATIA.Documents
                | Dim part1 As Document
                | Set part1 = CATDocs.Add("CATPart")
                | Dim density As RealParam
                | Set density = part1.Part.Parameters.CreateReal("density", 2.5)

    """

    def __init__(self, parameter):
        self.parameter = parameter

    @property
    def comment(self):
        """

        :return: str
        """
        return self.parameter.Comment

    @comment.setter
    def comment(self, comment):
        self.parameter.Comment = comment

    @property
    def context(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Context
                | o Property Context(    ) As AnyObject
                |
                | Returns the context of the parameter : a part, a product, a drafting,
                | a process, depending where the parameter is.
        """
        return self.parameter.Context

    @property
    def formula_name(self):
        if self.parameter.name.find("\\"):
            return self.parameter.name.split("\\", 1)[1]

        return self.parameter.name

    @property
    def is_true_parameter(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsTrueParameter
                | o Property IsTrueParameter(    ) As boolean
                |
                | Returns a boolean saying if the parameter is a true one (real,
                | dimension, string, etc.) or a geometrical one (isolated points,
                | curves, surfaces).
        """
        return self.parameter.IsTrueParameter

    @property
    def optional_relation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OptionalRelation
                | o Property OptionalRelation(    ) As Relation
                |
                | Returns the relation that can be used to compute the parameter. As
                | this relation might not exist, NULL may be returned, so a test is
                | required.

                | Example:
                | This example checks if there is a relation to compute the param1
                | parameter, and if no relation exists, displays a message box:
                |
                | Set param1_rel = param1.OptionalRelation
                | If param1_rel is Nothing Then
                |     MsgBox "No relation to compute param1" End If
        """
        if self.has_relation():
            return Relation(self.parameter.OptionalRelation)

    @property
    def name(self):
        """

        :return: str
        """
        return self.parameter.Name

    @property
    def read_only(self):
        return self.parameter.ReadOnly

    @property
    def type(self):
        """
        Returns the last element of parlament

        | Example:
        | Parameter.Name = Part.Name\\GeometricalSet\\SubGeometricalSet\\Element\\Radius
        | Parameter.type = Radius
        | EngineNom = Engine.Nomenclature

        :return: str
        """
        if self.is_renamed():
            return self.parameter.name00
        else:
            return self.parameter.name.rsplit("\\")[-1]

    @property
    def user_access_mode(self):
        """
        Returns the user access mode of the parameter:
        0 - Read only parameter (cannot be destroyed).
        1 - Read/write parameter (cannot be destroyed).
        2 - User parameter (can be read, written and destroyed).
        """
        return self.parameter.UserAccessMode

    @property
    def value(self):
        return self.parameter.Value

    @value.setter
    def value(self, value):
        self.parameter.Value = value

    def attributes(self):
        """
        Returns a string describing the parameter attributes.

        :return: str
        """

        return ('(Parameter) Attributes... \n'
                f'Name:                  {self.name}\n'
                f'Type:                  {self.type}\n'
                f'Class:                 {type(self)}\n'
                f'Comment:               {self.comment}\n'
                f'Context:               {self.context}\n'
                f'Visible:               {self.isVisible()}\n'
                f'Renamed:               {self.is_renamed()}\n'
                f'Read only:             {self.read_only}\n'
                f'Relation:              {self.has_relation()}')

    def has_relation(self):
        if self.parameter.OptionalRelation:
            return True

        return False

    def is_renamed(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Renamed
                | o Property Renamed(    ) As boolean
                |
                | Returns a boolean saying if the parameter is a renamed parameter or
                | not.
        """
        return self.parameter.Renamed

    def is_visible(self):
        """

        :return: bool
        """
        return not self.parameter.Hidden

    def rename(self, new_name):
        self.parameter.Rename(new_name)

    def set_visible(self, state):
        self.parameter.Hidden = not state

    def valuate_from_string(self, i_value):
        """
        .. note::
            CAA V5 Visual Basic help

                | ValuateFromString
                | o Sub ValuateFromString(    CATBSTR    iValue)
                |
                | Valuates a parameter using a string as input. The string depends on
                | parameter nature : "True" or "False" for Boolean a numerical value for
                | Integer or Real a numerical value with or without a unit for Dimension


                | Parameters:
                | iValue
                |    The value to assign to the dimension parameter
                |
                | Examples:
                | This example sets the value of the existing dimension parameter
                | to a new value:
                |
                | dimension.ValuateFromString("300mm");
        """
        return self.parameter.ValuateFromString(i_value)

    def value_as_string(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ValueAsString
                | o Func ValueAsString(    ) As CATBSTR
                |
                | Returns the value of the parameter as a string.
        """
        return self.parameter.ValueAsString()

    def __repr__(self):
        return "(Parameter) {}".format(self.name)
