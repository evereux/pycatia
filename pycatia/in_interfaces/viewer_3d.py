#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.light_sources import LightSources
from pycatia.in_interfaces.viewer import Viewer
from pycatia.in_interfaces.viewpoint_3d import ViewPoint3D


class Viewer3D(Viewer):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Viewer
                |                         Viewer3D
                | 
                | Represents a 3D viewer.
                | The 3D viewer aggregates a 3D viewpoint to display a 3D scene. In addition, the
                | Viewer3D object manages the lighting, the depth effects, the navigation style,
                | and the rendering mode.
                | 
                | See also:
                |     Viewpoint3D, CatLightingMode, CatNavigationStyle, CatRenderingMode
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.viewer_3d = com_object

    @property
    def clipping_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ClippingMode() As CatClippingMode
                | 
                |     Returns or sets the clipping mode.
                | 
                |     Example:
                |         This example sets the depth effect for the My3DViewer 3D viewer to
                |         catClippingModeNearAndFar.
                | 
                |          My3DViewer.ClippingMode = catClippingModeNearAndFar

        :return: enum cat_clipping_mode
        :rtype: int
        """

        return self.viewer_3d.ClippingMode

    @clipping_mode.setter
    def clipping_mode(self, value: int):
        """
        :param int value: enum cat_clipping_mode
        """

        self.viewer_3d.ClippingMode = value

    @property
    def far_limit(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FarLimit() As double
                | 
                |     Returns or sets the far limit for the far clipping plane. The distance is
                |     measured from the eye location, that is the origin of the viewpoint, and is
                |     expressed in model unit. The far clipping plane is available with the
                |     catClippingModeFar and catClippingModeNearAndFar values of the CatClippingMode
                |     enumeration only.
                | 
                |     Example:
                |         This example sets the far limit for the far clipping plane of the
                |         My3DViewer 3D viewer to 150 model units.
                | 
                |          My3DViewer.FarLimit = 150

        :rtype: float
        """

        return self.viewer_3d.FarLimit

    @far_limit.setter
    def far_limit(self, value: float):
        """
        :param float value:
        """

        self.viewer_3d.FarLimit = value

    @property
    def foggy(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Foggy() As boolean
                | 
                |     Returns or sets the fog mode. Useful when clipping is
                |     enabled.
                | 
                |     Example:
                |         This example sets the fog on for the My3DViewer 3D
                |         viewer:
                | 
                |          My3DViewer.Foggy = True

        :rtype: bool
        """

        return self.viewer_3d.Foggy

    @foggy.setter
    def foggy(self, value: bool):
        """
        :param bool value:
        """

        self.viewer_3d.Foggy = value

    @property
    def ground(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Ground() As boolean
                | 
                |     Returns or sets the ground displaying mode.
                | 
                |     Example:
                |         This example makes the ground visible for the My3DViewer 3D
                |         viewer:
                | 
                |          My3DViewer.Ground = True

        :rtype: bool
        """

        return self.viewer_3d.Ground

    @ground.setter
    def ground(self, value: bool):
        """
        :param bool value:
        """

        self.viewer_3d.Ground = value

    @property
    def light_sources(self) -> LightSources:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LightSources() As LightSources (Read Only)
                | 
                |     Returns the viewer's light source collection.
                | 
                |     Example:
                |         This example retrieves the light source collection for the My3DViewer
                |         3D viewer in VPLightSources.
                | 
                |          Set VPLightSources = My3DViewer.LightSources

        :rtype: LightSources
        """

        return LightSources(self.viewer_3d.LightSources)

    @property
    def lighting_intensity(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LightingIntensity() As double
                | 
                |     Returns or sets the lighting intensity. The lighting intensity ranges
                |     between 0 and 1.
                | 
                |     Example:
                |         This example sets the lighting intensity for the My3DViewer 3D viewer
                |         to 0.35.
                | 
                |          My3DViewer.LightingIntensity = 0.35

        :rtype: float
        """

        return self.viewer_3d.LightingIntensity

    @lighting_intensity.setter
    def lighting_intensity(self, value: float):
        """
        :param float value:
        """

        self.viewer_3d.LightingIntensity = value

    @property
    def lighting_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property LightingMode() As CatLightingMode
                | 
                |     Returns or sets the lighting mode.
                | 
                |     Example:
                |         This example sets the lighting mode for the My3DViewer 3D viewer to
                |         catInfiniteLightSource.
                | 
                |          My3DViewer.LightingMode = catInfiniteLightSource

        :return: enum cat_lighting_mode
        :rtype: int
        """

        return self.viewer_3d.LightingMode

    @lighting_mode.setter
    def lighting_mode(self, value: int):
        """
        :param int value: enum cat_lighting_mode
        """

        self.viewer_3d.LightingMode = value

    @property
    def navigation_style(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NavigationStyle() As CatNavigationStyle
                | 
                |     Returns or sets the navigation style.
                | 
                |     Example:
                |         This example sets the navigation style for the My3DViewer 3D viewer to
                |         catNavigationWalk.
                | 
                |          My3DViewer.NavigationStyle = catNavigationWalk

        :return: enum cat_navigation_style
        :rtype: int
        """

        return self.viewer_3d.NavigationStyle

    @navigation_style.setter
    def navigation_style(self, value: int):
        """
        :param int value: enum cat_navigation_style
        """

        self.viewer_3d.NavigationStyle = value

    @property
    def near_limit(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property NearLimit() As double
                | 
                |     Returns or sets the near limit for the near clipping plane. The distance is
                |     measured from the eye location, that is the origin of the viewpoint, and is
                |     expressed in model unit. The near clipping plane is available with the
                |     catClippingModeNear and catClippingModeNearAndFar values of the CatClippingMode
                |     enumeration only.
                | 
                |     Example:
                |         This example sets the near limit for the near clipping plane of the
                |         My3DViewer 3D viewer to 75 model units.
                | 
                |          My3DViewer.NearLimit = 75

        :rtype: float
        """

        return self.viewer_3d.NearLimit

    @near_limit.setter
    def near_limit(self, value: float):
        """
        :param float value:
        """

        self.viewer_3d.NearLimit = value

    @property
    def rendering_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RenderingMode() As CatRenderingMode
                | 
                |     Returns or sets the rendering mode.
                | 
                |     Example:
                |         This example sets the rendering mode for the My3DViewer 3D viewer to
                |         catRenderShadingWithEdges.
                | 
                |          My3DViewer.RenderingMode = catRenderShadingWithEdges

        :return: enum cat_rendering_mode
        :rtype: int
        """

        return self.viewer_3d.RenderingMode

    @rendering_mode.setter
    def rendering_mode(self, value: int):
        """
        :param int value: enum cat_rendering_mode
        """

        self.viewer_3d.RenderingMode = value

    @property
    def viewpoint_3d(self) -> ViewPoint3D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Viewpoint3D() As Viewpoint3D
                | 
                |     Returns or sets the 3D viewpoint of a 3D viewer.
                | 
                |     Example:
                |         This example retrieves the Nice3DViewpoint 3D viewpoint from the
                |         My3DViewer 3D viewer.
                | 
                |          Dim Nice3DViewpoint As Viewpoint3D
                |          Set Nice3DViewpoint = My3DViewer.Viewpoint3D

        :rtype: ViewPoint3D
        """

        return ViewPoint3D(self.viewer_3d.Viewpoint3D)

    @viewpoint_3d.setter
    def viewpoint_3d(self, value: ViewPoint3D):
        """
        :param ViewPoint3D value:
        """

        self.viewer_3d.Viewpoint3D = value

    def rotate(self, i_axis: tuple, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Rotate(CATSafeArrayVariant iAxis,
                | double iAngle)
                | 
                |     Applies a rotation. The rotation of iAngle degrees is applied to the
                |     viewer's contents around the axis iAxis (an array of 3 Variants), the invariant
                |     point being the target (ie: Origin +
                |     FocusDistance*SightDirection).
                | 
                |     Example:
                |         This applies a rotation of 10 degrees around the Up Direction to the
                |         contents of the MyViewer3D viewer.
                | 
                |          MyViewer3D.Rotate MyViewer3D.UpDirection, 10

        :param tuple i_axis:
        :param float i_angle:
        :rtype: None
        """
        return self.viewer_3d.Rotate(i_axis, i_angle)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'rotate'
        # # vba_code = """
        # # Public Function rotate(viewer_3d)
        # #     Dim iAxis (2)
        # #     viewer_3d.Rotate iAxis
        # #     rotate = iAxis
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def translate(self, i_vector: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub Translate(CATSafeArrayVariant iVector)
                | 
                |     Applies a translation. The translation vector is iVector (an array of 3
                |     Variants).
                | 
                |     Example:
                |         This applies a translation along (1, 1, 1) to the contents of the
                |         MyViewer3D viewer.
                | 
                |          MyViewer3D.Translate Array(1, 1, 1)

        :param tuple i_vector:
        :rtype: None
        """
        return self.viewer_3d.Translate(i_vector)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'translate'
        # # vba_code = """
        # # Public Function translate(viewer_3d)
        # #     Dim iVector (2)
        # #     viewer_3d.Translate iVector
        # #     translate = iVector
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Viewer3D(name="{self.name}")'
