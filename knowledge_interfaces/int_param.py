#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.knowledge_interfaces.parameter import Parameter


class IntParam(Parameter):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the integer parameter.The following example shows how to
                | create it:Dim CATDocs As Documents Set CATDocs = CATIA.Documents Dim
                | part1 As Dccument Set part1   = CATDocs.Add("CATPart")  Dim  year As
                | IntParam Set year    = part1.Part.Parameters.CreateInteger("year",
                | 1998)

    """

    def __init__(self, com_int_parameter):
        super().__init__(com_int_parameter)

    @property
    def range_max(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RangeMax
                | o Property RangeMax() As long
                |
                | Returns or sets the value of the upper bound that the parameter object
                | value can take.  Example: This example sets the RangeMax value to 0 if
                | its value is smaller than 0:  If (Length.RangeMax < 0.0 and
                | Length.RangeMaxValidity <> 0)  Then     Length.RangeMax = 0.0 End If


                | Parameters:


        """
        return self.parameter.RangeMax

    @property
    def range_max_validity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RangeMaxValidity
                | o Property RangeMaxValidity() As long
                |
                | Returns or sets the type of the upper bound of the parameter. 0the
                | upper bound is meaningless 1the upper bound can be reached 2the upper
                | bound cannot be reached


                | Parameters:


        """
        return self.parameter.RangeMaxValidity

    @property
    def range_min(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RangeMin
                | o Property RangeMin() As long
                |
                | Returns or sets the value of the lower bound that the parameter object
                | value can take.  Example: This example sets the RangeMin value to 0 if
                | its value is bigger than 0:  If (Length.RangeMin > 0.0 and
                | Length.RangeMinValidity <> 0)  Then     Length.RangeMin = 0.0 End If


                | Parameters:


        """
        return self.parameter.RangeMin

    @property
    def range_min_validity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RangeMinValidity
                | o Property RangeMinValidity() As long
                |
                | Returns or sets the type of the lower bound of the parameter. 0the
                | lower bound is meaningless 1the lower bound can be reached 2the lower
                | bound cannot be reached


                | Parameters:


        """
        return self.parameter.RangeMinValidity

    def get_enumerate_values(self, o_safe_array):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetEnumerateValues
                | o Sub GetEnumerateValues(    CATSafeArrayVariant    oSafeArray)
                |
                | Returns an array containing the different values that the int param
                | can take in the case of multiple values.  Example: Dim enumValues ()
                | as Variant ReDim enumValues
                | (anIntegerParameter.GetEnumerateValuesSize() - 1)
                | anIntegerParameter.GetEnumerateValues(enumValues) For i =
                | LBound(enumValues) to UBound(enumValues)   ... Next


                | Parameters:


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
                | Sets an array containing the different values that the real param can
                | take in the case of multiple values.


                | Parameters:


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


                | Parameters:


        """
        return self.parameter.SuppressEnumerateValues()

    def __repr__(self):
        return f'IntParam(name="{self.name}". value="{self.value}")'
