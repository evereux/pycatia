#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class SpecV4SettingAtt(SettingController):
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
                |                         SpecV4SettingAtt
                | 
                | Represents the V4/V5 SPEC setting controller object.
                | Role: The V4/V5 SPEC setting controller object deals with the setting
                | parameters displayed in the V4/V5SPEC property page. To access this property
                | page:
                | 
                |     Click the Options command in the Tools menu
                |     Click + left of General to unfold the workbench list
                |     Click Compatibility
                | 
                | 
                | The different options for V4/V5SPEC tab:
                | The Step By Step Update And Reroute
                | The Draft Feature Migration Mode
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.spec_v4_setting_att = com_object

    @property
    def draft_feature_migration_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DraftFeatureMigrationMode() As
                | CATV4IV4V5SpecDraftMigrationEnum
                | 
                |     Returns or sets the activation state of the mode of migration for draft
                |     feature.
                |     Role: This setting parameter manages the activation of the mode of
                |     migration for draft feature during a Copy/Paste As Spec.

        :return: enum catv4_iv4_v5_spec_draft_migration_enum
        :rtype: int
        """

        return self.spec_v4_setting_att.DraftFeatureMigrationMode

    @draft_feature_migration_mode.setter
    def draft_feature_migration_mode(self, value: int):
        """
        :param int value: enum catv4_iv4_v5_spec_draft_migration_enum
        """

        self.spec_v4_setting_att.DraftFeatureMigrationMode = value

    @property
    def step_by_step_update_and_reroute(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property StepByStepUpdateAndReroute() As boolean
                | 
                |     Returns or sets the activation state of Step By Step Update And
                |     Reroute.
                |     Role: The Step By Step Update And Reroute setting parameter manages the
                |     activation of the step by step update and reroute during a Copy/Paste As Spec
                |     when solids are involved.

        :rtype: bool
        """

        return self.spec_v4_setting_att.StepByStepUpdateAndReroute

    @step_by_step_update_and_reroute.setter
    def step_by_step_update_and_reroute(self, value: bool):
        """
        :param bool value:
        """

        self.spec_v4_setting_att.StepByStepUpdateAndReroute = value

    def get_draft_feature_migration_mode_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDraftFeatureMigrationModeInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the DraftFeatureMigrationMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.spec_v4_setting_att.GetDraftFeatureMigrationModeInfo(admin_level, o_locked)

    def get_step_by_step_update_and_reroute_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStepByStepUpdateAndRerouteInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the StepByStepUpdateAndReroute setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.spec_v4_setting_att.GetStepByStepUpdateAndRerouteInfo(admin_level, o_locked)

    def set_draft_feature_migration_mode_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDraftFeatureMigrationModeLock(boolean iLock)
                | 
                |     Locks or unlocks the DraftFeatureMigrationMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.spec_v4_setting_att.SetDraftFeatureMigrationModeLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_draft_feature_migration_mode_lock'
        # # vba_code = """
        # # Public Function set_draft_feature_migration_mode_lock(spec_v4_setting_att)
        # #     Dim iLock (2)
        # #     spec_v4_setting_att.SetDraftFeatureMigrationModeLock iLock
        # #     set_draft_feature_migration_mode_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_step_by_step_update_and_reroute_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStepByStepUpdateAndRerouteLock(boolean iLock)
                | 
                |     Locks or unlocks the StepByStepUpdateAndReroute setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :rtype: None
        """
        return self.spec_v4_setting_att.SetStepByStepUpdateAndRerouteLock(i_lock)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_step_by_step_update_and_reroute_lock'
        # # vba_code = """
        # # Public Function set_step_by_step_update_and_reroute_lock(spec_v4_setting_att)
        # #     Dim iLock (2)
        # #     spec_v4_setting_att.SetStepByStepUpdateAndRerouteLock iLock
        # #     set_step_by_step_update_and_reroute_lock = iLock
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SpecV4SettingAtt(name="{self.name}")'
