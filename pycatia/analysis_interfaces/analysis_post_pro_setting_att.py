#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class AnalysisPostProSettingAtt(SettingController):

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
                |                         AnalysisPostProSettingAtt
                | 
                | Interface to handle the Analysis & Simulation
                | "PostProcessingSetting".
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_post_pro_setting_att = com_object

    @property
    def auto_preview_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoPreviewMode() As boolean
                | 
                |     Returns or sets the AutoPreviewMode parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.analysis_post_pro_setting_att.AutoPreviewMode

    @auto_preview_mode.setter
    def auto_preview_mode(self, value: bool):
        """
        :param bool value:
        """

        self.analysis_post_pro_setting_att.AutoPreviewMode = value

    @property
    def image_text_size(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImageTextSize() As float
                | 
                |     Returns or sets the ImageTextSize parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.analysis_post_pro_setting_att.ImageTextSize

    @image_text_size.setter
    def image_text_size(self, value: float):
        """
        :param float value:
        """

        self.analysis_post_pro_setting_att.ImageTextSize = value

    @property
    def image_text_stacking(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImageTextStacking() As long
                | 
                |     Returns or sets the ImageTextStacking parameter.
                | 
                |     Parameters:
                | 
                |         iImageTextStacking
                |             Legal values:
                |             0 : Text stacking is Horizontal
                |             1 : Text stacking is Vertical Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.analysis_post_pro_setting_att.ImageTextStacking

    @image_text_stacking.setter
    def image_text_stacking(self, value: int):
        """
        :param int value:
        """

        self.analysis_post_pro_setting_att.ImageTextStacking = value

    @property
    def mode_image_text_size(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ModeImageTextSize() As boolean
                | 
                |     Returns or sets the ModeImageTextSize parameter.
                | 
                |     Parameters:
                | 
                |         iModeImageTextSize
                |             Legal values:
                |             TRUE : Enables the setting of image text size
                |             FALSE: Disables the setting of image text size Ensure consistency
                |             with the C++ interface to which the work is
                |             delegated.

        :rtype: bool
        """

        return self.analysis_post_pro_setting_att.ModeImageTextSize

    @mode_image_text_size.setter
    def mode_image_text_size(self, value: bool):
        """
        :param bool value:
        """

        self.analysis_post_pro_setting_att.ModeImageTextSize = value

    @property
    def save_as_new_template_directory(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SaveAsNewTemplateDirectory() As CATBSTR
                | 
                |     Returns or sets the SaveAsNewTemplateDirectory parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.analysis_post_pro_setting_att.SaveAsNewTemplateDirectory

    @save_as_new_template_directory.setter
    def save_as_new_template_directory(self, value: str):
        """
        :param str value:
        """

        self.analysis_post_pro_setting_att.SaveAsNewTemplateDirectory = value

    def get_auto_preview_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAutoPreviewModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AutoPreviewMode
                |     parameter.
                |     Role:Retrieves the state of the AutoPreviewMode parameter in the current
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
        return self.analysis_post_pro_setting_att.GetAutoPreviewModeInfo(io_admin_level, io_locked)

    def get_image_text_size_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImageTextSizeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImageTextSize
                |     parameter.
                |     Role:Retrieves the state of the ImageTextSize parameter in the current
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
        return self.analysis_post_pro_setting_att.GetImageTextSizeInfo(io_admin_level, io_locked)

    def get_image_text_stacking_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImageTextStackingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ImageTextStacking
                |     parameter.
                |     Role:Retrieves the state of the ImageTextStacking parameter in the current
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
        return self.analysis_post_pro_setting_att.GetImageTextStackingInfo(io_admin_level, io_locked)

    def get_mode_image_text_size_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetModeImageTextSizeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ModeImageTextSize
                |     parameter.
                |     Role:Retrieves the state of the ModeImageTextSize parameter in the current
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
        return self.analysis_post_pro_setting_att.GetModeImageTextSizeInfo(io_admin_level, io_locked)

    def get_save_as_new_template_directory_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSaveAsNewTemplateDirectoryInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SaveAsNewTemplateDirectory
                |     parameter.
                |     Role:Retrieves the state of the SaveAsNewTemplateDirectory parameter in the
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
        return self.analysis_post_pro_setting_att.GetSaveAsNewTemplateDirectoryInfo(io_admin_level, io_locked)

    def set_auto_preview_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAutoPreviewModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the AutoPreviewMode parameter.
                |     Role:Locks or unlocks the AutoPreviewMode parameter if it is possible in
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
        return self.analysis_post_pro_setting_att.SetAutoPreviewModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_preview_mode_lock'
        # # vba_code = """
        # # Public Function set_auto_preview_mode_lock(analysis_post_pro_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_post_pro_setting_att.SetAutoPreviewModeLock iLocked
        # #     set_auto_preview_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_image_text_size_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImageTextSizeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImageTextSize parameter.
                |     Role:Locks or unlocks the ImageTextSize parameter if it is possible in the
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
        return self.analysis_post_pro_setting_att.SetImageTextSizeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_image_text_size_lock'
        # # vba_code = """
        # # Public Function set_image_text_size_lock(analysis_post_pro_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_post_pro_setting_att.SetImageTextSizeLock iLocked
        # #     set_image_text_size_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_image_text_stacking_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImageTextStackingLock(boolean iLocked)
                | 
                |     Locks or unlocks the ImageTextStacking parameter.
                |     Role:Locks or unlocks the ImageTextStacking parameter if it is possible in
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
        return self.analysis_post_pro_setting_att.SetImageTextStackingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_image_text_stacking_lock'
        # # vba_code = """
        # # Public Function set_image_text_stacking_lock(analysis_post_pro_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_post_pro_setting_att.SetImageTextStackingLock iLocked
        # #     set_image_text_stacking_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_mode_image_text_size_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetModeImageTextSizeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ModeImageTextSize parameter.
                |     Role:Locks or unlocks the ModeImageTextSize parameter if it is possible in
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
        return self.analysis_post_pro_setting_att.SetModeImageTextSizeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_mode_image_text_size_lock'
        # # vba_code = """
        # # Public Function set_mode_image_text_size_lock(analysis_post_pro_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_post_pro_setting_att.SetModeImageTextSizeLock iLocked
        # #     set_mode_image_text_size_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_save_as_new_template_directory_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSaveAsNewTemplateDirectoryLock(boolean iLocked)
                | 
                |     Locks or unlocks the SaveAsNewTemplateDirectory parameter.
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
        return self.analysis_post_pro_setting_att.SetSaveAsNewTemplateDirectoryLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_save_as_new_template_directory_lock'
        # # vba_code = """
        # # Public Function set_save_as_new_template_directory_lock(analysis_post_pro_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_post_pro_setting_att.SetSaveAsNewTemplateDirectoryLock iLocked
        # #     set_save_as_new_template_directory_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AnalysisPostProSettingAtt(name="{ self.name }")'
