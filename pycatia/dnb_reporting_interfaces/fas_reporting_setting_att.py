#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class FasReportingSettingAtt(SettingController):

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
                |                         FASReportingSettingAtt
                | 
                | The interface to access a DNBIAFASReportingSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.fas_reporting_setting_att = com_object

    @property
    def default_style_sheet(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DefaultStyleSheet() As CATBSTR
                | 
                |     Gets value of "OLP Robot Program Directory" parameter.
                |     Role: Gets value of "OLP Robot Program Directory"
                |     parameter
                | 
                |     Parameters:
                | 
                |         oRobotProgramDir
                |             Variable to return value in. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :rtype: str
        """

        return self.fas_reporting_setting_att.DefaultStyleSheet

    @default_style_sheet.setter
    def default_style_sheet(self, value: str):
        """
        :param str value:
        """

        self.fas_reporting_setting_att.DefaultStyleSheet = value

    @property
    def java_class_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property JavaClassPath() As CATBSTR
                | 
                |     Gets value of "Java Class Path" parameter.
                |     Role: Gets value of "Java Class Path" parameter
                | 
                |     Parameters:
                | 
                |         o
                |             JavaClassPath Variable to return value in. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :rtype: str
        """

        return self.fas_reporting_setting_att.JavaClassPath

    @java_class_path.setter
    def java_class_path(self, value: str):
        """
        :param str value:
        """

        self.fas_reporting_setting_att.JavaClassPath = value

    @property
    def java_exe(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property JavaExe() As CATBSTR
                | 
                |     Gets value of "Java Executable" parameter.
                |     Role: Gets value of "Java Executable" parameter
                | 
                |     Parameters:
                | 
                |         oJavaExe
                |             Variable to return value in. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :rtype: str
        """

        return self.fas_reporting_setting_att.JavaExe

    @java_exe.setter
    def java_exe(self, value: str):
        """
        :param str value:
        """

        self.fas_reporting_setting_att.JavaExe = value

    @property
    def result_output_dir(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ResultOutputDir() As CATBSTR
                | 
                |     Gets value of "OLP Robot Program Directory" parameter.
                |     Role: Gets value of "OLP Robot Program Directory"
                |     parameter
                | 
                |     Parameters:
                | 
                |         oRobotProgramDir
                |             Variable to return value in. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :rtype: str
        """

        return self.fas_reporting_setting_att.ResultOutputDir

    @result_output_dir.setter
    def result_output_dir(self, value: str):
        """
        :param str value:
        """

        self.fas_reporting_setting_att.ResultOutputDir = value

    @property
    def svg_viewer(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SVGViewer() As long
                | 
                |     Gets value of "OLP Robot Program Directory" parameter.
                |     Role: Gets value of "OLP Robot Program Directory"
                |     parameter
                | 
                |     Parameters:
                | 
                |         oRobotProgramDir
                |             Variable to return value in. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :rtype: int
        """

        return self.fas_reporting_setting_att.SVGViewer

    @svg_viewer.setter
    def svg_viewer(self, value: int):
        """
        :param int value:
        """

        self.fas_reporting_setting_att.SVGViewer = value

    @property
    def style_sheet_dir(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StyleSheetDir() As CATBSTR
                | 
                |     Gets value of "OLP Robot Program Directory" parameter.
                |     Role: Gets value of "OLP Robot Program Directory"
                |     parameter
                | 
                |     Parameters:
                | 
                |         oRobotProgramDir
                |             Variable to return value in. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :rtype: str
        """

        return self.fas_reporting_setting_att.StyleSheetDir

    @style_sheet_dir.setter
    def style_sheet_dir(self, value: str):
        """
        :param str value:
        """

        self.fas_reporting_setting_att.StyleSheetDir = value

    def get_default_style_sheet_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDefaultStyleSheetInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Gets information on "OLP Robot Program Directory"
                |     parameter.
                |     Role: Gets information on "OLP Robot Program Directory"
                |     parameter
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
                |         the administrated value. Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.fas_reporting_setting_att.GetDefaultStyleSheetInfo(io_admin_level, io_locked)

    def get_java_class_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetJavaClassPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Gets information on "Java Class Path" parameter.
                |     Role: Gets information on "Java Class Path" parameter
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
                |         the administrated value. Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.fas_reporting_setting_att.GetJavaClassPathInfo(io_admin_level, io_locked)

    def get_java_exe_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetJavaExeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Gets information on "Java Executable" parameter.
                |     Role: Gets information on "Java Executable" parameter
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
                |         the administrated value. Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.fas_reporting_setting_att.GetJavaExeInfo(io_admin_level, io_locked)

    def get_result_output_dir_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetResultOutputDirInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Gets information on "OLP Robot Program Directory"
                |     parameter.
                |     Role: Gets information on "OLP Robot Program Directory"
                |     parameter
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
                |         the administrated value. Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.fas_reporting_setting_att.GetResultOutputDirInfo(io_admin_level, io_locked)

    def get_svg_viewer_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSVGViewerInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Gets information on "OLP Robot Program Directory"
                |     parameter.
                |     Role: Gets information on "OLP Robot Program Directory"
                |     parameter
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
                |         the administrated value. Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.fas_reporting_setting_att.GetSVGViewerInfo(io_admin_level, io_locked)

    def get_style_sheet_dir_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStyleSheetDirInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Gets information on "OLP Robot Program Directory"
                |     parameter.
                |     Role: Gets information on "OLP Robot Program Directory"
                |     parameter
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
                |         the administrated value. Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.fas_reporting_setting_att.GetStyleSheetDirInfo(io_admin_level, io_locked)

    def set_default_style_sheet_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDefaultStyleSheetLock(boolean iLocked)
                | 
                |     Locks or unlocks the "OLP Robot Program Directory"
                |     parameter.
                |     Role: Locks or unlocks the "OLP Robot Program Directory" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.fas_reporting_setting_att.SetDefaultStyleSheetLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_style_sheet_lock'
        # # vba_code = """
        # # Public Function set_default_style_sheet_lock(fas_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     fas_reporting_setting_att.SetDefaultStyleSheetLock iLocked
        # #     set_default_style_sheet_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_java_class_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetJavaClassPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Java Class Path" parameter.
                |     Role: Locks or unlocks the "Java Class Path" parameter if the operation is
                |     allowed in the current administrated environment. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.fas_reporting_setting_att.SetJavaClassPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_java_class_path_lock'
        # # vba_code = """
        # # Public Function set_java_class_path_lock(fas_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     fas_reporting_setting_att.SetJavaClassPathLock iLocked
        # #     set_java_class_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_java_exe_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetJavaExeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Java Executable" parameter.
                |     Role: Locks or unlocks the "Java Executable" parameter if the operation is
                |     allowed in the current administrated environment. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.fas_reporting_setting_att.SetJavaExeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_java_exe_lock'
        # # vba_code = """
        # # Public Function set_java_exe_lock(fas_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     fas_reporting_setting_att.SetJavaExeLock iLocked
        # #     set_java_exe_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_result_output_dir_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetResultOutputDirLock(boolean iLocked)
                | 
                |     Locks or unlocks the "OLP Robot Program Directory"
                |     parameter.
                |     Role: Locks or unlocks the "OLP Robot Program Directory" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.fas_reporting_setting_att.SetResultOutputDirLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_result_output_dir_lock'
        # # vba_code = """
        # # Public Function set_result_output_dir_lock(fas_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     fas_reporting_setting_att.SetResultOutputDirLock iLocked
        # #     set_result_output_dir_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_svg_viewer_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSVGViewerLock(boolean iLocked)
                | 
                |     Locks or unlocks the "OLP Robot Program Directory"
                |     parameter.
                |     Role: Locks or unlocks the "OLP Robot Program Directory" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.fas_reporting_setting_att.SetSVGViewerLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_svg_viewer_lock'
        # # vba_code = """
        # # Public Function set_svg_viewer_lock(fas_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     fas_reporting_setting_att.SetSVGViewerLock iLocked
        # #     set_svg_viewer_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_style_sheet_dir_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStyleSheetDirLock(boolean iLocked)
                | 
                |     Locks or unlocks the "OLP Robot Program Directory"
                |     parameter.
                |     Role: Locks or unlocks the "OLP Robot Program Directory" parameter if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on Failure

        :param bool i_locked:
        :rtype: None
        """
        return self.fas_reporting_setting_att.SetStyleSheetDirLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_style_sheet_dir_lock'
        # # vba_code = """
        # # Public Function set_style_sheet_dir_lock(fas_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     fas_reporting_setting_att.SetStyleSheetDirLock iLocked
        # #     set_style_sheet_dir_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'FasReportingSettingAtt(name="{ self.name }")'
