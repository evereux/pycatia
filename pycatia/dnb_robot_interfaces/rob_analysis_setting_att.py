#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class RobAnalysisSettingAtt(SettingController):
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
                |                         RobAnalysisSettingAtt
                | 
                | Interface to handle parameters of Infrastructure-DELMIA Infrastructure-Robot
                | Analysis Tools Options Tab page.
                | Role: This interface is implemented by a component which represents the
                | controller of Robot Analysis Tools Options parameter settings.
                | 
                |     Methods to set value of each parameter xxx
                |     Methods to get value of each parameter xxx
                |     Methods to get information on each parameter xxx
                |     Methods to lock/unlock value of each parameter xxx
                | 
                | Here is the list of parameters to use and their meaning:
                | 
                |     LinSpeedLimit: defines what behavior you can expect when the TCP linear
                |     speed limits are exeeded.
                |     RotSpeedLimit: defines what behavior you can expect when the TCP rotational
                |     speed limits are exeeded.
                |     LinAccelLimit: defines what behavior you can expect when the TCP linear
                |     acceleration limits are exeeded.
                |     RotAccelLimit: defines what behavior you can expect when the TCP rotational
                |     acceleration limits are exeeded.
                |     LinSpeedColor: defines the highlight color to be used when the TCP linear
                |     speed limits are exceeded.
                |     RotSpeedColor: defines the highlight color to be used when the TCP
                |     rotational speed limits are exceeded.
                |     LinAccelColor: defines the highlight color to be used when the TCP linear
                |     acceleration limits are exceeded.
                |     RotAccelColor: defines the highlight color to be used when the TCP
                |     rotational acceleration limits are exceeded.
                |     ReachColor: defines the highlight color to be used when the "unreachable"
                |     condition is detected.
                |     SingularColor: defines the highlight color to be used when the
                |     "singularity" condition is detected.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rob_analysis_setting_att = com_object

    def get_lin_accel_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLinAccelColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LinAccelColor
                |     parameter.
                |     Role:Retrieves the state of the LinAccelColor parameter in the current
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
        return self.rob_analysis_setting_att.GetLinAccelColorInfo(io_admin_level, io_locked)

    def get_lin_accel_limit_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLinAccelLimitInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LinAccelLimit
                |     parameter.
                |     Role:Retrieves the state of the LinAccelLimit parameter in the current
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
        return self.rob_analysis_setting_att.GetLinAccelLimitInfo(io_admin_level, io_locked)

    def get_lin_speed_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLinSpeedColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LinSpeedColor
                |     parameter.
                |     Role:Retrieves the state of the LinSpeedColor parameter in the current
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
        return self.rob_analysis_setting_att.GetLinSpeedColorInfo(io_admin_level, io_locked)

    def get_lin_speed_limit_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLinSpeedLimitInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LinSpeedLimit
                |     parameter.
                |     Role:Retrieves the state of the LinSpeedLimit parameter in the current
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
        return self.rob_analysis_setting_att.GetLinSpeedLimitInfo(io_admin_level, io_locked)

    def get_reach_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetReachColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment information for the ReachColor
                |     parameter.
                |     Role:Retrieves the state of the ReachColor parameter in the current
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
        return self.rob_analysis_setting_att.GetReachColorInfo(io_admin_level, io_locked)

    def get_rot_accel_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRotAccelColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RotAccelColor
                |     parameter.
                |     Role:Retrieves the state of the RotAccelColor parameter in the current
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
        return self.rob_analysis_setting_att.GetRotAccelColorInfo(io_admin_level, io_locked)

    def get_rot_accel_limit_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRotAccelLimitInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RotAccelLimit
                |     parameter.
                |     Role:Retrieves the state of the RotAccelLimit parameter in the current
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
        return self.rob_analysis_setting_att.GetRotAccelLimitInfo(io_admin_level, io_locked)

    def get_rot_speed_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRotSpeedColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RotSpeedColor
                |     parameter.
                |     Role:Retrieves the state of the RotSpeedColor parameter in the current
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
        return self.rob_analysis_setting_att.GetRotSpeedColorInfo(io_admin_level, io_locked)

    def get_rot_speed_limit_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRotSpeedLimitInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RotSpeedLimit
                |     parameter.
                |     Role:Retrieves the state of the RotSpeedLimit parameter in the current
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
        return self.rob_analysis_setting_att.GetRotSpeedLimitInfo(io_admin_level, io_locked)

    def get_singular_colour_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSingularColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SingularColor
                |     parameter.
                |     Role:Retrieves the state of the SingularColor parameter in the current
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
        return self.rob_analysis_setting_att.GetSingularColorInfo(io_admin_level, io_locked)

    def set_lin_accel_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLinAccelColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the LinAccelColor parameter.
                |     Role:Locks or unlocks the LinAccelColor parameter if it is possible in the
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
        return self.rob_analysis_setting_att.SetLinAccelColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_lin_accel_color_lock'
        # # vba_code = """
        # # Public Function set_lin_accel_color_lock(rob_analysis_setting_att)
        # #     Dim iLocked (2)
        # #     rob_analysis_setting_att.SetLinAccelColorLock iLocked
        # #     set_lin_accel_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_lin_accel_limit_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLinAccelLimitLock(boolean iLocked)
                | 
                |     Locks or unlocks the LinAccelLimit parameter.
                |     Role:Locks or unlocks the LinAccelLimit parameter if it is possible in the
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
        return self.rob_analysis_setting_att.SetLinAccelLimitLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_lin_accel_limit_lock'
        # # vba_code = """
        # # Public Function set_lin_accel_limit_lock(rob_analysis_setting_att)
        # #     Dim iLocked (2)
        # #     rob_analysis_setting_att.SetLinAccelLimitLock iLocked
        # #     set_lin_accel_limit_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_lin_speed_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLinSpeedColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the LinSpeedColor parameter.
                |     Role:Locks or unlocks the LinSpeedColor parameter if it is possible in the
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
        return self.rob_analysis_setting_att.SetLinSpeedColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_lin_speed_color_lock'
        # # vba_code = """
        # # Public Function set_lin_speed_color_lock(rob_analysis_setting_att)
        # #     Dim iLocked (2)
        # #     rob_analysis_setting_att.SetLinSpeedColorLock iLocked
        # #     set_lin_speed_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_lin_speed_limit_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLinSpeedLimitLock(boolean iLocked)
                | 
                |     Locks or unlocks the LinSpeedLimit parameter.
                |     Role:Locks or unlocks the LinSpeedLimit parameter if it is possible in the
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
        return self.rob_analysis_setting_att.SetLinSpeedLimitLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_lin_speed_limit_lock'
        # # vba_code = """
        # # Public Function set_lin_speed_limit_lock(rob_analysis_setting_att)
        # #     Dim iLocked (2)
        # #     rob_analysis_setting_att.SetLinSpeedLimitLock iLocked
        # #     set_lin_speed_limit_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_reach_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetReachColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the ReachColor parameter.
                |     Role:Locks or unlocks the ReachColor parameter if it is possible in the
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
        return self.rob_analysis_setting_att.SetReachColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_reach_color_lock'
        # # vba_code = """
        # # Public Function set_reach_color_lock(rob_analysis_setting_att)
        # #     Dim iLocked (2)
        # #     rob_analysis_setting_att.SetReachColorLock iLocked
        # #     set_reach_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rot_accel_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRotAccelColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the RotAccelColor parameter.
                |     Role:Locks or unlocks the RotAccelColor parameter if it is possible in the
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
        return self.rob_analysis_setting_att.SetRotAccelColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rot_accel_color_lock'
        # # vba_code = """
        # # Public Function set_rot_accel_color_lock(rob_analysis_setting_att)
        # #     Dim iLocked (2)
        # #     rob_analysis_setting_att.SetRotAccelColorLock iLocked
        # #     set_rot_accel_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rot_accel_limit_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRotAccelLimitLock(boolean iLocked)
                | 
                |     Locks or unlocks the RotAccelLimit parameter.
                |     Role:Locks or unlocks the RotAccelLimit parameter if it is possible in the
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
        return self.rob_analysis_setting_att.SetRotAccelLimitLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rot_accel_limit_lock'
        # # vba_code = """
        # # Public Function set_rot_accel_limit_lock(rob_analysis_setting_att)
        # #     Dim iLocked (2)
        # #     rob_analysis_setting_att.SetRotAccelLimitLock iLocked
        # #     set_rot_accel_limit_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rot_speed_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRotSpeedColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the RotSpeedColor parameter.
                |     Role:Locks or unlocks the RotSpeedColor parameter if it is possible in the
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
        return self.rob_analysis_setting_att.SetRotSpeedColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rot_speed_color_lock'
        # # vba_code = """
        # # Public Function set_rot_speed_color_lock(rob_analysis_setting_att)
        # #     Dim iLocked (2)
        # #     rob_analysis_setting_att.SetRotSpeedColorLock iLocked
        # #     set_rot_speed_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rot_speed_limit_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRotSpeedLimitLock(boolean iLocked)
                | 
                |     Locks or unlocks the RotSpeedLimit parameter.
                |     Role:Locks or unlocks the RotSpeedLimit parameter if it is possible in the
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
        return self.rob_analysis_setting_att.SetRotSpeedLimitLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rot_speed_limit_lock'
        # # vba_code = """
        # # Public Function set_rot_speed_limit_lock(rob_analysis_setting_att)
        # #     Dim iLocked (2)
        # #     rob_analysis_setting_att.SetRotSpeedLimitLock iLocked
        # #     set_rot_speed_limit_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_singular_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSingularColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the SingularColor parameter.
                |     Role:Locks or unlocks the SingularColor parameter if it is possible in the
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
        return self.rob_analysis_setting_att.SetSingularColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_singular_color_lock'
        # # vba_code = """
        # # Public Function set_singular_color_lock(rob_analysis_setting_att)
        # #     Dim iLocked (2)
        # #     rob_analysis_setting_att.SetSingularColorLock iLocked
        # #     set_singular_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'RobAnalysisSettingAtt(name="{self.name}")'
