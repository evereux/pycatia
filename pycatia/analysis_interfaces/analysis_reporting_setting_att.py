#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class AnalysisReportingSettingAtt(SettingController):

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
                |                         AnalysisReportingSettingAtt
                | 
                | Interface to handle the Analysis & Simulation
                | "ReportingSetting".
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_reporting_setting_att = com_object

    @property
    def background_image_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BackgroundImageMode() As boolean
                | 
                |     Returns or sets the BackgroundImageMode parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.analysis_reporting_setting_att.BackgroundImageMode

    @background_image_mode.setter
    def background_image_mode(self, value: bool):
        """
        :param bool value:
        """

        self.analysis_reporting_setting_att.BackgroundImageMode = value

    @property
    def custom_background_image(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CustomBackgroundImage() As CATBSTR
                | 
                |     Returns or sets the CustomBackgroundImage parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.analysis_reporting_setting_att.CustomBackgroundImage

    @custom_background_image.setter
    def custom_background_image(self, value: str):
        """
        :param str value:
        """

        self.analysis_reporting_setting_att.CustomBackgroundImage = value

    @property
    def custom_image_format(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CustomImageFormat() As CATBSTR
                | 
                |     Returns or sets the CustomImageFormat parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.analysis_reporting_setting_att.CustomImageFormat

    @custom_image_format.setter
    def custom_image_format(self, value: str):
        """
        :param str value:
        """

        self.analysis_reporting_setting_att.CustomImageFormat = value

    @property
    def custom_image_height(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CustomImageHeight() As long
                | 
                |     Returns or sets the CustomImageHeight parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.analysis_reporting_setting_att.CustomImageHeight

    @custom_image_height.setter
    def custom_image_height(self, value: int):
        """
        :param int value:
        """

        self.analysis_reporting_setting_att.CustomImageHeight = value

    @property
    def custom_image_width(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CustomImageWidth() As long
                | 
                |     Returns or sets the CustomImageWidth parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.analysis_reporting_setting_att.CustomImageWidth

    @custom_image_width.setter
    def custom_image_width(self, value: int):
        """
        :param int value:
        """

        self.analysis_reporting_setting_att.CustomImageWidth = value

    @property
    def image_quality_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImageQualityMode() As boolean
                | 
                |     Returns or sets the ImageQualityMode parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.analysis_reporting_setting_att.ImageQualityMode

    @image_quality_mode.setter
    def image_quality_mode(self, value: bool):
        """
        :param bool value:
        """

        self.analysis_reporting_setting_att.ImageQualityMode = value

    @property
    def temp_output_directory(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TempOutputDirectory() As CATBSTR
                | 
                |     Returns or sets the TempOutputDirectory parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.analysis_reporting_setting_att.TempOutputDirectory

    @temp_output_directory.setter
    def temp_output_directory(self, value: str):
        """
        :param str value:
        """

        self.analysis_reporting_setting_att.TempOutputDirectory = value

    def get_background_image_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetBackgroundImageModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the BackgroundImageMode
                |     parameter.
                |     Role:Retrieves the state of the BackgroundImageMode parameter in the
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
        return self.analysis_reporting_setting_att.GetBackgroundImageModeInfo(io_admin_level, io_locked)

    def get_custom_background_image_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCustomBackgroundImageInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the CustomBackgroundImage
                |     parameter.
                |     Role:Retrieves the state of the CustomBackgroundImage parameter in the
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
        return self.analysis_reporting_setting_att.GetCustomBackgroundImageInfo(io_admin_level, io_locked)

    def get_custom_image_format_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCustomImageFormatInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the CustomImageFormat
                |     parameter.
                |     Role:Retrieves the state of the CustomImageFormat parameter in the current
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
        return self.analysis_reporting_setting_att.GetCustomImageFormatInfo(io_admin_level, io_locked)

    def get_custom_image_height_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCustomImageHeightInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the CustomImageHeight
                |     parameter.
                |     Role:Retrieves the state of the CustomImageHeight parameter in the current
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
        return self.analysis_reporting_setting_att.GetCustomImageHeightInfo(io_admin_level, io_locked)

    def get_custom_image_width_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCustomImageWidthInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the CustomImageWidth
                |     parameter.
                |     Role:Retrieves the state of the CustomImageWidth parameter in the current
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
        return self.analysis_reporting_setting_att.GetCustomImageWidthInfo(io_admin_level, io_locked)

    def get_image_quality_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImageQualityModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImageQualityMode
                |     parameter.
                |     Role:Retrieves the state of the ImageQualityMode parameter in the current
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
        return self.analysis_reporting_setting_att.GetImageQualityModeInfo(io_admin_level, io_locked)

    def get_temp_output_directory_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTempOutputDirectoryInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TempOutputDirectory
                |     parameter.
                |     Role:Retrieves the state of the TempOutputDirectory parameter in the
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
        return self.analysis_reporting_setting_att.GetTempOutputDirectoryInfo(io_admin_level, io_locked)

    def set_background_image_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBackgroundImageModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the BackgroundImageMode parameter.
                |     Role:Locks or unlocks the BackgroundImageMode parameter if it is possible
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
        return self.analysis_reporting_setting_att.SetBackgroundImageModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_background_image_mode_lock'
        # # vba_code = """
        # # Public Function set_background_image_mode_lock(analysis_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_reporting_setting_att.SetBackgroundImageModeLock iLocked
        # #     set_background_image_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_custom_background_image_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCustomBackgroundImageLock(boolean iLocked)
                | 
                |     Locks or unlocks the CustomBackgroundImage parameter.
                |     Role:Locks or unlocks the CustomBackgroundImage parameter if it is possible
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
        return self.analysis_reporting_setting_att.SetCustomBackgroundImageLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_custom_background_image_lock'
        # # vba_code = """
        # # Public Function set_custom_background_image_lock(analysis_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_reporting_setting_att.SetCustomBackgroundImageLock iLocked
        # #     set_custom_background_image_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_custom_image_format_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCustomImageFormatLock(boolean iLocked)
                | 
                |     Locks or unlocks the CustomImageFormat parameter.
                |     Role:Locks or unlocks the CustomImageFormat parameter if it is possible in
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
        return self.analysis_reporting_setting_att.SetCustomImageFormatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_custom_image_format_lock'
        # # vba_code = """
        # # Public Function set_custom_image_format_lock(analysis_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_reporting_setting_att.SetCustomImageFormatLock iLocked
        # #     set_custom_image_format_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_custom_image_height_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCustomImageHeightLock(boolean iLocked)
                | 
                |     Locks or unlocks the CustomImageHeight parameter.
                |     Role:Locks or unlocks the ImageHeight parameter if it is possible in the
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
        return self.analysis_reporting_setting_att.SetCustomImageHeightLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_custom_image_height_lock'
        # # vba_code = """
        # # Public Function set_custom_image_height_lock(analysis_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_reporting_setting_att.SetCustomImageHeightLock iLocked
        # #     set_custom_image_height_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_custom_image_width_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCustomImageWidthLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImageWidth parameter.
                |     Role:Locks or unlocks the ImageWidth parameter if it is possible in the
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
        return self.analysis_reporting_setting_att.SetCustomImageWidthLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_custom_image_width_lock'
        # # vba_code = """
        # # Public Function set_custom_image_width_lock(analysis_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_reporting_setting_att.SetCustomImageWidthLock iLocked
        # #     set_custom_image_width_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_image_quality_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImageQualityModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImageQualityMode parameter.
                |     Role:Locks or unlocks the DefaultImageQuality parameter if it is possible
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
        return self.analysis_reporting_setting_att.SetImageQualityModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_image_quality_mode_lock'
        # # vba_code = """
        # # Public Function set_image_quality_mode_lock(analysis_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_reporting_setting_att.SetImageQualityModeLock iLocked
        # #     set_image_quality_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_temp_output_directory_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTempOutputDirectoryLock(boolean iLocked)
                | 
                |     Locks or unlocks the TempOutputDirectory parameter.
                |     Role:Locks or unlocks the TempOutputDirectory parameter if it is possible
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
        return self.analysis_reporting_setting_att.SetTempOutputDirectoryLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_temp_output_directory_lock'
        # # vba_code = """
        # # Public Function set_temp_output_directory_lock(analysis_reporting_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_reporting_setting_att.SetTempOutputDirectoryLock iLocked
        # #     set_temp_output_directory_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AnalysisReportingSettingAtt(name="{ self.name }")'
