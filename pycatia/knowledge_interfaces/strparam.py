#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.knowledge_interfaces.parameter import Parameter


class StrParam(Parameter):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the string parameter.The following example shows how to
                | create it:Dim CATDocs As Documents Set CATDocs = CATIA.Documents Dim
                | part1 As Document Set part1   = CATDocs.Add("CATPart") Dim material As
                | String Set material = part1.Parameters.CreateString("material",
                | "glass")

    """

    def __init__(self, com_string_parameter):
        super().__init__(com_string_parameter)

    def get_enumerate_values(self, o_safe_array):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetEnumerateValues
                | o Sub GetEnumerateValues(    CATSafeArrayVariant    oSafeArray)
                |
                | Returns an array containing the different values that the real param
                | can take in the case of multiple values.  Example: Dim enumValues ()
                | as Variant ReDim enumValues (aStrParameter.GetEnumerateValuesSize() -
                | 1) aStrParameter.GetEnumerateValues(enumValues) For i =
                | LBound(enumValues) to UBound(enumValues)   ... Next


                | Parameters:


        """
        return self.parameter.GetEnumerateValues(o_safe_array)

    def get_enumerate_values_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetEnumerateValuesSize
                | o Func GetEnumerateValuesSize(    ) As long
                |
                | Returns the number of enumerate values.


                | Parameters:


        """
        return self.parameter.GetEnumerateValuesSize()

    def set_enumerate_values(self, i_safe_array):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetEnumerateValues
                | o Sub SetEnumerateValues(    CATSafeArrayVariant    iSafeArray)
                |
                | Sets an array containing the different values that the StrParam object
                | can take in the case of multiple values.


                | Parameters:
                | The
                |  array of enumerated values.


        """
        return self.parameter.SetEnumerateValues(i_safe_array)

    def suppress_enumerate_values(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SuppressEnumerateValues
                | o Sub SuppressEnumerateValues(    )
                |
                | Resets the status of the object to a single value object.


                | Parameters:


        """
        return self.parameter.SuppressEnumerateValues()

    def __repr__(self):
        return f'StrParam(name="{self.name}". value="{self.value}")'
