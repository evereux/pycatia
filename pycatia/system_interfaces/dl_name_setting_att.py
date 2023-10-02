#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class DlNameSettingAtt(SettingController):
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
                |                         DLNameSettingAtt
                | 
                | Interface to handle the DLNames.
                | Role: This interface is implemented by a component which represents the
                | controller of the DLNames.
                | This interface defines:
                | 
                |     A method to set each DLName
                |     A method to get the value of each DLName
                |     A method to lock/unlock each parameter
                |     A method to retrieve the informations concerning each
                |     parameter
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dl_name_setting_att = com_object

    @property
    def dl_name_creation_right(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property DLNameCreationRight() As boolean
                | 
                |     Returns or set the right to create new DLNames.
                |     Role: Retrieves or set the right to create new DLNames.

        :return: bool
        """

        return self.dl_name_setting_att.DLNameCreationRight

    @dl_name_creation_right.setter
    def dl_name_creation_right(self, value):
        """
        :param bool value:
        """

        self.dl_name_setting_att.DLNameCreationRight = value

    @property
    def root_dl_name_creation_right(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property RootDLNameCreationRight() As boolean
                | 
                |     Returns or set the right to create new Root DLNames.
                |     Role: Retrieves or set the right to create new Root DLNames.

        :return: bool
        """

        return self.dl_name_setting_att.RootDLNameCreationRight

    @root_dl_name_creation_right.setter
    def root_dl_name_creation_right(self, value):
        """
        :param bool value:
        """

        self.dl_name_setting_att.RootDLNameCreationRight = value

    def get_dl_name(self, i_dl_name, o_real_name_unix, o_real_name_nt, o_father):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetDLName(CATBSTR iDLName,
                | CATBSTR oRealNameUnix,
                | CATBSTR oRealNameNT,
                | CATBSTR oFather)
                | 
                |     Retrieves the mapping between a logical name and the physical
                |     path.
                |     Role: Retrieves the mapping between a logical name and the physical
                |     path.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             the logical name. 
                |         oRealNameUnix
                |             the real physical path corresponding to the logical name on Unix.
                |             
                |         oRealNameNT
                |             the real physical path corresponding to the logical name on
                |             Windows. 
                |         iFather
                |             if applicable the Name of the parent DLName 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :param str o_real_name_unix:
        :param str o_real_name_nt:
        :param str o_father:
        :return: None
        """
        return self.dl_name_setting_att.GetDLName(i_dl_name, o_real_name_unix, o_real_name_nt, o_father)

    def get_dl_name_creation_right_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetDLNameCreationRightInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves the state of the parameter DLNameCreationRight.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.dl_name_setting_att.GetDLNameCreationRightInfo(admin_level, o_locked)

    def get_dl_name_exp(self, i_dl_name, o_real_name_unix, o_real_name_nt, o_father):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetDLNameExp(CATBSTR iDLName,
                | CATBSTR oRealNameUnix,
                | CATBSTR oRealNameNT,
                | CATBSTR oFather)
                | 
                |     Retrieves the mapping between a logical name and the physical
                |     path.
                |     Role: Retrieves the mapping between a logical name and the physical path in
                |     a literal form.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             the logical name. 
                |         oRealNameUnix
                |             the real physical path corresponding to the logical name on Unix.
                |             
                |         oRealNameNT
                |             the real physical path corresponding to the logical name on
                |             Windows. 
                |         iFather
                |             if applicable the Name of the parent DLName 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :param str o_real_name_unix:
        :param str o_real_name_nt:
        :param str o_father:
        :return: None
        """
        return self.dl_name_setting_att.GetDLNameExp(i_dl_name, o_real_name_unix, o_real_name_nt, o_father)

    def get_dl_name_info(self, i_dl_name, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetDLNameInfo(CATBSTR iDLName,
                | CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves the state of the for a given DLName.
                |     Role: This information defines the state of the setting parameter and is
                |     made up of:
                | 
                |         The administration level that sets the current value or the value used
                |         to reset it
                |         The administration level that has locked the setting
                |         parameter.
                |         A flag to indicate whether the setting parameter was
                |         modified.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             a DLname. 
                |         ioAdminLevel
                |             [inout] The administration leve that defines the value used when
                |             resetting the setting parameter.
                | 
                |             Legal values:
                | 
                |                 Default value if the DLName has never been defined in the
                |                 administration concatenation.
                |                 Admin Level n if the setting parameter has been
                |                 administered,
                |                 where n is an integer starting from 0 representing the rank of
                |                 the administration level.
                | 
                |         ioLocked
                |             [inout] A character string to indicate whether the parameter is
                |             locked and the level of administration where the locking has been
                |             proceeded.
                |             Legal values:
                | 
                |                 Locked at Admin Level n if the setting parameter is locked by
                |                 then administration level n,
                |                 where n is an integer starting from 0.
                |                 Upper Locked if the setting parameter is locked by the current
                |                 administration level
                |                 Unlocked if the setting parameter is not
                |                 locked
                | 
                |     Returns:
                |         True to indicate that the DLName value has been defined at the current
                |         administrator or user level. This is only possible with unlocked DLNames. False
                |         means that the DLName is inherited from the
                |         administration.

        :param str i_dl_name:
        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.dl_name_setting_att.GetDLNameInfo(i_dl_name, admin_level, o_locked)

    def get_dl_name_list(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetDLNameList() As CATSafeArrayVariant
                | 
                |     Retrieves the list of the DLNames.
                |     Role: Retrieves the list of the defined DLNames.
                | 
                |     Parameters:
                | 
                |         oTabDLName
                |             a CATSafeArrayVariant of CATBSTR of nb elements. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: tuple
        """
        return tuple(self.dl_name_setting_att.GetDLNameList())

    def get_dl_name_sub_list(self, i_dl_name):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetDLNameSubList(CATBSTR iDLName) As
                | CATSafeArrayVariant
                | 
                |     Retrieves the list of the Sub-DLNames.
                |     Role: Retrieves the list of the DLNames created in a given
                |     DLName.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             The Father DLName. if iDLName=NULL all DLNames created at the root
                |             level are return. 
                |         oNbDLname
                |             The number of defined DLNames. 
                |         oTabDLName
                |             The array of DLNames 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_OUTOFMEMORY: on allocation failure
                |         E_FAIL: on other failures

        :param str i_dl_name:
        :return: tuple
        """
        return tuple(self.dl_name_setting_att.GetDLNameSubList(i_dl_name))

    def get_root_dl_name_creation_right_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetRootDLNameCreationRightInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves the state of the parameter
                |     RootDLNameCreationRight.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.dl_name_setting_att.GetRootDLNameCreationRightInfo(admin_level, o_locked)

    def remove_dl_name(self, i_dl_name):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemoveDLName(CATBSTR iDLName)
                | 
                |     Remove a logical name.
                |     Role: Remove a DLName in the current set if it is
                |     possible.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             the logical name. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :return: None
        """
        return self.dl_name_setting_att.RemoveDLName(i_dl_name)

    def rename_dl_name(self, i_dl_name, i_new_name):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RenameDLName(CATBSTR iDLName,
                | CATBSTR iNewName)
                | 
                |     Rename an existing DLName.
                |     Role: Rename a DLName in the current set if it is
                |     possible.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             the logical name to rename. 
                |         iNewName
                |             the new logical name. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :param str i_new_name:
        :return: None
        """
        return self.dl_name_setting_att.RenameDLName(i_dl_name, i_new_name)

    def set_dl_name(self, i_dl_name, i_real_name_unix, i_real_name_nt, i_father, i_verif_directory):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetDLName(CATBSTR iDLName,
                | CATBSTR iRealNameUnix,
                | CATBSTR iRealNameNT,
                | CATBSTR iFather,
                | boolean iVerifDirectory)
                | 
                |     Sets the mapping between a logical name and the physical
                |     path.
                |     Role: Sets the value of the cache maximum size in Mo
                | 
                |     Parameters:
                | 
                |         iDLName
                |             the logical name. 
                |         oRealNameUnix
                |             the real physical path corresponding to the logical name on Unix.
                |             
                |         oRealNameNT
                |             the real physical path corresponding to the logical name on
                |             Windows. 
                |         iFather
                |             if applicable the Name of the parent DLName 
                |         iVerifDirectory
                |             if VerifDirectory is set the existence of the directory on the
                |             current platform will be check. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :param str i_real_name_unix:
        :param str i_real_name_nt:
        :param str i_father:
        :param bool i_verif_directory:
        :return: None
        """
        return self.dl_name_setting_att.SetDLName(
            i_dl_name,
            i_real_name_unix,
            i_real_name_nt,
            i_father,
            i_verif_directory
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dl_name'
        # # vba_code = """
        # # Public Function set_dl_name(dl_name_setting_att)
        # #     Dim iDLName (2)
        # #     dl_name_setting_att.SetDLName iDLName
        # #     set_dl_name = iDLName
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dl_name_creation_right_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetDLNameCreationRightLock(boolean iLocked)
                | 
                |     Locks or unlocks the parameter DLNameCreationRight.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.dl_name_setting_att.SetDLNameCreationRightLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dl_name_creation_right_lock'
        # # vba_code = """
        # # Public Function set_dl_name_creation_right_lock(dl_name_setting_att)
        # #     Dim iLocked (2)
        # #     dl_name_setting_att.SetDLNameCreationRightLock iLocked
        # #     set_dl_name_creation_right_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dl_name_lock(self, i_dl_name, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetDLNameLock(CATBSTR iDLName,
                | boolean iLocked)
                | 
                |     Locks or unlocks the DLName.
                |     Role: Locks or unlocks the given DLName if the operation is allowed in the
                |     current administrated environment. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iDLname
                |             the DLname to be locked. 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :param bool i_locked:
        :return: None
        """
        return self.dl_name_setting_att.SetDLNameLock(i_dl_name, i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dl_name_lock'
        # # vba_code = """
        # # Public Function set_dl_name_lock(dl_name_setting_att)
        # #     Dim iDLName (2)
        # #     dl_name_setting_att.SetDLNameLock iDLName
        # #     set_dl_name_lock = iDLName
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_root_dl_name_creation_right_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetRootDLNameCreationRightLock(boolean iLocked)
                | 
                |     Locks or unlocks the parameter RootDLNameCreationRight.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.dl_name_setting_att.SetRootDLNameCreationRightLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_root_dl_name_creation_right_lock'
        # # vba_code = """
        # # Public Function set_root_dl_name_creation_right_lock(dl_name_setting_att)
        # #     Dim iLocked (2)
        # #     dl_name_setting_att.SetRootDLNameCreationRightLock iLocked
        # #     set_root_dl_name_creation_right_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DlNameSettingAtt(name="{self.name}")'
