#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class TreeVizManipSettingAtt(SettingController):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         TreeVizManipSettingAtt
                | 
                | The Interface to retrieve and set the visual information on the specification
                | tree.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tree_viz_manip_setting_att = com_object

    @property
    def arc_selection_activation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ArcSelectionActivation() As boolean
                | 
                |     Retrieves or Sets the arc-selection mode applied to the specification tree.

        :rtype: bool
        """

        return self.tree_viz_manip_setting_att.ArcSelectionActivation

    @arc_selection_activation.setter
    def arc_selection_activation(self, value: bool):
        """
        :param bool value:
        """

        self.tree_viz_manip_setting_att.ArcSelectionActivation = value

    @property
    def auto_expand_activation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AutoExpandActivation() As boolean
                | 
                |     Retrieves or Sets the automatic expand mode applied to the specification
                |     tree.

        :rtype: bool
        """

        return self.tree_viz_manip_setting_att.AutoExpandActivation

    @auto_expand_activation.setter
    def auto_expand_activation(self, value: bool):
        """
        :param bool value:
        """

        self.tree_viz_manip_setting_att.AutoExpandActivation = value

    @property
    def auto_scroll_activation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AutoScrollActivation() As boolean
                | 
                |     Retrieves or Sets the automatic scrolling mode applied to the specification
                |     tree.

        :rtype: bool
        """

        return self.tree_viz_manip_setting_att.AutoScrollActivation

    @auto_scroll_activation.setter
    def auto_scroll_activation(self, value: bool):
        """
        :param bool value:
        """

        self.tree_viz_manip_setting_att.AutoScrollActivation = value

    @property
    def display_geom_on_scrolling(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DisplayGeomOnScrolling() As boolean
                | 
                |     Retrieves or Sets the "display geometry on scrolling" mode.

        :rtype: bool
        """

        return self.tree_viz_manip_setting_att.DisplayGeomOnScrolling

    @display_geom_on_scrolling.setter
    def display_geom_on_scrolling(self, value: bool):
        """
        :param bool value:
        """

        self.tree_viz_manip_setting_att.DisplayGeomOnScrolling = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation() As CatTreeOrientationEnum
                | 
                |     Retrieves or Sets the orientation applied to the specification tree.

        :return: enum cat_tree_orientation_enum
        :rtype: int
        """

        return self.tree_viz_manip_setting_att.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value: enum cat_tree_orientation_enum
        """

        self.tree_viz_manip_setting_att.Orientation = value

    @property
    def show_activation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ShowActivation() As boolean
                | 
                |     Retrieves or Sets the visualization Show/NoShow's mode applied to the
                |     specification tree.

        :rtype: bool
        """

        return self.tree_viz_manip_setting_att.ShowActivation

    @show_activation.setter
    def show_activation(self, value: bool):
        """
        :param bool value:
        """

        self.tree_viz_manip_setting_att.ShowActivation = value

    @property
    def size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Size() As long
                | 
                |     Retrieves or Sets the number of characters shown for the text of the
                |     specification tree.

        :rtype: int
        """

        return self.tree_viz_manip_setting_att.Size

    @size.setter
    def size(self, value: int):
        """
        :param int value:
        """

        self.tree_viz_manip_setting_att.Size = value

    @property
    def size_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SizeType() As CatTreeSizeTypeEnum
                | 
                |     Retrieves or Sets the type of size applied to the text of the specification
                |     tree.

        :return: enum cat_tree_size_type_enum
        :rtype: int
        """

        return self.tree_viz_manip_setting_att.SizeType

    @size_type.setter
    def size_type(self, value: int):
        """
        :param int value: enum cat_tree_size_type_enum
        """

        self.tree_viz_manip_setting_att.SizeType = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Type() As CatTreeTypeEnum
                | 
                |     Retrieves or Sets the type applied to the specification tree.

        :return: enum cat_tree_type_enum
        :rtype: int
        """

        return self.tree_viz_manip_setting_att.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value: enum cat_tree_type_enum
        """

        self.tree_viz_manip_setting_att.Type = value

    def get_arc_selection_activation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetArcSelectionActivationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for arc-selection mode applied to the
                |     specification tree.
                |     Role:Retrieves the state of arc-selection mode applied to the specification
                |     tree in the current environment.
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
        return self.tree_viz_manip_setting_att.GetArcSelectionActivationInfo(io_admin_level, io_locked)

    def get_auto_expand_activation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAutoExpandActivationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for automatic expand mode applied to the
                |     specification tree.
                |     Role:Retrieves the state of automatic expand mode applied to the
                |     specification tree in the current environment.
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
        return self.tree_viz_manip_setting_att.GetAutoExpandActivationInfo(io_admin_level, io_locked)

    def get_auto_scroll_activation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAutoScrollActivationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for automatic scrolling mode applied to
                |     the specification tree.
                |     Role:Retrieves the state of the automatic scrolling mode applied to the
                |     specification tree in the current environment.
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
        return self.tree_viz_manip_setting_att.GetAutoScrollActivationInfo(io_admin_level, io_locked)

    def get_display_geom_on_scrolling_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDisplayGeomOnScrollingInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for "display geometry on scrolling"
                |     mode.
                |     Role:Retrieves the state of "display geometry on scrolling" mode in the
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
        return self.tree_viz_manip_setting_att.GetDisplayGeomOnScrollingInfo(io_admin_level, io_locked)

    def get_orientation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetOrientationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the orientation applied to the
                |     specification tree.
                |     Role:Retrieves the state of the orientation applied to the specification
                |     tree in the current environment.
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
        return self.tree_viz_manip_setting_att.GetOrientationInfo(io_admin_level, io_locked)

    def get_show_activation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetShowActivationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the visualization Show/NoShow's mode
                |     applied to the specification tree.
                |     Role:Retrieves the state of the visualization Show/NoShow's mode applied to
                |     the specification tree in the current environment.
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
        return self.tree_viz_manip_setting_att.GetShowActivationInfo(io_admin_level, io_locked)

    def get_size_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetSizeTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the type of size applied to the text
                |     of the specification tree.
                |     Role:Retrieves the state of the type of size applied to the text of the
                |     specification tree in the current environment. Attributes "size" and "SizeType"
                |     are linked together by the same lock. So there is no function
                |     "GetSizeInfo".
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
        return self.tree_viz_manip_setting_att.GetSizeTypeInfo(io_admin_level, io_locked)

    def get_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the type applied to the
                |     specification tree.
                |     Role:Retrieves the state of the type applied to the specification tree in
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
        return self.tree_viz_manip_setting_att.GetTypeInfo(io_admin_level, io_locked)

    def set_arc_selection_activation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetArcSelectionActivationLock(boolean iLocked)
                | 
                |     Locks or unlocks the arc-selection mode applied to the specification
                |     tree.
                |     Role:Locks or unlocks the arc-selection mode applied to the specification
                |     tree if it is possible in the current administrative context. In user mode this
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
        return self.tree_viz_manip_setting_att.SetArcSelectionActivationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_arc_selection_activation_lock'
        # # vba_code = """
        # # Public Function set_arc_selection_activation_lock(tree_viz_manip_setting_att)
        # #     Dim iLocked (2)
        # #     tree_viz_manip_setting_att.SetArcSelectionActivationLock iLocked
        # #     set_arc_selection_activation_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_auto_expand_activation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAutoExpandActivationLock(boolean iLocked)
                | 
                |     Locks or unlocks the automatic expand mode applied to the specification
                |     tree.
                |     Role:Locks or unlocks the automatic expand mode applied to the
                |     specification tree if it is possible in the current administrative context. In
                |     user mode this method will always return E_FAIL.
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
        return self.tree_viz_manip_setting_att.SetAutoExpandActivationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_expand_activation_lock'
        # # vba_code = """
        # # Public Function set_auto_expand_activation_lock(tree_viz_manip_setting_att)
        # #     Dim iLocked (2)
        # #     tree_viz_manip_setting_att.SetAutoExpandActivationLock iLocked
        # #     set_auto_expand_activation_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_auto_scroll_activation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAutoScrollActivationLock(boolean iLocked)
                | 
                |     Locks or unlocks the automatic scrolling mode applied to the specification
                |     tree.
                |     Role:Locks or unlocks the automatic scrolling mode applied to the
                |     specification tree if it is possible in the current administrative context. In
                |     user mode this method will always return E_FAIL.
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
        return self.tree_viz_manip_setting_att.SetAutoScrollActivationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auto_scroll_activation_lock'
        # # vba_code = """
        # # Public Function set_auto_scroll_activation_lock(tree_viz_manip_setting_att)
        # #     Dim iLocked (2)
        # #     tree_viz_manip_setting_att.SetAutoScrollActivationLock iLocked
        # #     set_auto_scroll_activation_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_geom_on_scrolling_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDisplayGeomOnScrollingLock(boolean iLocked)
                | 
                |     Locks or unlocks the "display geometry on scrolling" mode.
                |     Role:Locks or unlocks "display geometry on scrolling" mode if it is
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
        return self.tree_viz_manip_setting_att.SetDisplayGeomOnScrollingLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_geom_on_scrolling_lock'
        # # vba_code = """
        # # Public Function set_display_geom_on_scrolling_lock(tree_viz_manip_setting_att)
        # #     Dim iLocked (2)
        # #     tree_viz_manip_setting_att.SetDisplayGeomOnScrollingLock iLocked
        # #     set_display_geom_on_scrolling_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_orientation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetOrientationLock(boolean iLocked)
                | 
                |     Locks or unlocks the orientation applied to the specification
                |     tree.
                |     Role:Locks or unlocks the orientation applied to the specification tree if
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
        return self.tree_viz_manip_setting_att.SetOrientationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_orientation_lock'
        # # vba_code = """
        # # Public Function set_orientation_lock(tree_viz_manip_setting_att)
        # #     Dim iLocked (2)
        # #     tree_viz_manip_setting_att.SetOrientationLock iLocked
        # #     set_orientation_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_show_activation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetShowActivationLock(boolean iLocked)
                | 
                |     Locks or unlocks the visualization Show/NoShow's mode applied to the
                |     specification tree.
                |     Role:Locks or unlocks the visualization Show/NoShow's mode applied to the
                |     specification tree if it is possible in the current administrative context. In
                |     user mode this method will always return E_FAIL.
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
        return self.tree_viz_manip_setting_att.SetShowActivationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_show_activation_lock'
        # # vba_code = """
        # # Public Function set_show_activation_lock(tree_viz_manip_setting_att)
        # #     Dim iLocked (2)
        # #     tree_viz_manip_setting_att.SetShowActivationLock iLocked
        # #     set_show_activation_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_size_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSizeTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the type of size applied to the text of the specification
                |     tree.
                |     Role:Locks or unlocks the type of size applied to the text of the
                |     specification tree if it is possible in the current administrative context. In
                |     user mode this method will always return E_FAIL. Attributs "size" and
                |     "SizeType" are linked together by the same lock. So there is no function
                |     "SetSizeTypeLock".
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
        return self.tree_viz_manip_setting_att.SetSizeTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_size_type_lock'
        # # vba_code = """
        # # Public Function set_size_type_lock(tree_viz_manip_setting_att)
        # #     Dim iLocked (2)
        # #     tree_viz_manip_setting_att.SetSizeTypeLock iLocked
        # #     set_size_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the type of the specification tree.
                |     Role:Locks or unlocks the type applied to the specification tree if it is
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
        return self.tree_viz_manip_setting_att.SetTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_type_lock'
        # # vba_code = """
        # # Public Function set_type_lock(tree_viz_manip_setting_att)
        # #     Dim iLocked (2)
        # #     tree_viz_manip_setting_att.SetTypeLock iLocked
        # #     set_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'TreeVizManipSettingAtt(name="{self.name}")'
