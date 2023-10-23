#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter


class IntParam(Parameter):

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
                |                         IntParam
                | 
                | Represents the integer parameter.
                | The following example shows how to create it:
                | 
                |  Dim CATDocs As Documents
                |  Set CATDocs = CATIA.Documents
                |  Dim part1 As Dccument
                |  Set part1   = CATDocs.Add("CATPart") 
                |  Dim  year As IntParam
                |  Set year    = part1.Part.Parameters.CreateInteger("year", 1998)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.int_param = com_object

    @property
    def range_max(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RangeMax() As long
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

        :rtype: int
        """

        return self.int_param.RangeMax

    @range_max.setter
    def range_max(self, value: int):
        """
        :param int value:
        """

        self.int_param.RangeMax = value

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

        return self.int_param.RangeMaxValidity

    @range_max_validity.setter
    def range_max_validity(self, value: int):
        """
        :param int value:
        """

        self.int_param.RangeMaxValidity = value

    @property
    def range_min(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RangeMin() As long
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

        :rtype: int
        """

        return self.int_param.RangeMin

    @range_min.setter
    def range_min(self, value: int):
        """
        :param int value:
        """

        self.int_param.RangeMin = value

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

        return self.int_param.RangeMinValidity

    @range_min_validity.setter
    def range_min_validity(self, value: int):
        """
        :param int value:
        """

        self.int_param.RangeMinValidity = value

    @property
    def value(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Value() As long
                | 
                |     Returns or sets the value of the integer parameter. Units are expressed in
                |     the IS unit system.
                | 
                |     Example:
                |         This example sets the year value to 0 if its value is equal to
                |         2000:
                | 
                |          If (year.Value = 2000)  Then
                |              year.Value = 0
                |          End If

        :rtype: int
        """

        return self.int_param.Value

    @value.setter
    def value(self, value: int):
        """
        :param int value:
        """

        self.int_param.Value = value

    def get_enumerate_values(self, o_safe_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetEnumerateValues(CATSafeArrayVariant oSafeArray)
                | 
                |     Returns an array containing the different values that the int param can
                |     take in the case of multiple values.
                | 
                |     Example:
                | 
                |          Dim enumValues () as Variant
                |          ReDim enumValues (anIntegerParameter.GetEnumerateValuesSize() -
                |          1)
                |          anIntegerParameter.GetEnumerateValues(enumValues)
                |          For i = LBound(enumValues) to UBound(enumValues)
                |            ...
                |          Next

        :param tuple o_safe_array:
        :rtype: None
        """
        return self.int_param.GetEnumerateValues(o_safe_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_enumerate_values'
        # # vba_code = """
        # # Public Function get_enumerate_values(int_param)
        # #     Dim oSafeArray (2)
        # #     int_param.GetEnumerateValues oSafeArray
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
        return self.int_param.GetEnumerateValuesSize()

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
        return self.int_param.SetEnumerateValues(i_safe_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_enumerate_values'
        # # vba_code = """
        # # Public Function set_enumerate_values(int_param)
        # #     Dim iSafeArray (2)
        # #     int_param.SetEnumerateValues iSafeArray
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
        return self.int_param.SuppressEnumerateValues()

    def __repr__(self):
        return f'IntParam(name="{ self.name }")'
