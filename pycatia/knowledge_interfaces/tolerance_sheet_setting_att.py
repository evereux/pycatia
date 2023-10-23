#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class ToleranceSheetSettingAtt(SettingController):
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
                |                         ToleranceSheetSettingAtt
                | 
                | The interface to access a CATIAToleranceSheetSettingAtt.
                | This interface may be used to read or modify in the CATIA/Tools/Option the
                | settings values of Tolerance sheet.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tolerance_sheet_setting_att = com_object

    @property
    def angle_max_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AngleMaxTolerance() As double
                | 
                |     Returns or sets the AngleMaxTolerance parameter.
                |     Role:Return or Set the AngleMaxTolerance parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oAngleMaxTolerance
                |             The angle maximum tolerance value.

        :rtype: float
        """

        return self.tolerance_sheet_setting_att.AngleMaxTolerance

    @angle_max_tolerance.setter
    def angle_max_tolerance(self, value: float):
        """
        :param float value:
        """

        self.tolerance_sheet_setting_att.AngleMaxTolerance = value

    @property
    def angle_min_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property AngleMinTolerance() As double
                | 
                |     Returns or sets the AngleMinTolerance parameter.
                |     Role:Return or Set the AngleMinTolerance parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oAngleMinTolerance
                |             The angle minimum tolerance value.

        :rtype: float
        """

        return self.tolerance_sheet_setting_att.AngleMinTolerance

    @angle_min_tolerance.setter
    def angle_min_tolerance(self, value: float):
        """
        :param float value:
        """

        self.tolerance_sheet_setting_att.AngleMinTolerance = value

    @property
    def default_tolerance(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DefaultTolerance() As short
                | 
                |     Returns or sets the DefaultTolerance parameter.
                |     Role:Return or Set the DefaultTolerance parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oDefaultTolerance
                |             Legal values:
                |             0 : to not accept a default tolerance
                |             1 : to accept a default tolerance.

        :rtype: int
        """

        return self.tolerance_sheet_setting_att.DefaultTolerance

    @default_tolerance.setter
    def default_tolerance(self, value: int):
        """
        :param int value:
        """

        self.tolerance_sheet_setting_att.DefaultTolerance = value

    @property
    def length_max_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property LengthMaxTolerance() As double
                | 
                |     Returns or sets the LengthMaxTolerance parameter.
                |     Role:Return or Set the LengthMaxTolerance parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oLengthMaxTolerance
                |             The length maximum tolerance value.

        :rtype: float
        """

        return self.tolerance_sheet_setting_att.LengthMaxTolerance

    @length_max_tolerance.setter
    def length_max_tolerance(self, value: float):
        """
        :param float value:
        """

        self.tolerance_sheet_setting_att.LengthMaxTolerance = value

    @property
    def length_min_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property LengthMinTolerance() As double
                | 
                |     Returns or sets the LengthMinTolerance parameter.
                |     Role:Return or Set the LengthMinTolerance parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         oLengthMinTolerance
                |             The length minimum tolerance value.

        :rtype: float
        """

        return self.tolerance_sheet_setting_att.LengthMinTolerance

    @length_min_tolerance.setter
    def length_min_tolerance(self, value: float):
        """
        :param float value:
        """

        self.tolerance_sheet_setting_att.LengthMinTolerance = value

    def get_angle_max_tolerance_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetAngleMaxToleranceInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AngleMaxTolerance
                |     parameter.
                |     Role:Retrieves the state of the AngleMaxTolerance parameter in the current
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
        return self.tolerance_sheet_setting_att.GetAngleMaxToleranceInfo(io_admin_level, io_locked)

    def get_angle_min_tolerance_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetAngleMinToleranceInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AngleMinTolerance
                |     parameter.
                |     Role:Retrieves the state of the AngleMinTolerance parameter in the current
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
        return self.tolerance_sheet_setting_att.GetAngleMinToleranceInfo(io_admin_level, io_locked)

    def get_default_tolerance_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetDefaultToleranceInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DefaultTolerance
                |     parameter.
                |     Role:Retrieves the state of the DefaultTolerance parameter in the current
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
        return self.tolerance_sheet_setting_att.GetDefaultToleranceInfo(io_admin_level, io_locked)

    def get_length_max_tolerance_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetLengthMaxToleranceInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LengthMaxTolerance
                |     parameter.
                |     Role:Retrieves the state of the LengthMaxTolerance parameter in the current
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
        return self.tolerance_sheet_setting_att.GetLengthMaxToleranceInfo(io_admin_level, io_locked)

    def get_length_min_tolerance_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetLengthMinToleranceInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LengthMinTolerance
                |     parameter.
                |     Role:Retrieves the state of the LengthMinTolerance parameter in the current
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
        return self.tolerance_sheet_setting_att.GetLengthMinToleranceInfo(io_admin_level, io_locked)

    def set_angle_max_tolerance_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetAngleMaxToleranceLock(boolean iLocked)
                | 
                |     Locks or unlocks the AngleMaxTolerance parameter.
                |     Role:Locks or unlocks the AngleMaxTolerance parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
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
        return self.tolerance_sheet_setting_att.SetAngleMaxToleranceLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_angle_max_tolerance_lock'
        # # vba_code = """
        # # Public Function set_angle_max_tolerance_lock(tolerance_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     tolerance_sheet_setting_att.SetAngleMaxToleranceLock iLocked
        # #     set_angle_max_tolerance_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_angle_min_tolerance_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetAngleMinToleranceLock(boolean iLocked)
                | 
                |     Locks or unlocks the AngleMinTolerance parameter.
                |     Role:Locks or unlocks the AngleMinTolerance parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
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
        return self.tolerance_sheet_setting_att.SetAngleMinToleranceLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_angle_min_tolerance_lock'
        # # vba_code = """
        # # Public Function set_angle_min_tolerance_lock(tolerance_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     tolerance_sheet_setting_att.SetAngleMinToleranceLock iLocked
        # #     set_angle_min_tolerance_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_tolerance_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetDefaultToleranceLock(boolean iLocked)
                | 
                |     Locks or unlocks the DefaultTolerance parameter.
                |     Role:Locks or unlocks the DefaultTolerance parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
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
        return self.tolerance_sheet_setting_att.SetDefaultToleranceLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_tolerance_lock'
        # # vba_code = """
        # # Public Function set_default_tolerance_lock(tolerance_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     tolerance_sheet_setting_att.SetDefaultToleranceLock iLocked
        # #     set_default_tolerance_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_length_max_tolerance_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetLengthMaxToleranceLock(boolean iLocked)
                | 
                |     Locks or unlocks the LengthMaxTolerance parameter.
                |     Role:Locks or unlocks the LengthMaxTolerance parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
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
        return self.tolerance_sheet_setting_att.SetLengthMaxToleranceLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_length_max_tolerance_lock'
        # # vba_code = """
        # # Public Function set_length_max_tolerance_lock(tolerance_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     tolerance_sheet_setting_att.SetLengthMaxToleranceLock iLocked
        # #     set_length_max_tolerance_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_length_min_tolerance_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetLengthMinToleranceLock(boolean iLocked)
                | 
                |     Locks or unlocks the LengthMinTolerance parameter.
                |     Role:Locks or unlocks the LengthMinTolerance parameter if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
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
        return self.tolerance_sheet_setting_att.SetLengthMinToleranceLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_length_min_tolerance_lock'
        # # vba_code = """
        # # Public Function set_length_min_tolerance_lock(tolerance_sheet_setting_att)
        # #     Dim iLocked (2)
        # #     tolerance_sheet_setting_att.SetLengthMinToleranceLock iLocked
        # #     set_length_min_tolerance_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ToleranceSheetSettingAtt(name="{self.name}")'
