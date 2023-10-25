#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class PartInfrastructureSettingAtt(SettingController):
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
                |                         PartInfrastructureSettingAtt
                | 
                | Setting controller for all the Part Infrastructure property tab
                | pages.
                | Role: This interface is implemented by a component representing the controller
                | for the Part Infrastructure settings.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.part_infrastructure_setting_att = com_object

    @property
    def also_delete_exclusive_parents(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AlsoDeleteExclusiveParents() As boolean
                | 
                |     Returns or sets the "AlsoDeleteExclusiveParents"
                |     parameter.
                |     Role: This parameter defines if a exclusive parents of an object will also
                |     be deleted when the object is deleted.
                |     This option is effective only when the "Deletion warning box" is
                |     displayed.
                | 
                |     Parameters:
                | 
                |         oDeleted
                |             Current "AlsoDeleteExclusiveParents" parameter's
                |             value:
                | 
                |                 TRUE or 1 if exclusive parents are also
                |                 deleted,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.AlsoDeleteExclusiveParents

    @also_delete_exclusive_parents.setter
    def also_delete_exclusive_parents(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.AlsoDeleteExclusiveParents = value

    @property
    def axis_system_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AxisSystemSize() As short
                | 
                |     Returns or sets the "AxisSystemSize" parameter.
                |     Role: This parameter determines the size of axis systems.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Current size of axis systems 
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: int
        """

        return self.part_infrastructure_setting_att.AxisSystemSize

    @axis_system_size.setter
    def axis_system_size(self, value: int):
        """
        :param int value:
        """

        self.part_infrastructure_setting_att.AxisSystemSize = value

    @property
    def bodies_under_operations_in_tree(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BodiesUnderOperationsInTree() As boolean
                | 
                |     Returns or sets the "BodiesUnderOperationsInTree"
                |     parameter.
                |     Role: This parameter determines if a Body node is displayed when it is
                |     being aggregated under a boolean operation (Add, Assemble, Remove, Intersect,
                |     Union Trim).
                |     Its value can be changed even after a boolean operation has been created.
                |     Simply collapse and expand the federating boolean operation node for the
                |     specification tree to be refreshed.
                | 
                |     Parameters:
                | 
                |         oNodeDisplayed
                |             Current "BodiesUnderOperationsInTree" parameter's
                |             value:
                | 
                |                 TRUE or 1 if such a node is displayed,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.BodiesUnderOperationsInTree

    @bodies_under_operations_in_tree.setter
    def bodies_under_operations_in_tree(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.BodiesUnderOperationsInTree = value

    @property
    def color_synchronization_editability(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ColorSynchronizationEditability() As boolean
                | 
                |     Returns or sets the "ColorSynchronizationEditability"
                |     parameter.
                |     Role: This parameter determines whether color synchronization property on
                |     Part is editable or not.
                |     Color synchronization editability defines whether the property of
                |     synchronization on Part can be interactively editable If it is valuated to 1,
                |     user will be able to interactively modify the Part property of Color management
                |     tab for synchronization. If it is defined to 0, user will not be able to
                |     interactively modify the Part property of Color management tab for
                |     synchronization. This option cannot be changed after a document has been
                |     opened.
                | 
                |     Parameters:
                | 
                |         oActivated
                |             Current "ColorSynchronizationEditability" parameter's
                |             value:
                | 
                |                 TRUE or 1, Part property option for synchronization is
                |                 editable
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ColorSynchronizationEditability

    @color_synchronization_editability.setter
    def color_synchronization_editability(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ColorSynchronizationEditability = value

    @property
    def color_synchronization_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ColorSynchronizationMode() As boolean
                | 
                |     Returns or sets the "ColorSynchronizationMode" parameter.
                |     Role: This parameter determines color synchronization mode for imported
                |     features in a part.
                |     Color synchronization mode defines whether the imported feature, created
                |     through copy/paste as result with link mechanism, copies reference feature
                |     colors on its faces or not. If it is valuated to 1, synchronization will be
                |     effective and referece feature colors will be reported. If it is defined to 0,
                |     nothing will be copied(default mode). This option cannot be changed after a
                |     document has been opened.
                | 
                |     Parameters:
                | 
                |         oActivated
                |             Current "ColorSynchronizationMode" parameter's
                |             value:
                | 
                |                 TRUE or 1 if reference feature colors are reported on imported
                |                 feature,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ColorSynchronizationMode

    @color_synchronization_mode.setter
    def color_synchronization_mode(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ColorSynchronizationMode = value

    @property
    def color_synchronization_mode_manage(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ColorSynchronizationModeManage() As boolean
                | 
                |     Returns or sets the "ColorSynchronizationModeManage"
                |     parameter.
                |     Role: This parameter determines access to specific color synchronization
                |     mode for imported features in a part.
                |     Color synchronization mode Manage defines if access is granted to color
                |     synchronization suboptions "on feature" and "on subelements". If it is valuated
                |     to 1, access will be granted. If it is defined to 0, no acces to color on
                |     feature & color on subelements options
                | 
                |     Parameters:
                | 
                |         oActivated
                |             Current "ColorSynchronizationModeManage" parameter's
                |             value:
                | 
                |                 TRUE or 1 if possibility to chose specific color copy
                |                 parameters
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ColorSynchronizationModeManage

    @color_synchronization_mode_manage.setter
    def color_synchronization_mode_manage(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ColorSynchronizationModeManage = value

    @property
    def color_synchronization_mode_on_feature(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ColorSynchronizationModeOnFeature() As boolean
                | 
                |     Returns or sets the "ColorSynchronizationModeOnFeature"
                |     parameter.
                |     Role: This parameter determines graphic properties synchronization mode on
                |     feature for imported features in a part.
                |     Color synchronization mode defines whether the imported feature, created
                |     through copy/paste as result with link mechanism, copies reference feature
                |     graphic properties or not. If it is valuated to 1, synchronization will be
                |     effective and referece feature graphic properties will be reported. If it is
                |     defined to 0, nothing will be copied(default mode).
                | 
                |     Parameters:
                | 
                |         oActivated
                |             Current "ColorSynchronizationModeOnFeature" parameter's
                |             value:
                | 
                |                 TRUE or 1 if reference feature graphic properties are reported
                |                 on imported feature,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ColorSynchronizationModeOnFeature

    @color_synchronization_mode_on_feature.setter
    def color_synchronization_mode_on_feature(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ColorSynchronizationModeOnFeature = value

    @property
    def color_synchronization_mode_on_sub_elements(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ColorSynchronizationModeOnSubElements() As boolean
                | 
                |     Returns or sets the "ColorSynchronizationModeOnSubElements"
                |     parameter.
                |     Role: This parameter determines color synchronization mode for imported
                |     features in a part.
                |     Color synchronization mode OnSubElements defines whether the imported
                |     feature, created through copy/paste as result with link mechanism, copies
                |     reference feature colors on his overloaded faces or not. If it is valuated to
                |     1, synchronization will be effective and reference subelements colors will be
                |     reported. If it is defined to 0, nothing will be copied(default
                |     mode).
                | 
                |     Parameters:
                | 
                |         oActivated
                |             Current "ColorSynchronizationModeOnSubElements" parameter's
                |             value:
                | 
                |                 TRUE or 1 if reference subelements colors are reported on
                |                 imported feature,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ColorSynchronizationModeOnSubElements

    @color_synchronization_mode_on_sub_elements.setter
    def color_synchronization_mode_on_sub_elements(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ColorSynchronizationModeOnSubElements = value

    @property
    def colors3_d_experience_management(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Colors3DExperienceManagement() As boolean
                | 
                |     Returns or sets the "Colors3DExperienceManagement"
                |     parameter.
                |     Role: This parameter determines whether color synchronization property on
                |     Part is editable or not.
                |     Color synchronization editability defines whether the property of
                |     synchronization on Part can be interactively editable If it is valuated to 1,
                |     user will be able to interactively modify the Part property of Color management
                |     tab for synchronization. If it is defined to 0, user will not be able to
                |     interactively modify the Part property of Color management tab for
                |     synchronization. This option cannot be changed after a document has been
                |     opened.
                | 
                |     Parameters:
                | 
                |         oActivated
                |             Current "Colors3DExperienceManagement" parameter's
                |             value:
                | 
                |                 TRUE or 1, Part property option for synchronization is
                |                 editable
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.Colors3DExperienceManagement

    @colors3_d_experience_management.setter
    def colors3_d_experience_management(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.Colors3DExperienceManagement = value

    @property
    def constraints_in_geometry(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ConstraintsInGeometry() As boolean
                | 
                |     Returns or sets the "ConstraintsInGeometry" parameter.
                |     Role: This parameter enables constraints to be visualized in the 3D
                |     view.
                | 
                |     Parameters:
                | 
                |         oDisplayed
                |             Current "Display constraints within 3D" parameter's
                |             value:
                | 
                |                 TRUE or 1 if constraints are displayed,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ConstraintsInGeometry

    @constraints_in_geometry.setter
    def constraints_in_geometry(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ConstraintsInGeometry = value

    @property
    def constraints_node_in_tree(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ConstraintsNodeInTree() As boolean
                | 
                |     Returns or sets the "ConstraintsNodeInTree" parameter.
                |     Role: This parameter determines if a node called "Constraints" is created
                |     to contain all constraints.
                |     Its value can be changed even after constraints have been created. The
                |     result is that the specification tree node display status will be
                |     affected.
                | 
                |     Parameters:
                | 
                |         oNodeDisplayed
                |             Current "ConstraintsNodeInTree" parameter's value:
                | 
                |                 TRUE or 1 if such a node is displayed,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ConstraintsNodeInTree

    @constraints_node_in_tree.setter
    def constraints_node_in_tree(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ConstraintsNodeInTree = value

    @property
    def contextual_features_selectable_at_creation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ContextualFeaturesSelectableAtCreation() As
                | boolean
                | 
                |     Returns or sets the "ContextualFeaturesSelectableAtCreation"
                |     parameter.
                |     Role: This parameter determines if contextual features can be selected
                |     during the creation of an other feature.
                | 
                |     Parameters:
                | 
                |         oContextualFeaturesSelectable
                |             Current "ContextualFeaturesSelectableAtCreation" parameter's
                |             value:
                | 
                |                 TRUE or 1 if contextual features can be
                |                 selected,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ContextualFeaturesSelectableAtCreation

    @contextual_features_selectable_at_creation.setter
    def contextual_features_selectable_at_creation(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ContextualFeaturesSelectableAtCreation = value

    @property
    def default_colors_editability(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DefaultColorsEditability() As boolean
                | 
                |     Returns or sets the "DefaultColorsEditability" parameter.
                |     Role: This parameter determines whether color synchronization property on
                |     Part is editable or not.
                |     Color synchronization editability defines whether the property of
                |     synchronization on Part can be interactively editable If it is valuated to 1,
                |     user will be able to interactively modify the Part property of Color management
                |     tab for synchronization. If it is defined to 0, user will not be able to
                |     interactively modify the Part property of Color management tab for
                |     synchronization. This option cannot be changed after a document has been
                |     opened.
                | 
                |     Parameters:
                | 
                |         oActivated
                |             Current "DefaultColorsEditability" parameter's
                |             value:
                | 
                |                 TRUE or 1, Part property option for synchronization is
                |                 editable
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.DefaultColorsEditability

    @default_colors_editability.setter
    def default_colors_editability(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.DefaultColorsEditability = value

    @property
    def delete_warning_box(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DeleteWarningBox() As boolean
                | 
                |     Returns or sets the "DeleteWarningBox" parameter.
                |     Role: This parameter defines if a warning box is displayed when an element
                |     is deleted.
                | 
                |     Parameters:
                | 
                |         oDisplayed
                |             Current "DeleteWarningBox" parameter's value:
                | 
                |                 TRUE or 1 if a warning box is displayed at
                |                 deletion,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.DeleteWarningBox

    @delete_warning_box.setter
    def delete_warning_box(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.DeleteWarningBox = value

    @property
    def display_geometry_after_current(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DisplayGeometryAfterCurrent() As boolean
                | 
                |     Returns or sets the "DisplayGeometryAfterCurrent"
                |     parameter.
                |     Role: This parameter enables to visualize in the 3D features after the
                |     current object in O.G.S. and "solid and surface set".
                | 
                |     Parameters:
                | 
                |         oDisplayed
                |             Current "DisplayGeometryAfterCurrent" parameter's
                |             value:
                | 
                |                 TRUE or 1 if such is the visualization,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.DisplayGeometryAfterCurrent

    @display_geometry_after_current.setter
    def display_geometry_after_current(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.DisplayGeometryAfterCurrent = value

    @property
    def expand_sketch_based_features_node_at_creation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExpandSketchBasedFeaturesNodeAtCreation() As
                | boolean
                | 
                |     Returns or sets the "ExpandSketchBasedFeaturesNodeAtCreation"
                |     parameter.
                |     Role: This parameter determines if specification tree nodes for
                |     sketch-based features are expanded when such elements are created. This will
                |     enable to view their sketch node.
                | 
                |     Parameters:
                | 
                |         oNodeExpanded
                |             Current "ExpandSketchBasedFeaturesNodeAtCreation" parameter's
                |             value:
                | 
                |                 TRUE or 1 if such nodes are expanded,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ExpandSketchBasedFeaturesNodeAtCreation

    @expand_sketch_based_features_node_at_creation.setter
    def expand_sketch_based_features_node_at_creation(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ExpandSketchBasedFeaturesNodeAtCreation = value

    @property
    def external_references_as_visible(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExternalReferencesAsVisible() As boolean
                | 
                |     Returns or sets the "ExternalReferencesAsVisible"
                |     parameter.
                |     Role: This parameter defines if an external reference is visible when being
                |     created.
                | 
                |     Parameters:
                | 
                |         oVisible
                |             Current "ExternalReferencesAsVisible" parameter's
                |             value:
                | 
                |                 TRUE or 1 if external references are visible when being
                |                 created,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ExternalReferencesAsVisible

    @external_references_as_visible.setter
    def external_references_as_visible(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ExternalReferencesAsVisible = value

    @property
    def external_references_assembly_root_context(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExternalReferencesAssemblyRootContext() As boolean
                | 
                |     Returns or sets the "ExternalReferencesAssemblyRootContext"
                |     parameter.
                |     Role: This parameter defines if external references are created using the
                |     root context of an assembly.
                | 
                |     Parameters:
                | 
                |         oRootContextUsed
                |             Current "ExternalReferencesAssemblyRootContext" parameter's
                |             value:
                | 
                |                 TRUE or 1 if external references are created using the root
                |                 context of an assembly,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ExternalReferencesAssemblyRootContext

    @external_references_assembly_root_context.setter
    def external_references_assembly_root_context(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ExternalReferencesAssemblyRootContext = value

    @property
    def external_references_node_in_tree(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExternalReferencesNodeInTree() As boolean
                | 
                |     Returns or sets the "ExternalReferencesNodeInTree"
                |     parameter.
                |     Role: This parameter determines if a node called "External Reference" is
                |     created to contain all linked external references.
                |     Its value can be changed even after linked external references have been
                |     created. The result is that the specification tree node display status will be
                |     affected.
                | 
                |     Parameters:
                | 
                |         oNodeDisplayed
                |             Current "ExternalReferencesNodeInTree" parameter's
                |             value:
                | 
                |                 TRUE or 1 if such a node is displayed,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ExternalReferencesNodeInTree

    @external_references_node_in_tree.setter
    def external_references_node_in_tree(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ExternalReferencesNodeInTree = value

    @property
    def hybrid_design_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HybridDesignMode() As boolean
                | 
                |     Returns or sets the "HybridDesignMode" parameter.
                |     Role: This parameter determines if hybrid design is possible inside Part
                |     Bodies and bodies.
                |     This option can be changed even after a document has been
                |     opened.
                | 
                |     Parameters:
                | 
                |         oHybridDesign
                |             Current "HybridDesignMode" parameter's value:
                | 
                |                 TRUE or 1 if hybrid design is enabled,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.HybridDesignMode

    @hybrid_design_mode.setter
    def hybrid_design_mode(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.HybridDesignMode = value

    @property
    def knowledge_in_hybrid_design_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property KnowledgeInHybridDesignMode() As boolean
                | 
                |     Returns or sets the "KnowledgeInHybridDesignMode"
                |     parameter.
                |     Role: This parameter determines if knowledge features (formulas,
                |     parameters, rules, ...) can be located inside ordered
                |     sets.
                |     This option can be changed even after a document has been
                |     opened.
                | 
                |     Parameters:
                | 
                |         oKnowledgeInHybridDesign
                |             Current "KnowledgeInHybridDesignMode" parameter's
                |             value:
                | 
                |                 TRUE or 1 if hybrid design is enabled,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.KnowledgeInHybridDesignMode

    @knowledge_in_hybrid_design_mode.setter
    def knowledge_in_hybrid_design_mode(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.KnowledgeInHybridDesignMode = value

    @property
    def linked_external_references(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LinkedExternalReferences() As boolean
                | 
                |     Returns or sets the "LinkedExternalReferences" parameter.
                |     Role: This parameter enables creation of external references with
                |     links.
                | 
                |     Parameters:
                | 
                |         oWithLink
                |             "LinkedExternalReferences" parameter's value:
                | 
                |                 TRUE or 1 if external references are created with
                |                 links,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.LinkedExternalReferences

    @linked_external_references.setter
    def linked_external_references(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.LinkedExternalReferences = value

    @property
    def linked_external_references_only_on_publication(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LinkedExternalReferencesOnlyOnPublication() As
                | boolean
                | 
                |     Returns or sets the "LinkedExternalReferencesOnlyOnPublication"
                |     parameter.
                |     Role: This parameter restricts the creation of external references with
                |     links to only published elements.
                |     This option is only used when external references are created with
                |     link.
                | 
                |     Parameters:
                | 
                |         oOnlyForPublishedElements
                |             Current "LinkedExternalReferencesOnlyOnPublication" parameter's
                |             value:
                | 
                |                 TRUE or 1 if external references with link are only allowed on
                |                 published elements,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.LinkedExternalReferencesOnlyOnPublication

    @linked_external_references_only_on_publication.setter
    def linked_external_references_only_on_publication(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.LinkedExternalReferencesOnlyOnPublication = value

    @property
    def linked_external_references_warning_at_creation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LinkedExternalReferencesWarningAtCreation() As
                | boolean
                | 
                |     Returns or sets the "LinkedExternalReferencesWarningAtCreation"
                |     parameter.
                |     Role: This parameter defines if a warning panel is displayed each time an
                |     external reference with llink is created. The panel enables the user to decide
                |     whether the link will be kept or not.
                |     This option is only used when external references are created with
                |     link.
                | 
                |     Parameters:
                | 
                |         oWarningAtCreation
                |             Current "LinkedExternalReferencesWarningAtCreation" parameter's
                |             value:
                | 
                |                 TRUE or 1 if a panel is displayed upon external references with
                |                 link creation,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.LinkedExternalReferencesWarningAtCreation

    @linked_external_references_warning_at_creation.setter
    def linked_external_references_warning_at_creation(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.LinkedExternalReferencesWarningAtCreation = value

    @property
    def naming_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NamingMode() As CatPartElementsNamingMode
                | 
                |     Returns or sets the "NamingMode" parameter.
                |     Role: This parameter determines how an element can be named through
                |     Edit/Properties or any operation creating a feature (Copy-Paste,
                |     etc.).
                |     When this option is being changed, it only affects elements whose name is
                |     modified afterwards.
                | 
                |     Parameters:
                | 
                |         oNamingMode
                |             Current "NamingMode" parameter's value:
                | 
                |                 catNoCheck when naming is rule-free,
                |                 catNamingCheckUnderSameNode when 2 elements cannot have the
                |                 same name under the same node,
                |                 catNamingCheckWithinUIActiveObject when 2 elements cannot have
                |                 the same name within a defined UIActiveObject.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :return: enum cat_part_elements_naming_mode
        :rtype: int
        """

        return self.part_infrastructure_setting_att.NamingMode

    @naming_mode.setter
    def naming_mode(self, value: int):
        """
        :param int value: enum cat_part_elements_naming_mode
        """

        self.part_infrastructure_setting_att.NamingMode = value

    @property
    def new_with3_d_support(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NewWith3DSupport() As boolean
                | 
                |     Returns or sets the "NewWith3DSupport" parameter.
                |     Role: This parameter determines if a new .CATPart document will be created
                |     with 3D working support.
                | 
                |     Parameters:
                | 
                |         o3DSupportCreated
                |             Current "NewWith3DSupport" parameter's value:
                | 
                |                 TRUE or 1 if a 3D support is created,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.NewWith3DSupport

    @new_with3_d_support.setter
    def new_with3_d_support(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.NewWith3DSupport = value

    @property
    def new_with_axis_system(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NewWithAxisSystem() As boolean
                | 
                |     Returns or sets the "NewWithAxisSystem" parameter.
                |     Role: This parameter determines if a new .CATPart document will be created
                |     with an Axis System.
                | 
                |     Parameters:
                | 
                |         oAxisSystemCreated
                |             Current "NewWithAxisSystem" parameter's value:
                | 
                |                 TRUE or 1 if an axis system is created,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.NewWithAxisSystem

    @new_with_axis_system.setter
    def new_with_axis_system(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.NewWithAxisSystem = value

    @property
    def new_with_gs(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NewWithGS() As boolean
                | 
                |     Returns or sets the "NewWithGS" parameter.
                |     Role: This parameter determines if a new .CATPart document will be created
                |     with a Geometrical Set.
                | 
                |     Parameters:
                | 
                |         oGSCreated
                |             Current "NewWithGS" parameter's value:
                | 
                |                 TRUE or 1 if a G.S. is created,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.NewWithGS

    @new_with_gs.setter
    def new_with_gs(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.NewWithGS = value

    @property
    def new_with_ogs(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NewWithOGS() As boolean
                | 
                |     Returns or sets the "NewWithOGS" parameter.
                |     Role: This parameter determines if a new .CATPart document will be created
                |     with an Ordered Geometrical Set.
                | 
                |     Parameters:
                | 
                |         oOGSCreated
                |             Current "NewWithOGS" parameter's value:
                | 
                |                 TRUE or 1 if an O.G.S. is created,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.NewWithOGS

    @new_with_ogs.setter
    def new_with_ogs(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.NewWithOGS = value

    @property
    def new_with_panel(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NewWithPanel() As boolean
                | 
                |     Returns or sets the "NewWithPanel" parameter.
                |     Role: This parameter determines if a dedicated 'New Part' panel is
                |     displayed when createing a new .CATPart document.
                | 
                |     Parameters:
                | 
                |         oNewPartPanelDisplayed
                |             Current "NewWithPanel" parameter's value:
                | 
                |                 TRUE or 1 if the 'New Part' panel is
                |                 displayed,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.NewWithPanel

    @new_with_panel.setter
    def new_with_panel(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.NewWithPanel = value

    @property
    def only_current_operated_solid_set_in_geometry(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OnlyCurrentOperatedSolidSetInGeometry() As boolean
                | 
                |     Returns or sets the "OnlyCurrentOperatedSolidSetInGeometry"
                |     parameter.
                |     Role: This parameter enables to visualize in the 3D only the current
                |     operated body's feature (operated means being aggregated in a boolean
                |     operation), as well as all other bodies and sets direcly inserted under the
                |     Part feature.
                | 
                |     Parameters:
                | 
                |         oDisplayed
                |             Current "Display in 3D only current operated solid set" parameter's
                |             value:
                | 
                |                 TRUE or 1 if such is the visualization,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.OnlyCurrentOperatedSolidSetInGeometry

    @only_current_operated_solid_set_in_geometry.setter
    def only_current_operated_solid_set_in_geometry(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.OnlyCurrentOperatedSolidSetInGeometry = value

    @property
    def only_current_solid_set_in_geometry(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OnlyCurrentSolidSetInGeometry() As boolean
                | 
                |     Returns or sets the "OnlyCurrentSolidSetInGeometry"
                |     parameter.
                |     Role: This parameter enables to visualize in the 3D only the current
                |     operated body's feature (operated means being aggregated in a boolean
                |     operation), as well as all other bodies and sets direcly inserted under the
                |     Part feature.
                | 
                |     Parameters:
                | 
                |         oDisplayed
                |             Current "Display in 3D only current operated solid set" parameter's
                |             value:
                | 
                |                 TRUE or 1 if such is the visualization,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.OnlyCurrentSolidSetInGeometry

    @only_current_solid_set_in_geometry.setter
    def only_current_solid_set_in_geometry(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.OnlyCurrentSolidSetInGeometry = value

    @property
    def parameters_node_in_tree(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ParametersNodeInTree() As boolean
                | 
                |     Returns or sets the "ParametersNodeInTree" parameter.
                |     Role: This parameter determines if a node called "Parameters" is created to
                |     contain all Knowledgeware parameters.
                |     Its value can be changed even after parameters have been created. The
                |     result is that the specification tree node display status will be
                |     affected.
                | 
                |     Parameters:
                | 
                |         oNodeDisplayed
                |             Current "ParametersNodeInTree" parameter's value:
                | 
                |                 TRUE or 1 if such a node is displayed,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ParametersNodeInTree

    @parameters_node_in_tree.setter
    def parameters_node_in_tree(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ParametersNodeInTree = value

    @property
    def publish_topological_elements(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PublishTopologicalElements() As boolean
                | 
                |     Returns or sets the "PublishTopologicalElements"
                |     parameter.
                |     Role: This parameter defines if topological elements (faces, edges,
                |     vertices, axes extremities) can be published.
                | 
                |     Parameters:
                | 
                |         oTopologyAllowed
                |             Current "PublishTopologicalElements" parameter's
                |             value:
                | 
                |                 TRUE or 1 if topological elements can be used for
                |                 publication,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.PublishTopologicalElements

    @publish_topological_elements.setter
    def publish_topological_elements(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.PublishTopologicalElements = value

    @property
    def relations_node_in_tree(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RelationsNodeInTree() As boolean
                | 
                |     Returns or sets the "RelationsNodeInTree" parameter.
                |     Role: This parameter determines if a node called "Relations" is created to
                |     contain all Knowledgeware relations (for instance
                |     formulas).
                |     Its value can be changed even after parameters have been created. The
                |     result is that the specification tree node display status will be
                |     affected.
                | 
                |     Parameters:
                | 
                |         oNodeDisplayed
                |             Current "RelationsNodeInTree" parameter's value:
                | 
                |                 TRUE or 1 if such a node is displayed,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.RelationsNodeInTree

    @relations_node_in_tree.setter
    def relations_node_in_tree(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.RelationsNodeInTree = value

    @property
    def replace_only_after_current(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ReplaceOnlyAfterCurrent() As boolean
                | 
                |     Returns or sets the "ReplaceOnlyAfterCurrent" parameter.
                |     Role: This parameter defines if the replace operation can only apply to
                |     components located after the current object.
                | 
                |     Parameters:
                | 
                |         oOnlyAfterCurrent
                |             Current "ReplaceOnlyAfterCurrent" parameter's
                |             value:
                | 
                |                 TRUE or 1 if the replace operation can only apply to components
                |                 located after the current object,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.ReplaceOnlyAfterCurrent

    @replace_only_after_current.setter
    def replace_only_after_current(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.ReplaceOnlyAfterCurrent = value

    @property
    def surface_elements_location(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SurfaceElementsLocation() As
                | CatPartSurfaceElementsLocation
                | 
                |     Returns or sets the "SurfaceElementsLocation" parameter.
                |     Role: This parameter determines where wireframe and surface elements are
                |     created when hybrid design is active.
                |     This option can be changed when hybrid design mode is not active (but
                |     useless then), and also even after a document has been
                |     opened.
                | 
                |     Parameters:
                | 
                |         oLocation
                |             Current "SurfaceElementsLocation" parameter's
                |             value:
                | 
                |                 catPartBodyLocation when elements are created within a
                |                 PartBody,
                |                 catXGSLocation when elements are created within a G.S. or an
                |                 O.G.S..
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :return: enum cat_part_surface_elements_location
        :rtype: int
        """

        return self.part_infrastructure_setting_att.SurfaceElementsLocation

    @surface_elements_location.setter
    def surface_elements_location(self, value: int):
        """
        :param int value: enum cat_part_surface_elements_location
        """

        self.part_infrastructure_setting_att.SurfaceElementsLocation = value

    @property
    def true_color_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TrueColorMode() As boolean
                | 
                |     Returns or sets the "ColorInheritanceMode" parameter.
                |     Role: This parameter determines color inheritance mode for absorbing
                |     features in a part.
                |     Color inheritance mode defines which mode of propagation will be used to
                |     set color on an absorbing feature. If it is valuated to 1, absorbing feature
                |     will inherit colors from all their input. If it is defined to 0, absorbing
                |     features will inherit colors from their main input only (default mode). This
                |     option can be changed even after a document has been
                |     opened.
                | 
                |     Parameters:
                | 
                |         oActivated
                |             Current "ColorInheritanceMode" parameter's value:
                | 
                |                 TRUE or 1 if absorbing features inherit from all their
                |                 inputs,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.TrueColorMode

    @true_color_mode.setter
    def true_color_mode(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.TrueColorMode = value

    @property
    def update_elements_refreshed(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property UpdateElementsRefreshed() As boolean
                | 
                |     Returns or sets the "UpdateElementsRefreshed" parameter.
                |     Role: This parameter determines if elements visualization has to be
                |     refreshed individually during update tasks.
                | 
                |     Parameters:
                | 
                |         oElementsRefreshed
                |             Current "UpdateElementsRefreshed" parameter's
                |             value:
                | 
                |                 TRUE or 1 if elements visualization is
                |                 refreshed,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.UpdateElementsRefreshed

    @update_elements_refreshed.setter
    def update_elements_refreshed(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.UpdateElementsRefreshed = value

    @property
    def update_linked_external_references(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property UpdateLinkedExternalReferences() As boolean
                | 
                |     Returns or sets the "UpdateLinkedExternalReferences"
                |     parameter.
                |     Role: This parameter determines if update tasks also apply to linked
                |     external references.
                | 
                |     Parameters:
                | 
                |         oExternalReferencesUpdated
                |             Current "UpdateLinkedExternalReferences" parameter's
                |             value:
                | 
                |                 TRUE or 1 if the update tasks apply to linked external
                |                 references,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.UpdateLinkedExternalReferences

    @update_linked_external_references.setter
    def update_linked_external_references(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.UpdateLinkedExternalReferences = value

    @property
    def update_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property UpdateMode() As CatPartUpdateMode
                | 
                |     Returns or sets the "UpdateMode" parameter.
                |     Role: This parameter determines how the update of a .CATPart document is
                |     conducted.
                | 
                |     Parameters:
                | 
                |         oUpdateMode
                |             Current update mode:
                | 
                |                 catAutomaticUpdate when update is automatically
                |                 launched,
                |                 catManualUpdate when update has to be launched
                |                 manually.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :return: enum cat_part_update_mode
        :rtype: int
        """

        return self.part_infrastructure_setting_att.UpdateMode

    @update_mode.setter
    def update_mode(self, value: int):
        """
        :param int value: enum cat_part_update_mode
        """

        self.part_infrastructure_setting_att.UpdateMode = value

    @property
    def update_stopped_on_error(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property UpdateStoppedOnError() As boolean
                | 
                |     Returns or sets the "UpdateStoppedOnError" parameter.
                |     Role: This parameter determines if update tasks stop on the first detected
                |     error.
                | 
                |     Parameters:
                | 
                |         oStoppedOnError
                |             Current "UpdateStoppedOnError" parameter's value:
                | 
                |                 TRUE or 1 if update tasks stop,
                |                 FALSE or 0 otherwise.
                | 
                |     Returns:
                |         S_OK if the parameter is correctly retrieved, E_FAIL otherwise.

        :rtype: bool
        """

        return self.part_infrastructure_setting_att.UpdateStoppedOnError

    @update_stopped_on_error.setter
    def update_stopped_on_error(self, value: bool):
        """
        :param bool value:
        """

        self.part_infrastructure_setting_att.UpdateStoppedOnError = value

    def get_also_delete_exclusive_parents_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAlsoDeleteExclusiveParentsInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "AlsoDeleteExclusiveParents"
                |     parameter.
                |     Role:Retrieves the state of the "AlsoDeleteExclusiveParents" parameter in
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
        return self.part_infrastructure_setting_att.GetAlsoDeleteExclusiveParentsInfo(io_admin_level, io_locked)

    def get_axis_system_size_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAxisSystemSizeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "AxisSystemSize"
                |     parameter.
                |     Role:Retrieves the state of the "AxisSystemSize" parameter in the current
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
        return self.part_infrastructure_setting_att.GetAxisSystemSizeInfo(io_admin_level, io_locked)

    def get_bodies_under_operations_in_tree_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBodiesUnderOperationsInTreeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "BodiesUnderOperationsInTree"
                |     parameter.
                |     Role:Retrieves the state of the "BodiesUnderOperationsInTree" parameter in
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
        return self.part_infrastructure_setting_att.GetBodiesUnderOperationsInTreeInfo(io_admin_level, io_locked)

    def get_color_synchronization_editability_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetColorSynchronizationEditabilityInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     "ColorSynchronizationEditability" parameter.
                |     Role:Retrieves the state of the "ColorSynchronizationEditability" parameter
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
        return self.part_infrastructure_setting_att.GetColorSynchronizationEditabilityInfo(io_admin_level, io_locked)

    def get_color_synchronization_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetColorSynchronizationModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "ColorSynchronizationMode"
                |     parameter.
                |     Role:Retrieves the state of the "ColorSynchronizationMode" parameter in the
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
        return self.part_infrastructure_setting_att.GetColorSynchronizationModeInfo(io_admin_level, io_locked)

    def get_color_synchronization_mode_manage_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetColorSynchronizationModeManageInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "ColorSynchronizationModeManage"
                |     parameter.
                |     Role:Retrieves the state of the "ColorSynchronizationModeManage" parameter
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
        return self.part_infrastructure_setting_att.GetColorSynchronizationModeManageInfo(io_admin_level, io_locked)

    def get_color_synchronization_mode_on_feature_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetColorSynchronizationModeOnFeatureInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     "ColorSynchronizationModeOnFeature" parameter.
                |     Role:Retrieves the state of the "ColorSynchronizationModeOnFeature"
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
        return self.part_infrastructure_setting_att.GetColorSynchronizationModeOnFeatureInfo(io_admin_level, io_locked)

    def get_color_synchronization_mode_on_sub_elements_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetColorSynchronizationModeOnSubElementsInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     "ColorSynchronizationModeOnSubElements" parameter.
                |     Role:Retrieves the state of the "ColorSynchronizationModeOnSubElements"
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
        return self.part_infrastructure_setting_att.GetColorSynchronizationModeOnSubElementsInfo(io_admin_level,
                                                                                                 io_locked)

    def get_colors3_d_experience_management_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetColors3DExperienceManagementInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "Colors3DExperienceManagement"
                |     parameter.
                |     Role:Retrieves the state of the "Colors3DExperienceManagement" parameter in
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
        return self.part_infrastructure_setting_att.GetColors3DExperienceManagementInfo(io_admin_level, io_locked)

    def get_constraints_in_geometry_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetConstraintsInGeometryInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "ConstraintsInGeometry"
                |     parameter.
                |     Role:Retrieves the state of the "ConstraintsInGeometry" parameter in the
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
        return self.part_infrastructure_setting_att.GetConstraintsInGeometryInfo(io_admin_level, io_locked)

    def get_constraints_node_in_tree_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetConstraintsNodeInTreeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "ConstraintsNodeInTree"
                |     parameter.
                |     Role:Retrieves the state of the "ConstraintsNodeInTree" parameter in the
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
        return self.part_infrastructure_setting_att.GetConstraintsNodeInTreeInfo(io_admin_level, io_locked)

    def get_contextual_features_selectable_at_creation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetContextualFeaturesSelectableAtCreationInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     "ContextualFeaturesSelectableAtCreation" parameter.
                |     Role:Retrieves the state of the "ContextualFeaturesSelectableAtCreation"
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
        return self.part_infrastructure_setting_att.GetContextualFeaturesSelectableAtCreationInfo(io_admin_level,
                                                                                                  io_locked)

    def get_default_colors_editability_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDefaultColorsEditabilityInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "DefaultColorsEditability"
                |     parameter.
                |     Role:Retrieves the state of the "DefaultColorsEditability" parameter in the
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
        return self.part_infrastructure_setting_att.GetDefaultColorsEditabilityInfo(io_admin_level, io_locked)

    def get_delete_warning_box_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDeleteWarningBoxInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "DeleteWarningBox"
                |     parameter.
                |     Role:Retrieves the state of the "DeleteWarningBox" parameter in the current
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
        return self.part_infrastructure_setting_att.GetDeleteWarningBoxInfo(io_admin_level, io_locked)

    def get_display_geometry_after_current_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDisplayGeometryAfterCurrentInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "DisplayGeometryAfterCurrent"
                |     parameter.
                |     Role:Retrieves the state of the "DisplayGeometryAfterCurrent" parameter in
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
        return self.part_infrastructure_setting_att.GetDisplayGeometryAfterCurrentInfo(io_admin_level, io_locked)

    def get_expand_sketch_based_features_node_at_creation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExpandSketchBasedFeaturesNodeAtCreationInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     "ExpandSketchBasedFeaturesNodeAtCreation" parameter.
                |     Role:Retrieves the state of the "ExpandSketchBasedFeaturesNodeAtCreation"
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
        return self.part_infrastructure_setting_att.GetExpandSketchBasedFeaturesNodeAtCreationInfo(io_admin_level,
                                                                                                   io_locked)

    def get_external_references_as_visible_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExternalReferencesAsVisibleInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "ExternalReferencesAsVisible"
                |     parameter.
                |     Role:Retrieves the state of the "ExternalReferencesAsVisible" parameter in
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
        return self.part_infrastructure_setting_att.GetExternalReferencesAsVisibleInfo(io_admin_level, io_locked)

    def get_external_references_assembly_root_context_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExternalReferencesAssemblyRootContextInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     "ExternalReferencesAssemblyRootContext" parameter.
                |     Role:Retrieves the state of the "ExternalReferencesAssemblyRootContext"
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
        return self.part_infrastructure_setting_att.GetExternalReferencesAssemblyRootContextInfo(io_admin_level,
                                                                                                 io_locked)

    def get_external_references_node_in_tree_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetExternalReferencesNodeInTreeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "ExternalReferencesNodeInTree"
                |     parameter.
                |     Role:Retrieves the state of the "ExternalReferencesNodeInTree" parameter in
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
        return self.part_infrastructure_setting_att.GetExternalReferencesNodeInTreeInfo(io_admin_level, io_locked)

    def get_hybrid_design_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetHybridDesignModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "HybridDesignMode"
                |     parameter.
                |     Role:Retrieves the state of the "HybridDesignMode" parameter in the current
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
        return self.part_infrastructure_setting_att.GetHybridDesignModeInfo(io_admin_level, io_locked)

    def get_knowledge_in_hybrid_design_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetKnowledgeInHybridDesignModeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "KnowledgeInHybridDesignMode"
                |     parameter.
                |     Role:Retrieves the state of the "KnowledgeInHybridDesignMode" parameter in
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
        return self.part_infrastructure_setting_att.GetKnowledgeInHybridDesignModeInfo(io_admin_level, io_locked)

    def get_linked_external_references_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLinkedExternalReferencesInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "LinkedExternalReferences"
                |     parameter.
                |     Role:Retrieves the state of the "LinkedExternalReferences" parameter in the
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
        return self.part_infrastructure_setting_att.GetLinkedExternalReferencesInfo(io_admin_level, io_locked)

    def get_linked_external_references_only_on_publication_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLinkedExternalReferencesOnlyOnPublicationInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     "LinkedExternalReferencesOnlyOnPublication" parameter.
                |     Role:Retrieves the state of the "LinkedExternalReferencesOnlyOnPublication"
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
        return self.part_infrastructure_setting_att.GetLinkedExternalReferencesOnlyOnPublicationInfo(io_admin_level,
                                                                                                     io_locked)

    def get_linked_external_references_warning_at_creation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLinkedExternalReferencesWarningAtCreationInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     "LinkedExternalReferencesWarningAtCreation" parameter.
                |     Role:Retrieves the state of the "LinkedExternalReferencesWarningAtCreation"
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
        return self.part_infrastructure_setting_att.GetLinkedExternalReferencesWarningAtCreationInfo(io_admin_level,
                                                                                                     io_locked)

    def get_naming_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNamingModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "NamingMode"
                |     parameter.
                |     Role:Retrieves the state of the "NamingMode" parameter in the current
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
        return self.part_infrastructure_setting_att.GetNamingModeInfo(io_admin_level, io_locked)

    def get_new_with3_d_support_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNewWith3DSupportInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "NewWith3DSupport"
                |     parameter.
                |     Role:Retrieves the state of the "NewWith3DSupport" parameter in the current
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
        return self.part_infrastructure_setting_att.GetNewWith3DSupportInfo(io_admin_level, io_locked)

    def get_new_with_axis_system_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNewWithAxisSystemInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "NewWithAxisSystem"
                |     parameter.
                |     Role:Retrieves the state of the "NewWithAxisSystem" parameter in the
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
        return self.part_infrastructure_setting_att.GetNewWithAxisSystemInfo(io_admin_level, io_locked)

    def get_new_with_gs_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNewWithGSInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "NewWithGS"
                |     parameter.
                |     Role:Retrieves the state of the "NewWithGS" parameter in the current
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
        return self.part_infrastructure_setting_att.GetNewWithGSInfo(io_admin_level, io_locked)

    def get_new_with_ogs_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNewWithOGSInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "NewWithOGS"
                |     parameter.
                |     Role:Retrieves the state of the "NewWithOGS" parameter in the current
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
        return self.part_infrastructure_setting_att.GetNewWithOGSInfo(io_admin_level, io_locked)

    def get_new_with_panel_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNewWithPanelInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "NewWithPanel"
                |     parameter.
                |     Role:Retrieves the state of the "NewWithPanel" parameter in the current
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
        return self.part_infrastructure_setting_att.GetNewWithPanelInfo(io_admin_level, io_locked)

    def get_only_current_operated_solid_set_in_geometry_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetOnlyCurrentOperatedSolidSetInGeometryInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the
                |     "OnlyCurrentOperatedSolidSetInGeometry" parameter.
                |     Role:Retrieves the state of the "OnlyCurrentOperatedSolidSetInGeometry"
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
        return self.part_infrastructure_setting_att.GetOnlyCurrentOperatedSolidSetInGeometryInfo(io_admin_level,
                                                                                                 io_locked)

    def get_only_current_solid_set_in_geometry_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetOnlyCurrentSolidSetInGeometryInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "OnlyCurrentSolidSetInGeometry"
                |     parameter.
                |     Role:Retrieves the state of the "OnlyCurrentSolidSetInGeometry" parameter
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
        return self.part_infrastructure_setting_att.GetOnlyCurrentSolidSetInGeometryInfo(io_admin_level, io_locked)

    def get_parameters_node_in_tree_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetParametersNodeInTreeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "ParametersNodeInTree"
                |     parameter.
                |     Role:Retrieves the state of the "ParametersNodeInTree" parameter in the
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
        return self.part_infrastructure_setting_att.GetParametersNodeInTreeInfo(io_admin_level, io_locked)

    def get_publish_topological_elements_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPublishTopologicalElementsInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "PublishTopologicalElements"
                |     parameter.
                |     Role:Retrieves the state of the "PublishTopologicalElements" parameter in
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
        return self.part_infrastructure_setting_att.GetPublishTopologicalElementsInfo(io_admin_level, io_locked)

    def get_relations_node_in_tree_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetRelationsNodeInTreeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "RelationsNodeInTree"
                |     parameter.
                |     Role:Retrieves the state of the "RelationsNodeInTree" parameter in the
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
        return self.part_infrastructure_setting_att.GetRelationsNodeInTreeInfo(io_admin_level, io_locked)

    def get_replace_only_after_current_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetReplaceOnlyAfterCurrentInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "ReplaceOnlyAfterCurrent"
                |     parameter.
                |     Role:Retrieves the state of the "ReplaceOnlyAfterCurrent" parameter in the
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
        return self.part_infrastructure_setting_att.GetReplaceOnlyAfterCurrentInfo(io_admin_level, io_locked)

    def get_surface_elements_location_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetSurfaceElementsLocationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "SurfaceElementsLocation"
                |     parameter.
                |     Role:Retrieves the state of the "SurfaceElementsLocation" parameter in the
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
        return self.part_infrastructure_setting_att.GetSurfaceElementsLocationInfo(io_admin_level, io_locked)

    def get_true_color_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTrueColorModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "ColorInheritanceMode"
                |     parameter.
                |     Role:Retrieves the state of the "ColorInheritanceMode" parameter in the
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
        return self.part_infrastructure_setting_att.GetTrueColorModeInfo(io_admin_level, io_locked)

    def get_update_elements_refreshed_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetUpdateElementsRefreshedInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "UpdateElementsRefreshed"
                |     parameter.
                |     Role:Retrieves the state of the "UpdateElementsRefreshed" parameter in the
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
        return self.part_infrastructure_setting_att.GetUpdateElementsRefreshedInfo(io_admin_level, io_locked)

    def get_update_linked_external_references_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetUpdateLinkedExternalReferencesInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "UpdateLinkedExternalReferences"
                |     parameter.
                |     Role:Retrieves the state of the "UpdateLinkedExternalReferences" parameter
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
        return self.part_infrastructure_setting_att.GetUpdateLinkedExternalReferencesInfo(io_admin_level, io_locked)

    def get_update_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetUpdateModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "UpdateMode"
                |     parameter.
                |     Role:Retrieves the state of the "UpdateMode" parameter in the current
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
        return self.part_infrastructure_setting_att.GetUpdateModeInfo(io_admin_level, io_locked)

    def get_update_stopped_on_error_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetUpdateStoppedOnErrorInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the "UpdateStoppedOnError"
                |     parameter.
                |     Role:Retrieves the state of the "UpdateStoppedOnError" parameter in the
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
        return self.part_infrastructure_setting_att.GetUpdateStoppedOnErrorInfo(io_admin_level, io_locked)

    def set_also_delete_exclusive_parents_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAlsoDeleteExclusiveParentsLock(boolean iLocked)
                | 
                |     Locks or unlocks the "AlsoDeleteExclusiveParents"
                |     parameter.
                |     Role:Locks or unlocks the "AlsoDeleteExclusiveParents" parameter if it is
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
        return self.part_infrastructure_setting_att.SetAlsoDeleteExclusiveParentsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_also_delete_exclusive_parents_lock'
        # # vba_code = """
        # # Public Function set_also_delete_exclusive_parents_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetAlsoDeleteExclusiveParentsLock iLocked
        # #     set_also_delete_exclusive_parents_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_axis_system_size_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAxisSystemSizeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "AxisSystemSize" parameter.
                |     Role:Locks or unlocks the "AxisSystemSize" parameter if it is possible in
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
        return self.part_infrastructure_setting_att.SetAxisSystemSizeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_axis_system_size_lock'
        # # vba_code = """
        # # Public Function set_axis_system_size_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetAxisSystemSizeLock iLocked
        # #     set_axis_system_size_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_bodies_under_operations_in_tree_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBodiesUnderOperationsInTreeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "BodiesUnderOperationsInTree"
                |     parameter.
                |     Role:Locks or unlocks the "BodiesUnderOperationsInTree" parameter if it is
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
        return self.part_infrastructure_setting_att.SetBodiesUnderOperationsInTreeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_bodies_under_operations_in_tree_lock'
        # # vba_code = """
        # # Public Function set_bodies_under_operations_in_tree_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetBodiesUnderOperationsInTreeLock iLocked
        # #     set_bodies_under_operations_in_tree_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_color_synchronization_editability_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetColorSynchronizationEditabilityLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the "ColorSynchronizationEditability"
                |     parameter.
                |     Role:Locks or unlocks the "ColorSynchronizationEditability" parameter if it
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
        return self.part_infrastructure_setting_att.SetColorSynchronizationEditabilityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_color_synchronization_editability_lock'
        # # vba_code = """
        # # Public Function set_color_synchronization_editability_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetColorSynchronizationEditabilityLock iLocked
        # #     set_color_synchronization_editability_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_color_synchronization_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetColorSynchronizationModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "ColorSynchronizationMode" parameter.
                |     Role:Locks or unlocks the "ColorSynchronizationMode" parameter if it is
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
        return self.part_infrastructure_setting_att.SetColorSynchronizationModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_color_synchronization_mode_lock'
        # # vba_code = """
        # # Public Function set_color_synchronization_mode_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetColorSynchronizationModeLock iLocked
        # #     set_color_synchronization_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_color_synchronization_mode_manage_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetColorSynchronizationModeManageLock(boolean iLocked)
                | 
                |     Locks or unlocks the "ColorSynchronizationModeManage"
                |     parameter.
                |     Role:Locks or unlocks the "ColorSynchronizationModeManage" parameter if it
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
        return self.part_infrastructure_setting_att.SetColorSynchronizationModeManageLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_color_synchronization_mode_manage_lock'
        # # vba_code = """
        # # Public Function set_color_synchronization_mode_manage_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetColorSynchronizationModeManageLock iLocked
        # #     set_color_synchronization_mode_manage_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_color_synchronization_mode_on_feature_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetColorSynchronizationModeOnFeatureLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the "ColorSynchronizationModeOnFeature"
                |     parameter.
                |     Role:Locks or unlocks the "ColorSynchronizationModeOnFeature" parameter if
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
        return self.part_infrastructure_setting_att.SetColorSynchronizationModeOnFeatureLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_color_synchronization_mode_on_feature_lock'
        # # vba_code = """
        # # Public Function set_color_synchronization_mode_on_feature_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetColorSynchronizationModeOnFeatureLock iLocked
        # #     set_color_synchronization_mode_on_feature_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_color_synchronization_mode_on_sub_elements_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetColorSynchronizationModeOnSubElementsLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the "ColorSynchronizationModeOnSubElements"
                |     parameter.
                |     Role:Locks or unlocks the "ColorSynchronizationModeOnSubElements" parameter
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
        return self.part_infrastructure_setting_att.SetColorSynchronizationModeOnSubElementsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_color_synchronization_mode_on_sub_elements_lock'
        # # vba_code = """
        # # Public Function set_color_synchronization_mode_on_sub_elements_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetColorSynchronizationModeOnSubElementsLock iLocked
        # #     set_color_synchronization_mode_on_sub_elements_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_colors3_d_experience_management_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetColors3DExperienceManagementLock(boolean iLocked)
                | 
                |     Locks or unlocks the "Colors3DExperienceManagement"
                |     parameter.
                |     Role:Locks or unlocks the "Colors3DExperienceManagement" parameter if it is
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
        return self.part_infrastructure_setting_att.SetColors3DExperienceManagementLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_colors3_d_experience_management_lock'
        # # vba_code = """
        # # Public Function set_colors3_d_experience_management_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetColors3DExperienceManagementLock iLocked
        # #     set_colors3_d_experience_management_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_constraints_in_geometry_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetConstraintsInGeometryLock(boolean iLocked)
                | 
                |     Locks or unlocks the "ConstraintsInGeometry" parameter.
                |     Role:Locks or unlocks the "ConstraintsInGeometry" parameter if it is
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
        return self.part_infrastructure_setting_att.SetConstraintsInGeometryLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_constraints_in_geometry_lock'
        # # vba_code = """
        # # Public Function set_constraints_in_geometry_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetConstraintsInGeometryLock iLocked
        # #     set_constraints_in_geometry_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_constraints_node_in_tree_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetConstraintsNodeInTreeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "ConstraintsNodeInTree" parameter.
                |     Role:Locks or unlocks the "ConstraintsNodeInTree" parameter if it is
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
        return self.part_infrastructure_setting_att.SetConstraintsNodeInTreeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_constraints_node_in_tree_lock'
        # # vba_code = """
        # # Public Function set_constraints_node_in_tree_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetConstraintsNodeInTreeLock iLocked
        # #     set_constraints_node_in_tree_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_contextual_features_selectable_at_creation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetContextualFeaturesSelectableAtCreationLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the "ContextualFeaturesSelectableAtCreation"
                |     parameter.
                |     Role:Locks or unlocks the "ContextualFeaturesSelectableAtCreation"
                |     parameter if it is possible in the current administrative context. In user mode
                |     this method will always return E_FAIL.
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
        return self.part_infrastructure_setting_att.SetContextualFeaturesSelectableAtCreationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_contextual_features_selectable_at_creation_lock'
        # # vba_code = """
        # # Public Function set_contextual_features_selectable_at_creation_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetContextualFeaturesSelectableAtCreationLock iLocked
        # #     set_contextual_features_selectable_at_creation_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_colors_editability_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDefaultColorsEditabilityLock(boolean iLocked)
                | 
                |     Locks or unlocks the "DefaultColorsEditability" parameter.
                |     Role:Locks or unlocks the "DefaultColorsEditability" parameter if it is
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
        return self.part_infrastructure_setting_att.SetDefaultColorsEditabilityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_colors_editability_lock'
        # # vba_code = """
        # # Public Function set_default_colors_editability_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetDefaultColorsEditabilityLock iLocked
        # #     set_default_colors_editability_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_delete_warning_box_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDeleteWarningBoxLock(boolean iLocked)
                | 
                |     Locks or unlocks the "DeleteWarningBox" parameter.
                |     Role:Locks or unlocks the "DeleteWarningBox" parameter if it is possible in
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
        return self.part_infrastructure_setting_att.SetDeleteWarningBoxLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_delete_warning_box_lock'
        # # vba_code = """
        # # Public Function set_delete_warning_box_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetDeleteWarningBoxLock iLocked
        # #     set_delete_warning_box_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_geometry_after_current_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDisplayGeometryAfterCurrentLock(boolean iLocked)
                | 
                |     Locks or unlocks the "DisplayGeometryAfterCurrent"
                |     parameter.
                |     Role:Locks or unlocks the "DisplayGeometryAfterCurrent" parameter if it is
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
        return self.part_infrastructure_setting_att.SetDisplayGeometryAfterCurrentLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_geometry_after_current_lock'
        # # vba_code = """
        # # Public Function set_display_geometry_after_current_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetDisplayGeometryAfterCurrentLock iLocked
        # #     set_display_geometry_after_current_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_expand_sketch_based_features_node_at_creation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExpandSketchBasedFeaturesNodeAtCreationLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the "ExpandSketchBasedFeaturesNodeAtCreation"
                |     parameter.
                |     Role:Locks or unlocks the "ExpandSketchBasedFeaturesNodeAtCreation"
                |     parameter if it is possible in the current administrative context. In user mode
                |     this method will always return E_FAIL.
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
        return self.part_infrastructure_setting_att.SetExpandSketchBasedFeaturesNodeAtCreationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_expand_sketch_based_features_node_at_creation_lock'
        # # vba_code = """
        # # Public Function set_expand_sketch_based_features_node_at_creation_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetExpandSketchBasedFeaturesNodeAtCreationLock iLocked
        # #     set_expand_sketch_based_features_node_at_creation_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_external_references_as_visible_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExternalReferencesAsVisibleLock(boolean iLocked)
                | 
                |     Locks or unlocks the "ExternalReferencesAsVisible"
                |     parameter.
                |     Role:Locks or unlocks the "ExternalReferencesAsVisible" parameter if it is
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
        return self.part_infrastructure_setting_att.SetExternalReferencesAsVisibleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_external_references_as_visible_lock'
        # # vba_code = """
        # # Public Function set_external_references_as_visible_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetExternalReferencesAsVisibleLock iLocked
        # #     set_external_references_as_visible_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_external_references_assembly_root_context_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExternalReferencesAssemblyRootContextLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the "ExternalReferencesAssemblyRootContext"
                |     parameter.
                |     Role:Locks or unlocks the "ExternalReferencesAssemblyRootContext" parameter
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
        return self.part_infrastructure_setting_att.SetExternalReferencesAssemblyRootContextLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_external_references_assembly_root_context_lock'
        # # vba_code = """
        # # Public Function set_external_references_assembly_root_context_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetExternalReferencesAssemblyRootContextLock iLocked
        # #     set_external_references_assembly_root_context_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_external_references_node_in_tree_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetExternalReferencesNodeInTreeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "ExternalReferencesNodeInTree"
                |     parameter.
                |     Role:Locks or unlocks the "ExternalReferencesNodeInTree" parameter if it is
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
        return self.part_infrastructure_setting_att.SetExternalReferencesNodeInTreeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_external_references_node_in_tree_lock'
        # # vba_code = """
        # # Public Function set_external_references_node_in_tree_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetExternalReferencesNodeInTreeLock iLocked
        # #     set_external_references_node_in_tree_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_hybrid_design_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetHybridDesignModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "HybridDesignMode" parameter.
                |     Role:Locks or unlocks the "HybridDesignMode" parameter if it is possible in
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
        return self.part_infrastructure_setting_att.SetHybridDesignModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_hybrid_design_mode_lock'
        # # vba_code = """
        # # Public Function set_hybrid_design_mode_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetHybridDesignModeLock iLocked
        # #     set_hybrid_design_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_knowledge_in_hybrid_design_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetKnowledgeInHybridDesignModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "KnowledgeInHybridDesignMode"
                |     parameter.
                |     Role:Locks or unlocks the "KnowledgeInHybridDesignMode" parameter if it is
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
        return self.part_infrastructure_setting_att.SetKnowledgeInHybridDesignModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_knowledge_in_hybrid_design_mode_lock'
        # # vba_code = """
        # # Public Function set_knowledge_in_hybrid_design_mode_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetKnowledgeInHybridDesignModeLock iLocked
        # #     set_knowledge_in_hybrid_design_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_linked_external_references_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLinkedExternalReferencesLock(boolean iLocked)
                | 
                |     Locks or unlocks the "LinkedExternalReferences" parameter.
                |     Role:Locks or unlocks the "LinkedExternalReferences" parameter if it is
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
        return self.part_infrastructure_setting_att.SetLinkedExternalReferencesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_linked_external_references_lock'
        # # vba_code = """
        # # Public Function set_linked_external_references_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetLinkedExternalReferencesLock iLocked
        # #     set_linked_external_references_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_linked_external_references_only_on_publication_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLinkedExternalReferencesOnlyOnPublicationLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the "LinkedExternalReferencesOnlyOnPublication"
                |     parameter.
                |     Role:Locks or unlocks the "LinkedExternalReferencesOnlyOnPublication"
                |     parameter if it is possible in the current administrative context. In user mode
                |     this method will always return E_FAIL.
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
        return self.part_infrastructure_setting_att.SetLinkedExternalReferencesOnlyOnPublicationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_linked_external_references_only_on_publication_lock'
        # # vba_code = """
        # # Public Function set_linked_external_references_only_on_publication_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetLinkedExternalReferencesOnlyOnPublicationLock iLocked
        # #     set_linked_external_references_only_on_publication_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_linked_external_references_warning_at_creation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLinkedExternalReferencesWarningAtCreationLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the "LinkedExternalReferencesWarningAtCreation"
                |     parameter.
                |     Role:Locks or unlocks the "LinkedExternalReferencesWarningAtCreation"
                |     parameter if it is possible in the current administrative context. In user mode
                |     this method will always return E_FAIL.
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
        return self.part_infrastructure_setting_att.SetLinkedExternalReferencesWarningAtCreationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_linked_external_references_warning_at_creation_lock'
        # # vba_code = """
        # # Public Function set_linked_external_references_warning_at_creation_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetLinkedExternalReferencesWarningAtCreationLock iLocked
        # #     set_linked_external_references_warning_at_creation_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_naming_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNamingModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "NamingMode" parameter.
                |     Role:Locks or unlocks the "NamingMode" parameter if it is possible in the
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
        return self.part_infrastructure_setting_att.SetNamingModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_naming_mode_lock'
        # # vba_code = """
        # # Public Function set_naming_mode_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetNamingModeLock iLocked
        # #     set_naming_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_new_with3_d_support_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNewWith3DSupportLock(boolean iLocked)
                | 
                |     Locks or unlocks the "NewWith3DSupport" parameter.
                |     Role:Locks or unlocks the "NewWith3DSupport" parameter if it is possible in
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
        return self.part_infrastructure_setting_att.SetNewWith3DSupportLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_new_with3_d_support_lock'
        # # vba_code = """
        # # Public Function set_new_with3_d_support_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetNewWith3DSupportLock iLocked
        # #     set_new_with3_d_support_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_new_with_axis_system_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNewWithAxisSystemLock(boolean iLocked)
                | 
                |     Locks or unlocks the "NewWithAxisSystem" parameter.
                |     Role:Locks or unlocks the "NewWithAxisSystem" parameter if it is possible
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
        return self.part_infrastructure_setting_att.SetNewWithAxisSystemLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_new_with_axis_system_lock'
        # # vba_code = """
        # # Public Function set_new_with_axis_system_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetNewWithAxisSystemLock iLocked
        # #     set_new_with_axis_system_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_new_with_gs_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNewWithGSLock(boolean iLocked)
                | 
                |     Locks or unlocks the "NewWithGS" parameter.
                |     Role:Locks or unlocks the "NewWithGS" parameter if it is possible in the
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
        return self.part_infrastructure_setting_att.SetNewWithGSLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_new_with_gs_lock'
        # # vba_code = """
        # # Public Function set_new_with_gs_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetNewWithGSLock iLocked
        # #     set_new_with_gs_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_new_with_ogs_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNewWithOGSLock(boolean iLocked)
                | 
                |     Locks or unlocks the "NewWithOGS" parameter.
                |     Role:Locks or unlocks the "NewWithOGS" parameter if it is possible in the
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
        return self.part_infrastructure_setting_att.SetNewWithOGSLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_new_with_ogs_lock'
        # # vba_code = """
        # # Public Function set_new_with_ogs_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetNewWithOGSLock iLocked
        # #     set_new_with_ogs_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_new_with_panel_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNewWithPanelLock(boolean iLocked)
                | 
                |     Locks or unlocks the "NewWithPanel" parameter.
                |     Role:Locks or unlocks the "NewWithPanel" parameter if it is possible in the
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
        return self.part_infrastructure_setting_att.SetNewWithPanelLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_new_with_panel_lock'
        # # vba_code = """
        # # Public Function set_new_with_panel_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetNewWithPanelLock iLocked
        # #     set_new_with_panel_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_only_current_operated_solid_set_in_geometry_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetOnlyCurrentOperatedSolidSetInGeometryLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the "OnlyCurrentOperatedSolidSetInGeometry"
                |     parameter.
                |     Role:Locks or unlocks the "OnlyCurrentOperatedSolidSetInGeometry" parameter
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
        return self.part_infrastructure_setting_att.SetOnlyCurrentOperatedSolidSetInGeometryLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_only_current_operated_solid_set_in_geometry_lock'
        # # vba_code = """
        # # Public Function set_only_current_operated_solid_set_in_geometry_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetOnlyCurrentOperatedSolidSetInGeometryLock iLocked
        # #     set_only_current_operated_solid_set_in_geometry_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_only_current_solid_set_in_geometry_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetOnlyCurrentSolidSetInGeometryLock(boolean iLocked)
                | 
                |     Locks or unlocks the "OnlyCurrentSolidSetInGeometry"
                |     parameter.
                |     Role:Locks or unlocks the "OnlyCurrentSolidSetInGeometry" parameter if it
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
        return self.part_infrastructure_setting_att.SetOnlyCurrentSolidSetInGeometryLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_only_current_solid_set_in_geometry_lock'
        # # vba_code = """
        # # Public Function set_only_current_solid_set_in_geometry_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetOnlyCurrentSolidSetInGeometryLock iLocked
        # #     set_only_current_solid_set_in_geometry_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_parameters_node_in_tree_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetParametersNodeInTreeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "ParametersNodeInTree" parameter.
                |     Role:Locks or unlocks the "ParametersNodeInTree" parameter if it is
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
        return self.part_infrastructure_setting_att.SetParametersNodeInTreeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_parameters_node_in_tree_lock'
        # # vba_code = """
        # # Public Function set_parameters_node_in_tree_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetParametersNodeInTreeLock iLocked
        # #     set_parameters_node_in_tree_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_publish_topological_elements_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPublishTopologicalElementsLock(boolean iLocked)
                | 
                |     Locks or unlocks the "PublishTopologicalElements"
                |     parameter.
                |     Role:Locks or unlocks the "PublishTopologicalElements" parameter if it is
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
        return self.part_infrastructure_setting_att.SetPublishTopologicalElementsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_publish_topological_elements_lock'
        # # vba_code = """
        # # Public Function set_publish_topological_elements_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetPublishTopologicalElementsLock iLocked
        # #     set_publish_topological_elements_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_relations_node_in_tree_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRelationsNodeInTreeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "RelationsNodeInTree" parameter.
                |     Role:Locks or unlocks the "RelationsNodeInTree" parameter if it is possible
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
        return self.part_infrastructure_setting_att.SetRelationsNodeInTreeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_relations_node_in_tree_lock'
        # # vba_code = """
        # # Public Function set_relations_node_in_tree_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetRelationsNodeInTreeLock iLocked
        # #     set_relations_node_in_tree_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_replace_only_after_current_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetReplaceOnlyAfterCurrentLock(boolean iLocked)
                | 
                |     Locks or unlocks the "ReplaceOnlyAfterCurrent" parameter.
                |     Role:Locks or unlocks the "ReplaceOnlyAfterCurrent" parameter if it is
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
        return self.part_infrastructure_setting_att.SetReplaceOnlyAfterCurrentLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_replace_only_after_current_lock'
        # # vba_code = """
        # # Public Function set_replace_only_after_current_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetReplaceOnlyAfterCurrentLock iLocked
        # #     set_replace_only_after_current_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_surface_elements_location_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSurfaceElementsLocationLock(boolean iLocked)
                | 
                |     Locks or unlocks the "SurfaceElementsLocation" parameter.
                |     Role:Locks or unlocks the "SurfaceElementsLocation" parameter if it is
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
        return self.part_infrastructure_setting_att.SetSurfaceElementsLocationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_surface_elements_location_lock'
        # # vba_code = """
        # # Public Function set_surface_elements_location_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetSurfaceElementsLocationLock iLocked
        # #     set_surface_elements_location_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_update_elements_refreshed_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetUpdateElementsRefreshedLock(boolean iLocked)
                | 
                |     Locks or unlocks the "UpdateElementsRefreshed" parameter.
                |     Role:Locks or unlocks the "UpdateElementsRefreshed" parameter if it is
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
        return self.part_infrastructure_setting_att.SetUpdateElementsRefreshedLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_update_elements_refreshed_lock'
        # # vba_code = """
        # # Public Function set_update_elements_refreshed_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetUpdateElementsRefreshedLock iLocked
        # #     set_update_elements_refreshed_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_update_linked_external_references_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetUpdateLinkedExternalReferencesLock(boolean iLocked)
                | 
                |     Locks or unlocks the "UpdateLinkedExternalReferences"
                |     parameter.
                |     Role:Locks or unlocks the "UpdateLinkedExternalReferences" parameter if it
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
        return self.part_infrastructure_setting_att.SetUpdateLinkedExternalReferencesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_update_linked_external_references_lock'
        # # vba_code = """
        # # Public Function set_update_linked_external_references_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetUpdateLinkedExternalReferencesLock iLocked
        # #     set_update_linked_external_references_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_update_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetUpdateModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the "UpdateMode" parameter.
                |     Role:Locks or unlocks the "UpdateMode" parameter if it is possible in the
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
        return self.part_infrastructure_setting_att.SetUpdateModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_update_mode_lock'
        # # vba_code = """
        # # Public Function set_update_mode_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetUpdateModeLock iLocked
        # #     set_update_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_update_stopped_on_error_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetUpdateStoppedOnErrorLock(boolean iLocked)
                | 
                |     Locks or unlocks the "UpdateStoppedOnError" parameter.
                |     Role:Locks or unlocks the "UpdateStoppedOnError" parameter if it is
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
        return self.part_infrastructure_setting_att.SetUpdateStoppedOnErrorLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_update_stopped_on_error_lock'
        # # vba_code = """
        # # Public Function set_update_stopped_on_error_lock(part_infrastructure_setting_att)
        # #     Dim iLocked (2)
        # #     part_infrastructure_setting_att.SetUpdateStoppedOnErrorLock iLocked
        # #     set_update_stopped_on_error_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PartInfrastructureSettingAtt(name="{self.name}")'
