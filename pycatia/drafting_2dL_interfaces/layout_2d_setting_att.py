#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class Layout2DSettingAtt(SettingController):
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
                |                         Layout2DSettingAtt
                | 
                | The interface to access a CATIA2DLSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.layout_2d_setting_att = com_object

    @property
    def activate_2d_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Activate2DMode() As boolean
                | 
                |     Returns the Activate2DMode parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.Activate2DMode

    @activate_2d_mode.setter
    def activate_2d_mode(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.Activate2DMode = value

    @property
    def back_clipping_plane(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BackClippingPlane() As boolean
                | 
                |     Returns the BackClippingPlane parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.BackClippingPlane

    @back_clipping_plane.setter
    def back_clipping_plane(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.BackClippingPlane = value

    @property
    def boundaries_2dl_display(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Boundaries2DLDisplay() As boolean
                | 
                |     Returns the Boundaries2DLDisplay parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.Boundaries2DLDisplay

    @boundaries_2dl_display.setter
    def boundaries_2dl_display(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.Boundaries2DLDisplay = value

    @property
    def boundaries_2dl_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Boundaries2DLLineType() As long
                | 
                |     Returns the Boundaries2DLLineType parameter.

        :rtype: int
        """

        return self.layout_2d_setting_att.Boundaries2DLLineType

    @boundaries_2dl_line_type.setter
    def boundaries_2dl_line_type(self, value: int):
        """
        :param int value:
        """

        self.layout_2d_setting_att.Boundaries2DLLineType = value

    @property
    def boundaries_2dl_thickness(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Boundaries2DLThickness() As long
                | 
                |     Returns the Boundaries2DLThickness parameter.

        :rtype: int
        """

        return self.layout_2d_setting_att.Boundaries2DLThickness

    @boundaries_2dl_thickness.setter
    def boundaries_2dl_thickness(self, value: int):
        """
        :param int value:
        """

        self.layout_2d_setting_att.Boundaries2DLThickness = value

    @property
    def callout_creation_dialog_box(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CalloutCreationDialogBox() As boolean
                | 
                |     Returns the CalloutCreationDialogBox parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.CalloutCreationDialogBox

    @callout_creation_dialog_box.setter
    def callout_creation_dialog_box(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.CalloutCreationDialogBox = value

    @property
    def callout_creation_in_active_view(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CalloutCreationInActiveView() As boolean
                | 
                |     Returns the CalloutCreationInActiveView parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.CalloutCreationInActiveView

    @callout_creation_in_active_view.setter
    def callout_creation_in_active_view(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.CalloutCreationInActiveView = value

    @property
    def clipping_frame(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ClippingFrame() As boolean
                | 
                |     Returns the ClippingFrame parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.ClippingFrame

    @clipping_frame.setter
    def clipping_frame(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.ClippingFrame = value

    @property
    def clipping_frame_reframe_on_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ClippingFrameReframeOnMode() As
                | CatClippingFrameReframeOnMode
                | 
                |     Returns the ClippingFrameReframeOnMode parameter.
                | 
                |     Deprecated:
                |         V5R18

        :return: enum cat_clipping_frame_reframe_on_mode
        :rtype: int
        """

        return self.layout_2d_setting_att.ClippingFrameReframeOnMode

    @clipping_frame_reframe_on_mode.setter
    def clipping_frame_reframe_on_mode(self, value: int):
        """
        :param int value:
        """

        self.layout_2d_setting_att.ClippingFrameReframeOnMode = value

    @property
    def clipping_view_outline_linetype(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ClippingViewOutlineLinetype() As long
                | 
                |     Returns the ClippingViewOutlineLinetype parameter.

        :rtype: int
        """

        return self.layout_2d_setting_att.ClippingViewOutlineLinetype

    @clipping_view_outline_linetype.setter
    def clipping_view_outline_linetype(self, value: int):
        """
        :param int value:
        """

        self.layout_2d_setting_att.ClippingViewOutlineLinetype = value

    @property
    def clipping_view_outline_thickness(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ClippingViewOutlineThickness() As long
                | 
                |     Returns the ClippingViewOutlineThickness parameter.

        :rtype: int
        """

        return self.layout_2d_setting_att.ClippingViewOutlineThickness

    @clipping_view_outline_thickness.setter
    def clipping_view_outline_thickness(self, value: int):
        """
        :param int value:
        """

        self.layout_2d_setting_att.ClippingViewOutlineThickness = value

    @property
    def create_associative_use_edges(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CreateAssociativeUseEdges() As boolean
                | 
                |     Returns the CreateAssociativeUseEdges parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.CreateAssociativeUseEdges

    @create_associative_use_edges.setter
    def create_associative_use_edges(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.CreateAssociativeUseEdges = value

    @property
    def dedicated_filter_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DedicatedFilterType() As CatDedicatedFilterType
                | 
                |     Returns the DedicatedFilterType parameter.

        :return: enum cat_dedicated_filter_type
        :rtype: int
        """

        return self.layout_2d_setting_att.DedicatedFilterType

    @dedicated_filter_type.setter
    def dedicated_filter_type(self, value: int):
        """
        :param int value:
        """

        self.layout_2d_setting_att.DedicatedFilterType = value

    @property
    def display_back_and_cutting_plane(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DisplayBackAndCuttingPlane() As boolean
                | 
                |     Returns the DisplayBackAndCuttingPlane parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.DisplayBackAndCuttingPlane

    @display_back_and_cutting_plane.setter
    def display_back_and_cutting_plane(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.DisplayBackAndCuttingPlane = value

    @property
    def display_clipping_outline(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DisplayClippingOutline() As boolean
                | 
                |     Returns the DisplayClippingOutline parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.DisplayClippingOutline

    @display_clipping_outline.setter
    def display_clipping_outline(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.DisplayClippingOutline = value

    @property
    def edit_dedicated_filter_dialog_box(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EditDedicatedFilterDialogBox() As boolean
                | 
                |     Returns the EditDedicatedFilterDialogBox parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.EditDedicatedFilterDialogBox

    @edit_dedicated_filter_dialog_box.setter
    def edit_dedicated_filter_dialog_box(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.EditDedicatedFilterDialogBox = value

    @property
    def fit_all_in_sheet_format(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FitAllInSheetFormat() As boolean
                | 
                |     Returns the FitAllInSheetFormat parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.FitAllInSheetFormat

    @fit_all_in_sheet_format.setter
    def fit_all_in_sheet_format(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.FitAllInSheetFormat = value

    @property
    def hide_in_3d(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HideIn3D() As boolean
                | 
                |     Returns the HideIn3D parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.HideIn3D

    @hide_in_3d.setter
    def hide_in_3d(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.HideIn3D = value

    @property
    def insure_filter_names_uniqueness(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InsureFilterNamesUniqueness() As boolean
                | 
                |     Returns the InsureFilterNamesUniqueness attribute value to apply to a
                |     Layout at its creation parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.InsureFilterNamesUniqueness

    @insure_filter_names_uniqueness.setter
    def insure_filter_names_uniqueness(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.InsureFilterNamesUniqueness = value

    @property
    def insure_sheet_names_uniqueness(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InsureSheetNamesUniqueness() As boolean
                | 
                |     Returns the InsureSheetNamesUniqueness attribute value to apply to a Layout
                |     at its creation parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.InsureSheetNamesUniqueness

    @insure_sheet_names_uniqueness.setter
    def insure_sheet_names_uniqueness(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.InsureSheetNamesUniqueness = value

    @property
    def insure_view_names_uniqueness(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InsureViewNamesUniqueness() As boolean
                | 
                |     Returns the InsureViewNamesUniqueness attribute value to apply to a Layout
                |     at its creation parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.InsureViewNamesUniqueness

    @insure_view_names_uniqueness.setter
    def insure_view_names_uniqueness(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.InsureViewNamesUniqueness = value

    @property
    def insure_view_names_uniqueness_scope(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property InsureViewNamesUniquenessScope() As
                | CatInsureViewNamesUniquenessScope
                | 
                |     Returns the InsureViewNamesUniquenessScope parameter.

        :return: enum cat_insure_view_names_uniqueness_scope
        :rtype: int
        """

        return self.layout_2d_setting_att.InsureViewNamesUniquenessScope

    @insure_view_names_uniqueness_scope.setter
    def insure_view_names_uniqueness_scope(self, value: int):
        """
        :param int value: enum cat_insure_view_names_uniqueness_scope
        """

        self.layout_2d_setting_att.InsureViewNamesUniquenessScope = value

    @property
    def layout_default_render_style(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LayoutDefaultRenderStyle() As long
                | 
                |     Returns the default render style attribute value to apply to a Layout at
                |     its creation parameter.

        :rtype: int
        """

        return self.layout_2d_setting_att.LayoutDefaultRenderStyle

    @layout_default_render_style.setter
    def layout_default_render_style(self, value: int):
        """
        :param int value:
        """

        self.layout_2d_setting_att.LayoutDefaultRenderStyle = value

    @property
    def propagate_highlight(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PropagateHighlight() As boolean
                | 
                |     Returns the PropagateHighlight parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.PropagateHighlight

    @propagate_highlight.setter
    def propagate_highlight(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.PropagateHighlight = value

    @property
    def tile_layout_window(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TileLayoutWindow() As boolean
                | 
                |     Returns the tile of Layout window parameter.

        :rtype: bool
        """

        return self.layout_2d_setting_att.TileLayoutWindow

    @tile_layout_window.setter
    def tile_layout_window(self, value: bool):
        """
        :param bool value:
        """

        self.layout_2d_setting_att.TileLayoutWindow = value

    @property
    def view_background_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ViewBackgroundMode() As CatViewBackgroundMode
                | 
                |     Returns the ViewBackgroundMode parameter.

        :return: enum cat_view_background_mode
        :rtype: int
        """

        return self.layout_2d_setting_att.ViewBackgroundMode

    @view_background_mode.setter
    def view_background_mode(self, value: int):
        """
        :param int value: enum cat_view_background_mode
        """

        self.layout_2d_setting_att.ViewBackgroundMode = value

    @property
    def view_filter_creation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ViewFilterCreationMode() As
                | CatViewFilterCreationMode
                | 
                |     Returns the ViewFilterCreationMode parameter.

        :return: enum cat_view_filter_creation_mode
        :rtype: int
        """

        return self.layout_2d_setting_att.ViewFilterCreationMode

    @view_filter_creation_mode.setter
    def view_filter_creation_mode(self, value: int):
        """
        :param int value: enum cat_view_filter_creation_mode
        """

        self.layout_2d_setting_att.ViewFilterCreationMode = value

    def get_activate_2d_mode_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetActivate2DModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the Activate2DMode
                |     parameter.
                |     Role:Retrieves the state of the Activate2DMode parameter in the current
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetActivate2DModeInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_activate2_d_mode_info'
        # # vba_code = """
        # # Public Function get_activate2_d_mode_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetActivate2DModeInfo ioAdminLevel
        # #     get_activate2_d_mode_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_back_clipping_plane_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetBackClippingPlaneInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the BackClippingPlane
                |     parameter.
                |     Role:Retrieves the state of the BackClippingPlane parameter in the current
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetBackClippingPlaneInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_back_clipping_plane_info'
        # # vba_code = """
        # # Public Function get_back_clipping_plane_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetBackClippingPlaneInfo ioAdminLevel
        # #     get_back_clipping_plane_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_boundaries_2dl_colour(self, o_value_r: int, o_value_g: int, o_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetBoundaries2DLColor(long oValueR,
                | long oValueG,
                | long oValueB)
                | 
                |     Returns the Boundaries2DLColor parameter.

        :param int o_value_r:
        :param int o_value_g:
        :param int o_value_b:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetBoundaries2DLColor(o_value_r, o_value_g, o_value_b)

    def get_boundaries_2dl_colour_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetBoundaries2DLColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the Boundaries2DLColor
                |     parameter.
                |     Role:Retrieves the state of the Boundaries2DLColor parameter in the current
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetBoundaries2DLColorInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_boundaries2_dl_color_info'
        # # vba_code = """
        # # Public Function get_boundaries2_dl_color_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetBoundaries2DLColorInfo ioAdminLevel
        # #     get_boundaries2_dl_color_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_boundaries_2dl_display_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetBoundaries2DLDisplayInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the Boundaries2DLDisplay
                |     parameter.
                |     Role:Retrieves the state of the Boundaries2DLDisplay parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetBoundaries2DLDisplayInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_boundaries2_dl_display_info'
        # # vba_code = """
        # # Public Function get_boundaries2_dl_display_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetBoundaries2DLDisplayInfo ioAdminLevel
        # #     get_boundaries2_dl_display_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_boundaries_2dl_line_type_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetBoundaries2DLLineTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the Boundaries2DLLineType
                |     parameter.
                |     Role:Retrieves the state of the Boundaries2DLLineType parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetBoundaries2DLLineTypeInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_boundaries2_dl_line_type_info'
        # # vba_code = """
        # # Public Function get_boundaries2_dl_line_type_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetBoundaries2DLLineTypeInfo ioAdminLevel
        # #     get_boundaries2_dl_line_type_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_boundaries_2dl_thickness_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetBoundaries2DLThicknessInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the Boundaries2DLThickness
                |     parameter.
                |     Role:Retrieves the state of the Boundaries2DLThickness parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetBoundaries2DLThicknessInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_boundaries2_dl_thickness_info'
        # # vba_code = """
        # # Public Function get_boundaries2_dl_thickness_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetBoundaries2DLThicknessInfo ioAdminLevel
        # #     get_boundaries2_dl_thickness_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_callout_creation_dialog_box_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetCalloutCreationDialogBoxInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the CalloutCreationDialogBox
                |     parameter.
                |     Role:Retrieves the state of the CalloutCreationDialogBox parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetCalloutCreationDialogBoxInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_callout_creation_dialog_box_info'
        # # vba_code = """
        # # Public Function get_callout_creation_dialog_box_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetCalloutCreationDialogBoxInfo ioAdminLevel
        # #     get_callout_creation_dialog_box_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_callout_creation_in_active_view_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetCalloutCreationInActiveViewInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the CalloutCreationInActiveView
                |     parameter.
                |     Role:Retrieves the state of the CalloutCreationInActiveView parameter in
                |     the current environment.
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetCalloutCreationInActiveViewInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_callout_creation_in_active_view_info'
        # # vba_code = """
        # # Public Function get_callout_creation_in_active_view_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetCalloutCreationInActiveViewInfo ioAdminLevel
        # #     get_callout_creation_in_active_view_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_clipping_frame_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetClippingFrameInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the ClippingFrame
                |     parameter.
                |     Role:Retrieves the state of the ClippingFrame parameter in the current
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetClippingFrameInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_clipping_frame_info'
        # # vba_code = """
        # # Public Function get_clipping_frame_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetClippingFrameInfo ioAdminLevel
        # #     get_clipping_frame_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_clipping_frame_reframe_on_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetClippingFrameReframeOnModeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Deprecated:
                |         V5R18 Retrieves environment informations for the
                |         ClippingFrameReframeOnMode parameter.
                |         Role:Retrieves the state of the ClippingFrameReframeOnMode parameter in
                |         the current environment. 
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
        return self.layout_2d_setting_att.GetClippingFrameReframeOnModeInfo(io_admin_level, io_locked)

    def get_clipping_view_outline_color(self, o_value_r: int, o_value_g: int, o_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetClippingViewOutlineColor(long oValueR,
                | long oValueG,
                | long oValueB)
                | 
                |     Returns the ClippingViewOutlineColor parameter.

        :param int o_value_r:
        :param int o_value_g:
        :param int o_value_b:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetClippingViewOutlineColor(o_value_r, o_value_g, o_value_b)

    def get_clipping_view_outline_color_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetClippingViewOutlineColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the ClippingViewOutlineColor
                |     parameter.
                |     Role:Retrieves the state of the ClippingViewOutlineColor parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetClippingViewOutlineColorInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_clipping_view_outline_color_info'
        # # vba_code = """
        # # Public Function get_clipping_view_outline_color_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetClippingViewOutlineColorInfo ioAdminLevel
        # #     get_clipping_view_outline_color_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_clipping_view_outline_linetype_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetClippingViewOutlineLinetypeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the ClippingViewOutlineLinetype
                |     parameter.
                |     Role:Retrieves the state of the ClippingViewOutlineLinetype parameter in
                |     the current environment.
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetClippingViewOutlineLinetypeInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_clipping_view_outline_linetype_info'
        # # vba_code = """
        # # Public Function get_clipping_view_outline_linetype_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetClippingViewOutlineLinetypeInfo ioAdminLevel
        # #     get_clipping_view_outline_linetype_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_clipping_view_outline_thickness_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetClippingViewOutlineThicknessInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the ClippingViewOutlineThickness
                |     parameter.
                |     Role:Retrieves the state of the ClippingViewOutlineThickness parameter in
                |     the current environment.
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetClippingViewOutlineThicknessInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_clipping_view_outline_thickness_info'
        # # vba_code = """
        # # Public Function get_clipping_view_outline_thickness_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetClippingViewOutlineThicknessInfo ioAdminLevel
        # #     get_clipping_view_outline_thickness_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_create_associative_use_edges_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetCreateAssociativeUseEdgesInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the CreateAssociativeUseEdges
                |     parameter.
                |     Role:Retrieves the state of the CreateAssociativeUseEdges parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetCreateAssociativeUseEdgesInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_create_associative_use_edges_info'
        # # vba_code = """
        # # Public Function get_create_associative_use_edges_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetCreateAssociativeUseEdgesInfo ioAdminLevel
        # #     get_create_associative_use_edges_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_dedicated_filter_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDedicatedFilterTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the DedicatedFilterType
                |     parameter.
                |     Role:Retrieves the state of the DedicatedFilterType parameter in the
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
        return self.layout_2d_setting_att.GetDedicatedFilterTypeInfo(io_admin_level, io_locked)

    def get_display_back_and_cutting_plane_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetDisplayBackAndCuttingPlaneInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the DisplayBackAndCuttingPlane
                |     parameter.
                |     Role:Retrieves the state of the DisplayBackAndCuttingPlane parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetDisplayBackAndCuttingPlaneInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_display_back_and_cutting_plane_info'
        # # vba_code = """
        # # Public Function get_display_back_and_cutting_plane_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetDisplayBackAndCuttingPlaneInfo ioAdminLevel
        # #     get_display_back_and_cutting_plane_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_display_clipping_outline_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetDisplayClippingOutlineInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the DisplayClippingOutline
                |     parameter.
                |     Role:Retrieves the state of the DisplayClippingOutline parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetDisplayClippingOutlineInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_display_clipping_outline_info'
        # # vba_code = """
        # # Public Function get_display_clipping_outline_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetDisplayClippingOutlineInfo ioAdminLevel
        # #     get_display_clipping_outline_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_edit_dedicated_filter_dialog_box_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetEditDedicatedFilterDialogBoxInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the EditDedicatedFilterDialogBox
                |     parameter.
                |     Role:Retrieves the state of the EditDedicatedFilterDialogBox parameter in
                |     the current environment.
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetEditDedicatedFilterDialogBoxInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_edit_dedicated_filter_dialog_box_info'
        # # vba_code = """
        # # Public Function get_edit_dedicated_filter_dialog_box_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetEditDedicatedFilterDialogBoxInfo ioAdminLevel
        # #     get_edit_dedicated_filter_dialog_box_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_fit_all_in_sheet_format_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetFitAllInSheetFormatInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the FitAllInSheetFormat
                |     parameter.
                |     Role:Retrieves the state of the FitAllInSheetFormat parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetFitAllInSheetFormatInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_fit_all_in_sheet_format_info'
        # # vba_code = """
        # # Public Function get_fit_all_in_sheet_format_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetFitAllInSheetFormatInfo ioAdminLevel
        # #     get_fit_all_in_sheet_format_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_hide_in_3d_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetHideIn3DInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the HideIn3D
                |     parameter.
                |     Role:Retrieves the state of the HideIn3D parameter in the current
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetHideIn3DInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_hide_in3_d_info'
        # # vba_code = """
        # # Public Function get_hide_in3_d_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetHideIn3DInfo ioAdminLevel
        # #     get_hide_in3_d_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_insure_filter_names_uniqueness_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetInsureFilterNamesUniquenessInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the InsureFilterNamesUniqueness
                |     parameter.
                |     Role:Retrieves the state of the InsureFilterNamesUniqueness parameter in
                |     the current environment.
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetInsureFilterNamesUniquenessInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_insure_filter_names_uniqueness_info'
        # # vba_code = """
        # # Public Function get_insure_filter_names_uniqueness_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetInsureFilterNamesUniquenessInfo ioAdminLevel
        # #     get_insure_filter_names_uniqueness_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_insure_sheet_names_uniqueness_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetInsureSheetNamesUniquenessInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the InsureSheetNamesUniqueness
                |     parameter.
                |     Role:Retrieves the state of the InsureSheetNamesUniqueness parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetInsureSheetNamesUniquenessInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_insure_sheet_names_uniqueness_info'
        # # vba_code = """
        # # Public Function get_insure_sheet_names_uniqueness_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetInsureSheetNamesUniquenessInfo ioAdminLevel
        # #     get_insure_sheet_names_uniqueness_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_insure_view_names_uniqueness_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetInsureViewNamesUniquenessInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the InsureViewNamesUniqueness
                |     parameter.
                |     Role:Retrieves the state of the InsureViewNamesUniqueness parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetInsureViewNamesUniquenessInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_insure_view_names_uniqueness_info'
        # # vba_code = """
        # # Public Function get_insure_view_names_uniqueness_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetInsureViewNamesUniquenessInfo ioAdminLevel
        # #     get_insure_view_names_uniqueness_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_insure_view_names_uniqueness_scope_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetInsureViewNamesUniquenessScopeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the InsureViewNamesUniquenessScope
                |     parameter.
                |     Role:Retrieves the state of the InsureViewNamesUniquenessScope parameter in
                |     the current environment.
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
        return self.layout_2d_setting_att.GetInsureViewNamesUniquenessScopeInfo(io_admin_level, io_locked)

    def get_layout_default_render_style_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetLayoutDefaultRenderStyleInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the default render style
                |     parameter.
                |     Role:Retrieves the state of the default render style parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetLayoutDefaultRenderStyleInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_layout_default_render_style_info'
        # # vba_code = """
        # # Public Function get_layout_default_render_style_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetLayoutDefaultRenderStyleInfo ioAdminLevel
        # #     get_layout_default_render_style_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_propagate_highlight_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPropagateHighlightInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the PropagateHighlight
                |     parameter.
                |     Role:Retrieves the state of the PropagateHighlight parameter in the current
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetPropagateHighlightInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_propagate_highlight_info'
        # # vba_code = """
        # # Public Function get_propagate_highlight_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetPropagateHighlightInfo ioAdminLevel
        # #     get_propagate_highlight_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_protected_elements_colour(self, o_value_r: int, o_value_g: int, o_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetProtectedElementsColor(long oValueR,
                | long oValueG,
                | long oValueB)
                | 
                |     Returns the ProtectedElementsColor parameter.

        :param int o_value_r:
        :param int o_value_g:
        :param int o_value_b:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetProtectedElementsColor(o_value_r, o_value_g, o_value_b)

    def get_protected_elements_colour_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetProtectedElementsColorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the ProtectedElementsColor
                |     parameter.
                |     Role:Retrieves the state of the ProtectedElementsColor parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetProtectedElementsColorInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_protected_elements_color_info'
        # # vba_code = """
        # # Public Function get_protected_elements_color_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetProtectedElementsColorInfo ioAdminLevel
        # #     get_protected_elements_color_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_tile_layout_window_info(self, io_admin_level: str, io_locked: str, o_modified: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTileLayoutWindowInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked,
                | boolean oModified)
                | 
                |     Retrieves environment informations for the tile of Layout window
                |     parameter.
                |     Role:Retrieves the state of the tile of Layout window parameter in the
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
        :param bool o_modified:
        :rtype: None
        """
        return self.layout_2d_setting_att.GetTileLayoutWindowInfo(io_admin_level, io_locked, o_modified)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_tile_layout_window_info'
        # # vba_code = """
        # # Public Function get_tile_layout_window_info(layout_2d_setting_att)
        # #     Dim ioAdminLevel (2)
        # #     layout_2d_setting_att.GetTileLayoutWindowInfo ioAdminLevel
        # #     get_tile_layout_window_info = ioAdminLevel
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_view_background_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetViewBackgroundModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ViewBackgroundMode
                |     parameter.
                |     Role:Retrieves the state of the ViewBackgroundMode parameter in the current
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
        return self.layout_2d_setting_att.GetViewBackgroundModeInfo(io_admin_level, io_locked)

    def get_view_filter_creation_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetViewFilterCreationModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the ViewFilterCreationMode
                |     parameter.
                |     Role:Retrieves the state of the ViewFilterCreationMode parameter in the
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
        return self.layout_2d_setting_att.GetViewFilterCreationModeInfo(io_admin_level, io_locked)

    def set_activate_2d_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetActivate2DModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Activate2DMode parameter.
                |     Role:Locks or unlocks the Activate2DMode parameter if it is possible in the
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
        return self.layout_2d_setting_att.SetActivate2DModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_activate2_d_mode_lock'
        # # vba_code = """
        # # Public Function set_activate2_d_mode_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetActivate2DModeLock iLocked
        # #     set_activate2_d_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_back_clipping_plane_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBackClippingPlaneLock(boolean iLocked)
                | 
                |     Locks or unlocks the BackClippingPlane parameter.
                |     Role:Locks or unlocks the BackClippingPlane parameter if it is possible in
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
        return self.layout_2d_setting_att.SetBackClippingPlaneLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_back_clipping_plane_lock'
        # # vba_code = """
        # # Public Function set_back_clipping_plane_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetBackClippingPlaneLock iLocked
        # #     set_back_clipping_plane_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_boundaries_2dl_colour(self, i_value_r: int, i_value_g: int, i_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBoundaries2DLColor(long iValueR,
                | long iValueG,
                | long iValueB)
                | 
                |     Sets the Boundaries2DLColor parameter.

        :param int i_value_r:
        :param int i_value_g:
        :param int i_value_b:
        :rtype: None
        """
        return self.layout_2d_setting_att.SetBoundaries2DLColor(i_value_r, i_value_g, i_value_b)

    def set_boundaries_2dl_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBoundaries2DLColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the Boundaries2DLColor parameter.
                |     Role:Locks or unlocks the Boundaries2DLColor parameter if it is possible in
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
        return self.layout_2d_setting_att.SetBoundaries2DLColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_boundaries2_dl_color_lock'
        # # vba_code = """
        # # Public Function set_boundaries2_dl_color_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetBoundaries2DLColorLock iLocked
        # #     set_boundaries2_dl_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_boundaries_2dl_display_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBoundaries2DLDisplayLock(boolean iLocked)
                | 
                |     Locks or unlocks the Boundaries2DLDisplay parameter.
                |     Role:Locks or unlocks the Boundaries2DLDisplay parameter if it is possible
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
        return self.layout_2d_setting_att.SetBoundaries2DLDisplayLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_boundaries2_dl_display_lock'
        # # vba_code = """
        # # Public Function set_boundaries2_dl_display_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetBoundaries2DLDisplayLock iLocked
        # #     set_boundaries2_dl_display_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_boundaries_2dl_line_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBoundaries2DLLineTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Boundaries2DLLineType parameter.
                |     Role:Locks or unlocks the Boundaries2DLLineType parameter if it is possible
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
        return self.layout_2d_setting_att.SetBoundaries2DLLineTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_boundaries2_dl_line_type_lock'
        # # vba_code = """
        # # Public Function set_boundaries2_dl_line_type_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetBoundaries2DLLineTypeLock iLocked
        # #     set_boundaries2_dl_line_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_boundaries_2dl_thickness_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetBoundaries2DLThicknessLock(boolean iLocked)
                | 
                |     Locks or unlocks the Boundaries2DLThickness parameter.
                |     Role:Locks or unlocks the Boundaries2DLThickness parameter if it is
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
        return self.layout_2d_setting_att.SetBoundaries2DLThicknessLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_boundaries2_dl_thickness_lock'
        # # vba_code = """
        # # Public Function set_boundaries2_dl_thickness_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetBoundaries2DLThicknessLock iLocked
        # #     set_boundaries2_dl_thickness_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_callout_creation_dialog_box_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCalloutCreationDialogBoxLock(boolean iLocked)
                | 
                |     Locks or unlocks the CalloutCreationDialogBox parameter.
                |     Role:Locks or unlocks the CalloutCreationDialogBox parameter if it is
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
        return self.layout_2d_setting_att.SetCalloutCreationDialogBoxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_callout_creation_dialog_box_lock'
        # # vba_code = """
        # # Public Function set_callout_creation_dialog_box_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetCalloutCreationDialogBoxLock iLocked
        # #     set_callout_creation_dialog_box_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_callout_creation_in_active_view_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCalloutCreationInActiveViewLock(boolean iLocked)
                | 
                |     Locks or unlocks the CalloutCreationInActiveView
                |     parameter.
                |     Role:Locks or unlocks the CalloutCreationInActiveView parameter if it is
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
        return self.layout_2d_setting_att.SetCalloutCreationInActiveViewLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_callout_creation_in_active_view_lock'
        # # vba_code = """
        # # Public Function set_callout_creation_in_active_view_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetCalloutCreationInActiveViewLock iLocked
        # #     set_callout_creation_in_active_view_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_clipping_frame_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetClippingFrameLock(boolean iLocked)
                | 
                |     Locks or unlocks the ClippingFrame parameter.
                |     Role:Locks or unlocks the ClippingFrame parameter if it is possible in the
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
        return self.layout_2d_setting_att.SetClippingFrameLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_clipping_frame_lock'
        # # vba_code = """
        # # Public Function set_clipping_frame_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetClippingFrameLock iLocked
        # #     set_clipping_frame_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_clipping_frame_reframe_on_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetClippingFrameReframeOnModeLock(boolean iLocked)
                | 
                |     Deprecated:
                |         V5R18 Locks or unlocks the ClippingFrameReframeOnMode
                |         parameter.
                |         Role:Locks or unlocks the ClippingFrameReframeOnMode parameter if it is
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
        return self.layout_2d_setting_att.SetClippingFrameReframeOnModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_clipping_frame_reframe_on_mode_lock'
        # # vba_code = """
        # # Public Function set_clipping_frame_reframe_on_mode_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetClippingFrameReframeOnModeLock iLocked
        # #     set_clipping_frame_reframe_on_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_clipping_view_outline_colour(self, i_value_r: int, i_value_g: int, i_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetClippingViewOutlineColor(long iValueR,
                | long iValueG,
                | long iValueB)
                | 
                |     Sets the ClippingViewOutlineColor parameter.

        :param int i_value_r:
        :param int i_value_g:
        :param int i_value_b:
        :rtype: None
        """
        return self.layout_2d_setting_att.SetClippingViewOutlineColor(i_value_r, i_value_g, i_value_b)

    def set_clipping_view_outline_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetClippingViewOutlineColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the ClippingViewOutlineColor parameter.
                |     Role:Locks or unlocks the ClippingViewOutlineColor parameter if it is
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
        return self.layout_2d_setting_att.SetClippingViewOutlineColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_clipping_view_outline_color_lock'
        # # vba_code = """
        # # Public Function set_clipping_view_outline_color_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetClippingViewOutlineColorLock iLocked
        # #     set_clipping_view_outline_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_clipping_view_outline_linetype_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetClippingViewOutlineLinetypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ClippingViewOutlineLinetype
                |     parameter.
                |     Role:Locks or unlocks the ClippingViewOutlineLinetype parameter if it is
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
        return self.layout_2d_setting_att.SetClippingViewOutlineLinetypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_clipping_view_outline_linetype_lock'
        # # vba_code = """
        # # Public Function set_clipping_view_outline_linetype_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetClippingViewOutlineLinetypeLock iLocked
        # #     set_clipping_view_outline_linetype_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_clipping_view_outline_thickness_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetClippingViewOutlineThicknessLock(boolean iLocked)
                | 
                |     Locks or unlocks the ClippingViewOutlineThickness
                |     parameter.
                |     Role:Locks or unlocks the ClippingViewOutlineThickness parameter if it is
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
        return self.layout_2d_setting_att.SetClippingViewOutlineThicknessLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_clipping_view_outline_thickness_lock'
        # # vba_code = """
        # # Public Function set_clipping_view_outline_thickness_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetClippingViewOutlineThicknessLock iLocked
        # #     set_clipping_view_outline_thickness_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_create_associative_use_edges_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCreateAssociativeUseEdgesLock(boolean iLocked)
                | 
                |     Locks or unlocks the CreateAssociativeUseEdges parameter.
                |     Role:Locks or unlocks the CreateAssociativeUseEdges parameter if it is
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
        return self.layout_2d_setting_att.SetCreateAssociativeUseEdgesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_create_associative_use_edges_lock'
        # # vba_code = """
        # # Public Function set_create_associative_use_edges_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetCreateAssociativeUseEdgesLock iLocked
        # #     set_create_associative_use_edges_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dedicated_filter_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDedicatedFilterTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the DedicatedFilterType parameter.
                |     Role:Locks or unlocks the DedicatedFilterType parameter if it is possible
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
        return self.layout_2d_setting_att.SetDedicatedFilterTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dedicated_filter_type_lock'
        # # vba_code = """
        # # Public Function set_dedicated_filter_type_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetDedicatedFilterTypeLock iLocked
        # #     set_dedicated_filter_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_back_and_cutting_plane_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDisplayBackAndCuttingPlaneLock(boolean iLocked)
                | 
                |     Locks or unlocks the DisplayBackAndCuttingPlane parameter.
                |     Role:Locks or unlocks the DisplayBackAndCuttingPlane parameter if it is
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
        return self.layout_2d_setting_att.SetDisplayBackAndCuttingPlaneLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_back_and_cutting_plane_lock'
        # # vba_code = """
        # # Public Function set_display_back_and_cutting_plane_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetDisplayBackAndCuttingPlaneLock iLocked
        # #     set_display_back_and_cutting_plane_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_clipping_outline_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDisplayClippingOutlineLock(boolean iLocked)
                | 
                |     Locks or unlocks the DisplayClippingOutline parameter.
                |     Role:Locks or unlocks the DisplayClippingOutline parameter if it is
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
        return self.layout_2d_setting_att.SetDisplayClippingOutlineLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_clipping_outline_lock'
        # # vba_code = """
        # # Public Function set_display_clipping_outline_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetDisplayClippingOutlineLock iLocked
        # #     set_display_clipping_outline_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_edit_dedicated_filter_dialog_box_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetEditDedicatedFilterDialogBoxLock(boolean iLocked)
                | 
                |     Locks or unlocks the EditDedicatedFilterDialogBox
                |     parameter.
                |     Role:Locks or unlocks the EditDedicatedFilterDialogBox parameter if it is
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
        return self.layout_2d_setting_att.SetEditDedicatedFilterDialogBoxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_edit_dedicated_filter_dialog_box_lock'
        # # vba_code = """
        # # Public Function set_edit_dedicated_filter_dialog_box_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetEditDedicatedFilterDialogBoxLock iLocked
        # #     set_edit_dedicated_filter_dialog_box_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_fit_all_in_sheet_format_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetFitAllInSheetFormatLock(boolean iLocked)
                | 
                |     Locks or unlocks the FitAllInSheetFormat parameter.
                |     Role:Locks or unlocks the FitAllInSheetFormat parameter if it is possible
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
        return self.layout_2d_setting_att.SetFitAllInSheetFormatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_fit_all_in_sheet_format_lock'
        # # vba_code = """
        # # Public Function set_fit_all_in_sheet_format_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetFitAllInSheetFormatLock iLocked
        # #     set_fit_all_in_sheet_format_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_hide_in_3d_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetHideIn3DLock(boolean iLocked)
                | 
                |     Locks or unlocks the HideIn3D parameter.
                |     Role:Locks or unlocks the HideIn3D parameter if it is possible in the
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
        return self.layout_2d_setting_att.SetHideIn3DLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_hide_in3_d_lock'
        # # vba_code = """
        # # Public Function set_hide_in3_d_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetHideIn3DLock iLocked
        # #     set_hide_in3_d_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_insure_filter_names_uniqueness_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetInsureFilterNamesUniquenessLock(boolean iLocked)
                | 
                |     Locks or unlocks the InsureFilterNamesUniqueness
                |     parameter.
                |     Role:Locks or unlocks the InsureFilterNamesUniqueness if it is possible in
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
        return self.layout_2d_setting_att.SetInsureFilterNamesUniquenessLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_insure_filter_names_uniqueness_lock'
        # # vba_code = """
        # # Public Function set_insure_filter_names_uniqueness_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetInsureFilterNamesUniquenessLock iLocked
        # #     set_insure_filter_names_uniqueness_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_insure_sheet_names_uniqueness_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetInsureSheetNamesUniquenessLock(boolean iLocked)
                | 
                |     Locks or unlocks the InsureSheetNamesUniqueness parameter.
                |     Role:Locks or unlocks the InsureSheetNamesUniqueness parameter if it is
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
        return self.layout_2d_setting_att.SetInsureSheetNamesUniquenessLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_insure_sheet_names_uniqueness_lock'
        # # vba_code = """
        # # Public Function set_insure_sheet_names_uniqueness_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetInsureSheetNamesUniquenessLock iLocked
        # #     set_insure_sheet_names_uniqueness_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_insure_view_names_uniqueness_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetInsureViewNamesUniquenessLock(boolean iLocked)
                | 
                |     Locks or unlocks InsureViewNamesUniqueness parameter.
                |     Role:Locks or unlocks the InsureViewNamesUniqueness parameter if it is
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
        return self.layout_2d_setting_att.SetInsureViewNamesUniquenessLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_insure_view_names_uniqueness_lock'
        # # vba_code = """
        # # Public Function set_insure_view_names_uniqueness_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetInsureViewNamesUniquenessLock iLocked
        # #     set_insure_view_names_uniqueness_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_insure_view_names_uniqueness_scope_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetInsureViewNamesUniquenessScopeLock(boolean iLocked)
                | 
                |     Locks or unlocks the InsureViewNamesUniquenessScope
                |     parameter.
                |     Role:Locks or unlocks the InsureViewNamesUniquenessScope parameter if it is
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
        return self.layout_2d_setting_att.SetInsureViewNamesUniquenessScopeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_insure_view_names_uniqueness_scope_lock'
        # # vba_code = """
        # # Public Function set_insure_view_names_uniqueness_scope_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetInsureViewNamesUniquenessScopeLock iLocked
        # #     set_insure_view_names_uniqueness_scope_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_layout_default_render_style_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLayoutDefaultRenderStyleLock(boolean iLocked)
                | 
                |     Locks or unlocks the default render style parameter.
                |     Role:Locks or unlocks the default render style parameter if it is possible
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
        return self.layout_2d_setting_att.SetLayoutDefaultRenderStyleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_layout_default_render_style_lock'
        # # vba_code = """
        # # Public Function set_layout_default_render_style_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetLayoutDefaultRenderStyleLock iLocked
        # #     set_layout_default_render_style_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_propagate_highlight_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPropagateHighlightLock(boolean iLocked)
                | 
                |     Locks or unlocks the PropagateHighlight parameter.
                |     Role:Locks or unlocks the PropagateHighlight parameter if it is possible in
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
        return self.layout_2d_setting_att.SetPropagateHighlightLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_propagate_highlight_lock'
        # # vba_code = """
        # # Public Function set_propagate_highlight_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetPropagateHighlightLock iLocked
        # #     set_propagate_highlight_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_protected_elements_colour(self, i_value_r: int, i_value_g: int, i_value_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProtectedElementsColor(long iValueR,
                | long iValueG,
                | long iValueB)
                | 
                |     Sets the ProtectedElementsColor parameter.

        :param int i_value_r:
        :param int i_value_g:
        :param int i_value_b:
        :rtype: None
        """
        return self.layout_2d_setting_att.SetProtectedElementsColor(i_value_r, i_value_g, i_value_b)

    def set_protected_elements_colour_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetProtectedElementsColorLock(boolean iLocked)
                | 
                |     Locks or unlocks the ProtectedElementsColor parameter.
                |     Role:Locks or unlocks the ProtectedElementsColor parameter if it is
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
        return self.layout_2d_setting_att.SetProtectedElementsColorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_protected_elements_color_lock'
        # # vba_code = """
        # # Public Function set_protected_elements_color_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetProtectedElementsColorLock iLocked
        # #     set_protected_elements_color_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tile_layout_window_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTileLayoutWindowLock(boolean iLocked)
                | 
                |     Locks or unlocks the tile of Layout window parameter.
                |     Role:Locks or unlocks the tile of Layout window parameter if it is possible
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
        return self.layout_2d_setting_att.SetTileLayoutWindowLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tile_layout_window_lock'
        # # vba_code = """
        # # Public Function set_tile_layout_window_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetTileLayoutWindowLock iLocked
        # #     set_tile_layout_window_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_view_background_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetViewBackgroundModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ViewBackgroundMode parameter.
                |     Role:Locks or unlocks the ViewBackgroundMode parameter if it is possible in
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
        return self.layout_2d_setting_att.SetViewBackgroundModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_view_background_mode_lock'
        # # vba_code = """
        # # Public Function set_view_background_mode_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetViewBackgroundModeLock iLocked
        # #     set_view_background_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_view_filter_creation_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetViewFilterCreationModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ViewFilterCreationMode parameter.
                |     Role:Locks or unlocks the ViewFilterCreationMode parameter if it is
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
        return self.layout_2d_setting_att.SetViewFilterCreationModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_view_filter_creation_mode_lock'
        # # vba_code = """
        # # Public Function set_view_filter_creation_mode_lock(layout_2d_setting_att)
        # #     Dim iLocked (2)
        # #     layout_2d_setting_att.SetViewFilterCreationModeLock iLocked
        # #     set_view_filter_creation_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Layout2DSettingAtt(name="{self.name}")'
