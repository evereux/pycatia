#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SettingController(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SettingController
                | 
                | Represents the base object for setting controllers.
                | Role: A setting controller manages all or only a part of the parameters
                | available in a property page of the dialog displayed using the Options command
                | of the Tools menu. Each setting parameter may be represented by one or several
                | setting attribute in the underlying setting repository.
                | 
                | All setting controllers share the five methods of the SettingController object
                | to deal with the whole set, or a subset of the setting
                | attributes:
                | 
                |     Commit to make a memory copy of the setting attribute
                |     values
                |     Rollback to restore the last memory copy of the setting attribute
                |     values
                |     ResetToAdminValues to restore the administered values of all the
                |     attributes
                |     ResetToAdminValuesByName to restore the administered values of a subset of
                |     the attributes
                |     SaveRepository to make a persistent copy of the setting attribute values on
                |     file.
                | 
                | In addition, each setting controller exposes four methods per setting
                | parameter: two methods to access the setting attribute values, that usually
                | make up a read/write property if the setting parameter is represented by a
                | single setting attribute, a method to manage the setting parameter lock, and a
                | method to retrieve the state of the setting parameter. The first two methods
                | are parameter-specific and are fully described in the setting controller object
                | that managing the setting parameter. The last two methods have always the same
                | signature and the same behavior whatever the setting parameter. They are
                | described below. PARAMETER is used in place of the actual setting parameter
                | name.
                | 
                |     Managing the Setting Parameter Lock
                | 
                |     HRESULT SetPARAMETERLock(in  boolean iLocked);
                | 
                |     Locks or unlocks the PARAMETER setting parameter.
                |     Role: Locking a setting parameter prevents the end user, or the
                |     administrators below the current one, from changing the setting parameter
                |     value. Locking or unlocking the PARAMETER setting parameter is an administrator
                |     task and is possible when running a session in the administration mode
                |     only.
                | 
                |     Parameters
                | 
                |         iLocked
                |             [in] A flag to indicate whether the PARAMETER setting parameter
                |             should be locked.
                |             Legal values: True to lock, and False to unlock.
                | 
                | 
                |     Retrieving the Setting Parameter State
                | 
                |     HRESULT GetPARAMETERInfo (inout CATBSTR ioAdminLevel,
                |                                     inout CATBSTR ioLocked,
                |                                     out  /*IDLRETVAL*/ boolean
                |                                     oModified);
                | 
                |     Retrieves information about the PARAMETER setting
                |     parameter.
                |     Role: This information defines the state of the setting parameter and is
                |     made up of:
                |         The administration level that sets the current value or the value used
                |         to reset it
                |         The administration level that has locked the setting
                |         parameter.
                |         A flag to indicate whether the setting parameter was
                |         modified.
                | 
                |     Parameters
                | 
                |         ioAdminLevel
                |             [inout] The administration leve that defines the value used when
                |             resetting the setting parameter.
                | 
                |             Legal values:
                |                 Default value if the setting parameter has never been
                |                 explicitly set in the administration
                |                 concatenation.
                |                 Set at Admin Level n if the setting parameter has been
                |                 administered,
                |                 where n is an integer starting from 0 representing the rank of
                |                 the administration level.
                |         ioLocked
                |             [inout] A character string to indicate whether the parameter is
                |             locked and the level of administration where the locking has been
                |             proceeded.
                |             Legal values:
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
                |     Returns
                |         True to indicate that the setting parameter value has been explicitely
                |         modified at the current administrator or user level. This is only possible with
                |         unlocked parameters. False means that it inherits the administered
                |         value.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.setting_controller = com_object

    def commit(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub Commit()
                | 
                |     Makes a memory copy of the setting attribute values.
                |     Role: Commit saves the current values of the setting attributes managed by
                |     the setting controller in a specific memory area. Successive calls to Commit
                |     overwrite the memory area. The values saved by the last call to Commit can be
                |     restored from that memory area using the Rollback method.

        :return: None
        """
        return self.setting_controller.Commit()

    def reset_to_admin_values(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub ResetToAdminValues()
                | 
                |     Restores the administrated values of the all attributes.
                |     Role: ResetToAdminValues restores all the values of the setting attributes
                |     managed by the setting controller to either the values set by the setting
                |     administrator, or to their default values if the setting administrator did not
                |     change them.

        :return: None
        """
        return self.setting_controller.ResetToAdminValues()

    def reset_to_admin_values_by_name(self, i_att_list):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub ResetToAdminValuesByName(CATSafeArrayVariant iAttList)
                | 
                |     Restores the administrated values of a subset of the
                |     attributes.
                |     Role: ResetToAdminValuesByName restores the values of a subset of the
                |     setting attributes managed by the setting controller to either the values set
                |     by the setting administrator, or to their default values if the setting
                |     administrator did not change them.
                | 
                |     Parameters:
                | 
                |         iAttList
                |             The attribute subset to which the administrated values are to be
                |             restored

        :param tuple i_att_list:
        :return: None
        """
        return self.setting_controller.ResetToAdminValuesByName(i_att_list)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'reset_to_admin_values_by_name'
        # # vba_code = """
        # # Public Function reset_to_admin_values_by_name(setting_controller)
        # #     Dim iAttList (2)
        # #     setting_controller.ResetToAdminValuesByName iAttList
        # #     reset_to_admin_values_by_name = iAttList
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def rollback(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub Rollback()
                | 
                |     Restores the last memory copy of the setting attribute
                |     values.
                |     Role: Rollback restores the values of the setting attributes managed by the
                |     setting controller from the memory area. All values of the setting attributes
                |     managed by the setting controller modified since the last call to Commit are
                |     restored to the values they had when this last Commit was called.

        :return: None
        """
        return self.setting_controller.Rollback()

    def save_repository(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SaveRepository()
                | 
                |     Makes a persistent copy of the setting attribute values on
                |     file.
                |     Role: SaveRepository saves the current values of the setting attributes
                |     managed by the setting controller in a setting repository file. To avoid
                |     inconsistencies, SaveRepository first saves the values in the memory area used
                |     by the Commit method by calling Commit before writing the values in the setting
                |     repository file.

        :return: None
        """
        return self.setting_controller.SaveRepository()

    def __repr__(self):
        return f'SettingController(name="{self.name}")'
