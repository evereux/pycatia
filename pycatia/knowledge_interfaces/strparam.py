#! /usr/bin/python3.7
from pycatia.knowledge_interfaces.parameter import Parameter


class StrParam(Parameter):
    def __init__(self, name=None, value=None, parameter=None, parent=None):
        if value and not isinstance(value, str):
            raise ValueError(f'Parameter value [{value}] has to be str()')

        self.parameters = self.set_parameters(parent)

        if parameter:
            self.parameter = parameter
        else:
            self.parameter = Parameter(self.parameters.CreateBoolean(name, value))

    def set_parameters(self, parent):
        try:
            # if parent is <class "Parameters">
            return parent.parameters
        except AttributeError:
            # if parent is something like Catia.ActiveDocument.Part.Parameters
            return parent

    def get_enumerate_values(self, o_safe_array):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetEnumerateValues
                | o Sub GetEnumerateValues(CATSafeArrayVariant oSafeArray)
                |
                | Returns an array containing the different values that the real param
                | can take in the case of multiple values.

                | Example:
                | Dim enumValues() as Variant
                | ReDim enumValues(aStrParameter.GetEnumerateValuesSize() - 1)
                | aStrParameter.GetEnumerateValues(enumValues)
                | For i = LBound(enumValues) to UBound(enumValues)
                |     ...
                | Next
        """
        return self.parameter.GetEnumerateValues(o_safe_array)

    def get_enumerate_values_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetEnumerateValuesSize
                | o Func GetEnumerateValuesSize() As long
                |
                | Returns the number of enumerate values.
        """
        return self.parameter.GetEnumerateValuesSize()

    def set_enumerate_values(self, i_safe_array):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetEnumerateValues
                | o Sub SetEnumerateValues(CATSafeArrayVariant iSafeArray)
                |
                | Sets an array containing the different values that the StrParam object
                | can take in the case of multiple values.

                | Parameters:
                | The array of enumerated values.
        """
        return self.parameter.SetEnumerateValues(i_safe_array)

    def suppress_enumerate_values(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SuppressEnumerateValues
                | o Sub SuppressEnumerateValues()
                |
                | Resets the status of the object to a single value object.
        """
        return self.parameter.SuppressEnumerateValues()
