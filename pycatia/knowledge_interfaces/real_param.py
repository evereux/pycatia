#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter


class RealParam(Parameter):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.Parameter
                |                         RealParam
                | 
                | Represents the real parameter.
                | The following example shows how to create it:
                | 
                |   Dim CATDocs As Documents
                |   Set CATDocs = CATIA.Documents
                |   Dim part1 As Document
                |   Set part1   = CATDocs.Add("CATPart")
                |   Dim density As RealParam
                |   Set density = part1.Part.Parameters.CreateReal("density", 2.5)
                |  
                | 
                | The real parameter is the base object for dimensions.
                | 
                | See also:
                |     Dimension
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.real_param = com_object

    @property
    def maximum_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property MaximumTolerance() As double
                | 
                |     Returns or sets the value of the maximum tolerance of a parameter. Units
                |     are expressed in the IS unit system.
                | 
                |     Example:
                |         This example sets the MaximumTolerance value to 0 if its value is
                |         bigger than 0:
                | 
                |          If (Length.MaximumTolerance < 0.0)  Then
                |              Length.MaximumTolerance = 0.0
                |          End If

        :rtype: float
        """

        return self.real_param.MaximumTolerance

    @maximum_tolerance.setter
    def maximum_tolerance(self, value: float):
        """
        :param float value:
        """

        self.real_param.MaximumTolerance = value

    @property
    def minimum_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property MinimumTolerance() As double
                | 
                |     Returns or sets the value of the minimum tolerance of a parameter. Units
                |     are expressed in the IS unit system.
                | 
                |     Example:
                |         This example sets the MinumumTolerance value to 0 if its value is
                |         bigger than 0:
                | 
                |          If (Length.MinimumTolerance > 0.0)  Then
                |              Length.MinimumTolerance = 0.0
                |          End If

        :rtype: float
        """

        return self.real_param.MinimumTolerance

    @minimum_tolerance.setter
    def minimum_tolerance(self, value: float):
        """
        :param float value:
        """

        self.real_param.MinimumTolerance = value

    @property
    def range_max(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RangeMax() As double
                | 
                |     Returns or sets the value of the upper bound that the parameter object
                |     value can take.
                | 
                |     Example:
                |         This example sets the RangeMax value to 0 if its value is smaller than
                |         0:
                | 
                |          If (Length.RangeMax < 0.0 and Length.RangeMaxValidity <> 0) 
                |          Then
                |              Length.RangeMax = 0.0
                |          End If

        :rtype: float
        """

        return self.real_param.RangeMax

    @range_max.setter
    def range_max(self, value: float):
        """
        :param float value:
        """

        self.real_param.RangeMax = value

    @property
    def range_max_validity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RangeMaxValidity() As long
                | 
                |     Returns or sets the type of the upper bound of the
                |     parameter.
                | 
                |     0
                |         the upper bound is meaningless 
                |     1
                |         the upper bound can be reached 
                |     2
                |         the upper bound cannot be reached

        :rtype: int
        """

        return self.real_param.RangeMaxValidity

    @range_max_validity.setter
    def range_max_validity(self, value: int):
        """
        :param int value:
        """

        self.real_param.RangeMaxValidity = value

    @property
    def range_min(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RangeMin() As double
                | 
                |     Returns or sets the value of the lower bound that the parameter object
                |     value can take.
                | 
                |     Example:
                |         This example sets the RangeMin value to 0 if its value is bigger than
                |         0:
                | 
                |          If (Length.RangeMin > 0.0 and Length.RangeMinValidity <> 0) 
                |          Then
                |              Length.RangeMin = 0.0
                |          End If

        :rtype: float
        """

        return self.real_param.RangeMin

    @range_min.setter
    def range_min(self, value: float):
        """
        :param float value:
        """

        self.real_param.RangeMin = value

    @property
    def range_min_validity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RangeMinValidity() As long
                | 
                |     Returns or sets the type of the lower bound of the
                |     parameter.
                | 
                |     0
                |         the lower bound is meaningless 
                |     1
                |         the lower bound can be reached 
                |     2
                |         the lower bound cannot be reached

        :rtype: int
        """

        return self.real_param.RangeMinValidity

    @range_min_validity.setter
    def range_min_validity(self, value: int):
        """
        :param int value:
        """

        self.real_param.RangeMinValidity = value

    @property
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Value() As double
                | 
                |     Returns or sets the value of the real parameter. Units are expressed in the
                |     IS unit system, except for lengths expressed in millimeters, and angles
                |     expressed in decimal degrees.
                | 
                |     Example:
                |         This example sets the density value to 1 if its value is greater than
                |         2.5:
                | 
                |          If (density.Value > 2.5)  Then
                |              density.Value = 1
                |          End If

        :rtype: float
        """

        return self.real_param.Value

    @value.setter
    def value(self, value: float):
        """
        :param float value:
        """

        self.real_param.Value = value

    def get_enumerate_values(self, o_safe_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetEnumerateValues(CATSafeArrayVariant oSafeArray)
                | 
                |     Returns an array containing the different values that the real param can
                |     take in the case of multiple values.
                | 
                |     Example:
                | 
                |          Dim enumValues () as Variant
                |          ReDim enumValues (aRealParameter.GetEnumerateValuesSize() -
                |          1)
                |          aRealParameter.GetEnumerateValues(enumValues)
                |          For i = LBound(enumValues) to UBound(enumValues)
                |            ...
                |          Next

        :param tuple o_safe_array:
        :rtype: None
        """
        return self.real_param.GetEnumerateValues(o_safe_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_enumerate_values'
        # # vba_code = """
        # # Public Function get_enumerate_values(real_param)
        # #     Dim oSafeArray (2)
        # #     real_param.GetEnumerateValues oSafeArray
        # #     get_enumerate_values = oSafeArray
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_enumerate_values_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetEnumerateValuesSize() As long
                | 
                |     Returns the number of enumerate values.

        :rtype: int
        """
        return self.real_param.GetEnumerateValuesSize()

    def is_equal_to(self, i_value_to_compare: float) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func IsEqualTo(double iValueToCompare) As boolean
                | 
                |     Tests the equality of the parameter value with a given
                |     value.
                | 
                |     Parameters:
                | 
                |         iValueToCompare
                |             The value to compare the parameter value with 
                | 
                |     Returns:
                | 
                |         True
                |             If the current value of the parameter (the one get by the get_Value
                |             property, for dimensions notice that it is not the MKS value) is equal to the
                |             one given in argument. Notice that two values are considered as equal if their
                |             difference is insignificant faced with the two compared values. This method
                |             allows you to avoid problems due to computation
                |             errors.
                |         False
                |             If the two values are different.

        :param float i_value_to_compare:
        :rtype: bool
        """
        return self.real_param.IsEqualTo(i_value_to_compare)

    def set_enumerate_values(self, i_safe_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetEnumerateValues(CATSafeArrayVariant iSafeArray)
                | 
                |     Sets an array containing the different values that the real param can take
                |     in the case of multiple values.

        :param tuple i_safe_array:
        :rtype: None
        """
        return self.real_param.SetEnumerateValues(i_safe_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_enumerate_values'
        # # vba_code = """
        # # Public Function set_enumerate_values(real_param)
        # #     Dim iSafeArray (2)
        # #     real_param.SetEnumerateValues iSafeArray
        # #     set_enumerate_values = iSafeArray
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def suppress_enumerate_values(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SuppressEnumerateValues()
                | 
                |     Resets the status of the object to a single value object.

        :rtype: None
        """
        return self.real_param.SuppressEnumerateValues()

    def __repr__(self):
        return f'RealParam(name="{ self.name }")'
