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


class DxfSettingAtt(SettingController):
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
                |                         DxfSettingAtt
                | 
                | Interface dedicated to modify or read the current settings corresponding to the
                | DXF Data Exchange (used for DXF or DWG files)
                | 
                | Ensure consistency with the C++ interface to which the work is
                | delegated.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dxf_setting_att = com_object

    @property
    def export_blocks(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExportBlocks() As CatDxfExportBlocksEnum (Read
                | Only)
                | 
                |     Get the value of the Export Blocks option. That value is only taken into
                |     account when the export mode is set to Semantic.
                | 
                |     Parameters:
                | 
                |         oExportBlocks
                |             Legal values: An available value of the enum
                |             CatDxfExportBlocksEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_dxf_export_blocks_enum
        :rtype: int
        """

        return self.dxf_setting_att.ExportBlocks

    @property
    def export_dimensions_as_dimensions(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExportDimensionsAsDimensions() As boolean (Read
                | Only)
                | 
                |     Get the value of the Export Dimensions As Dimensions option. That value is
                |     only taken into account when the export mode is set to
                |     Semantic.
                | 
                |     Parameters:
                | 
                |         oExportDimension
                |             Legal values:
                |             TRUE : Export dimensions as dimensions.
                |             FALSE : Export dimensions as graphical block. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: bool
        """

        return self.dxf_setting_att.ExportDimensionsAsDimensions

    @property
    def export_layer_name(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExportLayerName() As boolean (Read Only)
                | 
                |     Get the value of the Export Layer Name option. That value is only taken
                |     into account when the export mode is set to Semantic.
                | 
                |     Parameters:
                | 
                |         oExportLayerName
                |             Legal values:
                |             TRUE : Export Layer Name.
                |             FALSE : Export Layer Number. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: bool
        """

        return self.dxf_setting_att.ExportLayerName

    @property
    def export_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExportMode() As CatDxfExportModeEnum (Read Only)
                | 
                |     Get the Export Mode option value.
                | 
                |     Parameters:
                | 
                |         oMode
                |             Legal values: An available value of the enum CatDxfExportModeEnum.
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_dxf_export_mode_enum
        :rtype: int
        """

        return self.dxf_setting_att.ExportMode

    @property
    def export_sheets(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExportSheets() As CatDxfExportSheetsEnum (Read
                | Only)
                | 
                |     Get the Exported Sheets option value.
                | 
                |     Parameters:
                | 
                |         oSheets
                |             Legal values: An available value of the enum
                |             CatDxfExportSheetsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_dxf_export_sheets_enum
        :rtype: int
        """

        return self.dxf_setting_att.ExportSheets

    @property
    def export_version(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExportVersion() As CatDxfExportVersionEnum (Read
                | Only)
                | 
                |     Get the Export Version option value.
                | 
                |     Parameters:
                | 
                |         oVersion
                |             Legal values: An available value of the enum
                |             CatDxfExportVersionEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_dxf_export_version_enum
        :rtype: int
        """

        return self.dxf_setting_att.ExportVersion

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

        return self.dxf_setting_att.ExportViewAsViewport

    @property
    def export_views_as_viewports(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExportViewsAsViewports() As boolean (Read Only)
                | 
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

        return self.dxf_setting_att.ExportViewsAsViewports

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

        return self.dxf_setting_att.ImportDftStandard

    @property
    def import_dimensions(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportDimensions() As CatDxfImportDimensionsEnum (Read
                | Only)
                | 
                |     Get the Import dimensions option value.
                | 
                |     Parameters:
                | 
                |         oDimensions
                |             Legal values: An available value of the enum
                |             CatDxfImportDimensionsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_dxf_import_dimensions_enum
        :rtype: int
        """

        return self.dxf_setting_att.ImportDimensions

    @property
    def import_dxf_standard(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportDxfStandard() As CATBSTR (Read Only)
                | 
                |     Get the name of the Dxf standard, which define the different mapping used
                |     at import.
                | 
                |     Parameters:
                | 
                |         oDxfStandard
                |             the CATBSTR corresponding to the Dxf standard. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: str
        """

        return self.dxf_setting_att.ImportDxfStandard

    @property
    def import_end_points(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportEndPoints() As CatDxfImportCreateEndPointsEnum (Read
                | Only)
                | 
                |     Get the Create End Points option value.
                | 
                |     Parameters:
                | 
                |         oEndPoints
                |             Legal values: An available value of the enum
                |             CatDxfImportCreateEndPointsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_dxf_import_create_end_points_enum
        :rtype: int
        """

        return self.dxf_setting_att.ImportEndPoints

    @property
    def import_keep_model_space(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportKeepModelSpace() As boolean (Read Only)
                | 
                |     Get the value of the Keep Model Space option.
                | 
                |     Parameters:
                | 
                |         oKeepModelSpace
                |             Legal values:
                |             TRUE : always keep the entire Model Space in its own sheet.
                |             FALSE : keep the entire Model Space in its own sheet but only if the automatic management detects that it's required. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: bool
        """

        return self.dxf_setting_att.ImportKeepModelSpace

    @property
    def import_map_layer_on2_dl(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportMapLayerOn2DL() As boolean (Read Only)
                | 
                |     Get the value of Map Layer On 2DL sheet option.
                | 
                |     Parameters:
                | 
                |         oMapLayerOn2DL
                |             Legal values:
                |             TRUE : always Map Layer On 2DL sheets.
                |             FALSE : No specific treatment on layer 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: bool
        """

        return self.dxf_setting_att.ImportMapLayerOn2DL

    @property
    def import_paper_spaces_in_background(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportPaperSpacesInBackground() As boolean (Read
                | Only)
                | 
                |     Get the value of the Paper Spaces in Background option.
                | 
                |     Parameters:
                | 
                |         oPaperSpacesInBackground
                |             Legal values:
                |             TRUE : All Paper Spaces entities are put into the corresponding Sheet's Background
                |             FALSE : All Paper Spaces entities are put into a view inside the corresponding Sheet's Working Views 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: bool
        """

        return self.dxf_setting_att.ImportPaperSpacesInBackground

    @property
    def import_scale_denominator(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportScaleDenominator() As double (Read Only)
                | 
                |     Get the denominator value of the scale factor. That value is only taken
                |     into account when the import unit is set to Scale Factor.
                | 
                |     Parameters:
                | 
                |         oScaleDen
                |             the denominator value of the scale factor. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: float
        """

        return self.dxf_setting_att.ImportScaleDenominator

    @property
    def import_scale_numerator(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportScaleNumerator() As double (Read Only)
                | 
                |     Get the numerator value of the scale factor. That value is only taken into
                |     account when the import unit is set to Scale Factor.
                | 
                |     Parameters:
                | 
                |         oScaleNum
                |             the numerator value of the scale factor. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :rtype: float
        """

        return self.dxf_setting_att.ImportScaleNumerator

    @property
    def import_unit(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportUnit() As CatDxfImportUnitEnum (Read Only)
                | 
                |     Get the import unit.
                | 
                |     Parameters:
                | 
                |         oUnit
                |             Legal values: An available value of the enum CatDxfImportUnitEnum.
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: enum cat_dxf_import_unit_enum
        :rtype: int
        """

        return self.dxf_setting_att.ImportUnit

    def get_export_blocks_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExportBlocksInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Export Blocks
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
        return self.dxf_setting_att.GetExportBlocksInfo(io_admin_level, io_locked)

    def get_export_dimensions_as_dimensions_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExportDimensionsAsDimensionsInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Export Dimensions As Dimensions
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
        return self.dxf_setting_att.GetExportDimensionsAsDimensionsInfo(io_admin_level, io_locked)

    def get_export_layer_name_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExportLayerNameInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Export Layer Name
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
        return self.dxf_setting_att.GetExportLayerNameInfo(io_admin_level, io_locked)

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
        return self.dxf_setting_att.GetExportModeInfo(io_admin_level, io_locked)

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
        return self.dxf_setting_att.GetExportSheetsInfo(io_admin_level, io_locked)

    def get_export_version_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExportVersionInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Export Version
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
        return self.dxf_setting_att.GetExportVersionInfo(io_admin_level, io_locked)

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

        return self.dxf_setting_att.GetExportViewAsViewportInfo(io_admin_level, io_locked)

    def get_export_views_as_viewports_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExportViewsAsViewportsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
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
        return self.dxf_setting_att.GetExportViewsAsViewportsInfo(io_admin_level, io_locked)

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
        return self.dxf_setting_att.GetImportDftStandardInfo(io_admin_level, io_locked)

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
        return self.dxf_setting_att.GetImportDimensionsInfo(io_admin_level, io_locked)

    def get_import_dxf_standard_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportDxfStandardInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DXF standard
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
        return self.dxf_setting_att.GetImportDxfStandardInfo(io_admin_level, io_locked)

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
        return self.dxf_setting_att.GetImportEndPointsInfo(io_admin_level, io_locked)

    def get_import_keep_model_space_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportKeepModelSpaceInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Keep Model Space
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
        return self.dxf_setting_att.GetImportKeepModelSpaceInfo(io_admin_level, io_locked)

    def get_import_map_layer_on2_dl_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportMapLayerOn2DLInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for Map Layer On 2DL
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
        return self.dxf_setting_att.GetImportMapLayerOn2DLInfo(io_admin_level, io_locked)

    def get_import_paper_spaces_in_background_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportPaperSpacesInBackgroundInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the Paper Spaces in Background
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
        return self.dxf_setting_att.GetImportPaperSpacesInBackgroundInfo(io_admin_level, io_locked)

    def get_import_scale_denominator_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportScaleDenominatorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the scale factor's denominator value
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
        return self.dxf_setting_att.GetImportScaleDenominatorInfo(io_admin_level, io_locked)

    def get_import_scale_numerator_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportScaleNumeratorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the scale factor's numerator value
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
        return self.dxf_setting_att.GetImportScaleNumeratorInfo(io_admin_level, io_locked)

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
        return self.dxf_setting_att.GetImportUnitInfo(io_admin_level, io_locked)

    def set_export_blocks_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExportBlocksLock(boolean iLocked)
                | 
                |     Locks or unlocks the Export Blocks option if the operation is allowed in
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
        return self.dxf_setting_att.SetExportBlocksLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_blocks_lock'
        # # vba_code = """
        # # Public Function set_export_blocks_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetExportBlocksLock iLocked
        # #     set_export_blocks_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_dimensions_as_dimensions_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExportDimensionsAsDimensionsLock(boolean iLocked)
                | 
                |     Locks or unlocks the Export Dimensions As Dimensions option if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
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
        return self.dxf_setting_att.SetExportDimensionsAsDimensionsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_dimensions_as_dimensions_lock'
        # # vba_code = """
        # # Public Function set_export_dimensions_as_dimensions_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetExportDimensionsAsDimensionsLock iLocked
        # #     set_export_dimensions_as_dimensions_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_layer_name_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExportLayerNameLock(boolean iLocked)
                | 
                |     Locks or unlocks the Export Layer Name option if the operation is allowed
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
        return self.dxf_setting_att.SetExportLayerNameLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_layer_name_lock'
        # # vba_code = """
        # # Public Function set_export_layer_name_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetExportLayerNameLock iLocked
        # #     set_export_layer_name_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

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
        return self.dxf_setting_att.SetExportModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_mode_lock'
        # # vba_code = """
        # # Public Function set_export_mode_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetExportModeLock iLocked
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
        return self.dxf_setting_att.SetExportSheetsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_sheets_lock'
        # # vba_code = """
        # # Public Function set_export_sheets_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetExportSheetsLock iLocked
        # #     set_export_sheets_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_version_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExportVersionLock(boolean iLocked)
                | 
                |     Locks or unlocks the Export Version option if the operation is allowed in
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
        return self.dxf_setting_att.SetExportVersionLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_version_lock'
        # # vba_code = """
        # # Public Function set_export_version_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetExportVersionLock iLocked
        # #     set_export_version_lock = iLocked
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

        return self.dxf_setting_att.SetExportViewAsViewportLock(i_locked)

    def set_export_views_as_viewports_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExportViewsAsViewportsLock(boolean iLocked)
                | 
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
        return self.dxf_setting_att.SetExportViewsAsViewportsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_views_as_viewports_lock'
        # # vba_code = """
        # # Public Function set_export_views_as_viewports_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetExportViewsAsViewportsLock iLocked
        # #     set_export_views_as_viewports_lock = iLocked
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
        return self.dxf_setting_att.SetImportDftStandardLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_dft_standard_lock'
        # # vba_code = """
        # # Public Function set_import_dft_standard_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetImportDftStandardLock iLocked
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
        return self.dxf_setting_att.SetImportDimensionsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_dimensions_lock'
        # # vba_code = """
        # # Public Function set_import_dimensions_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetImportDimensionsLock iLocked
        # #     set_import_dimensions_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_dxf_standard_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportDxfStandardLock(boolean iLocked)
                | 
                |     Locks or unlocks the DXF standard option if the operation is allowed in the
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
        return self.dxf_setting_att.SetImportDxfStandardLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_dxf_standard_lock'
        # # vba_code = """
        # # Public Function set_import_dxf_standard_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetImportDxfStandardLock iLocked
        # #     set_import_dxf_standard_lock = iLocked
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
        return self.dxf_setting_att.SetImportEndPointsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_end_points_lock'
        # # vba_code = """
        # # Public Function set_import_end_points_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetImportEndPointsLock iLocked
        # #     set_import_end_points_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_keep_model_space_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportKeepModelSpaceLock(boolean iLocked)
                | 
                |     Locks or unlocks the Keep Model Space option if the operation is allowed in
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
        return self.dxf_setting_att.SetImportKeepModelSpaceLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_keep_model_space_lock'
        # # vba_code = """
        # # Public Function set_import_keep_model_space_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetImportKeepModelSpaceLock iLocked
        # #     set_import_keep_model_space_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_map_layer_on2_dl_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportMapLayerOn2DLLock(boolean iLocked)
                | 
                |     Locks or unlocks Map on Layer2DL option if the operation is allowed in the
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
        return self.dxf_setting_att.SetImportMapLayerOn2DLLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_map_layer_on2_dl_lock'
        # # vba_code = """
        # # Public Function set_import_map_layer_on2_dl_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetImportMapLayerOn2DLLock iLocked
        # #     set_import_map_layer_on2_dl_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_paper_spaces_in_background_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportPaperSpacesInBackgroundLock(boolean iLocked)
                | 
                |     Locks or unlocks the Paper Spaces in Background option if the operation is
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
        return self.dxf_setting_att.SetImportPaperSpacesInBackgroundLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_paper_spaces_in_background_lock'
        # # vba_code = """
        # # Public Function set_import_paper_spaces_in_background_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetImportPaperSpacesInBackgroundLock iLocked
        # #     set_import_paper_spaces_in_background_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_scale_denominator_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportScaleDenominatorLock(boolean iLocked)
                | 
                |     Locks or unlocks the scale factor's denominator value option if the
                |     operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
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
        return self.dxf_setting_att.SetImportScaleDenominatorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_scale_denominator_lock'
        # # vba_code = """
        # # Public Function set_import_scale_denominator_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetImportScaleDenominatorLock iLocked
        # #     set_import_scale_denominator_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_scale_numerator_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportScaleNumeratorLock(boolean iLocked)
                | 
                |     Locks or unlocks the scale factor's numerator value option if the operation
                |     is allowed in the current administrated environment. In user mode this method
                |     will always return E_FAIL.
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
        return self.dxf_setting_att.SetImportScaleNumeratorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_scale_numerator_lock'
        # # vba_code = """
        # # Public Function set_import_scale_numerator_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetImportScaleNumeratorLock iLocked
        # #     set_import_scale_numerator_lock = iLocked
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
        return self.dxf_setting_att.SetImportUnitLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_unit_lock'
        # # vba_code = """
        # # Public Function set_import_unit_lock(dxf_setting_att)
        # #     Dim iLocked (2)
        # #     dxf_setting_att.SetImportUnitLock iLocked
        # #     set_import_unit_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_blocks(self, i_export_blocks: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportBlocks(CatDxfExportBlocksEnum iExportBlocks)
                | 
                |     Set the value of the Export Layer Name option. That value is only taken
                |     into account when the export mode is set to Semantic.
                | 
                |     Parameters:
                | 
                |         iExportBlocks
                |             Legal values: An available value of the enum
                |             CatDxfExportBlocksEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_export_blocks: enum cat_dxf_export_blocks_enum
        :rtype: None
        """
        return self.dxf_setting_att.set_ExportBlocks(i_export_blocks)

    def set_export_dimensions_as_dimensions(self, i_export_dimension: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportDimensionsAsDimensions(boolean
                | iExportDimension)
                | 
                |     Set the value of the Export Dimensions As Dimensions option. That value is
                |     only taken into account when the export mode is set to
                |     Semantic.
                | 
                |     Parameters:
                | 
                |         iExportDimension
                |             Legal values:
                |             TRUE : Export dimensions as dimensions.
                |             FALSE : Export dimensions as graphical block. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_export_dimension:
        :rtype: None
        """
        return self.dxf_setting_att.set_ExportDimensionsAsDimensions(i_export_dimension)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_dimensions_as_dimensions'
        # # vba_code = """
        # # Public Function set_export_dimensions_as_dimensions(dxf_setting_att)
        # #     Dim iExportDimension (2)
        # #     dxf_setting_att.set_ExportDimensionsAsDimensions iExportDimension
        # #     set_export_dimensions_as_dimensions = iExportDimension
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_layer_name(self, i_export_layer_name: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportLayerName(boolean iExportLayerName)
                | 
                |     Set the value of the Export Layer Name option. That value is only taken
                |     into account when the export mode is set to Semantic.
                | 
                |     Parameters:
                | 
                |         iExportLayerName
                |             Legal values:
                |             TRUE : Export Layer Name.
                |             FALSE : Export Layer Number. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_export_layer_name:
        :rtype: None
        """
        return self.dxf_setting_att.set_ExportLayerName(i_export_layer_name)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_layer_name'
        # # vba_code = """
        # # Public Function set_export_layer_name(dxf_setting_att)
        # #     Dim iExportLayerName (2)
        # #     dxf_setting_att.set_ExportLayerName iExportLayerName
        # #     set_export_layer_name = iExportLayerName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_mode(self, i_mode: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportMode(CatDxfExportModeEnum iMode)
                | 
                |     Set the Export Mode option value.
                | 
                |     Parameters:
                | 
                |         iMode
                |             Legal values: An available value of the enum CatDxfExportModeEnum.
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_mode: enum cat_dxf_export_mode_enum
        :rtype: None
        """
        return self.dxf_setting_att.set_ExportMode(i_mode)

    def set_export_sheets(self, i_sheets: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportSheets(CatDxfExportSheetsEnum iSheets)
                | 
                |     set the Exported Sheets option value.
                | 
                |     Parameters:
                | 
                |         iSheets
                |             Legal values: An available value of the enum
                |             CatDxfExportSheetsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_sheets: enum cat_dxf_export_sheets_enum
        :rtype: None
        """
        return self.dxf_setting_att.set_ExportSheets(i_sheets)

    def set_export_version(self, i_version: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportVersion(CatDxfExportVersionEnum iVersion)
                | 
                |     Set the Export Version option value.
                | 
                |     Parameters:
                | 
                |         iVersion
                |             Legal values: An available value of the enum
                |             CatDxfExportVersionEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_version:enum cat_dxf_export_version_enum
        :rtype: None
        """
        return self.dxf_setting_att.set_ExportVersion(i_version)

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

        return self.dxf_setting_att.set_ExportViewAsViewport(i_views_as_viewports)

    def set_export_views_as_viewports(self, i_views_as_viewports: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ExportViewsAsViewports(boolean iViewsAsViewports)
                | 
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
        return self.dxf_setting_att.set_ExportViewsAsViewports(i_views_as_viewports)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_views_as_viewports'
        # # vba_code = """
        # # Public Function set_export_views_as_viewports(dxf_setting_att)
        # #     Dim iViewsAsViewports (2)
        # #     dxf_setting_att.set_ExportViewsAsViewports iViewsAsViewports
        # #     set_export_views_as_viewports = iViewsAsViewports
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

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
        return self.dxf_setting_att.set_ImportDftStandard(i_dft_standard)

    def set_import_dimensions(self, i_dimensions: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportDimensions(CatDxfImportDimensionsEnum
                | iDimensions)
                | 
                |     Set the Import dimensions option value.
                | 
                |     Parameters:
                | 
                |         iDimensions
                |             Legal values: An available value of the enum
                |             CatDxfImportDimensionsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_dimensions: enum cat_dxf_import_dimensions_enum
        :rtype: None
        """
        return self.dxf_setting_att.set_ImportDimensions(i_dimensions)

    def set_import_dxf_standard(self, i_dxf_standard: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportDxfStandard(CATBSTR iDxfStandard)
                | 
                |     Set the name of the Dxf standard, which define the different mapping used
                |     at import.
                | 
                |     Parameters:
                | 
                |         iDxfStandard
                |             the CATBSTR corresponding to the Dxf standard. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dxf_standard:
        :rtype: None
        """
        return self.dxf_setting_att.set_ImportDxfStandard(i_dxf_standard)

    def set_import_end_points(self, i_end_points: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportEndPoints(CatDxfImportCreateEndPointsEnum
                | iEndPoints)
                | 
                |     Set the Create End Points option value.
                | 
                |     Parameters:
                | 
                |         iEndPoints
                |             Legal values: An available value of the enum
                |             CatDxfImportCreateEndPointsEnum. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_end_points: enum cat_dxf_import_create_end_points_enum
        :rtype: None
        """
        return self.dxf_setting_att.set_ImportEndPoints(i_end_points)

    def set_import_keep_model_space(self, i_keep_model_space: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportKeepModelSpace(boolean iKeepModelSpace)
                | 
                |     Set the value of the Keep Model Space option.
                | 
                |     Parameters:
                | 
                |         iKeepModelSpace
                |             Legal values:
                |             TRUE : always keep the entire Model Space in its own sheet.
                |             FALSE : keep the entire Model Space in its own sheet but only if the automatic management detects that it's required. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_keep_model_space:
        :rtype: None
        """
        return self.dxf_setting_att.set_ImportKeepModelSpace(i_keep_model_space)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_keep_model_space'
        # # vba_code = """
        # # Public Function set_import_keep_model_space(dxf_setting_att)
        # #     Dim iKeepModelSpace (2)
        # #     dxf_setting_att.set_ImportKeepModelSpace iKeepModelSpace
        # #     set_import_keep_model_space = iKeepModelSpace
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_map_layer_on2_dl(self, i_map_layer_on2_dl: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportMapLayerOn2DL(boolean iMapLayerOn2DL)
                | 
                |     Set the value of Map Layer On 2DL sheet option.
                | 
                |     Parameters:
                | 
                |         iMapLayerOn2DL
                |             Legal values:
                |             TRUE : always Map Layer On 2DL sheets.
                |             FALSE : No specific treatment on layer 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_map_layer_on2_dl:
        :rtype: None
        """
        return self.dxf_setting_att.set_ImportMapLayerOn2DL(i_map_layer_on2_dl)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_map_layer_on2_dl'
        # # vba_code = """
        # # Public Function set_import_map_layer_on2_dl(dxf_setting_att)
        # #     Dim iMapLayerOn2DL (2)
        # #     dxf_setting_att.set_ImportMapLayerOn2DL iMapLayerOn2DL
        # #     set_import_map_layer_on2_dl = iMapLayerOn2DL
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_paper_spaces_in_background(self, i_paper_spaces_in_background: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportPaperSpacesInBackground(boolean
                | iPaperSpacesInBackground)
                | 
                |     Set the value of the Paper Spaces in Background option.
                | 
                |     Parameters:
                | 
                |         iPaperSpacesInBackground
                |             Legal values:
                |             TRUE : All Paper Spaces entities are put into the corresponding Sheet's Background
                |             FALSE : All Paper Spaces entities are put into a view inside the corresponding Sheet's Working Views 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param bool i_paper_spaces_in_background:
        :rtype: None
        """
        return self.dxf_setting_att.set_ImportPaperSpacesInBackground(i_paper_spaces_in_background)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_paper_spaces_in_background'
        # # vba_code = """
        # # Public Function set_import_paper_spaces_in_background(dxf_setting_att)
        # #     Dim iPaperSpacesInBackground (2)
        # #     dxf_setting_att.set_ImportPaperSpacesInBackground iPaperSpacesInBackground
        # #     set_import_paper_spaces_in_background = iPaperSpacesInBackground
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_scale_denominator(self, i_scale_den: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportScaleDenominator(double iScaleDen)
                | 
                |     Get the denominator value of the scale factor. That value is only taken
                |     into account when the import unit is set to Scale Factor.
                | 
                |     Parameters:
                | 
                |         iScaleDen
                |             the denominator value of the scale factor, which is supposed to be
                |             not null. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param float i_scale_den:
        :rtype: None
        """
        return self.dxf_setting_att.set_ImportScaleDenominator(i_scale_den)

    def set_import_scale_numerator(self, i_scale_num: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportScaleNumerator(double iScaleNum)
                | 
                |     Set the numerator value of the scale factor. That value is only taken into
                |     account when the import unit is set to Scale Factor.
                | 
                |     Parameters:
                | 
                |         iScaleNum
                |             the numerator value of the scale factor. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param float i_scale_num:
        :rtype: None
        """
        return self.dxf_setting_att.set_ImportScaleNumerator(i_scale_num)

    def set_import_unit(self, i_unit: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub set_ImportUnit(CatDxfImportUnitEnum iUnit)
                | 
                |     Set the import unit.
                | 
                |     Parameters:
                | 
                |         iUnit
                |             Legal values: An available value of the enum CatDxfImportUnitEnum
                |             
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param int i_unit: enum cat_dxf_import_unit_enum
        :rtype: None
        """
        return self.dxf_setting_att.set_ImportUnit(i_unit)

    def __repr__(self):
        return f'DxfSettingAtt(name="{self.name}")'
