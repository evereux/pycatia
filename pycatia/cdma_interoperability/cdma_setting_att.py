#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.system_interfaces.setting_controller import SettingController


class CDMASettingAtt(SettingController):
    """

    Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         CDMASettingAtt
                |
                | Represents the base object to handle the parameters of the
                | cache.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cdma_setting_att = com_object

    @property
    def allow_replace_struct_exposed_during_extract_save(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property AllowReplaceStructExposedDuringExtractSave() As
                | boolean
                |     Retrieves or sets the enabling of replacing the structure exposed assembly
                |     with the blackbox resulting of extract/save.
                |     Role: Sets the enabling of replacing the structure exposed assembly with
                |     the blackbox resulting of extract/save.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.AllowReplaceStructExposedDuringExtractSave

    @allow_replace_struct_exposed_during_extract_save.setter
    def allow_replace_struct_exposed_during_extract_save(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.AllowReplaceStructExposedDuringExtractSave = value

    @property
    def ask_before_overwrite_existing_parts(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property AskBeforeOverwriteExistingParts() As boolean
                |     Retrieves or sets the enabling of asking before overwriting existing
                |     part.
                |     Role: Sets the enabling of asking before overwriting existing part.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.AskBeforeOverwriteExistingParts

    @ask_before_overwrite_existing_parts.setter
    def ask_before_overwrite_existing_parts(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.AskBeforeOverwriteExistingParts = value

    @property
    def auto_high(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property AutoHigh() As boolean
                |     Retrieves or sets the automatic highlight in PSN status.
                |     Role: Sets the automatic highlight in PSN status.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.AutoHigh

    @auto_high.setter
    def auto_high(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.AutoHigh = value

    @property
    def check_exist_in_vpm_before_fbdi(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property CheckExistInVPMBeforeFBDI() As boolean
                |     Retrieves or sets the check of existence in VPM before
                |     FBDI.
                |     Role: Sets the check of existence in VPM before FBDI.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.CheckExistInVPMBeforeFBDI

    @check_exist_in_vpm_before_fbdi.setter
    def check_exist_in_vpm_before_fbdi(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.CheckExistInVPMBeforeFBDI = value

    @property
    def disable_app_obj_mgt(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property DisableAppObjMgt() As boolean
                |     Retrieves or sets the disabling of applicative object
                |     management.
                |     Role: Retrieves or sets the value of the disabling of applicative object
                |     management.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.DisableAppObjMgt

    @disable_app_obj_mgt.setter
    def disable_app_obj_mgt(self, value: bool):
        """
        :param bool value:
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        self.cdma_setting_att.DisableAppObjMgt = value

    @property
    def disable_overwrite_reload_warn_msg(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property DisableOverwriteReloadWarnMsg() As boolean
                |     Retrieves or sets the desabling of the overwrite/reload
                |     message.
                |     Role: Sets the desabling of the overwrite/reload message.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.DisableOverwriteReloadWarnMsg

    @disable_overwrite_reload_warn_msg.setter
    def disable_overwrite_reload_warn_msg(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.DisableOverwriteReloadWarnMsg = value

    @property
    def disable_vpm_save_commit_panel(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property DisableVPMSaveCommitPanel() As boolean
                |     Retrieves or sets the disabling of VPM Save Commit Panel.
                |     Role: Sets the disabling of VPM Save Commit Panel.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.DisableVPMSaveCommitPanel

    @disable_vpm_save_commit_panel.setter
    def disable_vpm_save_commit_panel(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.DisableVPMSaveCommitPanel = value

    @property
    def disable_vpm_save_report_panel(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property DisableVPMSaveReportPanel() As boolean
                |     Retrieves or sets the disabling of VPM Save Report Panel.
                |     Role: Sets the disabling of VPM Save Report Panel.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.DisableVPMSaveReportPanel

    @disable_vpm_save_report_panel.setter
    def disable_vpm_save_report_panel(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.DisableVPMSaveReportPanel = value

    @property
    def enable_direct_v5_vault_save(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property EnableDirectV5VaultSave() As boolean
                |     Retrieves or sets the enabling of the direct V5 Vault
                |     save.
                |     Role: Sets the enabling of the direct V5 Vault save.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.EnableDirectV5VaultSave

    @enable_direct_v5_vault_save.setter
    def enable_direct_v5_vault_save(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.EnableDirectV5VaultSave = value

    @property
    def forbid_inconsistent_save(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property ForbidInconsistentSave() As boolean
                |     Retrieves or sets the enabling of forbidding inconsistent
                |     save.
                |     Role: Sets the enabling of forbidding inconsistent save.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.ForbidInconsistentSave

    @forbid_inconsistent_save.setter
    def forbid_inconsistent_save(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.ForbidInconsistentSave = value

    @property
    def gfbdi(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property GFBDI() As boolean
                |     Retrieves or sets the enabling of generic FBDI.
                |     Role: Sets the enabling of generic FBDI.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GFBDI

    @gfbdi.setter
    def gfbdi(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.GFBDI = value

    @property
    def load_all_vpm_properties(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property LoadAllVPMProperties() As boolean
                |     Retrieves or sets the Load Of All VPM Properties status.
                |     Role: Sets the Load Of All VPM Properties status.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.LoadAllVPMProperties

    @load_all_vpm_properties.setter
    def load_all_vpm_properties(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.LoadAllVPMProperties = value

    @property
    def manual_cache_cleaning(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property ManualCacheCleaning() As boolean
                |     Retrieves or sets the manual cache cleaning activation.
                |     Role: Sets the manual cache cleaning activation.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.ManualCacheCleaning

    @manual_cache_cleaning.setter
    def manual_cache_cleaning(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.ManualCacheCleaning = value

    @property
    def mapping_file(self) -> str:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property MappingFile() As CATBSTR
                |     Retrieves or sets the mapping file.
                |     Role: Sets the mapping file.

        :rtype: str
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.MappingFile

    @mapping_file.setter
    def mapping_file(self, value: str):
        """
        :param str value:
        """

        self.cdma_setting_att.MappingFile = value

    @property
    def max_percent_cache_size(self) -> int:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property MaxPercentCacheSize() As long
                |     Retrieves or sets the maximum percentage cache size before automatic cache
                |     cleaning.
                |     Role: Sets the maximum percentage cache size before automatic cache
                |     cleaning.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.MaxPercentCacheSize

    @max_percent_cache_size.setter
    def max_percent_cache_size(self, value: int):
        """
        :param int value:
        """

        self.cdma_setting_att.MaxPercentCacheSize = value

    @property
    def nb_files_for_deletion(self) -> int:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property NbFilesForDeletion() As long
                |     Retrieves or sets the number of files to delete in VPM cache during
                |     automatic cache cleaning.
                |     Role: Sets the number of files to delete in VPM cache during automatic
                |     cache cleaning.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.NbFilesForDeletion

    @nb_files_for_deletion.setter
    def nb_files_for_deletion(self, value: int):
        """
        :param int value:
        """

        self.cdma_setting_att.NbFilesForDeletion = value

    @property
    def nb_files_max(self) -> int:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property NbFilesMax() As long
                |     Retrieves or sets the maximum number of files in VPM cache before automatic
                |     cache cleaning.
                |     Role: Sets the maximum number of files in VPM cache before automatic cache
                |     cleaning.

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.NbFilesMax

    @nb_files_max.setter
    def nb_files_max(self, value: int):
        """
        :param int value:
        """

        self.cdma_setting_att.NbFilesMax = value

    @property
    def never_overwrite_existing_parts(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property NeverOverwriteExistingParts() As boolean
                |     Retrieves or sets the enabling of forbidding overwriting existing
                |     part.
                |     Role: Sets the enabling of forbidding overwriting existing part.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.NeverOverwriteExistingParts

    @never_overwrite_existing_parts.setter
    def never_overwrite_existing_parts(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.NeverOverwriteExistingParts = value

    @property
    def no_db_connection(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property NoDBConnection() As boolean
                |     Retrieves or sets the database connection desabling.
                |     Role: Sets the database connection desabling.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.NoDBConnection

    @no_db_connection.setter
    def no_db_connection(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.NoDBConnection = value

    @property
    def vpm_cache_path(self) -> str:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property VPMCachePath() As CATBSTR
                |     Retrieves or sets the VPM cache path.
                |     Role: Sets the VPM cache path.

        :rtype: str
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.VPMCachePath

    @vpm_cache_path.setter
    def vpm_cache_path(self, value: str):
        """
        :param str value:
        """

        self.cdma_setting_att.VPMCachePath = value

    @property
    def work_with_vpm_cache(self) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property WorkWithVPMCache() As boolean
                |     Returns or sets the activation of the work with VPM Cache.
                |     Role: Returns or sets the value of VPM cache activation.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.WorkWithVPMCache

    @work_with_vpm_cache.setter
    def work_with_vpm_cache(self, value: bool):
        """
        :param bool value:
        """

        self.cdma_setting_att.WorkWithVPMCache = value

    def get_allow_replace_struct_exposed_during_extract_save_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetAllowReplaceStructExposedDuringExtractSaveInfo(CATBSTR
                | AdminLevel,CATBSTR Locked) As boolean
                |     Retrieves environment informations for the enabling of forbidding
                |     overwriting existing part.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetAllowReplaceStructExposedDuringExtractSaveInfo(admin_level, locked)

    def get_ask_before_overwrite_existing_parts_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetAskBeforeOverwriteExistingPartsInfo(CATBSTR AdminLevel,CATBSTR Locked)
                | As boolean
                |     Retrieves environment informations for the enabling of asking before
                |     overwriting existing part.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetAskBeforeOverwriteExistingPartsInfo(admin_level, locked)

    def get_auto_high_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetAutoHighInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the automatic highlight in PSN
                |     status.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetAutoHighInfo(admin_level, locked)

    def get_check_exist_in_vpm_before_fbdi_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetCheckExistInVPMBeforeFBDIInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the check of existence in VPM before
                |     FBDI.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetCheckExistInVPMBeforeFBDIInfo(admin_level, locked)

    def get_disable_app_obj_mgt_info(self, admin_level: str, o_locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetDisableAppObjMgtInfo(CATBSTR AdminLevel,CATBSTR oLocked) As
                | boolean
                |     Retrieves informations about the disabling of applicative object
                |     management.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetDisableAppObjMgtInfo(admin_level, o_locked)

    def get_disable_overwrite_reload_warn_msg_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetDisableOverwriteReloadWarnMsgInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the the desabling of the
                |     overwrite/reload message.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetDisableOverwriteReloadWarnMsgInfo(admin_level, locked)

    def get_disable_vpm_save_commit_panel_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetDisableVPMSaveCommitPanelInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the disabling of VPM Save Commit
                |     Panel.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetDisableVPMSaveCommitPanelInfo(admin_level, locked)

    def get_disable_vpm_save_report_panel_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetDisableVPMSaveReportPanelInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the disabling of VPM Save Report
                |     Panel.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetDisableVPMSaveReportPanelInfo(admin_level, locked)

    def get_enable_direct_v5_vault_save_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetEnableDirectV5VaultSaveInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the enabling of the direct V5 Vault
                |     save.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetEnableDirectV5VaultSaveInfo(admin_level, locked)

    def get_forbid_inconsistent_save_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetForbidInconsistentSaveInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the enabling of forbidding
                |     inconsistent save.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetForbidInconsistentSaveInfo(admin_level, locked)

    def get_gfbdi_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetGFBDIInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the enabling of generic
                |     FBDI.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetGFBDIInfo(admin_level, locked)

    def get_load_all_vpm_properties_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetLoadAllVPMPropertiesInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the Load Of All VPM Properties
                |     status.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetLoadAllVPMPropertiesInfo(admin_level, locked)

    def get_manual_cache_cleaning_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetManualCacheCleaningInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the manual cache cleaning
                |     activation.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetManualCacheCleaningInfo(admin_level, locked)

    def get_mapping_file_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetMappingFileInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the mapping file.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetMappingFileInfo(admin_level, locked)

    def get_max_percent_cache_size_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetMaxPercentCacheSizeInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the number of files to delete in VPM
                |     cache during automatic cache cleaning.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetMaxPercentCacheSizeInfo(admin_level, locked)

    def get_nb_files_for_deletion_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetNbFilesForDeletionInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the number of files to delete in VPM
                |     cache during automatic cache cleaning.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetNbFilesForDeletionInfo(admin_level, locked)

    def get_nb_files_max_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetNbFilesMaxInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the maximum number of files in VPM
                |     cache before automatic cache cleaning.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetNbFilesMaxInfo(admin_level, locked)

    def get_never_overwrite_existing_parts_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetNeverOverwriteExistingPartsInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the enabling of forbidding
                |     overwriting existing part.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetNeverOverwriteExistingPartsInfo(admin_level, locked)

    def get_no_db_connection_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetNoDBConnectionInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the database connection
                |     desabling.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetNoDBConnectionInfo(admin_level, locked)

    def get_vpm_cache_path_info(self, admin_level: str, locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetVPMCachePathInfo(CATBSTR AdminLevel,CATBSTR Locked) As
                | boolean
                |     Retrieves environment informations for the VPM cache path.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetVPMCachePathInfo(admin_level, locked)

    def get_work_with_vpm_cache_mode_info(self, admin_level: str, o_locked: str) -> bool:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetWorkWithVPMCacheModeInfo(CATBSTR AdminLevel,CATBSTR oLocked) As
                | boolean
                |     Retrieves informations about the VPM Cache activation
                |     mode.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.GetWorkWithVPMCacheModeInfo(admin_level, o_locked)

    def set_allow_replace_struct_exposed_during_extract_save_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetAllowReplaceStructExposedDuringExtractSaveLock(boolean
                | iLocked)
                |     Locks or unlocks the enabling of forbidding overwriting existing
                |     part.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetAllowReplaceStructExposedDuringExtractSaveLock(i_locked)

    def set_ask_before_overwrite_existing_parts_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetAskBeforeOverwriteExistingPartsLock(boolean iLocked)
                |     Locks or unlocks the enabling of asking before overwriting existing
                |     part.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetAskBeforeOverwriteExistingPartsLock(i_locked)

    def set_auto_high_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetAutoHighLock(boolean iLocked)
                |     Locks or unlocks the automatic highlight in PSN status.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetAutoHighLock(i_locked)

    def set_check_exist_in_vpm_before_fbdi_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetCheckExistInVPMBeforeFBDILock(boolean iLocked)
                |     Locks or unlocks the check of existence in VPM before
                |     FBDI.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetCheckExistInVPMBeforeFBDILock(i_locked)

    def set_disable_app_obj_mgt_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetDisableAppObjMgtLock(boolean iLocked)
                |     Locks or unlocks the disabling of applicative object
                |     management.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetDisableAppObjMgtLock(i_locked)

    def set_disable_overwrite_reload_warn_msg_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetDisableOverwriteReloadWarnMsgLock(boolean iLocked)
                |     Locks or unlocks the desabling of the overwrite/reload
                |     message.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetDisableOverwriteReloadWarnMsgLock(i_locked)

    def set_disable_vpm_save_commit_panel_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetDisableVPMSaveCommitPanelLock(boolean iLocked)
                |     Locks or unlocks the disabling of VPM Save Commit Panel.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetDisableVPMSaveCommitPanelLock(i_locked)

    def set_disable_vpm_save_report_panel_panel_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetDisableVPMSaveReportPanelPanelLock(boolean iLocked)
                |     Locks or unlocks the disabling of VPM Save Report Panel.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetDisableVPMSaveReportPanelPanelLock(i_locked)

    def set_enable_direct_v5_vault_save_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetEnableDirectV5VaultSaveLock(boolean iLocked)
                |     Locks or unlocks the enabling of the direct V5 Vault save.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetEnableDirectV5VaultSaveLock(i_locked)

    def set_forbid_inconsistent_save_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetForbidInconsistentSaveLock(boolean iLocked)
                |     Locks or unlocks the enabling of forbidding inconsistent
                |     save.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetForbidInconsistentSaveLock(i_locked)

    def set_gfbdi_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetGFBDILock(boolean iLocked)
                |     Locks or unlocks the enabling of generic FBDI.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """
        return self.cdma_setting_att.SetGFBDILock(i_locked)

    def set_load_all_vpm_properties_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetLoadAllVPMPropertiesLock(boolean iLocked)
                |     Locks or unlocks the Load Of All VPM Properties status.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetLoadAllVPMPropertiesLock(i_locked)

    def set_manual_cache_cleaning_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetManualCacheCleaningLock(boolean iLocked)
                |     Locks or unlocks the manual cache cleaning activation.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetManualCacheCleaningLock(i_locked)

    def set_mapping_file_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetMappingFileLock(boolean iLocked)
                |     Locks or unlocks the mapping file.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetMappingFileLock(i_locked)

    def set_max_percent_cache_size_lock(self, i_locked: int) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetMaxPercentCacheSizeLock(long iLocked)
                |     Locks or unlocks the maximum percentage cache size before automatic cache
                |     cleaning.
                |     Refer to SettingController for a detailled description.

        :param int i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetMaxPercentCacheSizeLock(i_locked)

    def set_nb_files_for_deletion_lock(self, i_locked: int) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetNbFilesForDeletionLock(long iLocked)
                |     Locks or unlocks the number of files to delete in VPM cache during
                |     automatic cache cleaning.
                |     Refer to SettingController for a detailled description.

        :param int i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetNbFilesForDeletionLock(i_locked)

    def set_nb_files_max_lock(self, i_locked: int) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetNbFilesMaxLock(long iLocked)
                |     Locks or unlocks the maximum number of files in VPM cache before automatic
                |     cache cleaning.
                |     Refer to SettingController for a detailled description.

        :param int i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetNbFilesMaxLock(i_locked)

    def set_never_overwrite_existing_parts_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetNeverOverwriteExistingPartsLock(boolean iLocked)
                |     Locks or unlocks the enabling of forbidding overwriting existing
                |     part.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetNeverOverwriteExistingPartsLock(i_locked)

    def set_no_db_connection_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetNoDBConnectionLock(boolean iLocked)
                |     Locks or unlocks the database connection desabling.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetNoDBConnectionLock(i_locked)

    def set_vpm_cache_path_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetVPMCachePathLock(boolean iLocked)
                |     Locks or unlocks the VPM cache path.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetVPMCachePathLock(i_locked)

    def set_work_with_vpm_cache_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2020.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetWorkWithVPMCacheLock(boolean iLocked)
                |     Locks or unlocks the VPM Cache Activation mode.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            30,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.cdma_setting_att.SetWorkWithVPMCacheLock(i_locked)

    def __repr__(self):
        return f'CdmaSettingAtt(name="{self.name}")'
