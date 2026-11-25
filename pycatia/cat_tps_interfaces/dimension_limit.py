#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class DimensionLimit(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DimensionLimit
                | 
                | Represents the limit object of tolerance dimensions.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def dimension_limit_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DimensionLimitType() As CATBSTR
                | 
                |     Returns or sets the dimension limit type.
                |     Legal values: Valid dimension limit type values are:
                | 
                |         CATTPSDLNotDefined
                |         CATTPSDLNumerical
                |         CATTPSDLTabulated
                |         CATTPSDLSingleLimit

        :rtype: str
        """

        return self.com_object.DimensionLimitType

    @dimension_limit_type.setter
    def dimension_limit_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.DimensionLimitType = value

    @property
    def modifier(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Modifier() As CATBSTR
                | 
                |     Returns or sets the dimension single limit modifier.

        :rtype: str
        """

        return self.com_object.Modifier

    @modifier.setter
    def modifier(self, value: str):
        """
        :param str value:
        """

        self.com_object.Modifier = value

    @property
    def nominal_value(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Nominalvalue() As double (Read Only)
                | 
                |     Returns the dimension limit nominal value.
                |     This value is expressed in millimeters.

        :rtype: float
        """

        return self.com_object.Nominalvalue

    @property
    def symetric_value(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SymetricValue() As boolean
                | 
                |     Returns or sets whether the dimension limit is symmetric.
                |     TRUE if it is symmetric.

        :rtype: bool
        """

        return self.com_object.SymetricValue

    @symetric_value.setter
    def symetric_value(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SymetricValue = value

    @property
    def tabulated_limit(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TabulatedLimit() As CATBSTR
                | 
                |     Returns or sets the dimension tabulated limit.
                |     This tabulated limit is expressed as a string.

        :rtype: str
        """

        return self.com_object.TabulatedLimit

    @tabulated_limit.setter
    def tabulated_limit(self, value: str):
        """
        :param str value:
        """

        self.com_object.TabulatedLimit = value

    def limits(self, o_bottom: float, o_up: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub Limits(double oBottom,
                | double oUp)
                | 
                |     Retrieves dimension limit values.
                |     These values are expressed in millimeters.
                | 
                |     Parameters:
                | 
                |         oBottom
                |             The dimension limit bottom value 
                |         oUp
                |             The dimension limit up value

        :param float o_bottom:
        :param float o_up:
        :rtype: None
        """
        return self.com_object.Limits(o_bottom, o_up)

    def put_limits(self, i_bottom: float, i_up: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Sub PutLimits(double iBottom,
                | double iUp)
                | 
                |     Sets dimension limit values.
                |     These values are expressed in millimeters.
                | 
                |     Parameters:
                | 
                |         iBottom
                |             The dimension limit bottom value 
                |         iUp
                |             The dimension limit up value

        :param float i_bottom:
        :param float i_up:
        :rtype: None
        """
        return self.com_object.PutLimits(i_bottom, i_up)

    def __repr__(self):
        return f'DimensionLimit(name="{self.name}")'
