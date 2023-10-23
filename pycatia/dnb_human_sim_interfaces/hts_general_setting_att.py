#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class HtsGeneralSettingAtt(SettingController):

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
                |                         HtsGeneralSettingAtt

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hts_general_setting_att = com_object

    @property
    def coll_walk_clearance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CollWalkClearance() As double

        :rtype: float
        """

        return self.hts_general_setting_att.CollWalkClearance

    @coll_walk_clearance.setter
    def coll_walk_clearance(self, value: float):
        """
        :param float value:
        """

        self.hts_general_setting_att.CollWalkClearance = value

    @property
    def collision_search_intensity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CollisionSearchIntensity() As short

        :rtype: int
        """

        return self.hts_general_setting_att.CollisionSearchIntensity

    @collision_search_intensity.setter
    def collision_search_intensity(self, value: int):
        """
        :param int value:
        """

        self.hts_general_setting_att.CollisionSearchIntensity = value

    @property
    def constraints_simul(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ConstraintsSimul() As short
                | 
                |     Returns or sets the ConstraintsSimul parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_general_setting_att.ConstraintsSimul

    @constraints_simul.setter
    def constraints_simul(self, value: int):
        """
        :param int value:
        """

        self.hts_general_setting_att.ConstraintsSimul = value

    @property
    def default_walk_speed(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DefaultWalkSpeed() As double
                | 
                |     Returns or sets the DefaultWalkSpeed parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.hts_general_setting_att.DefaultWalkSpeed

    @default_walk_speed.setter
    def default_walk_speed(self, value: float):
        """
        :param float value:
        """

        self.hts_general_setting_att.DefaultWalkSpeed = value

    @property
    def side_step_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SideStepAngle() As double
                | 
                |     Returns or sets the SideStepAngle parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.hts_general_setting_att.SideStepAngle

    @side_step_angle.setter
    def side_step_angle(self, value: float):
        """
        :param float value:
        """

        self.hts_general_setting_att.SideStepAngle = value

    @property
    def sync_time_and_speed_in_simulation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SyncTimeAndSpeedInSimulation() As short
                | 
                |     Returns or sets the SyncTimeAndSpeed parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_general_setting_att.SyncTimeAndSpeedInSimulation

    @sync_time_and_speed_in_simulation.setter
    def sync_time_and_speed_in_simulation(self, value: int):
        """
        :param int value:
        """

        self.hts_general_setting_att.SyncTimeAndSpeedInSimulation = value

    @property
    def update_analysis_in_simulation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UpdateAnalysisInSimulation() As short
                | 
                |     Returns or sets the UpdateAnalysisInSimulation parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_general_setting_att.UpdateAnalysisInSimulation

    @update_analysis_in_simulation.setter
    def update_analysis_in_simulation(self, value: int):
        """
        :param int value:
        """

        self.hts_general_setting_att.UpdateAnalysisInSimulation = value

    @property
    def user_walk_speed_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UserWalkSpeedStatus() As short
                | 
                |     Returns or sets the UserWalkSpeedStatus parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.hts_general_setting_att.UserWalkSpeedStatus

    @user_walk_speed_status.setter
    def user_walk_speed_status(self, value: int):
        """
        :param int value:
        """

        self.hts_general_setting_att.UserWalkSpeedStatus = value

    @property
    def walk_forward_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WalkForwardAngle() As double
                | 
                |     Returns or sets the WalkForwardAngle parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.hts_general_setting_att.WalkForwardAngle

    @walk_forward_angle.setter
    def walk_forward_angle(self, value: float):
        """
        :param float value:
        """

        self.hts_general_setting_att.WalkForwardAngle = value

    @property
    def walk_forward_distance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property WalkForwardDistance() As double
                | 
                |     Returns or sets the WalkForwardDistance parameter.
                | 
                |     Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: float
        """

        return self.hts_general_setting_att.WalkForwardDistance

    @walk_forward_distance.setter
    def walk_forward_distance(self, value: float):
        """
        :param float value:
        """

        self.hts_general_setting_att.WalkForwardDistance = value

    def get_coll_walk_clearance_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCollWalkClearanceInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.hts_general_setting_att.GetCollWalkClearanceInfo(io_admin_level, io_locked)

    def get_collision_search_intensity_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCollisionSearchIntensityInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.hts_general_setting_att.GetCollisionSearchIntensityInfo(io_admin_level, io_locked)

    def get_constraints_simul_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetConstraintsSimulInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ConstraintsSimul
                |     parameter.
                |     Role:Retrieves the state of the ConstraintsSimul parameter in the current
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
        return self.hts_general_setting_att.GetConstraintsSimulInfo(io_admin_level, io_locked)

    def get_default_walk_speed_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDefaultWalkSpeedInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DefaultWalkSpeed
                |     parameter.
                |     Role:Retrieves the state of the DefaultWalkSpeed parameter in the current
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
        return self.hts_general_setting_att.GetDefaultWalkSpeedInfo(io_admin_level, io_locked)

    def get_side_step_angle_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSideStepAngleInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SideStepAngle
                |     parameter.
                |     Role:Retrieves the state of the SideStepAngle parameter in the current
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
        return self.hts_general_setting_att.GetSideStepAngleInfo(io_admin_level, io_locked)

    def get_sync_time_and_speed_in_simulation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSyncTimeAndSpeedInSimulationInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SyncTimeAndSpeed
                |     parameter.
                |     Role:Retrieves the state of the SyncTimeAndSpeed parameter in the current
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
        return self.hts_general_setting_att.GetSyncTimeAndSpeedInSimulationInfo(io_admin_level, io_locked)

    def get_update_analysis_in_simulation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUpdateAnalysisInSimulationInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the UpdateAnalysisInSimulation
                |     parameter.
                |     Role:Retrieves the state of the UpdateAnalysisInSimulation parameter in the
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
        return self.hts_general_setting_att.GetUpdateAnalysisInSimulationInfo(io_admin_level, io_locked)

    def get_user_walk_speed_status_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUserWalkSpeedStatusInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the UserWalkSpeedStatus
                |     parameter.
                |     Role:Retrieves the state of the UserWalkSpeedStatus parameter in the
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
        return self.hts_general_setting_att.GetUserWalkSpeedStatusInfo(io_admin_level, io_locked)

    def get_walk_forward_angle_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetWalkForwardAngleInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the WalkForwardAngle
                |     parameter.
                |     Role:Retrieves the state of the WalkForwardAngle parameter in the current
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
        return self.hts_general_setting_att.GetWalkForwardAngleInfo(io_admin_level, io_locked)

    def get_walk_forward_distance_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetWalkForwardDistanceInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the WalkForwardDistance
                |     parameter.
                |     Role:Retrieves the state of the WalkForwardDistance parameter in the
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
        return self.hts_general_setting_att.GetWalkForwardDistanceInfo(io_admin_level, io_locked)

    def set_coll_walk_clearance_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCollWalkClearanceLock(boolean iLocked)

        :param bool i_locked:
        :rtype: None
        """
        return self.hts_general_setting_att.SetCollWalkClearanceLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_coll_walk_clearance_lock'
        # # vba_code = """
        # # Public Function set_coll_walk_clearance_lock(hts_general_setting_att)
        # #     Dim iLocked (2)
        # #     hts_general_setting_att.SetCollWalkClearanceLock iLocked
        # #     set_coll_walk_clearance_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_collision_search_intensity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCollisionSearchIntensityLock(boolean iLocked)

        :param bool i_locked:
        :rtype: None
        """
        return self.hts_general_setting_att.SetCollisionSearchIntensityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_collision_search_intensity_lock'
        # # vba_code = """
        # # Public Function set_collision_search_intensity_lock(hts_general_setting_att)
        # #     Dim iLocked (2)
        # #     hts_general_setting_att.SetCollisionSearchIntensityLock iLocked
        # #     set_collision_search_intensity_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_constraints_simul_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetConstraintsSimulLock(boolean iLocked)
                | 
                |     Locks or unlocks the ConstraintsSimul parameter.
                |     Role:Locks or unlocks the ConstraintsSimul parameter if it is possible in
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
        return self.hts_general_setting_att.SetConstraintsSimulLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_constraints_simul_lock'
        # # vba_code = """
        # # Public Function set_constraints_simul_lock(hts_general_setting_att)
        # #     Dim iLocked (2)
        # #     hts_general_setting_att.SetConstraintsSimulLock iLocked
        # #     set_constraints_simul_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_walk_speed_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDefaultWalkSpeedLock(boolean iLocked)
                | 
                |     Locks or unlocks the DefaultWalkSpeed parameter.
                |     Role:Locks or unlocks the DefaultWalkSpeed parameter if it is possible in
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
        return self.hts_general_setting_att.SetDefaultWalkSpeedLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_walk_speed_lock'
        # # vba_code = """
        # # Public Function set_default_walk_speed_lock(hts_general_setting_att)
        # #     Dim iLocked (2)
        # #     hts_general_setting_att.SetDefaultWalkSpeedLock iLocked
        # #     set_default_walk_speed_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_side_step_angle_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSideStepAngleLock(boolean iLocked)
                | 
                |     Locks or unlocks the SideStepAngle parameter.
                |     Role:Locks or unlocks the SideStepAngle parameter if it is possible in the
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
        return self.hts_general_setting_att.SetSideStepAngleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_side_step_angle_lock'
        # # vba_code = """
        # # Public Function set_side_step_angle_lock(hts_general_setting_att)
        # #     Dim iLocked (2)
        # #     hts_general_setting_att.SetSideStepAngleLock iLocked
        # #     set_side_step_angle_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_sync_time_and_speed_in_simulation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSyncTimeAndSpeedInSimulationLock(boolean iLocked)
                | 
                |     Locks or unlocks the SyncTimeAndSpeed parameter.
                |     Role:Locks or unlocks the SyncTimeAndSpeed parameter if it is possible in
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
        return self.hts_general_setting_att.SetSyncTimeAndSpeedInSimulationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_sync_time_and_speed_in_simulation_lock'
        # # vba_code = """
        # # Public Function set_sync_time_and_speed_in_simulation_lock(hts_general_setting_att)
        # #     Dim iLocked (2)
        # #     hts_general_setting_att.SetSyncTimeAndSpeedInSimulationLock iLocked
        # #     set_sync_time_and_speed_in_simulation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_update_analysis_in_simulation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUpdateAnalysisInSimulationLock(boolean iLocked)
                | 
                |     Locks or unlocks the UpdateAnalysisInSimulation parameter.
                |     Role:Locks or unlocks the UpdateAnalysisInSimulation parameter if it is
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
        return self.hts_general_setting_att.SetUpdateAnalysisInSimulationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_update_analysis_in_simulation_lock'
        # # vba_code = """
        # # Public Function set_update_analysis_in_simulation_lock(hts_general_setting_att)
        # #     Dim iLocked (2)
        # #     hts_general_setting_att.SetUpdateAnalysisInSimulationLock iLocked
        # #     set_update_analysis_in_simulation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_user_walk_speed_status_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUserWalkSpeedStatusLock(boolean iLocked)
                | 
                |     Locks or unlocks the UserWalkSpeedStatus parameter.
                |     Role:Locks or unlocks the UserWalkSpeedStatus parameter if it is possible
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
        return self.hts_general_setting_att.SetUserWalkSpeedStatusLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_user_walk_speed_status_lock'
        # # vba_code = """
        # # Public Function set_user_walk_speed_status_lock(hts_general_setting_att)
        # #     Dim iLocked (2)
        # #     hts_general_setting_att.SetUserWalkSpeedStatusLock iLocked
        # #     set_user_walk_speed_status_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_walk_forward_angle_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetWalkForwardAngleLock(boolean iLocked)
                | 
                |     Locks or unlocks the WalkForwardAngle parameter.
                |     Role:Locks or unlocks the WalkForwardAngle parameter if it is possible in
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
        return self.hts_general_setting_att.SetWalkForwardAngleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_walk_forward_angle_lock'
        # # vba_code = """
        # # Public Function set_walk_forward_angle_lock(hts_general_setting_att)
        # #     Dim iLocked (2)
        # #     hts_general_setting_att.SetWalkForwardAngleLock iLocked
        # #     set_walk_forward_angle_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_walk_forward_distance_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetWalkForwardDistanceLock(boolean iLocked)
                | 
                |     Locks or unlocks the WalkForwardDistance parameter.
                |     Role:Locks or unlocks the WalkForwardDistance parameter if it is possible
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
        return self.hts_general_setting_att.SetWalkForwardDistanceLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_walk_forward_distance_lock'
        # # vba_code = """
        # # Public Function set_walk_forward_distance_lock(hts_general_setting_att)
        # #     Dim iLocked (2)
        # #     hts_general_setting_att.SetWalkForwardDistanceLock iLocked
        # #     set_walk_forward_distance_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HtsGeneralSettingAtt(name="{ self.name }")'
