#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class RenderingLight(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RenderingLight
                | 
                | Represents a Rendering Light object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rendering_light = com_object

    @property
    def active_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveStatus() As short
                | 
                |     Returns or sets the light active status.
                |     A light illuminates only when it is active. The active status can
                |     be:
                |     1: light is on
                |     0: light is off

        :rtype: int
        """

        return self.rendering_light.ActiveStatus

    @active_status.setter
    def active_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.ActiveStatus = value

    @property
    def ambient(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Ambient() As double
                | 
                |     Returns or sets the light ambient intensity of a light.

        :rtype: float
        """

        return self.rendering_light.Ambient

    @ambient.setter
    def ambient(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.Ambient = value

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Angle() As double
                | 
                |     Returns or sets the light angle of a spot light.
                |     The angle ranges from 0. (directional light) to 360. (point light).

        :rtype: float
        """

        return self.rendering_light.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.Angle = value

    @property
    def area_samples_u(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AreaSamplesU() As short
                | 
                |     Changes the number of samples taken in U direction of the area source.

        :rtype: int
        """

        return self.rendering_light.AreaSamplesU

    @area_samples_u.setter
    def area_samples_u(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.AreaSamplesU = value

    @property
    def area_samples_v(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AreaSamplesV() As short
                | 
                |     Changes the number of samples taken in V direction of the area source.

        :rtype: int
        """

        return self.rendering_light.AreaSamplesV

    @area_samples_v.setter
    def area_samples_v(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.AreaSamplesV = value

    @property
    def area_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AreaStatus() As short
                | 
                |     Returns or sets the light area visibility status.
                |     The area visibility status can be:
                |     1: light area is rendered
                |     0: light area is not rendered

        :rtype: int
        """

        return self.rendering_light.AreaStatus

    @area_status.setter
    def area_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.AreaStatus = value

    @property
    def attenuation_angle_ratio(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttenuationAngleRatio() As double
                | 
                |     Returns or sets the light attenuation angle ratio.
                |     It represents the fraction of the light angle where the illumination starts
                |     to attenuate.
                |     The ratio ranges from 0. (attenuation starts when angle is null) to 1.
                |     (attenuation starts when angle is maximum = no angle attenuation).

        :rtype: float
        """

        return self.rendering_light.AttenuationAngleRatio

    @attenuation_angle_ratio.setter
    def attenuation_angle_ratio(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.AttenuationAngleRatio = value

    @property
    def attenuation_start_ratio(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AttenuationStartRatio() As double
                | 
                |     Returns or sets the light attenuation start ratio.
                |     It represents the fraction of the end distance where the light intensity
                |     starts to attenuate.
                |     The ratio ranges from 0. (attenuation starts at the origin) to 1.
                |     (attenuation starts at the end distance = no attenuation).

        :rtype: float
        """

        return self.rendering_light.AttenuationStartRatio

    @attenuation_start_ratio.setter
    def attenuation_start_ratio(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.AttenuationStartRatio = value

    @property
    def caustic_photons_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CausticPhotonsNumber() As long
                | 
                |     Changes the maximum number of caustic photons to emit from the light
                |     source.

        :rtype: int
        """

        return self.rendering_light.CausticPhotonsNumber

    @caustic_photons_number.setter
    def caustic_photons_number(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.CausticPhotonsNumber = value

    @property
    def cylinder_light_height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CylinderLightHeight() As double
                | 
                |     Returns or sets the cylinder light area radius.

        :rtype: float
        """

        return self.rendering_light.CylinderLightHeight

    @cylinder_light_height.setter
    def cylinder_light_height(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.CylinderLightHeight = value

    @property
    def cylinder_light_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CylinderLightRadius() As double
                | 
                |     Returns or sets the cylinder light area radius.

        :rtype: float
        """

        return self.rendering_light.CylinderLightRadius

    @cylinder_light_radius.setter
    def cylinder_light_radius(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.CylinderLightRadius = value

    @property
    def diffuse(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Diffuse() As double
                | 
                |     Returns or sets the light diffuse intensity of a light.

        :rtype: float
        """

        return self.rendering_light.Diffuse

    @diffuse.setter
    def diffuse(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.Diffuse = value

    @property
    def disk_light_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DiskLightRadius() As double
                | 
                |     Returns or sets the disk light area radius.

        :rtype: float
        """

        return self.rendering_light.DiskLightRadius

    @disk_light_radius.setter
    def disk_light_radius(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.DiskLightRadius = value

    @property
    def end_distance(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EndDistance() As double
                | 
                |     Returns or sets the light maximum distance of
                |     illumination.
                |     The light illuminates from its origin to its end distance. Objects farther
                |     than this distance are not affected by the light.

        :rtype: float
        """

        return self.rendering_light.EndDistance

    @end_distance.setter
    def end_distance(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.EndDistance = value

    @property
    def energy_factor(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EnergyFactor() As double
                | 
                |     Changes the factor for indirect illumination energy.

        :rtype: float
        """

        return self.rendering_light.EnergyFactor

    @energy_factor.setter
    def energy_factor(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.EnergyFactor = value

    @property
    def falloff_exponent(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FalloffExponent() As short
                | 
                |     Changes the light falloff exponent. Exponent value can be 0, 1 or
                |     2.
                |     An exponent of 0 means that the light energy does not fall off with distance.
                |     An exponent of 1 means that the light energy fall off is linear.
                |     An exponent of 2 is physically correct.

        :rtype: int
        """

        return self.rendering_light.FalloffExponent

    @falloff_exponent.setter
    def falloff_exponent(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.FalloffExponent = value

    @property
    def global_photons_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlobalPhotonsNumber() As long
                | 
                |     Changes the maximum number of global illumination photons to emit from the
                |     light source.

        :rtype: int
        """

        return self.rendering_light.GlobalPhotonsNumber

    @global_photons_number.setter
    def global_photons_number(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.GlobalPhotonsNumber = value

    @property
    def hardware_shadow_smoothing(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HardwareShadowSmoothing() As short
                | 
                |     Returns or sets the light shadow smoothing.
                |     It is an integer in the scale 0 to 10 It represents the cleanliness of the
                |     shadow limits

        :rtype: int
        """

        return self.rendering_light.HardwareShadowSmoothing

    @hardware_shadow_smoothing.setter
    def hardware_shadow_smoothing(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.HardwareShadowSmoothing = value

    @property
    def hardware_shadow_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HardwareShadowStatus() As short
                | 
                |     Returns or sets the light shadow status on environment.
                |     The shadow status can be:
                |     1: light casts shadows on environment
                |     0: light does not cast shadows on environment
                | 
                |     The shadow status on environmemt can be activate only with a directional
                |     light

        :rtype: int
        """

        return self.rendering_light.HardwareShadowStatus

    @hardware_shadow_status.setter
    def hardware_shadow_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.HardwareShadowStatus = value

    @property
    def hardware_shadow_transparency(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property HardwareShadowTransparency() As double
                | 
                |     Returns or sets the light shadow transparency.
                |     It is a float in the scale 0.0(no transparency) to 1.0 (full transparency)

        :rtype: float
        """

        return self.rendering_light.HardwareShadowTransparency

    @hardware_shadow_transparency.setter
    def hardware_shadow_transparency(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.HardwareShadowTransparency = value

    @property
    def illumination_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property IlluminationStatus() As short
                | 
                |     Changes the indirect illumination status.
                |     The indirect illumination status can be:
                |     1: indirect illumination is enabled
                |     0: indirect illumination is disabled

        :rtype: int
        """

        return self.rendering_light.IlluminationStatus

    @illumination_status.setter
    def illumination_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.IlluminationStatus = value

    @property
    def intensity(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Intensity() As double
                | 
                |     Returns or sets the light intensity of a light.

        :rtype: float
        """

        return self.rendering_light.Intensity

    @intensity.setter
    def intensity(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.Intensity = value

    @property
    def light_area_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LightAreaType() As short
                | 
                |     Returns or sets the light area type.
                | 
                |         Possible area light types are:
                |         1: CATNone
                |         2: CATRectangle
                |         3: CATDisk
                |         4: CATSphere
                |         5: CATCylinder

        :rtype: int
        """

        return self.rendering_light.LightAreaType

    @light_area_type.setter
    def light_area_type(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.LightAreaType = value

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Mode() As short
                | 
                |     Returns or sets the light mode.
                | 
                |         Possible light modes are:
                |         1: Light is linked to the viewpoint
                |         2: Light is linked to the model

        :rtype: int
        """

        return self.rendering_light.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.Mode = value

    @property
    def rectangle_light_length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RectangleLightLength() As double
                | 
                |     Returns or sets the light area length.

        :rtype: float
        """

        return self.rendering_light.RectangleLightLength

    @rectangle_light_length.setter
    def rectangle_light_length(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.RectangleLightLength = value

    @property
    def rectangle_light_width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RectangleLightWidth() As double
                | 
                |     Returns or sets the light area width.

        :rtype: float
        """

        return self.rendering_light.RectangleLightWidth

    @rectangle_light_width.setter
    def rectangle_light_width(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.RectangleLightWidth = value

    @property
    def shadow_fitting_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShadowFittingMode() As short
                | 
                |     Returns or sets the light shadow fitting mode.
                |     The shadow fitting mode can be:
                |     0: Standard
                |     1: Good

        :rtype: int
        """

        return self.rendering_light.ShadowFittingMode

    @shadow_fitting_mode.setter
    def shadow_fitting_mode(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.ShadowFittingMode = value

    @property
    def shadow_map_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShadowMapSize() As short
                | 
                |     Returns or sets the light shadow map size.
                |     The shadow map size can be:
                |     0: Small (512)
                |     1: Medium (1024)
                |     2: Large (2048)

        :rtype: int
        """

        return self.rendering_light.ShadowMapSize

    @shadow_map_size.setter
    def shadow_map_size(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.ShadowMapSize = value

    @property
    def shadow_object_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShadowObjectStatus() As short
                | 
                |     Returns or sets the light shadow status on objet.
                |     The shadow status can be:
                |     1: light casts shadows on objet
                |     0: light does not cast shadows on objet
                | 
                |     The shadow status on object can be activate only with a spot light

        :rtype: int
        """

        return self.rendering_light.ShadowObjectStatus

    @shadow_object_status.setter
    def shadow_object_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.ShadowObjectStatus = value

    @property
    def shadow_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShadowStatus() As short
                | 
                |     Returns or sets the light shadow status.
                |     The shadow status can be:
                |     1: light casts shadows
                |     0: light does not cast shadows

        :rtype: int
        """

        return self.rendering_light.ShadowStatus

    @shadow_status.setter
    def shadow_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.ShadowStatus = value

    @property
    def specular(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Specular() As double
                | 
                |     Returns or sets the light specular intensity of a light.

        :rtype: float
        """

        return self.rendering_light.Specular

    @specular.setter
    def specular(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.Specular = value

    @property
    def sphere_light_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SphereLightRadius() As double
                | 
                |     Returns or sets the sphere light area radius.

        :rtype: float
        """

        return self.rendering_light.SphereLightRadius

    @sphere_light_radius.setter
    def sphere_light_radius(self, value: float):
        """
        :param float value:
        """

        self.rendering_light.SphereLightRadius = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As short
                | 
                |     Returns or sets the light type.
                | 
                |         Possible light types are:
                |         1: Spot light
                |         2: Point light
                |         3: Directional light

        :rtype: int
        """

        return self.rendering_light.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.rendering_light.Type = value

    def get_colour(self, o_colour: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetColor(CATSafeArrayVariant oColor)
                | 
                |     Returns the color of a light.
                |     The color is expressed with r, g, and b coefficients (between 0 and
                |     255)
                | 
                |     Parameters:
                | 
                |         oColor
                |             The color as a safe array made up of three doubles: r, g,
                |             b
                |             The array must be previously initialized.

        :param tuple o_colour:
        :rtype: None
        """
        return self.rendering_light.GetColor(o_colour)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_color'
        # # vba_code = """
        # # Public Function get_color(rendering_light)
        # #     Dim oColor (2)
        # #     rendering_light.GetColor oColor
        # #     get_color = oColor
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOrigin(CATSafeArrayVariant oOrigin)
                | 
                |     Returns the coordinates of the origin of the light.
                |     These coordinates are set as an array of 3 Variants (double type).

        :param tuple o_origin:
        :rtype: None
        """
        return self.rendering_light.GetOrigin(o_origin)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_origin'
        # # vba_code = """
        # # Public Function get_origin(rendering_light)
        # #     Dim oOrigin (2)
        # #     rendering_light.GetOrigin oOrigin
        # #     get_origin = oOrigin
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_shadow_colour(self, o_shadow_colour: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetShadowColor(CATSafeArrayVariant oShadowColor)
                | 
                |     Returns the color of a shadow.
                |     The color is expressed with r, g, and b coefficients (between 0 and
                |     255)
                | 
                |     Parameters:
                | 
                |         oColor
                |             The color as a safe array made up of three doubles: r, g,
                |             b
                |             The array must be previously initialized.

        :param tuple o_shadow_color:
        :rtype: None
        """
        return self.rendering_light.GetShadowColor(o_shadow_colour)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_shadow_color'
        # # vba_code = """
        # # Public Function get_shadow_color(rendering_light)
        # #     Dim oShadowColor (2)
        # #     rendering_light.GetShadowColor oShadowColor
        # #     get_shadow_color = oShadowColor
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_target(self, o_target: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTarget(CATSafeArrayVariant oTarget)
                | 
                |     Returns the coordinates of the target point of the light.
                |     These coordinates are set as an array of 3 Variants (double type).

        :param tuple o_target:
        :rtype: None
        """
        return self.rendering_light.GetTarget(o_target)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_target'
        # # vba_code = """
        # # Public Function get_target(rendering_light)
        # #     Dim oTarget (2)
        # #     rendering_light.GetTarget oTarget
        # #     get_target = oTarget
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_colour(self, i_colour: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutColor(CATSafeArrayVariant iColor)
                | 
                |     Sets the color of a light.
                |     The color is expressed with r, g, and b coefficients (between 0 and
                |     255)

        :param tuple i_colour:
        :rtype: None
        """
        return self.rendering_light.PutColor(i_colour)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_color'
        # # vba_code = """
        # # Public Function put_color(rendering_light)
        # #     Dim iColor (2)
        # #     rendering_light.PutColor iColor
        # #     put_color = iColor
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_origin(self, i_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutOrigin(CATSafeArrayVariant iOrigin)
                | 
                |     Sets the coordinates of the origin of the light.
                |     These coordinates are set as an array of 3 Variants (double
                |     type).
                | 
                |     Example:
                |         This example sets the origin of the MyLight light. to the point with
                |         coordinates (10, 25, 15).
                | 
                |          MyLight.PutOrigin Array(10, 25, 15)

        :param tuple i_origin:
        :rtype: None
        """
        return self.rendering_light.PutOrigin(i_origin)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_origin'
        # # vba_code = """
        # # Public Function put_origin(rendering_light)
        # #     Dim iOrigin (2)
        # #     rendering_light.PutOrigin iOrigin
        # #     put_origin = iOrigin
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_shadow_colour(self, i_shadow_colour: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutShadowColor(CATSafeArrayVariant iShadowColor)
                | 
                |     Sets the color of a shadow.
                |     The color is expressed with r, g, and b coefficients (between 0 and
                |     255)

        :param tuple i_shadow_color:
        :rtype: None
        """
        return self.rendering_light.PutShadowColor(i_shadow_colour)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_shadow_color'
        # # vba_code = """
        # # Public Function put_shadow_color(rendering_light)
        # #     Dim iShadowColor (2)
        # #     rendering_light.PutShadowColor iShadowColor
        # #     put_shadow_color = iShadowColor
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def put_target(self, i_target: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutTarget(CATSafeArrayVariant iTarget)
                | 
                |     Sets the coordinates of the target point of the light.
                |     These coordinates are set as an array of 3 Variants (double type).

        :param tuple i_target:
        :rtype: None
        """
        return self.rendering_light.PutTarget(i_target)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'put_target'
        # # vba_code = """
        # # Public Function put_target(rendering_light)
        # #     Dim iTarget (2)
        # #     rendering_light.PutTarget iTarget
        # #     put_target = iTarget
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'RenderingLight(name="{self.name}")'
