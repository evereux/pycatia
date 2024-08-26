#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.knowledge_interfaces.parameter import Parameter
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingParameter(AnyObject):
    """

    Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingParameter
                |
                | This interface is used to handle with Enumeration Parameters for
                | Manufacturing

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_parameter = com_object

    def get_bool_value(self, i_name: str, o_value: bool) -> None:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub GetBoolValue(CATBSTR iName,boolean oValue)
                |     Get boolean value of parameter
                |
                |     Parameters:
                |
                |         iName
                |             The name of the parameter
                |         oValue
                |             The boolean value

        :param str i_name:
        :param bool o_value:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.manufacturing_parameter.GetBoolValue(i_name, o_value)

    def get_double_value(self, i_name: str, o_value: float, i_unit: int) -> None:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub GetDoubleValue(CATBSTR iName,double oValue,long iUnit)
                |     Get double value of parameter
                |
                |     Parameters:
                |
                |         iName
                |             The name of the parameter
                |         oValue
                |             The double value
                |         iUnit
                |             The unit value (default: 0)

        :param str i_name:
        :param float o_value:
        :param int i_unit:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.manufacturing_parameter.GetDoubleValue(i_name, o_value, i_unit)

    def get_long_value(self, i_name: str, o_value: int) -> None:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub GetLongValue(CATBSTR iName,long oValue)
                |     Get integer value of parameter
                |
                |     Parameters:
                |
                |         iName
                |             The name of the parameter
                |         oValue
                |             The double value

        :param str i_name:
        :param int o_value:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.manufacturing_parameter.GetLongValue(i_name, o_value)

    def get_string_value(self, i_name: str, o_value: str) -> None:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub GetStringValue(CATBSTR iName,CATBSTR oValue)
                |     Get string value of parameter
                |
                |     Parameters:
                |
                |         iName
                |             The name of the parameter
                |         oValue
                |             The string value

        :param str i_name:
        :param str o_value:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.manufacturing_parameter.GetStringValue(i_name, o_value)

    def get_value(self, i_name: str, o_value: Parameter) -> None:
        """

        Introduced in V5-6R2021.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub GetValue(CATBSTR iName,Parameter oValue)
                |     Get CATICkeParm value of parameter
                |
                |     Parameters:
                |
                |         iName
                |             The name of the parameter
                |         oValue
                |             The CATICkeParm value

        :param str i_name:
        :param Parameter o_value:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            31,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.manufacturing_parameter.GetValue(i_name, o_value.com_object)

    def __repr__(self):
        return f'ManufacturingParameter(name="{self.name}")'
