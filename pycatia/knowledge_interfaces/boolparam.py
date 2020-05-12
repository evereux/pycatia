#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.knowledge_interfaces.parameter import Parameter


class BoolParam(Parameter):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the boolean parameter.The following example shows how to
                | create it:Dim CATDocs As Documents  Set CATDocs      = CATIA.Documents
                | Dim part1 As Document  Set part1        = CATDocs.Add("CATPart")
                | Dim availability As BooleanParam  Set availability =
                | part1.Parameters.CreateBoolean("availability", True)

    """

    def __init__(self, com_boolean_parameter):
        super().__init__(com_boolean_parameter)

    @property
    def value(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Value
                | o Property Value(    ) As boolean
                |
                | Returns or sets the value of the boolean parameter.  Example: This
                | example sets the availability boolean parameter value to True if its
                | value is False:  If (availability.Value = False)  Then
                | availability.Value = True End If


                | Parameters:


        """
        return self.parameter.Value

    @value.setter
    def value(self, value):
        self.parameter.value = value

    def __repr__(self):
        return f'BoolParam(name="{self.name}". value="{self.value}")'
