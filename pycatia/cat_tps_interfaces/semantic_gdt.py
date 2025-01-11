#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
import inspect

from pycatia.cat_tps_interfaces.median_feature import MedianFeature
from pycatia.cat_tps_interfaces.semantic_gdt_frame_extension import SemanticGDTFrameExtension
from pycatia.cat_tps_interfaces.semantic_gdt_nx_display import SemanticGDTNxDisplay
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.associated_ref_frame import AssociatedRefFrame
from pycatia.cat_tps_interfaces.composite_tolerance import CompositeTolerance
from pycatia.cat_tps_interfaces.free_state import FreeState
from pycatia.cat_tps_interfaces.material_condition import MaterialCondition
from pycatia.cat_tps_interfaces.particular_tol_elem import ParticularTolElem
from pycatia.cat_tps_interfaces.projected_tolerance_zone import ProjectedToleranceZone
from pycatia.cat_tps_interfaces.shifted_profile_tolerance import ShiftedProfileTolerance
from pycatia.cat_tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen
from pycatia.cat_tps_interfaces.tangent_plane import TangentPlane
from pycatia.cat_tps_interfaces.tolerance_per_unit_basis_restrictive_value import TolerancePerUnitBasisRestrictiveValue
from pycatia.cat_tps_interfaces.tolerance_unit_basis_value import ToleranceUnitBasisValue
from pycatia.cat_tps_interfaces.tolerance_zone import ToleranceZone


