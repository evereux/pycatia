#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 08:14:46.168311

from .parameter import Parameter


class EnumParam(Parameter):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the enum parameter.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.enum_param = com_object

    @property
    def value_enum(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ValueEnum
                | o Property ValueEnum(    ) As
                |
                | Returns or sets the value of the EnumParameter object. Units
                | are expressed in the IS unit system, except for lengthes
                | expressed in millimeters, and angles expressed in decimal
                | degrees.
                |
                | Example:
                | This example sets the param1 value to 1 if
                | its value is greater than 2.5:
                | If (density.Value > 2.5) Then
                |   density.Value = 1
                | End If

        :return: str
        """
        return self.enum_param.ValueEnum

    @value_enum.setter
    def value_enum(self, value):
        """
            :param str value:
        """
        self.enum_param.ValueEnum = value

    def __repr__(self):
        return f'EnumParam()'
