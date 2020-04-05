#! /usr/bin/python3.7


class Parameter:
    """
    .. note::
        CAA V5 Visual Basic help

        Represents the Parameter.


    :param part: CATIA Parameter COM object.
    """

    def __init__(self, parameter):
        self.parameter = parameter

    @property
    def value(self):
        return self.parameter.Value

    @value.setter
    def value(self, value):
        self.parameter.Value = value

    @property
    def name(self):
        """

        :return: str
        """
        return self.parameter.Name

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

        :return: str
        """
        return self.parameter.Context

    @property
    def hidden(self):
        """

        :return: bool
        """
        return self.parameter.Hidden

    @hidden.setter
    def hidden(self, hidden):
        self.parameter.Hidden = hidden

    @property
    def true_parameter(self):
        return self.parameter.IsTrueParameter

    @property
    def relation(self):
        return self.parameter.OptionalRelation

    @property
    def read_only(self):
        return self.parameter.ReadOnly

    def is_renamed(self):
        """

        :return: bool
        """
        return self.parameter.Renamed

    @property
    def user_access_mode(self):
        """
        Returns the user access mode of the parameter:
        0 - Read only parameter (cannot be destroyed).
        1 - Read/write parameter (cannot be destroyed).
        2 - User parameter (can be read, written and destroyed).
        """
        return self.parameter.UserAccessMode

    def rename(self, new_name):
        self.parameter.Rename(new_name)

    def valuate_from_string(self, value):
        self.parameter.dimension.ValuateFroMString(value)

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
            return "UserType"
        else:
            return self.parameter.name.rsplit("\\")[-1]
