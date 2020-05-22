#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-18 10:56:40.651039

from pycatia.system_interfaces.settingcontroller import SettingController


class PartInfrastructureSettingAtt(SettingController):
    """
        .. note::
            CAA V5 Visual Basic help

                | Setting controller for all the Part Infrastructure property tab
                | pages.Role: This interface is implemented by a component representing
                | the controller for the Part Infrastructure settings.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.part_infrastructure_setting_att = com_object

    @property
    def also_delete_exclusive_parents(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AlsoDeleteExclusiveParents
                | o Property AlsoDeleteExclusiveParents(    ) As
                | 
                | Returns or sets the "AlsoDeleteExclusiveParents" parameter.
                | Role: This parameter defines if a exclusive parents of an
                | object will also be deleted when the object is deleted. This
                | option is effective only when the "Deletion warning box" is
                | displayed.

        :return: bool
        """
        return self.part_infrastructure_setting_att.AlsoDeleteExclusiveParents

    @also_delete_exclusive_parents.setter
    def also_delete_exclusive_parents(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.AlsoDeleteExclusiveParents = value

    @property
    def axis_system_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AxisSystemSize
                | o Property AxisSystemSize(    ) As
                | 
                | Returns or sets the "AxisSystemSize" parameter. Role: This
                | parameter determines the size of axis systems.

        :return: float
        """
        return self.part_infrastructure_setting_att.AxisSystemSize

    @axis_system_size.setter
    def axis_system_size(self, value):
        """
            :param float value:
        """
        self.part_infrastructure_setting_att.AxisSystemSize = value

    @property
    def bodies_under_operations_in_tree(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | BodiesUnderOperationsInTree
                | o Property BodiesUnderOperationsInTree(    ) As
                | 
                | Returns or sets the "BodiesUnderOperationsInTree" parameter.
                | Role: This parameter determines if a Body node is displayed
                | when it is being aggregated under a boolean operation (Add,
                | Assemble, Remove, Intersect, Union Trim). Its value can be
                | changed even after a boolean operation has been created.
                | Simply collapse and expand the federating boolean operation
                | node for the specification tree to be refreshed.

        :return: bool
        """
        return self.part_infrastructure_setting_att.BodiesUnderOperationsInTree

    @bodies_under_operations_in_tree.setter
    def bodies_under_operations_in_tree(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.BodiesUnderOperationsInTree = value

    @property
    def color_synchronization_editable(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ColorSynchronizationEditability
                | o Property ColorSynchronizationEditability(    ) As
                | 
                | Returns or sets the "ColorSynchronizationEditability"
                | parameter. Role: This parameter determines whether color
                | synchronization property on Part is editable or not. Color
                | synchronization editability defines whether the property of
                | synchronization on Part can be interactively editable If it
                | is valuated to 1, user will be able to interactively modify
                | the Part property of Color management tab for
                | synchronization. If it is defined to 0, user will not be
                | able to interactively modify the Part property of Color
                | management tab for synchronization. This option cannot be
                | changed after a document has been opened.

        :return: bool
        """
        return self.part_infrastructure_setting_att.ColorSynchronizationEditability

    @color_synchronization_editable.setter
    def color_synchronization_editable(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ColorSynchronizationEditability = value

    @property
    def color_synchronization_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ColorSynchronizationMode
                | o Property ColorSynchronizationMode(    ) As
                | 
                | Returns or sets the "ColorSynchronizationMode" parameter.
                | Role: This parameter determines color synchronization mode
                | for imported features in a part. Color synchronization mode
                | defines whether the imported feature, created through
                | copy/paste as result with link mechanism, copies reference
                | feature colors on its faces or not. If it is valuated to 1,
                | synchronization will be effective and referece feature
                | colors will be reported. If it is defined to 0, nothing will
                | be copied(default mode). This option cannot be changed after
                | a document has been opened.

        :return: bool
        """
        return self.part_infrastructure_setting_att.ColorSynchronizationMode

    @color_synchronization_mode.setter
    def color_synchronization_mode(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ColorSynchronizationMode = value

    @property
    def color_synchronization_mode_manage(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ColorSynchronizationModeManage
                | o Property ColorSynchronizationModeManage(    ) As
                | 
                | Returns or sets the "ColorSynchronizationModeManage"
                | parameter. Role: This parameter determines access to
                | specific color synchronization mode for imported features in
                | a part. Color synchronization mode Manage defines if access
                | is granted to color synchronization suboptions "on feature"
                | and "on subelements". If it is valuated to 1, access will be
                | granted. If it is defined to 0, no acces to color on feature
                | & color on subelements options

        :return: bool
        """
        return self.part_infrastructure_setting_att.ColorSynchronizationModeManage

    @color_synchronization_mode_manage.setter
    def color_synchronization_mode_manage(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ColorSynchronizationModeManage = value

    @property
    def color_synchronization_mode_on_feature(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ColorSynchronizationModeOnFeature
                | o Property ColorSynchronizationModeOnFeature(    ) As
                | 
                | Returns or sets the "ColorSynchronizationModeOnFeature"
                | parameter. Role: This parameter determines graphic
                | properties synchronization mode on feature for imported
                | features in a part. Color synchronization mode defines
                | whether the imported feature, created through copy/paste as
                | result with link mechanism, copies reference feature graphic
                | properties or not. If it is valuated to 1, synchronization
                | will be effective and referece feature graphic properties
                | will be reported. If it is defined to 0, nothing will be
                | copied(default mode).

        :return: bool
        """
        return self.part_infrastructure_setting_att.ColorSynchronizationModeOnFeature

    @color_synchronization_mode_on_feature.setter
    def color_synchronization_mode_on_feature(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ColorSynchronizationModeOnFeature = value

    @property
    def color_synchronization_mode_on_sub_elements(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ColorSynchronizationModeOnSubElements
                | o Property ColorSynchronizationModeOnSubElements(    ) As
                | 
                | Returns or sets the "ColorSynchronizationModeOnSubElements"
                | parameter. Role: This parameter determines color
                | synchronization mode for imported features in a part. Color
                | synchronization mode OnSubElements defines whether the
                | imported feature, created through copy/paste as result with
                | link mechanism, copies reference feature colors on his
                | overloaded faces or not. If it is valuated to 1,
                | synchronization will be effective and reference subelements
                | colors will be reported. If it is defined to 0, nothing will
                | be copied(default mode).

        :return: bool
        """
        return self.part_infrastructure_setting_att.ColorSynchronizationModeOnSubElements

    @color_synchronization_mode_on_sub_elements.setter
    def color_synchronization_mode_on_sub_elements(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ColorSynchronizationModeOnSubElements = value

    @property
    def colors_3d_experience_management(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Colors3DExperienceManagement
                | o Property Colors3DExperienceManagement(    ) As
                | 
                | Returns or sets the "Colors3DExperienceManagement"
                | parameter. Role: This parameter determines whether color
                | synchronization property on Part is editable or not. Color
                | synchronization editability defines whether the property of
                | synchronization on Part can be interactively editable If it
                | is valuated to 1, user will be able to interactively modify
                | the Part property of Color management tab for
                | synchronization. If it is defined to 0, user will not be
                | able to interactively modify the Part property of Color
                | management tab for synchronization. This option cannot be
                | changed after a document has been opened.

        :return:
        """
        return self.part_infrastructure_setting_att.Colors3DExperienceManagement

    @colors_3d_experience_management.setter
    def colors_3d_experience_management(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.Colors3DExperienceManagement = value

    @property
    def constraints_in_geometry(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConstraintsInGeometry
                | o Property ConstraintsInGeometry(    ) As
                | 
                | Returns or sets the "ConstraintsInGeometry" parameter. Role:
                | This parameter enables constraints to be visualized in the
                | 3D view.

        :return: bool
        """
        return self.part_infrastructure_setting_att.ConstraintsInGeometry

    @constraints_in_geometry.setter
    def constraints_in_geometry(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ConstraintsInGeometry = value

    @property
    def constraints_node_in_tree(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConstraintsNodeInTree
                | o Property ConstraintsNodeInTree(    ) As
                | 
                | Returns or sets the "ConstraintsNodeInTree" parameter. Role:
                | This parameter determines if a node called "Constraints" is
                | created to contain all constraints. Its value can be changed
                | even after constraints have been created. The result is that
                | the specification tree node display status will be affected.

        :return: bool
        """
        return self.part_infrastructure_setting_att.ConstraintsNodeInTree

    @constraints_node_in_tree.setter
    def constraints_node_in_tree(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ConstraintsNodeInTree = value

    @property
    def contextual_features_selectable_at_creation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ContextualFeaturesSelectableAtCreation
                | o Property ContextualFeaturesSelectableAtCreation(    ) As
                | 
                | Returns or sets the "ContextualFeaturesSelectableAtCreation"
                | parameter. Role: This parameter determines if contextual
                | features can be selected during the creation of an other
                | feature.

        :return: bool
        """
        return self.part_infrastructure_setting_att.ContextualFeaturesSelectableAtCreation

    @contextual_features_selectable_at_creation.setter
    def contextual_features_selectable_at_creation(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ContextualFeaturesSelectableAtCreation = value

    @property
    def default_colors_editability(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DefaultColorsEditability
                | o Property DefaultColorsEditability(    ) As
                | 
                | Returns or sets the "DefaultColorsEditability" parameter.
                | Role: This parameter determines whether color
                | synchronization property on Part is editable or not. Color
                | synchronization editability defines whether the property of
                | synchronization on Part can be interactively editable If it
                | is valuated to 1, user will be able to interactively modify
                | the Part property of Color management tab for
                | synchronization. If it is defined to 0, user will not be
                | able to interactively modify the Part property of Color
                | management tab for synchronization. This option cannot be
                | changed after a document has been opened.

        :return: bool
        """
        return self.part_infrastructure_setting_att.DefaultColorsEditability

    @default_colors_editability.setter
    def default_colors_editability(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.DefaultColorsEditability = value

    @property
    def delete_warning_box(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DeleteWarningBox
                | o Property DeleteWarningBox(    ) As
                | 
                | Returns or sets the "DeleteWarningBox" parameter. Role: This
                | parameter defines if a warning box is displayed when an
                | element is deleted.

        :return: bool
        """
        return self.part_infrastructure_setting_att.DeleteWarningBox

    @delete_warning_box.setter
    def delete_warning_box(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.DeleteWarningBox = value

    @property
    def display_geometry_after_current(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DisplayGeometryAfterCurrent
                | o Property DisplayGeometryAfterCurrent(    ) As
                | 
                | Returns or sets the "DisplayGeometryAfterCurrent" parameter.
                | Role: This parameter enables to visualize in the 3D features
                | after the current object in O.G.S. and "solid and surface
                | set".

        :return: bool
        """
        return self.part_infrastructure_setting_att.DisplayGeometryAfterCurrent

    @display_geometry_after_current.setter
    def display_geometry_after_current(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.DisplayGeometryAfterCurrent = value

    @property
    def expand_sketch_based_features_node_at_creation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExpandSketchBasedFeaturesNodeAtCreation
                | o Property ExpandSketchBasedFeaturesNodeAtCreation(    ) As
                | 
                | Returns or sets the
                | "ExpandSketchBasedFeaturesNodeAtCreation" parameter. Role:
                | This parameter determines if specification tree nodes for
                | sketch-based features are expanded when such elements are
                | created. This will enable to view their sketch node.

        :return: bool
        """
        return self.part_infrastructure_setting_att.ExpandSketchBasedFeaturesNodeAtCreation

    @expand_sketch_based_features_node_at_creation.setter
    def expand_sketch_based_features_node_at_creation(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ExpandSketchBasedFeaturesNodeAtCreation = value

    @property
    def external_references_as_visible(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExternalReferencesAsVisible
                | o Property ExternalReferencesAsVisible(    ) As
                | 
                | Returns or sets the "ExternalReferencesAsVisible" parameter.
                | Role: This parameter defines if an external reference is
                | visible when being created.

        :return: bool
        """
        return self.part_infrastructure_setting_att.ExternalReferencesAsVisible

    @external_references_as_visible.setter
    def external_references_as_visible(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ExternalReferencesAsVisible = value

    @property
    def external_references_assembly_root_context(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExternalReferencesAssemblyRootContext
                | o Property ExternalReferencesAssemblyRootContext(    ) As
                | 
                | Returns or sets the "ExternalReferencesAssemblyRootContext"
                | parameter. Role: This parameter defines if external
                | references are created using the root context of an
                | assembly.

        :return: bool
        """
        return self.part_infrastructure_setting_att.ExternalReferencesAssemblyRootContext

    @external_references_assembly_root_context.setter
    def external_references_assembly_root_context(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ExternalReferencesAssemblyRootContext = value

    @property
    def external_references_node_in_tree(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ExternalReferencesNodeInTree
                | o Property ExternalReferencesNodeInTree(    ) As
                | 
                | Returns or sets the "ExternalReferencesNodeInTree"
                | parameter. Role: This parameter determines if a node called
                | "External Reference" is created to contain all linked
                | external references. Its value can be changed even after
                | linked external references have been created. The result is
                | that the specification tree node display status will be
                | affected.

        :return: bool
        """
        return self.part_infrastructure_setting_att.ExternalReferencesNodeInTree

    @external_references_node_in_tree.setter
    def external_references_node_in_tree(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ExternalReferencesNodeInTree = value

    @property
    def hybrid_design_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | HybridDesignMode
                | o Property HybridDesignMode(    ) As
                | 
                | Returns or sets the "HybridDesignMode" parameter. Role: This
                | parameter determines if hybrid design is possible inside
                | Part Bodies and bodies. This option can be changed even
                | after a document has been opened.

        :return: bool
        """
        return self.part_infrastructure_setting_att.HybridDesignMode

    @hybrid_design_mode.setter
    def hybrid_design_mode(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.HybridDesignMode = value

    @property
    def knowledge_in_hybrid_design_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | KnowledgeInHybridDesignMode
                | o Property KnowledgeInHybridDesignMode(    ) As
                | 
                | Returns or sets the "KnowledgeInHybridDesignMode" parameter.
                | Role: This parameter determines if knowledge features
                | (formulas, parameters, rules, ...) can be located inside
                | ordered sets. This option can be changed even after a
                | document has been opened.

        :return: bool
        """
        return self.part_infrastructure_setting_att.KnowledgeInHybridDesignMode

    @knowledge_in_hybrid_design_mode.setter
    def knowledge_in_hybrid_design_mode(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.KnowledgeInHybridDesignMode = value

    @property
    def linked_external_references(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | LinkedExternalReferences
                | o Property LinkedExternalReferences(    ) As
                | 
                | Returns or sets the "LinkedExternalReferences" parameter.
                | Role: This parameter enables creation of external references
                | with links.

        :return: bool
        """
        return self.part_infrastructure_setting_att.LinkedExternalReferences

    @linked_external_references.setter
    def linked_external_references(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.LinkedExternalReferences = value

    @property
    def linked_external_references_only_on_publication(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | LinkedExternalReferencesOnlyOnPublication
                | o Property LinkedExternalReferencesOnlyOnPublication(    ) As
                | 
                | Returns or sets the
                | "LinkedExternalReferencesOnlyOnPublication" parameter. Role:
                | This parameter restricts the creation of external references
                | with links to only published elements. This option is only
                | used when external references are created with link.

        :return: bool
        """
        return self.part_infrastructure_setting_att.LinkedExternalReferencesOnlyOnPublication

    @linked_external_references_only_on_publication.setter
    def linked_external_references_only_on_publication(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.LinkedExternalReferencesOnlyOnPublication = value

    @property
    def linked_external_references_warning_at_creation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | LinkedExternalReferencesWarningAtCreation
                | o Property LinkedExternalReferencesWarningAtCreation(    ) As
                | 
                | Returns or sets the
                | "LinkedExternalReferencesWarningAtCreation" parameter. Role:
                | This parameter defines if a warning panel is displayed each
                | time an external reference with llink is created. The panel
                | enables the user to decide whether the link will be kept or
                | not. This option is only used when external references are
                | created with link.

        :return: bool
        """
        return self.part_infrastructure_setting_att.LinkedExternalReferencesWarningAtCreation

    @linked_external_references_warning_at_creation.setter
    def linked_external_references_warning_at_creation(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.LinkedExternalReferencesWarningAtCreation = value

    @property
    def naming_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NamingMode
                | o Property NamingMode(    ) As
                | 
                | Returns or sets the "NamingMode" parameter. Role: This
                | parameter determines how an element can be named through
                | Edit/Properties or any operation creating a feature (Copy-
                | Paste, etc.). When this option is being changed, it only
                | affects elements whose name is modified afterwards.

        :return: int enumeration_type
        """
        return self.part_infrastructure_setting_att.NamingMode

    @naming_mode.setter
    def naming_mode(self, value):
        """
            :param int value:
        """
        self.part_infrastructure_setting_att.NamingMode = value

    @property
    def new_with_3d_support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NewWith3DSupport
                | o Property NewWith3DSupport(    ) As
                | 
                | Returns or sets the "NewWith3DSupport" parameter. Role: This
                | parameter determines if a new .CATPart document will be
                | created with 3D working support.

        :return: bool
        """
        return self.part_infrastructure_setting_att.NewWith3DSupport

    @new_with_3d_support.setter
    def new_with_3d_support(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.NewWith3DSupport = value

    @property
    def new_with_axis_system(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NewWithAxisSystem
                | o Property NewWithAxisSystem(    ) As
                | 
                | Returns or sets the "NewWithAxisSystem" parameter. Role:
                | This parameter determines if a new .CATPart document will be
                | created with an Axis System.

        :return: bool
        """
        return self.part_infrastructure_setting_att.NewWithAxisSystem

    @new_with_axis_system.setter
    def new_with_axis_system(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.NewWithAxisSystem = value

    @property
    def new_with_gs(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NewWithGS
                | o Property NewWithGS(    ) As
                | 
                | Returns or sets the "NewWithGS" parameter. Role: This
                | parameter determines if a new .CATPart document will be
                | created with a Geometrical Set.

        :return: bool
        """
        return self.part_infrastructure_setting_att.NewWithGS

    @new_with_gs.setter
    def new_with_gs(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.NewWithGS = value

    @property
    def new_with_ogs(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NewWithOGS
                | o Property NewWithOGS(    ) As
                | 
                | Returns or sets the "NewWithOGS" parameter. Role: This
                | parameter determines if a new .CATPart document will be
                | created with an Ordered Geometrical Set.

        :return: bool
        """
        return self.part_infrastructure_setting_att.NewWithOGS

    @new_with_ogs.setter
    def new_with_ogs(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.NewWithOGS = value

    @property
    def new_with_panel(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | NewWithPanel
                | o Property NewWithPanel(    ) As
                | 
                | Returns or sets the "NewWithPanel" parameter. Role: This
                | parameter determines if a dedicated 'New Part' panel is
                | displayed when createing a new .CATPart document.

        :return: bool
        """
        return self.part_infrastructure_setting_att.NewWithPanel

    @new_with_panel.setter
    def new_with_panel(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.NewWithPanel = value

    @property
    def only_current_operated_solid_set_in_geometry(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OnlyCurrentOperatedSolidSetInGeometry
                | o Property OnlyCurrentOperatedSolidSetInGeometry(    ) As
                | 
                | Returns or sets the "OnlyCurrentOperatedSolidSetInGeometry"
                | parameter. Role: This parameter enables to visualize in the
                | 3D only the current operated body's feature (operated means
                | being aggregated in a boolean operation), as well as all
                | other bodies and sets direcly inserted under the Part
                | feature.

        :return: bool
        """
        return self.part_infrastructure_setting_att.OnlyCurrentOperatedSolidSetInGeometry

    @only_current_operated_solid_set_in_geometry.setter
    def only_current_operated_solid_set_in_geometry(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.OnlyCurrentOperatedSolidSetInGeometry = value

    @property
    def only_current_solid_set_in_geometry(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OnlyCurrentSolidSetInGeometry
                | o Property OnlyCurrentSolidSetInGeometry(    ) As
                | 
                | Returns or sets the "OnlyCurrentSolidSetInGeometry"
                | parameter. Role: This parameter enables to visualize in the
                | 3D only the current operated body's feature (operated means
                | being aggregated in a boolean operation), as well as all
                | other bodies and sets direcly inserted under the Part
                | feature.

        :return: bool
        """
        return self.part_infrastructure_setting_att.OnlyCurrentSolidSetInGeometry

    @only_current_solid_set_in_geometry.setter
    def only_current_solid_set_in_geometry(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.OnlyCurrentSolidSetInGeometry = value

    @property
    def parameters_node_in_tree(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ParametersNodeInTree
                | o Property ParametersNodeInTree(    ) As
                | 
                | Returns or sets the "ParametersNodeInTree" parameter. Role:
                | This parameter determines if a node called "Parameters" is
                | created to contain all Knowledgeware parameters. Its value
                | can be changed even after parameters have been created. The
                | result is that the specification tree node display status
                | will be affected.

        :return: bool
        """
        return self.part_infrastructure_setting_att.ParametersNodeInTree

    @parameters_node_in_tree.setter
    def parameters_node_in_tree(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ParametersNodeInTree = value

    @property
    def publish_topological_elements(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PublishTopologicalElements
                | o Property PublishTopologicalElements(    ) As
                | 
                | Returns or sets the "PublishTopologicalElements" parameter.
                | Role: This parameter defines if topological elements (faces,
                | edges, vertices, axes extremities) can be published.

        :return: bool
        """
        return self.part_infrastructure_setting_att.PublishTopologicalElements

    @publish_topological_elements.setter
    def publish_topological_elements(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.PublishTopologicalElements = value

    @property
    def relations_node_in_tree(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RelationsNodeInTree
                | o Property RelationsNodeInTree(    ) As
                | 
                | Returns or sets the "RelationsNodeInTree" parameter. Role:
                | This parameter determines if a node called "Relations" is
                | created to contain all Knowledgeware relations (for instance
                | formulas). Its value can be changed even after parameters
                | have been created. The result is that the specification tree
                | node display status will be affected.

        :return: bool
        """
        return self.part_infrastructure_setting_att.RelationsNodeInTree

    @relations_node_in_tree.setter
    def relations_node_in_tree(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.RelationsNodeInTree = value

    @property
    def replace_only_after_current(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ReplaceOnlyAfterCurrent
                | o Property ReplaceOnlyAfterCurrent(    ) As
                | 
                | Returns or sets the "ReplaceOnlyAfterCurrent" parameter.
                | Role: This parameter defines if the replace operation can
                | only apply to components located after the current object.

        :return: bool
        """
        return self.part_infrastructure_setting_att.ReplaceOnlyAfterCurrent

    @replace_only_after_current.setter
    def replace_only_after_current(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.ReplaceOnlyAfterCurrent = value

    @property
    def surface_elements_location(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SurfaceElementsLocation
                | o Property SurfaceElementsLocation(    ) As
                | 
                | Returns or sets the "SurfaceElementsLocation" parameter.
                | Role: This parameter determines where wireframe and surface
                | elements are created when hybrid design is active. This
                | option can be changed when hybrid design mode is not active
                | (but useless then), and also even after a document has been
                | opened.

        :return: int enumeration_type
        """
        return self.part_infrastructure_setting_att.SurfaceElementsLocation

    @surface_elements_location.setter
    def surface_elements_location(self, value):
        """
            :param int value:
        """
        self.part_infrastructure_setting_att.SurfaceElementsLocation = value

    @property
    def true_color_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TrueColorMode
                | o Property TrueColorMode(    ) As
                | 
                | Returns or sets the "ColorInheritanceMode" parameter. Role:
                | This parameter determines color inheritance mode for
                | absorbing features in a part. Color inheritance mode defines
                | which mode of propagation will be used to set color on an
                | absorbing feature. If it is valuated to 1, absorbing feature
                | will inherit colors from all their input. If it is defined
                | to 0, absorbing features will inherit colors from their main
                | input only (default mode). This option can be changed even
                | after a document has been opened.

        :return: bool
        """
        return self.part_infrastructure_setting_att.TrueColorMode

    @true_color_mode.setter
    def true_color_mode(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.TrueColorMode = value

    @property
    def update_elements_refreshed(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UpdateElementsRefreshed
                | o Property UpdateElementsRefreshed(    ) As
                | 
                | Returns or sets the "UpdateElementsRefreshed" parameter.
                | Role: This parameter determines if elements visualization
                | has to be refreshed individually during update tasks.

        :return: bool
        """
        return self.part_infrastructure_setting_att.UpdateElementsRefreshed

    @update_elements_refreshed.setter
    def update_elements_refreshed(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.UpdateElementsRefreshed = value

    @property
    def update_linked_external_references(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UpdateLinkedExternalReferences
                | o Property UpdateLinkedExternalReferences(    ) As
                | 
                | Returns or sets the "UpdateLinkedExternalReferences"
                | parameter. Role: This parameter determines if update tasks
                | also apply to linked external references.

        :return: bool
        """
        return self.part_infrastructure_setting_att.UpdateLinkedExternalReferences

    @update_linked_external_references.setter
    def update_linked_external_references(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.UpdateLinkedExternalReferences = value

    @property
    def update_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UpdateMode
                | o Property UpdateMode(    ) As
                | 
                | Returns or sets the "UpdateMode" parameter. Role: This
                | parameter determines how the update of a .CATPart document
                | is conducted.

        :return: int enumeration_type
        """
        return self.part_infrastructure_setting_att.UpdateMode

    @update_mode.setter
    def update_mode(self, value):
        """
            :param int value:
        """
        self.part_infrastructure_setting_att.UpdateMode = value

    @property
    def update_stopped_on_error(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | UpdateStoppedOnError
                | o Property UpdateStoppedOnError(    ) As
                | 
                | Returns or sets the "UpdateStoppedOnError" parameter. Role:
                | This parameter determines if update tasks stop on the first
                | detected error.

        :return: bool
        """
        return self.part_infrastructure_setting_att.UpdateStoppedOnError

    @update_stopped_on_error.setter
    def update_stopped_on_error(self, value):
        """
            :param bool value:
        """
        self.part_infrastructure_setting_att.UpdateStoppedOnError = value

    def get_also_delete_exclusive_parents_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAlsoDeleteExclusiveParentsInfo
                | o Func GetAlsoDeleteExclusiveParentsInfo(        ioAdminLevel,
                |                                                  ioLocked) As
                | 
                | Retrieves environment informations for the
                | "AlsoDeleteExclusiveParents" parameter. Role:Retrieves the
                | state of the "AlsoDeleteExclusiveParents" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetAlsoDeleteExclusiveParentsInfo(io_admin_level, io_locked)

    def get_axis_system_size_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAxisSystemSizeInfo
                | o Func GetAxisSystemSizeInfo(        ioAdminLevel,
                |                                      ioLocked) As
                | 
                | Retrieves environment informations for the "AxisSystemSize"
                | parameter. Role:Retrieves the state of the "AxisSystemSize"
                | parameter in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetAxisSystemSizeInfo(io_admin_level, io_locked)

    def get_bodies_under_operations_in_tree_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetBodiesUnderOperationsInTreeInfo
                | o Func GetBodiesUnderOperationsInTreeInfo(        ioAdminLevel,
                |                                                   ioLocked) As
                | 
                | Retrieves environment informations for the
                | "BodiesUnderOperationsInTree" parameter. Role:Retrieves the
                | state of the "BodiesUnderOperationsInTree" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetBodiesUnderOperationsInTreeInfo(io_admin_level, io_locked)

    def get_color_synchronization_editability_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetColorSynchronizationEditabilityInfo
                | o Func GetColorSynchronizationEditabilityInfo(        ioAdminLevel,
                |                                                       ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ColorSynchronizationEditability" parameter. Role:Retrieves
                | the state of the "ColorSynchronizationEditability" parameter
                | in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetColorSynchronizationEditabilityInfo(io_admin_level, io_locked)

    def get_color_synchronization_mode_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetColorSynchronizationModeInfo
                | o Func GetColorSynchronizationModeInfo(        ioAdminLevel,
                |                                                ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ColorSynchronizationMode" parameter. Role:Retrieves the
                | state of the "ColorSynchronizationMode" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetColorSynchronizationModeInfo(io_admin_level, io_locked)

    def get_color_synchronization_mode_manage_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetColorSynchronizationModeManageInfo
                | o Func GetColorSynchronizationModeManageInfo(        ioAdminLevel,
                |                                                      ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ColorSynchronizationModeManage" parameter. Role:Retrieves
                | the state of the "ColorSynchronizationModeManage" parameter
                | in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetColorSynchronizationModeManageInfo(io_admin_level, io_locked)

    def get_color_synchronization_mode_on_feature_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetColorSynchronizationModeOnFeatureInfo
                | o Func GetColorSynchronizationModeOnFeatureInfo(        ioAdminLevel,
                |                                                         ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ColorSynchronizationModeOnFeature" parameter.
                | Role:Retrieves the state of the
                | "ColorSynchronizationModeOnFeature" parameter in the current
                | environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetColorSynchronizationModeOnFeatureInfo(io_admin_level, io_locked)

    def get_color_synchronization_mode_on_sub_elements_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetColorSynchronizationModeOnSubElementsInfo
                | o Func GetColorSynchronizationModeOnSubElementsInfo(        ioAdminLevel,
                |                                                             ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ColorSynchronizationModeOnSubElements" parameter.
                | Role:Retrieves the state of the
                | "ColorSynchronizationModeOnSubElements" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetColorSynchronizationModeOnSubElementsInfo(io_admin_level,
                                                                                                 io_locked)

    def get_colors_3d_experience_management_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetColors3DExperienceManagementInfo
                | o Func GetColors3DExperienceManagementInfo(        ioAdminLevel,
                |                                                    ioLocked) As
                | 
                | Retrieves environment informations for the
                | "Colors3DExperienceManagement" parameter. Role:Retrieves the
                | state of the "Colors3DExperienceManagement" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetColors3DExperienceManagementInfo(io_admin_level, io_locked)

    def get_constraints_in_geometry_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetConstraintsInGeometryInfo
                | o Func GetConstraintsInGeometryInfo(        ioAdminLevel,
                |                                             ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ConstraintsInGeometry" parameter. Role:Retrieves the state
                | of the "ConstraintsInGeometry" parameter in the current
                | environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetConstraintsInGeometryInfo(io_admin_level, io_locked)

    def get_constraints_node_in_tree_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetConstraintsNodeInTreeInfo
                | o Func GetConstraintsNodeInTreeInfo(        ioAdminLevel,
                |                                             ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ConstraintsNodeInTree" parameter. Role:Retrieves the state
                | of the "ConstraintsNodeInTree" parameter in the current
                | environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetConstraintsNodeInTreeInfo(io_admin_level, io_locked)

    def get_contextual_features_selectable_at_creation_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetContextualFeaturesSelectableAtCreationInfo
                | o Func GetContextualFeaturesSelectableAtCreationInfo(        ioAdminLevel,
                |                                                              ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ContextualFeaturesSelectableAtCreation" parameter.
                | Role:Retrieves the state of the
                | "ContextualFeaturesSelectableAtCreation" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetContextualFeaturesSelectableAtCreationInfo(io_admin_level,
                                                                                                  io_locked)

    def get_default_colors_editability_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDefaultColorsEditabilityInfo
                | o Func GetDefaultColorsEditabilityInfo(        ioAdminLevel,
                |                                                ioLocked) As
                | 
                | Retrieves environment informations for the
                | "DefaultColorsEditability" parameter. Role:Retrieves the
                | state of the "DefaultColorsEditability" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetDefaultColorsEditabilityInfo(io_admin_level, io_locked)

    def get_delete_warning_box_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDeleteWarningBoxInfo
                | o Func GetDeleteWarningBoxInfo(        ioAdminLevel,
                |                                        ioLocked) As
                | 
                | Retrieves environment informations for the
                | "DeleteWarningBox" parameter. Role:Retrieves the state of
                | the "DeleteWarningBox" parameter in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetDeleteWarningBoxInfo(io_admin_level, io_locked)

    def get_display_geometry_after_current_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDisplayGeometryAfterCurrentInfo
                | o Func GetDisplayGeometryAfterCurrentInfo(        ioAdminLevel,
                |                                                   ioLocked) As
                | 
                | Retrieves environment informations for the
                | "DisplayGeometryAfterCurrent" parameter. Role:Retrieves the
                | state of the "DisplayGeometryAfterCurrent" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetDisplayGeometryAfterCurrentInfo(io_admin_level, io_locked)

    def get_expand_sketch_based_features_node_at_creation_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetExpandSketchBasedFeaturesNodeAtCreationInfo
                | o Func GetExpandSketchBasedFeaturesNodeAtCreationInfo(        ioAdminLevel,
                |                                                               ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ExpandSketchBasedFeaturesNodeAtCreation" parameter.
                | Role:Retrieves the state of the
                | "ExpandSketchBasedFeaturesNodeAtCreation" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetExpandSketchBasedFeaturesNodeAtCreationInfo(io_admin_level,
                                                                                                   io_locked)

    def get_external_references_as_visible_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetExternalReferencesAsVisibleInfo
                | o Func GetExternalReferencesAsVisibleInfo(        ioAdminLevel,
                |                                                   ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ExternalReferencesAsVisible" parameter. Role:Retrieves the
                | state of the "ExternalReferencesAsVisible" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetExternalReferencesAsVisibleInfo(io_admin_level, io_locked)

    def get_external_references_assembly_root_context_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetExternalReferencesAssemblyRootContextInfo
                | o Func GetExternalReferencesAssemblyRootContextInfo(        ioAdminLevel,
                |                                                             ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ExternalReferencesAssemblyRootContext" parameter.
                | Role:Retrieves the state of the
                | "ExternalReferencesAssemblyRootContext" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetExternalReferencesAssemblyRootContextInfo(io_admin_level,
                                                                                                 io_locked)

    def get_external_references_node_in_tree_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetExternalReferencesNodeInTreeInfo
                | o Func GetExternalReferencesNodeInTreeInfo(        ioAdminLevel,
                |                                                    ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ExternalReferencesNodeInTree" parameter. Role:Retrieves the
                | state of the "ExternalReferencesNodeInTree" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetExternalReferencesNodeInTreeInfo(io_admin_level, io_locked)

    def get_hybrid_design_mode_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetHybridDesignModeInfo
                | o Func GetHybridDesignModeInfo(        ioAdminLevel,
                |                                        ioLocked) As
                | 
                | Retrieves environment informations for the
                | "HybridDesignMode" parameter. Role:Retrieves the state of
                | the "HybridDesignMode" parameter in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetHybridDesignModeInfo(io_admin_level, io_locked)

    def get_knowledge_in_hybrid_design_mode_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetKnowledgeInHybridDesignModeInfo
                | o Func GetKnowledgeInHybridDesignModeInfo(        ioAdminLevel,
                |                                                   ioLocked) As
                | 
                | Retrieves environment informations for the
                | "KnowledgeInHybridDesignMode" parameter. Role:Retrieves the
                | state of the "KnowledgeInHybridDesignMode" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetKnowledgeInHybridDesignModeInfo(io_admin_level, io_locked)

    def get_linked_external_references_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLinkedExternalReferencesInfo
                | o Func GetLinkedExternalReferencesInfo(        ioAdminLevel,
                |                                                ioLocked) As
                | 
                | Retrieves environment informations for the
                | "LinkedExternalReferences" parameter. Role:Retrieves the
                | state of the "LinkedExternalReferences" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetLinkedExternalReferencesInfo(io_admin_level, io_locked)

    def get_linked_external_references_only_on_publication_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLinkedExternalReferencesOnlyOnPublicationInfo
                | o Func GetLinkedExternalReferencesOnlyOnPublicationInfo(        ioAdminLevel,
                |                                                                 ioLocked) As
                | 
                | Retrieves environment informations for the
                | "LinkedExternalReferencesOnlyOnPublication" parameter.
                | Role:Retrieves the state of the
                | "LinkedExternalReferencesOnlyOnPublication" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetLinkedExternalReferencesOnlyOnPublicationInfo(io_admin_level,
                                                                                                     io_locked)

    def get_linked_external_references_warning_at_creation_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLinkedExternalReferencesWarningAtCreationInfo
                | o Func GetLinkedExternalReferencesWarningAtCreationInfo(        ioAdminLevel,
                |                                                                 ioLocked) As
                | 
                | Retrieves environment informations for the
                | "LinkedExternalReferencesWarningAtCreation" parameter.
                | Role:Retrieves the state of the
                | "LinkedExternalReferencesWarningAtCreation" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetLinkedExternalReferencesWarningAtCreationInfo(io_admin_level,
                                                                                                     io_locked)

    def get_naming_mode_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNamingModeInfo
                | o Func GetNamingModeInfo(        ioAdminLevel,
                |                                  ioLocked) As
                | 
                | Retrieves environment informations for the "NamingMode"
                | parameter. Role:Retrieves the state of the "NamingMode"
                | parameter in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetNamingModeInfo(io_admin_level, io_locked)

    def get_new_with_3d_support_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNewWith3DSupportInfo
                | o Func GetNewWith3DSupportInfo(        ioAdminLevel,
                |                                        ioLocked) As
                | 
                | Retrieves environment informations for the
                | "NewWith3DSupport" parameter. Role:Retrieves the state of
                | the "NewWith3DSupport" parameter in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetNewWith3DSupportInfo(io_admin_level, io_locked)

    def get_new_with_axis_system_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNewWithAxisSystemInfo
                | o Func GetNewWithAxisSystemInfo(        ioAdminLevel,
                |                                         ioLocked) As
                | 
                | Retrieves environment informations for the
                | "NewWithAxisSystem" parameter. Role:Retrieves the state of
                | the "NewWithAxisSystem" parameter in the current
                | environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetNewWithAxisSystemInfo(io_admin_level, io_locked)

    def get_new_with_gs_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNewWithGSInfo
                | o Func GetNewWithGSInfo(        ioAdminLevel,
                |                                 ioLocked) As
                | 
                | Retrieves environment informations for the "NewWithGS"
                | parameter. Role:Retrieves the state of the "NewWithGS"
                | parameter in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetNewWithGSInfo(io_admin_level, io_locked)

    def get_new_with_ogs_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNewWithOGSInfo
                | o Func GetNewWithOGSInfo(        ioAdminLevel,
                |                                  ioLocked) As
                | 
                | Retrieves environment informations for the "NewWithOGS"
                | parameter. Role:Retrieves the state of the "NewWithOGS"
                | parameter in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetNewWithOGSInfo(io_admin_level, io_locked)

    def get_new_with_panel_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNewWithPanelInfo
                | o Func GetNewWithPanelInfo(        ioAdminLevel,
                |                                    ioLocked) As
                | 
                | Retrieves environment informations for the "NewWithPanel"
                | parameter. Role:Retrieves the state of the "NewWithPanel"
                | parameter in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetNewWithPanelInfo(io_admin_level, io_locked)

    def get_only_current_operated_solid_set_in_geometry_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOnlyCurrentOperatedSolidSetInGeometryInfo
                | o Func GetOnlyCurrentOperatedSolidSetInGeometryInfo(        ioAdminLevel,
                |                                                             ioLocked) As
                | 
                | Retrieves environment informations for the
                | "OnlyCurrentOperatedSolidSetInGeometry" parameter.
                | Role:Retrieves the state of the
                | "OnlyCurrentOperatedSolidSetInGeometry" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetOnlyCurrentOperatedSolidSetInGeometryInfo(io_admin_level,
                                                                                                 io_locked)

    def get_only_current_solid_set_in_geometry_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetOnlyCurrentSolidSetInGeometryInfo
                | o Func GetOnlyCurrentSolidSetInGeometryInfo(        ioAdminLevel,
                |                                                     ioLocked) As
                | 
                | Retrieves environment informations for the
                | "OnlyCurrentSolidSetInGeometry" parameter. Role:Retrieves
                | the state of the "OnlyCurrentSolidSetInGeometry" parameter
                | in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetOnlyCurrentSolidSetInGeometryInfo(io_admin_level, io_locked)

    def get_parameters_node_in_tree_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetParametersNodeInTreeInfo
                | o Func GetParametersNodeInTreeInfo(        ioAdminLevel,
                |                                            ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ParametersNodeInTree" parameter. Role:Retrieves the state
                | of the "ParametersNodeInTree" parameter in the current
                | environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetParametersNodeInTreeInfo(io_admin_level, io_locked)

    def get_publish_topological_elements_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPublishTopologicalElementsInfo
                | o Func GetPublishTopologicalElementsInfo(        ioAdminLevel,
                |                                                  ioLocked) As
                | 
                | Retrieves environment informations for the
                | "PublishTopologicalElements" parameter. Role:Retrieves the
                | state of the "PublishTopologicalElements" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetPublishTopologicalElementsInfo(io_admin_level, io_locked)

    def get_relations_node_in_tree_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetRelationsNodeInTreeInfo
                | o Func GetRelationsNodeInTreeInfo(        ioAdminLevel,
                |                                           ioLocked) As
                | 
                | Retrieves environment informations for the
                | "RelationsNodeInTree" parameter. Role:Retrieves the state of
                | the "RelationsNodeInTree" parameter in the current
                | environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetRelationsNodeInTreeInfo(io_admin_level, io_locked)

    def get_replace_only_after_current_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetReplaceOnlyAfterCurrentInfo
                | o Func GetReplaceOnlyAfterCurrentInfo(        ioAdminLevel,
                |                                               ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ReplaceOnlyAfterCurrent" parameter. Role:Retrieves the
                | state of the "ReplaceOnlyAfterCurrent" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetReplaceOnlyAfterCurrentInfo(io_admin_level, io_locked)

    def get_surface_elements_location_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSurfaceElementsLocationInfo
                | o Func GetSurfaceElementsLocationInfo(        ioAdminLevel,
                |                                               ioLocked) As
                | 
                | Retrieves environment informations for the
                | "SurfaceElementsLocation" parameter. Role:Retrieves the
                | state of the "SurfaceElementsLocation" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetSurfaceElementsLocationInfo(io_admin_level, io_locked)

    def get_true_color_mode_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetTrueColorModeInfo
                | o Func GetTrueColorModeInfo(        ioAdminLevel,
                |                                     ioLocked) As
                | 
                | Retrieves environment informations for the
                | "ColorInheritanceMode" parameter. Role:Retrieves the state
                | of the "ColorInheritanceMode" parameter in the current
                | environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetTrueColorModeInfo(io_admin_level, io_locked)

    def get_update_elements_refreshed_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetUpdateElementsRefreshedInfo
                | o Func GetUpdateElementsRefreshedInfo(        ioAdminLevel,
                |                                               ioLocked) As
                | 
                | Retrieves environment informations for the
                | "UpdateElementsRefreshed" parameter. Role:Retrieves the
                | state of the "UpdateElementsRefreshed" parameter in the
                | current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetUpdateElementsRefreshedInfo(io_admin_level, io_locked)

    def get_update_linked_external_references_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetUpdateLinkedExternalReferencesInfo
                | o Func GetUpdateLinkedExternalReferencesInfo(        ioAdminLevel,
                |                                                      ioLocked) As
                | 
                | Retrieves environment informations for the
                | "UpdateLinkedExternalReferences" parameter. Role:Retrieves
                | the state of the "UpdateLinkedExternalReferences" parameter
                | in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetUpdateLinkedExternalReferencesInfo(io_admin_level, io_locked)

    def get_update_mode_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetUpdateModeInfo
                | o Func GetUpdateModeInfo(        ioAdminLevel,
                |                                  ioLocked) As
                | 
                | Retrieves environment informations for the "UpdateMode"
                | parameter. Role:Retrieves the state of the "UpdateMode"
                | parameter in the current environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetUpdateModeInfo(io_admin_level, io_locked)

    def get_update_stopped_on_error_info(self, io_admin_level, io_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetUpdateStoppedOnErrorInfo
                | o Func GetUpdateStoppedOnErrorInfo(        ioAdminLevel,
                |                                            ioLocked) As
                | 
                | Retrieves environment informations for the
                | "UpdateStoppedOnError" parameter. Role:Retrieves the state
                | of the "UpdateStoppedOnError" parameter in the current
                | environment.
                |
                | Parameters:
                | ioAdminLevel
                |  If the parameter is locked, AdminLevel gives the administration
                |        level that imposes the value of the parameter.
                | 	 If the parameter is not locked, AdminLevel gives the administration
                |        level that will give the value of the parameter after a reset.
                |  
                |  ioLocked
                |       Indicates if the parameter has been locked.
                |  
                | 
                |  Returns:
                |         Indicates if the parameter has been explicitly modified or remain
                |       to the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.part_infrastructure_setting_att.GetUpdateStoppedOnErrorInfo(io_admin_level, io_locked)

    def set_also_delete_exclusive_parents_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAlsoDeleteExclusiveParentsLock
                | o Sub SetAlsoDeleteExclusiveParentsLock(        iLocked)
                | 
                | Locks or unlocks the "AlsoDeleteExclusiveParents" parameter.
                | Role:Locks or unlocks the "AlsoDeleteExclusiveParents"
                | parameter if it is possible in the current administrative
                | context. In user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetAlsoDeleteExclusiveParentsLock(i_locked)

    def set_axis_system_size_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAxisSystemSizeLock
                | o Sub SetAxisSystemSizeLock(        iLocked)
                | 
                | Locks or unlocks the "AxisSystemSize" parameter. Role:Locks
                | or unlocks the "AxisSystemSize" parameter if it is possible
                | in the current administrative context. In user mode this
                | method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetAxisSystemSizeLock(i_locked)

    def set_bodies_under_operations_in_tree_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetBodiesUnderOperationsInTreeLock
                | o Sub SetBodiesUnderOperationsInTreeLock(        iLocked)
                | 
                | Locks or unlocks the "BodiesUnderOperationsInTree"
                | parameter. Role:Locks or unlocks the
                | "BodiesUnderOperationsInTree" parameter if it is possible in
                | the current administrative context. In user mode this method
                | will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetBodiesUnderOperationsInTreeLock(i_locked)

    def set_color_synchronization_editability_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetColorSynchronizationEditabilityLock
                | o Sub SetColorSynchronizationEditabilityLock(        iLocked)
                | 
                | Locks or unlocks the "ColorSynchronizationEditability"
                | parameter. Role:Locks or unlocks the
                | "ColorSynchronizationEditability" parameter if it is
                | possible in the current administrative context. In user mode
                | this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetColorSynchronizationEditabilityLock(i_locked)

    def set_color_synchronization_mode_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetColorSynchronizationModeLock
                | o Sub SetColorSynchronizationModeLock(        iLocked)
                | 
                | Locks or unlocks the "ColorSynchronizationMode" parameter.
                | Role:Locks or unlocks the "ColorSynchronizationMode"
                | parameter if it is possible in the current administrative
                | context. In user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetColorSynchronizationModeLock(i_locked)

    def set_color_synchronization_mode_manage_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetColorSynchronizationModeManageLock
                | o Sub SetColorSynchronizationModeManageLock(        iLocked)
                | 
                | Locks or unlocks the "ColorSynchronizationModeManage"
                | parameter. Role:Locks or unlocks the
                | "ColorSynchronizationModeManage" parameter if it is possible
                | in the current administrative context. In user mode this
                | method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetColorSynchronizationModeManageLock(i_locked)

    def set_color_synchronization_mode_on_feature_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetColorSynchronizationModeOnFeatureLock
                | o Sub SetColorSynchronizationModeOnFeatureLock(        iLocked)
                | 
                | Locks or unlocks the "ColorSynchronizationModeOnFeature"
                | parameter. Role:Locks or unlocks the
                | "ColorSynchronizationModeOnFeature" parameter if it is
                | possible in the current administrative context. In user mode
                | this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetColorSynchronizationModeOnFeatureLock(i_locked)

    def set_color_synchronization_mode_on_sub_elements_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetColorSynchronizationModeOnSubElementsLock
                | o Sub SetColorSynchronizationModeOnSubElementsLock(        iLocked)
                | 
                | Locks or unlocks the "ColorSynchronizationModeOnSubElements"
                | parameter. Role:Locks or unlocks the
                | "ColorSynchronizationModeOnSubElements" parameter if it is
                | possible in the current administrative context. In user mode
                | this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetColorSynchronizationModeOnSubElementsLock(i_locked)

    def set_colors_3d_experience_management_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetColors3DExperienceManagementLock
                | o Sub SetColors3DExperienceManagementLock(        iLocked)
                | 
                | Locks or unlocks the "Colors3DExperienceManagement"
                | parameter. Role:Locks or unlocks the
                | "Colors3DExperienceManagement" parameter if it is possible
                | in the current administrative context. In user mode this
                | method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetColors3DExperienceManagementLock(i_locked)

    def set_constraints_in_geometry_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetConstraintsInGeometryLock
                | o Sub SetConstraintsInGeometryLock(        iLocked)
                | 
                | Locks or unlocks the "ConstraintsInGeometry" parameter.
                | Role:Locks or unlocks the "ConstraintsInGeometry" parameter
                | if it is possible in the current administrative context. In
                | user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetConstraintsInGeometryLock(i_locked)

    def set_constraints_node_in_tree_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetConstraintsNodeInTreeLock
                | o Sub SetConstraintsNodeInTreeLock(        iLocked)
                | 
                | Locks or unlocks the "ConstraintsNodeInTree" parameter.
                | Role:Locks or unlocks the "ConstraintsNodeInTree" parameter
                | if it is possible in the current administrative context. In
                | user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        :return:
        """
        self.part_infrastructure_setting_att.SetConstraintsNodeInTreeLock(i_locked)

    def set_contextual_features_selectable_at_creation_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetContextualFeaturesSelectableAtCreationLock
                | o Sub SetContextualFeaturesSelectableAtCreationLock(        iLocked)
                | 
                | Locks or unlocks the
                | "ContextualFeaturesSelectableAtCreation" parameter.
                | Role:Locks or unlocks the
                | "ContextualFeaturesSelectableAtCreation" parameter if it is
                | possible in the current administrative context. In user mode
                | this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param i_locked:
        """
        self.part_infrastructure_setting_att.SetContextualFeaturesSelectableAtCreationLock(i_locked)

    def set_default_colors_editability_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetDefaultColorsEditabilityLock
                | o Sub SetDefaultColorsEditabilityLock(        iLocked)
                | 
                | Locks or unlocks the "DefaultColorsEditability" parameter.
                | Role:Locks or unlocks the "DefaultColorsEditability"
                | parameter if it is possible in the current administrative
                | context. In user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetDefaultColorsEditabilityLock(i_locked)

    def set_delete_warning_box_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetDeleteWarningBoxLock
                | o Sub SetDeleteWarningBoxLock(        iLocked)
                | 
                | Locks or unlocks the "DeleteWarningBox" parameter.
                | Role:Locks or unlocks the "DeleteWarningBox" parameter if it
                | is possible in the current administrative context. In user
                | mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        return self.part_infrastructure_setting_att.SetDeleteWarningBoxLock(i_locked)

    def set_display_geometry_after_current_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetDisplayGeometryAfterCurrentLock
                | o Sub SetDisplayGeometryAfterCurrentLock(        iLocked)
                | 
                | Locks or unlocks the "DisplayGeometryAfterCurrent"
                | parameter. Role:Locks or unlocks the
                | "DisplayGeometryAfterCurrent" parameter if it is possible in
                | the current administrative context. In user mode this method
                | will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetDisplayGeometryAfterCurrentLock(i_locked)

    def set_expand_sketch_based_features_node_at_creation_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetExpandSketchBasedFeaturesNodeAtCreationLock
                | o Sub SetExpandSketchBasedFeaturesNodeAtCreationLock(        iLocked)
                | 
                | Locks or unlocks the
                | "ExpandSketchBasedFeaturesNodeAtCreation" parameter.
                | Role:Locks or unlocks the
                | "ExpandSketchBasedFeaturesNodeAtCreation" parameter if it is
                | possible in the current administrative context. In user mode
                | this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetExpandSketchBasedFeaturesNodeAtCreationLock(i_locked)

    def set_external_references_as_visible_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetExternalReferencesAsVisibleLock
                | o Sub SetExternalReferencesAsVisibleLock(        iLocked)
                | 
                | Locks or unlocks the "ExternalReferencesAsVisible"
                | parameter. Role:Locks or unlocks the
                | "ExternalReferencesAsVisible" parameter if it is possible in
                | the current administrative context. In user mode this method
                | will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetExternalReferencesAsVisibleLock(i_locked)

    def set_external_references_assembly_root_context_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetExternalReferencesAssemblyRootContextLock
                | o Sub SetExternalReferencesAssemblyRootContextLock(        iLocked)
                | 
                | Locks or unlocks the "ExternalReferencesAssemblyRootContext"
                | parameter. Role:Locks or unlocks the
                | "ExternalReferencesAssemblyRootContext" parameter if it is
                | possible in the current administrative context. In user mode
                | this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetExternalReferencesAssemblyRootContextLock(i_locked)

    def set_external_references_node_in_tree_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetExternalReferencesNodeInTreeLock
                | o Sub SetExternalReferencesNodeInTreeLock(        iLocked)
                | 
                | Locks or unlocks the "ExternalReferencesNodeInTree"
                | parameter. Role:Locks or unlocks the
                | "ExternalReferencesNodeInTree" parameter if it is possible
                | in the current administrative context. In user mode this
                | method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetExternalReferencesNodeInTreeLock(i_locked)

    def set_hybrid_design_mode_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetHybridDesignModeLock
                | o Sub SetHybridDesignModeLock(        iLocked)
                | 
                | Locks or unlocks the "HybridDesignMode" parameter.
                | Role:Locks or unlocks the "HybridDesignMode" parameter if it
                | is possible in the current administrative context. In user
                | mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetHybridDesignModeLock(i_locked)

    def set_knowledge_in_hybrid_design_mode_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetKnowledgeInHybridDesignModeLock
                | o Sub SetKnowledgeInHybridDesignModeLock(        iLocked)
                | 
                | Locks or unlocks the "KnowledgeInHybridDesignMode"
                | parameter. Role:Locks or unlocks the
                | "KnowledgeInHybridDesignMode" parameter if it is possible in
                | the current administrative context. In user mode this method
                | will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetKnowledgeInHybridDesignModeLock(i_locked)

    def set_linked_external_references_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLinkedExternalReferencesLock
                | o Sub SetLinkedExternalReferencesLock(        iLocked)
                | 
                | Locks or unlocks the "LinkedExternalReferences" parameter.
                | Role:Locks or unlocks the "LinkedExternalReferences"
                | parameter if it is possible in the current administrative
                | context. In user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetLinkedExternalReferencesLock(i_locked)

    def set_linked_external_references_only_on_publication_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLinkedExternalReferencesOnlyOnPublicationLock
                | o Sub SetLinkedExternalReferencesOnlyOnPublicationLock(        iLocked)
                | 
                | Locks or unlocks the
                | "LinkedExternalReferencesOnlyOnPublication" parameter.
                | Role:Locks or unlocks the
                | "LinkedExternalReferencesOnlyOnPublication" parameter if it
                | is possible in the current administrative context. In user
                | mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetLinkedExternalReferencesOnlyOnPublicationLock(i_locked)

    def set_linked_external_references_warning_at_creation_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLinkedExternalReferencesWarningAtCreationLock
                | o Sub SetLinkedExternalReferencesWarningAtCreationLock(        iLocked)
                | 
                | Locks or unlocks the
                | "LinkedExternalReferencesWarningAtCreation" parameter.
                | Role:Locks or unlocks the
                | "LinkedExternalReferencesWarningAtCreation" parameter if it
                | is possible in the current administrative context. In user
                | mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetLinkedExternalReferencesWarningAtCreationLock(i_locked)

    def set_naming_mode_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetNamingModeLock
                | o Sub SetNamingModeLock(        iLocked)
                | 
                | Locks or unlocks the "NamingMode" parameter. Role:Locks or
                | unlocks the "NamingMode" parameter if it is possible in the
                | current administrative context. In user mode this method
                | will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetNamingModeLock(i_locked)

    def set_new_with_3d_support_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetNewWith3DSupportLock
                | o Sub SetNewWith3DSupportLock(        iLocked)
                | 
                | Locks or unlocks the "NewWith3DSupport" parameter.
                | Role:Locks or unlocks the "NewWith3DSupport" parameter if it
                | is possible in the current administrative context. In user
                | mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetNewWith3DSupportLock(i_locked)

    def set_new_with_axis_system_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetNewWithAxisSystemLock
                | o Sub SetNewWithAxisSystemLock(        iLocked)
                | 
                | Locks or unlocks the "NewWithAxisSystem" parameter.
                | Role:Locks or unlocks the "NewWithAxisSystem" parameter if
                | it is possible in the current administrative context. In
                | user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetNewWithAxisSystemLock(i_locked)

    def set_new_with_gs_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetNewWithGSLock
                | o Sub SetNewWithGSLock(        iLocked)
                | 
                | Locks or unlocks the "NewWithGS" parameter. Role:Locks or
                | unlocks the "NewWithGS" parameter if it is possible in the
                | current administrative context. In user mode this method
                | will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetNewWithGSLock(i_locked)

    def set_new_with_ogs_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetNewWithOGSLock
                | o Sub SetNewWithOGSLock(        iLocked)
                | 
                | Locks or unlocks the "NewWithOGS" parameter. Role:Locks or
                | unlocks the "NewWithOGS" parameter if it is possible in the
                | current administrative context. In user mode this method
                | will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetNewWithOGSLock(i_locked)

    def set_new_with_panel_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetNewWithPanelLock
                | o Sub SetNewWithPanelLock(        iLocked)
                | 
                | Locks or unlocks the "NewWithPanel" parameter. Role:Locks or
                | unlocks the "NewWithPanel" parameter if it is possible in
                | the current administrative context. In user mode this method
                | will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetNewWithPanelLock(i_locked)

    def set_only_current_operated_solid_set_in_geometry_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetOnlyCurrentOperatedSolidSetInGeometryLock
                | o Sub SetOnlyCurrentOperatedSolidSetInGeometryLock(        iLocked)
                | 
                | Locks or unlocks the "OnlyCurrentOperatedSolidSetInGeometry"
                | parameter. Role:Locks or unlocks the
                | "OnlyCurrentOperatedSolidSetInGeometry" parameter if it is
                | possible in the current administrative context. In user mode
                | this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetOnlyCurrentOperatedSolidSetInGeometryLock(i_locked)

    def set_only_current_solid_set_in_geometry_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetOnlyCurrentSolidSetInGeometryLock
                | o Sub SetOnlyCurrentSolidSetInGeometryLock(        iLocked)
                | 
                | Locks or unlocks the "OnlyCurrentSolidSetInGeometry"
                | parameter. Role:Locks or unlocks the
                | "OnlyCurrentSolidSetInGeometry" parameter if it is possible
                | in the current administrative context. In user mode this
                | method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetOnlyCurrentSolidSetInGeometryLock(i_locked)

    def set_parameters_node_in_tree_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetParametersNodeInTreeLock
                | o Sub SetParametersNodeInTreeLock(        iLocked)
                | 
                | Locks or unlocks the "ParametersNodeInTree" parameter.
                | Role:Locks or unlocks the "ParametersNodeInTree" parameter
                | if it is possible in the current administrative context. In
                | user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetParametersNodeInTreeLock(i_locked)

    def set_publish_topological_elements_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPublishTopologicalElementsLock
                | o Sub SetPublishTopologicalElementsLock(        iLocked)
                | 
                | Locks or unlocks the "PublishTopologicalElements" parameter.
                | Role:Locks or unlocks the "PublishTopologicalElements"
                | parameter if it is possible in the current administrative
                | context. In user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetPublishTopologicalElementsLock(i_locked)

    def set_relations_node_in_tree_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetRelationsNodeInTreeLock
                | o Sub SetRelationsNodeInTreeLock(        iLocked)
                | 
                | Locks or unlocks the "RelationsNodeInTree" parameter.
                | Role:Locks or unlocks the "RelationsNodeInTree" parameter if
                | it is possible in the current administrative context. In
                | user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param i_locked:
        :return:
        """
        return self.part_infrastructure_setting_att.SetRelationsNodeInTreeLock(i_locked)

    def set_replace_only_after_current_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetReplaceOnlyAfterCurrentLock
                | o Sub SetReplaceOnlyAfterCurrentLock(        iLocked)
                | 
                | Locks or unlocks the "ReplaceOnlyAfterCurrent" parameter.
                | Role:Locks or unlocks the "ReplaceOnlyAfterCurrent"
                | parameter if it is possible in the current administrative
                | context. In user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetReplaceOnlyAfterCurrentLock(i_locked)

    def set_surface_elements_location_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSurfaceElementsLocationLock
                | o Sub SetSurfaceElementsLocationLock(        iLocked)
                | 
                | Locks or unlocks the "SurfaceElementsLocation" parameter.
                | Role:Locks or unlocks the "SurfaceElementsLocation"
                | parameter if it is possible in the current administrative
                | context. In user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetSurfaceElementsLocationLock(i_locked)

    def set_update_elements_refreshed_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetUpdateElementsRefreshedLock
                | o Sub SetUpdateElementsRefreshedLock(        iLocked)
                | 
                | Locks or unlocks the "UpdateElementsRefreshed" parameter.
                | Role:Locks or unlocks the "UpdateElementsRefreshed"
                | parameter if it is possible in the current administrative
                | context. In user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetUpdateElementsRefreshedLock(i_locked)

    def set_update_linked_external_references_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetUpdateLinkedExternalReferencesLock
                | o Sub SetUpdateLinkedExternalReferencesLock(        iLocked)
                | 
                | Locks or unlocks the "UpdateLinkedExternalReferences"
                | parameter. Role:Locks or unlocks the
                | "UpdateLinkedExternalReferences" parameter if it is possible
                | in the current administrative context. In user mode this
                | method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetUpdateLinkedExternalReferencesLock(i_locked)

    def set_update_mode_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetUpdateModeLock
                | o Sub SetUpdateModeLock(        iLocked)
                | 
                | Locks or unlocks the "UpdateMode" parameter. Role:Locks or
                | unlocks the "UpdateMode" parameter if it is possible in the
                | current administrative context. In user mode this method
                | will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param bool i_locked:
        """
        self.part_infrastructure_setting_att.SetUpdateModeLock(i_locked)

    def set_update_stopped_on_error_lock(self, i_locked):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetUpdateStoppedOnErrorLock
                | o Sub SetUpdateStoppedOnErrorLock(        iLocked)
                | 
                | Locks or unlocks the "UpdateStoppedOnError" parameter.
                | Role:Locks or unlocks the "UpdateStoppedOnError" parameter
                | if it is possible in the current administrative context. In
                | user mode this method will always return E_FAIL.
                |
                | Parameters:
                | iLocked
                | 	the locking operation to be performed
                | 	Legal values:
                | 	TRUE :   to lock the parameter.
                |  	FALSE:   to unlock the parameter.

        :param i_locked:
        """
        self.part_infrastructure_setting_att.SetUpdateStoppedOnErrorLock(i_locked)

    def __repr__(self):
        return f'PartInfrastructureSettingAtt()'
