#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject
from pycatia.cat_tps_interfaces.associated_ref_frame import AssociatedRefFrame
from pycatia.cat_tps_interfaces.composite_tolerance import CompositeTolerance
from pycatia.cat_tps_interfaces.controlled_radius import ControlledRadius
from pycatia.cat_tps_interfaces.datum_simple import DatumSimple
from pycatia.cat_tps_interfaces.datum_target import DatumTarget
from pycatia.cat_tps_interfaces.default_annotation import DefaultAnnotation
from pycatia.cat_tps_interfaces.dimension_3d import Dimension3D
from pycatia.cat_tps_interfaces.dimension_limit import DimensionLimit
from pycatia.cat_tps_interfaces.dimension_pattern import DimensionPattern
from pycatia.cat_tps_interfaces.envelope_condition import EnvelopeCondition
from pycatia.cat_tps_interfaces.flag_note import FlagNote
from pycatia.cat_tps_interfaces.free_state import FreeState
from pycatia.cat_tps_interfaces.material_condition import MaterialCondition
from pycatia.cat_tps_interfaces.noa import Noa
from pycatia.cat_tps_interfaces.particular_tol_elem import ParticularTolElem
from pycatia.cat_tps_interfaces.projected_tolerance_zone import ProjectedToleranceZone
from pycatia.cat_tps_interfaces.reference_frame import ReferenceFrame
from pycatia.cat_tps_interfaces.roughness import Roughness
from pycatia.cat_tps_interfaces.shifted_profile_tolerance import ShiftedProfileTolerance
from pycatia.cat_tps_interfaces.tangent_plane import TangentPlane
from pycatia.cat_tps_interfaces.text import Text
from pycatia.cat_tps_interfaces.tolerance_per_unit_basis_restrictive_value import TolerancePerUnitBasisRestrictiveValue
from pycatia.cat_tps_interfaces.tolerance_unit_basis_value import ToleranceUnitBasisValue
from pycatia.cat_tps_interfaces.tolerance_zone import ToleranceZone
from pycatia.cat_tps_interfaces.tps_view import TPSView


