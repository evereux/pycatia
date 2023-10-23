#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class IgesSettingAtt(SettingController):
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
                |                         IgesSettingAtt
                | 
                | Represents the CATIA IGES setting controller object.
                | Role: The CATIA IGES setting controller object deals with the setting
                | attributes displayed in the IGES property page. To access this property
                | page:
                | 
                |     Click the Options command in the Tools menu
                |     Click + left of General to unfold the workbench list
                |     Click Compatibility
                |     Right scroll to display the property pages titles until you get
                |     IGES
                |     Click IGES
                | 
                | The New Elements setting controller object can be retrieved as an item of the
                | setting controller collection using its name "CAACafNewEltSettingCtrl" as
                | follows:
                | 
                |  Dim settingControllers1 As SettingControllers
                |  Set settingControllers1 = CATIA.SettingControllers
                |  Dim CATIAIGESSettingAtt1 As SettingController
                |  Set CATIAIGESSettingAtt1 = settingControllers1.Item("CATIdeIgesSettingCtrl")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.iges_setting_att = com_object

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Angle() As double
                | 
                |     Returns or sets the Angle setting parameter value.
                |     Role: The Angle setting parameter manages the maximal angle of
                |     deformation.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             [out] The Angle parameter value
                |             Legal values: value of angle in degree, between 0.0 and 10.0
                |             deg.

        :rtype: float
        """

        return self.iges_setting_att.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.iges_setting_att.Angle = value

    @property
    def apply_join(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ApplyJoin() As long
                | 
                |     Returns or sets the Apply join setting parameter value.
                |     Role: The XXX setting parameter manages the Apply Join
                |     mode
                | 
                |     Parameters:
                | 
                |         oApplyJoin
                |             [out] The Apply join parameter value
                |             Legal values: 1 To Apply Join on faces, 0
                |             otherwise.

        :rtype: int
        """

        return self.iges_setting_att.ApplyJoin

    @apply_join.setter
    def apply_join(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.ApplyJoin = value

    @property
    def author_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AuthorName() As CATBSTR
                | 
                |     Returns or sets the Author Name setting parameter value.
                |     Role: The Author Name setting parameter manages the Author
                |     Name.
                | 
                |     Parameters:
                | 
                |         oAuthorName
                |             [out] The Author Name parameter value
                |             Legal values: (any text).

        :rtype: str
        """

        return self.iges_setting_att.AuthorName

    @author_name.setter
    def author_name(self, value: str):
        """
        :param str value:
        """

        self.iges_setting_att.AuthorName = value

    @property
    def author_organization(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AuthorOrganization() As CATBSTR
                | 
                |     Returns or sets the Author Organization setting parameter
                |     value.
                |     Role: The Author Organization setting parameter manages the Author
                |     Organization.
                | 
                |     Parameters:
                | 
                |         oAuthorOrganization
                |             [out] The Author Organization parameter value
                |             Legal values: (any text).

        :rtype: str
        """

        return self.iges_setting_att.AuthorOrganization

    @author_organization.setter
    def author_organization(self, value: str):
        """
        :param str value:
        """

        self.iges_setting_att.AuthorOrganization = value

    @property
    def crv_mod(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CrvMod() As long
                | 
                |     Returns or sets the Export BSpline mode setting parameter
                |     value.
                |     Role: The Export BSpline mode setting parameter manages the mode to export
                |     curves and surfaces
                | 
                |     Parameters:
                | 
                |         oCrvMod
                |             [out] The Export BSpline mode parameter value
                |             Legal values:
                |                 0 for standard mode;
                |                 1 for BSpline mode : all curves and surfaces will be exported
                |                                      as B-Spline curves and surfaces.

        :rtype: int
        """

        return self.iges_setting_att.CrvMod

    @crv_mod.setter
    def crv_mod(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.CrvMod = value

    @property
    def export_msbo(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExportMSBO() As long
                | 
                |     Returns or sets the Export Solid Mode setting parameter
                |     value.
                |     Role: The Export Solid Mode setting parameter manages the export of solids
                |     and shells
                | 
                |     Parameters:
                | 
                |         oExportMSBO
                |             [out] The Export Solid Mode parameter value
                |             Legal values: 1 to export solids and shells as 186/514 IGES
                |             entities, 0 to export them as trimmed surfaces.

        :rtype: int
        """

        return self.iges_setting_att.ExportMSBO

    @export_msbo.setter
    def export_msbo(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.ExportMSBO = value

    @property
    def export_unit(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ExportUnit() As long
                | 
                |     Returns or sets the Export Units setting parameter value.
                |     Role: The Export Units setting parameter manages the unit in exported IGES
                |     Files.
                | 
                |     Parameters:
                | 
                |         oExportUnit
                |             [out] The Export Units parameter value
                |             Legal values: 0-10 :
                |                 0 : user unit;
                |                 1 : Inches;
                |                 2 : Millimeters;
                |                 3 : Feet;
                |                 4 : Miles;
                |                 5 : Meters;
                |                 6 : Kilometers;
                |                 7 : Mils;
                |                 8 : Microns;
                |                 9 : Centimeters;
                |                10 : Microinches.

        :rtype: int
        """

        return self.iges_setting_att.ExportUnit

    @export_unit.setter
    def export_unit(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.ExportUnit = value

    @property
    def import_group_as_sel_set(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImportGroupAsSelSet() As long
                | 
                |     Returns or sets the Import Selection Set mode setting parameter
                |     value.
                |     Role: The Import Selection Set mode setting parameter manages the Import of
                |     IGES groups.
                | 
                |     Parameters:
                | 
                |         oImportGroupAsSelSet
                |             [out] The Import Selection Set mode parameter
                |             value
                |             Legal values:
                |                 1 To map IGES Groups as Selection Sets,
                |                 0 otherwise.

        :rtype: int
        """

        return self.iges_setting_att.ImportGroupAsSelSet

    @import_group_as_sel_set.setter
    def import_group_as_sel_set(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.ImportGroupAsSelSet = value

    @property
    def only_show(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OnlyShow() As long
                | 
                |     Returns or sets the Export only show setting parameter
                |     value.
                |     Role: The Export only show setting parameter manages the mode to export
                |     entities in No-Show
                | 
                |     Parameters:
                | 
                |         oOnlyShow
                |             [out] The Export only show parameter value
                |             Legal values: 1 to export only visible elements, 0 to export
                |             visible and invisible elements.

        :rtype: int
        """

        return self.iges_setting_att.OnlyShow

    @only_show.setter
    def only_show(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.OnlyShow = value

    @property
    def opt_c2_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OptC2Mode() As long
                | 
                |     Returns or sets the Continuity Optimization Mode setting parameter
                |     value.
                |     Role: The Continuity Optimization Mode setting parameter manages the
                |     ...
                | 
                |     Parameters:
                | 
                |         oOptC2Mode
                |             [out] The Continuity Optimization Mode parameter
                |             value
                |             Legal values: 0 to Disable Optimize Continuity ; 1 to Enable
                |             default Optimize Continuity 2 to Enable Advanced Optimize
                |             Continuity.

        :rtype: int
        """

        return self.iges_setting_att.OptC2Mode

    @opt_c2_mode.setter
    def opt_c2_mode(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.OptC2Mode = value

    @property
    def opt_clean_topo_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OptCleanTopoMode() As long
                | 
                |     Returns or sets the clean topo mode setting parameter
                |     value.
                |     Role: The clean topo mode setting parameter manages the the Fitting Mode,
                |     in Advanced Optimize Continuity Mode.
                | 
                |     Parameters:
                | 
                |         oOptCleanTopoMode
                |             [out] The clean topo mode parameter value
                |             Legal values: 0 to Disable the clean topo Mode, 1 to Enable the
                |             clean topo Mode.

        :rtype: int
        """

        return self.iges_setting_att.OptCleanTopoMode

    @opt_clean_topo_mode.setter
    def opt_clean_topo_mode(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.OptCleanTopoMode = value

    @property
    def opt_fitting_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OptFittingMode() As long
                | 
                |     Returns or sets the Fitting Mode setting parameter value.
                |     Role: The Fitting Mode setting parameter manages the Fitting Mode, in
                |     Advanced Optimize Continuity Mode.
                | 
                |     Parameters:
                | 
                |         oOptFittingMode
                |             [out] The Fitting Mode parameter value
                |             Fitting Mode values: 0 to Disable the Fitting Mode, 1 to Enable the
                |             Fitting Mode.

        :rtype: int
        """

        return self.iges_setting_att.OptFittingMode

    @opt_fitting_mode.setter
    def opt_fitting_mode(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.OptFittingMode = value

    @property
    def opt_invalid_geom_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OptInvalidGeomMode() As long
                | 
                |     Returns or sets the InvalidGeom mode setting parameter
                |     value.
                |     Role: The InvalidGeom mode setting parameter manages the Invalid Geometry
                |     Checks.
                | 
                |     Parameters:
                | 
                |         oOptInvalidGeomMode
                |             [out] The InvalidGeom mode parameter value
                |             Legal values: 0 to disable Invalid Geometry Checks, 1 to enable
                |             it.

        :rtype: int
        """

        return self.iges_setting_att.OptInvalidGeomMode

    @opt_invalid_geom_mode.setter
    def opt_invalid_geom_mode(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.OptInvalidGeomMode = value

    @property
    def opt_loop3_d_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OptLoop3DMode() As long
                | 
                |     Returns or sets the Force 3D Loop setting parameter value.
                |     Role: The Force 3D Loop setting parameter manages the Import of IGES
                |     boundaries, to use only the 3D representation.
                | 
                |     Parameters:
                | 
                |         oOptLoop3DMode
                |             [out] The Force 3D Loop parameter value
                |             Legal values: 0 to keep file preference, 1 to Force the use of 3D
                |             representation.

        :rtype: int
        """

        return self.iges_setting_att.OptLoop3DMode

    @opt_loop3_d_mode.setter
    def opt_loop3_d_mode(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.OptLoop3DMode = value

    @property
    def part_prod_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PartProdMode() As long
                | 
                |     Returns or sets the Import Product mode setting parameter
                |     value.
                |     Role: The Import Product mode setting parameter manages the Product mode
                |     for Import of 308/408 IGES entities.
                | 
                |     Parameters:
                | 
                |         oPartProdMode
                |             [out] The Import Product mode parameter value
                |             Legal values: 0 to import 308/408 in a CATPart, 1 to create a
                |             Product Structure.

        :rtype: int
        """

        return self.iges_setting_att.PartProdMode

    @part_prod_mode.setter
    def part_prod_mode(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.PartProdMode = value

    @property
    def rep_mod(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RepMod() As long
                | 
                |     Returns or sets the Export representation mode setting parameter
                |     value.
                |     Role: The Export representation mode setting parameter manages the export
                |     of faces as surfaces or as wireframe.
                | 
                |     Parameters:
                | 
                |         oRepMod
                |             [out] The Export representation mode parameter
                |             value
                |             Legal values: 1 to export surfaces as wireframes, 0
                |             otherwise.

        :rtype: int
        """

        return self.iges_setting_att.RepMod

    @rep_mod.setter
    def rep_mod(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.RepMod = value

    @property
    def show_completion_dialog_box(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShowCompletionDialogBox() As long
                | 
                |     Returns or sets the Show/No Show dialog box setting parameter
                |     value.
                |     Role: The Show/No Show dialog box setting parameter manages the visibility
                |     of the Completion dialog box.
                |     Legal values: 1 to show, and 0 to hide the Show/No Show dialog box.

        :rtype: int
        """

        return self.iges_setting_att.ShowCompletionDialogBox

    @show_completion_dialog_box.setter
    def show_completion_dialog_box(self, value: int):
        """
        :param int value:
        """

        self.iges_setting_att.ShowCompletionDialogBox = value

    @property
    def tol_join(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TolJoin() As double
                | 
                |     Returns or sets the join tolerance setting parameter
                |     value.
                |     Role: The join tolerance setting parameter manages the Tolerance for
                |     Join
                | 
                |     Parameters:
                | 
                |         oTolJoin
                |             [out] The join tolerance parameter value
                |             Legal values: Value of tolerance in mm, between 0.0 and 0.1
                |             mm.

        :rtype: float
        """

        return self.iges_setting_att.TolJoin

    @tol_join.setter
    def tol_join(self, value: float):
        """
        :param float value:
        """

        self.iges_setting_att.TolJoin = value

    @property
    def tol_opt_invalid_geom(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TolOptInvalidGeom() As double
                | 
                |     Returns or sets the InvalidGeom Tolerance setting parameter
                |     value.
                |     Role: The InvalidGeom Tolerance setting parameter manages the Tolerance for
                |     invalid geometry checks.
                | 
                |     Parameters:
                | 
                |         oTolOptInvalidGeom
                |             [out] The InvalidGeom Tolerance parameter value
                |             Legal values: value of tolerance, in mm, between 0.5 and 20
                |             mm.

        :rtype: float
        """

        return self.iges_setting_att.TolOptInvalidGeom

    @tol_opt_invalid_geom.setter
    def tol_opt_invalid_geom(self, value: float):
        """
        :param float value:
        """

        self.iges_setting_att.TolOptInvalidGeom = value

    @property
    def tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Tolerance() As double
                | 
                |     Returns or sets the tolerance ( optimize - fitting ) setting parameter
                |     value.
                |     Role: The tolerance ( optimize - fitting ) setting parameter manages the
                |     tolerance for Optimize continuity and Fitting.
                | 
                |     Parameters:
                | 
                |         oTolerance
                |             [out] The tolerance ( optimize - fitting ) parameter
                |             value
                |             Legal values: value of tolerance in mm, between 0.0005 and 0.10
                |             mm.

        :rtype: float
        """

        return self.iges_setting_att.Tolerance

    @tolerance.setter
    def tolerance(self, value: float):
        """
        :param float value:
        """

        self.iges_setting_att.Tolerance = value

    def get_angle_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAngleInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Angle setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetAngleInfo(io_admin_level, io_locked)

    def get_apply_join_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetApplyJoinInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Apply Join setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetApplyJoinInfo(io_admin_level, io_locked)

    def get_author_name_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAuthorNameInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AuthorName
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetAuthorNameInfo(io_admin_level, io_locked)

    def get_author_organization_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAuthorOrganizationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the AuthorOrganization
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetAuthorOrganizationInfo(io_admin_level, io_locked)

    def get_crv_mod_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCrvModInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Export BSpline mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetCrvModInfo(io_admin_level, io_locked)

    def get_export_msbo_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExportMSBOInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Export Solid Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetExportMSBOInfo(io_admin_level, io_locked)

    def get_export_unit_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetExportUnitInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Export Units setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetExportUnitInfo(io_admin_level, io_locked)

    def get_import_group_as_sel_set_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetImportGroupAsSelSetInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Import Selection Set mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetImportGroupAsSelSetInfo(io_admin_level, io_locked)

    def get_only_show_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOnlyShowInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Export only show setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetOnlyShowInfo(io_admin_level, io_locked)

    def get_opt_c2_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOptC2ModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Continuity Optimization Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetOptC2ModeInfo(io_admin_level, io_locked)

    def get_opt_clean_topo_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOptCleanTopoModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Clean Topo Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetOptCleanTopoModeInfo(io_admin_level, io_locked)

    def get_opt_fitting_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOptFittingModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Fitting Mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetOptFittingModeInfo(io_admin_level, io_locked)

    def get_opt_invalid_geom_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOptInvalidGeomModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the InvalidGeom mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetOptInvalidGeomModeInfo(io_admin_level, io_locked)

    def get_opt_loop3_d_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOptLoop3DModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Force 3D Loop setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetOptLoop3DModeInfo(io_admin_level, io_locked)

    def get_part_prod_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPartProdModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Import Product mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetPartProdModeInfo(io_admin_level, io_locked)

    def get_rep_mod_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRepModInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Export representation mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetRepModInfo(io_admin_level, io_locked)

    def get_show_completion_dialog_box_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetShowCompletionDialogBoxInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Show/No Show dialog box setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetShowCompletionDialogBoxInfo(io_admin_level, io_locked)

    def get_tol_join_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTolJoinInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the join tolerance setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetTolJoinInfo(io_admin_level, io_locked)

    def get_tol_opt_invalid_geom_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTolOptInvalidGeomInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the InvalidGeom Tolerance setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetTolOptInvalidGeomInfo(io_admin_level, io_locked)

    def get_tolerance_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetToleranceInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Tolerance ( optimize - fitting ) setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.iges_setting_att.GetToleranceInfo(io_admin_level, io_locked)

    def set_angle_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAngleLock(boolean iLocked)
                | 
                |     Locks or unlocks the Angle setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetAngleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_angle_lock'
        # # vba_code = """
        # # Public Function set_angle_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetAngleLock iLocked
        # #     set_angle_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_apply_join_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetApplyJoinLock(boolean iLocked)
                | 
                |     Locks or unlocks the Apply Join setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetApplyJoinLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_apply_join_lock'
        # # vba_code = """
        # # Public Function set_apply_join_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetApplyJoinLock iLocked
        # #     set_apply_join_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_author_name_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAuthorNameLock(boolean iLocked)
                | 
                |     Locks or unlocks the AuthorName parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetAuthorNameLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_author_name_lock'
        # # vba_code = """
        # # Public Function set_author_name_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetAuthorNameLock iLocked
        # #     set_author_name_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_author_organization_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAuthorOrganizationLock(boolean iLocked)
                | 
                |     Locks or unlocks the AuthorOrganization parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetAuthorOrganizationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_author_organization_lock'
        # # vba_code = """
        # # Public Function set_author_organization_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetAuthorOrganizationLock iLocked
        # #     set_author_organization_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_crv_mod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCrvModLock(boolean iLocked)
                | 
                |     Locks or unlocks the Export BSpline mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetCrvModLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_crv_mod_lock'
        # # vba_code = """
        # # Public Function set_crv_mod_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetCrvModLock iLocked
        # #     set_crv_mod_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_msbo_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExportMSBOLock(boolean iLocked)
                | 
                |     Locks or unlocks the Export Solid Mode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetExportMSBOLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_msbo_lock'
        # # vba_code = """
        # # Public Function set_export_msbo_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetExportMSBOLock iLocked
        # #     set_export_msbo_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_export_unit_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetExportUnitLock(boolean iLocked)
                | 
                |     Locks or unlocks the Export Units setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetExportUnitLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_export_unit_lock'
        # # vba_code = """
        # # Public Function set_export_unit_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetExportUnitLock iLocked
        # #     set_export_unit_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_import_group_as_sel_set_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetImportGroupAsSelSetLock(boolean iLocked)
                | 
                |     Locks or unlocks the Import Selection Set mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetImportGroupAsSelSetLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_import_group_as_sel_set_lock'
        # # vba_code = """
        # # Public Function set_import_group_as_sel_set_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetImportGroupAsSelSetLock iLocked
        # #     set_import_group_as_sel_set_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_only_show_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOnlyShowLock(boolean iLocked)
                | 
                |     Locks or unlocks the Export only show setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetOnlyShowLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_only_show_lock'
        # # vba_code = """
        # # Public Function set_only_show_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetOnlyShowLock iLocked
        # #     set_only_show_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_opt_c2_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOptC2ModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Continuity Optimizationmode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetOptC2ModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_opt_c2_mode_lock'
        # # vba_code = """
        # # Public Function set_opt_c2_mode_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetOptC2ModeLock iLocked
        # #     set_opt_c2_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_opt_clean_topo_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOptCleanTopoModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Clean Topo Mode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetOptCleanTopoModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_opt_clean_topo_mode_lock'
        # # vba_code = """
        # # Public Function set_opt_clean_topo_mode_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetOptCleanTopoModeLock iLocked
        # #     set_opt_clean_topo_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_opt_fitting_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOptFittingModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Fitting Mode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetOptFittingModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_opt_fitting_mode_lock'
        # # vba_code = """
        # # Public Function set_opt_fitting_mode_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetOptFittingModeLock iLocked
        # #     set_opt_fitting_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_opt_invalid_geom_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOptInvalidGeomModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the InvalidGeom mode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetOptInvalidGeomModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_opt_invalid_geom_mode_lock'
        # # vba_code = """
        # # Public Function set_opt_invalid_geom_mode_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetOptInvalidGeomModeLock iLocked
        # #     set_opt_invalid_geom_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_opt_loop3_d_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOptLoop3DModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Force 3D Loop setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetOptLoop3DModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_opt_loop3_d_mode_lock'
        # # vba_code = """
        # # Public Function set_opt_loop3_d_mode_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetOptLoop3DModeLock iLocked
        # #     set_opt_loop3_d_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_part_prod_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPartProdModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Import Product mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetPartProdModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_part_prod_mode_lock'
        # # vba_code = """
        # # Public Function set_part_prod_mode_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetPartProdModeLock iLocked
        # #     set_part_prod_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rep_mod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRepModLock(boolean iLocked)
                | 
                |     Locks or unlocks the Export representation mode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetRepModLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rep_mod_lock'
        # # vba_code = """
        # # Public Function set_rep_mod_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetRepModLock iLocked
        # #     set_rep_mod_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_show_completion_dialog_box_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetShowCompletionDialogBoxLock(boolean iLocked)
                | 
                |     Locks or unlocks the Show/No Show dialog box setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetShowCompletionDialogBoxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_show_completion_dialog_box_lock'
        # # vba_code = """
        # # Public Function set_show_completion_dialog_box_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetShowCompletionDialogBoxLock iLocked
        # #     set_show_completion_dialog_box_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tol_join_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTolJoinLock(boolean iLocked)
                | 
                |     Locks or unlocks the join tolerance setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetTolJoinLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tol_join_lock'
        # # vba_code = """
        # # Public Function set_tol_join_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetTolJoinLock iLocked
        # #     set_tol_join_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tol_opt_invalid_geom_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTolOptInvalidGeomLock(boolean iLocked)
                | 
                |     Locks or unlocks the InvalidGeom Tolerance setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetTolOptInvalidGeomLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tol_opt_invalid_geom_lock'
        # # vba_code = """
        # # Public Function set_tol_opt_invalid_geom_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetTolOptInvalidGeomLock iLocked
        # #     set_tol_opt_invalid_geom_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tolerance_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetToleranceLock(boolean iLocked)
                | 
                |     Locks or unlocks the Tolerance ( optimize - fitting ) setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.iges_setting_att.SetToleranceLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tolerance_lock'
        # # vba_code = """
        # # Public Function set_tolerance_lock(iges_setting_att)
        # #     Dim iLocked (2)
        # #     iges_setting_att.SetToleranceLock iLocked
        # #     set_tolerance_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'IgesSettingAtt(name="{self.name}")'
