#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class RenderingEnvironmentWall(AnyObject):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RenderingEnvironmentWall
                | 
                | Represents a Environment object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rendering_environment_wall = com_object

    @property
    def active_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ActiveStatus() As short
                | 
                |     Returns or sets the environment wall active status. A wall is visible only
                |     when it is active.
                | 
                |         The active status can be:
                |         1: wall is visible
                |         0: wall is invisible

        :rtype: int
        """

        return self.rendering_environment_wall.ActiveStatus

    @active_status.setter
    def active_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_environment_wall.ActiveStatus = value

    @property
    def auto_scale_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AutoScaleStatus() As short
                | 
                |     Returns or sets the texture automatic scaling status. If status is
                |     automatic scaling, the texture fit is locked when the environment size is
                |     modified.
                | 
                |         The scaling status can be:
                |         1: automatic scaling is on
                |         0: automatic scaling is off

        :rtype: int
        """

        return self.rendering_environment_wall.AutoScaleStatus

    @auto_scale_status.setter
    def auto_scale_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_environment_wall.AutoScaleStatus = value

    @property
    def flip_u_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FlipUStatus() As short
                | 
                |     Returns or sets texture orientation status along the U
                |     axis.
                | 
                |         The flip status can be:
                |         1: texture is flipped along the U axis
                |         0: texture is not flipped along the U axis

        :rtype: int
        """

        return self.rendering_environment_wall.FlipUStatus

    @flip_u_status.setter
    def flip_u_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_environment_wall.FlipUStatus = value

    @property
    def flip_v_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FlipVStatus() As short
                | 
                |     Returns or sets texture orientation status along the V
                |     axis.
                | 
                |         The flip status can be:
                |         1: texture is flipped along the V axis
                |         0: texture is not flipped along the V axis

        :rtype: int
        """

        return self.rendering_environment_wall.FlipVStatus

    @flip_v_status.setter
    def flip_v_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_environment_wall.FlipVStatus = value

    @property
    def linked_scale_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property LinkedScaleStatus() As short
                | 
                |     Returns or sets the texture scaling link status. If scales are linked,
                |     modifying one scale will update the other keeping the ratio between U and V
                |     constant.
                | 
                |         The link status can be:
                |         1: U and V scales are linked
                |         0: U and V scales are not linked

        :rtype: int
        """

        return self.rendering_environment_wall.LinkedScaleStatus

    @linked_scale_status.setter
    def linked_scale_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_environment_wall.LinkedScaleStatus = value

    @property
    def rotation(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Rotation() As double
                | 
                |     Returns or sets the texture rotation angle (in degrees). The rotation
                |     values must be between -360 and 360 degrees.

        :rtype: float
        """

        return self.rendering_environment_wall.Rotation

    @rotation.setter
    def rotation(self, value: float):
        """
        :param float value:
        """

        self.rendering_environment_wall.Rotation = value

    @property
    def scale_u(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ScaleU() As double
                | 
                |     Returns or sets the texture scale along the U axis. The scale value should
                |     be > 0. Note that the modification of this parameter is useless if automatic
                |     scaling is enabled.

        :rtype: float
        """

        return self.rendering_environment_wall.ScaleU

    @scale_u.setter
    def scale_u(self, value: float):
        """
        :param float value:
        """

        self.rendering_environment_wall.ScaleU = value

    @property
    def scale_v(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ScaleV() As double
                | 
                |     Returns or sets the texture scale along the V axis. The scale value should
                |     be > 0. Note that the modification of this parameter is useless if automatic
                |     scaling is enabled.

        :rtype: float
        """

        return self.rendering_environment_wall.ScaleV

    @scale_v.setter
    def scale_v(self, value: float):
        """
        :param float value:
        """

        self.rendering_environment_wall.ScaleV = value

    @property
    def shadows_status(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ShadowsStatus() As short
                | 
                |     Returns or sets the wall shadow status. A wall may or may not be affected
                |     by lights depending on this status.
                | 
                |         The shadows status can be:
                |         1: wall is affected by active lights and can bear
                |         shadows
                |         0: wall is not affected by active lights and is always
                |         seen

        :rtype: int
        """

        return self.rendering_environment_wall.ShadowsStatus

    @shadows_status.setter
    def shadows_status(self, value: int):
        """
        :param int value:
        """

        self.rendering_environment_wall.ShadowsStatus = value

    @property
    def texture(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Texture() As CATBSTR
                | 
                |     Returns or sets the wall texture name. To remove the texture, use an empty
                |     string.

        :rtype: str
        """

        return self.rendering_environment_wall.Texture

    @texture.setter
    def texture(self, value: str):
        """
        :param str value:
        """

        self.rendering_environment_wall.Texture = value

    @property
    def translation_u(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TranslationU() As double
                | 
                |     Returns or sets the texture offset along the U axis. Note that this
                |     parameter is useless if automatic scaling is enabled.

        :rtype: float
        """

        return self.rendering_environment_wall.TranslationU

    @translation_u.setter
    def translation_u(self, value: float):
        """
        :param float value:
        """

        self.rendering_environment_wall.TranslationU = value

    @property
    def translation_v(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TranslationV() As double
                | 
                |     Returns or sets the texture offset along the V axis. Note that this
                |     parameter is useless if automatic scaling is enabled.

        :rtype: float
        """

        return self.rendering_environment_wall.TranslationV

    @translation_v.setter
    def translation_v(self, value: float):
        """
        :param float value:
        """

        self.rendering_environment_wall.TranslationV = value

    def fit_all_in_wall(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub FitAllInWall()
                | 
                |     If a texture is mapped on the wall, scale automatically the texture to fit
                |     inside the wall.

        :rtype: None
        """
        return self.rendering_environment_wall.FitAllInWall()

    def __repr__(self):
        return f'RenderingEnvironmentWall(name="{ self.name }")'
