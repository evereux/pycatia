#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class GeneralSessionSettingAtt(SettingController):
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
                |                         GeneralSessionSettingAtt
                | 
                | Setting controller for the General property tab page.
                | Role: This interface is implemented by a component which represents the
                | controller of the general settings.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.general_session_setting_att = com_object

    @property
    def auto_save(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AutoSave() As CATGenDataSave
                | 
                |     Returns the data save parameter.

        :return: enum cat_gen_data_save
        :rtype: int
        """

        return self.general_session_setting_att.AutoSave

    @auto_save.setter
    def auto_save(self, value: int):
        """
        :param int value: enum cat_gen_data_save
        """

        self.general_session_setting_att.AutoSave = value

    @property
    def conferencing(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Conferencing() As CATGenConferencing
                | 
                |     Returns the conference driver parameter.

        :return: enum cat_gen_conferencing
        :rtype: int
        """

        return self.general_session_setting_att.Conferencing

    @conferencing.setter
    def conferencing(self, value: int):
        """
        :param int value: enum cat_gen_conferencing
        """

        self.general_session_setting_att.Conferencing = value

    @property
    def drag_drop(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DragDrop() As boolean
                | 
                |     Returns the drag & drop parameter.

        :rtype: bool
        """

        return self.general_session_setting_att.DragDrop

    @drag_drop.setter
    def drag_drop(self, value: bool):
        """
        :param bool value:
        """

        self.general_session_setting_att.DragDrop = value

    @property
    def ref_doc(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RefDoc() As boolean
                | 
                |     Returns the referenced documents parameter.

        :rtype: bool
        """

        return self.general_session_setting_att.RefDoc

    @ref_doc.setter
    def ref_doc(self, value: bool):
        """
        :param bool value:
        """

        self.general_session_setting_att.RefDoc = value

    @property
    def time_roll(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TimeRoll() As long
                | 
                |     Returns the data save parameter (in milliseconds).

        :rtype: int
        """

        return self.general_session_setting_att.TimeRoll

    @time_roll.setter
    def time_roll(self, value: int):
        """
        :param int value:
        """

        self.general_session_setting_att.TimeRoll = value

    @property
    def ui_style(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property UIStyle() As CATGenUIStyle
                | 
                |     Returns the user interface style parameter.

        :return: enum cat_gen_ui_style
        :rtype: int
        """

        return self.general_session_setting_att.UIStyle

    @ui_style.setter
    def ui_style(self, value: int):
        """
        :param int value: enum cat_gen_ui_style
        """

        self.general_session_setting_att.UIStyle = value

    def get_auto_save_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAutoSaveInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the data save
                |     parameter.
                |     Role:Retrieves the state of the data save parameter in the current
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
        return self.general_session_setting_att.GetAutoSaveInfo(io_admin_level, io_locked)

    def get_conferencing_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetConferencingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the conference driver
                |     parameter.
                |     Role:Retrieves the state of the conference driver parameter in the current
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
        return self.general_session_setting_att.GetConferencingInfo(io_admin_level, io_locked)

    def get_drag_drop_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDragDropInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the drag & drop
                |     parameter.
                |     Role:Retrieves the state of the drag & drop parameter in the current
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
        return self.general_session_setting_att.GetDragDropInfo(io_admin_level, io_locked)

    def get_ref_doc_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetRefDocInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the referenced documents
                |     parameter.
                |     Role:Retrieves the state of the referenced documents parameter in the
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
        return self.general_session_setting_att.GetRefDocInfo(io_admin_level, io_locked)

    def get_ui_style_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetUIStyleInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the user interface style
                |     parameter.
                |     Role:Retrieves the state of the user interface style parameter in the
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
        return self.general_session_setting_att.GetUIStyleInfo(io_admin_level, io_locked)

    def set_auto_save_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAutoSaveLock(boolean iLocked)
                | 
                |     Locks or unlocks the data save parameter.
                |     Role:Locks or unlocks the data save parameter if it is possible in the
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
        return self.general_session_setting_att.SetAutoSaveLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_save_lock'
        # # vba_code = """
        # # Public Function set_auto_save_lock(general_session_setting_att)
        # #     Dim iLocked (2)
        # #     general_session_setting_att.SetAutoSaveLock iLocked
        # #     set_auto_save_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_conferencing_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetConferencingLock(boolean iLocked)
                | 
                |     Locks or unlocks the conference driver parameter.
                |     Role:Locks or unlocks the conference driver parameter if it is possible in
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
        return self.general_session_setting_att.SetConferencingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_conferencing_lock'
        # # vba_code = """
        # # Public Function set_conferencing_lock(general_session_setting_att)
        # #     Dim iLocked (2)
        # #     general_session_setting_att.SetConferencingLock iLocked
        # #     set_conferencing_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_drag_drop_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDragDropLock(boolean iLocked)
                | 
                |     Locks or unlocks the drag & drop parameter.
                |     Role:Locks or unlocks the drag & drop parameter if it is possible in the
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
        return self.general_session_setting_att.SetDragDropLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_drag_drop_lock'
        # # vba_code = """
        # # Public Function set_drag_drop_lock(general_session_setting_att)
        # #     Dim iLocked (2)
        # #     general_session_setting_att.SetDragDropLock iLocked
        # #     set_drag_drop_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ref_doc_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRefDocLock(boolean iLocked)
                | 
                |     Locks or unlocks the referenced documents parameter.
                |     Role:Locks or unlocks the referenced documents parameter if it is possible
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
        return self.general_session_setting_att.SetRefDocLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ref_doc_lock'
        # # vba_code = """
        # # Public Function set_ref_doc_lock(general_session_setting_att)
        # #     Dim iLocked (2)
        # #     general_session_setting_att.SetRefDocLock iLocked
        # #     set_ref_doc_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ui_style_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetUIStyleLock(boolean iLocked)
                | 
                |     Locks or unlocks the user interface style parameter.
                |     Role:Locks or unlocks the user interface style parameter if it is possible
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
        return self.general_session_setting_att.SetUIStyleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ui_style_lock'
        # # vba_code = """
        # # Public Function set_ui_style_lock(general_session_setting_att)
        # #     Dim iLocked (2)
        # #     general_session_setting_att.SetUIStyleLock iLocked
        # #     set_ui_style_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'GeneralSessionSettingAtt(name="{self.name}")'
