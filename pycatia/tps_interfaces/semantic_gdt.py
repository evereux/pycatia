#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.tps_interfaces.associated_ref_frame import AssociatedRefFrame
from pycatia.tps_interfaces.composite_tolerance import CompositeTolerance
from pycatia.tps_interfaces.free_state import FreeState
from pycatia.tps_interfaces.material_condition import MaterialCondition
from pycatia.tps_interfaces.particular_tol_elem import ParticularTolElem
from pycatia.tps_interfaces.projected_tolerance_zone import ProjectedToleranceZone
from pycatia.tps_interfaces.shifted_profile_tolerance import ShiftedProfileTolerance
from pycatia.tps_interfaces.tps_parallel_on_screen import TPSParallelOnScreen
from pycatia.tps_interfaces.tangent_plane import TangentPlane
from pycatia.tps_interfaces.tolerance_per_unit_basis_restrictive_value import TolerancePerUnitBasisRestrictiveValue
from pycatia.tps_interfaces.tolerance_unit_basis_value import ToleranceUnitBasisValue
from pycatia.tps_interfaces.tolerance_zone import ToleranceZone


class SemanticGdt(AnyObject):
    """
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

        :return: AssociatedRefFrame
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

        :return: CompositeTolerance
        :rtype: CompositeTolerance
        """
        return CompositeTolerance(self.semantic_gdt.CompositeTolerance())

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

        :return: FreeState
        :rtype: FreeState
        """
        return FreeState(self.semantic_gdt.FreeState())

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

        :return: bool
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

        :return: bool
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

        :return: bool
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

        :return: bool
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

        :return: bool
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

        :return: bool
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

        :return: bool
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

        :return: bool
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

        :return: bool
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

        :return: bool
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

        :return: bool
        :rtype: bool
        """
        return self.semantic_gdt.IsAnAssociatedRefFrame()

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

        :return: MaterialCondition
        :rtype: MaterialCondition
        """
        return MaterialCondition(self.semantic_gdt.MaterialCondition())

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

        :return: ParticularTolElem
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

        :return: ProjectedToleranceZone
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

        :return: ShiftedProfileTolerance
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

        :return: TPSParallelOnScreen
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

        :return: TangentPlane
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

        :return: TolerancePerUnitBasisRestrictiveValue
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

        :return: ToleranceUnitBasisValue
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

        :return: ToleranceZone
        :rtype: ToleranceZone
        """
        return ToleranceZone(self.semantic_gdt.ToleranceZone())

    def __repr__(self):
        return f'SemanticGdt(name="{self.name}")'