class Annotation(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Annotation
                | 
                | Interface for the Technological Product Specification (TPS)
                | objects.
                | Leaf entity in the Design Pattern Composite. TPS modeler enables definition of
                | specification related to surfaces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.annotation = com_object

    @property
    def super_type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property SuperType() As CATBSTR (Read Only)
                | 
                |     Get the Super Type.
                | 
                |     Parameters:
                | 
                |         oSuperType
                |             The Super Type. The list of SuperType available: "FTA_NonSemantic"
                |             "FTA_Form" "FTA_Dimension" "FTA_Position" "FTA_Datum" "FTA_Orientation"
                |             "FTA_RunOut"

        :return: str
        :rtype: str
        """

        return self.annotation.SuperType

    @property
    def tps_status(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TPSStatus() As CATBSTR (Read Only)
                | 
                |     Get the TPS Status.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             The Status.

        :return: str
        :rtype: str
        """

        return self.annotation.TPSStatus

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Get the Type.
                | 
                |     Parameters:
                | 
                |         oType
                |             The Type. List of types available ordered by SuperType: SuperType = "FTA_NonSemantic" Type = "FTA_Text" Type = "FTA_FlagNote" Type = "FTA_Roughness" Type = "FTA_Weld" Type = "FTA_Noa" Type = "FTA_NonSemanticDatum" Type = "FTA_NonSemanticTarget" Type = "FTA_NonSemanticGDT" Type = "FTA_NonSemanticDimension" SuperType = "FTA_Form" Type = "FTA_Flatness" Type = "FTA_Straightness" Type = "FTA_Circularity" Type = "FTA_Cylindricity" Type = "FTA_ProfileOfAnyLine" Type = "FTA_ProfileOfASurface" Type = "FTA_PatternTruePos" SuperType = "FTA_Dimension" Type = "FTA_LinearDimension" Type = "FTA_AngularDimension" Type = "FTA_SecondLinearDimension" Type = "FTA_ChamferDimension" Type = "FTA_BasicDimension" SuperType = "FTA_Position" Type = "FTA_TruePosition" Type = "FTA_Concentricity" Type = "FTA_Symmetry" Type = "FTA_PositionOfAnyLine" Type = "FTA_PositionOfASurface" SuperType = "FTA_Datum" Type = "FTA_DatumSimple" Type = "FTA_DatumTarget" Type = "FTA_DatumSystem" Type = "FTA_ReferenceFrame" SuperType = "FTA_Orientation" Type = "FTA_Parallelism" Type = "FTA_Perpendicularity" Type = "FTA_Angularity" SuperType = "FTA_RunOut" Type = "FTA_TotalRunOut" Type = "FTA_CircularRunOut"

        :return: str
        :rtype: str
        """

        return self.annotation.Type

    @property
    def z(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Z(double iZ) (Write Only)
                | 
                |     method get_Z will never be exposed Set the offset of the
                |     annotation
                | 
                |     Parameters:
                | 
                |         iZ
                |             The offset.

        :return: float
        :rtype: float
        """

        return self.annotation.Z

    @z.setter
    def z(self, value: float):
        """
        :param float value:
        """

        self.annotation.Z = value

    def add_leader(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddLeader()
                | 
                |     Add a leader.

        :return: None
        :rtype: None
        """
        return self.annotation.AddLeader()

    def apply_referenced_geom_colour(self, i_releated_r: int, i_releated_g: int, i_releated_b: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ApplyReferencedGeomColor(long iReleatedR,
                | long iReleatedG,
                | long iReleatedB)
                | 
                |     Apply a color to referenced geometry.

        :param int i_releated_r:
        :param int i_releated_g:
        :param int i_releated_b:
        :return: None
        :rtype: None
        """
        return self.annotation.ApplyReferencedGeomColor(i_releated_r, i_releated_g, i_releated_b)

    def apply_referenced_init_colour(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ApplyReferencedInitColor()
                | 
                |     Apply the initial color to referenced geometry.

        :return: None
        :rtype: None
        """
        return self.annotation.ApplyReferencedInitColor()

    def associated_ref_frame(self) -> AssociatedRefFrame:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AssociatedRefFrame() As AssociatedRefFrame
                | 
                |     Get the annotation on the AssociatedRefFrame interface.

        :return: AssociatedRefFrame
        :rtype: AssociatedRefFrame
        """

        return AssociatedRefFrame(self.annotation.AssociatedRefFrame())

    def composite_tolerance(self) -> CompositeTolerance:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CompositeTolerance() As CompositeTolerance
                | 
                |     Get the annotation on the CompositeTolerance interface.

        :return: CompositeTolerance
        :rtype: CompositeTolerance
        """

        return CompositeTolerance(self.annotation.CompositeTolerance())

    def controlled_radius(self) -> ControlledRadius:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ControledRadius() As ControledRadius
                | 
                |     Get the annotation on the ControledRadius interface.

        :return: ControledRadius
        :rtype: ControledRadius
        """

        return ControlledRadius(self.annotation.ControlledRadius())

    def datum_simple(self) -> DatumSimple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DatumSimple() As DatumSimple
                | 
                |     Get the annotation on the DatumSimple interface.

        :return: DatumSimple
        :rtype: DatumSimple
        """

        return DatumSimple(self.annotation.DatumSimple())

    def datum_target(self) -> DatumTarget:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DatumTarget() As DatumTarget
                | 
                |     Get the annotation on the DatumTarget interface.

        :return: DatumTarget
        :rtype: DatumTarget
        """

        return DatumTarget(self.annotation.DatumTarget())

    def default_annotation(self) -> DefaultAnnotation:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DefaultAnnotation() As DefaultAnnotation
                | 
                |     Get the annotation on the DefaultAnnotation interface.

        :return: DefaultAnnotation
        :rtype: DefaultAnnotation
        """

        return DefaultAnnotation(self.annotation.DefaultAnnotation())

    def dimension_3d(self) -> Dimension3D:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Dimension3D() As Dimension3D
                | 
                |     Get the 3D Dimension on the 3D Dimension interface.
                | 
                |     Parameters:
                | 
                |         oDim
                |             The 3D Dimension.

        :return: Dimension3D
        :rtype: Dimension3D
        """

        return Dimension3D(self.annotation.Dimension3D())

    def dimension_limit(self) -> DimensionLimit:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DimensionLimit() As DimensionLimit
                | 
                |     Get the annotation on the DimensionLimit interface.

        :return: DimensionLimit
        :rtype: DimensionLimit
        """

        return DimensionLimit(self.annotation.DimensionLimit())

    def dimension_pattern(self) -> DimensionPattern:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func DimensionPattern() As DimensionPattern
                | 
                |     Get the annotation on the DimensionPattern interface.

        :return: DimensionPattern
        :rtype: DimensionPattern
        """

        return DimensionPattern(self.annotation.DimensionPattern())

    def envelop_condition(self) -> EnvelopeCondition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func EnvelopCondition() As EnvelopCondition
                | 
                |     Get the annotation on the EnvelopCondition interface.

        :return: EnvelopCondition
        :rtype: EnvelopCondition
        """

        return EnvelopeCondition(self.annotation.EnvelopeCondition())

    def flag_note(self) -> FlagNote:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func FlagNote() As FlagNote
                | 
                |     Get the annotation on the FlagNote interface.
                | 
                |     Parameters:
                | 
                |         oFlagNote
                |             The annotation Flag Note.

        :return: FlagNote
        :rtype: FlagNote
        """

        return FlagNote(self.annotation.FlagNote())

    def free_state(self) -> FreeState:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func FreeState() As FreeState
                | 
                |     Get the annotation on the FreeState interface.

        :return: FreeState
        :rtype: FreeState
        """

        return FreeState(self.annotation.FreeState())

    def get_surfaces(self, o_safe_array: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSurfaces(CATSafeArrayVariant oSafeArray)
                | 
                |     Get the geometry on which the Annotation is applied to.

        :param tuple o_safe_array:
        :return: tuple
        :rtype: tuple
        """
        return self.annotation.GetSurfaces(o_safe_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_surfaces'
        # # vba_code = """
        # # Public Function get_surfaces(annotation)
        # #     Dim oSafeArray (2)
        # #     annotation.GetSurfaces oSafeArray
        # #     get_surfaces = oSafeArray
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_surfaces_count(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSurfacesCount() As double
                | 
                |     Count the geometry on which the Annotation is applied to.

        :return: float
        :rtype: float
        """
        return self.annotation.GetSurfacesCount()

    def has_a_controlled_radius(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAControledRadius() As boolean
                | 
                |     To know if the Annotation has a Controled Radius.

        :return: bool
        :rtype: bool
        """
        return self.annotation.HasAControledRadius()

    def has_a_free_state(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAFreeState() As boolean
                | 
                |     To know if the Annotation has a Free State.

        :return: bool
        :rtype: bool
        """
        return self.annotation.HasAFreeState()

    def has_a_material_condition(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAMaterialCondition() As boolean
                | 
                |     To know if the Annotation has a Material Condition.

        :return: bool
        :rtype: bool
        """
        return self.annotation.HasAMaterialCondition()

    def has_a_particular_tol_elem(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAParticularTolElem() As boolean
                | 
                |     To know if the Annotation has a Particuler Element.

        :return: bool
        :rtype: bool
        """
        return self.annotation.HasAParticularTolElem()

    def has_a_tolerance_per_unit_basis_restrictive_value(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasATolerancePerUnitBasisRestrictiveValue() As boolean
                | 
                |     To know if the Annotation has a Tolerance Per Unit Basis Restricted Value.

        :return: bool
        :rtype: bool
        """
        return self.annotation.HasATolerancePerUnitBasisRestrictiveValue()

    def has_an_envelop_condition(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasAnEnvelopCondition() As boolean
                | 
                |     To know if the Annotation has an Envelop Condition.

        :return: bool
        :rtype: bool
        """
        return self.annotation.HasAnEnvelopCondition()

    def has_dimension_limit(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func HasDimensionLimit() As boolean
                | 
                |     To know if the Annotation has a Dimension Limit.

        :return: bool
        :rtype: bool
        """
        return self.annotation.HasDimensionLimit()

    def is_a_composite_tolerance(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsACompositeTolerance() As boolean
                | 
                |     To know if the Annotation is a composite Tolerance.

        :return: bool
        :rtype: bool
        """
        return self.annotation.IsACompositeTolerance()

    def is_a_default_annotation(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsADefaultAnnotation() As boolean
                | 
                |     To know if the Annotation is a Default Annotation.

        :return: bool
        :rtype: bool
        """
        return self.annotation.IsADefaultAnnotation()

    def is_a_dimension_pattern(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsADimensionPattern() As boolean
                | 
                |     To know if the Annotation is a Dimension Pattern.

        :return: bool
        :rtype: bool
        """
        return self.annotation.IsADimensionPattern()

    def is_a_projected_tolerance_zone(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAProjectedToleranceZone() As boolean
                | 
                |     To know if the Annotation is a Projected Zone.

        :return: bool
        :rtype: bool
        """
        return self.annotation.IsAProjectedToleranceZone()

    def is_a_shifted_profile_tolerance(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAShiftedProfileTolerance() As boolean
                | 
                |     To know if the Annotation is a Shifted Profile Tolerance.

        :return: bool
        :rtype: bool
        """
        return self.annotation.IsAShiftedProfileTolerance()

    def is_a_tangent_plane(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsATangentPlane() As boolean
                | 
                |     To know if the Annotation is a Tangent Plane.

        :return: bool
        :rtype: bool
        """
        return self.annotation.IsATangentPlane()

    def is_a_tolerance_unit_basis_value(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAToleranceUnitBasisValue() As boolean
                | 
                |     To know if the Annotation is a Tolerance Unit Basis Value.

        :return: bool
        :rtype: bool
        """
        return self.annotation.IsAToleranceUnitBasisValue()

    def is_a_tolerance_zone(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAToleranceZone() As boolean
                | 
                |     Is the a Tolerance Zone.

        :return: bool
        :rtype: bool
        """
        return self.annotation.IsAToleranceZone()

    def is_an_associated_ref_frame(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func IsAnAssociatedRefFrame() As boolean
                | 
                |     To know if the Annotation is an Associated Reference Frame.

        :return: bool
        :rtype: bool
        """
        return self.annotation.IsAnAssociatedRefFrame()

    def material_condition(self) -> MaterialCondition:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func MaterialCondition() As MaterialCondition
                | 
                |     Get the annotation on the MaterialCondition interface.

        :return: MaterialCondition
        :rtype: MaterialCondition
        """

        return MaterialCondition(self.annotation.MaterialCondition())

    def modify_visualisation(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ModifyVisu()
                | 
                |     To refresh the 3D visualization.

        :return: None
        :rtype: None
        """
        return self.annotation.ModifyVisu()

    def noa(self) -> Noa:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Noa() As Noa
                | 
                |     Get the annotation on the Noa interface.

        :return: Noa
        :rtype: Noa
        """

        return Noa(self.annotation.Noa())

    def particular_tol_elem(self) -> ParticularTolElem:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ParticularTolElem() As ParticularTolElem
                | 
                |     Get the annotation on the ParticularTolElem interface.

        :return: ParticularTolElem
        :rtype: ParticularTolElem
        """

        return ParticularTolElem(self.annotation.ParticularTolElem())

    def projected_tolerance_zone(self) -> ProjectedToleranceZone:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ProjectedToleranceZone() As ProjectedToleranceZone
                | 
                |     Get the annotation on the ProjectedToleranceZone interface.

        :return: ProjectedToleranceZone
        :rtype: ProjectedToleranceZone
        """
        return ProjectedToleranceZone(
            self.annotation.ProjectedToleranceZone())

    def reference_frame(self) -> ReferenceFrame:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ReferenceFrame() As ReferenceFrame
                | 
                |     Get the annotation on the ReferenceFrame interface.

        :return: ReferenceFrame
        :rtype: ReferenceFrame
        """

        return ReferenceFrame(self.annotation.ReferenceFrame())

    def roughness(self) -> Roughness:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Roughness() As Roughness
                | 
                |     Get the annotation on the Roughness interface.

        :return: Roughness
        :rtype: Roughness
        """

        return Roughness(self.annotation.Roughness())

    def set_xy(self, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetXY(double iX,
                | double iY)
                | 
                |     method GetXY will never be exposed Set TPS coordinates in the
                |     view
                | 
                |     Parameters:
                | 
                |         oX
                |             The X coordinate. 
                |         oY
                |             The Y coordinate.

        :param float i_x:
        :param float i_y:
        :return: None
        :rtype: None
        """
        return self.annotation.SetXY(i_x, i_y)

    def shifted_profile_tolerance(self) -> ShiftedProfileTolerance:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ShiftedProfileTolerance() As ShiftedProfileTolerance
                | 
                |     Get the annotation on the ShiftedProfileTolerance interface.

        :return: ShiftedProfileTolerance
        :rtype: ShiftedProfileTolerance
        """

        return ShiftedProfileTolerance(self.annotation.ShiftedProfileTolerance())

    def tangent_plane(self) -> TangentPlane:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TangentPlane() As TangentPlane
                | 
                |     Get the annotation on the TangentPlane interface.

        :return: TangentPlane
        :rtype: TangentPlane
        """

        return TangentPlane(self.annotation.TangentPlane())

    def text(self) -> Text:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Text() As Text
                | 
                |     Get the annotation on the Text interface.
                | 
                |     Parameters:
                | 
                |         oText
                |             The annotation Text.

        :return: Text
        :rtype: Text
        """
        return Text(self.annotation.Text())

    def tolerance_per_unit_basis_restrictive_value(self) -> TolerancePerUnitBasisRestrictiveValue:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func TolerancePerUnitBasisRestrictiveValue() As
                | TolerancePerUnitBasisRestrictiveValue
                | 
                |     Get the annotation on the TolerancePerUnitBasisRestrictiveValue interface.

        :return: TolerancePerUnitBasisRestrictiveValue
        :rtype: TolerancePerUnitBasisRestrictiveValue
        """
        return TolerancePerUnitBasisRestrictiveValue(self.annotation.TolerancePerUnitBasisRestrictiveValue())

    def tolerance_unit_basis_value(self) -> ToleranceUnitBasisValue:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ToleranceUnitBasisValue() As ToleranceUnitBasisValue
                | 
                |     Get the annotation on the ToleranceUnitBasisValue interface.

        :return: ToleranceUnitBasisValue
        :rtype: ToleranceUnitBasisValue
        """
        return ToleranceUnitBasisValue(self.annotation.ToleranceUnitBasisValue())

    def tolerance_zone(self) -> ToleranceZone:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ToleranceZone() As ToleranceZone
                | 
                |     Get the annotation on the ToleranceZone interface.

        :return: ToleranceZone
        :rtype: ToleranceZone
        """

        return ToleranceZone(self.annotation.ToleranceZone())

    def transfert_to_view(self, i_view: TPSView) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub TransfertToView(TPSView iView)
                | 
                |     Move the annotation in another view.
                | 
                |     Parameters:
                | 
                |         iView
                |             The destination view.

        :param TPSView i_view:
        :return: None
        :rtype: None
        """
        return self.annotation.TransfertToView(i_view.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'transfert_to_view'
        # # vba_code = """
        # # Public Function transfert_to_view(annotation)
        # #     Dim iView (2)
        # #     annotation.TransfertToView iView
        # #     transfert_to_view = iView
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Annotation(name="{self.name}")'
