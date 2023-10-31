#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class HtsJointSpeedSettingsAtt(SettingController):
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
                |                         HtsJointSpeedSettingsAtt
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement DNBIAHtsJointSpeedSettingAtt are
                | ...
                | 
                | Do not use the DNBIAHtsJointSpeedSettingAtt interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hts_joint_speed_settings_att = com_object

    @property
    def all_joints_speed(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AllJointsSpeed() As CATBSTR
                | 
                |     Returns or sets the JointSpeed parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.hts_joint_speed_settings_att.AllJointsSpeed

    @all_joints_speed.setter
    def all_joints_speed(self, value: str):
        """
        :param str value:
        """

        self.hts_joint_speed_settings_att.AllJointsSpeed = value

    @property
    def rating(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Rating() As CATBSTR
                | 
                |     Returns or sets the Rating parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: str
        """

        return self.hts_joint_speed_settings_att.Rating

    @rating.setter
    def rating(self, value: str):
        """
        :param str value:
        """

        self.hts_joint_speed_settings_att.Rating = value

    def get_all_joints_speed_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAllJointsSpeedInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the JointSpeed parameter.
                |     Role:Retrieves the state of the JointSpeed parameter in the current
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
        return self.hts_joint_speed_settings_att.GetAllJointsSpeedInfo(io_admin_level, io_locked)

    def get_rating_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRatingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Rating
                |     parameter.
                |     Role:Retrieves the state of the Rating parameter in the current
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
        return self.hts_joint_speed_settings_att.GetRatingInfo(io_admin_level, io_locked)

    def set_all_joints_speed_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAllJointsSpeedLock(boolean iLocked)
                | 
                |     Locks or unlocks the JointSpeed parameter.
                |     Role:Locks or unlocks the JointSpeed parameter if it is possible in the
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
        return self.hts_joint_speed_settings_att.SetAllJointsSpeedLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_all_joints_speed_lock'
        # # vba_code = """
        # # Public Function set_all_joints_speed_lock(hts_joint_speed_settings_att)
        # #     Dim iLocked (2)
        # #     hts_joint_speed_settings_att.SetAllJointsSpeedLock iLocked
        # #     set_all_joints_speed_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rating_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRatingLock(boolean iLocked)
                | 
                |     Locks or unlocks the Rating parameter.
                |     Role:Locks or unlocks the Rating parameter if it is possible in the current
                |     administrative context. In user mode this method will always return
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
        return self.hts_joint_speed_settings_att.SetRatingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rating_lock'
        # # vba_code = """
        # # Public Function set_rating_lock(hts_joint_speed_settings_att)
        # #     Dim iLocked (2)
        # #     hts_joint_speed_settings_att.SetRatingLock iLocked
        # #     set_rating_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HtsJointSpeedSettingsAtt(name="{self.name}")'
