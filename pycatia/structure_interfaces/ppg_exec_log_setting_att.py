#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class PpgExecLogSettingAtt(SettingController):

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
                |                         PPGExecLogSettingAtt
                | 
                | The interface to access a CATIAPPGExecLogSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ppg_exec_log_setting_att = com_object

    @property
    def exec_log_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExecLogPath() As CATBSTR
                | 
                |     Returns or sets the Xxx parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.ppg_exec_log_setting_att.ExecLogPath

    @exec_log_path.setter
    def exec_log_path(self, value: str):
        """
        :param str value:
        """

        self.ppg_exec_log_setting_att.ExecLogPath = value

    @property
    def gen_exec_log(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GenExecLog() As boolean

        :rtype: bool
        """

        return self.ppg_exec_log_setting_att.GenExecLog

    @gen_exec_log.setter
    def gen_exec_log(self, value: bool):
        """
        :param bool value:
        """

        self.ppg_exec_log_setting_att.GenExecLog = value

    def get_exec_log_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExecLogPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Xxx parameter.
                |     Role:Retrieves the state of the Xxx parameter in the current
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
        return self.ppg_exec_log_setting_att.GetExecLogPathInfo(io_admin_level, io_locked)

    def get_gen_exec_log_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetGenExecLogInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.ppg_exec_log_setting_att.GetGenExecLogInfo(io_admin_level, io_locked)

    def set_exec_log_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExecLogPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the Xxx parameter.
                |     Role:Locks or unlocks the Xxx parameter if it is possible in the current
                |     administrative context. In user mode this method will always return
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
        return self.ppg_exec_log_setting_att.SetExecLogPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_exec_log_path_lock'
        # # vba_code = """
        # # Public Function set_exec_log_path_lock(ppg_exec_log_setting_att)
        # #     Dim iLocked (2)
        # #     ppg_exec_log_setting_att.SetExecLogPathLock iLocked
        # #     set_exec_log_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_gen_exec_log_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGenExecLogLock(boolean iLocked)

        :param bool i_locked:
        :rtype: None
        """
        return self.ppg_exec_log_setting_att.SetGenExecLogLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_gen_exec_log_lock'
        # # vba_code = """
        # # Public Function set_gen_exec_log_lock(ppg_exec_log_setting_att)
        # #     Dim iLocked (2)
        # #     ppg_exec_log_setting_att.SetGenExecLogLock iLocked
        # #     set_gen_exec_log_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PpgExecLogSettingAtt(name="{ self.name }")'
