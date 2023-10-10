#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.exception_handling.exceptions import CATIAApplicationException
from pycatia.system_interfaces.any_object import AnyObject


class RenderingMaterial(AnyObject):
    """
    .. note::
        :class: toggle

        CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

            | System.IUnknown
            |     System.IDispatch
            |         System.CATBaseUnknown
            |             System.CATBaseDispatch
            |                 System.AnyObject
            |                     RenderingMaterial
            |
            | Represents an RenderingMaterial object.
            | This object is used to manage the Rendering properties of a
            | material.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rendering_material = com_object

    @property
    def adaptive_coeff(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AdaptiveCoeff() As short
                |
                |     Returns or sets the adaptive coefficient of a material. Adaptive coefficient
                |     value is between 1 an 8.

        :return: int
        :rtype: int
        """
        return self.rendering_material.AdaptiveCoeff

    @adaptive_coeff.setter
    def adaptive_coeff(self, value: int):
        """
        :param int value:
        """
        min_ = 1
        max_ = 8

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.AdaptiveCoeff = value

    @property
    def ambient_coefficient(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AmbientCoefficient() As double
                |
                |     Returns or sets the ambient coefficient of a material. Ambient coefficient
                |     value is between 0 to 1.

        :return: float
        :rtype: float
        """
        return self.rendering_material.AmbientCoefficient

    @ambient_coefficient.setter
    def ambient_coefficient(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 1

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.AmbientCoefficient = value

    @property
    def bump(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Bump() As double
                |
                |     Returns or sets the texture bump. Image texture bump value is between -10
                |     to 10.

        :return: float
        :rtype: float
        """
        return self.rendering_material.Bump

    @bump.setter
    def bump(self, value: float):
        """
        :param float value:
        """

        min_ = -10
        max_ = 10

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.Bump = value

    @property
    def chessboard_joint_height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ChessboardJointHeight() As double
                |
                |     Returns or sets the height of the join of a chessboard texture. Height
                |     value is between 0 to 100. N.B. Parameter use for CHESSBOARD texture type only.

        :return: float
        :rtype: float
        """
        return self.rendering_material.ChessboardJointHeight

    @chessboard_joint_height.setter
    def chessboard_joint_height(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 100

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.ChessboardJointHeight = value

    @property
    def chessboard_joint_width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ChessboardJointWidth() As double
                |
                |     Returns or sets the width of the join of a chessboard texture. Width value
                |     is between 0 to 100. N.B. Parameter use for CHESSBOARD texture type only.

        :return: float
        :rtype: float
        """
        return self.rendering_material.ChessboardJointWidth

    @chessboard_joint_width.setter
    def chessboard_joint_width(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 100

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.ChessboardJointWidth = value

    @property
    def chessboard_offset(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ChessboardOffset() As double
                |
                |     Returns or sets the offset coefficient for a chessboard texture. It
                |     indicates the offset between each line of the chessboard texture. Offset value
                |     is between 0 to 0.5. N.B. Parameter use for CHESSBOARD texture type only.

        :return: float
        :rtype: float
        """

        return self.rendering_material.ChessboardOffset

    @chessboard_offset.setter
    def chessboard_offset(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 0.5

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.ChessboardOffset = value

    @property
    def chessboard_tile_height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ChessboardTileHeight() As double
                |
                |     Returns or sets the height of the tile of a chessboard texture. Height
                |     value is between 0 to 100. N.B. Parameter use for CHESSBOARD texture type only.

        :return: float
        :rtype: float
        """

        return self.rendering_material.ChessboardTileHeight

    @chessboard_tile_height.setter
    def chessboard_tile_height(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 100

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.ChessboardTileHeight = value

    @property
    def chessboard_tile_width(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ChessboardTileWidth() As double
                |
                |     Returns or sets the width of the tile of a chessboard texture. Width value
                |     is between 0 to 100. N.B. Parameter use for CHESSBOARD texture type only.

        :return: float
        :rtype: float
        """

        return self.rendering_material.ChessboardTileWidth

    @chessboard_tile_width.setter
    def chessboard_tile_width(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 100

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.ChessboardTileWidth = value

    @property
    def color_number(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ColorNumber() As short
                |
                |     Returns or sets the 3d texture color number. Possible color numbers are: -
                |     From 2 to 5 for marble, vein and chessboard texture types - From 1 to 5 for
                |     alternate vein texture types N.B. Parameter useless for ROCK textures (color
                |     number is fixed) and IMAGE texture

        :return: int
        :rtype: int
        """

        return self.rendering_material.ColorNumber

    @color_number.setter
    def color_number(self, value: int):
        """
        :param int value:
        """

        self.rendering_material.ColorNumber = value

    @property
    def diffuse_coefficient(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property DiffuseCoefficient() As double
                |
                |     Returns or sets the diffuse coefficient of a material. Diffuse coefficient
                |     value is between 0 to 1.

        :return: float
        :rtype: float
        """

        return self.rendering_material.DiffuseCoefficient

    @diffuse_coefficient.setter
    def diffuse_coefficient(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 1

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.DiffuseCoefficient = value

    @property
    def environment_image(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EnvironmentImage() As CATBSTR
                |
                |     Returns or sets the environment image pathname of a material.

        :return: str
        :rtype: str
        """

        return self.rendering_material.EnvironmentImage

    @environment_image.setter
    def environment_image(self, value: str):
        """
        :param str value:
        """

        self.rendering_material.EnvironmentImage = value

    @property
    def flip_u(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FlipU() As boolean
                |
                |     Returns or sets the texture flip status along U axis. N.B. Parameter use
                |     for IMAGE texture type only

        :return: bool
        :rtype: bool
        """

        return self.rendering_material.FlipU

    @flip_u.setter
    def flip_u(self, value: bool):
        """
        :param bool value:
        """

        self.rendering_material.FlipU = value

    @property
    def flip_v(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property FlipV() As boolean
                |
                |     Returns or sets the texture flip status along V axis. N.B. Parameter use
                |     for IMAGE texture type only

        :return: bool
        :rtype: bool
        """

        return self.rendering_material.FlipV

    @flip_v.setter
    def flip_v(self, value: bool):
        """
        :param bool value:
        """

        self.rendering_material.FlipV = value

    @property
    def mapping_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property MappingType() As short
                |
                |     Returns or sets the mapping type of a material.
                |
                |         Possible types are:
                |         0: Planar mapping
                |         1: Spherical mapping
                |         2: Cylindrical mapping
                |         3: Cubical mapping
                |         4: Auto mapping
                |         5: Manual mapping

        :return: int
        :rtype: int
        """

        return self.rendering_material.MappingType

    @mapping_type.setter
    def mapping_type(self, value: int):
        """
        :param int value:
        """

        min_ = 0
        max_ = 5

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.MappingType = value

    @property
    def orientation(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Orientation() As double
                |
                |     Returns or sets the texture orientation. Orientation value should be
                |     between -360 to +360 degrees N.B. Parameter use for IMAGE texture type only

        :return: float
        :rtype: float
        """

        return self.rendering_material.Orientation

    @orientation.setter
    def orientation(self, value: float):
        """
        :param float value:
        """

        min_ = -360
        max_ = 360

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.Orientation = value

    @property
    def position_u(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PositionU() As double
                |
                |     Returns or sets the texture position along U axis. N.B. Parameter use for
                |     IMAGE texture type only

        :return: float
        :rtype: float
        """

        return self.rendering_material.PositionU

    @position_u.setter
    def position_u(self, value: float):
        """
        :param float value:
        """

        self.rendering_material.PositionU = value

    @property
    def position_v(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PositionV() As double
                |
                |     Returns or sets the texture position along V axis. N.B. Parameter use for
                |     IMAGE texture type only

        :return: float
        :rtype: float
        """

        return self.rendering_material.PositionV

    @position_v.setter
    def position_v(self, value: float):
        """
        :param float value:
        """

        self.rendering_material.PositionV = value

    @property
    def preview_size(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property PreviewSize() As double
                |
                |     Returns or sets the preview size of a material. Preview size value is 0.1mm
                |     minimum.

        :return: float
        :rtype: float
        """

        return self.rendering_material.PreviewSize

    @preview_size.setter
    def preview_size(self, value: float):
        """
        :param float value:
        """

        self.rendering_material.PreviewSize = value

    @property
    def reflection_height(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReflectionHeight() As double
                |
                |     Returns or sets the non-linear reflection height of a material. Non-linear
                |     reflection height value is between 0 to 1. N.B. Parameter use for CUSTOM
                |     reflection mode only.

        :return: float
        :rtype: float
        """

        return self.rendering_material.ReflectionHeight

    @reflection_height.setter
    def reflection_height(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 1

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.ReflectionHeight = value

    @property
    def reflection_length(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReflectionLength() As double
                |
                |     Returns or sets the non-linear reflection length of a material. Non-linear
                |     reflection length value is between 0 to 1. N.B. Parameter use for CUSTOM
                |     reflection mode only.

        :return: float
        :rtype: float
        """

        return self.rendering_material.ReflectionLength

    @reflection_length.setter
    def reflection_length(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 1

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.ReflectionLength = value

    @property
    def reflection_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReflectionMode() As short
                |
                |     Returns or sets the non-linear reflection mode of a
                |     material.
                |
                |         Possible reflection mode values are:
                |         0: CHROMA reflection mode
                |         1: PAINT reflection mode
                |         2: MATTE_METAL reflection mode
                |         3: BRIGHT_PLASTIC reflection mode
                |         4: CUSTOM reflection mode

        :return: int
        :rtype: int
        """

        return self.rendering_material.ReflectionMode

    @reflection_mode.setter
    def reflection_mode(self, value: int):
        """
        :param int value:
        """

        min_ = 0
        max_ = 4

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.ReflectionMode = value

    @property
    def reflectivity_coefficient(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ReflectivityCoefficient() As double
                |
                |     Returns or sets the reflectivity coefficient of a material. Reflectivity
                |     coefficient value is between 0 to 1.

        :return: float
        :rtype: float
        """

        return self.rendering_material.ReflectivityCoefficient

    @reflectivity_coefficient.setter
    def reflectivity_coefficient(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 1

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.ReflectivityCoefficient = value

    @property
    def refraction_coefficient(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RefractionCoefficient() As double
                |
                |     Returns or sets the refraction coefficient of a material. Refraction
                |     coefficient value is between 1 to 2.

        :return: float
        :rtype: float
        """

        return self.rendering_material.RefractionCoefficient

    @refraction_coefficient.setter
    def refraction_coefficient(self, value: float):
        """
        :param float value:
        """

        min_ = 1
        max_ = 2

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.RefractionCoefficient = value

    @property
    def repeat_u(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RepeatU() As boolean
                |
                |     Returns or sets the texture repeat status along U axis. N.B. Parameter use
                |     for IMAGE texture type only

        :return: bool
        :rtype: bool
        """

        return self.rendering_material.RepeatU

    @repeat_u.setter
    def repeat_u(self, value: bool):
        """
        :param bool value:
        """

        self.rendering_material.RepeatU = value

    @property
    def repeat_v(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property RepeatV() As boolean
                |
                |     Returns or sets the texture repeat status along V axis. N.B. Parameter use
                |     for IMAGE texture type only

        :return: bool
        :rtype: bool
        """

        return self.rendering_material.RepeatV

    @repeat_v.setter
    def repeat_v(self, value: bool):
        """
        :param bool value:
        """

        self.rendering_material.RepeatV = value

    @property
    def scale_u(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ScaleU() As double
                |
                |     Returns or sets the texture scale along U axis. U scale value is between 0
                |     to 100. N.B. Parameter use for IMAGE texture type only

        :return: float
        :rtype: float
        """

        return self.rendering_material.ScaleU

    @scale_u.setter
    def scale_u(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 100

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.ScaleU = value

    @property
    def scale_v(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ScaleV() As double
                |
                |     Returns or sets the texture scale along V axis. V scale value is between 0
                |     to 100. N.B. Parameter use for IMAGE texture type only

        :return: float
        :rtype: float
        """

        return self.rendering_material.ScaleV

    @scale_v.setter
    def scale_v(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 100

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.ScaleV = value

    @property
    def specular_coefficient(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SpecularCoefficient() As double
                |
                |     Returns or sets the specular coefficient of a material. Specular
                |     coefficient value is between 0 to 1.

        :return: float
        :rtype: float
        """

        return self.rendering_material.SpecularCoefficient

    @specular_coefficient.setter
    def specular_coefficient(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 1

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.SpecularCoefficient = value

    @property
    def specular_exponent(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SpecularExponent() As double
                |
                |     Returns or sets the specular exponent of a material. Specular exponent
                |     value is between 0 to 1.

        :return: float
        :rtype: float
        """

        return self.rendering_material.SpecularExponent

    @specular_exponent.setter
    def specular_exponent(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 1

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.SpecularExponent = value

    @property
    def texture_amplitude(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TextureAmplitude() As double
                |
                |     Returns or sets the 3d texture amplitude coefficient. Amplitude value is
                |     between 0 to 1. N.B. Parameter use for MARBLE and ROCK texture type only.

        :return: float
        :rtype: float
        """

        return self.rendering_material.TextureAmplitude

    @texture_amplitude.setter
    def texture_amplitude(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 1

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.TextureAmplitude = value

    @property
    def texture_complexity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TextureComplexity() As short
                |
                |     Returns or sets the 3d texture complexity. Complexity value is between 0 to
                |     10. N.B. Parameter use for MARBLE and ROCK texture types only.

        :return: int
        :rtype: int
        """

        return self.rendering_material.TextureComplexity

    @texture_complexity.setter
    def texture_complexity(self, value: int):
        """
        :param int value:
        """

        min_ = 0
        max_ = 10

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.TextureComplexity = value

    @property
    def texture_gain(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TextureGain() As double
                |
                |     Returns or sets the 3d texture gain coefficient. Gain value is between 0 to
                |     2. N.B. Parameter use for ROCK texture type only.

        :return: float
        :rtype: float
        """

        return self.rendering_material.TextureGain

    @texture_gain.setter
    def texture_gain(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 2

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.TextureGain = value

    @property
    def texture_image(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TextureImage() As CATBSTR
                |
                |     Returns or sets the texture image pathname of a material. N.B. Parameter
                |     use for IMAGE texture type only

        :return: str
        :rtype: str
        """

        return self.rendering_material.TextureImage

    @texture_image.setter
    def texture_image(self, value: str):
        """
        :param str value:
        """

        self.rendering_material.TextureImage = value

    @property
    def texture_perturbation(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TexturePerturbation() As double
                |
                |     Returns or sets the 3d texture perturbation coefficient. Perturbation value
                |     is between 1 to 10. N.B. Parameter use for VEIN, ALTERNATE VEIN and ROCK
                |     texture types only.

        :return: float
        :rtype: float
        """

        return self.rendering_material.TexturePerturbation

    @texture_perturbation.setter
    def texture_perturbation(self, value: float):
        """
        :param float value:
        """

        min_ = 10
        max_ = 10

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.TexturePerturbation = value

    @property
    def texture_turbulence(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TextureTurbulence() As boolean
                |
                |     Returns or sets the 3d texture turbulence status. N.B. Parameter use for
                |     ROCK texture type only.

        :return: bool
        :rtype: bool
        """

        return self.rendering_material.TextureTurbulence

    @texture_turbulence.setter
    def texture_turbulence(self, value: bool):
        """
        :param bool value:
        """

        self.rendering_material.TextureTurbulence = value

    @property
    def texture_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TextureType() As short
                |
                |     Returns or sets the texture type of a material. The possible values for
                |     this type can be:
                |
                |         Possible reflection mode values are:
                |         0: NO texture
                |         1: IMAGE texture
                |         2: MARBLE texture
                |         3: VEIN texture
                |         4: ALTERNATE VEIN texture
                |         5: ROCK texture
                |         6: CHESSBOARD texture

        :return: int
        :rtype: int
        """

        return self.rendering_material.TextureType

    @texture_type.setter
    def texture_type(self, value: int):
        """
        :param int value:
        """

        min_ = 0
        max_ = 6

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.TextureType = value

    @property
    def texture_vein_amplitude(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TextureVeinAmplitude() As double
                |
                |     Returns or sets the 3d texture vein amplitude coefficient. Amplitude value
                |     is between 0 to 10. N.B. Parameter use for VEIN and ALTERNATE VEIN texture
                |     types only.

        :return: float
        :rtype: float
        """

        return self.rendering_material.TextureVeinAmplitude

    @texture_vein_amplitude.setter
    def texture_vein_amplitude(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 10

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.TextureVeinAmplitude = value

    @property
    def transparency_coefficient(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TransparencyCoefficient() As double
                |
                |     Returns or sets the transparency coefficient of a material. Transparency
                |     coefficient value is between 0 to 1.

        :return: float
        :rtype: float
        """

        return self.rendering_material.TransparencyCoefficient

    @transparency_coefficient.setter
    def transparency_coefficient(self, value: float):
        """
        :param float value:
        """

        min_ = 0
        max_ = 1

        if not min_ <= value <= max_:
            raise CATIAApplicationException(f"Value must be between {min_} and {max_}.")

        self.rendering_material.TransparencyCoefficient = value

    def get_3d_texture_color(self, i_color_index: int) -> tuple[int, int, int]:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Get3DTextureColor(short iColorIndex,
                | CATSafeArrayVariant o3DTextureColor)
                |
                |     Returns one color of a 3d texture. The color to access is identified with
                |     its index. The color is expressed with r, g, and b coefficients (between 0 and
                |     255).
                |
                |     Parameters:
                |
                |         iColorIndex
                |             The index of the color to access
                |
                |     Returns:
                |         the color as a safe array made up of three doubles: r, g,
                |         b
                |         The r, g, b values ranges from 0 to 255.
                |         The array must be previously initialized. N.B. Parameter useless for
                |         image textures.

        :param int i_color_index:
        :return: tuple
        :rtype: tuple
        """
        vba_function_name = "get_3d_texture_color"
        vba_code = f"""
        Public Function {vba_function_name}(comObject, iColorIndex)
            Dim o3DTextureColor(3) As CATSafeArrayVariant
            comObject.Get3DTextureColor iColorIndex, o3DTextureColor
            {vba_function_name} = o3DTextureColor
        End Function
        """
        value = self.application.system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object, i_color_index]
        )
        return int(value[0]), int(value[1]), int(value[2])

    def get_3d_texture_color_coefficient(self, i_color_index: int) -> tuple[int, int, int]:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Get3DTextureColorCoefficient(short iColorIndex,
                | double o3DTextureColorCoefficient)
                |
                |     Returns one color coefficient of a 3d texture. The color to access is
                |     identified with its index.
                |
                |     Parameters:
                |
                |         iColorIndex
                |             The index of the color to access.
                |
                |     Returns:
                |         the color coefficient.
                |         If the color is enable, the color coefficient value should range from 0
                |         to 1.
                |         If color is disable, the color coefficient is equal to
                |         -1.
                |         N.B. Parameter useless for rock, chessboard and image textures.

        :param int i_color_index:
        :return: tuple
        :rtype: tuple
        """
        vba_function_name = "get_3d_texture_color_coefficient"
        vba_code = f"""
        Public Function {vba_function_name}(comObject, iColorIndex)
            Dim o3DTextureColorCoefficient(3) As CATSafeArrayVariant
            comObject.Get3DTextureColorCoefficient iColorIndex, o3DTextureColorCoefficient
            {vba_function_name} = o3DTextureColorCoefficient
        End Function
        """
        value = self.application.system_service.evaluate(
            vba_code, 0, vba_function_name, [self.com_object, i_color_index]
        )
        return int(value[0]), int(value[1]), int(value[2])

    def get_3d_texture_orientation(self) -> tuple[float, float, float]:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Get3DTextureOrientation(CATSafeArrayVariant
                | o3DTextureOrientation)
                |
                |     Returns the orientation of a texture. The orientation is expressed with 3
                |     coefficients (orientation around X, Y and Z axis). The orientation values must
                |     be between -360 and 360 degrees. N.B. Parameter useless for IMAGE textures (use
                |     get_Orientation, set_Orientation methods for IMAGE type).
                |
                |     Returns:
                |         the orientation as a safe array made up of three doubles: rotationX,
                |         rotationY, rotationZ.
                |         The array must be previously initialized.

        :return: tuple
        :rtype: tuple
        """
        vba_function_name = "get_3d_texture_orientation"
        vba_code = f"""
        Public Function {vba_function_name}(comObject)
            Dim o3DTextureOrientation(3) As CATSafeArrayVariant
            comObject.Get3DTextureOrientation o3DTextureOrientation
            {vba_function_name} = o3DTextureOrientation
        End Function
        """
        value = self.application.system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return value[0], value[1], value[2]

    def get_3d_texture_position(self) -> tuple[float, float, float]:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Get3DTexturePosition(CATSafeArrayVariant
                | o3DTexturePosition)
                |
                |     Returns the position of a texture. The position is expressed with 3
                |     coefficients (position along X, Y and Z axis). The position values must be
                |     between -100 and 100. N.B. Parameter useless for IMAGE textures (use PositionU,
                |     PositionV methods for IMAGE type).
                |
                |     Returns:
                |         the position as a safe array made up of three doubles: positionX,
                |         positionY, positionZ.
                |         The array must be previously initialized.

        :return: tuple
        :rtype: tuple
        """
        vba_function_name = "get_3d_texture_position"
        vba_code = f"""
        Public Function {vba_function_name}(comObject)
            Dim o3DTexturePosition(3) As CATSafeArrayVariant
            comObject.Get3DTexturePosition o3DTexturePosition
            {vba_function_name} = o3DTexturePosition
        End Function
        """
        value = self.application.system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return value[0], value[1], value[2]

    def get_3d_texture_scale(self) -> tuple[int, int, int]:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Get3DTextureScale(CATSafeArrayVariant o3DTextureScale)
                |
                |     Returns the scale of a texture. The scale is expressed with 3 coefficients
                |     (scale along X, Y and Z axis) The scale values must be > 0 and ≤ 100. N.B.
                |     Parameter useless for IMAGE textures. (use get_ScaleU, set_ScaleU, get_ScaleV,
                |     set_ScaleV methods for IMAGE type)
                |
                |     Returns:
                |         the scale as a safe array made up of three doubles: scaleX, scaleY,
                |         scaleZ.
                |         The array must be previously initialized.

        :return: tuple
        :rtype: tuple
        """
        vba_function_name = "get_3d_texture_scale"
        vba_code = f"""
        Public Function {vba_function_name}(comObject)
            Dim o3DTextureScale(3) As CATSafeArrayVariant
            comObject.Get3DTextureScale o3DTextureScale
            {vba_function_name} = o3DTextureScale
        End Function
        """
        value = self.application.system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return int(value[0]), int(value[1]), int(value[2])

    def get_ambient_color(self) -> tuple[int, int, int]:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAmbientColor(CATSafeArrayVariant oAmbientColor)
                |
                |     Returns the ambient color of a material. The color is expressed with r, g,
                |     and b coefficients (between 0 and 255)
                |
                |     Returns:
                |         the color as a safe array made up of three doubles: r, g,
                |         b
                |         The r, g, b values ranges from 0 to 255.
                |         The array must be previously initialized.

        :return: tuple
        :rtype: tuple
        """
        vba_function_name = "get_ambient_color"
        vba_code = f"""
        Public Function {vba_function_name}(comObject)
            Dim oAmbientColor(3) As CATSafeArrayVariant
            comObject.GetAmbientColor oAmbientColor
            {vba_function_name} = oAmbientColor
        End Function
        """
        value = self.application.system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return int(value[0]), int(value[1]), int(value[2])

    def get_diffuse_color(self) -> tuple[int, int, int]:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetDiffuseColor(CATSafeArrayVariant oDiffuseColor)
                |
                |     Returns the diffuse color of a material. The color is expressed with r, g,
                |     and b coefficients (between 0 and 255)
                |
                |     Returns:
                |         the color as a safe array made up of three doubles: r, g,
                |         b
                |         The r, g, b values ranges from 0 to 255.
                |         The array must be previously initialized.

        :return: tuple
        :rtype: tuple
        """
        vba_function_name = "get_diffuse_color"
        vba_code = f"""
        Public Function {vba_function_name}(comObject)
            Dim oDiffuseColor(3) As CATSafeArrayVariant
            comObject.GetDiffuseColor oDiffuseColor
            {vba_function_name} = oDiffuseColor
        End Function
        """
        value = self.application.system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return int(value[0]), int(value[1]), int(value[2])

    def get_specular_color(self) -> tuple[int, int, int]:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSpecularColor(CATSafeArrayVariant oSpecularColor)
                |
                |     Returns the specular color of a material. The color is expressed with r, g,
                |     and b coefficients (between 0 and 255)
                |
                |     Returns:
                |         the color as a safe array made up of three doubles: r, g,
                |         b
                |         The r, g, b values ranges from 0 to 255.
                |         The array must be previously initialized.

        :return: tuple
        :rtype: tuple
        """
        vba_function_name = "get_specular_color"
        vba_code = f"""
        Public Function {vba_function_name}(comObject)
            Dim oSpecularColor(3) As CATSafeArrayVariant
            comObject.GetSpecularColor oSpecularColor
            {vba_function_name} = oSpecularColor
        End Function
        """
        value = self.application.system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return int(value[0]), int(value[1]), int(value[2])

    def get_transparency_color(self) -> tuple[int, int, int]:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTransparencyColor(CATSafeArrayVariant
                | oTransparencyColor)
                |
                |     Returns the transparent color of a material. The color is expressed with r,
                |     g, and b coefficients (between 0 and 255)
                |
                |     Parameters:
                |
                |         oTransparencyColor
                |             The color as a safe array made up of three doubles: r, g,
                |             b
                |             The r, g, b values ranges from 0 to 255.
                |             The array must be previously initialized.

        :return: tuple
        :rtype: tuple
        """
        vba_function_name = "get_transparency_color"
        vba_code = f"""
        Public Function {vba_function_name}(comObject)
            Dim oTransparencyColor(3) As CATSafeArrayVariant
            comObject.GetTransparencyColor oTransparencyColor
            {vba_function_name} = oTransparencyColor
        End Function
        """
        value = self.application.system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])
        return int(value[0]), int(value[1]), int(value[2])

    def put_3d_texture_color(self, i_color_index: int, i_3d_texture_color: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Put3DTextureColor(short iColorIndex,
                | CATSafeArrayVariant i3DTextureColor)
                |
                |     Sets one color of a 3d texture. The color to access is identified with its
                |     index. The color is expressed with r, g, and b coefficients (between 0 and
                |     255)
                |
                |     Parameters:
                |
                |         iColorIndex
                |             The index of the color to access.
                |         i3DTextureColor
                |             The color as a safe array made up of three doubles: r, g,
                |             b
                |             The r, g, b values ranges from 0 to 255.
                |             The array must be previously initialized. N.B. Parameter useless
                |             for image textures.

        :param int i_color_index:
        :param tuple i_3d_texture_color:
        :return: None
        :rtype: None
        """
        return self.rendering_material.Put3DTextureColor(i_color_index, i_3d_texture_color)

    def put_3d_texture_color_coefficient(self, i_color_index: int, i_3d_texture_color_coefficient: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Put3DTextureColorCoefficient(short iColorIndex,
                | double i3DTextureColorCoefficient)
                |
                |     Sets one color coefficient of a 3d texture. The color to access is
                |     identified with its index.
                |
                |     Parameters:
                |
                |         iColorIndex
                |             The index of the color to access.
                |         i3DTextureColorCoefficient.
                |             The color coefficient.
                |             If color is enable, the color coefficient value should range from 0
                |             to 1.
                |             If color is disable, the color coefficient should be equal to
                |             -1.
                |             N.B. Parameter useless for rock, chessboard and image
                |             textures.

        :param int i_color_index:
        :param float i_3d_texture_color_coefficient:
        :return: None
        :rtype: None
        """
        return self.rendering_material.Put3DTextureColorCoefficient(i_color_index, i_3d_texture_color_coefficient)

    def put_3d_texture_orientation(self, i_3d_texture_orientation: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Put3DTextureOrientation(CATSafeArrayVariant
                | i3DTextureOrientation)
                |
                |     Sets the orientation of a texture. The orientation is expressed with 3
                |     coefficients (orientation around X, Y and Z axis). The orientation values must
                |     be between -360 and 360 degrees. N.B. Parameter useless for IMAGE textures (use
                |     get_Orientation, set_Orientation methods for IMAGE type).
                |
                |     Parameters:
                |
                |         i3DTextureOrientation
                |             The orientation as a safe array made up of three doubles:
                |             rotationX, rotationY, rotationZ.
                |             The array must be previously initialized.

        :param tuple i_3d_texture_orientation:
        :return: None
        :rtype: None
        """
        return self.rendering_material.Put3DTextureOrientation(i_3d_texture_orientation)

    def put_3d_texture_position(self, i_3d_texture_position: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Put3DTexturePosition(CATSafeArrayVariant
                | i3DTexturePosition)
                |
                |     Sets the position of a texture. The position is expressed with 3
                |     coefficients (position along X, Y and Z axis). The position values must be
                |     between -100 and 100. N.B. Parameter useless for IMAGE textures (use PositionU,
                |     PositionV methods for IMAGE type).
                |
                |     Parameters:
                |
                |         i3DTexturePosition
                |             The position as a safe array made up of three doubles: positionX,
                |             positionY, positionZ.
                |             The array must be previously initialized.

        :param tuple i_3d_texture_position:
        :return: None
        :rtype: None
        """
        return self.rendering_material.Put3DTexturePosition(i_3d_texture_position)

    def put_3d_texture_scale(self, i_3d_texture_scale: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Put3DTextureScale(CATSafeArrayVariant i3DTextureScale)
                |
                |     Sets the scale of a texture. The scale is expressed with 3 coefficients
                |     (scale along X, Y and Z axis). The scale values must be > 0 and ≤ 100. N.B.
                |     Parameter useless for IMAGE textures (use get_ScaleU, set_ScaleU, get_ScaleV,
                |     set_ScaleV methods for IMAGE type).
                |
                |     Parameters:
                |
                |         i3DTextureScale
                |             The scale as a safe array made up of three doubles: scaleX, scaleY,
                |             scaleZ.
                |             The array must be previously initialized.

        :param tuple i_3d_texture_scale:
        :return: None
        :rtype: None
        """
        return self.rendering_material.Put3DTextureScale(i_3d_texture_scale)

    def put_ambient_color(self, i_ambient_color: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutAmbientColor(CATSafeArrayVariant iAmbientColor)
                |
                |     Sets the ambient color of a material. The color is expressed with r, g, and
                |     b coefficients (between 0 and 255)
                |
                |     Parameters:
                |
                |         oAmbientColor
                |             The color as a safe array made up of three doubles: r, g,
                |             b
                |             The r, g, b values ranges from 0 to 255.
                |             The array must be previously initialized.

        :param tuple i_ambient_color:
        :return: None
        :rtype: None
        """
        return self.rendering_material.PutAmbientColor(i_ambient_color)

    def put_diffuse_color(self, i_diffuse_color: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutDiffuseColor(CATSafeArrayVariant iDiffuseColor)
                |
                |     Sets the diffuse color of a material. The color is expressed with r, g, and
                |     b coefficients (between 0 and 255)
                |
                |     Parameters:
                |
                |         oDiffuseColor
                |             The color as a safe array made up of three doubles: r, g,
                |             b
                |             The r, g, b values ranges from 0 to 255.
                |             The array must be previously initialized.

        :param tuple i_diffuse_color:
        :return: None
        :rtype: None
        """
        return self.rendering_material.PutDiffuseColor(i_diffuse_color)

    def put_specular_color(self, i_specular_color: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutSpecularColor(CATSafeArrayVariant iSpecularColor)
                |
                |     Sets the specular color of a material. The color is expressed with r, g,
                |     and b coefficients (between 0 and 255)
                |
                |     Parameters:
                |
                |         oSpecularColor
                |             The color as a safe array made up of three doubles: r, g,
                |             b
                |             The r, g, b values ranges from 0 to 255.
                |             The array must be previously initialized.

        :param tuple i_specular_color:
        :return: None
        :rtype: None
        """
        return self.rendering_material.PutSpecularColor(i_specular_color)

    def put_transparency_color(self, i_transparency_color: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub PutTransparencyColor(CATSafeArrayVariant
                | iTransparencyColor)
                |
                |     Sets the transparent color of a material. The color is expressed with r, g,
                |     and b coefficients (between 0 and 255)
                |
                |     Parameters:
                |
                |         iTransparencyColor
                |             The color as a safe array made up of three doubles: r, g,
                |             b
                |             The r, g, b values ranges from 0 to 255.
                |             The array must be previously initialized.

        :param tuple i_transparency_color:
        :return: None
        :rtype: None
        """
        return self.rendering_material.PutTransparencyColor(i_transparency_color)

    def __repr__(self):
        return f'RenderingMaterial(name="{self.name}")'
