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


class HybridShapeSweepExplicit(HybridShapeSweep):
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
                |                             HybridShapeSweepExplicit
                | 
                | Represents the hybrid shape Sweep explicit feature object.
                | Role: To access the data of the hybrid shape sweep explicit feature
                | object.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep_explicit = com_object

    @property
    def angle_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AngleLaw() As Reference
                | 
                |     Returns or sets the angle law feature associated to the reference
                |     surface.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Angle law element. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_explicit.AngleLaw)

    @angle_law.setter
    def angle_law(self, reference_law: Reference):
        """
        :param Reference reference_law:
        """

        self.hybrid_shape_sweep_explicit.AngleLaw = reference_law.com_object

    @property
    def angle_law_inversion(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AngleLawInversion() As long
                | 
                |     Returns or sets the angle law inversion information.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Angle law inversion information. 
                | 
                |     See also:
                |         HybridShapeFactory

        :rtype: int
        """

        return self.hybrid_shape_sweep_explicit.AngleLawInversion

    @angle_law_inversion.setter
    def angle_law_inversion(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_explicit.AngleLawInversion = value

    @property
    def angle_law_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property AngleLawType() As long
                | 
                |     Returns or sets the angle law type associated to the reference
                |     surface.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Angle law type. 
                | 
                |     See also:
                |         HybridShapeFactory

        :rtype: int
        """

        return self.hybrid_shape_sweep_explicit.AngleLawType

    @angle_law_type.setter
    def angle_law_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_explicit.AngleLawType = value

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

        return self.hybrid_shape_sweep_explicit.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_explicit.CanonicalDetection = value

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

        return self.hybrid_shape_sweep_explicit.Context

    @context.setter
    def context(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_explicit.Context = value

    @property
    def first_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstGuideCrv() As Reference
                | 
                |     Gets the first guide curve.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Guide curve. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_explicit.FirstGuideCrv)

    @first_guide_crv.setter
    def first_guide_crv(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_sweep_explicit.FirstGuideCrv = reference_curve.com_object

    @property
    def guide_deviation(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property GuideDeviation() As Length (Read Only)
                | 
                |     Returns deviation value (length) from guide curves allowed during sweeping
                |     operation in order to smooth it.

        :rtype: Length
        """

        return Length(self.hybrid_shape_sweep_explicit.GuideDeviation)

    @property
    def guide_deviation_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property GuideDeviationActivity() As boolean
                | 
                |     Returns or sets information whether a deviation from guide curves is
                |     allowed or not.
                |     Gives the information on performing smoothing during sweeping
                |     operation.
                |     TRUE or FALSE (FALSE if not specified).

        :rtype: bool
        """

        return self.hybrid_shape_sweep_explicit.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_sweep_explicit.GuideDeviationActivity = value

    @property
    def guide_projection(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property GuideProjection() As boolean
                | 
                |     Returns or sets the projection of the guide curve onto the reference plane
                |     in order to use it as spine, in pulling direction case only. Removes Spine if
                |     GuideProjection is set to TRUE.
                |     Legal values: True projection is required and False if not
                | 
                |     Example:
                | 
                |           This example sets that the GuideProjection mode of
                |          the Sweep hybrid shape sweep explicit feature to
                |          True.
                |          
                | 
                |          Sweep.GuideProjection = True

        :rtype: bool
        """

        return self.hybrid_shape_sweep_explicit.GuideProjection

    @guide_projection.setter
    def guide_projection(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_sweep_explicit.GuideProjection = value

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Mode() As long
                | 
                |     Returns or sets positioning mode used for the profile.
                | 
                |     Parameters:
                | 
                |         oElem
                | 
                |             Values :
                |             = 1 - CATGSMPositionMode_NoneOrPositioned : no positioning,
                | 
                |             = 2 - CATGSMPositionMode_ExplicitSweep : the explicit profile is to be moved from its
                |                   initial plane to the first sweep plane,
                | 
                |             = 3 - CATGSMPositionMode_Develop : === DO NOT USE IN THIS CASE === 
                | 
                |     See also:
                |         HybridShapeFactory

        :rtype: int
        """

        return self.hybrid_shape_sweep_explicit.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_explicit.Mode = value

    @property
    def position_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PositionMode() As long
                | 
                |     Returns or sets positioning mode.
                |     Legal values:
                | 
                |     0
                |         CATGSMPositionMode_NoneOrPositioned. 
                |     1
                |         CATGSMPositionMode_ExplicitSweep. if a positioning operation is
                |         done.
                | 
                | Example:
                |     This example retrieves in oPosMode the position mode for the Sweep hybrid
                |     shape feature.
                | 
                |      oPosMode = Sweep.PositionMode

        :rtype: int
        """

        return self.hybrid_shape_sweep_explicit.PositionMode

    @position_mode.setter
    def position_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_explicit.PositionMode = value

    @property
    def positioned_profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PositionedProfile() As Reference
                | 
                |     Returns or sets the positioning transformation associated to the explicit
                |     swept surface and which result corresponds to the positioned
                |     profile.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Positioning transformation / positioned profile. return value for
                |             CATScript applications, with (IDLRETVAL) function type
                |             
                | 
                |     See also:
                |         Reference 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_explicit.PositionedProfile)

    @positioned_profile.setter
    def positioned_profile(self, reference_profile: Reference):
        """
        :param Reference reference_profile:
        """

        self.hybrid_shape_sweep_explicit.PositionedProfile = reference_profile.com_object

    @property
    def profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Profile() As Reference
                | 
                |     Gets the profile to be swept out.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Profile element. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_explicit.Profile)

    @profile.setter
    def profile(self, reference_profile: Reference):
        """
        :param Reference reference_profile:
        """

        self.hybrid_shape_sweep_explicit.Profile = reference_profile.com_object

    @property
    def profile_x_axis_computation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ProfileXAxisComputationMode() As long
                | 
                |     Returns or sets the computation mode of the X axis (or direction) of the
                |     initial axis system (on the profile). Default value is
                |     CATGSMPositionDirCompMode_None when PosDirection(OutputDirection) is not
                |     specified and CATGSMPositionDirCompMode_User if OutputDirection is
                |     specified.
                |     Legal values:
                | 
                |     0
                |         CATGSMPositionDirCompMode_None. No X axis specified. 
                |     1
                |         CATGSMPositionDirCompMode_Tangent: the X axis is implicitly the tangent
                |         of the profile at the origin (the origin then HAS to be on the
                |         profile)
                |     2
                |         CATGSMPositionDirCompMode_User: the X axis is specified by a direction
                |         via SetPosDirection(UserInputDirection, 1)
                | 
                | Example:
                |     This example retrieves in oDirCompMode the Profile X Axis ComputationMode
                |     for the Sweep hybrid shape feature.
                | 
                |      oDirCompMode = Sweep.ProfileXAxisComputationMode

        :rtype: int
        """

        return self.hybrid_shape_sweep_explicit.ProfileXAxisComputationMode

    @profile_x_axis_computation_mode.setter
    def profile_x_axis_computation_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_explicit.ProfileXAxisComputationMode = value

    @property
    def pulling_direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property PullingDirection() As HybridShapeDirection
                | 
                |     Gets or sets the pulling direction
                |     If the direction is specified, the plane normal to this direction is taken
                |     as reference surface.
                | 
                |     Example:
                |         This example retrieves in ohDir the pulling direction feature for the
                |         Sweep hybrid shape feature.
                | 
                |          Dim ohDir As CATIAHybridShapeDirection
                |          Set ohDir = Sweep.PullingDirection

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_sweep_explicit.PullingDirection)

    @pulling_direction.setter
    def pulling_direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_sweep_explicit.PullingDirection = direction.com_object

    @property
    def reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Reference() As Reference
                | 
                |     Returns or sets the reference surface (optional).
                | 
                |     Parameters:
                | 
                |         oElem
                |             Reference surface. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_explicit.Reference)

    @reference.setter
    def reference(self, reference: Reference):
        """
        :param Reference reference:
        """

        self.hybrid_shape_sweep_explicit.Reference = reference.com_object

    @property
    def second_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondGuideCrv() As Reference
                | 
                |     Gets the second guide curve (optional).
                | 
                |     Parameters:
                | 
                |         oElem
                |             Guide curve. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_explicit.SecondGuideCrv)

    @second_guide_crv.setter
    def second_guide_crv(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_sweep_explicit.SecondGuideCrv = reference_curve.com_object

    @property
    def smooth_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothActivity() As boolean
                | 
                |     Returns or sets information whether sweeping operation is smoothed or
                |     not.
                |     TRUE or FALSE (FALSE if not specified).

        :rtype: bool
        """

        return self.hybrid_shape_sweep_explicit.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_sweep_explicit.SmoothActivity = value

    @property
    def smooth_angle_threshold(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothAngleThreshold() As Angle (Read Only)
                | 
                |     Returns angular threshold.

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_sweep_explicit.SmoothAngleThreshold)

    @property
    def solution_no(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SolutionNo() As long
                | 
                |     Returns or sets the choice number, which corresponds to each solution of a
                |     given explicit sweep case.
                |     For example: a explicit sweep with reference surface leads to four possible
                |     solutions.

        :rtype: int
        """

        return self.hybrid_shape_sweep_explicit.SolutionNo

    @solution_no.setter
    def solution_no(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_explicit.SolutionNo = value

    @property
    def spine(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Spine() As Reference
                | 
                |     Returns or sets the spine (optional) for sweep operation.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Spine curve. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference 
                |     See also:
                |         HybridShapeFactory

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_explicit.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        """
        :param Reference reference_spine:
        """

        self.hybrid_shape_sweep_explicit.Spine = reference_spine.com_object

    @property
    def sub_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SubType() As long
                | 
                |     Returns or sets the explicit sweep subtype.
                |     Legal subtype values are:
                |     1 Explicit profile swept surface defined with reference
                |     surface
                |     2 Explicit profile swept surface defined with two guide
                |     curves
                |     3 Explicit profile swept surface defined with pulling
                |     direction

        :rtype: int
        """

        return self.hybrid_shape_sweep_explicit.SubType

    @sub_type.setter
    def sub_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_explicit.SubType = value

    def get_angle_ref(self, ii: int) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetAngleRef(long ii) As Angle
                | 
                |     Gets the angle value associated to the reference surface.
                | 
                |     Parameters:
                | 
                |         iI
                |             Angle value index (1: start value, 2: end value). 
                |         oElem
                |             Angle value. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Angle 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :rtype: Angle
        """
        return Angle(self.hybrid_shape_sweep_explicit.GetAngleRef(ii))

    def get_fitting_points(self, op_ia_elem_a: Reference, op_ia_elem_b: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetFittingPoints(Reference opIAElemA,
                | Reference opIAElemB)
                | 
                |     Gets the fitting points : located in the profile plane, these points are used for two-guide
                |     swept surfaces to determine guide intersection locations.
                |     param opIAElem1 Fitting point associated to the first
                |     guide
                |     param opIAElem2 Fitting point associated to the second guide

        :param Reference op_ia_elem_a:
        :param Reference op_ia_elem_b:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.GetFittingPoints(op_ia_elem_a.com_object, op_ia_elem_b.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_fitting_points'
        # # vba_code = """
        # # Public Function get_fitting_points(hybrid_shape_sweep_explicit)
        # #     Dim opIAElemA (2)
        # #     hybrid_shape_sweep_explicit.GetFittingPoints opIAElemA
        # #     get_fitting_points = opIAElemA
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_longitudinal_relimiters(self, op_ia_elem_a: Reference, op_ia_elem_b: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetLongitudinalRelimiters(Reference opIAElemA,
                | Reference opIAElemB)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepExplicit#GetRelimiters Returns the elements
                |         relimiting the spine (or the default spine).
                |         param : opIAElem1 First relimiting feature (plane or point)
                |         param : opIAElem2 Second relimiting feature (plane or point)

        :param Reference op_ia_elem_a:
        :param Reference op_ia_elem_b:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.GetLongitudinalRelimiters(op_ia_elem_a.com_object,
                                                                          op_ia_elem_b.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_longitudinal_relimiters'
        # # vba_code = """
        # # Public Function get_longitudinal_relimiters(hybrid_shape_sweep_explicit)
        # #     Dim opIAElemA (2)
        # #     hybrid_shape_sweep_explicit.GetLongitudinalRelimiters opIAElemA
        # #     get_longitudinal_relimiters = opIAElemA
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
                |     Returns the number of Angles.
                |     param : oAng Number of Angle.

        :param int o_ang:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.GetNbAngle(o_ang)

    def get_nb_guide(self, o_num: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetNbGuide(long oNum)
                | 
                |     Gets the number of guides curves.
                |     param : oNum Number of guide curves.

        :param int o_num:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.GetNbGuide(o_num)

    def get_nb_pos_angle(self, o_pos_ang: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetNbPosAngle(long oPosAng)
                | 
                |     Gets the number of numerical positioning parameters corresponding to angles
                |     from the default positions of the X axes.
                |     param : oPosAng Number of parameters

        :param int o_pos_ang:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.GetNbPosAngle(o_pos_ang)

    def get_nb_pos_coord(self, o_pos_coord: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetNbPosCoord(long oPosCoord)
                | 
                |     Gets the number of numerical positioning parameters corresponding to
                |     coordinates of the new axes systems origins.
                |     param oPosCoord Number of parameters

        :param int o_pos_coord:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.GetNbPosCoord(o_pos_coord)

    def get_pos_angle(self, ii: int) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPosAngle(long ii) As Angle
                | 
                |     Gets angles if both profile and first sweep plane axis systems from default
                |     positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             Index of numerical positioning coordinates in profile (value 1) or
                |             first sweep plane (value 2) axis system. 
                |         oElem
                |             Angle value. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Angle 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :rtype: Angle
        """
        return Angle(self.hybrid_shape_sweep_explicit.GetPosAngle(ii))

    def get_pos_coord(self, ii: int) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPosCoord(long ii) As Length
                | 
                |     Gets translations coordinates if both profile axis system and first sweep
                |     plane axis system from default positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             Index of numerical positioning coordinates in profile (value 1 or
                |             2) or first sweep plane (value 3 or 4) axis system.
                |             
                |         oElem
                |             Coordinate value. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Length 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :rtype: Length
        """
        return Length(self.hybrid_shape_sweep_explicit.GetPosCoord(ii))

    def get_pos_direction(self, ii: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPosDirection(long ii) As Reference
                | 
                |     Gets the positioning directions : profile plane or first sweep plane X-axis direction.
                | 
                |     Parameters:
                | 
                |         iI
                |             Plane index : 1 for profile plane, 2 for first sweep plane. 
                |         oElem
                |             Direction element. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_sweep_explicit.GetPosDirection(ii))

    def get_pos_point(self, ii: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPosPoint(long ii) As Reference
                | 
                |     Gets the points designated as the origins of the profile plane and first
                |     sweep plane.
                | 
                |     Parameters:
                | 
                |         iI
                |             Plane index : 1 for profile plane, 2 for first sweep plane. 
                |         oElem
                |             Origin point. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_sweep_explicit.GetPosPoint(ii))

    def get_pos_swap_axes(self, ii: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetPosSwapAxes(long ii) As long
                | 
                |     Gets axes inversion from previous definition for both profile plane and
                |     first sweep plane.
                | 
                |     Parameters:
                | 
                |         iI
                |             Axis system index (1 for profile plane, 2 for first sweep plane).
                |             
                |         oElem
                |             Inversion value:
                |             Inversion values :
                |             = 1 - CATGSMAxisInversionMode_None : no axis inverted.
                |             = 2 - CATGSMAxisInversionMode_X : only X axis inverted.
                |             = 3 - CATGSMAxisInversionMode_Y : only Y axis inverted.
                |             = 4 - CATGSMAxisInversionMode_Both : both axes inverted. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :rtype: int
        """
        return self.hybrid_shape_sweep_explicit.GetPosSwapAxes(ii)

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
        return self.hybrid_shape_sweep_explicit.GetRelimiters(op_ia_elem1.com_object, op_orient1,
                                                              op_ia_elem2.com_object, op_orient2)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_relimiters'
        # # vba_code = """
        # # Public Function get_relimiters(hybrid_shape_sweep_explicit)
        # #     Dim opIAElem1 (2)
        # #     hybrid_shape_sweep_explicit.GetRelimiters opIAElem1
        # #     get_relimiters = opIAElem1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def is_sketch_axis_used_as_default(self, o_boolean: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub IsSketchAxisUsedAsDefault(boolean oBoolean)
                | 
                |     Queries status wherere Sketch axis used as default or not.
                |     In case of a sketch profile, specify if the 2D sketch axis must be used as
                |     default planar profile axis (for positioning purpose) or
                |     not.
                |     param oBoolean TRUE if the 2D sketch axis must be used, FALSE if not.

        :param bool o_boolean:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.IsSketchAxisUsedAsDefault(o_boolean)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'is_sketch_axis_used_as_default'
        # # vba_code = """
        # # Public Function is_sketch_axis_used_as_default(hybrid_shape_sweep_explicit)
        # #     Dim oBoolean (2)
        # #     hybrid_shape_sweep_explicit.IsSketchAxisUsedAsDefault oBoolean
        # #     is_sketch_axis_used_as_default = oBoolean
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_angle(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveAngle()
                | 
                |     Removes an Angle.

        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.RemoveAngle()

    def remove_fitting_points(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveFittingPoints()
                | 
                |     Removes the fitting points.

        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.RemoveFittingPoints()

    def remove_guide(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveGuide()
                | 
                |     Removes a guide curve.

        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.RemoveGuide()

    def set_angle_ref(self, ii: int, elem: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetAngleRef(long ii,
                | double Elem)
                | 
                |     Sets the angle value associated to the reference surface.
                | 
                |     Parameters:
                | 
                |         iI
                |             Angle value index (1: start value, 2: end value). 
                |         iElem
                |             Angle value. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param float elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.SetAngleRef(ii, elem)

    def set_fitting_points(self, ip_ia_elem_a: Reference, ip_ia_elem_b: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetFittingPoints(Reference ipIAElemA,
                | Reference ipIAElemB)
                | 
                |     Sets the fitting points.
                |     Does not work with NULL_var values, Use RemoveFittingPoints() method
                |     instead.
                |     param ipIAElem1 Fitting point associated to the first guide (must not be
                |     equal to NULL_var)
                |     param ipIAElem2 Fitting point associated to the second guide (can be equal
                |     to NULL_var)

        :param Reference ip_ia_elem_a:
        :param Reference ip_ia_elem_b:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.SetFittingPoints(ip_ia_elem_a.com_object, ip_ia_elem_b.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_fitting_points'
        # # vba_code = """
        # # Public Function set_fitting_points(hybrid_shape_sweep_explicit)
        # #     Dim ipIAElemA (2)
        # #     hybrid_shape_sweep_explicit.SetFittingPoints ipIAElemA
        # #     set_fitting_points = ipIAElemA
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_guide_deviation(self, i_length: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetGuideDeviation(double iLength)
                | 
                |     Sets deviation value (length) from guide curves allowed during sweeping.
                |     operation in order to smooth it.
                |     param : iLength Numerical value.

        :param float i_length:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.SetGuideDeviation(i_length)

    def set_longitudinal_relimiters(self, ip_ia_elem_a: Reference, ip_ia_elem_b: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLongitudinalRelimiters(Reference ipIAElemA,
                | Reference ipIAElemB)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepExplicit#SetRelimiters Sets the elements
                |         relimiting the spine (or the default spine).
                |         param : ipIAElem1 First relimiting feature (plane or point)
                |         param : ipIAElem2 Second relimiting feature (plane or point)

        :param Reference ip_ia_elem_a:
        :param Reference ip_ia_elem_b:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.SetLongitudinalRelimiters(ip_ia_elem_a.com_object,
                                                                          ip_ia_elem_b.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_longitudinal_relimiters'
        # # vba_code = """
        # # Public Function set_longitudinal_relimiters(hybrid_shape_sweep_explicit)
        # #     Dim ipIAElemA (2)
        # #     hybrid_shape_sweep_explicit.SetLongitudinalRelimiters ipIAElemA
        # #     set_longitudinal_relimiters = ipIAElemA
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pos_angle(self, ii: int, elem: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPosAngle(long ii,
                | double Elem)
                | 
                |     Sets angles if both profile and first sweep plane axis systems from default
                |     positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             Index of numerical positioning coordinates in profile (value 1) or
                |             first sweep plane (value 2) axis system. 
                |         iElem
                |             Angle value. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param float elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.SetPosAngle(ii, elem)

    def set_pos_coord(self, ii: int, elem: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPosCoord(long ii,
                | double Elem)
                | 
                |     Sets translations coordinates if both profile axis system and first sweep
                |     plane axis system from default positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             Index of numerical positioning coordinates in profile (value 1 or
                |             2) or first sweep plane (value 3 or 4) axis system.
                |             
                |         iElem
                |             Coordinate value. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param float elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.SetPosCoord(ii, elem)

    def set_pos_direction(self, ii: int, elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPosDirection(long ii,
                | Reference Elem)
                | 
                |     Sets the positioning directions : profile plane or first sweep plane X-axis direction.
                | 
                |     Parameters:
                | 
                |         iI
                |             Plane index : 1 for profile plane, 2 for first sweep plane. 
                |         iElem
                |             Direction element. 
                | 
                |     See also:
                |         Reference 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param Reference elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.SetPosDirection(ii, elem.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pos_direction'
        # # vba_code = """
        # # Public Function set_pos_direction(hybrid_shape_sweep_explicit)
        # #     Dim ii (2)
        # #     hybrid_shape_sweep_explicit.SetPosDirection ii
        # #     set_pos_direction = ii
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pos_point(self, ii: int, elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPosPoint(long ii,
                | Reference Elem)
                | 
                |     Sets the points designated as the origins of the profile plane and first
                |     sweep plane.
                | 
                |     Parameters:
                | 
                |         iI
                |             Plane index : 1 for profile plane, 2 for first sweep plane. 
                |         iElem
                |             Origin point. 
                | 
                |     See also:
                |         Reference 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param Reference elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.SetPosPoint(ii, elem.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pos_point'
        # # vba_code = """
        # # Public Function set_pos_point(hybrid_shape_sweep_explicit)
        # #     Dim ii (2)
        # #     hybrid_shape_sweep_explicit.SetPosPoint ii
        # #     set_pos_point = ii
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pos_swap_axes(self, ii: int, elem: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetPosSwapAxes(long ii,
                | long Elem)
                | 
                |     Sets axes inversion from previous definition for both profile plane and
                |     first sweep plane.
                | 
                |     Parameters:
                | 
                |         iI
                |             Axis system index (1 for profile plane, 2 for first sweep plane).
                |             
                |         iElem
                |             Inversion value:
                | 
                |             Inversion values :
                |             = 1 - CATGSMAxisInversionMode_None : no axis inverted.
                |             = 2 - CATGSMAxisInversionMode_X : only X axis inverted.
                |             = 3 - CATGSMAxisInversionMode_Y : only Y axis inverted.
                |             = 4 - CATGSMAxisInversionMode_Both : both axes inverted. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param int elem:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.SetPosSwapAxes(ii, elem)

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
        return self.hybrid_shape_sweep_explicit.SetRelimiters(ip_ia_elem1.com_object, ip_orient1,
                                                              ip_ia_elem2.com_object, ip_orient2)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_relimiters'
        # # vba_code = """
        # # Public Function set_relimiters(hybrid_shape_sweep_explicit)
        # #     Dim ipIAElem1 (2)
        # #     hybrid_shape_sweep_explicit.SetRelimiters ipIAElem1
        # #     set_relimiters = ipIAElem1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_smooth_angle_threshold(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSmoothAngleThreshold(double iAngle)
                | 
                |     Sets angular threshold.
                |     param : iAngle Numerical value.

        :param float i_angle:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.SetSmoothAngleThreshold(i_angle)

    def use_sketch_axis_as_default(self, i_boolean: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub UseSketchAxisAsDefault(boolean iBoolean)
                | 
                |     Uses Sketch Axis As Default.
                |     In case of a sketch profile, specify if the 2D sketch axis must be used as
                |     default planar profile axis (for positioning purpose) or
                |     not.
                |     param iBoolean TRUE if the 2D sketch axis must be used, FALSE if not.

        :param bool i_boolean:
        :rtype: None
        """
        return self.hybrid_shape_sweep_explicit.UseSketchAxisAsDefault(i_boolean)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'use_sketch_axis_as_default'
        # # vba_code = """
        # # Public Function use_sketch_axis_as_default(hybrid_shape_sweep_explicit)
        # #     Dim iBoolean (2)
        # #     hybrid_shape_sweep_explicit.UseSketchAxisAsDefault iBoolean
        # #     use_sketch_axis_as_default = iBoolean
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeSweepExplicit(name="{self.name}")'
