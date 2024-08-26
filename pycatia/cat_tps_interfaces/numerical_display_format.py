#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.system_interfaces.any_object import AnyObject


class NumericalDisplayFormat(AnyObject):
    """

    Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     NumericalDisplayFormat
                |
                | Interface to manage numerical format properties of GST, DRF and Datum
                | Target.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.numerical_display_format = com_object

    @property
    def available_display_factor(self) -> int:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property AvilableDisplayFactor() As long (Read Only)
                |     Retrieves or sets the maximun level of factor available to be
                |     displayed.
                |     It may vary according to the name of the format.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.numerical_display_format.AvilableDisplayFactor

    @property
    def display_factor(self) -> int:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property DisplayFactor() As long
                |     Retrieves or sets the level of factor to be displayed.
                |     The numerical values associated to the annotation will be displayed as per
                |     this Display Factor.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.numerical_display_format.DisplayFactor

    @display_factor.setter
    def display_factor(self, value: int):
        """
        :param int value:
        """

        self.numerical_display_format.DisplayFactor = value

    @property
    def display_leading_zero(self) -> int:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property DisplayLeadingZero() As long
                |     Retrieves or sets the annotation DisplayLeadingZero.
                |     The numerical values associated to the annotation will be displayed as per
                |     this DisplayLeadingZero.
                |     The integer value of onValue/inValue corresponding to:
                |     0 : no display of LeadingZero.
                |     1 : display the LeadingZero.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.numerical_display_format.DisplayLeadingZero

    @display_leading_zero.setter
    def display_leading_zero(self, value: int):
        """
        :param int value:
        """

        self.numerical_display_format.DisplayLeadingZero = value

    @property
    def display_trailing_zero(self) -> int:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property DisplayTrailingZero() As long
                |     Retrieves or sets the annotation DisplayTrailingZero.
                |     The numerical values associated to the annotation will be displayed as per
                |     this DisplayTrailingZero.
                |     The integer value of onValue/inValue corresponding to:
                |     0 : no display of TrailingZero.
                |     1 : display the TrailingZero.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.numerical_display_format.DisplayTrailingZero

    @display_trailing_zero.setter
    def display_trailing_zero(self, value: int):
        """
        :param int value:
        """

        self.numerical_display_format.DisplayTrailingZero = value

    @property
    def format_name(self) -> str:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property FormatName() As CATBSTR
                |     Retrieves or sets the format name.
                |     The numerical values associated to the annotation will be displayed as per
                |     this format.

        :rtype: str
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.numerical_display_format.FormatName

    @format_name.setter
    def format_name(self, value: str):
        """
        :param str value:
        """

        self.numerical_display_format.FormatName = value

    @property
    def precision(self) -> int:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property Precision() As long
                |     Retrieves or sets the precision of annotation.
                |     The numerical values associated to the annotation will be displayed as per
                |     this precision.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.numerical_display_format.Precision

    @precision.setter
    def precision(self, value: int):
        """
        :param int value:
        """

        self.numerical_display_format.Precision = value

    @property
    def separator(self) -> int:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property Separator() As long
                |     Retrieves or sets the annotation separator.
                |     The numerical values associated to the annotation will be displayed with
                |     this seperator.
                |     The integer value of onValue/inValue corresponding to:
                |     0 ""
                |     1 "/"
                |     2 ":"
                |     3 "("
                |     4 ")"
                |     5 "\\"
                |     6 ","
                |     7 "<"
                |     8 ">"
                |     9 "X"
                |     10 "*"
                |     11 "."
                |     12 ";"
                |     13 "+"
                |     14 "["
                |     15 "]"
                |     16 "-"
                |     17 "_"
                |     18 " "

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.numerical_display_format.Separator

    @separator.setter
    def separator(self, value: int):
        """
        :param int value:
        """

        self.numerical_display_format.Separator = value

    def __repr__(self):
        return f'NumericalDisplayFormat(name="{self.name}")'
