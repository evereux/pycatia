#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class AssemblyGeneralSettingAtt(SettingController):
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
                |                         AsmGeneralSettingAtt
                | 
                | Represents the Assembly General setting controller object.
                | Role: the Assembly General setting controller object deals with the setting
                | parameters displayed in the Assembly General property page. To access this
                | property page:
                | 
                |     Click the Options command in the Tools menu
                |     Click + left of Mechanical Design to unfold the workbench
                |     list
                |     Click Assembly Design: General tab
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.assembly_general_setting_att = com_object

    @property
    def auto_switch_to_design_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoSwitchToDesignMode() As
                | CatAsmAutoSwitchToDesignMode
                | 
                |     Returns or sets the implicit switch from visualization mode to design mode
                |     setting parameter .
                |     Role: The implicit switch from visualization mode to design mode setting
                |     parameter manages the loading of necessayr data whenever they are needed. Note
                |     that this option is useful only when the Cache option is
                |     activated
                |     Legal values:
                |     catAutoSwitchUnavailable Automatic switch to design mode
                |     unavailable
                |     catAutoSwitchAvailable Automatic switch to design mode
                |     available
                | 
                |     Example:
                |         The following example retrieves the implicit switch setting parameter
                |         of AsmGeneralSettingAtt1 in SwitchMode and enables the
                |         switch
                | 
                |          Set SwitchMode = AsmGeneralSettingAtt1.AutoSwitchToDesignMode
                |          AsmGeneralSettingAtt1.AutoSwitchToDesignMode = catAutoSwitchAvailable

        :return: enum cat_asm_auto_switch_to_design_mode
        :rtype: int
        """

        return self.assembly_general_setting_att.AutoSwitchToDesignMode

    @auto_switch_to_design_mode.setter
    def auto_switch_to_design_mode(self, value: int):
        """
        :param int value: enum cat_asm_auto_switch_to_design_mode
        """

        self.assembly_general_setting_att.AutoSwitchToDesignMode = value

    @property
    def auto_update_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoUpdateMode() As CatAsmUpdateMode
                | 
                |     Returns or sets the automatic update setting parameter.
                |     Role: The automatic update setting parameter manages the automatic
                |     launching of the Update command.
                |     Legal values:
                |     catManualUpdate Manual update mode
                |     catAutomaticUpdate Automatic update mode
                | 
                |     Example:
                |         The following example retrieves the automatic update setting parameter
                |         of AsmGeneralSettingAtt1 in UpdateMode and sets the mode to manual
                |         update.
                | 
                |          Set UpdateMode = AsmGeneralSettingAtt1.AutoUpdateMode
                |          AsmGeneralSettingAtt1.AutoUpdateMode = catManualUpdate

        :return: enum cat_asm_update_mode
        :rtype: int
        """

        return self.assembly_general_setting_att.AutoUpdateMode

    @auto_update_mode.setter
    def auto_update_mode(self, value: int):
        """
        :param int value: enum cat_asm_update_mode
        """

        self.assembly_general_setting_att.AutoUpdateMode = value

    @property
    def move_with_fix_t_extend_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MoveWithFixTExtendMode() As CatAsmExtendMoveToFixT
                | 
                |     Returns or sets the setting parameter managing the extension of a move to
                |     the components involved in a FixTogether.
                |     Role: This setting parameter manages whether the components involved in a
                |     FixTogether will be moved or not.
                |     Legal values:
                |     catNeverExtendMoveToFixT Never extend move to all component involved in a
                |     FixTogether
                |     catAskIfExtendMoveToFixT Ask question to extend move to all component
                |     involved in a FixTogether
                |     catAlwaysExtendMoveToFixT Always extend move to all component involved in
                |     a FixTogether
                | 
                |     Example:
                |         The following example retrieves the move setting parameter of
                |         AsmGeneralSettingAtt1 in MoveMode and sets it to
                |         Always
                | 
                |          Set MoveMode = AsmGeneralSettingAtt1.MoveWithFixTExtendMode
                |          AsmGeneralSettingAtt1.MoveWithFixTExtendMode = catAlwaysExtendMoveToFixT

        :return: enum cat_asm_extend_move_to_fix_t
        :rtype: int
        """

        return self.assembly_general_setting_att.MoveWithFixTExtendMode

    @move_with_fix_t_extend_mode.setter
    def move_with_fix_t_extend_mode(self, value: int):
        """
        :param int value:
        """

        self.assembly_general_setting_att.MoveWithFixTExtendMode = value

    @property
    def update_status_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UpdateStatusMode() As
                | CatAsmUpdateStatusComputeMode
                | 
                |     Returns or sets the update status computation setting
                |     parameter.
                |     Role: The update status computation setting parameter manages the loading
                |     at open of the data necessary to the exact update status computation. Note that
                |     this option is useful only when the Cache option is
                |     activated
                |     Legal values:
                |     catManualCompute At open the update status is unknown
                |     catAutomaticCompute Additional data are being loaded at open to compute an
                |     exact Update status
                | 
                |     Example:
                |         The following example retrieves the update status computation setting
                |         parameter of AsmGeneralSettingAtt1 in StatusMode and sets the mode to automatic
                |         computation.
                | 
                |          Set StatusMode = AsmGeneralSettingAtt1.UpdateStatusMode
                |          AsmGeneralSettingAtt1.UpdateStatusMode = catAutomaticCompute

        :return: enum cat_asm_update_status_compute_mode
        :rtype: int
        """

        return self.assembly_general_setting_att.UpdateStatusMode

    @update_status_mode.setter
    def update_status_mode(self, value: int):
        """
        :param int value: enum cat_asm_update_status_compute_mode
        """

        self.assembly_general_setting_att.UpdateStatusMode = value

    def get_auto_switch_to_design_mode_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAutoSwitchToDesignModeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves the state of the implicit switch from visualization mode to
                |     design mode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.assembly_general_setting_att.GetAutoSwitchToDesignModeInfo(admin_level, o_locked)

    def get_auto_update_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAutoUpdateModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves informations about the automatic update setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.assembly_general_setting_att.GetAutoUpdateModeInfo(io_admin_level, io_locked)

    def get_move_with_fix_t_extend_mode_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMoveWithFixTExtendModeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves the state of the setting parameter managing the extension of a
                |     move to the components involved in a FixTogether.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.assembly_general_setting_att.GetMoveWithFixTExtendModeInfo(admin_level, o_locked)

    def get_update_status_mode_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUpdateStatusModeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves informations about the update status computation setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.assembly_general_setting_att.GetUpdateStatusModeInfo(admin_level, o_locked)

    def set_auto_switch_to_design_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAutoSwitchToDesignModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the implicit switch from visualization mode to design mode
                |     setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.assembly_general_setting_att.SetAutoSwitchToDesignModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_switch_to_design_mode_lock'
        # # vba_code = """
        # # Public Function set_auto_switch_to_design_mode_lock(asm_general_setting_att)
        # #     Dim iLocked (2)
        # #     asm_general_setting_att.SetAutoSwitchToDesignModeLock iLocked
        # #     set_auto_switch_to_design_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_auto_update_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAutoUpdateModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the automatic update setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.assembly_general_setting_att.SetAutoUpdateModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_update_mode_lock'
        # # vba_code = """
        # # Public Function set_auto_update_mode_lock(asm_general_setting_att)
        # #     Dim iLocked (2)
        # #     asm_general_setting_att.SetAutoUpdateModeLock iLocked
        # #     set_auto_update_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_move_with_fix_t_extend_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMoveWithFixTExtendModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the setting parameter managing the extension of a move to
                |     the components involved in a FixTogether.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.assembly_general_setting_att.SetMoveWithFixTExtendModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_move_with_fix_t_extend_mode_lock'
        # # vba_code = """
        # # Public Function set_move_with_fix_t_extend_mode_lock(asm_general_setting_att)
        # #     Dim iLocked (2)
        # #     asm_general_setting_att.SetMoveWithFixTExtendModeLock iLocked
        # #     set_move_with_fix_t_extend_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_update_status_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUpdateStatusModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the update status computation setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.assembly_general_setting_att.SetUpdateStatusModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_update_status_mode_lock'
        # # vba_code = """
        # # Public Function set_update_status_mode_lock(asm_general_setting_att)
        # #     Dim iLocked (2)
        # #     asm_general_setting_att.SetUpdateStatusModeLock iLocked
        # #     set_update_status_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AssemblyGeneralSettingAtt(name="{self.name}")'
