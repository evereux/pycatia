#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class TreeTabSettingAtt(SettingController):

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
                |                         TreeTabSettingAtt

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.tree_tab_setting_att = com_object

    @property
    def applicative_data_filter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ApplicativeDataFilter() As long
                | 
                |     Returns of sets the value to signify Whether "Applicative Data" created by
                |     an application is visible in the PPR tree
                |     Role: Returns or sets the value of "Applicative Data" option to signify
                |     whether the applicative containers are visualized in the PPR tree

        :rtype: int
        """

        return self.tree_tab_setting_att.ApplicativeDataFilter

    @applicative_data_filter.setter
    def applicative_data_filter(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.ApplicativeDataFilter = value

    @property
    def assigned_viewer(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AssignedViewer() As long
                | 
                |     Returns or sets the value to signify whether the 3D Assigned Viewer is
                |     default viewer or not
                |     Role: Returns or sets the value to signify whether 3D Assigned Viewer is
                |     default viewer or not

        :rtype: int
        """

        return self.tree_tab_setting_att.AssignedViewer

    @assigned_viewer.setter
    def assigned_viewer(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.AssignedViewer = value

    @property
    def attributes_filter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttributesFilter() As long
                | 
                |     Returns or sets the value for "Attributes" option
                |     Role: Returns or sets the value of "Attributes" option to signify whether
                |     the 'User Attributes' of an Activity is visualized in the PPR tree

        :rtype: int
        """

        return self.tree_tab_setting_att.AttributesFilter

    @attributes_filter.setter
    def attributes_filter(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.AttributesFilter = value

    @property
    def collapse_expand_filter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CollapseExpandFilter() As long
                | 
                |     Returns or sets the value to signify Whether the double clicking on an
                |     activity expands/collapses a given activity in the PPR
                |     tree
                |     Role: Returns or sets the value to signify Whether the double clicking on
                |     an activity expands/collapses a given activity in the PPR tree

        :rtype: int
        """

        return self.tree_tab_setting_att.CollapseExpandFilter

    @collapse_expand_filter.setter
    def collapse_expand_filter(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.CollapseExpandFilter = value

    @property
    def display_name_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DisplayNameMode() As long
                | 
                |     Returns or sets the value to signify whether the E5 Configured Name is to
                |     be displayed
                |     Role: Returns or sets the value to signify whether the E5 Configured Name
                |     is to be displayed

        :rtype: int
        """

        return self.tree_tab_setting_att.DisplayNameMode

    @display_name_mode.setter
    def display_name_mode(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.DisplayNameMode = value

    @property
    def display_order(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DisplayOrder() As long
                | 
                |     Returns or sets the value for 'Display Order'
                |     Role: Returns or sets the value of 'Display Order' to signify which order
                |     the product/resource list are in the PPR tree

        :rtype: int
        """

        return self.tree_tab_setting_att.DisplayOrder

    @display_order.setter
    def display_order(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.DisplayOrder = value

    @property
    def display_process_order(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DisplayProcessOrder() As long
                | 
                |     Returns or sets the value for 'Display Order for
                |     Processes'
                |     Role: Returns or sets the value of 'Display Order for Processes' to signify
                |     which order the processes under ProcessList and ResourcesList are listed in the
                |     PPR tree. Legal values:
                |     1 : manufacturing hub order
                |     0 : loaded order

        :rtype: int
        """

        return self.tree_tab_setting_att.DisplayProcessOrder

    @display_process_order.setter
    def display_process_order(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.DisplayProcessOrder = value

    @property
    def items_filter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ItemsFilter() As long
                | 
                |     Returns or sets the value for 'Items Folder'
                |     Role: Returns or sets the value of 'Items Folder' to signify whether the
                |     'Assigned Items' are visualized in the PPR tree

        :rtype: int
        """

        return self.tree_tab_setting_att.ItemsFilter

    @items_filter.setter
    def items_filter(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.ItemsFilter = value

    @property
    def items_per_relation_filter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ItemsPerRelationFilter() As long
                | 
                |     Returns or sets the value for 'Items Folder (Per Relation
                |     Type)'
                |     Role: Returns or sets the value of 'Items Folder(Per Relation Type)' to
                |     signify whether the 'Assigned Items'with proper relations ( like First
                |     Processes Product) are visualized in the PPR tree

        :rtype: int
        """

        return self.tree_tab_setting_att.ItemsPerRelationFilter

    @items_per_relation_filter.setter
    def items_per_relation_filter(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.ItemsPerRelationFilter = value

    @property
    def logical_act_filter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LogicalActFilter() As long
                | 
                |     Returns or sets the value to signify Whether the logical activites are
                |     visible in the PPR tree
                |     Role: Returns or sets the value of "Logical Activities" option to signify
                |     whether the logical activites are visible in the PPR tree

        :rtype: int
        """

        return self.tree_tab_setting_att.LogicalActFilter

    @logical_act_filter.setter
    def logical_act_filter(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.LogicalActFilter = value

    @property
    def output_product_filter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property OutputProductFilter() As long
                | 
                |     Returns of sets the value to signify Whether "Output Products" assigned to
                |     a given activity is visible in the PPR tree
                |     Role: Returns or sets the value of "Output Products Folder" option to
                |     signify whether the output products associated with an activity are visualized
                |     in the PPR tree

        :rtype: int
        """

        return self.tree_tab_setting_att.OutputProductFilter

    @output_product_filter.setter
    def output_product_filter(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.OutputProductFilter = value

    @property
    def paste_same_instance(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PasteSameInstance() As long
                | 
                |     Returns or sets the value for 'Paste Same Instance'
                |     Role: Returns or sets the value of 'Paste Same Instance' to signify whether
                |     a same product instance in the target process document should be reused or not.
                |     Legal values:
                |     1 : Always paste an instance and do not reuse existing one
                |     0 : Reuse existing instance wherever possible

        :rtype: int
        """

        return self.tree_tab_setting_att.PasteSameInstance

    @paste_same_instance.setter
    def paste_same_instance(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.PasteSameInstance = value

    @property
    def render_style(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RenderStyle() As long
                | 
                |     Returns or sets the value to signify whether the 3D Render Style is
                |     Parallel or Perspective
                |     Role: Returns or sets the value to signify whether the 3D Render Style is
                |     Parallel or Perspective

        :rtype: int
        """

        return self.tree_tab_setting_att.RenderStyle

    @render_style.setter
    def render_style(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.RenderStyle = value

    @property
    def resource_filter(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ResourceFilter() As long
                | 
                |     Returns or sets the value for 'Resources Folder'
                |     Role: Returns or sets the value of 'Resources Folder' to signify whether
                |     the 'Assigned Resources' are visualized in the PPR tree

        :rtype: int
        """

        return self.tree_tab_setting_att.ResourceFilter

    @resource_filter.setter
    def resource_filter(self, value: int):
        """
        :param int value:
        """

        self.tree_tab_setting_att.ResourceFilter = value

    def get_applicative_data_filter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetApplicativeDataFilterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "Applicative Data"
                |     parameter.
                |     Role:Retrieves the state of the "Applicative Data" parameter in the current
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
        return self.tree_tab_setting_att.GetApplicativeDataFilterInfo(io_admin_level, io_locked)

    def get_assigned_viewer_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAssignedViewerInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "Assigned Viewer"
                |     parameter.
                |     Role:Retrieves the state of the "Assigned Viewer" parameter in the current
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
        return self.tree_tab_setting_att.GetAssignedViewerInfo(io_admin_level, io_locked)

    def get_attributes_filter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetAttributesFilterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "Attributes"
                |     parameter.
                |     Role:Retrieves the state of the "Attributes" parameter in the current
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
        return self.tree_tab_setting_att.GetAttributesFilterInfo(io_admin_level, io_locked)

    def get_collapse_expand_filter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetCollapseExpandFilterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "Disable Collapse/Expand"
                |     parameter.
                |     Role:Retrieves the state of the "Disable Collapse/Expand" parameter in the
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
        return self.tree_tab_setting_att.GetCollapseExpandFilterInfo(io_admin_level, io_locked)

    def get_display_name_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDisplayNameModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "Display Name Mode"
                |     parameter.
                |     Role:Retrieves the state of the "Display Name Mode" parameter in the
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
        return self.tree_tab_setting_att.GetDisplayNameModeInfo(io_admin_level, io_locked)

    def get_display_order_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDisplayOrderInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the 'Display Order'
                |     parameter.
                |     Role:Retrieves the state of the 'Display Order' parameter in the current
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
        return self.tree_tab_setting_att.GetDisplayOrderInfo(io_admin_level, io_locked)

    def get_display_process_order_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetDisplayProcessOrderInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the 'Display Order for Processes'
                |     parameter.
                |     Role:Retrieves the state of the 'Display Order for Processes' parameter in
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
        return self.tree_tab_setting_att.GetDisplayProcessOrderInfo(io_admin_level, io_locked)

    def get_items_filter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetItemsFilterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the 'Items Folder'
                |     parameter.
                |     Role:Retrieves the state of the 'Items Folder' parameter in the current
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
        return self.tree_tab_setting_att.GetItemsFilterInfo(io_admin_level, io_locked)

    def get_items_per_relation_filter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetItemsPerRelationFilterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the 'Items Folder(Per Relation
                |     Type)' parameter.
                |     Role:Retrieves the state of the 'Items Folder(Per Relation Type)' parameter
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
        return self.tree_tab_setting_att.GetItemsPerRelationFilterInfo(io_admin_level, io_locked)

    def get_logical_act_filter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetLogicalActFilterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "Logical Activities"
                |     parameter.
                |     Role:Retrieves the state of the "Logical Activities" parameter in the
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
        return self.tree_tab_setting_att.GetLogicalActFilterInfo(io_admin_level, io_locked)

    def get_output_product_filter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetOutputProductFilterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "Output Products Folder"
                |     parameter.
                |     Role:Retrieves the state of the "Output Products Folder" parameter in the
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
        return self.tree_tab_setting_att.GetOutputProductFilterInfo(io_admin_level, io_locked)

    def get_paste_same_instance_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetPasteSameInstanceInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment information for the 'Paste Same Instance'
                |     parameter.
                |     Role:Retrieves the state of the 'Paste Same Instance' parameter in the
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
        return self.tree_tab_setting_att.GetPasteSameInstanceInfo(io_admin_level, io_locked)

    def get_render_style_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRenderStyleInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "Render Style"
                |     parameter.
                |     Role:Retrieves the state of the "Render Style" parameter in the current
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
        return self.tree_tab_setting_att.GetRenderStyleInfo(io_admin_level, io_locked)

    def get_resource_filter_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetResourceFilterInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the 'Resource Folder'
                |     parameter.
                |     Role:Retrieves the state of the 'Resource Folder' parameter in the current
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
        return self.tree_tab_setting_att.GetResourceFilterInfo(io_admin_level, io_locked)

    def set_applicative_data_filter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetApplicativeDataFilterLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Applicative Data" parameter.
                |     Role:Locks or unlocks the "Attributes" parameter if it is possible in the
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
        return self.tree_tab_setting_att.SetApplicativeDataFilterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_applicative_data_filter_lock'
        # # vba_code = """
        # # Public Function set_applicative_data_filter_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetApplicativeDataFilterLock iLocked
        # #     set_applicative_data_filter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_assigned_viewer_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAssignedViewerLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Assigned Viewer" parameter.
                |     Role:Locks or unlocks the "Assigned Viewer" parameter if it is possible in
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
        return self.tree_tab_setting_att.SetAssignedViewerLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_assigned_viewer_lock'
        # # vba_code = """
        # # Public Function set_assigned_viewer_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetAssignedViewerLock iLocked
        # #     set_assigned_viewer_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_attributes_filter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAttributesFilterLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Attributes" parameter.
                |     Role:Locks or unlocks the "Attributes" parameter if it is possible in the
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
        return self.tree_tab_setting_att.SetAttributesFilterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_attributes_filter_lock'
        # # vba_code = """
        # # Public Function set_attributes_filter_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetAttributesFilterLock iLocked
        # #     set_attributes_filter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_collapse_expand_filter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCollapseExpandFilterLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Disable Collapse/Expand" parameter.
                |     Role:Locks or unlocks the "Disable Collapse/Expand" parameter if it is
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
        return self.tree_tab_setting_att.SetCollapseExpandFilterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_collapse_expand_filter_lock'
        # # vba_code = """
        # # Public Function set_collapse_expand_filter_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetCollapseExpandFilterLock iLocked
        # #     set_collapse_expand_filter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_name_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDisplayNameModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Display Name Mode" parameter.
                |     Role:Locks or unlocks the "Display Name Mode" parameter if it is possible
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
        return self.tree_tab_setting_att.SetDisplayNameModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_name_mode_lock'
        # # vba_code = """
        # # Public Function set_display_name_mode_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetDisplayNameModeLock iLocked
        # #     set_display_name_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_order_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDisplayOrderLock(boolean iLocked)
                | 
                |     Locks or unlocks the 'Display Order' parameter.
                |     Role:Locks or unlocks the 'Display Order' parameter if it is possible in
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
        return self.tree_tab_setting_att.SetDisplayOrderLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_order_lock'
        # # vba_code = """
        # # Public Function set_display_order_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetDisplayOrderLock iLocked
        # #     set_display_order_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_process_order_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetDisplayProcessOrderLock(boolean iLocked)
                | 
                |     Locks or unlocks the 'Display Order for Processes'
                |     parameter.
                |     Role:Locks or unlocks the 'Display Order for Processes' parameter if it is
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
        return self.tree_tab_setting_att.SetDisplayProcessOrderLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_process_order_lock'
        # # vba_code = """
        # # Public Function set_display_process_order_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetDisplayProcessOrderLock iLocked
        # #     set_display_process_order_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_items_filter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetItemsFilterLock(boolean iLocked)
                | 
                |     Locks or unlocks the 'Items Folder' parameter.
                |     Role:Locks or unlocks the 'Items Folder' parameter if it is possible in the
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
        return self.tree_tab_setting_att.SetItemsFilterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_items_filter_lock'
        # # vba_code = """
        # # Public Function set_items_filter_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetItemsFilterLock iLocked
        # #     set_items_filter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_items_per_relation_filter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetItemsPerRelationFilterLock(boolean iLocked)
                | 
                |     Locks or unlocks the 'Items Folde(Per Relation Type)r'
                |     parameter.
                |     Role:Locks or unlocks the 'Items Folder(Per Relation Type)' parameter if it
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
        return self.tree_tab_setting_att.SetItemsPerRelationFilterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_items_per_relation_filter_lock'
        # # vba_code = """
        # # Public Function set_items_per_relation_filter_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetItemsPerRelationFilterLock iLocked
        # #     set_items_per_relation_filter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_logical_act_filter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetLogicalActFilterLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Logical Activities" parameter.
                |     Role:Locks or unlocks the "Logical Activities" parameter if it is possible
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
        return self.tree_tab_setting_att.SetLogicalActFilterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_logical_act_filter_lock'
        # # vba_code = """
        # # Public Function set_logical_act_filter_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetLogicalActFilterLock iLocked
        # #     set_logical_act_filter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_output_product_filter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOutputProductFilterLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Output Products Folder" parameter.
                |     Role:Locks or unlocks the "Output Products Folder" parameter if it is
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
        return self.tree_tab_setting_att.SetOutputProductFilterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_output_product_filter_lock'
        # # vba_code = """
        # # Public Function set_output_product_filter_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetOutputProductFilterLock iLocked
        # #     set_output_product_filter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_paste_same_instance_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPasteSameInstanceLock(boolean iLocked)
                | 
                |     Locks or unlocks the 'Paste Same Instance' parameter.
                |     Role:Locks or unlocks the 'Paste Same Instance' parameter if it is possible
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
        return self.tree_tab_setting_att.SetPasteSameInstanceLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_paste_same_instance_lock'
        # # vba_code = """
        # # Public Function set_paste_same_instance_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetPasteSameInstanceLock iLocked
        # #     set_paste_same_instance_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_render_style_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetRenderStyleLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Render Style" parameter.
                |     Role:Locks or unlocks the "Render Style" parameter if it is possible in the
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
        return self.tree_tab_setting_att.SetRenderStyleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_render_style_lock'
        # # vba_code = """
        # # Public Function set_render_style_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetRenderStyleLock iLocked
        # #     set_render_style_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_resource_filter_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetResourceFilterLock(boolean iLocked)
                | 
                |     Locks or unlocks the 'Resource Folder' parameter.
                |     Role:Locks or unlocks the 'Resource Folder' parameter if it is possible in
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
        return self.tree_tab_setting_att.SetResourceFilterLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_resource_filter_lock'
        # # vba_code = """
        # # Public Function set_resource_filter_lock(tree_tab_setting_att)
        # #     Dim iLocked (2)
        # #     tree_tab_setting_att.SetResourceFilterLock iLocked
        # #     set_resource_filter_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'TreeTabSettingAtt(name="{ self.name }")'
