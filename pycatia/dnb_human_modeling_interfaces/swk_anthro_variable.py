#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_modeling_interfaces.swk_manikin_part import SWKManikinPart


class SWKAnthroVariable(SWKManikinPart):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBHumanModelingInterfaces.SWKManikinPart
                |                         SWKAnthroVariable
                | 
                | This interface is used to access an anthropometric variable.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.swk_anthro_variable = com_object

    @property
    def full_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FullName() As CATBSTR (Read Only)
                | 
                |     Returns the full name of the variable.
                |     This property is different from the property
                |     Name of AnyObject,
                |     which gives the short name or acronym name
                |     of the variable.
                | 
                |     For instance, if the variable in question is
                |     the head length, then property Name
                |     yields "<HEADLGTH>", whereas
                |     property FullName yields the character
                |     string "Head length".

        :rtype: str
        """

        return self.swk_anthro_variable.FullName

    @property
    def manual(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Manual() As boolean
                | 
                |     Returns or sets the management of the variable.
                |     A anthropometric variable being manual means that
                |     the variable's value is managed by the user and its current value will
                |     remain until the user changes it again.
                | 
                |     If the variable is not manual, then it is automatic, which means that the
                |     variable is managed by the system and that its value may be overriden, every
                |     time the anthropometry is updated.

        :rtype: bool
        """

        return self.swk_anthro_variable.Manual

    @manual.setter
    def manual(self, value: bool):
        """
        :param bool value:
        """

        self.swk_anthro_variable.Manual = value

    @property
    def max_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MaxValue() As double (Read Only)
                | 
                |     Returns the highest value that the variable can take. This value
                |     corresponds to percentile 100.
                | 
                |     If this variable is a mass, the value returned is in
                |     kilograms; if not, the value returned is in centimeters.

        :rtype: float
        """

        return self.swk_anthro_variable.MaxValue

    @property
    def mean(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Mean() As double (Read Only)
                | 
                |     Returns the mean value os the variable. This value corresponds to
                |     percentile 50.
                | 
                |     If this variable is a mass, the value returned is in
                |     kilograms; if not, the value returned is in centimeters.

        :rtype: float
        """

        return self.swk_anthro_variable.Mean

    @property
    def min_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MinValue() As double (Read Only)
                | 
                |     Returns the lowest value that the variable can take. This value corresponds
                |     to percentile 0.
                | 
                |     If this variable is a mass, the value returned is in
                |     kilograms; if not, the value returned is in centimeters.

        :rtype: float
        """

        return self.swk_anthro_variable.MinValue

    @property
    def reference_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReferenceNumber() As long (Read Only)
                | 
                |     Returns the reference number of the variable.
                |     This reference number is unique to the variable.

        :rtype: int
        """

        return self.swk_anthro_variable.ReferenceNumber

    @property
    def std_dev(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StdDev() As double (Read Only)
                | 
                |     Returns the standard deviation of the variable.
                | 
                |     If this variable is a mass, the value returned is in
                |     kilograms; if not, the value returned is in centimeters.

        :rtype: float
        """

        return self.swk_anthro_variable.StdDev

    @property
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Value() As double
                | 
                |     Returns or sets the value of the variable.

        :rtype: float
        """

        return self.swk_anthro_variable.Value

    @value.setter
    def value(self, value: float):
        """
        :param float value:
        """

        self.swk_anthro_variable.Value = value

    @property
    def value_as_percentile(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ValueAsPercentile() As double
                | 
                |     Returns or sets the value of the variable.
                |     When using that property, the number returned or set
                |     must be a percentile, that is, must be between 0.0 and 100.0
                |     inclusive.
                | 
                |     If this variable is a mass, the value returned or set is in
                |     kilograms, if not, the value returned or set is in centimeters.

        :rtype: float
        """

        return self.swk_anthro_variable.ValueAsPercentile

    @value_as_percentile.setter
    def value_as_percentile(self, value: float):
        """
        :param float value:
        """

        self.swk_anthro_variable.ValueAsPercentile = value

    @property
    def value_as_string(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ValueAsString() As CATBSTR
                | 
                |     Returns or sets the value of the variable, as a string.

        :rtype: str
        """

        return self.swk_anthro_variable.ValueAsString

    @value_as_string.setter
    def value_as_string(self, value: str):
        """
        :param str value:
        """

        self.swk_anthro_variable.ValueAsString = value

    def get_correlation_with(self, pi_ref_number_of_other: int) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCorrelationWith(long piRefNumberOfOther) As double
                | 
                |     Returns the correlation between this variable and another.
                | 
                |     Parameters:
                | 
                |         piRefNumberOfOther
                |             The reference number of the other variable (ex.: 3 for us3, 100 for
                |             us100, etc).

        :param int pi_ref_number_of_other:
        :rtype: float
        """
        return self.swk_anthro_variable.GetCorrelationWith(pi_ref_number_of_other)

    def __repr__(self):
        return f'SWKAnthroVariable(name="{self.name}")'
