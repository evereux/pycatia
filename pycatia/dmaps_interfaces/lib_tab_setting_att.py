#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class LibTabSettingAtt(SettingController):
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
                |                         LibTabSettingAtt

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.lib_tab_setting_att = com_object

    def get_id_unique_setting(self, o_is_unique: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetIDUniqueSetting(long oIsUnique)
                | 
                |     Retrieves the option which enables to check ID uniqueness amongst sibling
                |     processes
                |     Role: Retrieves the option which enables to check ID uniqueness amongst
                |     sibling processes
                | 
                |     Parameters:
                | 
                |         oIsUnique
                |             Flag indicating whether the check should be enabled or not
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int o_is_unique:
        :rtype: None
        """
        return self.lib_tab_setting_att.GetIDUniqueSetting(o_is_unique)

    def get_id_unique_setting_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetIDUniqueSettingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the 'Unique Check'
                |     parameter.
                |     Role:Retrieves the state of the 'Unique Check' parameter in the current
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
        return self.lib_tab_setting_att.GetIDUniqueSettingInfo(io_admin_level, io_locked)

    def get_list_of_library_file_path(self) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetListOfLibraryFilePath() As CATSafeArrayVariant
                | 
                |     Retrieves the List of Libraries that are used in the Process
                |     document
                |     Role: Retrieves the List of Libraries that are used in the Process
                |     document
                | 
                |     Parameters:
                | 
                |         ioPath
                |             a CATSafeArrayVariant of CATBSTR that has the list of libraries
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: tuple
        """
        return self.lib_tab_setting_att.GetListOfLibraryFilePath()

    def get_list_of_library_file_path_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetListOfLibraryFilePathInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves the information about the list of libraries path that are used in
                |     the Process document
                |     Role:Retrieves the information about the list of libraries path that are
                |     used in the Process document
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
        return self.lib_tab_setting_att.GetListOfLibraryFilePathInfo(io_admin_level, io_locked)

    def get_process_id_script(self, o_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetProcessIDScript(CATBSTR oPath)
                | 
                |     Retrieves the path of custom VB script to generate process
                |     ID
                |     Role: Retrieves the path of custom VB script to generate process
                |     ID
                | 
                |     Parameters:
                | 
                |         oPath
                |             The output path of the custom VB script 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str o_path:
        :rtype: None
        """
        return self.lib_tab_setting_att.GetProcessIDScript(o_path)

    def get_process_id_script_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetProcessIDScriptInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves the information about the custom VB script path that are used in
                |     the Process document
                |     Role:Retrieves the information about the custom VB script path that are
                |     used in the Process document
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
        return self.lib_tab_setting_att.GetProcessIDScriptInfo(io_admin_level, io_locked)

    def put_list_of_library_file_path(self, i_path: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutListOfLibraryFilePath(CATSafeArrayVariant iPath)
                | 
                |     Sets a List of Libraries that are used in the Process
                |     document
                |     Role: Sets the List of Libraries that are used in the Process
                |     document
                | 
                |     Parameters:
                | 
                |         iPath
                |             a CATSafeArrayVariant of CATBSTR that has the list of libraries.
                |
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param tuple i_path:
        :rtype: None
        """
        return self.lib_tab_setting_att.PutListOfLibraryFilePath(i_path)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_list_of_library_file_path'
        # # vba_code = """
        # # Public Function put_list_of_library_file_path(lib_tab_setting_att)
        # #     Dim iPath (2)
        # #     lib_tab_setting_att.PutListOfLibraryFilePath iPath
        # #     put_list_of_library_file_path = iPath
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_id_unique_setting(self, is_unique: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetIDUniqueSetting(long isUnique)
                | 
                |     Sets the option which enables to check ID uniqueness amongst sibling
                |     processes
                |     Role: Sets the option which enables to check ID uniqueness amongst sibling
                |     processes
                | 
                |     Parameters:
                | 
                |         isUnique
                |             Sets the option to enable uniqueness check or not 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int is_unique:
        :rtype: None
        """
        return self.lib_tab_setting_att.SetIDUniqueSetting(is_unique)

    def set_id_unique_setting_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetIDUniqueSettingLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Unique Check" parameter.
                |     Role: Locks or unlocks the 'Unique Check' parameter if the operation is
                |     allowed in the current administrated environment. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.lib_tab_setting_att.SetIDUniqueSettingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_id_unique_setting_lock'
        # # vba_code = """
        # # Public Function set_id_unique_setting_lock(lib_tab_setting_att)
        # #     Dim iLocked (2)
        # #     lib_tab_setting_att.SetIDUniqueSettingLock iLocked
        # #     set_id_unique_setting_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_list_of_library_file_path_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetListOfLibraryFilePathLock(boolean iLocked)
                | 
                |     Locks or unlocks the list of libraries to be used
                |     Role:Locks or unlocks the "list of libraries" parameter if it is possible
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
        return self.lib_tab_setting_att.SetListOfLibraryFilePathLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_list_of_library_file_path_lock'
        # # vba_code = """
        # # Public Function set_list_of_library_file_path_lock(lib_tab_setting_att)
        # #     Dim iLocked (2)
        # #     lib_tab_setting_att.SetListOfLibraryFilePathLock iLocked
        # #     set_list_of_library_file_path_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_process_id_script(self, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProcessIDScript(CATBSTR iPath)
                | 
                |     Sets the path of custom VB script to generate process ID
                |     Role: Sets the path of custom VB script to generate process
                |     ID
                | 
                |     Parameters:
                | 
                |         iPath
                |             Path of the custom VB script to be set 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_path:
        :rtype: None
        """
        return self.lib_tab_setting_att.SetProcessIDScript(i_path)

    def set_process_id_script_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProcessIDScriptLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Custom VB Script" parameter.
                |     Role: Locks or unlocks the 'Custom VB Script' parameter if the operation is
                |     allowed in the current administrated environment. In user mode this method will
                |     always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             1 : to lock the parameter.
                |             0: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.lib_tab_setting_att.SetProcessIDScriptLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_process_id_script_lock'
        # # vba_code = """
        # # Public Function set_process_id_script_lock(lib_tab_setting_att)
        # #     Dim iLocked (2)
        # #     lib_tab_setting_att.SetProcessIDScriptLock iLocked
        # #     set_process_id_script_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'LibTabSettingAtt(name="{self.name}")'
