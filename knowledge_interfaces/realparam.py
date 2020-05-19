#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.knowledge_interfaces.parameter import Parameter


class RealParam(Parameter):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the real parameter.The following example shows how to
                | create it:Dim CATDocs As Documents  Set CATDocs = CATIA.Documents  Dim
                | part1 As Document  Set part1   = CATDocs.Add("CATPart")  Dim density
                | As RealParam  Set density =
                | part1.Part.Parameters.CreateReal("density", 2.5)The real parameter is
                | the base object for dimensions.

    """

    def __init__(self, com_real_parameter):
        super().__init__(com_real_parameter)

    @property
    def maximum_tolerance(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MaximumTolerance
                | o Property MaximumTolerance(    ) As double
                |
                | Returns or sets the value of the maximum tolerance of a parameter.
                | Units are expressed in the IS unit system.  Example: This example sets
                | the MaximumTolerance value to 0 if its value is bigger than 0:  If
                | (Length.MaximumTolerance < 0.0)  Then     Length.MaximumTolerance =
                | 0.0 End If


                | Parameters:


        """
        return self.parameter.MaximumTolerance

    @property
    def minimum_tolerance(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MinimumTolerance
                | o Property MinimumTolerance(    ) As double
                |
                | Returns or sets the value of the minimum tolerance of a parameter.
                | Units are expressed in the IS unit system.  Example: This example sets
                | the MinumumTolerance value to 0 if its value is bigger than 0:  If
                | (Length.MinimumTolerance > 0.0)  Then     Length.MinimumTolerance =
                | 0.0 End If


                | Parameters:


        """
        return self.parameter.MinimumTolerance

    @property
    def range_max(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RangeMax
                | o Property RangeMax(    ) As double
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
                | o Property RangeMaxValidity(    ) As long
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
                | o Property RangeMin(    ) As double
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
                | o Property RangeMinValidity(    ) As long
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
                | Returns an array containing the different values that the real param
                | can take in the case of multiple values.  Example: Dim enumValues ()
                | as Variant ReDim enumValues (aRealParameter.GetEnumerateValuesSize() -
                | 1) aRealParameter.GetEnumerateValues(enumValues) For i =
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

    def is_equal_to(self, i_value_to_compare):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsEqualTo
                | o Func IsEqualTo(    double    iValueToCompare) As boolean
                |
                | Tests the equality of the parameter value with a given value.


                | Parameters:
                | iValueToCompare
                |    The value to compare the parameter value with
                |
                |
                |  Returns:
                |
                | True
                | If the current value of the parameter (the one get by the get_Value property, for dimensions
                |  notice that it is not the MKS value) is equal to the one given in argument.
                |  Notice that two values are considered as equal if their difference is insignificant faced with the
                |  two compared values. This method allows you to avoid problems due to computation errors.
                | False
                | If the two values are different.


        """
        return self.parameter.IsEqualTo(i_value_to_compare)

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
                | o Sub SuppressEnumerateValues(    )
                |
                | Resets the status of the object to a single value object.


                | Parameters:


        """
        return self.parameter.SuppressEnumerateValues()

    def __repr__(self):
        return f'RealParam(name="{self.name}". value="{self.value}")'
