#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class LicenseSettingAtt(SettingController):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         LicenseSettingAtt
                | 
                | Interface to handle the licensing settings.
                | Role: This interface is implemented by a component which represents the
                | controller of the static Licenses.
                | To access this property page:
                | Click the Options command in the Tools menu
                | Click General
                | Click the Licensing Property Page
                | 
                | This interface defines:
                | A method to set each License
                | A method to get the value of each License
                | A method to lock/unlock each parameter
                | A method to retrieve the information concerning each parameter
    
    """

    def __init__(self, setting_controller):
        super().__init__(setting_controller.com_object)
        self.license_setting_att = setting_controller.com_object

    @property
    def demo_mode(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property DemoMode() As boolean
                | 
                |     Retrieves or Sets the demo mode.
                |     Role: Retrieves or sets the value of the parameter describing if the demo
                |     mode is active.

        :return: bool
        """

        return self.license_setting_att.DemoMode

    @demo_mode.setter
    def demo_mode(self, value):
        """
        :param bool value:
        """

        self.license_setting_att.DemoMode = value

    @property
    def frequency(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Frequency() As float
                | 
                |     Retrieves or Sets the contact frequency.
                |     Role: Retrieves or sets the value of the parameter describing the server
                |     contact frequency in minutes. Note that a null value represents the maximum
                |     contact frequency value. For more information about the range and maximum,
                |     refers to the Infrastructure documentation.

        :return: float
        """

        return self.license_setting_att.Frequency

    @frequency.setter
    def frequency(self, value):
        """
        :param float value:
        """

        self.license_setting_att.Frequency = value

    @property
    def nodelock_alert(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property NodelockAlert() As long
                | 
                |     Retrieves or Sets the license expiry alert.
                |     Role: Retrieves or sets the value of the parameter describing the lthe
                |     license expiry alertt in days. For more information about the range and
                |     maximum, refers to the Infrastructure documentation.

        :return: int
        """

        return self.license_setting_att.NodelockAlert

    @nodelock_alert.setter
    def nodelock_alert(self, value):
        """
        :param int value:
        """

        self.license_setting_att.NodelockAlert = value

    @property
    def server_time_out(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ServerTimeOut() As float
                | 
                |     Retrieves or Sets the server time out.
                |     Role: Retrieves or sets the value of the parameter describing the licensing
                |     server time out in minutes. For more information about the range and maximum,
                |     refers to the Infrastructure documentation.

        :return: float
        """

        return self.license_setting_att.ServerTimeOut

    @server_time_out.setter
    def server_time_out(self, value):
        """
        :param float value:
        """

        self.license_setting_att.ServerTimeOut = value

    @property
    def show_license(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ShowLicense() As boolean
                | 
                |     Retrieves or Sets the show license .
                |     Role: Retrieves or sets the value of the parameter describing the complete
                |     license information. When the parameter is set, the user gets more information
                |     about the reason of the failure to request a license.

        :return: bool
        """

        return self.license_setting_att.ShowLicense

    @show_license.setter
    def show_license(self, value):
        """
        :param bool value:
        """

        self.license_setting_att.ShowLicense = value

    def get_demo_mode_info(self, io_admin_level, io_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetDemoModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the DemoMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: None
        """
        return self.license_setting_att.GetDemoModeInfo(io_admin_level, io_locked)

    def get_frequency_info(self, io_admin_level, io_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetFrequencyInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Frequency setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: None
        """
        return self.license_setting_att.GetFrequencyInfo(io_admin_level, io_locked)

    def get_granted_licenses_list(self, i_default_licenses):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetGrantedLicensesList(long iDefaultLicenses) As
                | CATSafeArrayVariant
                | 
                |     Deprecated:
                |         V5R15 CATSysLicenseSettingAtt#GetLicensesList

        :param int i_default_licenses:
        :return: tuple
        """
        return tuple(self.license_setting_att.GetGrantedLicensesList(i_default_licenses))

    def get_license(self, i_license):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLicense(CATBSTR iLicense) As CATBSTR
                | 
                |     Retrieves the value of the license.
                |     Role: Retrieves the mapping between a name of a license and the value of
                |     the license. The license does not need to be returned by GetLicensesList(). But
                |     if the license is not installed the license will be
                |     "NotRequested"
                | 
                |     Parameters:
                | 
                |         iLicense
                |             the name of the License: "PMG.prd", "_MD2.slt+", "_MD2.slt+GSD" for
                |             example.
                |             "PMG.prd" represent the license of the product
                |             PMG.
                |             "_MD2.slt+" represent the license of the solution
                |             MD2.
                |             "_MD2.slt+GSD" represent the license of the solution MD2, with the
                |             AddOn product GSD. 
                | 
                |     Returns:
                |         the value of the License:
                |         NotRequested : License is not Requested
                |         key : the name of the license, the default available license has been chosen by the user.
                |               License is Requested.
                |         License Number : a specific license number has been chosen by the user. License is Requested.

        :param str i_license:
        :return: str
        """
        return str(self.license_setting_att.GetLicense(i_license))

    def get_license_info(self, i_license, io_admin_level, io_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLicenseInfo(CATBSTR iLicense,
                | CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the License setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str i_license:
        :param str io_admin_level:
        :param str io_locked:
        :return: None
        """
        return self.license_setting_att.GetLicenseInfo(i_license, io_admin_level, io_locked)

    def get_licenses_list(self, i_default_licenses):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLicensesList(long iDefaultLicenses) As
                | CATSafeArrayVariant
                | 
                |     Retrieves the list of the requested or locked licenses.
                |     Role: Retrieves the list of the requested or locked licenses. There is no
                |     SetLicensesList() because the list is initialized using
                |     LUM.
                | 
                |     Parameters:
                | 
                |         iDefaultLicenses
                |             If iDefaultLicenses!=0 and the settings are empty, returns the
                |             default licenses, that is, the visible nodolocked licenses. If iDefaultLicenses
                |             == 0 and the settings are empty, returns the selected licenses (not yet stored,
                |             because not yet validated by OK button). 
                | 
                |     Returns:
                |         The array of Licenses.
                |         character meaning in license name:
                |         "_": internal notation for a license configuration
                |         "+": you chose "Any license" mode, example of returned value:
                |         _ME1.slt+FS1
                |         When the return value is a serial number (_ME1.slt_SerialNumber), you
                |         have chosen the "Explicit" license mode. In this case the add on product is not
                |         indicated in the license name.

        :param int i_default_licenses:
        :return: tuple
        """
        return tuple(self.license_setting_att.GetLicensesList(i_default_licenses))

    def get_licenses_list_info(self, io_admin_level, io_lock):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLicensesListInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLock) As boolean
                | 
                |     Retrieves information about the LicensesList setting
                |     parameter.
                |     Role: Retrieves information about the LicensesList setting locking state
                |     (global lock for the LicensesList). It is used to get the lock status of the
                |     List of the Licenses. If the LicensesList is locked all the licenses are
                |     locked. When the licenses are locked, it means that an administrator has locked
                |     the attribute. It does not means that an administrator has changed the value of
                |     the attribute. The value of the setting is not updatable because it refers to a
                |     lock on a list. That is why the return value is false.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel:
                |             Level of administrator. 
                |         ioLock:
                |             Locked/Unlocked. 
                | 
                |     Returns:
                |         False
                |         Information returned in the dump:
                |         Parameter 1 : "Value taken in case of reset" : useless. Default value : "Default value"
                |         Parameter 2 : "Locking state" value : unlocked / locked / locked at Admin Level n
                |         Parameter 3 : "Returned value" : useless, default value : False
                | 
                |         Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_lock:
        :return: None
        """
        return self.license_setting_att.GetLicensesListInfo(io_admin_level, io_lock)

    def get_nodelock_alert_info(self, io_admin_level, io_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetNodelockAlertInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the license expiry alert setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: None
        """
        return self.license_setting_att.GetNodelockAlertInfo(io_admin_level, io_locked)

    def get_server_time_out_info(self, io_admin_level, io_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetServerTimeOutInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the TimeOut setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: None
        """
        return self.license_setting_att.GetServerTimeOutInfo(io_admin_level, io_locked)

    def get_show_license_info(self, io_admin_level, io_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetShowLicenseInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ShowLicense setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: None
        """
        return self.license_setting_att.GetShowLicenseInfo(io_admin_level, io_locked)

    def set_demo_mode_lock(self, i_lock):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetDemoModeLock(boolean iLock)
                | 
                |     Locks or unlocks the DemoMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :return: None
        """
        return self.license_setting_att.SetDemoModeLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_demo_mode_lock'
        # # vba_code = """
        # # Public Function set_demo_mode_lock(license_setting_att)
        # #     Dim iLock (2)
        # #     license_setting_att.SetDemoModeLock iLock
        # #     set_demo_mode_lock = iLock
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_frequency_lock(self, i_lock):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetFrequencyLock(boolean iLock)
                | 
                |     Locks or unlocks the Frequency setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :return: None
        """
        return self.license_setting_att.SetFrequencyLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_frequency_lock'
        # # vba_code = """
        # # Public Function set_frequency_lock(license_setting_att)
        # #     Dim iLock (2)
        # #     license_setting_att.SetFrequencyLock iLock
        # #     set_frequency_lock = iLock
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_license(self, i_license, i_value):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetLicense(CATBSTR iLicense,
                | CATBSTR iValue)
                | 
                |     Sets the License.
                |     Role: Sets the value of the license.
                | 
                |     Parameters:
                | 
                |         iLicense
                |             the name of the License: "PMG.prd", "_MD2.slt+", "_MD2.slt+GSD" for
                |             example.
                |             "PMG.prd" represent the license of the product
                |             PMG.
                |             "_MD2.slt+" represent the license of the solution
                |             MD2.
                |             "_MD2.slt+GSD" represent the license of the solution MD2, with the
                |             AddOn product GSD. 
                |         iValue
                | 
                |             the value of the License:
                |             NotRequested : License is not Requested
                |             key : the name of the license, the default available license has been chosen by the user.
                |                   License is Requested.
                |             License Number : a specific license number has been chosen by the user.
                |                              License is Requested.

        :param str i_license:
        :param str i_value:
        :return: None
        """
        return self.license_setting_att.SetLicense(i_license, i_value)

    def set_license_lock(self, i_license, i_lock):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetLicenseLock(CATBSTR iLicense,
                | boolean iLock)
                | 
                |     Locks or unlocks the License setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str i_license:
        :param bool i_lock:
        :return: None
        """
        return self.license_setting_att.SetLicenseLock(i_license, i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_license_lock'
        # # vba_code = """
        # # Public Function set_license_lock(license_setting_att)
        # #     Dim iLicense (2)
        # #     license_setting_att.SetLicenseLock iLicense
        # #     set_license_lock = iLicense
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_licenses_list_lock(self, i_lock):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetLicensesListLock(boolean iLock)
                | 
                |     Locks or unlocks the LicensesList setting parameter.
                |     Role:Locks or unlocks the LicensesList setting parameter. Locks or unlocks
                |     the parameter describing the list of installed licenses, if the operation is
                |     allowed in the current administrated environment. It is the global lock on all
                |     the licenses. When the LicenseList is locked all the licenses are locked. When
                |     the LicenseList is unlocked all the licenses are unlocked.
                | 
                |     Parameters:
                | 
                |         iLock
                |             the locking operation to be performed:
                |             True: to lock the parameter.
                |             False: to unlock the parameter.
                |             Refer to 
                | 
                |         SettingController for a detailed description.

        :param bool i_lock:
        :return: None
        """
        return self.license_setting_att.SetLicensesListLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_licenses_list_lock'
        # # vba_code = """
        # # Public Function set_licenses_list_lock(license_setting_att)
        # #     Dim iLock (2)
        # #     license_setting_att.SetLicensesListLock iLock
        # #     set_licenses_list_lock = iLock
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_nodelock_alert_lock(self, i_lock):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetNodelockAlertLock(boolean iLock)
                | 
                |     Locks or unlocks the license expiry alert setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :return: None
        """
        return self.license_setting_att.SetNodelockAlertLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_nodelock_alert_lock'
        # # vba_code = """
        # # Public Function set_nodelock_alert_lock(license_setting_att)
        # #     Dim iLock (2)
        # #     license_setting_att.SetNodelockAlertLock iLock
        # #     set_nodelock_alert_lock = iLock
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_server_time_out_lock(self, i_lock):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetServerTimeOutLock(boolean iLock)
                | 
                |     Locks or unlocks the TimeOut setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :return: None
        """
        return self.license_setting_att.SetServerTimeOutLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_server_time_out_lock'
        # # vba_code = """
        # # Public Function set_server_time_out_lock(license_setting_att)
        # #     Dim iLock (2)
        # #     license_setting_att.SetServerTimeOutLock iLock
        # #     set_server_time_out_lock = iLock
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_show_license_lock(self, i_lock):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetShowLicenseLock(boolean iLock)
                | 
                |     Locks or unlocks the ShowLicense setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :return: None
        """
        return self.license_setting_att.SetShowLicenseLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_show_license_lock'
        # # vba_code = """
        # # Public Function set_show_license_lock(license_setting_att)
        # #     Dim iLock (2)
        # #     license_setting_att.SetShowLicenseLock iLock
        # #     set_show_license_lock = iLock
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'LicenseSettingAtt(name="{self.name}")'
