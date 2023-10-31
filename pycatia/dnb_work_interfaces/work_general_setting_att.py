#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class WorkGeneralSettingAtt(SettingController):

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
                |                         WorkGeneralSettingAtt
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement DNBIAWorkGeneralSettingAtt are
                | ...
                | 
                | Do not use the DNBIAWorkGeneralSettingAtt interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.work_general_setting_att = com_object

    @property
    def annotation_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnnotationActivity() As boolean
                | 
                |     Returns or sets the AnnotationActivity parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.work_general_setting_att.AnnotationActivity

    @annotation_activity.setter
    def annotation_activity(self, value: bool):
        """
        :param bool value:
        """

        self.work_general_setting_att.AnnotationActivity = value

    @property
    def dnbwi_num_column_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DNBWINumColumnList() As CATSafeArrayVariant
                | 
                |     Returns the DNBWINumColumnList parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: tuple
        """

        return self.work_general_setting_att.DNBWINumColumnList

    @dnbwi_num_column_list.setter
    def dnbwi_num_column_list(self, value: tuple):
        """
        :param tuple value:
        """

        self.work_general_setting_att.DNBWINumColumnList = value

    @property
    def move_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MoveActivity() As boolean
                | 
                |     Returns or sets the MoveActivity parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.work_general_setting_att.MoveActivity

    @move_activity.setter
    def move_activity(self, value: bool):
        """
        :param bool value:
        """

        self.work_general_setting_att.MoveActivity = value

    @property
    def style_sheet_path(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StyleSheetPath() As CATBSTR
                | 
                |     Returns or sets the StyleSheetPath parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.work_general_setting_att.StyleSheetPath

    @style_sheet_path.setter
    def style_sheet_path(self, value: str):
        """
        :param str value:
        """

        self.work_general_setting_att.StyleSheetPath = value

    @property
    def text_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TextActivity() As boolean
                | 
                |     Returns or sets the TextActivity parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.work_general_setting_att.TextActivity

    @text_activity.setter
    def text_activity(self, value: bool):
        """
        :param bool value:
        """

        self.work_general_setting_att.TextActivity = value

    @property
    def view_point_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ViewPointActivity() As boolean
                | 
                |     Returns or sets the ViewPointActivity parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.work_general_setting_att.ViewPointActivity

    @view_point_activity.setter
    def view_point_activity(self, value: bool):
        """
        :param bool value:
        """

        self.work_general_setting_att.ViewPointActivity = value

    @property
    def visibility_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property VisibilityActivity() As boolean
                | 
                |     Returns or sets the VisibilityActivity parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: bool
        """

        return self.work_general_setting_att.VisibilityActivity

    @visibility_activity.setter
    def visibility_activity(self, value: bool):
        """
        :param bool value:
        """

        self.work_general_setting_att.VisibilityActivity = value

    def get_annotation_activity_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAnnotationActivityInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AnnotationActivity
                |     parameter.
                |     Role:Retrieves the state of the AnnotationActivity parameter in the current
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
        return self.work_general_setting_att.GetAnnotationActivityInfo(io_admin_level, io_locked)

    def get_dnbwi_num_column_list_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDNBWINumColumnListInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DNBWINumColumnList
                |     parameter.
                |     Role:Retrieves the state of the DNBWINumColumnList parameter in the current
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
        return self.work_general_setting_att.GetDNBWINumColumnListInfo(io_admin_level, io_locked)

    def get_move_activity_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMoveActivityInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MoveActivity
                |     parameter.
                |     Role:Retrieves the state of the MoveActivity parameter in the current
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
        return self.work_general_setting_att.GetMoveActivityInfo(io_admin_level, io_locked)

    def get_style_sheet_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStyleSheetPathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the StyleSheetPath
                |     parameter.
                |     Role:Retrieves the state of the StyleSheetPath parameter in the current
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
        return self.work_general_setting_att.GetStyleSheetPathInfo(io_admin_level, io_locked)

    def get_text_activity_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTextActivityInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the TextActivity
                |     parameter.
                |     Role:Retrieves the state of the TextActivity parameter in the current
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
        return self.work_general_setting_att.GetTextActivityInfo(io_admin_level, io_locked)

    def get_view_point_activity_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetViewPointActivityInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ViewPointActivity
                |     parameter.
                |     Role:Retrieves the state of the ViewPointActivity parameter in the current
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
        return self.work_general_setting_att.GetViewPointActivityInfo(io_admin_level, io_locked)

    def get_visibility_activity_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetVisibilityActivityInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the VisibilityActivity
                |     parameter.
                |     Role:Retrieves the state of the VisibilityActivity parameter in the current
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
        return self.work_general_setting_att.GetVisibilityActivityInfo(io_admin_level, io_locked)

    def set_annotation_activity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAnnotationActivityLock(boolean iLocked)
                | 
                |     Locks or unlocks the AnnotationActivity parameter.
                |     Role:Locks or unlocks the AnnotationActivity parameter if it is possible in
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
        return self.work_general_setting_att.SetAnnotationActivityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_annotation_activity_lock'
        # # vba_code = """
        # # Public Function set_annotation_activity_lock(work_general_setting_att)
        # #     Dim iLocked (2)
        # #     work_general_setting_att.SetAnnotationActivityLock iLocked
        # #     set_annotation_activity_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dnbwi_num_column_list_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDNBWINumColumnListLock(boolean iLocked)

        :param bool i_locked:
        :rtype: None
        """
        return self.work_general_setting_att.SetDNBWINumColumnListLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dnbwi_num_column_list_lock'
        # # vba_code = """
        # # Public Function set_dnbwi_num_column_list_lock(work_general_setting_att)
        # #     Dim iLocked (2)
        # #     work_general_setting_att.SetDNBWINumColumnListLock iLocked
        # #     set_dnbwi_num_column_list_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_move_activity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMoveActivityLock(boolean iLocked)
                | 
                |     Locks or unlocks the MoveActivity parameter.
                |     Role:Locks or unlocks the MoveActivity parameter if it is possible in the
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
        return self.work_general_setting_att.SetMoveActivityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_move_activity_lock'
        # # vba_code = """
        # # Public Function set_move_activity_lock(work_general_setting_att)
        # #     Dim iLocked (2)
        # #     work_general_setting_att.SetMoveActivityLock iLocked
        # #     set_move_activity_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_style_sheet_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStyleSheetPathLock(boolean iLocked)
                | 
                |     Locks or unlocks the StyleSheetPath parameter.
                |     Role:Locks or unlocks the StyleSheetPath parameter if it is possible in the
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
        return self.work_general_setting_att.SetStyleSheetPathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_style_sheet_path_lock'
        # # vba_code = """
        # # Public Function set_style_sheet_path_lock(work_general_setting_att)
        # #     Dim iLocked (2)
        # #     work_general_setting_att.SetStyleSheetPathLock iLocked
        # #     set_style_sheet_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_text_activity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTextActivityLock(boolean iLocked)
                | 
                |     Locks or unlocks the TextActivity parameter.
                |     Role:Locks or unlocks the TextActivity parameter if it is possible in the
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
        return self.work_general_setting_att.SetTextActivityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_text_activity_lock'
        # # vba_code = """
        # # Public Function set_text_activity_lock(work_general_setting_att)
        # #     Dim iLocked (2)
        # #     work_general_setting_att.SetTextActivityLock iLocked
        # #     set_text_activity_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_view_point_activity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetViewPointActivityLock(boolean iLocked)
                | 
                |     Locks or unlocks the ViewPointActivity parameter.
                |     Role:Locks or unlocks the ViewPointActivity parameter if it is possible in
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
        return self.work_general_setting_att.SetViewPointActivityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_view_point_activity_lock'
        # # vba_code = """
        # # Public Function set_view_point_activity_lock(work_general_setting_att)
        # #     Dim iLocked (2)
        # #     work_general_setting_att.SetViewPointActivityLock iLocked
        # #     set_view_point_activity_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_visibility_activity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetVisibilityActivityLock(boolean iLocked)
                | 
                |     Locks or unlocks the VisibilityActivity parameter.
                |     Role:Locks or unlocks the VisibilityActivity parameter if it is possible in
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
        return self.work_general_setting_att.SetVisibilityActivityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_visibility_activity_lock'
        # # vba_code = """
        # # Public Function set_visibility_activity_lock(work_general_setting_att)
        # #     Dim iLocked (2)
        # #     work_general_setting_att.SetVisibilityActivityLock iLocked
        # #     set_visibility_activity_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'WorkGeneralSettingAtt(name="{ self.name }")'
