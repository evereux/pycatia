#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class DynLicenseSettingAtt(SettingController):
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
                |                         DynLicenseSettingAtt
                | 
                | Interface to handle the dynamic licensing settings.
                | Role: This interface is implemented by a component which represents the
                | controller of the dynamic Licenses.
                | To access this property page:
                | Click the Options command in the Tools menu
                | Click General
                | Click the Shareable Products Property Page
                | 
                | This interface defines:
                | A method to lock/unlock each parameter
                | A method to retrieve the information concerning each parameter
                | Note that when a license is selected, no information is written in the
                | settings, only the lock status is written in the settings.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dyn_license_setting_att = com_object

    def get_license(self, i_license):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLicense(CATBSTR iLicense) As CATBSTR
                | 
                |     The method is not relevant for the settings.
                |     Role: The method is not relevant for the settings, because a dynamic
                |     license is only taken in account for the current session. That is why
                |     GetLicense() does not appears in the dump, even when GetLicenseInfo() appears.
                |     The output oValue will always be "".
                | 
                |     Parameters:
                | 
                |         iLicense
                |             the name of the License. 
                | 
                |     Returns:
                |         the value of the License.
                |         License ""

        :param str i_license:
        :return: str
        """
        return str(self.dyn_license_setting_att.GetLicense(i_license))

    def get_license_info(self, i_license, io_admin_level, io_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLicenseInfo(CATBSTR iLicense,
                | CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves the state of a given License.
                |     Role: Retrieves the state of a given License. It it is used to get the lock
                |     status of a specific license. When the license is locked, it means that an
                |     administrator has locked the attribute. It does not means that an administrator
                |     has changed the value of the license.
                | 
                |     Parameters:
                | 
                |         iLicense:
                |             the name of the License. 
                |         ioAdminLevel:
                |             Level of administrator. 
                |         ioLocked:
                |             Locked/Unlocked. 
                | 
                |     Returns:
                |         False.
                |         Refer to SettingController for a detailed description.
                |         Dump information:
                |         Parameter 1 : the name of the License.
                |         Parameter 2 : "Default value".
                |         Parameter 3 : locking state of the licenses Unlocked / Locked / Locked at Admin Level j.
                |         Return value : Always false, because the status of the license is not modified, only the lock
                |           status is modified.

        :param str i_license:
        :param str io_admin_level:
        :param str io_locked:
        :return: None
        """
        return self.dyn_license_setting_att.GetLicenseInfo(i_license, io_admin_level, io_locked)

    def get_licenses_list(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLicensesList() As CATSafeArrayVariant
                | 
                |     Retrieves the List of the Licenses.
                |     Role: Retrieves the list of the locked Licenses. There is no
                |     SetLicenseList() because the list is initialized using
                |     LUM.
                | 
                |     Returns:
                |         The array of Licenses.

        :return: tuple
        """
        return tuple(self.dyn_license_setting_att.GetLicensesList())

    def get_licenses_list_info(self, io_admin_level, io_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetLicensesListInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the LicensesList setting locking state (global
                |     lock for the LicensesList).
                |     Role: Retrieves information about the LicensesList setting locking state
                |     (global lock for the LicensesList) It is used to get the lock status of the
                |     List of the Licenses. If the LicenseList is locked all the licenses are locked.
                |     When the licenses are locked, it means that an administrator has locked the
                |     attribute. It does not means that an administrator has changed the value of the
                |     attribute. The value of the setting is not updatable because it refers to a
                |     lock on a list. That is why the return value is false.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel:
                |             Level of administrator. 
                |         ioLocked:
                |             Locked/Unlocked. 
                | 
                |     Returns:
                |         False.
                |         Parameter values in dump:
                |         Parameter 1 : "Value taken in case of reset" : useless. Default value: "Default value".
                |         Parameter 2 : "Locking state" value : unlocked / locked / locked at Admin Level n
                |         Parameter 3 : "Returned value" : useless, default value : False
                | 
                |         Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: None
        """
        return self.dyn_license_setting_att.GetLicensesListInfo(io_admin_level, io_locked)

    def set_license_lock(self, i_license, i_lock):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetLicenseLock(CATBSTR iLicense,
                | boolean iLock)
                | 
                |     Locks or unlocks the License setting parameter.
                |     Role: Locks or unlocks the given License if the operation is allowed in the
                |     current administrated environment.
                | 
                |     Parameters:
                | 
                |         iLicense:
                |             the name of the License. 
                |         iLock
                |             the locking operation to be performed:
                |             True: to lock the parameter.
                |             False: to unlock the parameter.
                |             Refer to 
                | 
                |         SettingController for a detailed description.

        :param str i_license:
        :param bool i_lock:
        :return: None
        """
        return self.dyn_license_setting_att.SetLicenseLock(i_license, i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_license_lock'
        # # vba_code = """
        # # Public Function set_license_lock(dyn_license_setting_att)
        # #     Dim iLicense (2)
        # #     dyn_license_setting_att.SetLicenseLock iLicense
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
                |     Role: Locks or unlocks the parameter describing the list of installed
                |     licenses, if the operation is allowed in the current administrated environment.
                |     When the LicenseList is locked all the licenses are locked. When the
                |     LicenseList is unlocked all the licenses are unlocked.
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
        return self.dyn_license_setting_att.SetLicensesListLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_licenses_list_lock'
        # # vba_code = """
        # # Public Function set_licenses_list_lock(dyn_license_setting_att)
        # #     Dim iLock (2)
        # #     dyn_license_setting_att.SetLicensesListLock iLock
        # #     set_licenses_list_lock = iLock
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DynLicenseSettingAtt(name="{self.name}")'
