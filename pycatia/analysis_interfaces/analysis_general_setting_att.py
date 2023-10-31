#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class AnalysisGeneralSettingAtt(SettingController):

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
                |                         AnalysisGeneralSettingAtt
                | 
                | Interface to handle the Analysis & Simulation
                | "GeneralSetting".
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_general_setting_att = com_object

    @property
    def analysis_cache_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisCacheMode() As long
                | 
                |     Tells if Product Structure Cache Mode will be handled.

        :rtype: int
        """

        return self.analysis_general_setting_att.AnalysisCacheMode

    @analysis_cache_mode.setter
    def analysis_cache_mode(self, value: int):
        """
        :param int value:
        """

        self.analysis_general_setting_att.AnalysisCacheMode = value

    @property
    def analysis_load_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisLoadMode() As long
                | 
                |     Retrieves if pointed document will be loaded.

        :rtype: int
        """

        return self.analysis_general_setting_att.AnalysisLoadMode

    @analysis_load_mode.setter
    def analysis_load_mode(self, value: int):
        """
        :param int value:
        """

        self.analysis_general_setting_att.AnalysisLoadMode = value

    @property
    def analysis_naming_auto(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisNamingAuto() As long
                | 
                |     Tells if Automatic naming will be activated.

        :rtype: int
        """

        return self.analysis_general_setting_att.AnalysisNamingAuto

    @analysis_naming_auto.setter
    def analysis_naming_auto(self, value: int):
        """
        :param int value:
        """

        self.analysis_general_setting_att.AnalysisNamingAuto = value

    @property
    def default_analysis_flag(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DefaultAnalysisFlag() As long
                | 
                |     Retrieves if a default analysis Case will be created.

        :rtype: int
        """

        return self.analysis_general_setting_att.DefaultAnalysisFlag

    @default_analysis_flag.setter
    def default_analysis_flag(self, value: int):
        """
        :param int value:
        """

        self.analysis_general_setting_att.DefaultAnalysisFlag = value

    @property
    def default_analysis_template(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DefaultAnalysisTemplate() As CATBSTR
                | 
                |     Retrieves the name of the default analysis Case that will be created.

        :rtype: str
        """

        return self.analysis_general_setting_att.DefaultAnalysisTemplate

    @default_analysis_template.setter
    def default_analysis_template(self, value: str):
        """
        :param str value:
        """

        self.analysis_general_setting_att.DefaultAnalysisTemplate = value

    @property
    def view_analysis_parameter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ViewAnalysisParameter() As long
                | 
                |     Retrieves if the Parameter set is visible in the feature tree of the
                |     analysis document.

        :rtype: int
        """

        return self.analysis_general_setting_att.ViewAnalysisParameter

    @view_analysis_parameter.setter
    def view_analysis_parameter(self, value: int):
        """
        :param int value:
        """

        self.analysis_general_setting_att.ViewAnalysisParameter = value

    @property
    def view_analysis_relation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ViewAnalysisRelation() As long
                | 
                |     Retrieves if the Relation set is visible in the feature tree of the
                |     analysis document.

        :rtype: int
        """

        return self.analysis_general_setting_att.ViewAnalysisRelation

    @view_analysis_relation.setter
    def view_analysis_relation(self, value: int):
        """
        :param int value:
        """

        self.analysis_general_setting_att.ViewAnalysisRelation = value

    def get_analysis_cache_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAnalysisCacheModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the parameter.
                |     Role:Retrieves the state of the parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.analysis_general_setting_att.GetAnalysisCacheModeInfo(io_admin_level, io_locked)

    def get_analysis_load_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAnalysisLoadModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the parameter.
                |     Role:Retrieves the state of the parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.analysis_general_setting_att.GetAnalysisLoadModeInfo(io_admin_level, io_locked)

    def get_analysis_naming_auto_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAnalysisNamingAutoInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the parameter.
                |     Role:Retrieves the state of the parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.analysis_general_setting_att.GetAnalysisNamingAutoInfo(io_admin_level, io_locked)

    def get_default_analysis_flag_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDefaultAnalysisFlagInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the default flag.
                |     Role:Retrieves the state of the default flag in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.analysis_general_setting_att.GetDefaultAnalysisFlagInfo(io_admin_level, io_locked)

    def get_default_analysis_template_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDefaultAnalysisTemplateInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the default
                |     template.
                |     Role:Retrieves the state of the default template in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.analysis_general_setting_att.GetDefaultAnalysisTemplateInfo(io_admin_level, io_locked)

    def get_view_analysis_parameter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetViewAnalysisParameterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the parameter.
                |     Role:Retrieves the state of the parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.analysis_general_setting_att.GetViewAnalysisParameterInfo(io_admin_level, io_locked)

    def get_view_analysis_relation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetViewAnalysisRelationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the parameter.
                |     Role:Retrieves the state of the parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.analysis_general_setting_att.GetViewAnalysisRelationInfo(io_admin_level, io_locked)

    def set_analysis_cache_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAnalysisCacheModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.analysis_general_setting_att.SetAnalysisCacheModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_analysis_cache_mode_lock'
        # # vba_code = """
        # # Public Function set_analysis_cache_mode_lock(analysis_general_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_general_setting_att.SetAnalysisCacheModeLock iLocked
        # #     set_analysis_cache_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_analysis_load_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAnalysisLoadModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.analysis_general_setting_att.SetAnalysisLoadModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_analysis_load_mode_lock'
        # # vba_code = """
        # # Public Function set_analysis_load_mode_lock(analysis_general_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_general_setting_att.SetAnalysisLoadModeLock iLocked
        # #     set_analysis_load_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_analysis_naming_auto_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAnalysisNamingAutoLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.analysis_general_setting_att.SetAnalysisNamingAutoLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_analysis_naming_auto_lock'
        # # vba_code = """
        # # Public Function set_analysis_naming_auto_lock(analysis_general_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_general_setting_att.SetAnalysisNamingAutoLock iLocked
        # #     set_analysis_naming_auto_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_analysis_flag_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDefaultAnalysisFlagLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.analysis_general_setting_att.SetDefaultAnalysisFlagLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_analysis_flag_lock'
        # # vba_code = """
        # # Public Function set_default_analysis_flag_lock(analysis_general_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_general_setting_att.SetDefaultAnalysisFlagLock iLocked
        # #     set_default_analysis_flag_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_analysis_template_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDefaultAnalysisTemplateLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.analysis_general_setting_att.SetDefaultAnalysisTemplateLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_analysis_template_lock'
        # # vba_code = """
        # # Public Function set_default_analysis_template_lock(analysis_general_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_general_setting_att.SetDefaultAnalysisTemplateLock iLocked
        # #     set_default_analysis_template_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_view_analysis_parameter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetViewAnalysisParameterLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.analysis_general_setting_att.SetViewAnalysisParameterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_view_analysis_parameter_lock'
        # # vba_code = """
        # # Public Function set_view_analysis_parameter_lock(analysis_general_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_general_setting_att.SetViewAnalysisParameterLock iLocked
        # #     set_view_analysis_parameter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_view_analysis_relation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetViewAnalysisRelationLock(boolean iLocked)
                | 
                |     Locks or unlocks the flag.
                |     Role:Locks or unlocks the parameter if it is possible in the current
                |     administrated. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             The locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.analysis_general_setting_att.SetViewAnalysisRelationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_view_analysis_relation_lock'
        # # vba_code = """
        # # Public Function set_view_analysis_relation_lock(analysis_general_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_general_setting_att.SetViewAnalysisRelationLock iLocked
        # #     set_view_analysis_relation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AnalysisGeneralSettingAtt(name="{ self.name }")'
