#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class AnalysisPostProANRSettingAtt(SettingController):
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
                |                         AnalysisPostProANRSettingAtt
                | 
                | Interface to handle the Analysis & Simulation
                | "PostProcessingSetting".
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_post_pro_anr_setting_att = com_object

    @property
    def dmu_player_deformation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DMUPlayerDeformation() As long
                | 
                |     Returns or sets the DMUPlayerDeformation parameter.
                | 
                |     Parameters:
                | 
                |         iDMUPlayerDeformation
                |             Legal values:
                |             1 : Deformation is real
                |             2 : Deformation is amplified Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.analysis_post_pro_anr_setting_att.DMUPlayerDeformation

    @dmu_player_deformation.setter
    def dmu_player_deformation(self, value: int):
        """
        :param int value:
        """

        self.analysis_post_pro_anr_setting_att.DMUPlayerDeformation = value

    @property
    def dmu_player_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DMUPlayerMode() As long
                | 
                |     Returns or sets the DMUPlayerMode parameter.
                | 
                |     Parameters:
                | 
                |         iDMUPlayerMode
                |             Legal values:
                |             1 : Mode is One Occurrence
                |             2 : Mode is All Occurrences Ensure consistency with the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.analysis_post_pro_anr_setting_att.DMUPlayerMode

    @dmu_player_mode.setter
    def dmu_player_mode(self, value: int):
        """
        :param int value:
        """

        self.analysis_post_pro_anr_setting_att.DMUPlayerMode = value

    @property
    def dmu_player_steps_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DMUPlayerStepsNumber() As long
                | 
                |     Returns or sets the DMUPlayerStepsNumber parameter. Ensure consistency with
                |     the C++ interface to which the work is delegated.

        :rtype: int
        """

        return self.analysis_post_pro_anr_setting_att.DMUPlayerStepsNumber

    @dmu_player_steps_number.setter
    def dmu_player_steps_number(self, value: int):
        """
        :param int value:
        """

        self.analysis_post_pro_anr_setting_att.DMUPlayerStepsNumber = value

    def get_dmu_player_deformation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDMUPlayerDeformationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUPlayerDeformation
                |     parameter.
                |     Role:Retrieves the state of the DMUPlayerDeformation parameter in the
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
        return self.analysis_post_pro_anr_setting_att.GetDMUPlayerDeformationInfo(io_admin_level, io_locked)

    def get_dmu_player_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDMUPlayerModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUPlayerMode
                |     parameter.
                |     Role:Retrieves the state of the DMUPlayerMode parameter in the current
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
        return self.analysis_post_pro_anr_setting_att.GetDMUPlayerModeInfo(io_admin_level, io_locked)

    def set_dmu_player_deformation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDMUPlayerDeformationLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUPlayerDeformation parameter.
                |     Role:Locks or unlocks the DMUPlayerDeformation parameter if it is possible
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
        return self.analysis_post_pro_anr_setting_att.SetDMUPlayerDeformationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_player_deformation_lock'
        # # vba_code = """
        # # Public Function set_dmu_player_deformation_lock(analysis_post_pro_anr_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_post_pro_anr_setting_att.SetDMUPlayerDeformationLock iLocked
        # #     set_dmu_player_deformation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_player_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDMUPlayerModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUPlayerMode parameter.
                |     Role:Locks or unlocks the DMUPlayerMode parameter if it is possible in the
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
        return self.analysis_post_pro_anr_setting_att.SetDMUPlayerModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_player_mode_lock'
        # # vba_code = """
        # # Public Function set_dmu_player_mode_lock(analysis_post_pro_anr_setting_att)
        # #     Dim iLocked (2)
        # #     analysis_post_pro_anr_setting_att.SetDMUPlayerModeLock iLocked
        # #     set_dmu_player_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AnalysisPostProANRSettingAtt(name="{self.name}")'
