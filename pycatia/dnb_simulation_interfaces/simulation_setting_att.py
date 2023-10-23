#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class SimulationSettingAtt(SettingController):

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
                |                         SimulationSettingAtt
                | 
                | Interface to handle parameters of DELMIA Simulation Tools Options Tab page
                | Role: This interface is implemented by a component which represents the
                | controller of Simulation Tools Options parameter settings.
                | 
                |     Methods to set value of each parameter
                |     Methods to get value of each parameter
                |     Methods to get information on each parameter
                |     Methods to lock/unlock value of each parameter
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.simulation_setting_att = com_object

    def get_as_navigation_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetASNavigationModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ASNavigationMode
                |     parameter.
                |     Role:Retrieves the state of the ASNavigationMode parameter in the current
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
        return self.simulation_setting_att.GetASNavigationModeInfo(io_admin_level, io_locked)

    def get_as_step_size_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetASStepSizeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ASStepSize
                |     parameter.
                |     Role:Retrieves the state of the ASStepSize parameter in the current
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
        return self.simulation_setting_att.GetASStepSizeInfo(io_admin_level, io_locked)

    def get_ath_annotation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAthAnnotationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AthAnnotation
                |     parameter.
                |     Role:Retrieves the state of the AthAnnotation parameter in the current
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
        return self.simulation_setting_att.GetAthAnnotationInfo(io_admin_level, io_locked)

    def get_ath_disable_sim_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAthDisableSimInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AthDisableSim
                |     parameter.
                |     Role:Retrieves the state of the AthDisableSim parameter in the current
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
        return self.simulation_setting_att.GetAthDisableSimInfo(io_admin_level, io_locked)

    def get_ath_end_condition_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAthEndConditionInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AthEndCondition
                |     parameter.
                |     Role:Retrieves the state of the AthEndCondition parameter in the current
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
        return self.simulation_setting_att.GetAthEndConditionInfo(io_admin_level, io_locked)

    def get_ath_hyperlink_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAthHyperlinkInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AthHyperlink
                |     parameter.
                |     Role:Retrieves the state of the AthHyperlink parameter in the current
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
        return self.simulation_setting_att.GetAthHyperlinkInfo(io_admin_level, io_locked)

    def get_ath_sel_agent_dlg_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAthSelAgentDlgInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AthSelAgentDlg
                |     parameter.
                |     Role:Retrieves the state of the AthSelAgentDlg parameter in the current
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
        return self.simulation_setting_att.GetAthSelAgentDlgInfo(io_admin_level, io_locked)

    def get_ath_state_mgt_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAthStateMgtInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AthStateMgt
                |     parameter.
                |     Role:Retrieves the state of the AthStateMgt parameter in the current
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
        return self.simulation_setting_att.GetAthStateMgtInfo(io_admin_level, io_locked)

    def get_ath_text_msg_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAthTextMsgInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AthTextMsg
                |     parameter.
                |     Role:Retrieves the state of the AthTextMsg parameter in the current
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
        return self.simulation_setting_att.GetAthTextMsgInfo(io_admin_level, io_locked)

    def get_ath_viewpoint_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAthViewpointInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AthViewpoint
                |     parameter.
                |     Role:Retrieves the state of the AthViewpoint parameter in the current
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
        return self.simulation_setting_att.GetAthViewpointInfo(io_admin_level, io_locked)

    def get_ps_cycle_time_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPSCycleTimeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PSCycleTime
                |     parameter.
                |     Role:Retrieves the state of the PSCycleTime parameter in the current
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
        return self.simulation_setting_att.GetPSCycleTimeInfo(io_admin_level, io_locked)

    def get_ps_dyn_clash_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPSDynClashModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PSDynClashMode
                |     parameter.
                |     Role:Retrieves the state of the PSDynClashMode parameter in the current
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
        return self.simulation_setting_att.GetPSDynClashModeInfo(io_admin_level, io_locked)

    def get_ps_graphic_sim_step_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPSGraphicSimStepInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PSGraphicSimStep
                |     parameter.
                |     Role:Retrieves the state of the PSGraphicSimStep parameter in the current
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
        return self.simulation_setting_att.GetPSGraphicSimStepInfo(io_admin_level, io_locked)

    def get_ps_graphic_update_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPSGraphicUpdateInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PSGraphicUpdate
                |     parameter.
                |     Role:Retrieves the state of the PSGraphicUpdate parameter in the current
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
        return self.simulation_setting_att.GetPSGraphicUpdateInfo(io_admin_level, io_locked)

    def get_pv_end_condition_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPVEndConditionInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PVEndCondition
                |     parameter.
                |     Role:Retrieves the state of the PVEndCondition parameter in the current
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
        return self.simulation_setting_att.GetPVEndConditionInfo(io_admin_level, io_locked)

    def get_pv_state_mgt_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPVStateMgtInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PVStateMgt
                |     parameter.
                |     Role:Retrieves the state of the PVStateMgt parameter in the current
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
        return self.simulation_setting_att.GetPVStateMgtInfo(io_admin_level, io_locked)

    def get_run_annot_behavior_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunAnnotBehaviorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunAnnotBehavior
                |     parameter.
                |     Role:Retrieves the state of the RunAnnotBehavior parameter in the current
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
        return self.simulation_setting_att.GetRunAnnotBehaviorInfo(io_admin_level, io_locked)

    def get_run_annotation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunAnnotationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunAnnotation
                |     parameter.
                |     Role:Retrieves the state of the RunAnnotation parameter in the current
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
        return self.simulation_setting_att.GetRunAnnotationInfo(io_admin_level, io_locked)

    def get_run_end_condition_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunEndConditionInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunEndCondition
                |     parameter.
                |     Role:Retrieves the state of the RunEndCondition parameter in the current
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
        return self.simulation_setting_att.GetRunEndConditionInfo(io_admin_level, io_locked)

    def get_run_hlnk_behavior_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunHlnkBehaviorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunHlnkBehavior
                |     parameter.
                |     Role:Retrieves the state of the RunHlnkBehavior parameter in the current
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
        return self.simulation_setting_att.GetRunHlnkBehaviorInfo(io_admin_level, io_locked)

    def get_run_hyperlink_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunHyperlinkInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunHyperlink
                |     parameter.
                |     Role:Retrieves the state of the RunHyperlink parameter in the current
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
        return self.simulation_setting_att.GetRunHyperlinkInfo(io_admin_level, io_locked)

    def get_run_pause_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunPauseInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunPause
                |     parameter.
                |     Role:Retrieves the state of the RunPause parameter in the current
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
        return self.simulation_setting_att.GetRunPauseInfo(io_admin_level, io_locked)

    def get_run_state_mgt_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunStateMgtInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunStateMgt
                |     parameter.
                |     Role:Retrieves the state of the RunStateMgt parameter in the current
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
        return self.simulation_setting_att.GetRunStateMgtInfo(io_admin_level, io_locked)

    def get_run_step_size_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunStepSizeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunStepSize
                |     parameter.
                |     Role:Retrieves the state of the RunStepSize parameter in the current
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
        return self.simulation_setting_att.GetRunStepSizeInfo(io_admin_level, io_locked)

    def get_run_text_behavior_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunTextBehaviorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunTextBehavior
                |     parameter.
                |     Role:Retrieves the state of the RunTextBehavior parameter in the current
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
        return self.simulation_setting_att.GetRunTextBehaviorInfo(io_admin_level, io_locked)

    def get_run_text_msg_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunTextMsgInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunTextMsg
                |     parameter.
                |     Role:Retrieves the state of the RunTextMsg parameter in the current
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
        return self.simulation_setting_att.GetRunTextMsgInfo(io_admin_level, io_locked)

    def get_run_viewpoint_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunViewpointInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunViewpoint
                |     parameter.
                |     Role:Retrieves the state of the RunViewpoint parameter in the current
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
        return self.simulation_setting_att.GetRunViewpointInfo(io_admin_level, io_locked)

    def get_run_vis_behavior_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRunVisBehaviorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the RunVisBehavior
                |     parameter.
                |     Role:Retrieves the state of the RunVisBehavior parameter in the current
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
        return self.simulation_setting_att.GetRunVisBehaviorInfo(io_admin_level, io_locked)

    def set_as_navigation_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetASNavigationModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ASNavigationMode parameter.
                |     Role:Locks or unlocks the ASNavigationMode parameter if it is possible in
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
        return self.simulation_setting_att.SetASNavigationModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_as_navigation_mode_lock'
        # # vba_code = """
        # # Public Function set_as_navigation_mode_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetASNavigationModeLock iLocked
        # #     set_as_navigation_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_as_step_size_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetASStepSizeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ASStepSize parameter.
                |     Role:Locks or unlocks the ASStepSize parameter if it is possible in the
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
        return self.simulation_setting_att.SetASStepSizeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_as_step_size_lock'
        # # vba_code = """
        # # Public Function set_as_step_size_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetASStepSizeLock iLocked
        # #     set_as_step_size_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ath_annotation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAthAnnotationLock(boolean iLocked)
                | 
                |     Locks or unlocks the AthAnnotation parameter.
                |     Role:Locks or unlocks the AthAnnotation parameter if it is possible in the
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
        return self.simulation_setting_att.SetAthAnnotationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ath_annotation_lock'
        # # vba_code = """
        # # Public Function set_ath_annotation_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetAthAnnotationLock iLocked
        # #     set_ath_annotation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ath_disable_sim_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAthDisableSimLock(boolean iLocked)
                | 
                |     Locks or unlocks the AthDisableSim parameter.
                |     Role:Locks or unlocks the AthDisableSim parameter if it is possible in the
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
        return self.simulation_setting_att.SetAthDisableSimLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ath_disable_sim_lock'
        # # vba_code = """
        # # Public Function set_ath_disable_sim_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetAthDisableSimLock iLocked
        # #     set_ath_disable_sim_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ath_end_condition_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAthEndConditionLock(boolean iLocked)
                | 
                |     Locks or unlocks the AthEndCondition parameter.
                |     Role:Locks or unlocks the AthEndCondition parameter if it is possible in
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
        return self.simulation_setting_att.SetAthEndConditionLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ath_end_condition_lock'
        # # vba_code = """
        # # Public Function set_ath_end_condition_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetAthEndConditionLock iLocked
        # #     set_ath_end_condition_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ath_hyperlink_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAthHyperlinkLock(boolean iLocked)
                | 
                |     Locks or unlocks the AthHyperlink parameter.
                |     Role:Locks or unlocks the AthHyperlink parameter if it is possible in the
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
        return self.simulation_setting_att.SetAthHyperlinkLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ath_hyperlink_lock'
        # # vba_code = """
        # # Public Function set_ath_hyperlink_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetAthHyperlinkLock iLocked
        # #     set_ath_hyperlink_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ath_sel_agent_dlg_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAthSelAgentDlgLock(boolean iLocked)
                | 
                |     Locks or unlocks the AthSelAgentDlg parameter.
                |     Role:Locks or unlocks the AthSelAgentDlg parameter if it is possible in the
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
        return self.simulation_setting_att.SetAthSelAgentDlgLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ath_sel_agent_dlg_lock'
        # # vba_code = """
        # # Public Function set_ath_sel_agent_dlg_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetAthSelAgentDlgLock iLocked
        # #     set_ath_sel_agent_dlg_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ath_state_mgt_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAthStateMgtLock(boolean iLocked)
                | 
                |     Locks or unlocks the AthStateMgt parameter.
                |     Role:Locks or unlocks the AthStateMgt parameter if it is possible in the
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
        return self.simulation_setting_att.SetAthStateMgtLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ath_state_mgt_lock'
        # # vba_code = """
        # # Public Function set_ath_state_mgt_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetAthStateMgtLock iLocked
        # #     set_ath_state_mgt_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ath_text_msg_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAthTextMsgLock(boolean iLocked)
                | 
                |     Locks or unlocks the AthTextMsg parameter.
                |     Role:Locks or unlocks the AthTextMsg parameter if it is possible in the
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
        return self.simulation_setting_att.SetAthTextMsgLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ath_text_msg_lock'
        # # vba_code = """
        # # Public Function set_ath_text_msg_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetAthTextMsgLock iLocked
        # #     set_ath_text_msg_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ath_viewpoint_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAthViewpointLock(boolean iLocked)
                | 
                |     Locks or unlocks the AthViewpoint parameter.
                |     Role:Locks or unlocks the AthViewpoint parameter if it is possible in the
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
        return self.simulation_setting_att.SetAthViewpointLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ath_viewpoint_lock'
        # # vba_code = """
        # # Public Function set_ath_viewpoint_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetAthViewpointLock iLocked
        # #     set_ath_viewpoint_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ps_cycle_time_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPSCycleTimeLock(boolean iLocked)
                | 
                |     Locks or unlocks the PSCycleTime parameter.
                |     Role:Locks or unlocks the PSCycleTime parameter if it is possible in the
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
        return self.simulation_setting_att.SetPSCycleTimeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ps_cycle_time_lock'
        # # vba_code = """
        # # Public Function set_ps_cycle_time_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetPSCycleTimeLock iLocked
        # #     set_ps_cycle_time_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ps_dyn_clash_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPSDynClashModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the PSDynClashMode parameter.
                |     Role:Locks or unlocks the PSDynClashMode parameter if it is possible in the
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
        return self.simulation_setting_att.SetPSDynClashModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ps_dyn_clash_mode_lock'
        # # vba_code = """
        # # Public Function set_ps_dyn_clash_mode_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetPSDynClashModeLock iLocked
        # #     set_ps_dyn_clash_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ps_graphic_sim_step_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPSGraphicSimStepLock(boolean iLocked)
                | 
                |     Locks or unlocks the PSGraphicSimStep parameter.
                |     Role:Locks or unlocks the PSGraphicSimStep parameter if it is possible in
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
        return self.simulation_setting_att.SetPSGraphicSimStepLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ps_graphic_sim_step_lock'
        # # vba_code = """
        # # Public Function set_ps_graphic_sim_step_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetPSGraphicSimStepLock iLocked
        # #     set_ps_graphic_sim_step_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ps_graphic_update_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPSGraphicUpdateLock(boolean iLocked)
                | 
                |     Locks or unlocks the PSGraphicUpdate parameter.
                |     Role:Locks or unlocks the PSGraphicUpdate parameter if it is possible in
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
        return self.simulation_setting_att.SetPSGraphicUpdateLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ps_graphic_update_lock'
        # # vba_code = """
        # # Public Function set_ps_graphic_update_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetPSGraphicUpdateLock iLocked
        # #     set_ps_graphic_update_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pv_end_condition_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPVEndConditionLock(boolean iLocked)
                | 
                |     Locks or unlocks the PVEndCondition parameter.
                |     Role:Locks or unlocks the PVEndCondition parameter if it is possible in the
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
        return self.simulation_setting_att.SetPVEndConditionLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pv_end_condition_lock'
        # # vba_code = """
        # # Public Function set_pv_end_condition_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetPVEndConditionLock iLocked
        # #     set_pv_end_condition_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pv_state_mgt_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPVStateMgtLock(boolean iLocked)
                | 
                |     Locks or unlocks the PVStateMgt parameter.
                |     Role:Locks or unlocks the PVStateMgt parameter if it is possible in the
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
        return self.simulation_setting_att.SetPVStateMgtLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pv_state_mgt_lock'
        # # vba_code = """
        # # Public Function set_pv_state_mgt_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetPVStateMgtLock iLocked
        # #     set_pv_state_mgt_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_annot_behavior_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunAnnotBehaviorLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunAnnotBehavior parameter.
                |     Role:Locks or unlocks the RunAnnotBehavior parameter if it is possible in
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
        return self.simulation_setting_att.SetRunAnnotBehaviorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_annot_behavior_lock'
        # # vba_code = """
        # # Public Function set_run_annot_behavior_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunAnnotBehaviorLock iLocked
        # #     set_run_annot_behavior_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_annotation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunAnnotationLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunAnnotation parameter.
                |     Role:Locks or unlocks the RunAnnotation parameter if it is possible in the
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
        return self.simulation_setting_att.SetRunAnnotationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_annotation_lock'
        # # vba_code = """
        # # Public Function set_run_annotation_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunAnnotationLock iLocked
        # #     set_run_annotation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_end_condition_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunEndConditionLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunEndCondition parameter.
                |     Role:Locks or unlocks the RunEndCondition parameter if it is possible in
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
        return self.simulation_setting_att.SetRunEndConditionLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_end_condition_lock'
        # # vba_code = """
        # # Public Function set_run_end_condition_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunEndConditionLock iLocked
        # #     set_run_end_condition_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_hlnk_behavior_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunHlnkBehaviorLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunHlnkBehavior parameter.
                |     Role:Locks or unlocks the RunHlnkBehavior parameter if it is possible in
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
        return self.simulation_setting_att.SetRunHlnkBehaviorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_hlnk_behavior_lock'
        # # vba_code = """
        # # Public Function set_run_hlnk_behavior_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunHlnkBehaviorLock iLocked
        # #     set_run_hlnk_behavior_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_hyperlink_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunHyperlinkLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunHyperlink parameter.
                |     Role:Locks or unlocks the RunHyperlink parameter if it is possible in the
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
        return self.simulation_setting_att.SetRunHyperlinkLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_hyperlink_lock'
        # # vba_code = """
        # # Public Function set_run_hyperlink_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunHyperlinkLock iLocked
        # #     set_run_hyperlink_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_pause_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunPauseLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunPause parameter.
                |     Role:Locks or unlocks the RunPause parameter if it is possible in the
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
        return self.simulation_setting_att.SetRunPauseLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_pause_lock'
        # # vba_code = """
        # # Public Function set_run_pause_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunPauseLock iLocked
        # #     set_run_pause_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_state_mgt_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunStateMgtLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunStateMgt parameter.
                |     Role:Locks or unlocks the RunStateMgt parameter if it is possible in the
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
        return self.simulation_setting_att.SetRunStateMgtLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_state_mgt_lock'
        # # vba_code = """
        # # Public Function set_run_state_mgt_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunStateMgtLock iLocked
        # #     set_run_state_mgt_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_step_size_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunStepSizeLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunStepSize parameter.
                |     Role:Locks or unlocks the RunStepSize parameter if it is possible in the
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
        return self.simulation_setting_att.SetRunStepSizeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_step_size_lock'
        # # vba_code = """
        # # Public Function set_run_step_size_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunStepSizeLock iLocked
        # #     set_run_step_size_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_text_behavior_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunTextBehaviorLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunTextBehavior parameter.
                |     Role:Locks or unlocks the RunTextBehavior parameter if it is possible in
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
        return self.simulation_setting_att.SetRunTextBehaviorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_text_behavior_lock'
        # # vba_code = """
        # # Public Function set_run_text_behavior_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunTextBehaviorLock iLocked
        # #     set_run_text_behavior_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_text_msg_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunTextMsgLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunTextMsg parameter.
                |     Role:Locks or unlocks the RunTextMsg parameter if it is possible in the
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
        return self.simulation_setting_att.SetRunTextMsgLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_text_msg_lock'
        # # vba_code = """
        # # Public Function set_run_text_msg_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunTextMsgLock iLocked
        # #     set_run_text_msg_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_viewpoint_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunViewpointLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunViewpoint parameter.
                |     Role:Locks or unlocks the RunViewpoint parameter if it is possible in the
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
        return self.simulation_setting_att.SetRunViewpointLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_viewpoint_lock'
        # # vba_code = """
        # # Public Function set_run_viewpoint_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunViewpointLock iLocked
        # #     set_run_viewpoint_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_run_vis_behavior_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRunVisBehaviorLock(boolean iLocked)
                | 
                |     Locks or unlocks the RunVisBehavior parameter.
                |     Role:Locks or unlocks the RunVisBehavior parameter if it is possible in the
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
        return self.simulation_setting_att.SetRunVisBehaviorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_run_vis_behavior_lock'
        # # vba_code = """
        # # Public Function set_run_vis_behavior_lock(simulation_setting_att)
        # #     Dim iLocked (2)
        # #     simulation_setting_att.SetRunVisBehaviorLock iLocked
        # #     set_run_vis_behavior_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SimulationSettingAtt(name="{ self.name }")'
