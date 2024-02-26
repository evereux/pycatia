#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_rsc_interfaces.rendering_environment import RenderingEnvironment
from pycatia.cat_rsc_interfaces.rendering_light import RenderingLight
from pycatia.in_interfaces.camera_3d import Camera3D
from pycatia.system_interfaces.any_object import AnyObject


class RenderingShooting(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RenderingShooting
                | 
                | Represents a Material object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rendering_shooting = com_object

    @property
    def active_camera(self) -> Camera3D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveCamera() As Camera3D
                | 
                |     Returns or sets the active camera for shooting. A shooting can only have
                |     one active camera at a time.

        :rtype: Camera3D
        """

        return Camera3D(self.rendering_shooting.ActiveCamera)

    @active_camera.setter
    def active_camera(self, value: Camera3D):
        """
        :param Camera3D value:
        """

        self.rendering_shooting.ActiveCamera = value

    @property
    def active_environment(self) -> RenderingEnvironment:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveEnvironment() As RenderingEnvironment
                | 
                |     Returns or sets the active environment for shooting.
                |     A shooting can have one or zero active environment at a time.

        :rtype: RenderingEnvironment
        """

        return RenderingEnvironment(self.rendering_shooting.ActiveEnvironment)

    @active_environment.setter
    def active_environment(self, value: RenderingEnvironment):
        """
        :param RenderingEnvironment value:
        """

        self.rendering_shooting.ActiveEnvironment = value

    @property
    def ambient_factor(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AmbientFactor() As short
                | 
                |     Returns or sets amount of ambient used for indirect illumination (final
                |     gathering or global illumination).
                |     The ambient factor can be:
                |     1: Ambient is taken into account
                |     0: No ambient used

        :rtype: int
        """

        return self.rendering_shooting.AmbientFactor

    @ambient_factor.setter
    def ambient_factor(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.AmbientFactor = value

    @property
    def antialiasing_contrast(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AntialiasingContrast() As short
                | 
                |     Returns or sets the antialiasing contrast threshold value.
                |     This value ranges from 0. to 100.%. Contrast value sets the contrast
                |     threshold for adaptative oversampling, that is, the maximum contrast threshold
                |     between pixels, below which no oversampling will be done.
                |     If the contrast of any RGB component between the currently calculated pixel
                |     and heighboring pixels weighted by their sum is greater than this threshold,
                |     the pixel is oversampled.

        :rtype: int
        """

        return self.rendering_shooting.AntialiasingContrast

    @antialiasing_contrast.setter
    def antialiasing_contrast(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.AntialiasingContrast = value

    @property
    def antialiasing_max_sample(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AntialiasingMaxSample() As short
                | 
                |     Returns or sets the antialiasing maximum sample number for image
                |     computation.
                |     This value ranges from 0/code> to 5/code>.
                |     Maximum samples value sets the minimum number of rays casted for 1,4 or 16
                |     pixels.
                | 
                |         The possible maximum sample number are:
                |         0 : 1 ray casted for a 4x4 pixel square
                |         1 : 1 ray casted for a 2x2 pixel square
                |         2 : 1 ray casted per pixel
                |         3 : 4 rays casted per pixel
                |         4 : 16 rays casted per pixel
                |         5 : 64 rays casted per pixel

        :rtype: int
        """

        return self.rendering_shooting.AntialiasingMaxSample

    @antialiasing_max_sample.setter
    def antialiasing_max_sample(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.AntialiasingMaxSample = value

    @property
    def antialiasing_min_sample(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AntialiasingMinSample() As short
                | 
                |     Returns or sets the antialiasing minimum sample number for image
                |     computation.
                |     This value ranges from 0/code> to 5/code>.
                |     Minimum samples value sets the minimum number of rays casted for 1,4 or 16
                |     pixels.
                | 
                |         The possible minimum sample number are:
                |         0 : 1 ray casted for a 4x4 pixel square
                |         1 : 1 ray casted for a 2x2 pixel square
                |         2 : 1 ray casted per pixel
                |         3 : 4 rays casted per pixel
                |         4 : 16 rays casted per pixel
                |         5 : 64 rays casted per pixel

        :rtype: int
        """

        return self.rendering_shooting.AntialiasingMinSample

    @antialiasing_min_sample.setter
    def antialiasing_min_sample(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.AntialiasingMinSample = value

    @property
    def cartoon_contour_thickness(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CartoonContourThickness() As double
                | 
                |     Returns or sets the cartoon contour thickness.
                |     The line thickness is given as image size percentage.
                |     The line thickness ranges from 0.0 (none) to 100.0.

        :rtype: float
        """

        return self.rendering_shooting.CartoonContourThickness

    @cartoon_contour_thickness.setter
    def cartoon_contour_thickness(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.CartoonContourThickness = value

    @property
    def cartoon_shading_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CartoonShadingStatus() As short
                | 
                |     Returns or sets the cartoon shading status of shooting.
                |     This status defines if the cartoon shading is activated or
                |     not.
                |     If shading is deactivated, only contours are rendered.
                |     The cartoon shading effect status can be:
                |     1: Shading status is active
                |     0: Shading status is deactivated

        :rtype: int
        """

        return self.rendering_shooting.CartoonShadingStatus

    @cartoon_shading_status.setter
    def cartoon_shading_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.CartoonShadingStatus = value

    @property
    def cartoon_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CartoonStatus() As short
                | 
                |     Returns or sets the cartoon status of shooting.
                |     This status defines if the cartoon rendering is activated or
                |     not.
                |     The cartoon effect status can be:
                |     1: Cartoon status is active
                |     0: Cartoon status is deactivated

        :rtype: int
        """

        return self.rendering_shooting.CartoonStatus

    @cartoon_status.setter
    def cartoon_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.CartoonStatus = value

    @property
    def cartoon_stroke_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CartoonStrokeStatus() As short
                | 
                |     Returns or sets the cartoon stroke status of shooting.
                |     This status defines if the cartoon stroke effect (ink pen effect) is
                |     activated or not.
                |     The stroke status can be:
                |     1: Stroke status is active
                |     0: Stroke status is deactivated

        :rtype: int
        """

        return self.rendering_shooting.CartoonStrokeStatus

    @cartoon_stroke_status.setter
    def cartoon_stroke_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.CartoonStrokeStatus = value

    @property
    def caustic_accuracy(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CausticAccuracy() As short
                | 
                |     Returns or sets the number of photons to use when estimating radiance for
                |     caustics.

        :rtype: int
        """

        return self.rendering_shooting.CausticAccuracy

    @caustic_accuracy.setter
    def caustic_accuracy(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.CausticAccuracy = value

    @property
    def caustic_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CausticRadius() As double
                | 
                |     Returns or sets the maximum distance in which photons for caustics are
                |     located.
                |     If the value is 0.0 an estimate based on the scene extent will be used.

        :rtype: float
        """

        return self.rendering_shooting.CausticRadius

    @caustic_radius.setter
    def caustic_radius(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.CausticRadius = value

    @property
    def caustic_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CausticStatus() As short
                | 
                |     Returns or sets the caustic status of shooting.
                |     This status defines if caustics are calculated or not.
                |     The caustic status can be:
                |     1: Caustics are enabled
                |     0: Caustics are disabled

        :rtype: int
        """

        return self.rendering_shooting.CausticStatus

    @caustic_status.setter
    def caustic_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.CausticStatus = value

    @property
    def depth_of_field_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DepthOfFieldRadius() As double
                | 
                |     Returns or sets the depth of field radius of confusion.
                |     The radius of confusion ranges from 1.0 to 10.0%.

        :rtype: float
        """

        return self.rendering_shooting.DepthOfFieldRadius

    @depth_of_field_radius.setter
    def depth_of_field_radius(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.DepthOfFieldRadius = value

    @property
    def depth_of_field_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DepthOfFieldStatus() As short
                | 
                |     Returns or sets the depth of field status of shooting. This status defines
                |     if depth of field effect is activated or not.
                |     The depth of field status can be:
                |     1: Depth of field is active
                |     0: Depth of field is deactivated

        :rtype: int
        """

        return self.rendering_shooting.DepthOfFieldStatus

    @depth_of_field_status.setter
    def depth_of_field_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.DepthOfFieldStatus = value

    @property
    def final_gathering_accuracy(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FinalGatheringAccuracy() As short
                | 
                |     Returns or sets the number of rays shot in each final gather.

        :rtype: int
        """

        return self.rendering_shooting.FinalGatheringAccuracy

    @final_gathering_accuracy.setter
    def final_gathering_accuracy(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.FinalGatheringAccuracy = value

    @property
    def final_gathering_max_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FinalGatheringMaxRadius() As double
                | 
                |     Returns or sets the maximum distance in which a final gather result can be
                |     used.
                |     If the value is 0.0 an estimate based on the scene extent will be used.

        :rtype: float
        """

        return self.rendering_shooting.FinalGatheringMaxRadius

    @final_gathering_max_radius.setter
    def final_gathering_max_radius(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.FinalGatheringMaxRadius = value

    @property
    def final_gathering_min_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FinalGatheringMinRadius() As double
                | 
                |     Returns or sets the minimum distance in which a final gather result can be
                |     used.
                |     If the value is 0.0 it will be set to 10% of maximum distance.

        :rtype: float
        """

        return self.rendering_shooting.FinalGatheringMinRadius

    @final_gathering_min_radius.setter
    def final_gathering_min_radius(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.FinalGatheringMinRadius = value

    @property
    def final_gathering_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FinalGatheringStatus() As short
                | 
                |     Returns or sets the final gathering status of shooting.
                |     This status defines if final gathering is activated or
                |     not.
                |     The final gathering status can be:
                |     1: Final gathering is enabled
                |     0: Final gathering is disabled

        :rtype: int
        """

        return self.rendering_shooting.FinalGatheringStatus

    @final_gathering_status.setter
    def final_gathering_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.FinalGatheringStatus = value

    @property
    def global_illumination_accuracy(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlobalIlluminationAccuracy() As short
                | 
                |     Returns or sets the number of photons to use when estimating radiance for
                |     global illumination.

        :rtype: int
        """

        return self.rendering_shooting.GlobalIlluminationAccuracy

    @global_illumination_accuracy.setter
    def global_illumination_accuracy(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.GlobalIlluminationAccuracy = value

    @property
    def global_illumination_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlobalIlluminationRadius() As double
                | 
                |     Returns or sets the maximum distance in which photons for global
                |     illumination are located.
                |     If the value is 0.0 an estimate based on the scene extent will be used.

        :rtype: float
        """

        return self.rendering_shooting.GlobalIlluminationRadius

    @global_illumination_radius.setter
    def global_illumination_radius(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.GlobalIlluminationRadius = value

    @property
    def global_illumination_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlobalIlluminationStatus() As short
                | 
                |     Returns or sets the global illumination status of
                |     shooting.
                |     This status defines if global illumination is used or not.
                |     The global illumination status can be:
                |     1: Global illumination is enabled
                |     0: Global illumination is disabled

        :rtype: int
        """

        return self.rendering_shooting.GlobalIlluminationStatus

    @global_illumination_status.setter
    def global_illumination_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.GlobalIlluminationStatus = value

    @property
    def glow_flare_diffusion(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlowFlareDiffusion() As double
                | 
                |     Returns or sets the glow flare diffusion.
                |     The flare diffusion value ranges from 0.0 to 1.0%.

        :rtype: float
        """

        return self.rendering_shooting.GlowFlareDiffusion

    @glow_flare_diffusion.setter
    def glow_flare_diffusion(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.GlowFlareDiffusion = value

    @property
    def glow_flare_factor(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlowFlareFactor() As double
                | 
                |     Returns or sets the glow flare factor.
                |     The flare factor ranges from 0.0 to 1.0%.

        :rtype: float
        """

        return self.rendering_shooting.GlowFlareFactor

    @glow_flare_factor.setter
    def glow_flare_factor(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.GlowFlareFactor = value

    @property
    def glow_intensity(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlowIntensity() As double
                | 
                |     Returns or sets the glow intensity factor.
                |     The glow intensity factor ranges from 1.0 to 10.0%.

        :rtype: float
        """

        return self.rendering_shooting.GlowIntensity

    @glow_intensity.setter
    def glow_intensity(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.GlowIntensity = value

    @property
    def glow_radial_line_size(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlowRadialLineSize() As double
                | 
                |     Returns or sets the glow radial lines size.
                |     The lines size ranges from 0.0 (none) to 1.0 (max length).

        :rtype: float
        """

        return self.rendering_shooting.GlowRadialLineSize

    @glow_radial_line_size.setter
    def glow_radial_line_size(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.GlowRadialLineSize = value

    @property
    def glow_size(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlowSize() As double
                | 
                |     Returns or sets the glow filter size in percentage of image
                |     size.
                |     The filter size ranges from 0.1 to 1.0%.

        :rtype: float
        """

        return self.rendering_shooting.GlowSize

    @glow_size.setter
    def glow_size(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.GlowSize = value

    @property
    def glow_star_effect(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlowStarEffect() As double
                | 
                |     Returns or sets the glow star effect.
                |     The effect coefficient ranges from 0.0 (random star) to 1.0 (cross).

        :rtype: float
        """

        return self.rendering_shooting.GlowStarEffect

    @glow_star_effect.setter
    def glow_star_effect(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.GlowStarEffect = value

    @property
    def glow_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlowStatus() As short
                | 
                |     Returns or sets the glow status of shooting. This status defines if the
                |     glow effect is activated or not.
                |     The glow status can be:
                |     1: Glow is active
                |     0: Glow is deactivated

        :rtype: int
        """

        return self.rendering_shooting.GlowStatus

    @glow_status.setter
    def glow_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.GlowStatus = value

    @property
    def glow_threshold(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property GlowThreshold() As double
                | 
                |     Returns or sets the glow color threshold.
                |     The color threshold ranges from 0.5 to 1.5%.

        :rtype: float
        """

        return self.rendering_shooting.GlowThreshold

    @glow_threshold.setter
    def glow_threshold(self, value: float):
        """
        :param float value:
        """

        self.rendering_shooting.GlowThreshold = value

    @property
    def image_height(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImageHeight() As short
                | 
                |     Returns or sets the image height for shooting.
                |     The image height ranges from 10 to 8000 pixels.

        :rtype: int
        """

        return self.rendering_shooting.ImageHeight

    @image_height.setter
    def image_height(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.ImageHeight = value

    @property
    def image_output_directory(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImageOutputDirectory() As CATBSTR
                | 
                |     Returns or sets the output directory for image.
                |     This is the place where rendered images are saved.

        :rtype: str
        """

        return self.rendering_shooting.ImageOutputDirectory

    @image_output_directory.setter
    def image_output_directory(self, value: str):
        """
        :param str value:
        """

        self.rendering_shooting.ImageOutputDirectory = value

    @property
    def image_output_format(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImageOutputFormat() As short
                | 
                |     Returns or sets the file type used for saved image.
                | 
                |         Possible format types
                |         1 TIFF True Color (\\*.tif)
                |         2 TIFF True Color Packbits (\\*.tif)
                |         3 SGI Format (\\*.rgb)
                |         4 Windows Bitmap (\\*.bmp)
                |         5 JPEG Fair Quality (\\*.jpg)
                |         6 JPEG Medium Quality (\\*.jpg)
                |         7 JPEG High Quality (\\*.jpg)
                |         8 Apple Macintosh Format (\\*.pic)
                |         9 Adobe Photoshop Format (\\*.psd)
                |         10 Portable Network Graphics (\\*.png)
                |         11 Truevision Targa (\\*.tga)

        :rtype: int
        """

        return self.rendering_shooting.ImageOutputFormat

    @image_output_format.setter
    def image_output_format(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.ImageOutputFormat = value

    @property
    def image_output_name(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImageOutputName() As CATBSTR
                | 
                |     Returns or sets the output name for image (extension
                |     excluded).
                |     This is the name of saved files (with no extension).

        :rtype: str
        """

        return self.rendering_shooting.ImageOutputName

    @image_output_name.setter
    def image_output_name(self, value: str):
        """
        :param str value:
        """

        self.rendering_shooting.ImageOutputName = value

    @property
    def image_output_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImageOutputType() As short
                | 
                |     Returns or sets the image output location.
                | 
                |         Output types
                |         1 On screen
                |         2 On disk

        :rtype: int
        """

        return self.rendering_shooting.ImageOutputType

    @image_output_type.setter
    def image_output_type(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.ImageOutputType = value

    @property
    def image_predefined_ratio(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImagePredefinedRatio() As short
                | 
                |     Returns or sets the image height for shooting.
                |     Sets the image ratio to a standard predefined value. The image size keeps
                |     the same height and the image length is recalculated.
                | 
                |         Possible predefined ratio. 0 no predefined ratio
                |         1 0.708333 (A4)
                |         2 1.0 (6 x 6)
                |         3 1.25 (Standard)
                |         4 1.333333 (4 / 3)
                |         5 1.5 (24 x 36)
                |         6 1.687331 (16 mm.)
                |         7 1.777777 (16 / 9)
                |         8 1.855072 (HDTV)
                |         9 2.2 (Panavision)
                |         10 3.0 (Panorama)
                |         11 1.32 (CCD 1/2")
                |         12 1.333333 (CCD 1/4")

        :rtype: int
        """

        return self.rendering_shooting.ImagePredefinedRatio

    @image_predefined_ratio.setter
    def image_predefined_ratio(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.ImagePredefinedRatio = value

    @property
    def image_width(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ImageWidth() As short
                | 
                |     Returns or sets the image width for shooting.
                |     The image width ranges from 10 to 8000 pixels.

        :rtype: int
        """

        return self.rendering_shooting.ImageWidth

    @image_width.setter
    def image_width(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.ImageWidth = value

    @property
    def raytracing_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RaytracingStatus() As short
                | 
                |     Returns or sets the the raytracing status for shooting.
                |     The raytracing status can be:
                |     1: Raytracing is active
                |     0: Raytracing is deactivated

        :rtype: int
        """

        return self.rendering_shooting.RaytracingStatus

    @raytracing_status.setter
    def raytracing_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.RaytracingStatus = value

    @property
    def rebounds_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReboundsCount() As short
                | 
                |     Returns or sets the maximum number of rebounds levels to take into account
                |     for image computation.
                |     This number ranges from 0 to 18 levels.

        :rtype: int
        """

        return self.rendering_shooting.ReboundsCount

    @rebounds_count.setter
    def rebounds_count(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.ReboundsCount = value

    @property
    def reflections_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReflectionsCount() As short
                | 
                |     Returns or sets the maximum number of reflections levels to take into
                |     account for image computation.
                |     This number ranges from 0 to 9 levels.

        :rtype: int
        """

        return self.rendering_shooting.ReflectionsCount

    @reflections_count.setter
    def reflections_count(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.ReflectionsCount = value

    @property
    def refractions_count(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RefractionsCount() As short
                | 
                |     Returns or sets the maximum number of refractions levels to take into
                |     account for image computation.
                |     This number ranges from 0 to 9 levels.

        :rtype: int
        """

        return self.rendering_shooting.RefractionsCount

    @refractions_count.setter
    def refractions_count(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.RefractionsCount = value

    @property
    def shadows_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShadowsStatus() As short
                | 
                |     Returns or sets the shadows status of shooting. This status defines if
                |     shadows are calculated or not.
                |     The shadows status can be:
                |     1: Shadows on
                |     0: Shadows off

        :rtype: int
        """

        return self.rendering_shooting.ShadowsStatus

    @shadows_status.setter
    def shadows_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.ShadowsStatus = value

    @property
    def textures_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TexturesStatus() As short
                | 
                |     Returns or sets the textures status of shooting. This status defines if
                |     textures are taken into account for image computation.
                |     The texture status can be:
                |     1: Textures are taking into account
                |     0: Textures are ignored

        :rtype: int
        """

        return self.rendering_shooting.TexturesStatus

    @textures_status.setter
    def textures_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_shooting.TexturesStatus = value

    def add_active_light(self, i_active_light: RenderingLight) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddActiveLight(RenderingLight iActiveLight)
                | 
                |     Adds a new active light to the shooting active lights list.

        :param RenderingLight i_active_light:
        :rtype: None
        """
        return self.rendering_shooting.AddActiveLight(i_active_light.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_active_light'
        # # vba_code = """
        # # Public Function add_active_light(rendering_shooting)
        # #     Dim iActiveLight (2)
        # #     rendering_shooting.AddActiveLight iActiveLight
        # #     add_active_light = iActiveLight
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def count_active_lights(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CountActiveLights() As short
                | 
                |     Returns the number of active light for the shooting.

        :rtype: int
        """
        return self.rendering_shooting.CountActiveLights()

    def get_active_light(self, i_index: int) -> RenderingLight:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetActiveLight(short iIndex) As RenderingLight
                | 
                |     Returns the active light of the shooting using its index.

        :param int i_index:
        :rtype: RenderingLight
        """
        return RenderingLight(self.rendering_shooting.GetActiveLight(i_index))

    def remove_active_light(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveActiveLight(short iIndex)
                | 
                |     Removes a light from the shootings active lights list.

        :param int i_index:
        :rtype: None
        """
        return self.rendering_shooting.RemoveActiveLight(i_index)

    def render(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Render()
                | 
                |     Render the shooting
                |     Caution: Product involved in rendering calculation should not be closed
                |     before the end of computation. If product is closed, calculation is
                |     interrupted.

        :rtype: None
        """
        return self.rendering_shooting.Render()

    def __repr__(self):
        return f'RenderingShooting(name="{self.name}")'
