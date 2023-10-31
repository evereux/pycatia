#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class UnitsSheetSettingAtt(SettingController):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         UnitsSheetSettingAtt
                | 
                | The interface to access a CATIAUnitsSheetSettingAtt.
                | This interface may be used to read or modify in the CATIA/Tools/Option the
                | settings values of Units sheet.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.units_sheet_setting_att = com_object

    @property
    def display_trailing_zeros(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DisplayTrailingZeros() As short
                | 
                |     Returns or sets the DisplayTrailingZeros parameter.
                |     Role:Return or Set the DisplayTrailingZeros parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oDisplayTrailingZeros
                |             Legal values:
                |             0 : to not display trailing zeros
                |             1 : to display trailing zeros.

        :rtype: int
        """

        return self.units_sheet_setting_att.DisplayTrailingZeros

    @display_trailing_zeros.setter
    def display_trailing_zeros(self, value: int):
        """
        :param int value:
        """

        self.units_sheet_setting_att.DisplayTrailingZeros = value

    @property
    def exp_notation_values_greater(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ExpNotationValuesGreater() As double
                | 
                |     Returns or sets the ExpNotationValuesGreater parameter.
                |     Role:Return or Set the ExpNotationValuesGreater parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oExpNotationValuesGreater
                |             The minimum value for exponential notation values.

        :rtype: float
        """

        return self.units_sheet_setting_att.ExpNotationValuesGreater

    @exp_notation_values_greater.setter
    def exp_notation_values_greater(self, value: float):
        """
        :param float value:
        """

        self.units_sheet_setting_att.ExpNotationValuesGreater = value

    @property
    def exp_notation_values_lower(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ExpNotationValuesLower() As double
                | 
                |     Returns or sets the ExpNotationValuesLower parameter.
                |     Role:Return or Set the ExpNotationValuesGreater parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         oExpNotationValuesLower
                |             The maximum value for exponential notation values.

        :rtype: float
        """

        return self.units_sheet_setting_att.ExpNotationValuesLower

    @exp_notation_values_lower.setter
    def exp_notation_values_lower(self, value: float):
        """
        :param float value:
        """

        self.units_sheet_setting_att.ExpNotationValuesLower = value

    @property
    def list_of_magnitudes(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ListOfMagnitudes() As CATSafeArrayVariant (Read
                | Only)
                | 
                |     Returns or sets the ListOfMagnitudes parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: tuple
        """

        return self.units_sheet_setting_att.ListOfMagnitudes

    @property
    def list_of_magnitudes_size(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ListOfMagnitudesSize() As double (Read Only)
                | 
                |     Returns or sets the ListOfMagnitudesSize parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.units_sheet_setting_att.ListOfMagnitudesSize

    @property
    def same_display(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SameDisplay() As short
                | 
                |     Returns or sets the SameDisplay parameter.
                |     Role:Return or Set the SameDisplay parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oSameDisplay
                |             Legal values:
                |             0 : to not display same display
                |             1 : to display same display.

        :rtype: int
        """

        return self.units_sheet_setting_att.SameDisplay

    @same_display.setter
    def same_display(self, value: int):
        """
        :param int value:
        """

        self.units_sheet_setting_att.SameDisplay = value

    def commit_for_units(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub CommitForUnits()
                | 
                |     Implements a function from an interface.
                | 
                |     See also:
                |         UnitsSheetSettingAtt.CommitForUnits

        :rtype: None
        """
        return self.units_sheet_setting_att.CommitForUnits()

    def get_decimal_read_only(self, i_magnitude_name: str, o_decimal_place_read_only: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetDecimalReadOnly(CATBSTR iMagnitudeName,
                | double oDecimalPlaceReadOnly)
                | 
                |     Returns the number of decimals for ReadOnly number.

        :param str i_magnitude_name:
        :param float o_decimal_place_read_only:
        :rtype: None
        """
        return self.units_sheet_setting_att.GetDecimalReadOnly(i_magnitude_name, o_decimal_place_read_only)

    def get_decimal_read_write(self, i_magnitude_name: str, o_decimal_place_read_write: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetDecimalReadWrite(CATBSTR iMagnitudeName,
                | double oDecimalPlaceReadWrite)
                | 
                |     Returns the number of decimals for ReadWrite number.

        :param str i_magnitude_name:
        :param float o_decimal_place_read_write:
        :rtype: None
        """
        return self.units_sheet_setting_att.GetDecimalReadWrite(i_magnitude_name, o_decimal_place_read_write)

    def get_dimensions_display_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetDimensionsDisplayInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the DimensionsDisplay setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.units_sheet_setting_att.GetDimensionsDisplayInfo(io_admin_level, io_locked)

    def get_display_trailing_zeros_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetDisplayTrailingZerosInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DisplayTrailingZeros
                |     parameter.
                |     Role:Retrieves the state of the DisplayTrailingZeros parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.units_sheet_setting_att.GetDisplayTrailingZerosInfo(io_admin_level, io_locked)

    def get_exp_notation_values_greater_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetExpNotationValuesGreaterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ExpNotationValuesGreater
                |     parameter.
                |     Role:Retrieves the state of the ExpNotationValuesGreater parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.units_sheet_setting_att.GetExpNotationValuesGreaterInfo(io_admin_level, io_locked)

    def get_exp_notation_values_lower_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetExpNotationValuesLowerInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ExpNotationValuesLower
                |     parameter.
                |     Role:Retrieves the state of the ExpNotationValuesLower parameter in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.units_sheet_setting_att.GetExpNotationValuesLowerInfo(io_admin_level, io_locked)

    def get_list_of_magnitudes_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetListOfMagnitudesInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ListOfMagnitudes setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.units_sheet_setting_att.GetListOfMagnitudesInfo(io_admin_level, io_locked)

    def get_magnitude_values(self,
                             i_magnitude_name: str,
                             o_unit_name: str,
                             o_decimal_place_read_write: float,
                             o_decimal_place_read_only: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetMagnitudeValues(CATBSTR iMagnitudeName,
                | CATBSTR oUnitName,
                | double oDecimalPlaceReadWrite,
                | double oDecimalPlaceReadOnly)
                | 
                |     Returns the Magnitude parameters.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :param str i_magnitude_name:
        :param str o_unit_name:
        :param float o_decimal_place_read_write:
        :param float o_decimal_place_read_only:
        :rtype: None
        """
        return self.units_sheet_setting_att.GetMagnitudeValues(i_magnitude_name, o_unit_name,
                                                               o_decimal_place_read_write, o_decimal_place_read_only)

    def get_same_display_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSameDisplayInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SameDisplay
                |     parameter.
                |     Role:Retrieves the state of the SameDisplay parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.units_sheet_setting_att.GetSameDisplayInfo(io_admin_level, io_locked)

    def reset_to_admin_values_for_units(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ResetToAdminValuesForUnits()
                | 
                |     Implements a function from an interface.
                | 
                |     See also:
                |         UnitsSheetSettingAtt.ResetToAdminValuesForUnits

        :rtype: None
        """
        return self.units_sheet_setting_att.ResetToAdminValuesForUnits()

    def rollback_for_units(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RollbackForUnits()
                | 
                |     Implements a function from an interface.
                | 
                |     See also:
                |         UnitsSheetSettingAtt.RollbackForUnits

        :rtype: None
        """
        return self.units_sheet_setting_att.RollbackForUnits()

    def save_repository_for_units(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SaveRepositoryForUnits()
                | 
                |     Implements a function from an interface.
                | 
                |     See also:
                |         UnitsSheetSettingAtt.SaveRepositoryForUnits

        :rtype: None
        """
        return self.units_sheet_setting_att.SaveRepositoryForUnits()

    def set_dimensions_display_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetDimensionsDisplayLock(boolean iLocked)
                | 
                |     Locks or unlocks the DimensionsDisplay setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.units_sheet_setting_att.SetDimensionsDisplayLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dimensions_display_lock'
        # # vba_code = """
        # # Public Function set_dimensions_display_lock(units_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     units_sheet_setting_att.SetDimensionsDisplayLock iLocked
        # #     set_dimensions_display_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_trailing_zeros_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetDisplayTrailingZerosLock(boolean iLocked)
                | 
                |     Deprecated:
                |         V5R15. Use SetDimensionsDisplayLock. Locks or unlocks the
                |         DisplayTrailingZeros parameter.
                |         Role:Locks or unlocks the DisplayTrailingZeros parameter if it is
                |         possible in the current administrative context. In user mode this method will
                |         always return E_FAIL. 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.units_sheet_setting_att.SetDisplayTrailingZerosLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_trailing_zeros_lock'
        # # vba_code = """
        # # Public Function set_display_trailing_zeros_lock(units_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     units_sheet_setting_att.SetDisplayTrailingZerosLock iLocked
        # #     set_display_trailing_zeros_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_exp_notation_values_greater_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetExpNotationValuesGreaterLock(boolean iLocked)
                | 
                |     Deprecated:
                |         V5R15. Use SetSameDisplayLock. Locks or unlocks the
                |         ExpNotationValuesGreater parameter.
                |         Role:Locks or unlocks the ExpNotationValuesGreater parameter if it is
                |         possible in the current administrative context. In user mode this method will
                |         always return E_FAIL. 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.units_sheet_setting_att.SetExpNotationValuesGreaterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_exp_notation_values_greater_lock'
        # # vba_code = """
        # # Public Function set_exp_notation_values_greater_lock(units_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     units_sheet_setting_att.SetExpNotationValuesGreaterLock iLocked
        # #     set_exp_notation_values_greater_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_exp_notation_values_lower_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetExpNotationValuesLowerLock(boolean iLocked)
                | 
                |     Deprecated:
                |         V5R15. Use SetDimensionsDisplayLock. Locks or unlocks the
                |         ExpNotationValuesLower parameter.
                |         Role:Locks or unlocks the ExpNotationValuesLower parameter if it is
                |         possible in the current administrative context. In user mode this method will
                |         always return E_FAIL. 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.units_sheet_setting_att.SetExpNotationValuesLowerLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_exp_notation_values_lower_lock'
        # # vba_code = """
        # # Public Function set_exp_notation_values_lower_lock(units_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     units_sheet_setting_att.SetExpNotationValuesLowerLock iLocked
        # #     set_exp_notation_values_lower_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_list_of_magnitudes_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetListOfMagnitudesLock(boolean iLocked)
                | 
                |     Locks or unlocks the ListOfMagnitudes setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.units_sheet_setting_att.SetListOfMagnitudesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_list_of_magnitudes_lock'
        # # vba_code = """
        # # Public Function set_list_of_magnitudes_lock(units_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     units_sheet_setting_att.SetListOfMagnitudesLock iLocked
        # #     set_list_of_magnitudes_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_magnitude_values(self,
                             i_magnitude_name: str,
                             i_unit_name: str,
                             i_decimal_place_read_write: float,
                             i_decimal_place_read_only: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetMagnitudeValues(CATBSTR iMagnitudeName,
                | CATBSTR iUnitName,
                | double iDecimalPlaceReadWrite,
                | double iDecimalPlaceReadOnly)
                | 
                |     Sets the Magnitude parameters.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :param str i_magnitude_name:
        :param str i_unit_name:
        :param float i_decimal_place_read_write:
        :param float i_decimal_place_read_only:
        :rtype: None
        """
        return self.units_sheet_setting_att.SetMagnitudeValues(i_magnitude_name, i_unit_name,
                                                               i_decimal_place_read_write, i_decimal_place_read_only)

    def set_same_display_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSameDisplayLock(boolean iLocked)
                | 
                |     Deprecated:
                |         V5R15. Use SetDimensionsDisplayLock. Locks or unlocks the SameDisplay
                |         parameter.
                |         Role:Locks or unlocks the SameDisplay parameter if it is possible in
                |         the current administrative context. In user mode this method will always return
                |         E_FAIL. 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.units_sheet_setting_att.SetSameDisplayLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_same_display_lock'
        # # vba_code = """
        # # Public Function set_same_display_lock(units_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     units_sheet_setting_att.SetSameDisplayLock iLocked
        # #     set_same_display_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'UnitsSheetSettingAtt(name="{self.name}")'
