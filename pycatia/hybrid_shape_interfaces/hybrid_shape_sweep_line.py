#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.hybrid_shape_interfaces.hybrid_shape_sweep import HybridShapeSweep
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length


class HybridShapeSweepLine(HybridShapeSweep):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeSweep
                |                             HybridShapeSweepLine
                | 
                | Represents the sweep line object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep_line = com_object

    @property
    def angle_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AngleLaw() As Reference
                | 
                |     Returns or sets the angular law.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_line.AngleLaw)

    @angle_law.setter
    def angle_law(self, reference_law: Reference):
        """
        :param Reference reference_law:
        """

        self.hybrid_shape_sweep_line.AngleLaw = reference_law.com_object

    @property
    def angle_law_inversion(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AngleLawInversion() As long
                | 
                |     Returns or sets whether the angular law has to be
                |     inverted.
                |     Legal angular law inversion values are:
                |     0 The angular law has NOT to be inverted
                |     1 The angular law has to be inverted

        :rtype: int
        """

        return self.hybrid_shape_sweep_line.AngleLawInversion

    @angle_law_inversion.setter
    def angle_law_inversion(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_line.AngleLawInversion = value

    @property
    def angle_law_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AngleLawType() As long
                | 
                |     Returns or sets the angular law type.
                |     Legal angular law type values are:
                |     0 Undefined law type (CATGSMBasicLawType_None)
                |     1 Constant law type (CATGSMBasicLawType_Constant)
                |     2 Linear law type (CATGSMBasicLawType_Linear)
                |     3 S law type (CATGSMBasicLawType_SType)
                |     4 Law specified by a GSD law feature
                |     (CATGSMBasicLawType_Advanced)

        :rtype: int
        """

        return self.hybrid_shape_sweep_line.AngleLawType

    @angle_law_type.setter
    def angle_law_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_line.AngleLawType = value

    @property
    def canonical_detection(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CanonicalDetection() As long
                | 
                |     Returns or sets whether canonical surfaces of the swept surface are
                |     detected.
                |     Legal values:
                |     0 No detection of canonical surface is performed.
                |     2 Detection of canonical surfaces is performed.

        :rtype: int
        """

        return self.hybrid_shape_sweep_line.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_line.CanonicalDetection = value

    @property
    def context(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Context() As long
                | 
                |     Returns or sets the context on Sweep feature.
                | 
                |         0 This option creates Swept surface.
                |         1 This option creates Swept volume.
                | 
                | 
                |     Note: Setting volume result requires GSO License.
                | 
                |     Example:
                |         This example retrieves in oContext the context for the Sweep hybrid
                |         shape feature.
                | 
                |          Dim oContext
                |          Set oContext = Sweep.Context

        :rtype: int
        """

        return self.hybrid_shape_sweep_line.Context

    @context.setter
    def context(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_line.Context = value

    @property
    def draft_computation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DraftComputationMode() As long
                | 
                |     Returns or sets the draft computation mode.

        :rtype: int
        """

        return self.hybrid_shape_sweep_line.DraftComputationMode

    @draft_computation_mode.setter
    def draft_computation_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_line.DraftComputationMode = value

    @property
    def draft_direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DraftDirection() As HybridShapeDirection
                | 
                |     Returns or sets the draft direction.
                | 
                |     Example
                |     :
                |         This example retrieves in oDirection the direction of the LinearSweep
                |         feature.
                | 
                |          Dim oDirection As CATIAHybridShapeDirection
                |          Set oDirection = LinearSweep.DraftDirection

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_sweep_line.DraftDirection)

    @draft_direction.setter
    def draft_direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_sweep_line.DraftDirection = direction.com_object

    @property
    def first_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstGuideCrv() As Reference
                | 
                |     Returns or sets the sweep operation first guide curve.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_line.FirstGuideCrv)

    @first_guide_crv.setter
    def first_guide_crv(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_sweep_line.FirstGuideCrv = reference_curve.com_object

    @property
    def first_guide_surf(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstGuideSurf() As Reference
                | 
                |     Returns or sets the sweep operation first guide surface.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_line.FirstGuideSurf)

    @first_guide_surf.setter
    def first_guide_surf(self, reference_surface: Reference):
        """
        :param Reference reference_surface:
        """

        self.hybrid_shape_sweep_line.FirstGuideSurf = reference_surface.com_object

    @property
    def first_length_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstLengthLaw() As Reference
                | 
                |     Returns or sets the first length law useful in some linear sweep types.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_line.FirstLengthLaw)

    @first_length_law.setter
    def first_length_law(self, reference_law: Reference):
        """
        :param Reference reference_law:
        """

        self.hybrid_shape_sweep_line.FirstLengthLaw = reference_law.com_object

    @property
    def first_length_law_inversion(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstLengthLawInversion() As long
                | 
                |     Returns or sets whether the first length law has to be
                |     inverted.
                |     Legal length law inversion values are:
                |     0 The length law has NOT to be inverted
                |     1 The length law has to be inverted

        :rtype: int
        """

        return self.hybrid_shape_sweep_line.FirstLengthLawInversion

    @first_length_law_inversion.setter
    def first_length_law_inversion(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_line.FirstLengthLawInversion = value

    @property
    def guide_deviation(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property GuideDeviation() As Length (Read Only)
                | 
                |     Returns the deviation value (length) from guide curves allowed during a
                |     sweeping operation in order to smooth it.

        :rtype: Length
        """

        return Length(self.hybrid_shape_sweep_line.GuideDeviation)

    @property
    def guide_deviation_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property GuideDeviationActivity() As boolean
                | 
                |     Returns or sets whether a deviation from guide curves is
                |     allowed.
                |     This property gives the information on performing smoothing during sweeping
                |     operation.
                |     TRUE if a deviation from guide curves is allowed, or FALSE otherwise (FALSE
                |     if not specified).

        :rtype: bool
        """

        return self.hybrid_shape_sweep_line.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_sweep_line.GuideDeviationActivity = value

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Mode() As long
                | 
                |     Returns or sets the linear sweep mode.
                |     Legal mode values are:
                |     0 Undefined linear profile swept surface
                |     (CATGSMLinearSweep_None)
                |     1 Linear profile swept surface defined by two guide curves
                |     (CATGSMLinearSweep_TwoGuides)
                |     2 Linear profile swept surface defined by a guide curve and an angle
                |     (CATGSMLinearSweep_GuideAndAngleCurve)
                |     3 Linear profile swept surface defined by a guide curve and a middle curve
                |     (CATGSMLinearSweep_GuideAndMiddle)
                |     4 Linear profile swept surface defined by a guide curve and an angle from
                |     a reference surface
                |     (CATGSMLinearSweep_GuideAndRefSurfaceAngle)
                |     5 Linear profile swept surface defined by a guide curve and a tangency
                |     surface (CATGSMLinearSweep_GuideAndTangencySurface)
                |     6 Linear profile swept surface defined by a guide curve and a draft
                |     directio (CATGSMLinearSweep_GuideAndDraftDirection)
                |     7 Linear profile swept surface defined by two tangency surfaces
                |     (CATGSMLinearSweep_TwoTangencySurfaces)

        :rtype: int
        """

        return self.hybrid_shape_sweep_line.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_line.Mode = value

    @property
    def second_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondGuideCrv() As Reference
                | 
                |     Returns or sets the sweep operation second guide curve.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_line.SecondGuideCrv)

    @second_guide_crv.setter
    def second_guide_crv(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_sweep_line.SecondGuideCrv = reference_curve.com_object

    @property
    def second_guide_surf(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondGuideSurf() As Reference
                | 
                |     Returns or sets the sweep operation second guide surface.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_line.SecondGuideSurf)

    @second_guide_surf.setter
    def second_guide_surf(self, reference_surface: Reference):
        """
        :param Reference reference_surface:
        """

        self.hybrid_shape_sweep_line.SecondGuideSurf = reference_surface.com_object

    @property
    def second_length_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondLengthLaw() As Reference
                | 
                |     Returns or sets second length law useful in some linear sweep types.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_line.SecondLengthLaw)

    @second_length_law.setter
    def second_length_law(self, reference_law: Reference):
        """
        :param Reference reference_law:
        """

        self.hybrid_shape_sweep_line.SecondLengthLaw = reference_law.com_object

    @property
    def second_length_law_inversion(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondLengthLawInversion() As long
                | 
                |     Returns or sets whether the second length law has to be
                |     inverted.
                |     Legal length law inversion values are:
                |     0 The length law has NOT to be inverted
                |     1 The length law has to be inverted

        :rtype: int
        """

        return self.hybrid_shape_sweep_line.SecondLengthLawInversion

    @second_length_law_inversion.setter
    def second_length_law_inversion(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_line.SecondLengthLawInversion = value

    @property
    def second_trim_option(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondTrimOption() As long
                | 
                |     Returns or sets the trim option for the second tangency
                |     surface.
                | 
                |     Legal trim option values are:
                |     0 No trim computed or trim undefined
                |     (CATGSMSweepTrimMode_None)
                |     1 Trim computed (CATGSMSweepTrimMode_On)

        :rtype: int
        """

        return self.hybrid_shape_sweep_line.SecondTrimOption

    @second_trim_option.setter
    def second_trim_option(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_line.SecondTrimOption = value

    @property
    def smooth_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothActivity() As boolean
                | 
                |     Returns whether the sweeping operation is smoothed.
                |     TRUE if the sweeping operation is smoothed, or FALSE otherwise (FALSE if
                |     not specified).

        :rtype: bool
        """

        return self.hybrid_shape_sweep_line.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_sweep_line.SmoothActivity = value

    @property
    def smooth_angle_threshold(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothAngleThreshold() As Angle (Read Only)
                | 
                |     Returns the angular threshold.

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_sweep_line.SmoothAngleThreshold)

    @property
    def solution_no(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SolutionNo() As long
                | 
                |     Returns or sets the choice number, which corresponds to each solution of a
                |     given linear sweep case.
                |     For example: a linear sweep with reference surface leads to four possible
                |     solutions.

        :rtype: int
        """

        return self.hybrid_shape_sweep_line.SolutionNo

    @solution_no.setter
    def solution_no(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_line.SolutionNo = value

    @property
    def spine(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Spine() As Reference
                | 
                |     Returns or sets the sweep operation spine (optional).

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_line.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        """
        :param Reference reference_spine:
        """

        self.hybrid_shape_sweep_line.Spine = reference_spine.com_object

    @property
    def trim_option(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TrimOption() As long
                | 
                |     Returns or sets the trim option.
                | 
                |     Legal trim option values are:
                |     0 No trim computed or trim undefined
                |     (CATGSMSweepTrimMode_None)
                |     1 Trim computed (CATGSMSweepTrimMode_On)

        :rtype: int
        """

        return self.hybrid_shape_sweep_line.TrimOption

    @trim_option.setter
    def trim_option(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_line.TrimOption = value

    def add_draft_angle_definition_location(self, ip_ia_loc_elem: Reference, i_ang: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddDraftAngleDefinitionLocation(Reference ipIALocElem,
                | double iAng)
                | 
                |     Adds a draft angle location.
                | 
                |     Parameters:
                | 
                |         ipIALocElem
                |             The geometric element where the draft angle applies
                |             
                |         iAng
                |             The draft angle

        :param Reference ip_ia_loc_elem:
        :param float i_ang:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.AddDraftAngleDefinitionLocation(ip_ia_loc_elem.com_object, i_ang)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_draft_angle_definition_location'
        # # vba_code = """
        # # Public Function add_draft_angle_definition_location(hybrid_shape_sweep_line)
        # #     Dim ipIALocElem (2)
        # #     hybrid_shape_sweep_line.AddDraftAngleDefinitionLocation ipIALocElem
        # #     add_draft_angle_definition_location = ipIALocElem
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_angle(self, i_i: int) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAngle(long iI) As Angle
                | 
                |     Returns the angle values useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The angle value index 
                | 
                |     Returns:
                |         The angle value

        :param int i_i:
        :rtype: Angle
        """
        return Angle(self.hybrid_shape_sweep_line.GetAngle(i_i))

    def get_angular_law(self, op_start_ang: Angle, op_end_ang: Angle, o_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetAngularLaw(Angle opStartAng,
                | Angle opEndAng,
                | long oLawType)
                | 
                |     Retrieves the angular law useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         opStartAng
                |             The angular law start value 
                |         opEndAng
                |             The angular law end value 
                |         oLawType
                |             The angular law type
                |             Legal angular law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param Angle op_start_ang:
        :param Angle op_end_ang:
        :param int o_law_type:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetAngularLaw(op_start_ang.com_object, op_end_ang.com_object, o_law_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_angular_law'
        # # vba_code = """
        # # Public Function get_angular_law(hybrid_shape_sweep_line)
        # #     Dim opStartAng (2)
        # #     hybrid_shape_sweep_line.GetAngularLaw opStartAng
        # #     get_angular_law = opStartAng
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_choice_nb_surfaces(self, o_surf_ori1: int, o_surf_ori2: int, o_surf_coupl_ori1: int, o_surf_coupl_ori2: int,
                               o_no: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetChoiceNbSurfaces(long oSurfOri1,
                | long oSurfOri2,
                | long oSurfCouplOri1,
                | long oSurfCouplOri2,
                | long oNo)
                | 
                |     Gets a sequence which identifies a solution amongst all possibilities of a
                |     line-profile swept surface, case
                |     CATGSMLinearSweep_TwoTangencySurfaces.
                | 
                |     Parameters:
                | 
                |         oSurfOri1
                |             This orientation determines the location of the results with regard
                |             to the first surface. Possible values are:
                |             * +1 : the result is in the semi-space defined by the normal to the surface,
                |             * -1 : the result is in the semi-space defined by the opposite to the normal to the
                |                    surface,
                |             * 0 : no orientation is specified, all the results are output,
                |             * 2 : the result changes of semi-space along the spine.
                |         oSurfOri2
                |             This orientation determines the location of the results with regard
                |             to the second surface. Possible values are as for oSurfOri1.
                |             
                |         oSurfCouplOri1
                |             This orientation determines the location of the results with regard
                |             to the trihedron defined by the the spine, the normal to the first surface and
                |             the tangent to the linear profile. Possible values
                |             are:
                |             * +1 : the output results are such that the triedron is counter clockwise,
                |             * -1 : the output results are such that the triedron is clockwise,
                |             * 0 : no orientation is specified, all the results are output,
                |             * 2 : the orientation of the trihedron changes along the spine. 
                |         oSurfCouplOri2
                |             This orientation determines the location of the results with regard
                |             to the trihedron defined by the the spine, the normal to the second surface and
                |             the tangent to the linear profile. Possible values are as for oSurfCouplOri1.
                |             
                |         oNo
                |             Given the previous orientations, solution number in a distance
                |             ordered list.

        :param int o_surf_ori1:
        :param int o_surf_ori2:
        :param int o_surf_coupl_ori1:
        :param int o_surf_coupl_ori2:
        :param int o_no:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetChoiceNbSurfaces(o_surf_ori1, o_surf_ori2, o_surf_coupl_ori1,
                                                                o_surf_coupl_ori2, o_no)

    def get_choice_no(self, o_val1: int, o_val2: int, o_val3: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetChoiceNo(long oVal1,
                | long oVal2,
                | long oVal3)
                | 
                |     Retrieves the choice number associated with each solution of a given linear
                |     sweep case.
                |     Example: a linear sweep with one guide curve and a tangency surface may
                |     lead to several possible solutions.
                | 
                |     Parameters:
                | 
                |         oVal1
                |             The solution number (from 1 to n) 
                |         oVal2
                |             In the example, the shell orientation : -1, +1 or 0 (both +1 and -1) 
                |         val3
                |             In the example, the wire orientation : -1, +1 or 0 (both +1 and -1)

        :param int o_val1:
        :param int o_val2:
        :param int o_val3:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetChoiceNo(o_val1, o_val2, o_val3)

    def get_draft_angle_definition_location(self, i_loc: int, op_ia_element: Reference, o_angle: Angle) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetDraftAngleDefinitionLocation(long iLoc,
                | Reference opIAElement,
                | Angle oAngle)
                | 
                |     Retrieves the draft angle location element.
                | 
                |     Parameters:
                | 
                |         iLoc
                |             The draft angle location position in the list 
                |         opIAElement
                |             The geometric element at that location and where the draft angle
                |             applies 
                |         oAngle
                |             The draft angle

        :param int i_loc:
        :param Reference op_ia_element:
        :param Angle o_angle:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetDraftAngleDefinitionLocation(i_loc, op_ia_element.com_object,
                                                                            o_angle.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_draft_angle_definition_location'
        # # vba_code = """
        # # Public Function get_draft_angle_definition_location(hybrid_shape_sweep_line)
        # #     Dim iLoc (2)
        # #     hybrid_shape_sweep_line.GetDraftAngleDefinitionLocation iLoc
        # #     get_draft_angle_definition_location = iLoc
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_draft_angle_definition_locations_nb(self, o_count: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetDraftAngleDefinitionLocationsNb(long oCount)
                | 
                |     Retrieves the draft angle location list size.
                | 
                |     Parameters:
                | 
                |         oCount
                |             The draft angle location list size

        :param int o_count:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetDraftAngleDefinitionLocationsNb(o_count)

    def get_first_length_definition_type(self, o_first_type: int, op_ia_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetFirstLengthDefinitionType(long oFirstType,
                | Reference opIAElem)
                | 
                |     Retrieves the first length definition type.
                | 
                |     Parameters:
                | 
                |         oFirstType
                |             The first length definition type
                |             Legal length definition types are:
                |             0 Undefined length type
                |             (CATGSMLinearSweepLengthType_None)
                |             1 Length of the swept line in the sweeping plane from the guide
                |             curve (CATGSMLinearSweepLengthType_Standard)
                |             2 No numerical value is required, equivalent to standard length at
                |             zero (CATGSMLinearSweepLengthType_FromCurve)
                |             3 Up to or from a geometrical reference (a surface)
                |             (CATGSMLinearSweepLengthType_Reference)
                |             4 Only for draft surfaces, the length is computed in the draft
                |             direction from an extremum point on the guide curve
                |             (CATGSMLinearSweepLengthType_FromExtremum)
                |             5 Only for draft surfaces, the length will be used in a way
                |             similar to euclidean parallel curve distance on the swept surface
                |             (CATGSMLinearSweepLengthType_AlongSurface)
                |         opIAElem
                |             The geometric element where the first length definition type
                |             applies

        :param int o_first_type:
        :param Reference op_ia_elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetFirstLengthDefinitionType(o_first_type, op_ia_elem.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_first_length_definition_type'
        # # vba_code = """
        # # Public Function get_first_length_definition_type(hybrid_shape_sweep_line)
        # #     Dim oFirstType (2)
        # #     hybrid_shape_sweep_line.GetFirstLengthDefinitionType oFirstType
        # #     get_first_length_definition_type = oFirstType
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_first_length_law(self, o_length1: Length, o_length2: Length, o_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetFirstLengthLaw(Length oLength1,
                | Length oLength2,
                | long oLawType)
                | 
                |     Retrieves the first length law useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         oLength1
                |             The length law start value 
                |         oLength2
                |             The length law end value 
                |         oLawType
                |             The length law type
                |             Legal length law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param Length o_length1:
        :param Length o_length2:
        :param int o_law_type:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetFirstLengthLaw(o_length1.com_object, o_length2.com_object, o_law_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_first_length_law'
        # # vba_code = """
        # # Public Function get_first_length_law(hybrid_shape_sweep_line)
        # #     Dim oLength1 (2)
        # #     hybrid_shape_sweep_line.GetFirstLengthLaw oLength1
        # #     get_first_length_law = oLength1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_length(self, i_i: int) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetLength(long iI) As Length
                | 
                |     Returns the length values useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The length value index 
                | 
                |     Returns:
                |         The length value

        :param int i_i:
        :rtype: Length
        """
        return Length(self.hybrid_shape_sweep_line.GetLength(i_i))

    def get_length_law_types(self, o_first_type: int, o_second_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetLengthLawTypes(long oFirstType,
                | long oSecondType)
                | 
                |     Gets length law types.
                | 
                |     Parameters:
                | 
                |         oFirstType
                |             First type of law. 
                |         oSecondType
                |             Second type of law. oFirstType and oSecondType
                |             0 : Undefined law type
                |             1 : Constant law type
                |             2 : Linear law type
                |             3 : S law type
                |             4 : Law specified by a GSD law feature
                |             5 : Law specified by a set of points and parameters

        :param int o_first_type:
        :param int o_second_type:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetLengthLawTypes(o_first_type, o_second_type)

    def get_longitudinal_relimiters(self, op_ia_elem1: Reference, op_ia_elem2: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetLongitudinalRelimiters(Reference opIAElem1,
                | Reference opIAElem2)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepLine#GetRelimiters Retrieves the elements
                |         relimiting the spine (or the default spine). 
                |     Parameters:
                | 
                |         opIAElem1
                |             The first relimiting feature (plane or point) 
                |         opIAElem2
                |             The second relimiting feature (plane or point)

        :param Reference op_ia_elem1:
        :param Reference op_ia_elem2:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetLongitudinalRelimiters(op_ia_elem1.com_object, op_ia_elem2.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_longitudinal_relimiters'
        # # vba_code = """
        # # Public Function get_longitudinal_relimiters(hybrid_shape_sweep_line)
        # #     Dim opIAElem1 (2)
        # #     hybrid_shape_sweep_line.GetLongitudinalRelimiters opIAElem1
        # #     get_longitudinal_relimiters = opIAElem1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_nb_angle(self, o_ang: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetNbAngle(long oAng)
                | 
                |     Retrieves the number of angles.
                | 
                |     Parameters:
                | 
                |         oAng
                |             The number of angles

        :param int o_ang:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetNbAngle(o_ang)

    def get_nb_guide_crv(self, o_num: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetNbGuideCrv(long oNum)
                | 
                |     Retrieves the number of guides curves.
                | 
                |     Parameters:
                | 
                |         oNum
                |             The number of guide curves

        :param int o_num:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetNbGuideCrv(o_num)

    def get_nb_guide_sur(self, o_num: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetNbGuideSur(long oNum)
                | 
                |     Retrieves the number of guide surfaces.
                | 
                |     Parameters:
                | 
                |         oNum
                |             The number of guides surfaces

        :param int o_num:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetNbGuideSur(o_num)

    def get_nb_length(self, o_len: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetNbLength(long oLen)
                | 
                |     Retrieves the number of lengths.
                | 
                |     Parameters:
                | 
                |         oLen
                |             The number of lengths

        :param int o_len:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetNbLength(o_len)

    def get_relimiters(self, op_ia_elem1: Reference, op_orient1: int, op_ia_elem2: Reference, op_orient2: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetRelimiters(Reference opIAElem1,
                | long opOrient1,
                | Reference opIAElem2,
                | long opOrient2)
                | 
                |     Retrieves the elements relimiting the spine (or the default
                |     spine).
                | 
                |     Parameters:
                | 
                |         opIAElem1
                |             The first relimiting feature (plane or point) 
                |         opOrient1
                |             Split direction for the first relimitation
                |             0 means that the beginning of the spine (considering its
                |             orientation) is removed, 1 means that the end of the spine is removed
                |             
                |         opIAElem2
                |             The second relimiting feature (plane or point) 
                |         opOrient2
                |             Split direction for the second relimitation

        :param Reference op_ia_elem1:
        :param int op_orient1:
        :param Reference op_ia_elem2:
        :param int op_orient2:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetRelimiters(op_ia_elem1.com_object, op_orient1, op_ia_elem2.com_object,
                                                          op_orient2)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_relimiters'
        # # vba_code = """
        # # Public Function get_relimiters(hybrid_shape_sweep_line)
        # #     Dim opIAElem1 (2)
        # #     hybrid_shape_sweep_line.GetRelimiters opIAElem1
        # #     get_relimiters = opIAElem1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_second_length_definition_type(self, o_second_type: int, op_ia_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSecondLengthDefinitionType(long oSecondType,
                | Reference opIAElem)
                | 
                |     Retrieves the second length definition type.
                | 
                |     Parameters:
                | 
                |         oSecondType
                |             The second length definition type
                |             Legal length definition types are:
                |             0 Undefined length type
                |             (CATGSMLinearSweepLengthType_None)
                |             1 Length of the swept line in the sweeping plane from the guide
                |             curve (CATGSMLinearSweepLengthType_Standard)
                |             2 No numerical value is required, equivalent to standard length at
                |             zero (CATGSMLinearSweepLengthType_FromCurve)
                |             3 Up to or from a geometrical reference (a surface)
                |             (CATGSMLinearSweepLengthType_Reference)
                |             4 Only for draft surfaces, the length is computed in the draft
                |             direction from an extremum point on the guide curve
                |             (CATGSMLinearSweepLengthType_FromExtremum)
                |             5 Only for draft surfaces, the length will be used in a way
                |             similar to euclidean parallel curve distance on the swept surface
                |             (CATGSMLinearSweepLengthType_AlongSurface)
                |         opIAElem
                |             The geometric element where the second length definition type
                |             applies

        :param int o_second_type:
        :param Reference op_ia_elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetSecondLengthDefinitionType(o_second_type, op_ia_elem.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_second_length_definition_type'
        # # vba_code = """
        # # Public Function get_second_length_definition_type(hybrid_shape_sweep_line)
        # #     Dim oSecondType (2)
        # #     hybrid_shape_sweep_line.GetSecondLengthDefinitionType oSecondType
        # #     get_second_length_definition_type = oSecondType
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_second_length_law(self, o_length1: Length, o_length2: Length, o_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetSecondLengthLaw(Length oLength1,
                | Length oLength2,
                | long oLawType)
                | 
                |     Retrieves the second length law useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         oLength1
                |             The length law start value 
                |         oLength2
                |             The length law end value 
                |         oLawType
                |             The length law type
                |             Legal length law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param Length o_length1:
        :param Length o_length2:
        :param int o_law_type:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.GetSecondLengthLaw(o_length1.com_object, o_length2.com_object, o_law_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_second_length_law'
        # # vba_code = """
        # # Public Function get_second_length_law(hybrid_shape_sweep_line)
        # #     Dim oLength1 (2)
        # #     hybrid_shape_sweep_line.GetSecondLengthLaw oLength1
        # #     get_second_length_law = oLength1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def insert_draft_angle_definition_location(self, i_elem: Reference, i_angle: Angle, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertDraftAngleDefinitionLocation(Reference iElem,
                | Angle iAngle,
                | long iPos)
                | 
                |     Inserts a geometrical element and a value necessary for draft angle
                |     definition after a given position in the lists.
                | 
                |     Parameters:
                | 
                |         iElem
                |             Geometrical element 
                |         iAngle
                |             Angular parameter 
                |         iPos
                |             Position in lists. To insert in the beginning of the list put iPos = 0.

        :param Reference i_elem:
        :param Angle i_angle:
        :param int i_pos:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.InsertDraftAngleDefinitionLocation(i_elem.com_object, i_angle.com_object,
                                                                               i_pos)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'insert_draft_angle_definition_location'
        # # vba_code = """
        # # Public Function insert_draft_angle_definition_location(hybrid_shape_sweep_line)
        # #     Dim iElem (2)
        # #     hybrid_shape_sweep_line.InsertDraftAngleDefinitionLocation iElem
        # #     insert_draft_angle_definition_location = iElem
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_all_draft_angle_definition_locations(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveAllDraftAngleDefinitionLocations()
                | 
                |     Removes all geometrical elements and values necessary for draft angle
                |     definition.

        :rtype: None
        """
        return self.hybrid_shape_sweep_line.RemoveAllDraftAngleDefinitionLocations()

    def remove_angle(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveAngle()
                | 
                |     Removes an angle.

        :rtype: None
        """
        return self.hybrid_shape_sweep_line.RemoveAngle()

    def remove_draft_angle_definition_location_position(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveDraftAngleDefinitionLocationPosition(long iPos)
                | 
                |     Removes a draft angle location.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position in the list of the draft angle location to
                |             remove

        :param int i_pos:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.RemoveDraftAngleDefinitionLocationPosition(i_pos)

    def remove_guide_crv(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveGuideCrv()
                | 
                |     Removes a guide curve.

        :rtype: None
        """
        return self.hybrid_shape_sweep_line.RemoveGuideCrv()

    def remove_guide_sur(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveGuideSur()
                | 
                |     Removes a guide surface.

        :rtype: None
        """
        return self.hybrid_shape_sweep_line.RemoveGuideSur()

    def remove_length(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveLength()
                | 
                |     Removes a length.

        :rtype: None
        """
        return self.hybrid_shape_sweep_line.RemoveLength()

    def set_angle(self, i_i: int, i_elem: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAngle(long iI,
                | double iElem)
                | 
                |     Sets the angle values useful in some linear sweep types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The angle value index 
                |         iElem
                |             The angle value

        :param int i_i:
        :param float i_elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetAngle(i_i, i_elem)

    def set_angular_law(self, i_start_ang: float, i_end_ang: float, i_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAngularLaw(double iStartAng,
                | double iEndAng,
                | long iLawType)
                | 
                |     Sets the angular law useful in some linear sweep types.
                | 
                |     Parameters:
                | 
                |         iStartAng
                |             The angular law start value 
                |         iEndAng
                |             The angular law end value 
                |         iLawType
                |             The angular law type
                |             Legal angular law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param float i_start_ang:
        :param float i_end_ang:
        :param int i_law_type:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetAngularLaw(i_start_ang, i_end_ang, i_law_type)

    def set_choice_nb_surfaces(self, i_surf_ori1: int, i_surf_ori2: int, i_surf_coupl_ori1: int, i_surf_coupl_ori2: int,
                               i_no: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetChoiceNbSurfaces(long iSurfOri1,
                | long iSurfOri2,
                | long iSurfCouplOri1,
                | long iSurfCouplOri2,
                | long iNo)
                | 
                |     Sets a sequence which identifies a solution amongst all possibilities of a
                |     line-profile swept surface, case
                |     CATGSMLinearSweep_TwoTangencySurfaces.
                | 
                |     Parameters:
                | 
                |         iSurfOri1
                |             This orientation determines the location of the results with regard
                |             to the first surface. Possible values are:
                |             * +1 : the result is in the semi-space defined by the normal to the surface,
                |             * -1 : the result is in the semi-space defined by the opposite to the normal to the ,
                |             * 0 : no orientation is specified, all the results are output,
                |             * 2 : the result changes of semi-space along the spine.
                |         iSurfOri2
                |             This orientation determines the location of the results with regard
                |             to the second surface. Possible values are as for iSurfOri1.
                |             
                |         iSurfCouplOri1
                |             This orientation determines the location of the results with regard
                |             to the trihedron defined by the the spine, the normal to the first surface and
                |             the tangent to the linear profile. Possible values
                |             are:
                |             * +1 : the output results are such that the triedron is counter clockwise,
                |             * -1 : the output results are such that the triedron is clockwise,
                |             * 0 : no orientation is specified, all the results are output,
                |             * 2 : the orientation of the trihedron changes along the spine. 
                |         iSurfCouplOri2
                |             This orientation determines the location of the results with regard
                |             to the trihedron defined by the the spine, the normal to the second surface and
                |             the tangent to the linear profile. Possible values are as for iSurfCouplOri2.
                |             
                |         iNo
                |             Given the previous orientations, solution number in a distance
                |             ordered list.

        :param int i_surf_ori1:
        :param int i_surf_ori2:
        :param int i_surf_coupl_ori1:
        :param int i_surf_coupl_ori2:
        :param int i_no:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetChoiceNbSurfaces(i_surf_ori1, i_surf_ori2, i_surf_coupl_ori1,
                                                                i_surf_coupl_ori2, i_no)

    def set_choice_no(self, i_val1: int, i_val2: int, i_val3: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetChoiceNo(long iVal1,
                | long iVal2,
                | long iVal3)
                | 
                |     Sets the choice number associated with each solution of a given linear
                |     sweep case.
                |     Example: a linear sweep with one guide curve and a tangency surface may
                |     lead to several possible solutions.
                | 
                |     Parameters:
                | 
                |         iVal1
                |             The solution number (from 1 to n) 
                |         iVal2
                |             In the example, the shell orientation : -1, +1 or 0 (both +1 and -1) 
                |         iVal3
                |             In the example, the wire orientation : -1, +1 or 0 (both +1 and -1)

        :param int i_val1:
        :param int i_val2:
        :param int i_val3:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetChoiceNo(i_val1, i_val2, i_val3)

    def set_first_length_definition_type(self, i_first_type: int, ip_ia_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFirstLengthDefinitionType(long iFirstType,
                | Reference ipIAElem)
                | 
                |     Sets the first length definition type.
                | 
                |     Parameters:
                | 
                |         iFirstType
                |             The first length definition type
                |             Legal length definition types are:
                |             0 Undefined length type
                |             (CATGSMLinearSweepLengthType_None)
                |             1 Length of the swept line in the sweeping plane from the guide
                |             curve (CATGSMLinearSweepLengthType_Standard)
                |             2 No numerical value is required, equivalent to standard length at
                |             zero (CATGSMLinearSweepLengthType_FromCurve)
                |             3 Up to or from a geometrical reference (a surface)
                |             (CATGSMLinearSweepLengthType_Reference)
                |             4 Only for draft surfaces, the length is computed in the draft
                |             direction from an extremum point on the guide curve
                |             (CATGSMLinearSweepLengthType_FromExtremum)
                |             5 Only for draft surfaces, the length will be used in a way
                |             similar to euclidean parallel curve distance on the swept surface
                |             (CATGSMLinearSweepLengthType_AlongSurface)
                |         ipIAElem
                |             The geometric element where the first length definition type
                |             applies

        :param int i_first_type:
        :param Reference ip_ia_elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetFirstLengthDefinitionType(i_first_type, ip_ia_elem.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_first_length_definition_type'
        # # vba_code = """
        # # Public Function set_first_length_definition_type(hybrid_shape_sweep_line)
        # #     Dim iFirstType (2)
        # #     hybrid_shape_sweep_line.SetFirstLengthDefinitionType iFirstType
        # #     set_first_length_definition_type = iFirstType
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_first_length_law(self, i_length1: float, i_length2: float, i_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFirstLengthLaw(double iLength1,
                | double iLength2,
                | long iLawType)
                | 
                |     Sets the first length law useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iLength1
                |             The length law start value 
                |         iLength2
                |             The length law end value 
                |         iLawType
                |             The length law type
                |             Legal length law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param float i_length1:
        :param float i_length2:
        :param int i_law_type:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetFirstLengthLaw(i_length1, i_length2, i_law_type)

    def set_guide_deviation(self, i_length: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetGuideDeviation(double iLength)
                | 
                |     Sets the deviation value (length) from guide curves allowed during sweeping
                |     operation in order to smooth it.
                | 
                |     Parameters:
                | 
                |         iLength
                |             The deviation value

        :param float i_length:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetGuideDeviation(i_length)

    def set_length(self, i_i: int, i_elem: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLength(long iI,
                | double iElem)
                | 
                |     Sets the linear values useful in some linear sweep types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The linear value index 
                |         iElem
                |             The linear value

        :param int i_i:
        :param float i_elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetLength(i_i, i_elem)

    def set_length_law_types(self, i_first_type: int, i_second_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLengthLawTypes(long iFirstType,
                | long iSecondType)
                | 
                |     Sets length law types.
                | 
                |     Parameters:
                | 
                |         iFirstType
                |             First type of law. 
                |         iSecondType
                |             Second type of law. iFirstType and iSecondType
                |             0 : Undefined law type
                |             1 : Constant law type
                |             2 : Linear law type
                |             3 : S law type
                |             4 : Law specified by a GSD law feature
                |             5 : Law specified by a set of points and parameters

        :param int i_first_type:
        :param int i_second_type:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetLengthLawTypes(i_first_type, i_second_type)

    def set_longitudinal_relimiters(self, ip_ia_elem1: Reference, ip_ia_elem2: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLongitudinalRelimiters(Reference ipIAElem1,
                | Reference ipIAElem2)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepLine#SetRelimiters Sets the elements
                |         relimiting the spine (or the default spine). 
                |     Parameters:
                | 
                |         ipIAElem1
                |             The first relimiting feature (plane or point) 
                |         ipIAElem2
                |             The second relimiting feature (plane or point)

        :param Reference ip_ia_elem1:
        :param Reference ip_ia_elem2:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetLongitudinalRelimiters(ip_ia_elem1.com_object, ip_ia_elem2.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_longitudinal_relimiters'
        # # vba_code = """
        # # Public Function set_longitudinal_relimiters(hybrid_shape_sweep_line)
        # #     Dim ipIAElem1 (2)
        # #     hybrid_shape_sweep_line.SetLongitudinalRelimiters ipIAElem1
        # #     set_longitudinal_relimiters = ipIAElem1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_relimiters(self, ip_ia_elem1: Reference, ip_orient1: int, ip_ia_elem2: Reference, ip_orient2: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRelimiters(Reference ipIAElem1,
                | long ipOrient1,
                | Reference ipIAElem2,
                | long ipOrient2)
                | 
                |     Sets the elements relimiting the spine (or the default
                |     spine).
                | 
                |     Parameters:
                | 
                |         ipIAElem1
                |             The first relimiting feature (plane or point) 
                |         ipOrient1
                |             Split direction for the first relimitation
                |             0 means that the beginning of the spine (considering its
                |             orientation) is removed, 1 means that the end of the spine is removed
                |             
                |         ipIAElem2
                |             The second relimiting feature (plane or point) 
                |         ipOrient2
                |             Split direction for the second relimitation

        :param Reference ip_ia_elem1:
        :param int ip_orient1:
        :param Reference ip_ia_elem2:
        :param int ip_orient2:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetRelimiters(ip_ia_elem1.com_object, ip_orient1, ip_ia_elem2.com_object,
                                                          ip_orient2)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_relimiters'
        # # vba_code = """
        # # Public Function set_relimiters(hybrid_shape_sweep_line)
        # #     Dim ipIAElem1 (2)
        # #     hybrid_shape_sweep_line.SetRelimiters ipIAElem1
        # #     set_relimiters = ipIAElem1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_second_length_definition_type(self, i_second_type: int, ip_ia_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSecondLengthDefinitionType(long iSecondType,
                | Reference ipIAElem)
                | 
                |     Sets the second length definition type.
                | 
                |     Parameters:
                | 
                |         iSecondType
                |             The second length definition type
                |             Legal length definition types are:
                |             0 Undefined length type
                |             (CATGSMLinearSweepLengthType_None)
                |             1 Length of the swept line in the sweeping plane from the guide
                |             curve (CATGSMLinearSweepLengthType_Standard)
                |             2 No numerical value is required, equivalent to standard length at
                |             zero (CATGSMLinearSweepLengthType_FromCurve)
                |             3 Up to or from a geometrical reference (a surface)
                |             (CATGSMLinearSweepLengthType_Reference)
                |             4 Only for draft surfaces, the length is computed in the draft
                |             direction from an extremum point on the guide curve
                |             (CATGSMLinearSweepLengthType_FromExtremum)
                |             5 Only for draft surfaces, the length will be used in a way
                |             similar to euclidean parallel curve distance on the swept surface
                |             (CATGSMLinearSweepLengthType_AlongSurface)
                |         ipIAElem
                |             The geometric element where the second length definition type
                |             applies

        :param int i_second_type:
        :param Reference ip_ia_elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetSecondLengthDefinitionType(i_second_type, ip_ia_elem.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_second_length_definition_type'
        # # vba_code = """
        # # Public Function set_second_length_definition_type(hybrid_shape_sweep_line)
        # #     Dim iSecondType (2)
        # #     hybrid_shape_sweep_line.SetSecondLengthDefinitionType iSecondType
        # #     set_second_length_definition_type = iSecondType
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_second_length_law(self, i_length1: float, i_length2: float, i_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSecondLengthLaw(double iLength1,
                | double iLength2,
                | long iLawType)
                | 
                |     Sets the second length law useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iLength1
                |             The length law start value 
                |         iLength2
                |             The length law end value 
                |         iLawType
                |             The length law type
                |             Legal length law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param float i_length1:
        :param float i_length2:
        :param int i_law_type:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetSecondLengthLaw(i_length1, i_length2, i_law_type)

    def set_smooth_angle_threshold(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSmoothAngleThreshold(double iAngle)
                | 
                |     Sets the angular threshold.
                | 
                |     Parameters:
                | 
                |         iAngle
                |             The angle numerical value

        :param float i_angle:
        :rtype: None
        """
        return self.hybrid_shape_sweep_line.SetSmoothAngleThreshold(i_angle)

    def __repr__(self):
        return f'HybridShapeSweepLine(name="{self.name}")'
