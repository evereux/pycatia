#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class MemoryWarningSettingAtt(SettingController):

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
                |                         MemoryWarningSettingAtt
                | 
                | Represents the base object to handle the parameters of memory warning
                | mechanism.
                | This mechanism informs the user when the process memory use exceeds a given
                | percentage of the address space usage. This mechanism warns you that because
                | the amout of remaining memory is becoming low, you should save your data and
                | leave the session.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.memory_warning_setting_att = com_object

    @property
    def activation_state(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ActivationState() As boolean
                | 
                |     Returns or sets the activation state of the memory warning
                |     mechanism.
                |     Role: Returns or sets the value of of the memory warning.

        :return: bool
        """

        return self.memory_warning_setting_att.ActivationState

    @activation_state.setter
    def activation_state(self, value):
        """
        :param bool value:
        """

        self.memory_warning_setting_att.ActivationState = value

    @property
    def memory_stopper_state(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property MemoryStopperState() As boolean
                | 
                |     Returns or sets the activation state of the memory stopper
                |     mechanism.
                |     Role: Returns or sets the value of of the memory stopper.

        :return: bool
        """

        return self.memory_warning_setting_att.MemoryStopperState

    @memory_stopper_state.setter
    def memory_stopper_state(self, value):
        """
        :param bool value:
        """

        self.memory_warning_setting_att.MemoryStopperState = value

    @property
    def usage_limit(self):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property UsageLimit() As long
                | 
                |     Returns or sets the alert percentage.
                |     Role: Returns or sets the percentage of the address space usage that can be
                |     used by the process before sending the warning.

        :return: int
        """

        return self.memory_warning_setting_att.UsageLimit

    @usage_limit.setter
    def usage_limit(self, value):
        """
        :param int value:
        """

        self.memory_warning_setting_att.UsageLimit = value

    def get_activation_state_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetActivationStateInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the memory warning
                |     mechanism.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.memory_warning_setting_att.GetActivationStateInfo(admin_level, o_locked)

    def get_memory_stopper_state_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetMemoryStopperStateInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the memory stopper
                |     mechanism.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.memory_warning_setting_att.GetMemoryStopperStateInfo(admin_level, o_locked)

    def get_usage_limit_info(self, admin_level, o_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetUsageLimitInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves environment informations for the alert
                |     percentage.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :return: None
        """
        return self.memory_warning_setting_att.GetUsageLimitInfo(admin_level, o_locked)

    def set_activation_state_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetActivationStateLock(boolean iLocked)
                | 
                |     Locks or unlocks the activation mode of the memory warning
                |     mechanism.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.memory_warning_setting_att.SetActivationStateLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_activation_state_lock'
        # # vba_code = """
        # # Public Function set_activation_state_lock(memory_warning_setting_att)
        # #     Dim iLocked (2)
        # #     memory_warning_setting_att.SetActivationStateLock iLocked
        # #     set_activation_state_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_memory_stopper_state_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetMemoryStopperStateLock(boolean iLocked)
                | 
                |     Locks or unlocks the activation mode of the memory stopper
                |     mechanism.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.memory_warning_setting_att.SetMemoryStopperStateLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_memory_stopper_state_lock'
        # # vba_code = """
        # # Public Function set_memory_stopper_state_lock(memory_warning_setting_att)
        # #     Dim iLocked (2)
        # #     memory_warning_setting_att.SetMemoryStopperStateLock iLocked
        # #     set_memory_stopper_state_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_usage_limit_lock(self, i_locked):
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub SetUsageLimitLock(boolean iLocked)
                | 
                |     Locks or unlocks the the alert percentage.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :return: None
        """
        return self.memory_warning_setting_att.SetUsageLimitLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_usage_limit_lock'
        # # vba_code = """
        # # Public Function set_usage_limit_lock(memory_warning_setting_att)
        # #     Dim iLocked (2)
        # #     memory_warning_setting_att.SetUsageLimitLock iLocked
        # #     set_usage_limit_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MemoryWarningSettingAtt(name="{ self.name }")'
