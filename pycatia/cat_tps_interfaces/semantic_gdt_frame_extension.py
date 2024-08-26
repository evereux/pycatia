#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R31 on 2024-08-20 16:04:57.203445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.

"""
import inspect

from pycatia.cat_tps_interfaces.datum_simple import DatumSimple
from pycatia.system_interfaces.any_object import AnyObject


class SemanticGDTFrameExtension(AnyObject):
    """

    Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SemanticGDTFrameExtension
                |
                | Interface to parse Semantic GDT auxiliary feature.
                |
                | Its allows getting information of Intersection Plane, Orientation Plane,
                | Collection Plane or Direction Feature. (ISO Standard only).

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.semantic_gdt_frame_extension = com_object

    @property
    def direction_specification(self) -> str:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property DirectionSpecification() As CATBSTR (Read Only)
                |     Gets the direction specification.
                |
                |     Parameters:
                |
                |         oDirSpec
                |             The Direction of Specification.
                |             List of legal values are the same as the ones obtained using
                |             SuperType property (equals to "FTA_Orientation") from Annotation2 augmented by
                |             specific type "FTA_Symmetry":
                |             oDirSpec = "FTA_Parallelism"
                |             oDirSpec = "FTA_Perpendicularity"
                |             oDirSpec = "FTA_Angularity"
                |             oDirSpec = "FTA_Symmetry"

        :rtype: str
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.semantic_gdt_frame_extension.DirectionSpecification

    @property
    def type(self) -> str:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Property Type() As CATBSTR (Read Only)
                |     Gets the Type.
                |
                |     Parameters:
                |
                |         oType
                |             The Type.
                |             List of types available:
                |             Type = "FTA_IntersectionPlane"
                |             Type = "FTA_OrientationPlane"
                |             Type = "FTA_CollectionPlane"
                |             Type = "FTA_DirectionFeature"

        :rtype: str
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.semantic_gdt_frame_extension.Type

    def direction_reference(self) -> DatumSimple:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func DirectionReference() As DatumSimple
                |     Returns the Datum Feature used as reference to specify auxiliary
                |     feature.
                |
                |     Parameters:
                |
                |         oDatumFeature
                |             The Datum Feature.

        :rtype: DatumSimple
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return DatumSimple(self.semantic_gdt_frame_extension.DirectionReference())

    def orientation(self) -> float:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func Orientation() As double
                |     Retrieves orientation angle when DirectionSpecification is
                |     "FTA_Angularity".
                |     These values are expressed in degrees.
                |
                |     Parameters:
                |
                |         oOrientation
                |             The orientation value with respect to Datum Feature reference.

        :rtype: float
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.semantic_gdt_frame_extension.Orientation()

    def __repr__(self):
        return f'SemanticGdtFrameExtension(name="{self.name}")'
