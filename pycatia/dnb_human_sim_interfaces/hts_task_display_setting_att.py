#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class HtsTaskDisplaySettingAtt(SettingController):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         HtsTaskDisplaySettingAtt

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hts_task_display_setting_att = com_object

    @property
    def auto_walk_act_colour(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoWalkActColor() As long
                | 
                |     Returns or sets the AutoWalkActColor parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_task_display_setting_att.AutoWalkActColor

    @auto_walk_act_colour.setter
    def auto_walk_act_colour(self, value: int):
        """
        :param int value:
        """

        self.hts_task_display_setting_att.AutoWalkActColor = value

    @property
    def auto_walk_act_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoWalkActLineType() As long
                | 
                |     Returns or sets the AutoWalkActLineType parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_task_display_setting_att.AutoWalkActLineType

    @auto_walk_act_line_type.setter
    def auto_walk_act_line_type(self, value: int):
        """
        :param int value:
        """

        self.hts_task_display_setting_att.AutoWalkActLineType = value

    @property
    def auto_walk_act_line_weight(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoWalkActLineWeight() As long
                | 
                |     Returns or sets the AutoWalkActLineWeight parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_task_display_setting_att.AutoWalkActLineWeight

    @auto_walk_act_line_weight.setter
    def auto_walk_act_line_weight(self, value: int):
        """
        :param int value:
        """

        self.hts_task_display_setting_att.AutoWalkActLineWeight = value

    @property
    def mtp_act_colour(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MTPActColor() As long
                | 
                |     Returns or sets the MTPActColor parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_task_display_setting_att.MTPActColor

    @mtp_act_colour.setter
    def mtp_act_colour(self, value: int):
        """
        :param int value:
        """

        self.hts_task_display_setting_att.MTPActColor = value

    @property
    def mtp_act_symbol(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MTPActSymbol() As long
                | 
                |     Returns or sets the MTPActSymbol parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_task_display_setting_att.MTPActSymbol

    @mtp_act_symbol.setter
    def mtp_act_symbol(self, value: int):
        """
        :param int value:
        """

        self.hts_task_display_setting_att.MTPActSymbol = value

    @property
    def walk_act_colour(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WalkActColor() As long
                | 
                |     Returns or sets the WalkActColor parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_task_display_setting_att.WalkActColor

    @walk_act_colour.setter
    def walk_act_colour(self, value: int):
        """
        :param int value:
        """

        self.hts_task_display_setting_att.WalkActColor = value

    @property
    def walk_act_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WalkActLineType() As long
                | 
                |     Returns or sets the WalkActLineType parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_task_display_setting_att.WalkActLineType

    @walk_act_line_type.setter
    def walk_act_line_type(self, value: int):
        """
        :param int value:
        """

        self.hts_task_display_setting_att.WalkActLineType = value

    @property
    def walk_act_line_weight(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WalkActLineWeight() As long
                | 
                |     Returns or sets the WalkActLineWeight parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_task_display_setting_att.WalkActLineWeight

    @walk_act_line_weight.setter
    def walk_act_line_weight(self, value: int):
        """
        :param int value:
        """

        self.hts_task_display_setting_att.WalkActLineWeight = value

    def get_auto_walk_act_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAutoWalkActColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AutoWalkActColor
                |     parameter.
                |     Role:Retrieves the state of the AutoWalkActColor parameter in the current
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
        return self.hts_task_display_setting_att.GetAutoWalkActColorInfo(io_admin_level, io_locked)

    def get_auto_walk_act_line_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAutoWalkActLineTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AutoWalkActLineType
                |     parameter.
                |     Role:Retrieves the state of the AutoWalkActLineType parameter in the
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
        return self.hts_task_display_setting_att.GetAutoWalkActLineTypeInfo(io_admin_level, io_locked)

    def get_auto_walk_act_line_weight_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAutoWalkActLineWeightInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AutoWalkActLineWeight
                |     parameter.
                |     Role:Retrieves the state of the AutoWalkActLineWeight parameter in the
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
        return self.hts_task_display_setting_att.GetAutoWalkActLineWeightInfo(io_admin_level, io_locked)

    def get_mtp_act_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMTPActColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MTPActColor
                |     parameter.
                |     Role:Retrieves the state of the MTPActColor parameter in the current
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
        return self.hts_task_display_setting_att.GetMTPActColorInfo(io_admin_level, io_locked)

    def get_mtp_act_symbol_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMTPActSymbolInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MTPActSymbol
                |     parameter.
                |     Role:Retrieves the state of the MTPActSymbol parameter in the current
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
        return self.hts_task_display_setting_att.GetMTPActSymbolInfo(io_admin_level, io_locked)

    def get_walk_act_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetWalkActColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the WalkActColor
                |     parameter.
                |     Role:Retrieves the state of the WalkActColor parameter in the current
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
        return self.hts_task_display_setting_att.GetWalkActColorInfo(io_admin_level, io_locked)

    def get_walk_act_line_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetWalkActLineTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the WalkActLineType
                |     parameter.
                |     Role:Retrieves the state of the WalkActLineType parameter in the current
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
        return self.hts_task_display_setting_att.GetWalkActLineTypeInfo(io_admin_level, io_locked)

    def get_walk_act_line_weight_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetWalkActLineWeightInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the WalkActLineWeight
                |     parameter.
                |     Role:Retrieves the state of the WalkActLineWeight parameter in the current
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
        return self.hts_task_display_setting_att.GetWalkActLineWeightInfo(io_admin_level, io_locked)

    def set_auto_walk_act_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAutoWalkActColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the AutoWalkActColor parameter.
                |     Role:Locks or unlocks the AutoWalkActColor parameter if it is possible in
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
        return self.hts_task_display_setting_att.SetAutoWalkActColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_walk_act_color_lock'
        # # vba_code = """
        # # Public Function set_auto_walk_act_color_lock(hts_task_display_setting_att)
        # #     Dim iLocked (2)
        # #     hts_task_display_setting_att.SetAutoWalkActColorLock iLocked
        # #     set_auto_walk_act_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_auto_walk_act_line_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAutoWalkActLineTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the AutoWalkActLineType parameter.
                |     Role:Locks or unlocks the AutoWalkActLineType parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
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
        return self.hts_task_display_setting_att.SetAutoWalkActLineTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_walk_act_line_type_lock'
        # # vba_code = """
        # # Public Function set_auto_walk_act_line_type_lock(hts_task_display_setting_att)
        # #     Dim iLocked (2)
        # #     hts_task_display_setting_att.SetAutoWalkActLineTypeLock iLocked
        # #     set_auto_walk_act_line_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_auto_walk_act_line_weight_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAutoWalkActLineWeightLock(boolean iLocked)
                | 
                |     Locks or unlocks the AutoWalkActLineWeight parameter.
                |     Role:Locks or unlocks the AutoWalkActLineWeight parameter if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
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
        return self.hts_task_display_setting_att.SetAutoWalkActLineWeightLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_walk_act_line_weight_lock'
        # # vba_code = """
        # # Public Function set_auto_walk_act_line_weight_lock(hts_task_display_setting_att)
        # #     Dim iLocked (2)
        # #     hts_task_display_setting_att.SetAutoWalkActLineWeightLock iLocked
        # #     set_auto_walk_act_line_weight_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_mtp_act_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMTPActColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the MTPActColor parameter.
                |     Role:Locks or unlocks the MTPActColor parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
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
        return self.hts_task_display_setting_att.SetMTPActColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_mtp_act_color_lock'
        # # vba_code = """
        # # Public Function set_mtp_act_color_lock(hts_task_display_setting_att)
        # #     Dim iLocked (2)
        # #     hts_task_display_setting_att.SetMTPActColorLock iLocked
        # #     set_mtp_act_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_mtp_act_symbol_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMTPActSymbolLock(boolean iLocked)
                | 
                |     Locks or unlocks the MTPActSymbol parameter.
                |     Role:Locks or unlocks the MTPActSymbol parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
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
        return self.hts_task_display_setting_att.SetMTPActSymbolLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_mtp_act_symbol_lock'
        # # vba_code = """
        # # Public Function set_mtp_act_symbol_lock(hts_task_display_setting_att)
        # #     Dim iLocked (2)
        # #     hts_task_display_setting_att.SetMTPActSymbolLock iLocked
        # #     set_mtp_act_symbol_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_walk_act_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetWalkActColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the WalkActColor parameter.
                |     Role:Locks or unlocks the WalkActColor parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
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
        return self.hts_task_display_setting_att.SetWalkActColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_walk_act_color_lock'
        # # vba_code = """
        # # Public Function set_walk_act_color_lock(hts_task_display_setting_att)
        # #     Dim iLocked (2)
        # #     hts_task_display_setting_att.SetWalkActColorLock iLocked
        # #     set_walk_act_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_walk_act_line_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetWalkActLineTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the WalkActLineType parameter.
                |     Role:Locks or unlocks the WalkActLineType parameter if it is possible in
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
        return self.hts_task_display_setting_att.SetWalkActLineTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_walk_act_line_type_lock'
        # # vba_code = """
        # # Public Function set_walk_act_line_type_lock(hts_task_display_setting_att)
        # #     Dim iLocked (2)
        # #     hts_task_display_setting_att.SetWalkActLineTypeLock iLocked
        # #     set_walk_act_line_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_walk_act_line_weight_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetWalkActLineWeightLock(boolean iLocked)
                | 
                |     Locks or unlocks the WalkActLineWeight parameter.
                |     Role:Locks or unlocks the WalkActLineWeight parameter if it is possible in
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
        return self.hts_task_display_setting_att.SetWalkActLineWeightLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_walk_act_line_weight_lock'
        # # vba_code = """
        # # Public Function set_walk_act_line_weight_lock(hts_task_display_setting_att)
        # #     Dim iLocked (2)
        # #     hts_task_display_setting_att.SetWalkActLineWeightLock iLocked
        # #     set_walk_act_line_weight_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HtsTaskDisplaySettingAtt(name="{self.name}")'
