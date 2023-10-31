#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class N4DNavigatorSettingAtt(SettingController):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         N4DNavigatorSettingAtt
                | 
                | Interface to handle the settings of the DMU Navigator
                | workbench.
                | 
                | 
                | The different settings are:
                | 
                | DMUClashPreview:
                | Display of the preview viewer when editing an interference.
                | 
                | DMUDistancePreview:
                | Display of the preview viewer when editing a distance.
                | 
                | DMUGroupPreview:
                | Display of the preview viewer when editing a group.
                | 
                | DMUSectionPreview:
                | Display of the preview viewer when editing a section.
                | 
                | DMUShuttlePreview:
                | Display of the preview viewer when editing a shuttle.
                | 
                | DMUThicknessPreview:
                | Display of the preview viewer for the thickness command.
                | 
                | DMUOffsetPreview:
                | Display of the preview viewer for the offset command.
                | 
                | DMUSweptVolPreview:
                | Display of the preview viewer for the swept volume command.
                | 
                | DMUSilhouettePreview:
                | Display of the preview viewer for the silhouette command.
                | 
                | DMUWrappingPreview:
                | Display of the preview viewer for the wrapping command.
                | 
                | DMUFreeSpacePreview:
                | Display of the preview viewer for the free space command.
                | 
                | DMUSimplifPreview:
                | Display of the preview viewer for the simplification command.
                | 
                | DMUVibrationVolPreview:
                | Display of the preview viewer for the vibration volume
                | command.
                | 
                | DMUCut3DPreview:
                | Display of the preview viewer for the 3D cut command.
                | 
                | DMUMergerPreview:
                | Display of the preview viewer for the merger command.
                | 
                | NumUrlName:
                | Display of the hyperlink name.
                | 
                | MarkerAutoUpdate:
                | Update on product structure modifications and scenes
                | activation.
                | 
                | MarkerDefaultsColor:
                | Default color of an annotation.
                | 
                | SceneDefaultsColor:
                | Default background color for scene environment.
                | 
                | MarkerTextColor:
                | Default color of a text annotation.
                | 
                | MarkerDefaultsWeight:
                | Default weight value of an annotation.
                | 
                | MarkerDefaultsDashed:
                | Default dashed value of an annotation.
                | 
                | MarkerDefaultsSize:
                | Default size value of an annotation.
                | 
                | MarkerDefaultsFont:
                | Default font of an annotation.
                | 
                | MarkerTextDashed:
                | Default dashed value of a text annotation.
                | 
                | MarkerTextWeight:
                | Default weight value of a text annotation.
                | 
                | PublishAutoLaunchBrowser:
                | Automatic launching of publish results in a browser.
                | 
                | Marker2DAutoNaming:
                | Automatically use a Part's name as the default for the creation of text
                | annotations.
                | 
                | Marker3DAutoNaming:
                | Activation of the mechanism that enables to transform temporary markers into
                | persistent 3D annotations.
                | 
                | DMUReviewName:
                | The desired default name for DMU Reviews
                | 
                | ForceVoxel:
                | Force users of the Spatial Query command to use the defined Released
                | Accuracy.
                | 
                | ClearanceVoxel:
                | Definition of the Clearance value.
                | 
                | ForceClearanceVoxel:
                | Force users of the Spatial Query command to use the defined Clearance
                | value.
                | 
                | InsertMode:
                | Mode for the Import applicative data command.
                | 
                | DMUGroupPreviewHiddenObjectsDisplayMode:
                | Display mode for hidden objects of a DMU Group in its preview: visualized as in
                | main 3D viewer or visualized with customized graphic
                | properties
                | 
                | DMUGroupPreviewHiddenObjectsColor:
                | Color for hidden objects in DMU Group Preview.
                | 
                | DMUGroupPreviewHiddenObjectsOpacity:
                | Opacity for hidden objects in DMU Group Preview.
                | 
                | DMUGroupPreviewHiddenObjectsLowIntMode:
                | Hidden objects are low intensified or not in DMU Group
                | Preview.
                | 
                | DMUGroupPreviewHiddenObjectsPickMode:
                | Hidden objects can be picked or not in DMU Group Preview.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.n_4d_navigator_setting_att = com_object

    @property
    def clearance_voxel(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ClearanceVoxel() As float
                | 
                |     Returns or sets the clearance value (oValue the clearance value in mm).

        :rtype: float
        """

        return self.n_4d_navigator_setting_att.ClearanceVoxel

    @clearance_voxel.setter
    def clearance_voxel(self, value: float):
        """
        :param float value:
        """

        self.n_4d_navigator_setting_att.ClearanceVoxel = value

    @property
    def dmu_clash_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUClashPreview() As boolean
                | 
                |     Returns or sets the preview activation state for Interference (TRUE the
                |     preview window is automatically displayed, FALSE the preview window is not
                |     displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUClashPreview

    @dmu_clash_preview.setter
    def dmu_clash_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUClashPreview = value

    @property
    def dmu_cut_3d_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUCut3DPreview() As boolean
                | 
                |     Returns or sets the preview activation state for 3D Cut (TRUE the preview
                |     window is automatically displayed, FALSE the preview window is not displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUCut3DPreview

    @dmu_cut_3d_preview.setter
    def dmu_cut_3d_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUCut3DPreview = value

    @property
    def dmu_distance_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUDistancePreview() As boolean
                | 
                |     Returns or sets the preview activation state for Distance (TRUE the preview
                |     window is automatically displayed, FALSE the preview window is not displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUDistancePreview

    @dmu_distance_preview.setter
    def dmu_distance_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUDistancePreview = value

    @property
    def dmu_free_space_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUFreeSpacePreview() As boolean
                | 
                |     Returns or sets the preview activation state for Free Space (TRUE the
                |     preview window is automatically displayed, FALSE the preview window is not
                |     displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUFreeSpacePreview

    @dmu_free_space_preview.setter
    def dmu_free_space_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUFreeSpacePreview = value

    @property
    def dmu_group_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUGroupPreview() As boolean
                | 
                |     Returns or sets the preview activation state for Group (TRUE the preview
                |     window is automatically displayed, FALSE the preview window is not displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUGroupPreview

    @dmu_group_preview.setter
    def dmu_group_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUGroupPreview = value

    @property
    def dmu_group_preview_hidden_objects_display_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUGroupPreviewHiddenObjectsDisplayMode() As
                | CatDMUGroupPreviewHiddenObjectsDisplayMode
                | 
                |     Returns or sets the mode for the display of hidden objects in DMU Group
                |     Preview.

        :rtype: enum cat_dmu_group_preview_hidden_objects_display_mode
        :rtype: int
        """

        return self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsDisplayMode

    @dmu_group_preview_hidden_objects_display_mode.setter
    def dmu_group_preview_hidden_objects_display_mode(self, value: int):
        """
        :param int value: enum cat_dmu_group_preview_hidden_objects_display_mode
        """

        self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsDisplayMode = value

    @property
    def dmu_group_preview_hidden_objects_low_int(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUGroupPreviewHiddenObjectsLowInt() As boolean
                | 
                |     Returns or sets the Low Intensity mode for the display of hidden objects in
                |     DMU Group Preview.

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsLowInt

    @dmu_group_preview_hidden_objects_low_int.setter
    def dmu_group_preview_hidden_objects_low_int(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsLowInt = value

    @property
    def dmu_group_preview_hidden_objects_opacity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUGroupPreviewHiddenObjectsOpacity() As long
                | 
                |     Returns or sets the opacity for the display of hidden objects in DMU Group
                |     Preview.

        :rtype: int
        """

        return self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsOpacity

    @dmu_group_preview_hidden_objects_opacity.setter
    def dmu_group_preview_hidden_objects_opacity(self, value: int):
        """
        :param int value:
        """

        self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsOpacity = value

    @property
    def dmu_group_preview_hidden_objects_pick(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUGroupPreviewHiddenObjectsPick() As boolean
                | 
                |     Returns or sets the pick mode for the display of hidden objects in DMU
                |     Group Preview.

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsPick

    @dmu_group_preview_hidden_objects_pick.setter
    def dmu_group_preview_hidden_objects_pick(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUGroupPreviewHiddenObjectsPick = value

    @property
    def dmu_merger_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUMergerPreview() As boolean
                | 
                |     Returns or sets the preview activation state for Merger (TRUE the preview
                |     window is automatically displayed, FALSE the preview window is not displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUMergerPreview

    @dmu_merger_preview.setter
    def dmu_merger_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUMergerPreview = value

    @property
    def dmu_offset_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUOffsetPreview() As boolean
                | 
                |     Returns or sets the preview activation state for Offset (TRUE the preview
                |     window is automatically displayed, FALSE the preview window is not displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUOffsetPreview

    @dmu_offset_preview.setter
    def dmu_offset_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUOffsetPreview = value

    @property
    def dmu_review_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUReviewName() As CATBSTR
                | 
                |     Returns or sets the default name for the DMU Reviews (oValue, the DMU
                |     Review name).

        :rtype: str
        """

        return self.n_4d_navigator_setting_att.DMUReviewName

    @dmu_review_name.setter
    def dmu_review_name(self, value: str):
        """
        :param str value:
        """

        self.n_4d_navigator_setting_att.DMUReviewName = value

    @property
    def dmu_section_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUSectionPreview() As boolean
                | 
                |     Returns or sets the preview activation state for Section (TRUE the preview
                |     window is automatically displayed, FALSE the preview window is not displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUSectionPreview

    @dmu_section_preview.setter
    def dmu_section_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUSectionPreview = value

    @property
    def dmu_shuttle_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUShuttlePreview() As boolean
                | 
                |     Returns or sets the preview activation state for Shuttle (TRUE the preview
                |     window is automatically displayed, FALSE the preview window is not displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUShuttlePreview

    @dmu_shuttle_preview.setter
    def dmu_shuttle_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUShuttlePreview = value

    @property
    def dmu_silhouette_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUSilhouettePreview() As boolean
                | 
                |     Returns or sets the preview activation state for Silhouette (TRUE the
                |     preview window is automatically displayed, FALSE the preview window is not
                |     displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUSilhouettePreview

    @dmu_silhouette_preview.setter
    def dmu_silhouette_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUSilhouettePreview = value

    @property
    def dmu_simplif_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUSimplifPreview() As boolean
                | 
                |     Returns or sets the preview activation state for Simplification (TRUE the
                |     preview window is automatically displayed, FALSE the preview window is not
                |     displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUSimplifPreview

    @dmu_simplif_preview.setter
    def dmu_simplif_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUSimplifPreview = value

    @property
    def dmu_swept_vol_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUSweptVolPreview() As boolean
                | 
                |     Returns or sets the preview activation state for Swept Volume (TRUE the
                |     preview window is automatically displayed, FALSE the preview window is not
                |     displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUSweptVolPreview

    @dmu_swept_vol_preview.setter
    def dmu_swept_vol_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUSweptVolPreview = value

    @property
    def dmu_thickness_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUThicknessPreview() As boolean
                | 
                |     Returns or sets the preview activation state for Thickness (TRUE the
                |     preview window is automatically displayed, FALSE the preview window is not
                |     displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUThicknessPreview

    @dmu_thickness_preview.setter
    def dmu_thickness_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUThicknessPreview = value

    @property
    def dmu_vibration_vol_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUVibrationVolPreview() As boolean
                | 
                |     Returns or sets the preview activation state for Vibration volume (TRUE the
                |     preview window is automatically displayed, FALSE the preview window is not
                |     displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUVibrationVolPreview

    @dmu_vibration_vol_preview.setter
    def dmu_vibration_vol_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUVibrationVolPreview = value

    @property
    def dmu_wrapping_preview(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DMUWrappingPreview() As boolean
                | 
                |     Returns or sets the preview activation state for Wrapping (TRUE the preview
                |     window is automatically displayed, FALSE the preview window is not displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.DMUWrappingPreview

    @dmu_wrapping_preview.setter
    def dmu_wrapping_preview(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.DMUWrappingPreview = value

    @property
    def force_clearance_voxel(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ForceClearanceVoxel() As boolean
                | 
                |     Returns or sets the activation state for the use of the clearance value
                |     (TRUE the clearance value is used, FALSE the clearance value is not used);

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.ForceClearanceVoxel

    @force_clearance_voxel.setter
    def force_clearance_voxel(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.ForceClearanceVoxel = value

    @property
    def force_voxel(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ForceVoxel() As boolean
                | 
                |     Returns or sets the activation state for the use of the Released accuracy
                |     value (TRUE the released accuracy value is used, FALSE the released accuracy
                |     value is not used);

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.ForceVoxel

    @force_voxel.setter
    def force_voxel(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.ForceVoxel = value

    @property
    def insert_level(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InsertLevel() As boolean
                | 
                |     Returns or sets the level for the Import Applicative Data command
                |     (True : at highest review level, False : in current review).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.InsertLevel

    @insert_level.setter
    def insert_level(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.InsertLevel = value

    @property
    def insert_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InsertMode() As CatSacSettingsEnum
                | 
                |     Returns or sets the mode for the Import Applicative Data command
                |     (CatSacSettingsEnumNoInsert no import of applicative data,
                |     CatSacSettingsEnumAutomatic the import of applicative is automatic,
                |     CatSacSettingsEnumUserPrompt the user can select the applicative data to
                |     import).

        :return: enum cat_sac_settings_enum
        :rtype: int
        """

        return self.n_4d_navigator_setting_att.InsertMode

    @insert_mode.setter
    def insert_mode(self, value: int):
        """
        :param int value: enum cat_sac_settings_enum
        """

        self.n_4d_navigator_setting_att.InsertMode = value

    @property
    def marker_2d_auto_naming(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Marker2DAutoNaming() As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.get_Marker2DAutoNaming This method will be replaced by
                |         MarkerSettingAtt.put_Marker2DAutoNaming Returns or sets the activation state
                |         for 2D annotations automatic naming (TRUE naming is automatic, FALSE the naming
                |         is not automatic).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.Marker2DAutoNaming

    @marker_2d_auto_naming.setter
    def marker_2d_auto_naming(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.Marker2DAutoNaming = value

    @property
    def marker_3d_auto_naming(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Marker3DAutoNaming() As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.get_Marker3DAutoNaming This method will be replaced by
                |         MarkerSettingAtt.put_Marker3DAutoNaming Returns or sets the activation state
                |         for 3D annotations automatic naming (TRUE naming is automatic, FALSE the naming
                |         is not automatic).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.Marker3DAutoNaming

    @marker_3d_auto_naming.setter
    def marker_3d_auto_naming(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.Marker3DAutoNaming = value

    @property
    def marker_auto_update(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerAutoUpdate() As boolean
                | 
                |     Returns or sets the activation of the automatic update on product structure
                |     modification (TRUE update is done automatically, FALSE update is done
                |     manually).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.MarkerAutoUpdate

    @marker_auto_update.setter
    def marker_auto_update(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.MarkerAutoUpdate = value

    @property
    def marker_defaults_dashed(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerDefaultsDashed() As long
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.get_MarkerDefaultsDashed This method will be replaced by
                |         MarkerSettingAtt.put_MarkerDefaultsDashed Returns or sets the default dashed
                |         value of an annotation (oValue the dashed value).

        :rtype: int
        """

        return self.n_4d_navigator_setting_att.MarkerDefaultsDashed

    @marker_defaults_dashed.setter
    def marker_defaults_dashed(self, value: int):
        """
        :param int value:
        """

        self.n_4d_navigator_setting_att.MarkerDefaultsDashed = value

    @property
    def marker_defaults_font(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerDefaultsFont() As CATBSTR
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.get_MarkerTextDefaultsFont2D This method will be replaced by
                |         MarkerSettingAtt.put_MarkerTextDefaultsFont2D Returns or sets the default font
                |         of an annotation (oValue the font name).

        :rtype: str
        """

        return self.n_4d_navigator_setting_att.MarkerDefaultsFont

    @marker_defaults_font.setter
    def marker_defaults_font(self, value: str):
        """
        :param str value:
        """

        self.n_4d_navigator_setting_att.MarkerDefaultsFont = value

    @property
    def marker_defaults_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerDefaultsSize() As long
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.get_MarkerTextDefaultsSize2D This method will be replaced by
                |         MarkerSettingAtt.put_MarkerTextDefaultsSize2D Returns or sets the default size
                |         value of an annotation (oValue the size value)..

        :rtype: int
        """

        return self.n_4d_navigator_setting_att.MarkerDefaultsSize

    @marker_defaults_size.setter
    def marker_defaults_size(self, value: int):
        """
        :param int value:
        """

        self.n_4d_navigator_setting_att.MarkerDefaultsSize = value

    @property
    def marker_defaults_weight(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerDefaultsWeight() As long
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.get_MarkerDefaultsWeight This method will be replaced by
                |         MarkerSettingAtt.put_MarkerDefaultsWeight Returns or sets the default weight
                |         value of an annotation (oValue the weight value).

        :rtype: int
        """

        return self.n_4d_navigator_setting_att.MarkerDefaultsWeight

    @marker_defaults_weight.setter
    def marker_defaults_weight(self, value: int):
        """
        :param int value:
        """

        self.n_4d_navigator_setting_att.MarkerDefaultsWeight = value

    @property
    def marker_text_dashed(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerTextDashed() As long
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.get_MarkerTextDashed2D This method will be replaced by
                |         MarkerSettingAtt.put_MarkerTextDashed2D Returns or sets the default dashed
                |         value of a text annotation (oValue the dashed value).

        :rtype: int
        """

        return self.n_4d_navigator_setting_att.MarkerTextDashed

    @marker_text_dashed.setter
    def marker_text_dashed(self, value: int):
        """
        :param int value:
        """

        self.n_4d_navigator_setting_att.MarkerTextDashed = value

    @property
    def marker_text_weight(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MarkerTextWeight() As long
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.get_MarkerTextWeight2D This method will be replaced by
                |         MarkerSettingAtt.put_MarkerTextWeight2D Returns or sets the default weight
                |         value of a text annotation (oValue the weight value).

        :rtype: int
        """

        return self.n_4d_navigator_setting_att.MarkerTextWeight

    @marker_text_weight.setter
    def marker_text_weight(self, value: int):
        """
        :param int value:
        """

        self.n_4d_navigator_setting_att.MarkerTextWeight = value

    @property
    def num_url_name(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NumUrlName() As boolean
                | 
                |     Returns or sets the name activation state for Hyperlink (TRUE the hyperlink
                |     name is displayed, FALSE the hyperlink name is not displayed).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.NumUrlName

    @num_url_name.setter
    def num_url_name(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.NumUrlName = value

    @property
    def publish_auto_launch_browser(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PublishAutoLaunchBrowser() As boolean
                | 
                |     Returns or sets the activation state of the automatic launching of the
                |     publish browser (TRUE the publish browser is automatically opened, FALSE the
                |     publish browser is not automatically opened).

        :rtype: bool
        """

        return self.n_4d_navigator_setting_att.PublishAutoLaunchBrowser

    @publish_auto_launch_browser.setter
    def publish_auto_launch_browser(self, value: bool):
        """
        :param bool value:
        """

        self.n_4d_navigator_setting_att.PublishAutoLaunchBrowser = value

    def get_clearance_voxel_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetClearanceVoxelInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ClearanceVoxel
                |     parameter.
                |     Role:Retrieves the state of the ClearanceVoxel parameter in the current
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
        return self.n_4d_navigator_setting_att.GetClearanceVoxelInfo(io_admin_level, io_locked)

    def get_dmu_clash_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUClashPreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUClashPreview
                |     parameter.
                |     Role:Retrieves the state of the DMUClashPreview parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUClashPreviewInfo(io_admin_level, io_locked)

    def get_dmu_cut_3d_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUCut3DPreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUCut3DPreview
                |     parameter.
                |     Role:Retrieves the state of the DMUCut3DPreview parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUCut3DPreviewInfo(io_admin_level, io_locked)

    def get_dmu_distance_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUDistancePreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUDistancePreview
                |     parameter.
                |     Role:Retrieves the state of the DMUDistancePreview parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUDistancePreviewInfo(io_admin_level, io_locked)

    def get_dmu_free_space_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUFreeSpacePreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUFreeSpacePreview
                |     parameter.
                |     Role:Retrieves the state of the DMUFreeSpacePreview parameter in the
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
        return self.n_4d_navigator_setting_att.GetDMUFreeSpacePreviewInfo(io_admin_level, io_locked)

    def get_dmu_group_preview_hidden_objects_color(self, o_red: int, o_green: int, o_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetDMUGroupPreviewHiddenObjectsColor(long oRed,
                | long oGreen,
                | long oBlue)
                | 
                |     Returns the color for the display of hidden objects in DMU Group Preview.

        :param int o_red:
        :param int o_green:
        :param int o_blue:
        :rtype: None
        """
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsColor(o_red, o_green, o_blue)

    def get_dmu_group_preview_hidden_objects_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUGroupPreviewHiddenObjectsColorInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     DMUGroupPreviewHiddenObjectsColor parameter.
                |     Role:Retrieves the state of the DMUGroupPreviewHiddenObjectsColor parameter
                |     in the current environment.
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
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsColorInfo(io_admin_level, io_locked)

    def get_dmu_group_preview_hidden_objects_display_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUGroupPreviewHiddenObjectsDisplayModeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     DMUGroupPreviewHiddenObjectsDisplayMode parameter.
                |     Role:Retrieves the state of the DMUGroupPreviewHiddenObjectsDisplayMode
                |     parameter in the current environment.
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
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsDisplayModeInfo(io_admin_level, io_locked)

    def get_dmu_group_preview_hidden_objects_low_int_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUGroupPreviewHiddenObjectsLowIntInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     DMUGroupPreviewHiddenObjectsLowInt parameter.
                |     Role:Retrieves the state of the DMUGroupPreviewHiddenObjectsLowInt
                |     parameter in the current environment.
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
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsLowIntInfo(io_admin_level, io_locked)

    def get_dmu_group_preview_hidden_objects_opacity_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUGroupPreviewHiddenObjectsOpacityInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     DMUGroupPreviewHiddenObjectsOpacity parameter.
                |     Role:Retrieves the state of the DMUGroupPreviewHiddenObjectsOpacity
                |     parameter in the current environment.
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
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsOpacityInfo(io_admin_level, io_locked)

    def get_dmu_group_preview_hidden_objects_pick_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUGroupPreviewHiddenObjectsPickInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUGroupPreviewHiddenObjectsPick
                |     parameter.
                |     Role:Retrieves the state of the DMUGroupPreviewHiddenObjectsPick parameter
                |     in the current environment.
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
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewHiddenObjectsPickInfo(io_admin_level, io_locked)

    def get_dmu_group_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUGroupPreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUGroupPreview
                |     parameter.
                |     Role:Retrieves the state of the DMUGroupPreview parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUGroupPreviewInfo(io_admin_level, io_locked)

    def get_dmu_merger_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUMergerPreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUMergerPreview
                |     parameter.
                |     Role:Retrieves the state of the DMUMergerPreview parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUMergerPreviewInfo(io_admin_level, io_locked)

    def get_dmu_offset_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUOffsetPreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUOffsetPreview
                |     parameter.
                |     Role:Retrieves the state of the DMUOffsetPreview parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUOffsetPreviewInfo(io_admin_level, io_locked)

    def get_dmu_review_name_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUReviewNameInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUReviewName
                |     parameter.
                |     Role:Retrieves the state of the DMUReviewName parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUReviewNameInfo(io_admin_level, io_locked)

    def get_dmu_section_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUSectionPreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUSectionPreview
                |     parameter.
                |     Role:Retrieves the state of the DMUSectionPreview parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUSectionPreviewInfo(io_admin_level, io_locked)

    def get_dmu_shuttle_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUShuttlePreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUShuttlePreview
                |     parameter.
                |     Role:Retrieves the state of the DMUShuttlePreview parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUShuttlePreviewInfo(io_admin_level, io_locked)

    def get_dmu_silhouette_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUSilhouettePreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUSilhouettePreview
                |     parameter.
                |     Role:Retrieves the state of the DMUSilhouettePreview parameter in the
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
        return self.n_4d_navigator_setting_att.GetDMUSilhouettePreviewInfo(io_admin_level, io_locked)

    def get_dmu_simplif_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUSimplifPreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUSimplifPreview
                |     parameter.
                |     Role:Retrieves the state of the DMUSimplifPreview parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUSimplifPreviewInfo(io_admin_level, io_locked)

    def get_dmu_swept_vol_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUSweptVolPreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUSweptVolPreview
                |     parameter.
                |     Role:Retrieves the state of the DMUSweptVolPreview parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUSweptVolPreviewInfo(io_admin_level, io_locked)

    def get_dmu_thickness_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUThicknessPreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUThicknessPreview
                |     parameter.
                |     Role:Retrieves the state of the DMUThicknessPreview parameter in the
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
        return self.n_4d_navigator_setting_att.GetDMUThicknessPreviewInfo(io_admin_level, io_locked)

    def get_dmu_vibration_vol_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUVibrationVolPreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUVibrationVolPreview
                |     parameter.
                |     Role:Retrieves the state of the DMUVibrationVolPreview parameter in the
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
        return self.n_4d_navigator_setting_att.GetDMUVibrationVolPreviewInfo(io_admin_level, io_locked)

    def get_dmu_wrapping_preview_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDMUWrappingPreviewInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DMUWrappingPreview
                |     parameter.
                |     Role:Retrieves the state of the DMUWrappingPreview parameter in the current
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
        return self.n_4d_navigator_setting_att.GetDMUWrappingPreviewInfo(io_admin_level, io_locked)

    def get_force_clearance_voxel_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetForceClearanceVoxelInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ForceClearanceVoxel
                |     parameter.
                |     Role:Retrieves the state of the ForceClearanceVoxel parameter in the
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
        return self.n_4d_navigator_setting_att.GetForceClearanceVoxelInfo(io_admin_level, io_locked)

    def get_force_voxel_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetForceVoxelInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ForceVoxel
                |     parameter.
                |     Role:Retrieves the state of the ForceVoxel parameter in the current
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
        return self.n_4d_navigator_setting_att.GetForceVoxelInfo(io_admin_level, io_locked)

    def get_insert_level_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetInsertLevelInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the InsertLevel
                |     parameter.
                |     Role:Retrieves the state of the InsertLevel parameter in the current
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
        return self.n_4d_navigator_setting_att.GetInsertLevelInfo(io_admin_level, io_locked)

    def get_insert_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetInsertModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the InsertMode
                |     parameter.
                |     Role:Retrieves the state of the InsertMode parameter in the current
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
        return self.n_4d_navigator_setting_att.GetInsertModeInfo(io_admin_level, io_locked)

    def get_marker_2d_auto_naming_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarker2DAutoNamingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.GetMarker2DAutoNamingInfo Retrieves environment informations
                |         for the Marker2DAutoNaming parameter.
                |         Role:Retrieves the state of the Marker2DAutoNaming parameter in the
                |         current environment. 
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
        return self.n_4d_navigator_setting_att.GetMarker2DAutoNamingInfo(io_admin_level, io_locked)

    def get_marker_3d_auto_naming_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarker3DAutoNamingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.GetMarker3DAutoNamingInfo Retrieves environment informations
                |         for the Marker3DAutoNaming parameter.
                |         Role:Retrieves the state of the Marker3DAutoNaming parameter in the
                |         current environment. 
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
        return self.n_4d_navigator_setting_att.GetMarker3DAutoNamingInfo(io_admin_level, io_locked)

    def get_marker_auto_update_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerAutoUpdateInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the MarkerAutoUpdate
                |     parameter.
                |     Role:Retrieves the state of the MarkerAutoUpdate parameter in the current
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
        return self.n_4d_navigator_setting_att.GetMarkerAutoUpdateInfo(io_admin_level, io_locked)

    def get_marker_defaults_color(self, o_red: int, o_green: int, o_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetMarkerDefaultsColor(long oRed,
                | long oGreen,
                | long oBlue)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.GetMarkerDefaultsColor Returns the default color of an
                |         annotation (oRed, oGreen, oBlue: RGB values of the color).

        :param int o_red:
        :param int o_green:
        :param int o_blue:
        :rtype: None
        """
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsColor(o_red, o_green, o_blue)

    def get_marker_defaults_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerDefaultsColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.GetMarkerDefaultsColorInfo Retrieves environment informations
                |         for the MarkerDefaultsColor parameter.
                |         Role:Retrieves the state of the MarkerDefaultsColor parameter in the
                |         current environment. 
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
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsColorInfo(io_admin_level, io_locked)

    def get_marker_defaults_dashed_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerDefaultsDashedInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.GetMarkerDefaultsDashedInfo Retrieves environment informations
                |         for the MarkerDefaultsDashed parameter.
                |         Role:Retrieves the state of the MarkerDefaultsDashed parameter in the
                |         current environment. 
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
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsDashedInfo(io_admin_level, io_locked)

    def get_marker_defaults_font_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerDefaultsFontInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.GetMarkerDefaultsFont2DInfo Retrieves environment informations
                |         for the MarkerDefaultsFont parameter.
                |         Role:Retrieves the state of the MarkerDefaultsFont parameter in the
                |         current environment. 
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
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsFontInfo(io_admin_level, io_locked)

    def get_marker_defaults_size_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerDefaultsSizeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by CATIAmarkerSettingAtt Retrieves
                |         environment informations for the MarkerDefaultsSize
                |         parameter.
                |         Role:Retrieves the state of the MarkerDefaultsSize parameter in the
                |         current environment. 
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
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsSizeInfo(io_admin_level, io_locked)

    def get_marker_defaults_weight_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerDefaultsWeightInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.GetMarkerDefaultsWeightInfo Retrieves environment informations
                |         for the MarkerDefaultsWeight parameter.
                |         Role:Retrieves the state of the MarkerDefaultsWeight parameter in the
                |         current environment. 
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
        return self.n_4d_navigator_setting_att.GetMarkerDefaultsWeightInfo(io_admin_level, io_locked)

    def get_marker_text_color(self, o_red: int, o_green: int, o_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetMarkerTextColor(long oRed,
                | long oGreen,
                | long oBlue)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.GetMarkerTextColor2DInfo Returns the default color of a text
                |         annotation (oRed, oGreen, oBlue: RGB values of the color).

        :param int o_red:
        :param int o_green:
        :param int o_blue:
        :rtype: None
        """
        return self.n_4d_navigator_setting_att.GetMarkerTextColor(o_red, o_green, o_blue)

    def get_marker_text_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.GetMarkerTextColor2DInfo Retrieves environment informations
                |         for the MarkerTextColor parameter.
                |         Role:Retrieves the state of the MarkerTextColor parameter in the
                |         current environment. 
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
        return self.n_4d_navigator_setting_att.GetMarkerTextColorInfo(io_admin_level, io_locked)

    def get_marker_text_dashed_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextDashedInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.GetMarkerTextDashed2DInfo Retrieves environment informations
                |         for the MarkerTextDashed parameter.
                |         Role:Retrieves the state of the MarkerTextDashed parameter in the
                |         current environment. 
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
        return self.n_4d_navigator_setting_att.GetMarkerTextDashedInfo(io_admin_level, io_locked)

    def get_marker_text_weight_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMarkerTextWeightInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.GetMarkerTextWeight2DInfo Retrieves environment informations
                |         for the MarkerTextWeight parameter.
                |         Role:Retrieves the state of the MarkerTextWeight parameter in the
                |         current environment. 
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
        return self.n_4d_navigator_setting_att.GetMarkerTextWeightInfo(io_admin_level, io_locked)

    def get_num_url_name_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNumUrlNameInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the NumUrlName
                |     parameter.
                |     Role:Retrieves the state of the NumUrlName parameter in the current
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
        return self.n_4d_navigator_setting_att.GetNumUrlNameInfo(io_admin_level, io_locked)

    def get_publish_auto_launch_browser_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPublishAutoLaunchBrowserInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the PublishAutoLaunchBrowser
                |     parameter.
                |     Role:Retrieves the state of the PublishAutoLaunchBrowser parameter in the
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
        return self.n_4d_navigator_setting_att.GetPublishAutoLaunchBrowserInfo(io_admin_level, io_locked)

    def get_scene_defaults_color(self, o_r: int, o_g: int, o_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSceneDefaultsColor(long oR,
                | long oG,
                | long oB)
                | 
                |     Returns the scene background color (oRed, oGreen, oBlue: RGB values of the
                |     color).

        :param int o_r:
        :param int o_g:
        :param int o_b:
        :rtype: None
        """
        return self.n_4d_navigator_setting_att.GetSceneDefaultsColor(o_r, o_g, o_b)

    def get_scene_defaults_color_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetSceneDefaultsColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SceneDefaultsColor
                |     parameter.
                |     Role:Retrieves the state of the SceneDefaultsColor parameter in the current
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
        return self.n_4d_navigator_setting_att.GetSceneDefaultsColorInfo(io_admin_level, io_locked)

    def set_clearance_voxel_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetClearanceVoxelLock(boolean iLocked)
                | 
                |     Locks or unlocks the ClearanceVoxel parameter.
                |     Role:Locks or unlocks the ClearanceVoxel parameter if it is possible in the
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
        return self.n_4d_navigator_setting_att.SetClearanceVoxelLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_clearance_voxel_lock'
        # # vba_code = """
        # # Public Function set_clearance_voxel_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetClearanceVoxelLock iLocked
        # #     set_clearance_voxel_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_clash_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUClashPreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUClashPreview parameter.
                |     Role:Locks or unlocks the DMUClashPreview parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetDMUClashPreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_clash_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_clash_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUClashPreviewLock iLocked
        # #     set_dmu_clash_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_cut_3d_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUCut3DPreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUCut3DPreview parameter.
                |     Role:Locks or unlocks the DMUCut3DPreview parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetDMUCut3DPreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_cut_3d_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_cut_3d_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUCut3DPreviewLock iLocked
        # #     set_dmu_cut_3d_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_distance_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUDistancePreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUDistancePreview parameter.
                |     Role:Locks or unlocks the DMUDistancePreview parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetDMUDistancePreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_distance_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_distance_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUDistancePreviewLock iLocked
        # #     set_dmu_distance_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_free_space_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUFreeSpacePreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUFreeSpacePreview parameter.
                |     Role:Locks or unlocks the DMUFreeSpacePreview parameter if it is possible
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
        return self.n_4d_navigator_setting_att.SetDMUFreeSpacePreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_free_space_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_free_space_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUFreeSpacePreviewLock iLocked
        # #     set_dmu_free_space_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_group_preview_hidden_objects_color(self, i_red: int, i_green: int, i_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUGroupPreviewHiddenObjectsColor(long iRed,
                | long iGreen,
                | long iBlue)
                | 
                |     Sets the color for the display of hidden objects in DMU Group Preview.

        :param int i_red:
        :param int i_green:
        :param int i_blue:
        :rtype: None
        """
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsColor(i_red, i_green, i_blue)

    def set_dmu_group_preview_hidden_objects_color_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUGroupPreviewHiddenObjectsColorLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the DMUGroupPreviewHiddenObjectsColor
                |     parameter.
                |     Role:Locks or unlocks the DMUGroupPreviewHiddenObjectsColor parameter if it
                |     is possible in the current administrative context. In user mode this method
                |     will always return E_FAIL.
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
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_group_preview_hidden_objects_color_lock'
        # # vba_code = """
        # # Public Function set_dmu_group_preview_hidden_objects_color_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsColorLock iLocked
        # #     set_dmu_group_preview_hidden_objects_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_group_preview_hidden_objects_display_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUGroupPreviewHiddenObjectsDisplayModeLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the DMUGroupPreviewHiddenObjectsDisplayMode
                |     parameter.
                |     Role:Locks or unlocks the DMUGroupPreviewHiddenObjectsDisplayMode parameter
                |     if it is possible in the current administrative context. In user mode this
                |     method will always return E_FAIL.
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
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsDisplayModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_group_preview_hidden_objects_display_mode_lock'
        # # vba_code = """
        # # Public Function set_dmu_group_preview_hidden_objects_display_mode_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsDisplayModeLock iLocked
        # #     set_dmu_group_preview_hidden_objects_display_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_group_preview_hidden_objects_low_int_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUGroupPreviewHiddenObjectsLowIntLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the DMUGroupPreviewHiddenObjectsLowInt
                |     parameter.
                |     Role:Locks or unlocks the DMUGroupPreviewHiddenObjectsLowInt parameter if
                |     it is possible in the current administrative context. In user mode this method
                |     will always return E_FAIL.
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
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsLowIntLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_group_preview_hidden_objects_low_int_lock'
        # # vba_code = """
        # # Public Function set_dmu_group_preview_hidden_objects_low_int_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsLowIntLock iLocked
        # #     set_dmu_group_preview_hidden_objects_low_int_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_group_preview_hidden_objects_opacity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUGroupPreviewHiddenObjectsOpacityLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the DMUGroupPreviewHiddenObjectsOpacity
                |     parameter.
                |     Role:Locks or unlocks the DMUGroupPreviewHiddenObjectsOpacity parameter if
                |     it is possible in the current administrative context. In user mode this method
                |     will always return E_FAIL.
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
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsOpacityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_group_preview_hidden_objects_opacity_lock'
        # # vba_code = """
        # # Public Function set_dmu_group_preview_hidden_objects_opacity_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsOpacityLock iLocked
        # #     set_dmu_group_preview_hidden_objects_opacity_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_group_preview_hidden_objects_pick_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUGroupPreviewHiddenObjectsPickLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the DMUGroupPreviewHiddenObjectsPick
                |     parameter.
                |     Role:Locks or unlocks the DMUGroupPreviewHiddenObjectsPick parameter if it
                |     is possible in the current administrative context. In user mode this method
                |     will always return E_FAIL.
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
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsPickLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_group_preview_hidden_objects_pick_lock'
        # # vba_code = """
        # # Public Function set_dmu_group_preview_hidden_objects_pick_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUGroupPreviewHiddenObjectsPickLock iLocked
        # #     set_dmu_group_preview_hidden_objects_pick_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_group_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUGroupPreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUGroupPreview parameter.
                |     Role:Locks or unlocks the DMUGroupPreview parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetDMUGroupPreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_group_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_group_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUGroupPreviewLock iLocked
        # #     set_dmu_group_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_merger_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUMergerPreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUMergerPreview parameter.
                |     Role:Locks or unlocks the DMUMergerPreview parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetDMUMergerPreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_merger_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_merger_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUMergerPreviewLock iLocked
        # #     set_dmu_merger_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_offset_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUOffsetPreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUOffsetPreview parameter.
                |     Role:Locks or unlocks the DMUOffsetPreview parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetDMUOffsetPreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_offset_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_offset_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUOffsetPreviewLock iLocked
        # #     set_dmu_offset_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_review_name_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUReviewNameLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUReviewName parameter.
                |     Role:Locks or unlocks the DMUReviewName parameter if it is possible in the
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
        return self.n_4d_navigator_setting_att.SetDMUReviewNameLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_review_name_lock'
        # # vba_code = """
        # # Public Function set_dmu_review_name_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUReviewNameLock iLocked
        # #     set_dmu_review_name_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_section_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUSectionPreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUSectionPreview parameter.
                |     Role:Locks or unlocks the DMUSectionPreview parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetDMUSectionPreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_section_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_section_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUSectionPreviewLock iLocked
        # #     set_dmu_section_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_shuttle_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUShuttlePreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUShuttlePreview parameter.
                |     Role:Locks or unlocks the DMUShuttlePreview parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetDMUShuttlePreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_shuttle_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_shuttle_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUShuttlePreviewLock iLocked
        # #     set_dmu_shuttle_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_silhouette_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUSilhouettePreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUSilhouettePreview parameter.
                |     Role:Locks or unlocks the DMUSilhouettePreview parameter if it is possible
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
        return self.n_4d_navigator_setting_att.SetDMUSilhouettePreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_silhouette_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_silhouette_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUSilhouettePreviewLock iLocked
        # #     set_dmu_silhouette_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_simplif_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUSimplifPreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUSimplifPreview parameter.
                |     Role:Locks or unlocks the DMUSimplifPreview parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetDMUSimplifPreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_simplif_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_simplif_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUSimplifPreviewLock iLocked
        # #     set_dmu_simplif_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_swept_vol_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUSweptVolPreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUSweptVolPreview parameter.
                |     Role:Locks or unlocks the DMUSweptVolPreview parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetDMUSweptVolPreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_swept_vol_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_swept_vol_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUSweptVolPreviewLock iLocked
        # #     set_dmu_swept_vol_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_thickness_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUThicknessPreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUThicknessPreview parameter.
                |     Role:Locks or unlocks the DMUThicknessPreview parameter if it is possible
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
        return self.n_4d_navigator_setting_att.SetDMUThicknessPreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_thickness_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_thickness_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUThicknessPreviewLock iLocked
        # #     set_dmu_thickness_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_vibration_vol_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUVibrationVolPreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUVibrationVolPreview parameter.
                |     Role:Locks or unlocks the DMUVibrationVolPreview parameter if it is
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
        return self.n_4d_navigator_setting_att.SetDMUVibrationVolPreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_vibration_vol_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_vibration_vol_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUVibrationVolPreviewLock iLocked
        # #     set_dmu_vibration_vol_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dmu_wrapping_preview_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDMUWrappingPreviewLock(boolean iLocked)
                | 
                |     Locks or unlocks the DMUWrappingPreview parameter.
                |     Role:Locks or unlocks the DMUWrappingPreview parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetDMUWrappingPreviewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dmu_wrapping_preview_lock'
        # # vba_code = """
        # # Public Function set_dmu_wrapping_preview_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetDMUWrappingPreviewLock iLocked
        # #     set_dmu_wrapping_preview_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_force_clearance_voxel_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetForceClearanceVoxelLock(boolean iLocked)
                | 
                |     Locks or unlocks the ForceClearanceVoxel parameter.
                |     Role:Locks or unlocks the ForceClearanceVoxel parameter if it is possible
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
        return self.n_4d_navigator_setting_att.SetForceClearanceVoxelLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_force_clearance_voxel_lock'
        # # vba_code = """
        # # Public Function set_force_clearance_voxel_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetForceClearanceVoxelLock iLocked
        # #     set_force_clearance_voxel_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_force_voxel_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetForceVoxelLock(boolean iLocked)
                | 
                |     Locks or unlocks the ForceVoxel parameter.
                |     Role:Locks or unlocks the ForceVoxel parameter if it is possible in the
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
        return self.n_4d_navigator_setting_att.SetForceVoxelLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_force_voxel_lock'
        # # vba_code = """
        # # Public Function set_force_voxel_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetForceVoxelLock iLocked
        # #     set_force_voxel_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_insert_level_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetInsertLevelLock(boolean iLocked)
                | 
                |     Locks or unlocks the InsertMode parameter.
                |     Role:Locks or unlocks the InsertMode parameter if it is possible in the
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
        return self.n_4d_navigator_setting_att.SetInsertLevelLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_insert_level_lock'
        # # vba_code = """
        # # Public Function set_insert_level_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetInsertLevelLock iLocked
        # #     set_insert_level_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_insert_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetInsertModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the InsertMode parameter.
                |     Role:Locks or unlocks the InsertMode parameter if it is possible in the
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
        return self.n_4d_navigator_setting_att.SetInsertModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_insert_mode_lock'
        # # vba_code = """
        # # Public Function set_insert_mode_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetInsertModeLock iLocked
        # #     set_insert_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_2d_auto_naming_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarker2DAutoNamingLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarker2DAutoNamingLock Locks or unlocks the
                |         Marker2DAutoNaming parameter.
                |         Role:Locks or unlocks the Marker2DAutoNaming parameter if it is
                |         possible in the current administrative context. In user mode this method will
                |         always return E_FAIL. 
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
        return self.n_4d_navigator_setting_att.SetMarker2DAutoNamingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_2d_auto_naming_lock'
        # # vba_code = """
        # # Public Function set_marker_2d_auto_naming_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetMarker2DAutoNamingLock iLocked
        # #     set_marker_2d_auto_naming_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_3d_auto_naming_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarker3DAutoNamingLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarker3DAutoNamingLock Locks or unlocks the
                |         Marker3DAutoNaming parameter.
                |         Role:Locks or unlocks the Marker3DAutoNaming parameter if it is
                |         possible in the current administrative context. In user mode this method will
                |         always return E_FAIL. 
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
        return self.n_4d_navigator_setting_att.SetMarker3DAutoNamingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_3d_auto_naming_lock'
        # # vba_code = """
        # # Public Function set_marker_3d_auto_naming_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetMarker3DAutoNamingLock iLocked
        # #     set_marker_3d_auto_naming_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_auto_update_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerAutoUpdateLock(boolean iLocked)
                | 
                |     Locks or unlocks the MarkerAutoUpdate parameter.
                |     Role:Locks or unlocks the MarkerAutoUpdate parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetMarkerAutoUpdateLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_auto_update_lock'
        # # vba_code = """
        # # Public Function set_marker_auto_update_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetMarkerAutoUpdateLock iLocked
        # #     set_marker_auto_update_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_defaults_color(self, i_red: int, i_green: int, i_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerDefaultsColor(long iRed,
                | long iGreen,
                | long iBlue)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarkerDefaultsColor Sets the default color of an annotation
                |         (iRed, iGreen, iBlue: RGB values for the desired color)

        :param int i_red:
        :param int i_green:
        :param int i_blue:
        :rtype: None
        """
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsColor(i_red, i_green, i_blue)

    def set_marker_defaults_color_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerDefaultsColorLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarkerDefaultsColorLock Locks or unlocks the
                |         MarkerDefaultsColor parameter.
                |         Role:Locks or unlocks the MarkerDefaultsColor parameter if it is
                |         possible in the current administrative context. In user mode this method will
                |         always return E_FAIL. 
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
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_defaults_color_lock'
        # # vba_code = """
        # # Public Function set_marker_defaults_color_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetMarkerDefaultsColorLock iLocked
        # #     set_marker_defaults_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_defaults_dashed_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerDefaultsDashedLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarkerDefaultsDashedLock Locks or unlocks the
                |         MarkerDefaultsDashed parameter.
                |         Role:Locks or unlocks the MarkerDefaultsDashed parameter if it is
                |         possible in the current administrative context. In user mode this method will
                |         always return E_FAIL. 
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
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsDashedLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_defaults_dashed_lock'
        # # vba_code = """
        # # Public Function set_marker_defaults_dashed_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetMarkerDefaultsDashedLock iLocked
        # #     set_marker_defaults_dashed_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_defaults_font_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerDefaultsFontLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarkerDefaultsFont2DLock Locks or unlocks the
                |         MarkerDefaultsFont parameter.
                |         Role:Locks or unlocks the MarkerDefaultsSize parameter if it is
                |         possible in the current administrative context. In user mode this method will
                |         always return E_FAIL. 
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
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsFontLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_defaults_font_lock'
        # # vba_code = """
        # # Public Function set_marker_defaults_font_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetMarkerDefaultsFontLock iLocked
        # #     set_marker_defaults_font_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_defaults_size_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerDefaultsSizeLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarkerTextDefaultsSize2DLock Locks or unlocks the
                |         MarkerDefaultsSize parameter.
                |         Role:Locks or unlocks the MarkerDefaultsSize parameter if it is
                |         possible in the current administrative context. In user mode this method will
                |         always return E_FAIL. 
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
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsSizeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_defaults_size_lock'
        # # vba_code = """
        # # Public Function set_marker_defaults_size_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetMarkerDefaultsSizeLock iLocked
        # #     set_marker_defaults_size_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_defaults_weight_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerDefaultsWeightLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarkerDefaultsWeightLock Locks or unlocks the
                |         MarkerDefaultsWeight parameter.
                |         Role:Locks or unlocks the MarkerDefaultsColor parameter if it is
                |         possible in the current administrative context. In user mode this method will
                |         always return E_FAIL. 
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
        return self.n_4d_navigator_setting_att.SetMarkerDefaultsWeightLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_defaults_weight_lock'
        # # vba_code = """
        # # Public Function set_marker_defaults_weight_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetMarkerDefaultsWeightLock iLocked
        # #     set_marker_defaults_weight_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_color(self, i_red: int, i_green: int, i_blue: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextColor(long iRed,
                | long iGreen,
                | long iBlue)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarkerTextColor2D Sets the default color of a text
                |         annotation (iRed, iGreen, iBlue: RGB values for the desired color).

        :param int i_red:
        :param int i_green:
        :param int i_blue:
        :rtype: None
        """
        return self.n_4d_navigator_setting_att.SetMarkerTextColor(i_red, i_green, i_blue)

    def set_marker_text_color_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextColorLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarkerTextColor2DLock Locks or unlocks the MarkerTextColor
                |         parameter.
                |         Role:Locks or unlocks the MarkerTextColor parameter if it is possible
                |         in the current administrative context. In user mode this method will always
                |         return E_FAIL. 
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
        return self.n_4d_navigator_setting_att.SetMarkerTextColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_color_lock'
        # # vba_code = """
        # # Public Function set_marker_text_color_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetMarkerTextColorLock iLocked
        # #     set_marker_text_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_dashed_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextDashedLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarkerTextDashed2DLock Locks or unlocks the
                |         MarkerTextDashed parameter.
                |         Role:Locks or unlocks the MarkerTextDashed parameter if it is possible
                |         in the current administrative context. In user mode this method will always
                |         return E_FAIL. 
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
        return self.n_4d_navigator_setting_att.SetMarkerTextDashedLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_dashed_lock'
        # # vba_code = """
        # # Public Function set_marker_text_dashed_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetMarkerTextDashedLock iLocked
        # #     set_marker_text_dashed_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_marker_text_weight_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMarkerTextWeightLock(boolean iLocked)
                | 
                |     Deprecated:
                |         R17 This method will be replaced by
                |         MarkerSettingAtt.SetMarkerTextWeight2DLock Locks or unlocks the
                |         MarkerTextWeight parameter.
                |         Role:Locks or unlocks the MarkerTextWeight parameter if it is possible
                |         in the current administrative context. In user mode this method will always
                |         return E_FAIL. 
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
        return self.n_4d_navigator_setting_att.SetMarkerTextWeightLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_marker_text_weight_lock'
        # # vba_code = """
        # # Public Function set_marker_text_weight_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetMarkerTextWeightLock iLocked
        # #     set_marker_text_weight_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_num_url_name_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNumUrlNameLock(boolean iLocked)
                | 
                |     Locks or unlocks the NumUrlName parameter.
                |     Role:Locks or unlocks the NumUrlName parameter if it is possible in the
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
        return self.n_4d_navigator_setting_att.SetNumUrlNameLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_num_url_name_lock'
        # # vba_code = """
        # # Public Function set_num_url_name_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetNumUrlNameLock iLocked
        # #     set_num_url_name_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_publish_auto_launch_browser_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPublishAutoLaunchBrowserLock(boolean iLocked)
                | 
                |     Locks or unlocks the PublishAutoLaunchBrowser parameter.
                |     Role:Locks or unlocks the PublishAutoLaunchBrowser parameter if it is
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
        return self.n_4d_navigator_setting_att.SetPublishAutoLaunchBrowserLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_publish_auto_launch_browser_lock'
        # # vba_code = """
        # # Public Function set_publish_auto_launch_browser_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetPublishAutoLaunchBrowserLock iLocked
        # #     set_publish_auto_launch_browser_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_scene_defaults_color(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSceneDefaultsColor(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the scene background color (iRed, iGreen, iBlue: RGB values for the
                |     desired color)

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.n_4d_navigator_setting_att.SetSceneDefaultsColor(i_r, i_g, i_b)

    def set_scene_defaults_color_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSceneDefaultsColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the SceneDefaultsColor parameter.
                |     Role:Locks or unlocks the SceneDefaultsColor parameter if it is possible in
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
        return self.n_4d_navigator_setting_att.SetSceneDefaultsColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_scene_defaults_color_lock'
        # # vba_code = """
        # # Public Function set_scene_defaults_color_lock(n_4d_navigator_setting_att)
        # #     Dim iLocked (2)
        # #     n_4d_navigator_setting_att.SetSceneDefaultsColorLock iLocked
        # #     set_scene_defaults_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'N4DNavigatorSettingAtt(name="{self.name}")'
