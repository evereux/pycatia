#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.knowledge_interfaces.parameter import Parameter


class EnumParam(Parameter):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the enum parameter.

    """

    def __init__(self, parameter_com_object):
        super().__init__(parameter_com_object)
        self.enumparam = parameter_com_object

    @property
    def value_enum(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ValueEnum
                | o Property ValueEnum(    ) As CATBSTR
                | 
                | Returns or sets the value of the EnumParameter object. Units are
                | expressed in the IS unit system, except for lengthes expressed in
                | millimeters, and angles expressed in decimal degrees.  Example: This
                | example sets the param1 value to 1 if its value is greater than 2.5:
                | If (density.Value > 2.5)  Then     density.Value = 1 End If


                | Parameters:


        """
        return self.enumparam.ValueEnum
