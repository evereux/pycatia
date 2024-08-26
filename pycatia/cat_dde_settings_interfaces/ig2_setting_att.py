#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.system_interfaces.setting_controller import SettingController


class Ig2SettingAtt(SettingController):
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
                |                         Ig2SettingAtt
                | 
                | Interface dedicated to modify or read the current settings corresponding to the
                | IG2 Data Exchange
                | 
                | Ensure consistency with the C++ interface to which the work is
                | delegated.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.ig2_setting_att = com_object

    @property
    def export_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExportMode() As CatIg2ExportModeEnum (Read Only)
                | 
                |     Get the Export Mode option value.
                | 
                |     Parameters:
                | 
                |         oMode
                |             Legal values: An available value of the enum CatIg2ExportModeEnum.
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_ig2_export_mode_enum
        :rtype: int
        """

        return self.ig2_setting_att.ExportMode

    @property
    def export_sheets(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExportSheets() As CatIg2ExportSheetsEnum (Read
                | Only)
                | 
                |     Get the Exported Sheets option value.
                | 
                |     Parameters:
                | 
                |         oSheets
                |             Legal values: An available value of the enum
                |             CatIg2ExportSheetsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: int
        """

        return self.ig2_setting_att.ExportSheets

    @property
    def export_view_as_viewport(self) -> bool:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property ExportViewAsViewport() As boolean (Read Only)
                |     Get the value of the Export Views as Viewports option. That value is only
                |     taken into account when the export mode is set to
                |     Semantic.
                |
                |     Parameters:
                |
                |         oViewsAsViewports
                |             Legal values:
                |             TRUE : Export Views as Viewports enable.
                |             FALSE : Export Views as Viewports disable.
                |
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.ig2_setting_att.ExportViewAsViewport

    @property
    def import_destination_view(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportDestinationView() As CatIg2ImportDestinationViewEnum (Read
                | Only)
                | 
                |     Get the destination view.
                | 
                |     Parameters:
                | 
                |         oDestinationView
                |             Legal values: An available value of the enum
                |             CatIg2ImportDestinationViewEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_ig2_import_destination_view_enum
        :rtype: int
        """

        return self.ig2_setting_att.ImportDestinationView

    @property
    def import_dft_standard(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportDftStandard() As CATBSTR (Read Only)
                | 
                |     Get the name of the Drafting standard, which define the standard of the
                |     resulting CATDrawing file.
                | 
                |     Parameters:
                | 
                |         oDftStandard
                |             the CATBSTR corresponding to the Drafting standard.
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: str
        """

        return self.ig2_setting_att.ImportDftStandard

    @property
    def import_dimensions(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportDimensions() As CatIg2ImportDimensionsEnum (Read
                | Only)
                | 
                |     Get the Import dimensions option value.
                | 
                |     Parameters:
                | 
                |         oDimensions
                |             Legal values: An available value of the enum
                |             CatIg2ImportDimensionsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_ig2_import_dimensions_enum
        :rtype: int
        """

        return self.ig2_setting_att.ImportDimensions

    @property
    def import_end_points(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportEndPoints() As CatIg2ImportCreateEndPointsEnum (Read
                | Only)
                | 
                |     Get the Create End Points option value.
                | 
                |     Parameters:
                | 
                |         oEndPoints
                |             Legal values: An available value of the enum
                |             CatIg2ImportCreateEndPointsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_ig2_import_create_end_points_enum
        :rtype: int
        """

        return self.ig2_setting_att.ImportEndPoints

    @property
    def import_unit(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportUnit() As CatIg2ImportUnitEnum (Read Only)
                | 
                |     Get the import unit.
                | 
                |     Parameters:
                | 
                |         oUnit
                |             Legal values: An available value of the enum CatIg2ImportUnitEnum.
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_ig2_import_unit_enum
        :rtype: int
        """

        return self.ig2_setting_att.ImportUnit

    def get_export_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExportModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Export Mode
                |     option.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the option is locked, AdminLevel gives the administration level
                |             that imposes the value of the option.
                |             If the option is not locked, AdminLevel gives the administration
                |             level that will give the value of the option after a reset.
                |             
                |         ioLocked
                |             Indicates if the option has been locked. 
                |         oModified
                |             Indicates if the option has been explicitly modified or remain to
                |             the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.ig2_setting_att.GetExportModeInfo(io_admin_level, io_locked)

    def get_export_sheets_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExportSheetsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Exported Sheets
                |     option.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the option is locked, AdminLevel gives the administration level
                |             that imposes the value of the option.
                |             If the option is not locked, AdminLevel gives the administration
                |             level that will give the value of the option after a reset.
                |             
                |         ioLocked
                |             Indicates if the option has been locked. 
                |         oModified
                |             Indicates if the option has been explicitly modified or remain to
                |             the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.ig2_setting_att.GetExportSheetsInfo(io_admin_level, io_locked)

    def get_export_view_as_viewport_info(self, io_admin_level: str, io_locked: str) -> bool:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetExportViewAsViewportInfo(CATBSTR ioAdminLevel,CATBSTR ioLocked) As
                | boolean
                |     Retrieves environment informations for the Export Views as Viewports
                |     option.
                |
                |     Parameters:
                |
                |         ioAdminLevel
                |
                |             If the option is locked, AdminLevel gives the administration level
                |             that imposes the value of the option.
                |             If the option is not locked, AdminLevel gives the administration
                |             level that will give the value of the option after a reset.
                |
                |         ioLocked
                |             Indicates if the option has been locked.
                |         oModified
                |             Indicates if the option has been explicitly modified or remain to
                |             the administrated value.
                |
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.ig2_setting_att.GetExportViewAsViewportInfo(io_admin_level, io_locked)

    def get_import_destination_view_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportDestinationViewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the destination view
                |     option.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the option is locked, AdminLevel gives the administration level
                |             that imposes the value of the option.
                |             If the option is not locked, AdminLevel gives the administration
                |             level that will give the value of the option after a reset.
                |             
                |         ioLocked
                |             Indicates if the option has been locked. 
                |         oModified
                |             Indicates if the option has been explicitly modified or remain to
                |             the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.ig2_setting_att.GetImportDestinationViewInfo(io_admin_level, io_locked)

    def get_import_dft_standard_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportDftStandardInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Drafting standard
                |     option.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the option is locked, AdminLevel gives the administration level
                |             that imposes the value of the option.
                |             If the option is not locked, AdminLevel gives the administration
                |             level that will give the value of the option after a reset.
                |             
                |         ioLocked
                |             Indicates if the option has been locked. 
                |         oModified
                |             Indicates if the option has been explicitly modified or remain to
                |             the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.ig2_setting_att.GetImportDftStandardInfo(io_admin_level, io_locked)

    def get_import_dimensions_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportDimensionsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Import dimensions
                |     option.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the option is locked, AdminLevel gives the administration level
                |             that imposes the value of the option.
                |             If the option is not locked, AdminLevel gives the administration
                |             level that will give the value of the option after a reset.
                |             
                |         ioLocked
                |             Indicates if the option has been locked. 
                |         oModified
                |             Indicates if the option has been explicitly modified or remain to
                |             the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.ig2_setting_att.GetImportDimensionsInfo(io_admin_level, io_locked)

    def get_import_end_points_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportEndPointsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Create End Points
                |     option.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the option is locked, AdminLevel gives the administration level
                |             that imposes the value of the option.
                |             If the option is not locked, AdminLevel gives the administration
                |             level that will give the value of the option after a reset.
                |             
                |         ioLocked
                |             Indicates if the option has been locked. 
                |         oModified
                |             Indicates if the option has been explicitly modified or remain to
                |             the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.ig2_setting_att.GetImportEndPointsInfo(io_admin_level, io_locked)

    def get_import_unit_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportUnitInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the import unit
                |     option.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the option is locked, AdminLevel gives the administration level
                |             that imposes the value of the option.
                |             If the option is not locked, AdminLevel gives the administration
                |             level that will give the value of the option after a reset.
                |             
                |         ioLocked
                |             Indicates if the option has been locked. 
                |         oModified
                |             Indicates if the option has been explicitly modified or remain to
                |             the administrated value. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.ig2_setting_att.GetImportUnitInfo(io_admin_level, io_locked)

    def set_export_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExportModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Export Mode option if the operation is allowed in the
                |     current administrated environment. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE: to lock the option.
                |             FALSE: to unlock the option. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.ig2_setting_att.SetExportModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_mode_lock'
        # # vba_code = """
        # # Public Function set_export_mode_lock(ig2_setting_att)
        # #     Dim iLocked (2)
        # #     ig2_setting_att.SetExportModeLock iLocked
        # #     set_export_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_sheets_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExportSheetsLock(boolean iLocked)
                | 
                |     Locks or unlocks the Exported Sheets option if the operation is allowed in
                |     the current administrated environment. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE: to lock the option.
                |             FALSE: to unlock the option. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.ig2_setting_att.SetExportSheetsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_sheets_lock'
        # # vba_code = """
        # # Public Function set_export_sheets_lock(ig2_setting_att)
        # #     Dim iLocked (2)
        # #     ig2_setting_att.SetExportSheetsLock iLocked
        # #     set_export_sheets_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_view_as_viewport_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetExportViewAsViewportLock(boolean iLocked)
                |     Locks or unlocks the Export Views as Viewports option if the operation is
                |     allowed in the current administrated environment. In user mode this method will
                |     always return E_FAIL.
                |
                |     Parameters:
                |
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE: to lock the option.
                |             FALSE: to unlock the option.
                |
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.ig2_setting_att.SetExportViewAsViewportLock(i_locked)

    def set_import_destination_view_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportDestinationViewLock(boolean iLocked)
                | 
                |     Locks or unlocks the import destination view if the operation is allowed in
                |     the current administrated environment. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE: to lock the option.
                |             FALSE: to unlock the option. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.ig2_setting_att.SetImportDestinationViewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_destination_view_lock'
        # # vba_code = """
        # # Public Function set_import_destination_view_lock(ig2_setting_att)
        # #     Dim iLocked (2)
        # #     ig2_setting_att.SetImportDestinationViewLock iLocked
        # #     set_import_destination_view_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_dft_standard_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportDftStandardLock(boolean iLocked)
                | 
                |     Locks or unlocks the Drafting standard option if the operation is allowed
                |     in the current administrated environment. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE: to lock the option.
                |             FALSE: to unlock the option. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.ig2_setting_att.SetImportDftStandardLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_dft_standard_lock'
        # # vba_code = """
        # # Public Function set_import_dft_standard_lock(ig2_setting_att)
        # #     Dim iLocked (2)
        # #     ig2_setting_att.SetImportDftStandardLock iLocked
        # #     set_import_dft_standard_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_dimensions_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportDimensionsLock(boolean iLocked)
                | 
                |     Locks or unlocks the Import dimensions option if the operation is allowed
                |     in the current administrated environment. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE: to lock the option.
                |             FALSE: to unlock the option. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.ig2_setting_att.SetImportDimensionsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_dimensions_lock'
        # # vba_code = """
        # # Public Function set_import_dimensions_lock(ig2_setting_att)
        # #     Dim iLocked (2)
        # #     ig2_setting_att.SetImportDimensionsLock iLocked
        # #     set_import_dimensions_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_end_points_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportEndPointsLock(boolean iLocked)
                | 
                |     Locks or unlocks the Create End Points option if the operation is allowed
                |     in the current administrated environment. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE: to lock the option.
                |             FALSE: to unlock the option. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.ig2_setting_att.SetImportEndPointsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_end_points_lock'
        # # vba_code = """
        # # Public Function set_import_end_points_lock(ig2_setting_att)
        # #     Dim iLocked (2)
        # #     ig2_setting_att.SetImportEndPointsLock iLocked
        # #     set_import_end_points_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_unit_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportUnitLock(boolean iLocked)
                | 
                |     Locks or unlocks the import unit option if the operation is allowed in the
                |     current administrated environment. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE: to lock the option.
                |             FALSE: to unlock the option. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_locked:
        :rtype: None
        """
        return self.ig2_setting_att.SetImportUnitLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_unit_lock'
        # # vba_code = """
        # # Public Function set_import_unit_lock(ig2_setting_att)
        # #     Dim iLocked (2)
        # #     ig2_setting_att.SetImportUnitLock iLocked
        # #     set_import_unit_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_mode(self, i_mode: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportMode(CatIg2ExportModeEnum iMode)
                | 
                |     Set the Export Mode option value.
                | 
                |     Parameters:
                | 
                |         iMode
                |             Legal values: An available value of the enum CatIg2ExportModeEnum.
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_mode: enum cat_ig2_export_mode_enum
        :rtype: None
        """
        return self.ig2_setting_att.set_ExportMode(i_mode)

    def set_export_sheets(self, i_sheets: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportSheets(CatIg2ExportSheetsEnum iSheets)
                | 
                |     set the Exported Sheets option value.
                | 
                |     Parameters:
                | 
                |         iSheets
                |             Legal values: An available value of the enum
                |             CatIg2ExportSheetsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_sheets:
        :rtype: None
        """
        return self.ig2_setting_att.set_ExportSheets(i_sheets)

    def set_export_view_as_viewport(self, i_views_as_viewports: bool) -> None:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub set_ExportViewAsViewport(boolean iViewsAsViewports)
                |     Set the value of the Export Views as Viewports option. That value is only
                |     taken into account when the export mode is set to
                |     Semantic.
                |
                |     Parameters:
                |
                |         iViewsAsViewports
                |             Legal values:
                |             TRUE : Enable the export of views as Viewports.
                |             FALSE : Disable the export of views as Viewports.
                |
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_views_as_viewports:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.ig2_setting_att.set_ExportViewAsViewport(i_views_as_viewports)

    def set_import_destination_view(self, i_destination_view: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportDestinationView(CatIg2ImportDestinationViewEnum
                | iDestinationView)
                | 
                |     Set the destination view.
                | 
                |     Parameters:
                | 
                |         iDestinationView
                |             Legal values: An available value of the enum
                |             CatIg2ImportDestinationViewEnum 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_destination_view: enum cat_ig2_import_destination_view_enum
        :rtype: None
        """
        return self.ig2_setting_att.set_ImportDestinationView(i_destination_view)

    def set_import_dft_standard(self, i_dft_standard: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportDftStandard(CATBSTR iDftStandard)
                | 
                |     Set the name of the Drafting standard, which define the standard of the
                |     resulting CATDrawing file.
                | 
                |     Parameters:
                | 
                |         iDftStandard
                |             the CATBSTR corresponding to the Drafting standard.
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dft_standard:
        :rtype: None
        """
        return self.ig2_setting_att.set_ImportDftStandard(i_dft_standard)

    def set_import_dimensions(self, i_dimensions: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportDimensions(CatIg2ImportDimensionsEnum
                | iDimensions)
                | 
                |     Set the Import dimensions option value.
                | 
                |     Parameters:
                | 
                |         iDimensions
                |             Legal values: An available value of the enum
                |             CatIg2ImportDimensionsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_dimensions: enum cat_ig2_import_dimensions_enum
        :rtype: None
        """
        return self.ig2_setting_att.set_ImportDimensions(i_dimensions)

    def set_import_end_points(self, i_end_points: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportEndPoints(CatIg2ImportCreateEndPointsEnum
                | iEndPoints)
                | 
                |     Set the Create End Points option value.
                | 
                |     Parameters:
                | 
                |         iEndPoints
                |             Legal values: An available value of the enum
                |             CatIg2ImportCreateEndPointsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_end_points: enum cat_ig2_import_create_end_points_enum
        :rtype: None
        """
        return self.ig2_setting_att.set_ImportEndPoints(i_end_points)

    def set_import_unit(self, i_unit: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportUnit(CatIg2ImportUnitEnum iUnit)
                | 
                |     Set the import unit.
                | 
                |     Parameters:
                | 
                |         iUnit
                |             Legal values: An available value of the enum CatIg2ImportUnitEnum
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_unit: enum cat_ig2_import_unit_enum
        :rtype: None
        """
        return self.ig2_setting_att.set_ImportUnit(i_unit)

    def __repr__(self):
        return f'Ig2SettingAtt(name="{self.name}")'