class SemanticGDT(AnyObject):
    """

    Introduced in V5-6R2017.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SemanticGDT
                | 
                | Interface managing Semantic GDT.
    
    """

    def __init__(self, com_object):
        self.release_check(
            self.application.system_configuration.release,
            27,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )
        super().__init__(com_object)
        self.semantic_gdt = com_object

    def associated_ref_frame(self) -> AssociatedRefFrame:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AssociatedRefFrame() As AssociatedRefFrame
                | 
                |     Returns the annotation on the AssociatedRefFrame
                |     interface.
                | 
                |     Parameters:
                | 
                |         oAssRefFra
                |             The AssociatedRefFrame.

        :rtype: AssociatedRefFrame
        """
        return AssociatedRefFrame(self.semantic_gdt.AssociatedRefFrame())

    def composite_tolerance(self) -> CompositeTolerance:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CompositeTolerance() As CompositeTolerance
                | 
                |     Returns the CompositeTolerance interface.
                | 
                |     Parameters:
                | 
                |         oCompTol
                |             The CompositeTolerance.

        :rtype: CompositeTolerance
        """
        return CompositeTolerance(self.semantic_gdt.CompositeTolerance())

    def frame_extensions(self, i_frame_extent_index: int) -> SemanticGDTFrameExtension:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func FrameExtensions(long iFrameExtentIndex) As
                | SemanticGDTFrameExtension
                |
                |     Role: Gets the Auxiliary Features at given Index applied on
                |     GDT.
                |
                |     Parameters:
                |
                |         iFrameExtentIndex
                |             Index of the Frame Extension to retrieve.
                |         oAuxiliaryFeatures
                |             The list of Auxiliary Features specified on GDT (implies ISO
                |             Standard applied).

        :param int i_frame_extent_index:
        :rtype: SemanticGDTFrameExtension
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return SemanticGDTFrameExtension(self.semantic_gdt.FrameExtensions(i_frame_extent_index))

    def free_state(self) -> FreeState:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func FreeState() As FreeState
                | 
                |     Returns the FreeState interface.
                | 
                |     Parameters:
                | 
                |         oFreeState
                |             The FreeState.

        :rtype: FreeState
        """
        return FreeState(self.semantic_gdt.FreeState())

    def has_a_centered_element(self) -> bool:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func HasACenteredElement() As boolean
                |
                |     Role: Checks if the geometrical specification has a centered
                |     element.
                |     Precondition: Median Feature characteristics is valid only for ISO
                |     standard
                |
                |     Parameters:
                |
                |         oHasCenterElt
                |
                |                 TRUE: The GDT has a center element
                |                 FALSE: The GDT has not a center element or standard different
                |                 from ISO.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.semantic_gdt.HasACenteredElement()

    def has_a_frame_extension(self) -> int:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func HasAFrameExtension() As long
                |
                |     Role: Checks if the geometrical specification wears a frame extension
                |     specification.
                |     Precondition: Intersection Plane, Orientation Plane, Collection Plane or
                |     Direction Feature are only meaningful in ISO Standard.
                |
                |     Parameters:
                |
                |         oFrameExtentNumber
                |
                |                 Greater than 0: The GDT has oFrameExtentNumber frame
                |                 extensions
                |                 Equal or less than 0: The GDT has not a frame extension or
                |                 standard different from ISO (value is -1).

        :rtype: int
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.semantic_gdt.HasAFrameExtension()

    def has_a_free_state(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAFreeState() As boolean
                | 
                |     Checks if the GDT has a Free State.
                | 
                |     Parameters:
                | 
                |         oHasAFreeState
                | 
                |                 TRUE: There is a Free State
                |                 FALSE: There is no Free State

        :rtype: bool
        """
        return self.semantic_gdt.HasAFreeState()

    def has_a_material_condition(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAMaterialCondition() As boolean
                | 
                |     Checks if the GDT has a Material Condition.
                | 
                |     Parameters:
                | 
                |         oHasMatCond
                | 
                |                 TRUE: A Material Condition exits
                |                 FALSE: There is no Material Condition

        :rtype: bool
        """
        return self.semantic_gdt.HasAMaterialCondition()

    def has_a_particular_tol_elem(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAParticularTolElem() As boolean
                | 
                |     Checks if the GDT has a Particuler Element.
                | 
                |     Parameters:
                | 
                |         oHasAParTolElem
                | 
                |                 TRUE: There is a Particuler Element
                |                 FALSE: There is no Particuler Element

        :rtype: bool
        """
        return self.semantic_gdt.HasAParticularTolElem()

    def has_a_tangent_plane(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasATangentPlane() As boolean
                | 
                |     Checks if the GDT has a Tangent Plane Modifier.
                | 
                |     Parameters:
                | 
                |         oIsATangentPlane
                | 
                |                 TRUE: There has a Tangent Plane
                |                 FALSE: There has not Tangent Plane

        :rtype: bool
        """
        return self.semantic_gdt.HasATangentPlane()

    def has_a_tolerance_per_unit_basis_restrictive_value(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasATolerancePerUnitBasisRestrictiveValue() As boolean
                | 
                |     Checks if the GDT has a Tolerance Per Unit Basis Restricted
                |     Value.
                | 
                |     Parameters:
                | 
                |         oHasATolRes
                | 
                |                 TRUE: There is a Tolerance Per Unit Basis Restricted
                |                 Value
                |                 FALSE: There is no Tolerance Per Unit Basis Restricted
                |                 Value

        :rtype: bool
        """
        return self.semantic_gdt.HasATolerancePerUnitBasisRestrictiveValue()

    def is_a_composite_tolerance(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsACompositeTolerance() As boolean
                | 
                |     Checks if the GDT is a Composite Tolerance.
                | 
                |     Parameters:
                | 
                |         oIsACompTol
                | 
                |                 TRUE: There is a Composite Tolerance
                |                 FALSE: There is no Composite Tolerance

        :rtype: bool
        """
        return self.semantic_gdt.IsACompositeTolerance()

    def is_a_projected_tolerance_zone(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAProjectedToleranceZone() As boolean
                | 
                |     Checks if the GDT is a Projected Zone.
                | 
                |     Parameters:
                | 
                |         oIsAProjTolZone
                | 
                |                 TRUE: There is a Projected Zone
                |                 FALSE: There is no Projected Zone

        :rtype: bool
        """
        return self.semantic_gdt.IsAProjectedToleranceZone()

    def is_a_shifted_profile_tolerance(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAShiftedProfileTolerance() As boolean
                | 
                |     Checks if the GDT is a Shifted Profile Tolerance.
                | 
                |     Parameters:
                | 
                |         oIsAShiftProTol
                | 
                |                 TRUE: There is a Shifted Profile Tolerance
                |                 FALSE: There is no Shifted Profile Tolerance

        :rtype: bool
        """
        return self.semantic_gdt.IsAShiftedProfileTolerance()

    def is_a_tolerance_unit_basis_value(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAToleranceUnitBasisValue() As boolean
                | 
                |     Checks if the GDT is a Tolerance Unit Basis Value.
                | 
                |     Parameters:
                | 
                |         oIsATolUnitBas
                | 
                |                 TRUE: A Tolerance Zone exits
                |                 FALSE: There is no Tolerance Zone

        :rtype: bool
        """
        return self.semantic_gdt.IsAToleranceUnitBasisValue()

    def is_a_tolerance_zone(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAToleranceZone() As boolean
                | 
                |     Checks if a Tolerance Zone exists.
                | 
                |     Parameters:
                | 
                |         oIsATolZone
                | 
                |                 TRUE: A Tolerance Zone exits
                |                 FALSE: There is no Tolerance Zone

        :rtype: bool
        """
        return self.semantic_gdt.IsAToleranceZone()

    def is_an_associated_ref_frame(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAnAssociatedRefFrame() As boolean
                | 
                |     Checks if the GDT is an Associated Reference Frame.
                | 
                |     Parameters:
                | 
                |         oIsAnAssRefFra
                | 
                |                 TRUE: There is an Associated Reference Frame
                |                 FALSE: There is no Associated Reference Frame

        :rtype: bool
        """
        return self.semantic_gdt.IsAnAssociatedRefFrame()

    def is_applied_on_multiple_entities(self) -> bool:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func IsAppliedOnMultipleEntities() As boolean
                |
                |     Role: Checks if the geometrical specification is applied onto multiple
                |     geometries.
                |
                |     Parameters:
                |
                |       oIsAPattern
                |
                |         TRUE: The GDT is applied on Nx elements
                |         FALSE: The GDT is applied on a unique surface.

        :rtype: bool
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return self.semantic_gdt.IsAppliedOnMultipleEntities()

    def material_condition(self) -> MaterialCondition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func MaterialCondition() As MaterialCondition
                | 
                |     Returns the MaterialCondition interface.
                | 
                |     Parameters:
                | 
                |         oMatCond
                |             The Material Condition.

        :rtype: MaterialCondition
        """
        return MaterialCondition(self.semantic_gdt.MaterialCondition())

    def median_feature(self) -> MedianFeature:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func MedianFeature() As MedianFeature
                |
                |     Role: Gets the GDT on the Median Feature interface.
                |
                |     Parameters:
                |
                |         oMedianFeat
                |             The Median Feature.

        :rtype: MedianFeature
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return MedianFeature(self.semantic_gdt.MedianFeature())

    def nx_display(self) -> SemanticGDTNxDisplay:
        """

        Introduced in V5-6R2019.

        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2024-08-20 16:04:57.203445)
                | Func NxDisplay() As SemanticGDTNxDisplay
                |
                |     Role: Gets the GDT on the handle to read Nx instance count, Collection or
                |     Separate type of the geometrical specification.
                |
                |     Parameters:
                |
                |         oNxDisplay
                |             Behavior to qualify Nx application context of this GDT.

        :rtype: SemanticGDTNxDisplay
        """

        self.release_check(
            self.application.system_configuration.release,
            29,
            f'{self.__class__.__name__}.{inspect.stack()[0][3]}',
        )

        return SemanticGDTNxDisplay(self.semantic_gdt.NxDisplay())

    def particular_tol_elem(self) -> ParticularTolElem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ParticularTolElem() As ParticularTolElem
                | 
                |     Returns the ParticularTolElem interface.
                | 
                |     Parameters:
                | 
                |         oParTolElem
                |             The ParticularTolElem.

        :rtype: ParticularTolElem
        """
        return ParticularTolElem(self.semantic_gdt.ParticularTolElem())

    def projected_tolerance_zone(self) -> ProjectedToleranceZone:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ProjectedToleranceZone() As ProjectedToleranceZone
                | 
                |     Returrns the ProjectedToleranceZone interface.
                | 
                |     Parameters:
                | 
                |         oProjTolZone
                |             The ProjectedToleranceZone.

        :rtype: ProjectedToleranceZone
        """
        return ProjectedToleranceZone(self.semantic_gdt.ProjectedToleranceZone())

    def shifted_profile_tolerance(self) -> ShiftedProfileTolerance:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ShiftedProfileTolerance() As ShiftedProfileTolerance
                | 
                |     Returns the ShiftedProfileTolerance interface.
                | 
                |     Parameters:
                | 
                |         oShiftProTol
                |             The ShiftedProfileTolerance.

        :rtype: ShiftedProfileTolerance
        """
        return ShiftedProfileTolerance(self.semantic_gdt.ShiftedProfileTolerance())

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TPSParallelOnScreen() As TPSParallelOnScreen
                | 
                |     Gets the annotation on TPSParallelOnScreen interface.

        :rtype: TPSParallelOnScreen
        """
        return TPSParallelOnScreen(self.semantic_gdt.TPSParallelOnScreen())

    def tangent_plane(self) -> TangentPlane:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TangentPlane() As TangentPlane
                | 
                |     Returns the Tangent Plane interface.
                | 
                |     Parameters:
                | 
                |         oTangentPlane
                |             The Tangent Plane.

        :rtype: TangentPlane
        """
        return TangentPlane(self.semantic_gdt.TangentPlane())

    def tolerance_per_unit_basis_restrictive_value(self) -> TolerancePerUnitBasisRestrictiveValue:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TolerancePerUnitBasisRestrictiveValue() As
                | TolerancePerUnitBasisRestrictiveValue
                | 
                |     Returns the TolerancePerUnitBasisRestrictiveValue
                |     interface.
                | 
                |     Parameters:
                | 
                |         oTolRes
                |             The TolerancePerUnitBasisRestrictiveValue.

        :rtype: TolerancePerUnitBasisRestrictiveValue
        """
        return TolerancePerUnitBasisRestrictiveValue(self.semantic_gdt.TolerancePerUnitBasisRestrictiveValue())

    def tolerance_unit_basis_value(self) -> ToleranceUnitBasisValue:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ToleranceUnitBasisValue() As ToleranceUnitBasisValue
                | 
                |     Returns the ToleranceUnitBasisValue interface.
                | 
                |     Parameters:
                | 
                |         oTolUnitBas
                |             The Tolerance Unit Basis Value.

        :rtype: ToleranceUnitBasisValue
        """
        return ToleranceUnitBasisValue(self.semantic_gdt.ToleranceUnitBasisValue())

    def tolerance_zone(self) -> ToleranceZone:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ToleranceZone() As ToleranceZone
                | 
                |     Returns the ToleranceZone interface.
                | 
                |     Parameters:
                | 
                |         oTolZone
                |             The Tolerance Zone.

        :rtype: ToleranceZone
        """
        return ToleranceZone(self.semantic_gdt.ToleranceZone())

    def __repr__(self):
        return f'SemanticGdt(name="{self.name}")'
