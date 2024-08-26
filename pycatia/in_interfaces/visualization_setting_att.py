#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.system_interfaces.setting_controller import SettingController


class VisualizationSettingAtt(SettingController):
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
                |                         VisualizationSettingAtt
                | 
                | The interface to access a CATIAVisualizationSettingAtt.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.visualization_setting_att = com_object

    @property
    def accurate_picking_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AccuratePickingMode() As boolean
                | 
                |     Returns the AccuratePickingMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.AccuratePickingMode

    @accurate_picking_mode.setter
    def accurate_picking_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.AccuratePickingMode = value

    @property
    def accurate_picking_window_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AccuratePickingWindowSize() As long
                | 
                |     Returns the AccuratePickingWindowSize parameter.

        :rtype: int
        """

        return self.visualization_setting_att.AccuratePickingWindowSize

    @accurate_picking_window_size.setter
    def accurate_picking_window_size(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.AccuratePickingWindowSize = value

    @property
    def all_z_buffer_element_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AllZBufferElementMode() As boolean
                | 
                |     Returns the AllZBufferElementMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.AllZBufferElementMode

    @all_z_buffer_element_mode.setter
    def all_z_buffer_element_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.AllZBufferElementMode = value

    @property
    def ambient_activation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AmbientActivation() As long
                | 
                |     Returns the AmbientActivation parameter.

        :rtype: int
        """

        return self.visualization_setting_att.AmbientActivation

    @ambient_activation.setter
    def ambient_activation(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.AmbientActivation = value

    @property
    def anti_aliasing_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AntiAliasingMode() As boolean
                | 
                |     Returns the AntiAliasingMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.AntiAliasingMode

    @anti_aliasing_mode.setter
    def anti_aliasing_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.AntiAliasingMode = value

    @property
    def anti_aliasing_offset(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AntiAliasingOffset() As double
                | 
                |     Returns the AntiAliasingOffset parameter.

        :rtype: float
        """

        return self.visualization_setting_att.AntiAliasingOffset

    @anti_aliasing_offset.setter
    def anti_aliasing_offset(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.AntiAliasingOffset = value

    @property
    def auxiliary_drill_viewer(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AuxiliaryDrillViewer() As boolean
                | 
                |     Returns the AuxiliaryDrillViewer parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.AuxiliaryDrillViewer

    @auxiliary_drill_viewer.setter
    def auxiliary_drill_viewer(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.AuxiliaryDrillViewer = value

    @property
    def back_face_culling_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BackFaceCullingMode() As boolean
                | 
                |     Deprecated:
                |         V5R16. Returns the BackFaceCullingMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.BackFaceCullingMode

    @back_face_culling_mode.setter
    def back_face_culling_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.BackFaceCullingMode = value

    @property
    def border_edges_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BorderEdgesMode() As boolean
                | 
                |     Returns the BorderEdgesMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.BorderEdgesMode

    @border_edges_mode.setter
    def border_edges_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.BorderEdgesMode = value

    @property
    def border_edges_thickness(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BorderEdgesThickness() As long
                | 
                |     Returns the BorderEdgesThickness parameter.

        :rtype: int
        """

        return self.visualization_setting_att.BorderEdgesThickness

    @border_edges_thickness.setter
    def border_edges_thickness(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.BorderEdgesThickness = value

    @property
    def bounding_box_selection_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property BoundingBoxSelectionMode() As boolean
                | 
                |     Returns the BoundingBoxSelectionMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.BoundingBoxSelectionMode

    @bounding_box_selection_mode.setter
    def bounding_box_selection_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.BoundingBoxSelectionMode = value

    @property
    def color_background_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ColorBackgroundMode() As boolean
                | 
                |     Returns the ColorBackgroundMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.ColorBackgroundMode

    @color_background_mode.setter
    def color_background_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.ColorBackgroundMode = value

    @property
    def default_diffuse_ambient_coefficient(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DefaultDiffuseAmbientCoefficient() As double
                | 
                |     Returns the AmbientActivation parameter.

        :rtype: float
        """

        return self.visualization_setting_att.DefaultDiffuseAmbientCoefficient

    @default_diffuse_ambient_coefficient.setter
    def default_diffuse_ambient_coefficient(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.DefaultDiffuseAmbientCoefficient = value

    @property
    def default_shininess(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DefaultShininess() As double
                | 
                |     Returns the AmbientActivation parameter.

        :rtype: float
        """

        return self.visualization_setting_att.DefaultShininess

    @default_shininess.setter
    def default_shininess(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.DefaultShininess = value

    @property
    def default_specular_coefficient(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DefaultSpecularCoefficient() As double
                | 
                |     Returns the AmbientActivation parameter.

        :rtype: float
        """

        return self.visualization_setting_att.DefaultSpecularCoefficient

    @default_specular_coefficient.setter
    def default_specular_coefficient(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.DefaultSpecularCoefficient = value

    @property
    def display_current_scale(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DisplayCurrentScale() As boolean
                | 
                |     Returns the SetStereoModeLock parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.DisplayCurrentScale

    @display_current_scale.setter
    def display_current_scale(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.DisplayCurrentScale = value

    @property
    def display_drill_list(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DisplayDrillList() As boolean
                | 
                |     Returns the DisplayDrillList parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.DisplayDrillList

    @display_drill_list.setter
    def display_drill_list(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.DisplayDrillList = value

    @property
    def display_immersive_drill_viewer(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DisplayImmersiveDrillViewer() As boolean
                | 
                |     Returns the DisplayImmersiveDrillViewer parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.DisplayImmersiveDrillViewer

    @display_immersive_drill_viewer.setter
    def display_immersive_drill_viewer(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.DisplayImmersiveDrillViewer = value

    @property
    def dynamic_cull(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DynamicCull() As long
                | 
                |     Returns the DynamicCull parameter.

        :rtype: int
        """

        return self.visualization_setting_att.DynamicCull

    @dynamic_cull.setter
    def dynamic_cull(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.DynamicCull = value

    @property
    def dynamic_lod(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DynamicLOD() As double
                | 
                |     Returns the DynamicLOD parameter.

        :rtype: float
        """

        return self.visualization_setting_att.DynamicLOD

    @dynamic_lod.setter
    def dynamic_lod(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.DynamicLOD = value

    @property
    def face_hl_drill(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FaceHLDrill() As boolean
                | 
                |     Returns the FaceHLDrill parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.FaceHLDrill

    @face_hl_drill.setter
    def face_hl_drill(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.FaceHLDrill = value

    @property
    def fly_collision_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FlyCollisionMode() As boolean
                | 
                |     Returns the FlyCollisionMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.FlyCollisionMode

    @fly_collision_mode.setter
    def fly_collision_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.FlyCollisionMode = value

    @property
    def fly_collision_sphere_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FlyCollisionSphereRadius() As double
                | 
                |     Returns the FlyCollisionSphereRadius parameter.

        :rtype: float
        """

        return self.visualization_setting_att.FlyCollisionSphereRadius

    @fly_collision_sphere_radius.setter
    def fly_collision_sphere_radius(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.FlyCollisionSphereRadius = value

    @property
    def fly_collision_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FlyCollisionType() As long
                | 
                |     Returns the FlyCollisionType parameter.

        :rtype: int
        """

        return self.visualization_setting_att.FlyCollisionType

    @fly_collision_type.setter
    def fly_collision_type(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.FlyCollisionType = value

    @property
    def fly_sensitivity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FlySensitivity() As long
                | 
                |     Returns the FlySensitivity parameter.

        :rtype: int
        """

        return self.visualization_setting_att.FlySensitivity

    @fly_sensitivity.setter
    def fly_sensitivity(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.FlySensitivity = value

    @property
    def fly_speed(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FlySpeed() As long
                | 
                |     Returns the FlySpeed parameter.

        :rtype: int
        """

        return self.visualization_setting_att.FlySpeed

    @fly_speed.setter
    def fly_speed(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.FlySpeed = value

    @property
    def fly_speed_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FlySpeedMode() As long
                | 
                |     Returns the FlySpeedMode parameter.

        :rtype: int
        """

        return self.visualization_setting_att.FlySpeedMode

    @fly_speed_mode.setter
    def fly_speed_mode(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.FlySpeedMode = value

    @property
    def follow_ground_altitude(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FollowGroundAltitude() As double
                | 
                |     Returns the FollowGroundAltitude parameter.

        :rtype: float
        """

        return self.visualization_setting_att.FollowGroundAltitude

    @follow_ground_altitude.setter
    def follow_ground_altitude(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.FollowGroundAltitude = value

    @property
    def follow_ground_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FollowGroundMode() As boolean
                | 
                |     Returns the FollowGroundMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.FollowGroundMode

    @follow_ground_mode.setter
    def follow_ground_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.FollowGroundMode = value

    @property
    def full_scene_anti_aliasing_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FullSceneAntiAliasingMode() As
                | CATFullSceneAntiAliasingMode
                | 
                |     Returns the AntiAliasingMode parameter.

        :return: enum cat_full_scene_anti_aliasing_mode
        :rtype: int
        """

        return self.visualization_setting_att.FullSceneAntiAliasingMode

    @full_scene_anti_aliasing_mode.setter
    def full_scene_anti_aliasing_mode(self, value: int):
        """
        :param int value: enum cat_full_scene_anti_aliasing_mode
        """

        self.visualization_setting_att.FullSceneAntiAliasingMode = value

    @property
    def gravity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Gravity() As boolean
                | 
                |     Returns the Gravity parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.Gravity

    @gravity.setter
    def gravity(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.Gravity = value

    @property
    def gravity_axis(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property GravityAxis() As long
                | 
                |     Returns the GravityAxis parameter.

        :rtype: int
        """

        return self.visualization_setting_att.GravityAxis

    @gravity_axis.setter
    def gravity_axis(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.GravityAxis = value

    @property
    def halo_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property HaloMode() As boolean
                | 
                |     Returns the HaloMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.HaloMode

    @halo_mode.setter
    def halo_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.HaloMode = value

    @property
    def isopar_generation_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property IsoparGenerationMode() As boolean
                | 
                |     Returns the IsoparGenerationMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.IsoparGenerationMode

    @isopar_generation_mode.setter
    def isopar_generation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.IsoparGenerationMode = value

    @property
    def keyboard_rotation_angle_value(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property KeyboardRotationAngleValue() As long
                | 
                |     Retrieves the angle value for rotations operated through key combinations.

        :rtype: int
        """

        return self.visualization_setting_att.KeyboardRotationAngleValue

    @keyboard_rotation_angle_value.setter
    def keyboard_rotation_angle_value(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.KeyboardRotationAngleValue = value

    @property
    def light_viewer_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LightViewerMode() As boolean
                | 
                |     Returns the LightViewerMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.LightViewerMode

    @light_viewer_mode.setter
    def light_viewer_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.LightViewerMode = value

    @property
    def lineic_cgr_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LineicCgrMode() As boolean
                | 
                |     Returns the LineicCgrMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.LineicCgrMode

    @lineic_cgr_mode.setter
    def lineic_cgr_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.LineicCgrMode = value

    @property
    def max_selection_move(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MaxSelectionMove() As long
                | 
                |     Returns the MaxSelectionMove parameter.

        :rtype: int
        """

        return self.visualization_setting_att.MaxSelectionMove

    @max_selection_move.setter
    def max_selection_move(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.MaxSelectionMove = value

    @property
    def minimum_fps_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MinimumFPSMode() As boolean
                | 
                |     Returns the MinimumFPSMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.MinimumFPSMode

    @minimum_fps_mode.setter
    def minimum_fps_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.MinimumFPSMode = value

    @property
    def minimum_space_fps_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MinimumSpaceFPSMode() As boolean
                | 
                |     Returns the MinimumSpaceFPSMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.MinimumSpaceFPSMode

    @minimum_space_fps_mode.setter
    def minimum_space_fps_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.MinimumSpaceFPSMode = value

    @property
    def mouse_double_clic_delay(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MouseDoubleClicDelay() As long
                | 
                |     Returns the MouseDoubleClicDelay parameter.

        :rtype: int
        """

        return self.visualization_setting_att.MouseDoubleClicDelay

    @mouse_double_clic_delay.setter
    def mouse_double_clic_delay(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.MouseDoubleClicDelay = value

    @property
    def mouse_speed_value(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MouseSpeedValue() As long
                | 
                |     Returns the MouseSpeedValue parameter.

        :rtype: int
        """

        return self.visualization_setting_att.MouseSpeedValue

    @mouse_speed_value.setter
    def mouse_speed_value(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.MouseSpeedValue = value

    @property
    def nb_isopars(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NbIsopars() As long
                | 
                |     Returns the NbIsopars parameter.

        :rtype: int
        """

        return self.visualization_setting_att.NbIsopars

    @nb_isopars.setter
    def nb_isopars(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.NbIsopars = value

    @property
    def no_z_buffer_selection_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NoZBufferSelectionMode() As boolean
                | 
                |     Returns the NoZBufferSelectionMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.NoZBufferSelectionMode

    @no_z_buffer_selection_mode.setter
    def no_z_buffer_selection_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.NoZBufferSelectionMode = value

    @property
    def number_of_minimum_fps(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NumberOfMinimumFPS() As long
                | 
                |     Returns the NumberOfMinimumFPS parameter.

        :rtype: int
        """

        return self.visualization_setting_att.NumberOfMinimumFPS

    @number_of_minimum_fps.setter
    def number_of_minimum_fps(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.NumberOfMinimumFPS = value

    @property
    def number_of_minimum_space_fps(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NumberOfMinimumSpaceFPS() As long
                | 
                |     Returns the NumberOfMinimumSpaceFPS parameter.

        :rtype: int
        """

        return self.visualization_setting_att.NumberOfMinimumSpaceFPS

    @number_of_minimum_space_fps.setter
    def number_of_minimum_space_fps(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.NumberOfMinimumSpaceFPS = value

    @property
    def occlusion_culling_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OcclusionCullingMode() As boolean
                | 
                |     Returns the OcclusionCullingMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.OcclusionCullingMode

    @occlusion_culling_mode.setter
    def occlusion_culling_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.OcclusionCullingMode = value

    @property
    def opaque_faces(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OpaqueFaces() As boolean
                | 
                |     Returns the SetStereoModeLock parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.OpaqueFaces

    @opaque_faces.setter
    def opaque_faces(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.OpaqueFaces = value

    @property
    def other_selection_timeout(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OtherSelectionTimeout() As double
                | 
                |     Returns the OtherSelectionTimeout parameter.

        :rtype: float
        """

        return self.visualization_setting_att.OtherSelectionTimeout

    @other_selection_timeout.setter
    def other_selection_timeout(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.OtherSelectionTimeout = value

    @property
    def other_selection_timeout_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OtherSelectionTimeoutActivity() As boolean
                | 
                |     Returns the OtherSelectionTimeoutActivity parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.OtherSelectionTimeoutActivity

    @other_selection_timeout_activity.setter
    def other_selection_timeout_activity(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.OtherSelectionTimeoutActivity = value

    @property
    def picking_window_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PickingWindowSize() As long
                | 
                |     Returns the PickingWindowSize parameter.

        :rtype: int
        """

        return self.visualization_setting_att.PickingWindowSize

    @picking_window_size.setter
    def picking_window_size(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.PickingWindowSize = value

    @property
    def pre_sel_navigator_started_by_arrow_keys(self) -> bool:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property PreSelNavigatorStartedByArrowKeys() As boolean
                |     Returns the PreSelNavigatorStartedByArrowKeys parameter.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.visualization_setting_att.PreSelNavigatorStartedByArrowKeys

    @pre_sel_navigator_started_by_arrow_keys.setter
    def pre_sel_navigator_started_by_arrow_keys(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.PreSelNavigatorStartedByArrowKeys = value

    @property
    def pre_selection_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PreSelectionMode() As boolean
                | 
                |     Returns the PreSelectionMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.PreSelectionMode

    @pre_selection_mode.setter
    def pre_selection_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.PreSelectionMode = value

    @property
    def preselected_element_linetype(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PreselectedElementLinetype() As long
                | 
                |     Returns the PreselectedElementLinetype parameter.

        :rtype: int
        """

        return self.visualization_setting_att.PreselectedElementLinetype

    @preselected_element_linetype.setter
    def preselected_element_linetype(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.PreselectedElementLinetype = value

    @property
    def rotation_sphere_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RotationSphereMode() As boolean
                | 
                |     Returns the RotationSphereMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.RotationSphereMode

    @rotation_sphere_mode.setter
    def rotation_sphere_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.RotationSphereMode = value

    @property
    def shader_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ShaderMode() As boolean
                | 
                |     Returns the ShaderMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.ShaderMode

    @shader_mode.setter
    def shader_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.ShaderMode = value

    @property
    def static_cull(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StaticCull() As long
                | 
                |     Returns the StaticCull parameter.

        :rtype: int
        """

        return self.visualization_setting_att.StaticCull

    @static_cull.setter
    def static_cull(self, value: int):
        """
        :param int value:
        """

        self.visualization_setting_att.StaticCull = value

    @property
    def static_lod(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StaticLOD() As double
                | 
                |     Returns the StaticLOD parameter.

        :rtype: float
        """

        return self.visualization_setting_att.StaticLOD

    @static_lod.setter
    def static_lod(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.StaticLOD = value

    @property
    def stereo_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StereoMode() As boolean
                | 
                |     Returns the StereoMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.StereoMode

    @stereo_mode.setter
    def stereo_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.StereoMode = value

    @property
    def transparency_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TransparencyMode() As boolean
                | 
                |     Returns the TransparencyMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.TransparencyMode

    @transparency_mode.setter
    def transparency_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.TransparencyMode = value

    @property
    def two_side_lighting_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TwoSideLightingMode() As boolean
                | 
                |     Returns the TwoSideLightingMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.TwoSideLightingMode

    @two_side_lighting_mode.setter
    def two_side_lighting_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.TwoSideLightingMode = value

    @property
    def viewpoint_animation_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ViewpointAnimationMode() As boolean
                | 
                |     Returns the ViewpointAnimationMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.ViewpointAnimationMode

    @viewpoint_animation_mode.setter
    def viewpoint_animation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.ViewpointAnimationMode = value

    @property
    def viz2_d_accuracy_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Viz2DAccuracyMode() As boolean
                | 
                |     Returns the 2DAccuracyMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.Viz2DAccuracyMode

    @viz2_d_accuracy_mode.setter
    def viz2_d_accuracy_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.Viz2DAccuracyMode = value

    @property
    def viz2_d_fixed_accuracy(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Viz2DFixedAccuracy() As double
                | 
                |     Returns the 2DFixedAccuracy parameter.

        :rtype: float
        """

        return self.visualization_setting_att.Viz2DFixedAccuracy

    @viz2_d_fixed_accuracy.setter
    def viz2_d_fixed_accuracy(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.Viz2DFixedAccuracy = value

    @property
    def viz2_d_proportionnal_accuracy(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Viz2DProportionnalAccuracy() As double
                | 
                |     Returns the 2DProportionnalAccuracy parameter.

        :rtype: float
        """

        return self.visualization_setting_att.Viz2DProportionnalAccuracy

    @viz2_d_proportionnal_accuracy.setter
    def viz2_d_proportionnal_accuracy(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.Viz2DProportionnalAccuracy = value

    @property
    def viz3_d_accuracy_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Viz3DAccuracyMode() As boolean
                | 
                |     Returns the Viz3DAccuracyMode parameter.

        :rtype: bool
        """

        return self.visualization_setting_att.Viz3DAccuracyMode

    @viz3_d_accuracy_mode.setter
    def viz3_d_accuracy_mode(self, value: bool):
        """
        :param bool value:
        """

        self.visualization_setting_att.Viz3DAccuracyMode = value

    @property
    def viz3_d_curve_accuracy(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Viz3DCurveAccuracy() As double
                | 
                |     Returns the 3DCurveAccuracy parameter.

        :rtype: float
        """

        return self.visualization_setting_att.Viz3DCurveAccuracy

    @viz3_d_curve_accuracy.setter
    def viz3_d_curve_accuracy(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.Viz3DCurveAccuracy = value

    @property
    def viz3_d_fixed_accuracy(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Viz3DFixedAccuracy() As double
                | 
                |     Returns the 3DFixedAccuracy parameter.

        :rtype: float
        """

        return self.visualization_setting_att.Viz3DFixedAccuracy

    @viz3_d_fixed_accuracy.setter
    def viz3_d_fixed_accuracy(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.Viz3DFixedAccuracy = value

    @property
    def viz3_d_proportionnal_accuracy(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Viz3DProportionnalAccuracy() As double
                | 
                |     Returns the Viz3DProportionnalAccuracy parameter.

        :rtype: float
        """

        return self.visualization_setting_att.Viz3DProportionnalAccuracy

    @viz3_d_proportionnal_accuracy.setter
    def viz3_d_proportionnal_accuracy(self, value: float):
        """
        :param float value:
        """

        self.visualization_setting_att.Viz3DProportionnalAccuracy = value

    def get_accurate_picking_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAccuratePickingModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the AccuratePickingMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetAccuratePickingModeInfo(io_admin_level, io_locked)

    def get_accurate_picking_window_size_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAccuratePickingWindowSizeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the AccuratePickingWindowSize setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetAccuratePickingWindowSizeInfo(io_admin_level, io_locked)

    def get_all_z_buffer_element_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAllZBufferElementModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the AllZBufferElementMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetAllZBufferElementModeInfo(io_admin_level, io_locked)

    def get_ambient_activation_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAmbientActivationInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the AmbientActivation setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetAmbientActivationInfo(io_admin_level, io_locked)

    def get_anti_aliasing_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAntiAliasingModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the AntiAliasingMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetAntiAliasingModeInfo(io_admin_level, io_locked)

    def get_anti_aliasing_offset_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAntiAliasingOffsetInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the AntiAliasingOffset setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetAntiAliasingOffsetInfo(io_admin_level, io_locked)

    def get_auxiliary_drill_viewer_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAuxiliaryDrillViewerInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the AuxiliaryDrillViewer setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetAuxiliaryDrillViewerInfo(io_admin_level, io_locked)

    def get_back_face_culling_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBackFaceCullingMode() As CATBackFaceCullingMode
                | 
                |     Retrieves the BackFaceCullingMode parameter.
                | 
                |     Parameters:
                | 
                |         oBackFaceCullingMode
                |             Value of the back face culling mode setting option. The retrieved
                |             value can be one of the four possible values defined by the
                |             
                | 
                |         CATBackFaceCullingMode enumeration. 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             if the operation succeeded. 
                |         E_FAIL
                |             if the operation failed.

        :return: enum cat_back_face_culling_mode
        :rtype: int
        """
        return self.visualization_setting_att.GetBackFaceCullingMode()

    def get_back_face_culling_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBackFaceCullingModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the BackFaceCullingMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetBackFaceCullingModeInfo(io_admin_level, io_locked)

    def get_background_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetBackgroundRGB(long ioR,
                | long ioG,
                | long ioB)
                | 
                |     Returns the BackgroundRGB parameter.

        :param int io_r:
        :param int io_g:
        :param int io_b:
        :rtype: None
        """
        return self.visualization_setting_att.GetBackgroundRGB(io_r, io_g, io_b)

    def get_background_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBackgroundRGBInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the BackgroundRGB setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetBackgroundRGBInfo(io_admin_level, io_locked)

    def get_border_edges_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBorderEdgesModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the BorderEdgesMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetBorderEdgesModeInfo(io_admin_level, io_locked)

    def get_border_edges_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetBorderEdgesRGB(long ioR,
                | long ioG,
                | long ioB)
                | 
                |     Returns the BorderEdgesRGB parameter.

        :param int io_r:
        :param int io_g:
        :param int io_b:
        :rtype: None
        """
        return self.visualization_setting_att.GetBorderEdgesRGB(io_r, io_g, io_b)

    def get_border_edges_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBorderEdgesRGBInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the BorderEdgesRGB setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetBorderEdgesRGBInfo(io_admin_level, io_locked)

    def get_border_edges_thickness_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBorderEdgesThicknessInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the BorderEdgesThickness setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetBorderEdgesThicknessInfo(io_admin_level, io_locked)

    def get_bounding_box_selection_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBoundingBoxSelectionModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the BoundingBoxSelectionMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetBoundingBoxSelectionModeInfo(io_admin_level, io_locked)

    def get_color_background_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetColorBackgroundModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ColorBackgroundMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetColorBackgroundModeInfo(io_admin_level, io_locked)

    def get_default_diffuse_ambient_coefficient_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDefaultDiffuseAmbientCoefficientInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the DefaultDiffuseAmbientCoefficient setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetDefaultDiffuseAmbientCoefficientInfo(io_admin_level, io_locked)

    def get_default_shininess_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDefaultShininessInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the DefaultShininess setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetDefaultShininessInfo(io_admin_level, io_locked)

    def get_default_specular_coefficient_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDefaultSpecularCoefficientInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the DefaultSpecularCoefficient setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetDefaultSpecularCoefficientInfo(io_admin_level, io_locked)

    def get_display_current_scale_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDisplayCurrentScaleInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SetStereoModeLock setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetDisplayCurrentScaleInfo(io_admin_level, io_locked)

    def get_display_drill_list_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDisplayDrillListInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the DisplayDrillList setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetDisplayDrillListInfo(io_admin_level, io_locked)

    def get_display_immersive_drill_viewer_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDisplayImmersiveDrillViewerInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the DisplayImmersiveDrillViewer setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetDisplayImmersiveDrillViewerInfo(io_admin_level, io_locked)

    def get_dynamic_cull_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDynamicCullInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the DynamicCull setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetDynamicCullInfo(io_admin_level, io_locked)

    def get_dynamic_lod_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetDynamicLODInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the DynamicLOD setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetDynamicLODInfo(io_admin_level, io_locked)

    def get_face_hl_drill_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetFaceHLDrillInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the FaceHLDrill setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetFaceHLDrillInfo(io_admin_level, io_locked)

    def get_fly_collision_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetFlyCollisionModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the FlyCollisionMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetFlyCollisionModeInfo(io_admin_level, io_locked)

    def get_fly_collision_sphere_radius_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetFlyCollisionSphereRadiusInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the FlyCollisionSphereRadius setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetFlyCollisionSphereRadiusInfo(io_admin_level, io_locked)

    def get_fly_collision_type_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetFlyCollisionTypeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the FlyCollisionType setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetFlyCollisionTypeInfo(io_admin_level, io_locked)

    def get_fly_sensitivity_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetFlySensitivityInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the FlySensitivity setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetFlySensitivityInfo(io_admin_level, io_locked)

    def get_fly_speed_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetFlySpeedInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the FlySpeed setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetFlySpeedInfo(io_admin_level, io_locked)

    def get_fly_speed_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetFlySpeedModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the FlySpeedMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetFlySpeedModeInfo(io_admin_level, io_locked)

    def get_follow_ground_altitude_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetFollowGroundAltitudeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the FollowGroundAltitude setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetFollowGroundAltitudeInfo(io_admin_level, io_locked)

    def get_follow_ground_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetFollowGroundModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the FollowGroundMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetFollowGroundModeInfo(io_admin_level, io_locked)

    def get_full_scene_anti_aliasing_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetFullSceneAntiAliasingModeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the AntiAliasingMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetFullSceneAntiAliasingModeInfo(io_admin_level, io_locked)

    def get_gravity_axis_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetGravityAxisInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the GravityAxis setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetGravityAxisInfo(io_admin_level, io_locked)

    def get_gravity_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetGravityInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Gravity setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetGravityInfo(io_admin_level, io_locked)

    def get_halo_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetHaloModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the HaloMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetHaloModeInfo(io_admin_level, io_locked)

    def get_handles_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetHandlesRGB(long ioR,
                | long ioG,
                | long ioB)
                | 
                |     Returns the HandlesRGB parameter.

        :param int io_r:
        :param int io_g:
        :param int io_b:
        :rtype: None
        """
        return self.visualization_setting_att.GetHandlesRGB(io_r, io_g, io_b)

    def get_handles_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetHandlesRGBInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the HandlesRGB setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetHandlesRGBInfo(io_admin_level, io_locked)

    def get_isopar_generation_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetIsoparGenerationModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the IsoparGenerationMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetIsoparGenerationModeInfo(io_admin_level, io_locked)

    def get_keyboard_rotation_angle_value_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetKeyboardRotationAngleValueInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the KeyboardRotationAngleValue setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetKeyboardRotationAngleValueInfo(io_admin_level, io_locked)

    def get_light_viewer_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLightViewerModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the LightViewerMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetLightViewerModeInfo(io_admin_level, io_locked)

    def get_lineic_cgr_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLineicCgrModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the LineicCgrMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetLineicCgrModeInfo(io_admin_level, io_locked)

    def get_max_selection_move_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMaxSelectionMoveInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the MaxSelectionMove setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetMaxSelectionMoveInfo(io_admin_level, io_locked)

    def get_minimum_fps_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMinimumFPSModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the MinimumFPSMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetMinimumFPSModeInfo(io_admin_level, io_locked)

    def get_minimum_space_fps_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMinimumSpaceFPSModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the MinimumSpaceFPSMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetMinimumSpaceFPSModeInfo(io_admin_level, io_locked)

    def get_mouse_double_clic_delay_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMouseDoubleClicDelayInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the MouseDoubleClicDelay setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetMouseDoubleClicDelayInfo(io_admin_level, io_locked)

    def get_mouse_speed_value_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetMouseSpeedValueInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the MouseSpeedValue setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetMouseSpeedValueInfo(io_admin_level, io_locked)

    def get_nb_isopars_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNbIsoparsInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the NbIsopars setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetNbIsoparsInfo(io_admin_level, io_locked)

    def get_no_show_background_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetNoShowBackgroundRGB(long ioR,
                | long ioG,
                | long ioB)
                | 
                |     Retrieves the No Show Background Color setting attribute
                |     value.
                |     Role: The No Show Background Color setting attribute manages the
                |     backgraound color of no show space
                | 
                |     Parameters:
                | 
                |         ioR,
                |             ioG, ioB [inout] The Red, Green, Blue components of the No Show
                |             Background Color setting attribute value 
                | 
                |     Returns:
                |         S_OK if the No Show Background Color setting attribute value is
                |         successfully retrieved, and E_FAIL otherwise

        :param int io_r:
        :param int io_g:
        :param int io_b:
        :rtype: None
        """
        return self.visualization_setting_att.GetNoShowBackgroundRGB(io_r, io_g, io_b)

    def get_no_show_background_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNoShowBackgroundRGBInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves the No Show Background Color setting attribute
                |     information.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel,
                |             ioLocked [inout] and oModified [out] The No Show Background Color
                |             setting attribute information 
                | 
                |     Returns:
                |         S_OK if the No Show Background Color setting attribute information is
                |         successfully retrieved, and E_FAIL otherwise
                |         Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetNoShowBackgroundRGBInfo(io_admin_level, io_locked)

    def get_no_z_buffer_selection_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNoZBufferSelectionModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the NoZBufferSelectionMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetNoZBufferSelectionModeInfo(io_admin_level, io_locked)

    def get_number_of_minimum_fps_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNumberOfMinimumFPSInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the NumberOfMinimumFPS setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetNumberOfMinimumFPSInfo(io_admin_level, io_locked)

    def get_number_of_minimum_space_fps_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetNumberOfMinimumSpaceFPSInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the NumberOfMinimumSpaceFPS setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetNumberOfMinimumSpaceFPSInfo(io_admin_level, io_locked)

    def get_occlusion_culling_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetOcclusionCullingModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OcclusionCullingMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetOcclusionCullingModeInfo(io_admin_level, io_locked)

    def get_opaque_faces_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetOpaqueFacesInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SetStereoModeLock setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetOpaqueFacesInfo(io_admin_level, io_locked)

    def get_other_selection_timeout_activity_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetOtherSelectionTimeoutActivityInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OtherSelectionTimeoutActivity setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetOtherSelectionTimeoutActivityInfo(io_admin_level, io_locked)

    def get_other_selection_timeout_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetOtherSelectionTimeoutInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the OtherSelectionTimeout setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetOtherSelectionTimeoutInfo(io_admin_level, io_locked)

    def get_picking_window_size_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPickingWindowSizeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the PickingWindowSize setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetPickingWindowSizeInfo(io_admin_level, io_locked)

    def get_pre_sel_navigator_started_by_arrow_keys_info(self, io_admin_level: str, io_locked: str) -> bool:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func GetPreSelNavigatorStartedByArrowKeysInfo(CATBSTR ioAdminLevel,CATBSTR
                | ioLocked) As boolean
                |     Retrieves information about the PreSelNavigatorStartedByArrowKeys setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.visualization_setting_att.GetPreSelNavigatorStartedByArrowKeysInfo(io_admin_level, io_locked)

    def get_pre_selection_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPreSelectionModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the PreSelectionMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetPreSelectionModeInfo(io_admin_level, io_locked)

    def get_preselected_element_linetype_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPreselectedElementLinetypeInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the PreselectedElementLinetype setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetPreselectedElementLinetypeInfo(io_admin_level, io_locked)

    def get_preselected_element_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetPreselectedElementRGB(long ioR,
                | long ioG,
                | long ioB)
                | 
                |     Returns the PreselectedElementRGB parameter.

        :param int io_r:
        :param int io_g:
        :param int io_b:
        :rtype: None
        """
        return self.visualization_setting_att.GetPreselectedElementRGB(io_r, io_g, io_b)

    def get_preselected_element_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPreselectedElementRGBInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the PreselectedElementRGB setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetPreselectedElementRGBInfo(io_admin_level, io_locked)

    def get_rotation_sphere_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetRotationSphereModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the RotationSphereMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetRotationSphereModeInfo(io_admin_level, io_locked)

    def get_selected_edge_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSelectedEdgeRGB(long ioR,
                | long ioG,
                | long ioB)
                | 
                |     Returns the SelectedEdgeRGB parameter.

        :param int io_r:
        :param int io_g:
        :param int io_b:
        :rtype: None
        """
        return self.visualization_setting_att.GetSelectedEdgeRGB(io_r, io_g, io_b)

    def get_selected_edge_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetSelectedEdgeRGBInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SelectedEdgeRGB setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetSelectedEdgeRGBInfo(io_admin_level, io_locked)

    def get_selected_element_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSelectedElementRGB(long ioR,
                | long ioG,
                | long ioB)
                | 
                |     Returns the SelectedElementRGB parameter.

        :param int io_r:
        :param int io_g:
        :param int io_b:
        :rtype: None
        """
        return self.visualization_setting_att.GetSelectedElementRGB(io_r, io_g, io_b)

    def get_selected_element_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetSelectedElementRGBInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the SelectedElementRGB setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetSelectedElementRGBInfo(io_admin_level, io_locked)

    def get_shader_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetShaderModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ShaderMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetShaderModeInfo(io_admin_level, io_locked)

    def get_static_cull_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetStaticCullInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the StaticCull setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetStaticCullInfo(io_admin_level, io_locked)

    def get_static_lod_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetStaticLODInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the StaticLOD setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetStaticLODInfo(io_admin_level, io_locked)

    def get_stereo_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetStereoModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the StereoMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetStereoModeInfo(io_admin_level, io_locked)

    def get_transparency_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTransparencyModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the TransparencyMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetTransparencyModeInfo(io_admin_level, io_locked)

    def get_two_side_lighting_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTwoSideLightingModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the TwoSideLightingMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetTwoSideLightingModeInfo(io_admin_level, io_locked)

    def get_under_intensified_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetUnderIntensifiedRGB(long ioR,
                | long ioG,
                | long ioB)
                | 
                |     Returns the UnderIntensifiedRGB parameter.

        :param int io_r:
        :param int io_g:
        :param int io_b:
        :rtype: None
        """
        return self.visualization_setting_att.GetUnderIntensifiedRGB(io_r, io_g, io_b)

    def get_under_intensified_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetUnderIntensifiedRGBInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the UnderIntensifiedRGB setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetUnderIntensifiedRGBInfo(io_admin_level, io_locked)

    def get_update_needed_rgb(self, io_r: int, io_g: int, io_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetUpdateNeededRGB(long ioR,
                | long ioG,
                | long ioB)
                | 
                |     Returns the UpdateNeededRGB parameter.

        :param int io_r:
        :param int io_g:
        :param int io_b:
        :rtype: None
        """
        return self.visualization_setting_att.GetUpdateNeededRGB(io_r, io_g, io_b)

    def get_update_needed_rgb_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetUpdateNeededRGBInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the UpdateNeededRGB setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetUpdateNeededRGBInfo(io_admin_level, io_locked)

    def get_viewpoint_animation_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetViewpointAnimationModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the ViewpointAnimationMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetViewpointAnimationModeInfo(io_admin_level, io_locked)

    def get_viz2_d_accuracy_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetViz2DAccuracyModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the 2DAccuracyMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetViz2DAccuracyModeInfo(io_admin_level, io_locked)

    def get_viz2_d_fixed_accuracy_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetViz2DFixedAccuracyInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the 2DFixedAccuracy setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetViz2DFixedAccuracyInfo(io_admin_level, io_locked)

    def get_viz2_d_proportionnal_accuracy_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetViz2DProportionnalAccuracyInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the 2DProportionnalAccuracy setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetViz2DProportionnalAccuracyInfo(io_admin_level, io_locked)

    def get_viz3_d_accuracy_mode_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetViz3DAccuracyModeInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Viz3DAccuracyMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetViz3DAccuracyModeInfo(io_admin_level, io_locked)

    def get_viz3_d_curve_accuracy_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetViz3DCurveAccuracyInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the 3DCurveAccuracy setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetViz3DCurveAccuracyInfo(io_admin_level, io_locked)

    def get_viz3_d_fixed_accuracy_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetViz3DFixedAccuracyInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the 3DFixedAccuracy setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetViz3DFixedAccuracyInfo(io_admin_level, io_locked)

    def get_viz3_d_proportionnal_accuracy_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetViz3DProportionnalAccuracyInfo(CATBSTR
                | ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves information about the Viz3DProportionnalAccuracy setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.visualization_setting_att.GetViz3DProportionnalAccuracyInfo(io_admin_level, io_locked)

    def put_back_face_culling_mode(self, i_back_face_culling_mode: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub PutBackFaceCullingMode(CATBackFaceCullingMode
                | iBackFaceCullingMode)
                | 
                |     Sets the BackFaceCullingMode attribute.
                | 
                |     Parameters:
                | 
                |         iBackFaceCullingMode
                |             Value of the back face culling mode setting option. The value to
                |             set can be one of the four possible values defined by the
                |             
                | 
                |         CATBackFaceCullingMode enumeration. 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             if the operation succeeded. 
                |         E_FAIL
                |             if the operation failed.

        :param int i_back_face_culling_mode: enum cat_back_face_culling_mode
        :rtype: None
        """
        return self.visualization_setting_att.PutBackFaceCullingMode(i_back_face_culling_mode)

    def set_accurate_picking_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAccuratePickingModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the AccuratePickingMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetAccuratePickingModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_accurate_picking_mode_lock'
        # # vba_code = """
        # # Public Function set_accurate_picking_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetAccuratePickingModeLock iLocked
        # #     set_accurate_picking_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_accurate_picking_window_size_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAccuratePickingWindowSizeLock(boolean iLocked)
                | 
                |     Locks or unlocks the AccuratePickingWindowSize setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetAccuratePickingWindowSizeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_accurate_picking_window_size_lock'
        # # vba_code = """
        # # Public Function set_accurate_picking_window_size_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetAccuratePickingWindowSizeLock iLocked
        # #     set_accurate_picking_window_size_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_all_z_buffer_element_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAllZBufferElementModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the AllZBufferElementMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetAllZBufferElementModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_all_z_buffer_element_mode_lock'
        # # vba_code = """
        # # Public Function set_all_z_buffer_element_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetAllZBufferElementModeLock iLocked
        # #     set_all_z_buffer_element_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_ambient_activation_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAmbientActivationLock(boolean iLocked)
                | 
                |     Locks or unlocks the AmbientActivation setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetAmbientActivationLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_ambient_activation_lock'
        # # vba_code = """
        # # Public Function set_ambient_activation_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetAmbientActivationLock iLocked
        # #     set_ambient_activation_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_anti_aliasing_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAntiAliasingModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the AntiAliasingMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetAntiAliasingModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_anti_aliasing_mode_lock'
        # # vba_code = """
        # # Public Function set_anti_aliasing_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetAntiAliasingModeLock iLocked
        # #     set_anti_aliasing_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_anti_aliasing_offset_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAntiAliasingOffsetLock(boolean iLocked)
                | 
                |     Locks or unlocks the AntiAliasingOffset setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetAntiAliasingOffsetLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_anti_aliasing_offset_lock'
        # # vba_code = """
        # # Public Function set_anti_aliasing_offset_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetAntiAliasingOffsetLock iLocked
        # #     set_anti_aliasing_offset_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_auxiliary_drill_viewer_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAuxiliaryDrillViewerLock(boolean iLocked)
                | 
                |     Locks or unlocks the AuxiliaryDrillViewer setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetAuxiliaryDrillViewerLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_auxiliary_drill_viewer_lock'
        # # vba_code = """
        # # Public Function set_auxiliary_drill_viewer_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetAuxiliaryDrillViewerLock iLocked
        # #     set_auxiliary_drill_viewer_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_back_face_culling_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBackFaceCullingModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the BackFaceCullingMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetBackFaceCullingModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_back_face_culling_mode_lock'
        # # vba_code = """
        # # Public Function set_back_face_culling_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetBackFaceCullingModeLock iLocked
        # #     set_back_face_culling_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_background_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBackgroundRGB(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the BackgroundRGB parameter.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.visualization_setting_att.SetBackgroundRGB(i_r, i_g, i_b)

    def set_background_rgb_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBackgroundRGBLock(boolean iLocked)
                | 
                |     Locks or unlocks the BackgroundRGB setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetBackgroundRGBLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_background_rgb_lock'
        # # vba_code = """
        # # Public Function set_background_rgb_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetBackgroundRGBLock iLocked
        # #     set_background_rgb_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_border_edges_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBorderEdgesModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the BorderEdgesMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetBorderEdgesModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_border_edges_mode_lock'
        # # vba_code = """
        # # Public Function set_border_edges_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetBorderEdgesModeLock iLocked
        # #     set_border_edges_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_border_edges_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBorderEdgesRGB(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the BorderEdgesRGB parameter.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.visualization_setting_att.SetBorderEdgesRGB(i_r, i_g, i_b)

    def set_border_edges_rgb_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBorderEdgesRGBLock(boolean iLocked)
                | 
                |     Locks or unlocks the BorderEdgesRGB setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetBorderEdgesRGBLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_border_edges_rgb_lock'
        # # vba_code = """
        # # Public Function set_border_edges_rgb_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetBorderEdgesRGBLock iLocked
        # #     set_border_edges_rgb_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_border_edges_thickness_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBorderEdgesThicknessLock(boolean iLocked)
                | 
                |     Locks or unlocks the BorderEdgesThickness setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetBorderEdgesThicknessLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_border_edges_thickness_lock'
        # # vba_code = """
        # # Public Function set_border_edges_thickness_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetBorderEdgesThicknessLock iLocked
        # #     set_border_edges_thickness_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_bounding_box_selection_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBoundingBoxSelectionModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the BoundingBoxSelectionMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetBoundingBoxSelectionModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_bounding_box_selection_mode_lock'
        # # vba_code = """
        # # Public Function set_bounding_box_selection_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetBoundingBoxSelectionModeLock iLocked
        # #     set_bounding_box_selection_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_color_background_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetColorBackgroundModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ColorBackgroundMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetColorBackgroundModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_color_background_mode_lock'
        # # vba_code = """
        # # Public Function set_color_background_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetColorBackgroundModeLock iLocked
        # #     set_color_background_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_diffuse_ambient_coefficient_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDefaultDiffuseAmbientCoefficientLock(boolean
                | iLocked)
                | 
                |     Locks or unlocks the DefaultDiffuseAmbientCoefficient setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetDefaultDiffuseAmbientCoefficientLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_diffuse_ambient_coefficient_lock'
        # # vba_code = """
        # # Public Function set_default_diffuse_ambient_coefficient_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetDefaultDiffuseAmbientCoefficientLock iLocked
        # #     set_default_diffuse_ambient_coefficient_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_shininess_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDefaultShininessLock(boolean iLocked)
                | 
                |     Locks or unlocks the DefaultShininess setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetDefaultShininessLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_shininess_lock'
        # # vba_code = """
        # # Public Function set_default_shininess_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetDefaultShininessLock iLocked
        # #     set_default_shininess_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_default_specular_coefficient_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDefaultSpecularCoefficientLock(boolean iLocked)
                | 
                |     Locks or unlocks the DefaultSpecularCoefficient setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetDefaultSpecularCoefficientLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_default_specular_coefficient_lock'
        # # vba_code = """
        # # Public Function set_default_specular_coefficient_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetDefaultSpecularCoefficientLock iLocked
        # #     set_default_specular_coefficient_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_current_scale_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDisplayCurrentScaleLock(boolean iLocked)
                | 
                |     Locks or unlocks the SetStereoModeLock setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetDisplayCurrentScaleLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_current_scale_lock'
        # # vba_code = """
        # # Public Function set_display_current_scale_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetDisplayCurrentScaleLock iLocked
        # #     set_display_current_scale_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_drill_list_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDisplayDrillListLock(boolean iLocked)
                | 
                |     Locks or unlocks the DisplayDrillList setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetDisplayDrillListLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_drill_list_lock'
        # # vba_code = """
        # # Public Function set_display_drill_list_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetDisplayDrillListLock iLocked
        # #     set_display_drill_list_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_display_immersive_drill_viewer_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDisplayImmersiveDrillViewerLock(boolean iLocked)
                | 
                |     Locks or unlocks the DisplayImmersiveDrillViewer setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetDisplayImmersiveDrillViewerLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_display_immersive_drill_viewer_lock'
        # # vba_code = """
        # # Public Function set_display_immersive_drill_viewer_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetDisplayImmersiveDrillViewerLock iLocked
        # #     set_display_immersive_drill_viewer_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dynamic_cull_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDynamicCullLock(boolean iLocked)
                | 
                |     Locks or unlocks the DynamicCull setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetDynamicCullLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dynamic_cull_lock'
        # # vba_code = """
        # # Public Function set_dynamic_cull_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetDynamicCullLock iLocked
        # #     set_dynamic_cull_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_dynamic_lod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetDynamicLODLock(boolean iLocked)
                | 
                |     Locks or unlocks the DynamicLOD setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetDynamicLODLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_dynamic_lod_lock'
        # # vba_code = """
        # # Public Function set_dynamic_lod_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetDynamicLODLock iLocked
        # #     set_dynamic_lod_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_face_hl_drill_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFaceHLDrillLock(boolean iLocked)
                | 
                |     Locks or unlocks the FaceHLDrill setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetFaceHLDrillLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_face_hl_drill_lock'
        # # vba_code = """
        # # Public Function set_face_hl_drill_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetFaceHLDrillLock iLocked
        # #     set_face_hl_drill_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_fly_collision_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFlyCollisionModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the FlyCollisionMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetFlyCollisionModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_fly_collision_mode_lock'
        # # vba_code = """
        # # Public Function set_fly_collision_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetFlyCollisionModeLock iLocked
        # #     set_fly_collision_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_fly_collision_sphere_radius_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFlyCollisionSphereRadiusLock(boolean iLocked)
                | 
                |     Locks or unlocks the FlyCollisionSphereRadius setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetFlyCollisionSphereRadiusLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_fly_collision_sphere_radius_lock'
        # # vba_code = """
        # # Public Function set_fly_collision_sphere_radius_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetFlyCollisionSphereRadiusLock iLocked
        # #     set_fly_collision_sphere_radius_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_fly_collision_type_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFlyCollisionTypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the FlyCollisionType setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetFlyCollisionTypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_fly_collision_type_lock'
        # # vba_code = """
        # # Public Function set_fly_collision_type_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetFlyCollisionTypeLock iLocked
        # #     set_fly_collision_type_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_fly_sensitivity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFlySensitivityLock(boolean iLocked)
                | 
                |     Locks or unlocks the FlySensitivity setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetFlySensitivityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_fly_sensitivity_lock'
        # # vba_code = """
        # # Public Function set_fly_sensitivity_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetFlySensitivityLock iLocked
        # #     set_fly_sensitivity_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_fly_speed_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFlySpeedLock(boolean iLocked)
                | 
                |     Locks or unlocks the FlySpeed setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetFlySpeedLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_fly_speed_lock'
        # # vba_code = """
        # # Public Function set_fly_speed_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetFlySpeedLock iLocked
        # #     set_fly_speed_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_fly_speed_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFlySpeedModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the FlySpeedMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetFlySpeedModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_fly_speed_mode_lock'
        # # vba_code = """
        # # Public Function set_fly_speed_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetFlySpeedModeLock iLocked
        # #     set_fly_speed_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_follow_ground_altitude_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFollowGroundAltitudeLock(boolean iLocked)
                | 
                |     Locks or unlocks the FollowGroundAltitude setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetFollowGroundAltitudeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_follow_ground_altitude_lock'
        # # vba_code = """
        # # Public Function set_follow_ground_altitude_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetFollowGroundAltitudeLock iLocked
        # #     set_follow_ground_altitude_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_follow_ground_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFollowGroundModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the FollowGroundMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetFollowGroundModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_follow_ground_mode_lock'
        # # vba_code = """
        # # Public Function set_follow_ground_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetFollowGroundModeLock iLocked
        # #     set_follow_ground_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_full_scene_anti_aliasing_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFullSceneAntiAliasingModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the AntiAliasingMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetFullSceneAntiAliasingModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_full_scene_anti_aliasing_mode_lock'
        # # vba_code = """
        # # Public Function set_full_scene_anti_aliasing_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetFullSceneAntiAliasingModeLock iLocked
        # #     set_full_scene_anti_aliasing_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_gravity_axis_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetGravityAxisLock(boolean iLocked)
                | 
                |     Locks or unlocks the GravityAxis setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetGravityAxisLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_gravity_axis_lock'
        # # vba_code = """
        # # Public Function set_gravity_axis_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetGravityAxisLock iLocked
        # #     set_gravity_axis_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_gravity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetGravityLock(boolean iLocked)
                | 
                |     Locks or unlocks the Gravity setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetGravityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_gravity_lock'
        # # vba_code = """
        # # Public Function set_gravity_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetGravityLock iLocked
        # #     set_gravity_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_halo_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetHaloModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the HaloMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetHaloModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_halo_mode_lock'
        # # vba_code = """
        # # Public Function set_halo_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetHaloModeLock iLocked
        # #     set_halo_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_handles_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetHandlesRGB(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the HandlesRGB parameter.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.visualization_setting_att.SetHandlesRGB(i_r, i_g, i_b)

    def set_handles_rgb_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetHandlesRGBLock(boolean iLocked)
                | 
                |     Locks or unlocks the HandlesRGB setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetHandlesRGBLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_handles_rgb_lock'
        # # vba_code = """
        # # Public Function set_handles_rgb_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetHandlesRGBLock iLocked
        # #     set_handles_rgb_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_isopar_generation_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetIsoparGenerationModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the IsoparGenerationMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetIsoparGenerationModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_isopar_generation_mode_lock'
        # # vba_code = """
        # # Public Function set_isopar_generation_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetIsoparGenerationModeLock iLocked
        # #     set_isopar_generation_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_keyboard_rotation_angle_value_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetKeyboardRotationAngleValueLock(boolean iLocked)
                | 
                |     Locks or unlocks the KeyboardRotationAngleValue setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetKeyboardRotationAngleValueLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_keyboard_rotation_angle_value_lock'
        # # vba_code = """
        # # Public Function set_keyboard_rotation_angle_value_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetKeyboardRotationAngleValueLock iLocked
        # #     set_keyboard_rotation_angle_value_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_light_viewer_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLightViewerModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the LightViewerMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetLightViewerModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_light_viewer_mode_lock'
        # # vba_code = """
        # # Public Function set_light_viewer_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetLightViewerModeLock iLocked
        # #     set_light_viewer_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_lineic_cgr_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLineicCgrModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the v setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetLineicCgrModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_lineic_cgr_mode_lock'
        # # vba_code = """
        # # Public Function set_lineic_cgr_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetLineicCgrModeLock iLocked
        # #     set_lineic_cgr_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_max_selection_move_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMaxSelectionMoveLock(boolean iLocked)
                | 
                |     Locks or unlocks the MaxSelectionMove setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetMaxSelectionMoveLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_max_selection_move_lock'
        # # vba_code = """
        # # Public Function set_max_selection_move_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetMaxSelectionMoveLock iLocked
        # #     set_max_selection_move_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_minimum_fps_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMinimumFPSModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the MinimumFPSMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetMinimumFPSModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_minimum_fps_mode_lock'
        # # vba_code = """
        # # Public Function set_minimum_fps_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetMinimumFPSModeLock iLocked
        # #     set_minimum_fps_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_minimum_space_fps_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMinimumSpaceFPSModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the MinimumSpaceFPSMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetMinimumSpaceFPSModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_minimum_space_fps_mode_lock'
        # # vba_code = """
        # # Public Function set_minimum_space_fps_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetMinimumSpaceFPSModeLock iLocked
        # #     set_minimum_space_fps_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_mouse_double_clic_delay_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMouseDoubleClicDelayLock(boolean iLocked)
                | 
                |     Locks or unlocks the MouseDoubleClicDelay setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetMouseDoubleClicDelayLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_mouse_double_clic_delay_lock'
        # # vba_code = """
        # # Public Function set_mouse_double_clic_delay_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetMouseDoubleClicDelayLock iLocked
        # #     set_mouse_double_clic_delay_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_mouse_speed_value_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetMouseSpeedValueLock(boolean iLocked)
                | 
                |     Locks or unlocks the MouseSpeedValue setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetMouseSpeedValueLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_mouse_speed_value_lock'
        # # vba_code = """
        # # Public Function set_mouse_speed_value_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetMouseSpeedValueLock iLocked
        # #     set_mouse_speed_value_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_nb_isopars_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNbIsoparsLock(boolean iLocked)
                | 
                |     Locks or unlocks the NbIsopars setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetNbIsoparsLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_nb_isopars_lock'
        # # vba_code = """
        # # Public Function set_nb_isopars_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetNbIsoparsLock iLocked
        # #     set_nb_isopars_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_no_show_background_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNoShowBackgroundRGB(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the No Show Background Color setting attribute value.
                |     Role: The No Show Background Color setting attribute manages the
                |     backgraound color of no show space
                | 
                |     Parameters:
                | 
                |         iR,
                |             iG, iB [in] The Red, Green, Blue components of the No Show
                |             Background Color setting attribute value
                |             Legal values: between 0 and 255 
                | 
                |     Returns:
                |         S_OK if the No Show Background Color setting attribute value is
                |         successfully set, and E_FAIL otherwise

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.visualization_setting_att.SetNoShowBackgroundRGB(i_r, i_g, i_b)

    def set_no_show_background_rgb_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNoShowBackgroundRGBLock(boolean iLocked)
                | 
                |     Locks or unlocks the No Show Background Color setting
                |     attribute.
                |     Role: Locks or unlocks the No Show Background Color setting attribute if
                |     the operation is allowed in the current administrated environment. In user mode
                |     this method will always return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             [in] A flag to indicate whether the No Show Background Color
                |             setting attribute should be locked.
                |             Legal values:
                |             TRUE to lock
                |             FALSE to unlock 
                | 
                |     Returns:
                |         S_OK if the No Show Background Color setting attribute is successfully
                |         locked or unlocked, and E_FAIL otherwise
                |         Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetNoShowBackgroundRGBLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_no_show_background_rgb_lock'
        # # vba_code = """
        # # Public Function set_no_show_background_rgb_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetNoShowBackgroundRGBLock iLocked
        # #     set_no_show_background_rgb_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_no_z_buffer_selection_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNoZBufferSelectionModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the NoZBufferSelectionMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetNoZBufferSelectionModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_no_z_buffer_selection_mode_lock'
        # # vba_code = """
        # # Public Function set_no_z_buffer_selection_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetNoZBufferSelectionModeLock iLocked
        # #     set_no_z_buffer_selection_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_number_of_minimum_fps_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNumberOfMinimumFPSLock(boolean iLocked)
                | 
                |     Locks or unlocks the NumberOfMinimumFPS setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetNumberOfMinimumFPSLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_number_of_minimum_fps_lock'
        # # vba_code = """
        # # Public Function set_number_of_minimum_fps_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetNumberOfMinimumFPSLock iLocked
        # #     set_number_of_minimum_fps_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_number_of_minimum_space_fps_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetNumberOfMinimumSpaceFPSLock(boolean iLocked)
                | 
                |     Locks or unlocks the NumberOfMinimumSpaceFPS setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetNumberOfMinimumSpaceFPSLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_number_of_minimum_space_fps_lock'
        # # vba_code = """
        # # Public Function set_number_of_minimum_space_fps_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetNumberOfMinimumSpaceFPSLock iLocked
        # #     set_number_of_minimum_space_fps_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_occlusion_culling_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetOcclusionCullingModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the OcclusionCullingMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetOcclusionCullingModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_occlusion_culling_mode_lock'
        # # vba_code = """
        # # Public Function set_occlusion_culling_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetOcclusionCullingModeLock iLocked
        # #     set_occlusion_culling_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_opaque_faces_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetOpaqueFacesLock(boolean iLocked)
                | 
                |     Locks or unlocks the SetStereoModeLock setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetOpaqueFacesLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_opaque_faces_lock'
        # # vba_code = """
        # # Public Function set_opaque_faces_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetOpaqueFacesLock iLocked
        # #     set_opaque_faces_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_other_selection_timeout_activity_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetOtherSelectionTimeoutActivityLock(boolean iLocked)
                | 
                |     Locks or unlocks the OtherSelectionTimeoutActivity setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetOtherSelectionTimeoutActivityLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_other_selection_timeout_activity_lock'
        # # vba_code = """
        # # Public Function set_other_selection_timeout_activity_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetOtherSelectionTimeoutActivityLock iLocked
        # #     set_other_selection_timeout_activity_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_other_selection_timeout_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetOtherSelectionTimeoutLock(boolean iLocked)
                | 
                |     Locks or unlocks the OtherSelectionTimeout setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetOtherSelectionTimeoutLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_other_selection_timeout_lock'
        # # vba_code = """
        # # Public Function set_other_selection_timeout_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetOtherSelectionTimeoutLock iLocked
        # #     set_other_selection_timeout_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_picking_window_size_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPickingWindowSizeLock(boolean iLocked)
                | 
                |     Locks or unlocks the PickingWindowSize setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetPickingWindowSizeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_picking_window_size_lock'
        # # vba_code = """
        # # Public Function set_picking_window_size_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetPickingWindowSizeLock iLocked
        # #     set_picking_window_size_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pre_sel_navigator_started_by_arrow_keys_lock(self, i_locked: bool) -> None:
        """

        Introduced in V5-6R2018.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Sub SetPreSelNavigatorStartedByArrowKeysLock(boolean iLocked)
                |     Locks or unlocks the PreSelNavigatorStartedByArrowKeys setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """

        self.release_check(
            self.application.system_configuration.release,
            28,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.visualization_setting_att.SetPreSelNavigatorStartedByArrowKeysLock(i_locked)

    def set_pre_selection_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPreSelectionModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreSelectionMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetPreSelectionModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pre_selection_mode_lock'
        # # vba_code = """
        # # Public Function set_pre_selection_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetPreSelectionModeLock iLocked
        # #     set_pre_selection_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_preselected_element_linetype_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPreselectedElementLinetypeLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreselectedElementLinetype setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetPreselectedElementLinetypeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_preselected_element_linetype_lock'
        # # vba_code = """
        # # Public Function set_preselected_element_linetype_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetPreselectedElementLinetypeLock iLocked
        # #     set_preselected_element_linetype_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_preselected_element_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPreselectedElementRGB(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the PreselectedElementRGB parameter.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.visualization_setting_att.SetPreselectedElementRGB(i_r, i_g, i_b)

    def set_preselected_element_rgb_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPreselectedElementRGBLock(boolean iLocked)
                | 
                |     Locks or unlocks the PreselectedElementRGB setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetPreselectedElementRGBLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_preselected_element_rgb_lock'
        # # vba_code = """
        # # Public Function set_preselected_element_rgb_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetPreselectedElementRGBLock iLocked
        # #     set_preselected_element_rgb_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_rotation_sphere_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRotationSphereModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the RotationSphereMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetRotationSphereModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_rotation_sphere_mode_lock'
        # # vba_code = """
        # # Public Function set_rotation_sphere_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetRotationSphereModeLock iLocked
        # #     set_rotation_sphere_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_selected_edge_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSelectedEdgeRGB(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the SelectedEdgeRGB parameter.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.visualization_setting_att.SetSelectedEdgeRGB(i_r, i_g, i_b)

    def set_selected_edge_rgb_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSelectedEdgeRGBLock(boolean iLocked)
                | 
                |     Locks or unlocks the SelectedEdgeRGB setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetSelectedEdgeRGBLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_selected_edge_rgb_lock'
        # # vba_code = """
        # # Public Function set_selected_edge_rgb_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetSelectedEdgeRGBLock iLocked
        # #     set_selected_edge_rgb_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_selected_element_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSelectedElementRGB(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the SelectedElementRGB parameter.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.visualization_setting_att.SetSelectedElementRGB(i_r, i_g, i_b)

    def set_selected_element_rgb_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSelectedElementRGBLock(boolean iLocked)
                | 
                |     Locks or unlocks the SelectedElementRGB setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetSelectedElementRGBLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_selected_element_rgb_lock'
        # # vba_code = """
        # # Public Function set_selected_element_rgb_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetSelectedElementRGBLock iLocked
        # #     set_selected_element_rgb_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_shader_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetShaderModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ShaderMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetShaderModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_shader_mode_lock'
        # # vba_code = """
        # # Public Function set_shader_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetShaderModeLock iLocked
        # #     set_shader_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_static_cull_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetStaticCullLock(boolean iLocked)
                | 
                |     Locks or unlocks the StaticCull setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetStaticCullLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_static_cull_lock'
        # # vba_code = """
        # # Public Function set_static_cull_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetStaticCullLock iLocked
        # #     set_static_cull_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_static_lod_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetStaticLODLock(boolean iLocked)
                | 
                |     Locks or unlocks the StaticLOD setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetStaticLODLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_static_lod_lock'
        # # vba_code = """
        # # Public Function set_static_lod_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetStaticLODLock iLocked
        # #     set_static_lod_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_stereo_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetStereoModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the StereoMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetStereoModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_stereo_mode_lock'
        # # vba_code = """
        # # Public Function set_stereo_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetStereoModeLock iLocked
        # #     set_stereo_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_transparency_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTransparencyModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the TransparencyMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetTransparencyModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_transparency_mode_lock'
        # # vba_code = """
        # # Public Function set_transparency_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetTransparencyModeLock iLocked
        # #     set_transparency_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_two_side_lighting_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTwoSideLightingModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the TwoSideLightingMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetTwoSideLightingModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_two_side_lighting_mode_lock'
        # # vba_code = """
        # # Public Function set_two_side_lighting_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetTwoSideLightingModeLock iLocked
        # #     set_two_side_lighting_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_under_intensified_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetUnderIntensifiedRGB(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the UnderIntensifiedRGB parameter.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.visualization_setting_att.SetUnderIntensifiedRGB(i_r, i_g, i_b)

    def set_under_intensified_rgb_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetUnderIntensifiedRGBLock(boolean iLocked)
                | 
                |     Locks or unlocks the UnderIntensifiedRGB setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetUnderIntensifiedRGBLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_under_intensified_rgb_lock'
        # # vba_code = """
        # # Public Function set_under_intensified_rgb_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetUnderIntensifiedRGBLock iLocked
        # #     set_under_intensified_rgb_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_update_needed_rgb(self, i_r: int, i_g: int, i_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetUpdateNeededRGB(long iR,
                | long iG,
                | long iB)
                | 
                |     Sets the UpdateNeededRGB parameter.

        :param int i_r:
        :param int i_g:
        :param int i_b:
        :rtype: None
        """
        return self.visualization_setting_att.SetUpdateNeededRGB(i_r, i_g, i_b)

    def set_update_needed_rgb_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetUpdateNeededRGBLock(boolean iLocked)
                | 
                |     Locks or unlocks the UpdateNeededRGB setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetUpdateNeededRGBLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_update_needed_rgb_lock'
        # # vba_code = """
        # # Public Function set_update_needed_rgb_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetUpdateNeededRGBLock iLocked
        # #     set_update_needed_rgb_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_viewpoint_animation_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetViewpointAnimationModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the ViewpointAnimationMode setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetViewpointAnimationModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_viewpoint_animation_mode_lock'
        # # vba_code = """
        # # Public Function set_viewpoint_animation_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetViewpointAnimationModeLock iLocked
        # #     set_viewpoint_animation_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_viz2_d_accuracy_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetViz2DAccuracyModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the 2DAccuracyMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetViz2DAccuracyModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_viz2_d_accuracy_mode_lock'
        # # vba_code = """
        # # Public Function set_viz2_d_accuracy_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetViz2DAccuracyModeLock iLocked
        # #     set_viz2_d_accuracy_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_viz2_d_fixed_accuracy_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetViz2DFixedAccuracyLock(boolean iLocked)
                | 
                |     Locks or unlocks the 2DFixedAccuracy setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetViz2DFixedAccuracyLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_viz2_d_fixed_accuracy_lock'
        # # vba_code = """
        # # Public Function set_viz2_d_fixed_accuracy_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetViz2DFixedAccuracyLock iLocked
        # #     set_viz2_d_fixed_accuracy_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_viz2_d_proportionnal_accuracy_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetViz2DProportionnalAccuracyLock(boolean iLocked)
                | 
                |     Locks or unlocks the 2DProportionnalAccuracy setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetViz2DProportionnalAccuracyLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_viz2_d_proportionnal_accuracy_lock'
        # # vba_code = """
        # # Public Function set_viz2_d_proportionnal_accuracy_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetViz2DProportionnalAccuracyLock iLocked
        # #     set_viz2_d_proportionnal_accuracy_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_viz3_d_accuracy_mode_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetViz3DAccuracyModeLock(boolean iLocked)
                | 
                |     Locks or unlocks the Viz3DAccuracyMode setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetViz3DAccuracyModeLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_viz3_d_accuracy_mode_lock'
        # # vba_code = """
        # # Public Function set_viz3_d_accuracy_mode_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetViz3DAccuracyModeLock iLocked
        # #     set_viz3_d_accuracy_mode_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_viz3_d_curve_accuracy_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetViz3DCurveAccuracyLock(boolean iLocked)
                | 
                |     Locks or unlocks the 3DCurveAccuracy setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetViz3DCurveAccuracyLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_viz3_d_curve_accuracy_lock'
        # # vba_code = """
        # # Public Function set_viz3_d_curve_accuracy_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetViz3DCurveAccuracyLock iLocked
        # #     set_viz3_d_curve_accuracy_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_viz3_d_fixed_accuracy_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetViz3DFixedAccuracyLock(boolean iLocked)
                | 
                |     Locks or unlocks the 3DFixedAccuracy setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetViz3DFixedAccuracyLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_viz3_d_fixed_accuracy_lock'
        # # vba_code = """
        # # Public Function set_viz3_d_fixed_accuracy_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetViz3DFixedAccuracyLock iLocked
        # #     set_viz3_d_fixed_accuracy_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_viz3_d_proportionnal_accuracy_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetViz3DProportionnalAccuracyLock(boolean iLocked)
                | 
                |     Locks or unlocks the Viz3DProportionnalAccuracy setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_locked:
        :rtype: None
        """
        return self.visualization_setting_att.SetViz3DProportionnalAccuracyLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_viz3_d_proportionnal_accuracy_lock'
        # # vba_code = """
        # # Public Function set_viz3_d_proportionnal_accuracy_lock(visualization_setting_att)
        # #     Dim iLocked (2)
        # #     visualization_setting_att.SetViz3DProportionnalAccuracyLock iLocked
        # #     set_viz3_d_proportionnal_accuracy_lock = iLocked
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'VisualizationSettingAtt(name="{self.name}")'
