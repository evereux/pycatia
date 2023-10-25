#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class DraftingSettingAtt(SettingController):
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
                |                         DraftingSettingAtt
                | 
                | Manages drafting settings.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.drafting_setting_att = com_object

    @property
    def create_new_sheet_from(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CreateNewSheetFrom() As CatDrwNewSheetFrom
                | 
                |     Returns the CreateNewSheetFrom parameter.

        :return: enum cat_drw_new_sheet_from
        :rtype: int
        """

        return self.drafting_setting_att.CreateNewSheetFrom

    @create_new_sheet_from.setter
    def create_new_sheet_from(self, value: int):
        """
        :param int value: enum cat_drw_new_sheet_from
        """

        self.drafting_setting_att.CreateNewSheetFrom = value

    @property
    def display_reset_button(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property DisplayResetButton() As boolean
                | 
                |     Returns the DisplayResetButton parameter.

        :rtype: bool
        """

        return self.drafting_setting_att.DisplayResetButton

    @display_reset_button.setter
    def display_reset_button(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.DisplayResetButton = value

    @property
    def lock_user_default(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property LockUserDefault() As boolean
                | 
                |     Returns the LockUserDefault parameter.

        :rtype: bool
        """

        return self.drafting_setting_att.LockUserDefault

    @lock_user_default.setter
    def lock_user_default(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.LockUserDefault = value

    @property
    def prevent_background_access(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PreventBackgroundAccess() As boolean
                | 
                |     Returns the PreventBackgroundAccess parameter.

        :rtype: bool
        """

        return self.drafting_setting_att.PreventBackgroundAccess

    @prevent_background_access.setter
    def prevent_background_access(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.PreventBackgroundAccess = value

    @property
    def prevent_dim_driving_3d_cstr(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PreventDimDriving3DCstr() As boolean
                | 
                |     Returns the PreventDimDriving3DCstr parameter.

        :rtype: bool
        """

        return self.drafting_setting_att.PreventDimDriving3DCstr

    @prevent_dim_driving_3d_cstr.setter
    def prevent_dim_driving_3d_cstr(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.PreventDimDriving3DCstr = value

    @property
    def prevent_file_new(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PreventFileNew() As boolean
                | 
                |     Returns the PreventFileNew parameter.

        :return: bool
        """

        return self.drafting_setting_att.PreventFileNew

    @prevent_file_new.setter
    def prevent_file_new(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.PreventFileNew = value

    @property
    def prevent_gen_view_style(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PreventGenViewStyle() As boolean
                | 
                |     Returns the PreventGenViewStyle parameter.

        :rtype: bool
        """

        return self.drafting_setting_att.PreventGenViewStyle

    @prevent_gen_view_style.setter
    def prevent_gen_view_style(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.PreventGenViewStyle = value

    @property
    def prevent_set_as_default(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PreventSetAsDefault() As boolean
                | 
                |     Returns the PreventSetAsDefault parameter.

        :rtype: bool
        """

        return self.drafting_setting_att.PreventSetAsDefault

    @prevent_set_as_default.setter
    def prevent_set_as_default(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.PreventSetAsDefault = value

    @property
    def prevent_switch_standard(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PreventSwitchStandard() As boolean
                | 
                |     Returns the PreventSwitchStandard parameter.

        :rtype: bool
        """

        return self.drafting_setting_att.PreventSwitchStandard

    @prevent_switch_standard.setter
    def prevent_switch_standard(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.PreventSwitchStandard = value

    @property
    def prevent_true_dimension_creation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PreventTrueDimensionCreation() As boolean
                | 
                |     Returns the PreventTrueDimensionCreation parameter.

        :rtype: bool
        """

        return self.drafting_setting_att.PreventTrueDimensionCreation

    @prevent_true_dimension_creation.setter
    def prevent_true_dimension_creation(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.PreventTrueDimensionCreation = value

    @property
    def prevent_update_standard(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PreventUpdateStandard() As boolean
                | 
                |     Returns the PreventUpdateStandard parameter.

        :rtype: bool
        """

        return self.drafting_setting_att.PreventUpdateStandard

    @prevent_update_standard.setter
    def prevent_update_standard(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.PreventUpdateStandard = value

    @property
    def prevent_view_geom_upgrade(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property PreventViewGeomUpgrade() As boolean
                | 
                |     Returns the PreventViewGeomUpgrade parameter.

        :return: bool
        """

        return self.drafting_setting_att.PreventViewGeomUpgrade

    @prevent_view_geom_upgrade.setter
    def prevent_view_geom_upgrade(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.PreventViewGeomUpgrade = value

    @property
    def use_style_create_objects(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property UseStyleCreateObjects() As boolean
                | 
                |     Returns the UseStyleCreateObjects parameter.

        :rtype: bool
        """

        return self.drafting_setting_att.UseStyleCreateObjects

    @use_style_create_objects.setter
    def use_style_create_objects(self, value: bool):
        """
        :param bool value:
        """

        self.drafting_setting_att.UseStyleCreateObjects = value

    def get_create_new_sheet_from_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetCreateNewSheetFromInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the CreateNewSheetFrom
                |     parameter.
                |     Role:Retrieves the state of the CreateNewSheetFrom parameter in the current
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
        return self.drafting_setting_att.GetCreateNewSheetFromInfo(io_admin_level, io_locked)

    def get_display_reset_button_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetDisplayResetButtonInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DisplayResetButton
                |     parameter.
                |     Role:Retrieves the state of the DisplayResetButton parameter in the current
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
        return self.drafting_setting_att.GetDisplayResetButtonInfo(io_admin_level, io_locked)

    def get_lock_user_default_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetLockUserDefaultInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the LockUserDefault
                |     parameter.
                |     Role:Retrieves the state of the LockUserDefault parameter in the current
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
        return self.drafting_setting_att.GetLockUserDefaultInfo(io_admin_level, io_locked)

    def get_prevent_background_access_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPreventBackgroundAccessInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PreventBackgroundAccess
                |     parameter.
                |     Role:Retrieves the state of the PreventBackgroundAccess parameter in the
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
        return self.drafting_setting_att.GetPreventBackgroundAccessInfo(io_admin_level, io_locked)

    def get_prevent_dim_driving_3d_cstr_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPreventDimDriving3DCstrInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PreventDimDriving3DCstr
                |     parameter.
                |     Role:Retrieves the state of the PreventDimDriving3DCstr parameter in the
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
        return self.drafting_setting_att.GetPreventDimDriving3DCstrInfo(io_admin_level, io_locked)

    def get_prevent_file_new_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetPreventFileNewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the PreventFileNew
                |     parameter.
                |     Role:Retrieves the state of the PreventFileNew parameter in the current
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
        :param bool o_modified:
        :rtype: None
        """
        return self.drafting_setting_att.GetPreventFileNewInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_prevent_file_new_info'
        # # vba_code = """
        # # Public Function get_prevent_file_new_info(drafting_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     drafting_setting_att.GetPreventFileNewInfo ioAdminLevel
        # #     get_prevent_file_new_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_prevent_gen_view_style_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPreventGenViewStyleInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PreventGenViewStyle
                |     parameter.
                |     Role:Retrieves the state of the PreventGenViewStyle parameter in the
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
        return self.drafting_setting_att.GetPreventGenViewStyleInfo(io_admin_level, io_locked)

    def get_prevent_set_as_default_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPreventSetAsDefaultInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PreventSetAsDefault
                |     parameter.
                |     Role:Retrieves the state of the PreventSetAsDefault parameter in the
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
        return self.drafting_setting_att.GetPreventSetAsDefaultInfo(io_admin_level, io_locked)

    def get_prevent_switch_standard_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPreventSwitchStandardInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PreventSwitchStandard
                |     parameter.
                |     Role:Retrieves the state of the PreventSwitchStandard parameter in the
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
        return self.drafting_setting_att.GetPreventSwitchStandardInfo(io_admin_level, io_locked)

    def get_prevent_true_dimension_creation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPreventTrueDimensionCreationInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PreventTrueDimensionCreation
                |     parameter.
                |     Role:Retrieves the state of the PreventTrueDimensionCreation parameter in
                |     the current environment.
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
        return self.drafting_setting_att.GetPreventTrueDimensionCreationInfo(io_admin_level, io_locked)

    def get_prevent_update_standard_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPreventUpdateStandardInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PreventUpdateStandard
                |     parameter.
                |     Role:Retrieves the state of the PreventUpdateStandard parameter in the
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
        return self.drafting_setting_att.GetPreventUpdateStandardInfo(io_admin_level, io_locked)

    def get_prevent_view_geom_upgrade_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetPreventViewGeomUpgradeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PreventViewGeomUpgrade
                |     parameter.
                |     Role:Retrieves the state of the PreventViewGeomUpgrade parameter in the
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
        return self.drafting_setting_att.GetPreventViewGeomUpgradeInfo(io_admin_level, io_locked)

    def get_use_style_create_objects_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetUseStyleCreateObjectsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the UseStyleCreateObjects
                |     parameter.
                |     Role:Retrieves the state of the UseStyleCreateObjects parameter in the
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
        return self.drafting_setting_att.GetUseStyleCreateObjectsInfo(io_admin_level, io_locked)

    def set_create_new_sheet_from_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetCreateNewSheetFromLock(boolean iLocked)
                | 
                |     Locks or unlocks the CreateNewSheetFrom parameter.
                |     Role:Locks or unlocks the CreateNewSheetFrom parameter if it is possible in
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
        return self.drafting_setting_att.SetCreateNewSheetFromLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_create_new_sheet_from_lock'
        # # vba_code = """
        # # Public Function set_create_new_sheet_from_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetCreateNewSheetFromLock iLocked
        # #     set_create_new_sheet_from_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_reset_button_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetDisplayResetButtonLock(boolean iLocked)
                | 
                |     Locks or unlocks the DisplayResetButton parameter.
                |     Role:Locks or unlocks the DisplayResetButton parameter if it is possible in
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
        return self.drafting_setting_att.SetDisplayResetButtonLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_reset_button_lock'
        # # vba_code = """
        # # Public Function set_display_reset_button_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetDisplayResetButtonLock iLocked
        # #     set_display_reset_button_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_lock_user_default_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetLockUserDefaultLock(boolean iLocked)
                | 
                |     Locks or unlocks the LockUserDefault parameter.
                |     Role:Locks or unlocks the LockUserDefault parameter if it is possible in
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
        return self.drafting_setting_att.SetLockUserDefaultLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_lock_user_default_lock'
        # # vba_code = """
        # # Public Function set_lock_user_default_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetLockUserDefaultLock iLocked
        # #     set_lock_user_default_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_prevent_background_access_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPreventBackgroundAccessLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreventBackgroundAccess parameter.
                |     Role:Locks or unlocks the PreventBackgroundAccess parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.drafting_setting_att.SetPreventBackgroundAccessLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_prevent_background_access_lock'
        # # vba_code = """
        # # Public Function set_prevent_background_access_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetPreventBackgroundAccessLock iLocked
        # #     set_prevent_background_access_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_prevent_dim_driving_3d_cstr_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPreventDimDriving3DCstrLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreventDimDriving3DCstr parameter.
                |     Role:Locks or unlocks the PreventDimDriving3DCstr parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.drafting_setting_att.SetPreventDimDriving3DCstrLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_prevent_dim_driving3_d_cstr_lock'
        # # vba_code = """
        # # Public Function set_prevent_dim_driving3_d_cstr_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetPreventDimDriving3DCstrLock iLocked
        # #     set_prevent_dim_driving3_d_cstr_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_prevent_file_new_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPreventFileNewLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreventFileNew parameter.
                |     Role:Locks or unlocks the PreventFileNew parameter if it is possible in the
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
        return self.drafting_setting_att.SetPreventFileNewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_prevent_file_new_lock'
        # # vba_code = """
        # # Public Function set_prevent_file_new_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetPreventFileNewLock iLocked
        # #     set_prevent_file_new_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_prevent_gen_view_style_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPreventGenViewStyleLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreventGenViewStyle parameter.
                |     Role:Locks or unlocks the PreventGenViewStyle parameter if it is possible
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
        return self.drafting_setting_att.SetPreventGenViewStyleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_prevent_gen_view_style_lock'
        # # vba_code = """
        # # Public Function set_prevent_gen_view_style_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetPreventGenViewStyleLock iLocked
        # #     set_prevent_gen_view_style_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_prevent_set_as_default_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPreventSetAsDefaultLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreventSetAsDefault parameter.
                |     Role:Locks or unlocks the PreventSetAsDefault parameter if it is possible
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
        return self.drafting_setting_att.SetPreventSetAsDefaultLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_prevent_set_as_default_lock'
        # # vba_code = """
        # # Public Function set_prevent_set_as_default_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetPreventSetAsDefaultLock iLocked
        # #     set_prevent_set_as_default_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_prevent_switch_standard_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPreventSwitchStandardLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreventSwitchStandard parameter.
                |     Role:Locks or unlocks the PreventSwitchStandard parameter if it is possible
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
        return self.drafting_setting_att.SetPreventSwitchStandardLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_prevent_switch_standard_lock'
        # # vba_code = """
        # # Public Function set_prevent_switch_standard_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetPreventSwitchStandardLock iLocked
        # #     set_prevent_switch_standard_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_prevent_true_dimension_creation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPreventTrueDimensionCreationLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreventTrueDimensionCreation
                |     parameter.
                |     Role:Locks or unlocks the PreventTrueDimensionCreation parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
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
        return self.drafting_setting_att.SetPreventTrueDimensionCreationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_prevent_true_dimension_creation_lock'
        # # vba_code = """
        # # Public Function set_prevent_true_dimension_creation_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetPreventTrueDimensionCreationLock iLocked
        # #     set_prevent_true_dimension_creation_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_prevent_update_standard_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPreventUpdateStandardLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreventUpdateStandard parameter.
                |     Role:Locks or unlocks the PreventUpdateStandard parameter if it is possible
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
        return self.drafting_setting_att.SetPreventUpdateStandardLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_prevent_update_standard_lock'
        # # vba_code = """
        # # Public Function set_prevent_update_standard_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetPreventUpdateStandardLock iLocked
        # #     set_prevent_update_standard_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_prevent_view_geom_upgrade_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetPreventViewGeomUpgradeLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreventViewGeomUpgrade parameter.
                |     Role:Locks or unlocks the PreventViewGeomUpgrade parameter if it is
                |     possible in the current administrative context. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.drafting_setting_att.SetPreventViewGeomUpgradeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_prevent_view_geom_upgrade_lock'
        # # vba_code = """
        # # Public Function set_prevent_view_geom_upgrade_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetPreventViewGeomUpgradeLock iLocked
        # #     set_prevent_view_geom_upgrade_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_use_style_create_objects_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetUseStyleCreateObjectsLock(boolean iLocked)
                | 
                |     Locks or unlocks the UseStyleCreateObjects parameter.
                |     Role:Locks or unlocks the UseStyleCreateObjects parameter if it is possible
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
        return self.drafting_setting_att.SetUseStyleCreateObjectsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_use_style_create_objects_lock'
        # # vba_code = """
        # # Public Function set_use_style_create_objects_lock(drafting_setting_att)
        # #     Dim iLocked (2)
        # #     drafting_setting_att.SetUseStyleCreateObjectsLock iLocked
        # #     set_use_style_create_objects_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DraftingSettingAtt(name="{self.name}")'
