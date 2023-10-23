#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class VerifyTabSettingAtt(SettingController):
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
                |                         VerifTabSettingAtt

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.verify_tab_setting_att = com_object

    @property
    def all_resource_filter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AllResourceFilter() As long
                | 
                |     Returns or sets the value to signify Whether all the resources will appear
                |     during Process Navigation
                |     Role: Returns or sets the value to signify Whether all the resources will
                |     appear during Process Navigation

        :rtype: int
        """

        return self.verify_tab_setting_att.AllResourceFilter

    @all_resource_filter.setter
    def all_resource_filter(self, value: int):
        """
        :param int value:
        """

        self.verify_tab_setting_att.AllResourceFilter = value

    @property
    def auto_reframe_filter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoReframeFilter() As long
                | 
                |     Returns or sets the value to signify Whether the 'Auto Reframe' will happen
                |     during Process navigation
                |     Role: Returns or sets the value to signify Whether all the items/resources
                |     will be reframed during Process Navigation

        :rtype: int
        """

        return self.verify_tab_setting_att.AutoReframeFilter

    @auto_reframe_filter.setter
    def auto_reframe_filter(self, value: int):
        """
        :param int value:
        """

        self.verify_tab_setting_att.AutoReframeFilter = value

    @property
    def implied_resource_filter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImpliedResourceFilter() As long
                | 
                |     Returns or sets the value to signify Whether the Assigned resource will
                |     appear during Process Navigation
                |     Role: Returns or sets the value to signify Whether all the Assigned
                |     resource will appear during Process Navigation

        :rtype: int
        """

        return self.verify_tab_setting_att.ImpliedResourceFilter

    @implied_resource_filter.setter
    def implied_resource_filter(self, value: int):
        """
        :param int value:
        """

        self.verify_tab_setting_att.ImpliedResourceFilter = value

    def get_all_resource_filter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAllResourceFilterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "View All Resources"
                |     parameter.
                |     Role:Retrieves the state of the "View All Resources" parameter in the
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
        return self.verify_tab_setting_att.GetAllResourceFilterInfo(io_admin_level, io_locked)

    def get_auto_reframe_filter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAutoReframeFilterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "Auto Reframe"
                |     parameter.
                |     Role:Retrieves the state of the "Auto Reframe" parameter in the current
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
        return self.verify_tab_setting_att.GetAutoReframeFilterInfo(io_admin_level, io_locked)

    def get_implied_resource_filter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImpliedResourceFilterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "View Implied Resource"
                |     parameter.
                |     Role:Retrieves the state of the "View Implied Resource" parameter in the
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
        return self.verify_tab_setting_att.GetImpliedResourceFilterInfo(io_admin_level, io_locked)

    def set_all_resource_filter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAllResourceFilterLock(boolean iLocked)
                | 
                |     Locks or unlocks the "View All Resources" parameter.
                |     Role:Locks or unlocks the "View All Resources" parameter if it is possible
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
        return self.verify_tab_setting_att.SetAllResourceFilterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_all_resource_filter_lock'
        # # vba_code = """
        # # Public Function set_all_resource_filter_lock(verif_tab_setting_att)
        # #     Dim iLocked (2)
        # #     verif_tab_setting_att.SetAllResourceFilterLock iLocked
        # #     set_all_resource_filter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_auto_reframe_filter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAutoReframeFilterLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Auto Reframe" parameter.
                |     Role:Locks or unlocks the "Auto Reframe" parameter if it is possible in the
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
        return self.verify_tab_setting_att.SetAutoReframeFilterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_reframe_filter_lock'
        # # vba_code = """
        # # Public Function set_auto_reframe_filter_lock(verif_tab_setting_att)
        # #     Dim iLocked (2)
        # #     verif_tab_setting_att.SetAutoReframeFilterLock iLocked
        # #     set_auto_reframe_filter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_implied_resource_filter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImpliedResourceFilterLock(boolean iLocked)
                | 
                |     Locks or unlocks the Xxx parameter.
                |     Role:Locks or unlocks the "View Implied Resource" parameter if it is
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
        return self.verify_tab_setting_att.SetImpliedResourceFilterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_implied_resource_filter_lock'
        # # vba_code = """
        # # Public Function set_implied_resource_filter_lock(verif_tab_setting_att)
        # #     Dim iLocked (2)
        # #     verif_tab_setting_att.SetImpliedResourceFilterLock iLocked
        # #     set_implied_resource_filter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'VerifTabSettingAtt(name="{self.name}")'
