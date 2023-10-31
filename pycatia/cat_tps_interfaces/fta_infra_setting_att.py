#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class FtaInfraSettingAtt(SettingController):
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
                |                         FTAInfraSettingAtt
                | 
                | Represents the FT&A (Functional Tolerancing & Annotation) infrastructure
                | setting controller object.
                | Role: The FT&A infrastructure setting controller object deals with the setting
                | parameters displayed in:
                | 
                |     The Tolerancing property page for the Tolerancing Standard and the Leader
                |     Associativity setting parameters.
                |     To access this property page:
                |         Click the Options command in the Tools menu
                |         Click + left of Mechanical Design to unfold the workbench
                |         list
                |         Click Functional Tolerancing & Annotation
                |         Click Tolerancing
                |     The Display property page for the Grid Display, the Grid Snap Point, the
                |     Allow Distorsions, the Grid Primary Spacing, the Grid Secondary Step, the GridV
                |     Primary Spacing, the GridV Secondary Step, the Under Set Tree Visu, the Under
                |     View Tree Visu, and the Under Feature Tree Visu setting
                |     parameters.
                |     To access this property page:
                |         Click the Options command in the Tools menu
                |         Click + left of Mechanical Design to unfold the workbench
                |         list
                |         Click Functional Tolerancing & Annotation
                |         Click Display
                |     The Manipulators property page for the Manipulator Reference Size, the
                |     Manipulator Zoom Capability, and the Move After Creation, setting
                |     parameters.
                |     To access this property page:
                |         Click the Options command in the Tools menu
                |         Click + left of Mechanical Design to unfold the workbench
                |         list
                |         Click Functional Tolerancing & Annotation
                |         Click Manipulators
                |     The View/Annotation Plane property page for the View Associativity, the
                |     View Referential, the View Referential Zoomable, and the View Profile setting
                |     parameters.
                |     To access this property page:
                |         Click the Options command in the Tools menu
                |         Click + left of Mechanical Design to unfold the workbench
                |         list
                |         Click Functional Tolerancing & Annotation
                |         Click View/Annotation Plane
                |     The Cgr Management property page for the Save in CGR setting
                |     parameter.
                |     To access this property page:
                |         Click the Options command in the Tools menu
                |         Click + left of Infrastructure to unfold the workbench
                |         list
                |         Click Product Structure
                |         Click Cgr Management
                | 
                |     The Save in CGR setting parameter represents the state of the check button
                |     named: Save FTA 3D Annotation representation in CGR.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.fta_infra_setting_att = com_object

    @property
    def allow_distortions(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AllowDistortions() As boolean
                | 
                |     Returns or sets the Allow Distortions setting parameter
                |     value.
                |     True if the Allow Distortions setting parameter is checked and thus enables
                |     distorsions.
                |     Role: The Allow Distortions setting parameter defines whether grid spacing
                |     and graduations are the same horizontally and vertically (no distorsion) or not
                |     (distorsions enabled).

        :rtype: bool
        """

        return self.fta_infra_setting_att.AllowDistortions

    @allow_distortions.setter
    def allow_distortions(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.AllowDistortions = value

    @property
    def grid_display(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GridDisplay() As boolean
                | 
                |     Returns or sets the Grid Display setting parameter value.
                |     True if the Grid Display setting parameter is checked and thus enables the
                |     grid to be displayed.
                |     Role: The Grid Display setting parameter displays a grid on the active
                |     view.

        :rtype: bool
        """

        return self.fta_infra_setting_att.GridDisplay

    @grid_display.setter
    def grid_display(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.GridDisplay = value

    @property
    def grid_primary_spacing(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GridPrimarySpacing() As double
                | 
                |     Returns or sets the Grid Primary Spacing setting parameter
                |     value.
                |     Role: The Grid Primary Spacing setting parameter defines the horizontal
                |     spacing on the grid, expressed in millimiters. The default value is 100mm.

        :rtype: float
        """

        return self.fta_infra_setting_att.GridPrimarySpacing

    @grid_primary_spacing.setter
    def grid_primary_spacing(self, value: float):
        """
        :param float value:
        """

        self.fta_infra_setting_att.GridPrimarySpacing = value

    @property
    def grid_secondary_step(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GridSecondaryStep() As long
                | 
                |     Returns or sets the Grid Secondary Step setting parameter
                |     value.
                |     Role: The Grid Secondary Step setting parameter defines the grid's
                |     horizontal graduations. The default value is 10.

        :rtype: int
        """

        return self.fta_infra_setting_att.GridSecondaryStep

    @grid_secondary_step.setter
    def grid_secondary_step(self, value: int):
        """
        :param int value:
        """

        self.fta_infra_setting_att.GridSecondaryStep = value

    @property
    def grid_snap_point(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GridSnapPoint() As boolean
                | 
                |     Returns or sets the Grid Snap Point setting parameter
                |     value.
                |     True if the Grid Snap Point setting parameter is checked and thus enables
                |     the annotation to be snapped to the nearest grid point. Otherwise, the gris is
                |     not used to anchor the annotation.

        :rtype: bool
        """

        return self.fta_infra_setting_att.GridSnapPoint

    @grid_snap_point.setter
    def grid_snap_point(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.GridSnapPoint = value

    @property
    def grid_v_primary_spacing(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GridVPrimarySpacing() As double
                | 
                |     Returns or sets the GridV Primary Spacing setting parameter
                |     value.
                |     Role: The GridV Primary Spacing setting parameter defines the vertical
                |     spacing on the grid, expressed in millimiters. The default value is 100mm. Set
                |     this value only if distorsions are allowed thanks to the AllowDistortions
                |     property. Otherwise, the value sets to the Grid Primary Spacing setting
                |     parameter thanks to the GridPrimarySpacing for horizontal spacing is taken into
                |     account.

        :rtype: float
        """

        return self.fta_infra_setting_att.GridVPrimarySpacing

    @grid_v_primary_spacing.setter
    def grid_v_primary_spacing(self, value: float):
        """
        :param float value:
        """

        self.fta_infra_setting_att.GridVPrimarySpacing = value

    @property
    def grid_v_secondary_step(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GridVSecondaryStep() As long
                | 
                |     Returns or sets the GridV Secondary Step setting parameter
                |     value.
                |     Role: The GridV Secondary Step setting parameter defines the grid's
                |     vertical graduations. The default value is 10. Set this value only if
                |     distorsions are allowed thanks to the AllowDistortions property. Otherwise, the
                |     value sets to the Grid Secondary Step setting parameter thanks to the
                |     GridSecondaryStep for the number of horizontal graduations is taken into
                |     account.

        :rtype: int
        """

        return self.fta_infra_setting_att.GridVSecondaryStep

    @grid_v_secondary_step.setter
    def grid_v_secondary_step(self, value: int):
        """
        :param int value:
        """

        self.fta_infra_setting_att.GridVSecondaryStep = value

    @property
    def leader_associativity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LeaderAssociativity() As CATFTALeaderAssociativity
                | 
                |     Returns or sets the Leader Associativity setting parameter
                |     value.
                |     Role: The Leader Associativity setting parameter defines the associativity
                |     of a leader with the pointed geometrical element.

        :return: enum catfta_leader_associativity
        :rtype: int
        """

        return self.fta_infra_setting_att.LeaderAssociativity

    @leader_associativity.setter
    def leader_associativity(self, value: int):
        """
        :param int value: enum catfta_leader_associativity
        """

        self.fta_infra_setting_att.LeaderAssociativity = value

    @property
    def man_ref_siz(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ManRefSiz() As double
                | 
                |     Returns or sets the Manipulator Reference Size setting parameter
                |     value.
                |     Role: The Manipulator Reference Size setting parameter defines the size of
                |     the manipulator attached to the end of an annotation leader. The default value
                |     is 2mm.

        :rtype: float
        """

        return self.fta_infra_setting_att.ManRefSiz

    @man_ref_siz.setter
    def man_ref_siz(self, value: float):
        """
        :param float value:
        """

        self.fta_infra_setting_att.ManRefSiz = value

    @property
    def man_zoo_cap(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ManZooCap() As boolean
                | 
                |     Returns or sets the Manipulator Zoom Capability setting parameter
                |     value.
                |     True if the Manipulator Zoom Capability setting parameter is checked and
                |     thus enables the annotation leader end manipulator to be zoomable. Otherwise,
                |     it is not zoomable.

        :rtype: bool
        """

        return self.fta_infra_setting_att.ManZooCap

    @man_zoo_cap.setter
    def man_zoo_cap(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.ManZooCap = value

    @property
    def move_after_creation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MoveAfterCreation() As boolean
                | 
                |     Returns or sets the Move After Creation setting parameter
                |     value.
                |     True if the Move After Creation setting parameter is checked and thus
                |     enables the annotation leader end manipulator to be moved, after the annotation
                |     creation, along lines or curves that represent the intersection between the
                |     geometry and the annotation's plane. Otherwise, the annotation leader end
                |     manipulator cannot be moved.

        :rtype: bool
        """

        return self.fta_infra_setting_att.MoveAfterCreation

    @move_after_creation.setter
    def move_after_creation(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.MoveAfterCreation = value

    @property
    def save_in_cgr(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SaveInCGR() As boolean
                | 
                |     Returns or sets the Save In CGR setting parameter value.
                |     True if the Save In CGR setting parameter is checked.
                |     Role: When set to True, the FT&A 3D Annotation representations are saved in
                |     CGR. Otherwise, they are not saved.

        :rtype: bool
        """

        return self.fta_infra_setting_att.SaveInCGR

    @save_in_cgr.setter
    def save_in_cgr(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.SaveInCGR = value

    @property
    def standard(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Standard() As CATBSTR
                | 
                |     Returns or sets the Tolerancing Standard setting parameter
                |     value.
                |     Role: The Tolerancing Standard setting parameter defines the standard of
                |     the annotation's set.
                |     Legal values: five conventional standards are available:
                | 
                |         ASME: American Society for Mechanical Engineers
                |         ASME_3D: American Society for Mechanical Engineers
                |         ANSI: American National Standards Institute
                |         JIS: Japanese Industrial Standard
                |         ISO: International Organization for Standardization

        :rtype: str
        """

        return self.fta_infra_setting_att.Standard

    @standard.setter
    def standard(self, value: str):
        """
        :param str value:
        """

        self.fta_infra_setting_att.Standard = value

    @property
    def under_feature(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UnderFeature() As boolean
                | 
                |     Returns or sets the Under Geometric Feature Nodes setting parameter
                |     value.
                |     True if the Under Geometric Feature Nodes setting parameter is checked and
                |     thus enables 3D annotations to be displayed in the specification tree. This
                |     lets you view 3D annotations under the Part Design or Generative Shape Design
                |     feature nodes to which they are applied.

        :rtype: bool
        """

        return self.fta_infra_setting_att.UnderFeature

    @under_feature.setter
    def under_feature(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.UnderFeature = value

    @property
    def under_set(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UnderSet() As boolean
                | 
                |     Returns or sets the Under Annotation Set Node setting parameter
                |     value.
                |     True if the Under Annotation Set Node setting parameter is checked and thus
                |     enables 3D annotations to be displayed under the annotation set node in the
                |     specification tree. Set this parameter to True only if the Under
                |     View/Annotation Plane Nodes setting parameter managed by UnderView is set to
                |     True.

        :rtype: bool
        """

        return self.fta_infra_setting_att.UnderSet

    @under_set.setter
    def under_set(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.UnderSet = value

    @property
    def under_view(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property UnderView() As boolean
                | 
                |     Returns or sets the Under View/Annotation Plane Nodes setting parameter
                |     value.
                |     True if the Under View/Annotation Plane Nodes setting parameter is checked
                |     and thus enables 3D annotations to be displayed under the view/annotation plane
                |     nodes in the specification tree. This lets you view 3D annotations under the
                |     view node to which they are linked.

        :rtype: bool
        """

        return self.fta_infra_setting_att.UnderView

    @under_view.setter
    def under_view(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.UnderView = value

    @property
    def view_associativity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ViewAssociativity() As boolean
                | 
                |     Returns or sets the View Associativity setting parameter
                |     value.
                |     True if the View Associativity setting parameter is checked and thus
                |     enables the associativity of the view/annotation plane associativity with the
                |     pointed geometrical elements.
                |     Role: The View Associativity setting parameter defines whether the views
                |     created are associative with the geometry. When views are associative to the
                |     geometry, any modification applied to the geometry or to the axis system is
                |     reflected in the view definition.

        :rtype: bool
        """

        return self.fta_infra_setting_att.ViewAssociativity

    @view_associativity.setter
    def view_associativity(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.ViewAssociativity = value

    @property
    def view_profile(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ViewProfile() As boolean
                | 
                |     Returns or sets the View Profile setting parameter value.
                |     True if the View Profile setting parameter is checked and thus enables the
                |     view/annotation plane profile on the part/product to be displayed.

        :rtype: bool
        """

        return self.fta_infra_setting_att.ViewProfile

    @view_profile.setter
    def view_profile(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.ViewProfile = value

    @property
    def view_referential(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ViewReferential() As boolean
                | 
                |     Returns or sets the View Referential setting parameter
                |     value.
                |     True if the View Referential setting parameter is checked and thus enables
                |     the display of the active annotation plane axis system.

        :rtype: bool
        """

        return self.fta_infra_setting_att.ViewReferential

    @view_referential.setter
    def view_referential(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.ViewReferential = value

    @property
    def view_referential_zoomable(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ViewReferentialZoomable() As boolean
                | 
                |     Returns or sets the View Referential Zoomable setting parameter
                |     value.
                |     True if the View Referential Zoomable setting parameter is checked and thus
                |     enables the annotation plane axis to be zoomable.

        :rtype: bool
        """

        return self.fta_infra_setting_att.ViewReferentialZoomable

    @view_referential_zoomable.setter
    def view_referential_zoomable(self, value: bool):
        """
        :param bool value:
        """

        self.fta_infra_setting_att.ViewReferentialZoomable = value

    def get_allow_distortions_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAllowDistortionsInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Allow Distorsions setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetAllowDistortionsInfo(admin_level, o_locked)

    def get_grid_display_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetGridDisplayInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Grid Display setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetGridDisplayInfo(admin_level, o_locked)

    def get_grid_primary_spacing_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetGridPrimarySpacingInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Grid Primary Spacing setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetGridPrimarySpacingInfo(admin_level, o_locked)

    def get_grid_secondary_step_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetGridSecondaryStepInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Grid Secondary Step setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetGridSecondaryStepInfo(admin_level, o_locked)

    def get_grid_snap_point_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetGridSnapPointInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Grid Snap Point setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetGridSnapPointInfo(admin_level, o_locked)

    def get_grid_v_primary_spacing_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetGridVPrimarySpacingInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the GridV Primary Spacing setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetGridVPrimarySpacingInfo(admin_level, o_locked)

    def get_grid_v_secondary_step_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetGridVSecondaryStepInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the GridV Secondary Step setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetGridVSecondaryStepInfo(admin_level, o_locked)

    def get_leader_associativity_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLeaderAssociativityInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Leader Associativity setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetLeaderAssociativityInfo(admin_level, o_locked)

    def get_man_ref_size_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetManRefSizInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Manipulator Reference Size setting
                |     parameter value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetManRefSizInfo(admin_level, o_locked)

    def get_man_zoo_cap_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetManZooCapInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Manipulator Zoom Capability setting
                |     parameter value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetManZooCapInfo(admin_level, o_locked)

    def get_move_after_creation_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetMoveAfterCreationInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Move After Creation setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetMoveAfterCreationInfo(admin_level, o_locked)

    def get_save_in_cgr_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSaveInCGRInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Save In CGR setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetSaveInCGRInfo(admin_level, o_locked)

    def get_standard_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetStandardInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Tolerancing Standard setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetStandardInfo(admin_level, o_locked)

    def get_under_feature_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUnderFeatureInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Under Geometric Feature Nodes setting
                |     parameter value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetUnderFeatureInfo(admin_level, o_locked)

    def get_under_set_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUnderSetInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Under Annotation Set Node setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetUnderSetInfo(admin_level, o_locked)

    def get_under_view_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetUnderViewInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the Under View/Annotation Plane Nodes setting
                |     parameter value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetUnderViewInfo(admin_level, o_locked)

    def get_view_associativity_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetViewAssociativityInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the View Associativity setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetViewAssociativityInfo(admin_level, o_locked)

    def get_view_profile_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetViewProfileInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the View Profile setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetViewProfileInfo(admin_level, o_locked)

    def get_view_referential_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetViewReferentialInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the View Referential setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetViewReferentialInfo(admin_level, o_locked)

    def get_view_referential_zoomable_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetViewReferentialZoomableInfo(CATBSTR AdminLevel,
                | CATBSTR oLocked) As boolean
                | 
                |     Retrieves information about the View Referential Zoomable setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param str admin_level:
        :param str o_locked:
        :rtype: bool
        """
        return self.fta_infra_setting_att.GetViewReferentialZoomableInfo(admin_level, o_locked)

    def set_allow_distortions_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAllowDistortionsLock(boolean iLocked)
                | 
                |     Locks or unlocks the Allow Distorsions setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetAllowDistortionsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_allow_distortions_lock'
        # # vba_code = """
        # # Public Function set_allow_distortions_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetAllowDistortionsLock iLocked
        # #     set_allow_distortions_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_display_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGridDisplayLock(boolean iLocked)
                | 
                |     Locks or unlocks the Grid Display setting parameter value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetGridDisplayLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_display_lock'
        # # vba_code = """
        # # Public Function set_grid_display_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetGridDisplayLock iLocked
        # #     set_grid_display_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_primary_spacing_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGridPrimarySpacingLock(boolean iLocked)
                | 
                |     Locks or unlocks the Grid Primary Spacing setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetGridPrimarySpacingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_primary_spacing_lock'
        # # vba_code = """
        # # Public Function set_grid_primary_spacing_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetGridPrimarySpacingLock iLocked
        # #     set_grid_primary_spacing_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_secondary_step_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGridSecondaryStepLock(boolean iLocked)
                | 
                |     Locks or unlocks the Grid Secondary Step setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetGridSecondaryStepLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_secondary_step_lock'
        # # vba_code = """
        # # Public Function set_grid_secondary_step_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetGridSecondaryStepLock iLocked
        # #     set_grid_secondary_step_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_snap_point_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGridSnapPointLock(boolean iLocked)
                | 
                |     Locks or unlocks the Grid Snap Point setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetGridSnapPointLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_snap_point_lock'
        # # vba_code = """
        # # Public Function set_grid_snap_point_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetGridSnapPointLock iLocked
        # #     set_grid_snap_point_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_v_primary_spacing_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGridVPrimarySpacingLock(boolean iLocked)
                | 
                |     Locks or unlocks the GridV Primary Spacing setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetGridVPrimarySpacingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_v_primary_spacing_lock'
        # # vba_code = """
        # # Public Function set_grid_v_primary_spacing_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetGridVPrimarySpacingLock iLocked
        # #     set_grid_v_primary_spacing_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grid_v_secondary_step_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGridVSecondaryStepLock(boolean iLocked)
                | 
                |     Locks or unlocks the GridV Secondary Step setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetGridVSecondaryStepLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_grid_v_secondary_step_lock'
        # # vba_code = """
        # # Public Function set_grid_v_secondary_step_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetGridVSecondaryStepLock iLocked
        # #     set_grid_v_secondary_step_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_leader_associativity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLeaderAssociativityLock(boolean iLocked)
                | 
                |     Locks or unlocks the Leader Associativity setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetLeaderAssociativityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_leader_associativity_lock'
        # # vba_code = """
        # # Public Function set_leader_associativity_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetLeaderAssociativityLock iLocked
        # #     set_leader_associativity_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_man_ref_size_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetManRefSizLock(boolean iLocked)
                | 
                |     Locks or unlocks the Manipulator Reference Size setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetManRefSizLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_man_ref_siz_lock'
        # # vba_code = """
        # # Public Function set_man_ref_siz_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetManRefSizLock iLocked
        # #     set_man_ref_siz_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_man_zoo_cap_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetManZooCapLock(boolean iLocked)
                | 
                |     Locks or unlocks the Manipulator Zoom Capability setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetManZooCapLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_man_zoo_cap_lock'
        # # vba_code = """
        # # Public Function set_man_zoo_cap_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetManZooCapLock iLocked
        # #     set_man_zoo_cap_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_move_after_creation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMoveAfterCreationLock(boolean iLocked)
                | 
                |     Locks or unlocks the Move After Creation setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetMoveAfterCreationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_move_after_creation_lock'
        # # vba_code = """
        # # Public Function set_move_after_creation_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetMoveAfterCreationLock iLocked
        # #     set_move_after_creation_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_save_in_cgr_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSaveInCGRLock(boolean iLocked)
                | 
                |     Locks or unlocks the Save In CGR setting parameter value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetSaveInCGRLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_save_in_cgr_lock'
        # # vba_code = """
        # # Public Function set_save_in_cgr_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetSaveInCGRLock iLocked
        # #     set_save_in_cgr_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_standard_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStandardLock(boolean iLocked)
                | 
                |     Locks or unlocks the Tolerancing Standard setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetStandardLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_standard_lock'
        # # vba_code = """
        # # Public Function set_standard_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetStandardLock iLocked
        # #     set_standard_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_under_feature_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUnderFeatureLock(boolean iLocked)
                | 
                |     Locks or unlocks the Under Geometric Feature Nodes setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetUnderFeatureLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_under_feature_lock'
        # # vba_code = """
        # # Public Function set_under_feature_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetUnderFeatureLock iLocked
        # #     set_under_feature_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_under_set_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUnderSetLock(boolean iLocked)
                | 
                |     Locks or unlocks the Under Annotation Set Node setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetUnderSetLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_under_set_lock'
        # # vba_code = """
        # # Public Function set_under_set_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetUnderSetLock iLocked
        # #     set_under_set_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_under_view_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetUnderViewLock(boolean iLocked)
                | 
                |     Locks or unlocks the Under View/Annotation Plane Nodes setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetUnderViewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_under_view_lock'
        # # vba_code = """
        # # Public Function set_under_view_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetUnderViewLock iLocked
        # #     set_under_view_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_view_associativity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetViewAssociativityLock(boolean iLocked)
                | 
                |     Locks or unlocks the View Associativity setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetViewAssociativityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_view_associativity_lock'
        # # vba_code = """
        # # Public Function set_view_associativity_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetViewAssociativityLock iLocked
        # #     set_view_associativity_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_view_profile_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetViewProfileLock(boolean iLocked)
                | 
                |     Locks or unlocks the View Profile setting parameter value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetViewProfileLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_view_profile_lock'
        # # vba_code = """
        # # Public Function set_view_profile_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetViewProfileLock iLocked
        # #     set_view_profile_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_view_referential_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetViewReferentialLock(boolean iLocked)
                | 
                |     Locks or unlocks the View Referential setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetViewReferentialLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_view_referential_lock'
        # # vba_code = """
        # # Public Function set_view_referential_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetViewReferentialLock iLocked
        # #     set_view_referential_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_view_referential_zoomable_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetViewReferentialZoomableLock(boolean iLocked)
                | 
                |     Locks or unlocks the View Referential Zoomable setting parameter
                |     value.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.fta_infra_setting_att.SetViewReferentialZoomableLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_view_referential_zoomable_lock'
        # # vba_code = """
        # # Public Function set_view_referential_zoomable_lock(fta_infra_setting_att)
        # #     Dim iLocked (2)
        # #     fta_infra_setting_att.SetViewReferentialZoomableLock iLocked
        # #     set_view_referential_zoomable_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'FtaInfraSettingAtt(name="{self.name}")'
