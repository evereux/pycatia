#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class SettingRepository(SettingController):
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
                |                         SettingRepository
                | 
                | Represents the base object to handle the parameters of a
                | setting
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.setting_repository = com_object

    def get_attr(self, i_attr_name):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetAttr(CATBSTR iAttrName) As CATVariant
                | 
                |     Retieves a attribute.
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             the attribute name 
                |         oAttr
                |             a CATVariant 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_attr_name:
        :return: CATVariant
        """
        return self.setting_repository.GetAttr(i_attr_name)

    def get_attr_array(self, i_attr_name):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetAttrArray(CATBSTR iAttrName) As
                | CATSafeArrayVariant
                | 
                |     Retieves a attribute of type array
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             the attribute name 
                |         oArray
                |             a CATSafeArrayVariant 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_attr_name:
        :return: tuple
        """
        return tuple(self.setting_repository.GetAttrArray(i_attr_name))

    def get_attr_info(self, i_attr_name, admin_level, locked, o_modified):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub GetAttrInfo(CATBSTR iAttrName,
                | CATBSTR AdminLevel,
                | CATBSTR Locked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the given
                |     attribute.
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
                |         iAttrName
                |             [in] the attribute name. 
                |         ioAdminLevel
                |             [inout] The administration level that defines the value used when
                |             resetting the setting parameter.
                | 
                |             Legal values:
                | 
                |                 Default value if the setting parameter has never been
                |                 explicitly set in the administration
                |                 concatenation.
                |                 Set at Admin Level n if the setting parameter has been
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
                |                 where n is an integer starting from 0. The setting parameter
                |                 can not be modified at the current level.
                |                 Locked if the setting parameter is locked by the current
                |                 administration level. Only an admistrator can get this
                |                 value.
                |                 Unlocked if the setting parameter is not
                |                 locked
                | 
                |         oModified
                |             [out] True to indicate that the setting parameter value has been
                |             explicitely modified at the current administrator or user level. This is only
                |             possible with unlocked parameters. False means that it inherits the
                |             administered value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_attr_name:
        :param str admin_level:
        :param str locked:
        :param bool o_modified:
        :return: None
        """
        return self.setting_repository.GetAttrInfo(i_attr_name, admin_level, locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_attr_info'
        # # vba_code = """
        # # Public Function get_attr_info(setting_repository)
        # #     Dim iAttrName (2)
        # #     setting_repository.GetAttrInfo iAttrName
        # #     get_attr_info = iAttrName
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_attr(self, i_attr_name, i_attr):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub PutAttr(CATBSTR iAttrName,
                | CATVariant iAttr)
                | 
                |     Sets an attribute of type array.
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             the attribute name 
                |         iArray
                |             a CATSafeArrayVariant. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_attr_name:
        :param cat_variant i_attr:
        :return: None
        """
        return self.setting_repository.PutAttr(i_attr_name, i_attr)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_attr'
        # # vba_code = """
        # # Public Function put_attr(setting_repository)
        # #     Dim iAttrName (2)
        # #     setting_repository.PutAttr iAttrName
        # #     put_attr = iAttrName
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_attr_array(self, i_attr_name, i_array):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub PutAttrArray(CATBSTR iAttrName,
                | CATSafeArrayVariant iArray)
                | 
                |     Sets an attribute of type array.
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             the attribute name 
                |         iArray
                |             a CATSafeArrayVariant. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_attr_name:
        :param tuple i_array:
        :return: None
        """
        return self.setting_repository.PutAttrArray(i_attr_name, i_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_attr_array'
        # # vba_code = """
        # # Public Function put_attr_array(setting_repository)
        # #     Dim iAttrName (2)
        # #     setting_repository.PutAttrArray iAttrName
        # #     put_attr_array = iAttrName
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_attr_lock(self, i_attr_name, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetAttrLock(CATBSTR iAttrName,
                | boolean iLocked)
                | 
                |     Locks or unlocks an attribute.
                |     Role: Locking a setting attribute prevents the end user, or the
                |     administrators below the current one, from changing the setting parameter
                |     value. Locking or unlocking the attribute setting parameter is an administrator
                |     task and is possible when running a session in the administration mode
                |     only.
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             [in] the attribute name. 
                |         iLocked
                |             [in] A flag to indicate whether the attribute setting parameter
                |             should be locked.
                |             Legal values: True to lock, and False to unlock.

        :param str i_attr_name:
        :param bool i_locked:
        :return: None
        """
        return self.setting_repository.SetAttrLock(i_attr_name, i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_attr_lock'
        # # vba_code = """
        # # Public Function set_attr_lock(setting_repository)
        # #     Dim iAttrName (2)
        # #     setting_repository.SetAttrLock iAttrName
        # #     set_attr_lock = iAttrName
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SettingRepository(name="{self.name}")'
