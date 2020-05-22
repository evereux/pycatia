#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSweepExplicit(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape Sweep explicit feature object.Role: To
                | access the data of the hybrid shape sweep explicit feature object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep_explicit = com_object     

    @property
    def angle_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AngleLaw
                | o Property AngleLaw(    ) As
                | 
                | Returns or sets the angle law feature associated to the
                | reference surface.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.AngleLaw

    @angle_law.setter
    def angle_law(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.AngleLaw = value 

    @property
    def angle_law_inversion(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AngleLawInversion
                | o Property AngleLawInversion(    ) As
                | 
                | Returns or sets the angle law inversion information.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.AngleLawInversion

    @angle_law_inversion.setter
    def angle_law_inversion(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.AngleLawInversion = value 

    @property
    def angle_law_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AngleLawType
                | o Property AngleLawType(    ) As
                | 
                | Returns or sets the angle law type associated to the
                | reference surface.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.AngleLawType

    @angle_law_type.setter
    def angle_law_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.AngleLawType = value 

    @property
    def canonical_detection(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CanonicalDetection
                | o Property CanonicalDetection(    ) As
                | 
                | Returns or sets whether canonical surfaces of the swept
                | surface are detected. Legal values: 0 No detection of
                | canonical surface is performed. 2 Detection of canonical
                | surfaces is performed.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.CanonicalDetection = value 

    @property
    def context(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Context
                | o Property Context(    ) As
                | 
                | Returns or sets the context on Sweep feature. 0 This option
                | creates Swept surface. 1 This option creates Swept volume.
                | Note: Setting volume result requires GSO License. Example:
                | This example retrieves in oContext the context for the Sweep
                | hybrid shape feature. Dim oContext Set oContext =
                | Sweep.Context

        :return:
        """
        return self.hybrid_shape_sweep_explicit.Context

    @context.setter
    def context(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.Context = value 

    @property
    def first_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstGuideCrv
                | o Property FirstGuideCrv(    ) As
                | 
                | Gets the first guide curve.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.FirstGuideCrv

    @property
    def guide_deviation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GuideDeviation
                | o Property GuideDeviation(    ) As   (Read Only)
                | 
                | Returns deviation value (length) from guide curves allowed
                | during sweeping operation in order to smooth it.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.GuideDeviation

    @property
    def guide_deviation_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GuideDeviationActivity
                | o Property GuideDeviationActivity(    ) As
                | 
                | Returns or sets information whether a deviation from guide
                | curves is allowed or not. Gives the information on
                | performing smoothing during sweeping operation. TRUE or
                | FALSE (FALSE if not specified).

        :return:
        """
        return self.hybrid_shape_sweep_explicit.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.GuideDeviationActivity = value 

    @property
    def guide_projection(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GuideProjection
                | o Property GuideProjection(    ) As
                | 
                | Returns or sets the projection of the guide curve onto the
                | reference plane in order to use it as spine, in pulling
                | direction case only. Removes Spine if GuideProjection is set
                | to TRUE. Legal values: True projection is required and False
                | if not 
                |
                | Example:
                | This example sets that the GuideProjection
                | mode of the Sweep hybrid shape sweep explicit feature to
                | True. Sweep.GuideProjection = True

        :return:
        """
        return self.hybrid_shape_sweep_explicit.GuideProjection

    @guide_projection.setter
    def guide_projection(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.GuideProjection = value 

    @property
    def mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Mode
                | o Property Mode(    ) As
                | 
                | Returns or sets positioning mode used for the profile.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.Mode

    @mode.setter
    def mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.Mode = value 

    @property
    def position_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PositionMode
                | o Property PositionMode(    ) As
                | 
                | Returns or sets positioning mode. Legal values: 0
                | CATGSMPositionMode_NoneOrPositioned. 1
                | CATGSMPositionMode_ExplicitSweep. if a positioning operation
                | is done.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.PositionMode

    @position_mode.setter
    def position_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.PositionMode = value 

    @property
    def positioned_profile(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PositionedProfile
                | o Property PositionedProfile(    ) As
                | 
                | Returns or sets the positioning transformation associated to
                | the explicit swept surface and which result corresponds to
                | the positioned profile.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.PositionedProfile

    @positioned_profile.setter
    def positioned_profile(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.PositionedProfile = value 

    @property
    def profile(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Profile
                | o Property Profile(    ) As
                | 
                | Gets the profile to be swept out.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.Profile

    @property
    def profile_x_axis_computation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ProfileXAxisComputationMode
                | o Property ProfileXAxisComputationMode(    ) As
                | 
                | Returns or sets the computation mode of the X axis (or
                | direction) of the initial axis system (on the profile).
                | Default value is CATGSMPositionDirCompMode_None when
                | PosDirection(OutputDirection) is not specified and
                | CATGSMPositionDirCompMode_User if OutputDirection is
                | specified. Legal values: 0 CATGSMPositionDirCompMode_None.
                | No X axis specified. 1 CATGSMPositionDirCompMode_Tangent:
                | the X axis is implicitly the tangent of the profile at the
                | origin (the origin then HAS to be on the profile) 2
                | CATGSMPositionDirCompMode_User: the X axis is specified by a
                | direction via SetPosDirection(UserInputDirection, 1)

        :return:
        """
        return self.hybrid_shape_sweep_explicit.ProfileXAxisComputationMode

    @profile_x_axis_computation_mode.setter
    def profile_x_axis_computation_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.ProfileXAxisComputationMode = value 

    @property
    def pulling_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | PullingDirection
                | o Property PullingDirection(    ) As
                | 
                | Gets or sets the pulling direction If the direction is
                | specified, the plane normal to this direction is taken as
                | reference surface. 
                |
                | Example:
                | This example retrieves in ohDir
                | the pulling direction feature for the Sweep hybrid shape
                | feature. Dim ohDir As CATIAHybridShapeDirection Set ohDir =
                | Sweep.PullingDirection

        :return:
        """
        return self.hybrid_shape_sweep_explicit.PullingDirection

    @property
    def reference(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Reference
                | o Property Reference(    ) As
                | 
                | Returns or sets the reference surface (optional).

        :return:
        """
        return self.hybrid_shape_sweep_explicit.Reference

    @reference.setter
    def reference(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.Reference = value 

    @property
    def second_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondGuideCrv
                | o Property SecondGuideCrv(    ) As
                | 
                | Gets the second guide curve (optional).

        :return:
        """
        return self.hybrid_shape_sweep_explicit.SecondGuideCrv

    @property
    def smooth_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothActivity
                | o Property SmoothActivity(    ) As
                | 
                | Returns or sets information whether sweeping operation is
                | smoothed or not. TRUE or FALSE (FALSE if not specified).

        :return:
        """
        return self.hybrid_shape_sweep_explicit.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.SmoothActivity = value 

    @property
    def smooth_angle_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothAngleThreshold
                | o Property SmoothAngleThreshold(    ) As   (Read Only)
                | 
                | Returns angular threshold.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.SmoothAngleThreshold

    @property
    def solution_no(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SolutionNo
                | o Property SolutionNo(    ) As
                | 
                | Returns or sets the choice number, which corresponds to each
                | solution of a given explicit sweep case. For example: a
                | explicit sweep with reference surface leads to four possible
                | solutions.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.SolutionNo

    @solution_no.setter
    def solution_no(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.SolutionNo = value 

    @property
    def spine(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Spine
                | o Property Spine(    ) As
                | 
                | Returns or sets the spine (optional) for sweep operation.

        :return:
        """
        return self.hybrid_shape_sweep_explicit.Spine

    @spine.setter
    def spine(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.Spine = value 

    @property
    def sub_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SubType
                | o Property SubType(    ) As
                | 
                | Returns or sets the explicit sweep subtype. Legal subtype
                | values are: 1 Explicit profile swept surface defined with
                | reference surface 2 Explicit profile swept surface defined
                | with two guide curves 3 Explicit profile swept surface
                | defined with pulling direction

        :return:
        """
        return self.hybrid_shape_sweep_explicit.SubType

    @sub_type.setter
    def sub_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_explicit.SubType = value 

    def get_angle_ref(self, ii):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAngleRef
                | o Func GetAngleRef(        ii) As
                | 
                | Gets the angle value associated to the reference surface.
                |
                | Parameters:
                | iI
                |     Angle value index (1: start value, 2: end value).
                |  
                |  oElem
                |     Angle value.
                |    return value for CATScript applications, with (IDLRETVAL) function type
                |    
                | 
                |  See also:
                |  
                |  See also:


        :param ii:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetAngleRef(ii)

    def get_fitting_points(self, op_ia_elem_a, op_ia_elem_b):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFittingPoints
                | o Sub GetFittingPoints(        opIAElemA,
                |                                opIAElemB)
                | 
                | Gets the fitting points : located in the profile plane,
                | these points are used for two-guide swept surfaces to
                | determine guide intersection locations. param opIAElem1
                | Fitting point associated to the first guide param opIAElem2
                | Fitting point associated to the second guide
                |
                | Parameters:


        :param op_ia_elem_a:
        :param op_ia_elem_b:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetFittingPoints(op_ia_elem_a, op_ia_elem_b)

    def get_longitudinal_relimiters(self, op_ia_elem_a, op_ia_elem_b):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLongitudinalRelimiters
                | o Sub GetLongitudinalRelimiters(        opIAElemA,
                |                                         opIAElemB)
                | 
                | Deprecated: V5R16 CATHybridShapeSweepExplicit#GetRelimiters
                | Returns the elements relimiting the spine (or the default
                | spine). param : opIAElem1 First relimiting feature (plane or
                | point) param : opIAElem2 Second relimiting feature (plane or
                | point)
                |
                | Parameters:


        :param op_ia_elem_a:
        :param op_ia_elem_b:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetLongitudinalRelimiters(op_ia_elem_a, op_ia_elem_b)

    def get_nb_angle(self, o_ang):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbAngle
                | o Sub GetNbAngle(        oAng)
                | 
                | Returns the number of Angles. param : oAng Number of Angle.
                |
                | Parameters:


        :param o_ang:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetNbAngle(o_ang)

    def get_nb_guide(self, o_num):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbGuide
                | o Sub GetNbGuide(        oNum)
                | 
                | Gets the number of guides curves. param : oNum Number of
                | guide curves.
                |
                | Parameters:


        :param o_num:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetNbGuide(o_num)

    def get_nb_pos_angle(self, o_pos_ang):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbPosAngle
                | o Sub GetNbPosAngle(        oPosAng)
                | 
                | Gets the number of numerical positioning parameters
                | corresponding to angles from the default positions of the X
                | axes. param : oPosAng Number of parameters
                |
                | Parameters:


        :param o_pos_ang:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetNbPosAngle(o_pos_ang)

    def get_nb_pos_coord(self, o_pos_coord):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbPosCoord
                | o Sub GetNbPosCoord(        oPosCoord)
                | 
                | Gets the number of numerical positioning parameters
                | corresponding to coordinates of the new axes systems
                | origins. param oPosCoord Number of parameters
                |
                | Parameters:


        :param o_pos_coord:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetNbPosCoord(o_pos_coord)

    def get_pos_angle(self, ii):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPosAngle
                | o Func GetPosAngle(        ii) As
                | 
                | Gets angles if both profile and first sweep plane axis
                | systems from default positions.
                |
                | Parameters:
                | iI
                |     Index of numerical positioning coordinates in profile
                |            (value 1) or first sweep plane (value 2) axis system.
                |  
                |  oElem
                |     Angle value.
                |    return value for CATScript applications, with (IDLRETVAL) function type
                |    
                | 
                |  See also:
                |  
                |  See also:


        :param ii:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetPosAngle(ii)

    def get_pos_coord(self, ii):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPosCoord
                | o Func GetPosCoord(        ii) As
                | 
                | Gets translations coordinates if both profile axis system
                | and first sweep plane axis system from default positions.
                |
                | Parameters:
                | iI
                |     Index of numerical positioning coordinates in profile
                |            (value 1 or 2) or first sweep plane (value 3 or 4) axis system.
                |  
                |  oElem
                |     Coordinate value.
                |    return value for CATScript applications, with (IDLRETVAL) function type
                |    
                | 
                |  See also:
                |  
                |  See also:


        :param ii:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetPosCoord(ii)

    def get_pos_direction(self, ii):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPosDirection
                | o Func GetPosDirection(        ii) As
                | 
                | Gets the positioning directions : profile plane or first
                | sweep plane X-axis direction.
                |
                | Parameters:
                | iI
                |     Plane index : 1 for profile plane, 2 for first sweep plane.
                |  
                |  oElem
                |     Direction element.
                |    return value for CATScript applications, with (IDLRETVAL) function type
                |    
                | 
                |  See also:
                |  
                |  See also:


        :param ii:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetPosDirection(ii)

    def get_pos_point(self, ii):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPosPoint
                | o Func GetPosPoint(        ii) As
                | 
                | Gets the points designated as the origins of the profile
                | plane and first sweep plane.
                |
                | Parameters:
                | iI
                |     Plane index : 1 for profile plane, 2 for first sweep plane.
                |  
                |  oElem
                |     Origin point.
                |    return value for CATScript applications, with (IDLRETVAL) function type
                |    
                | 
                |  See also:
                |  
                |  See also:


        :param ii:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetPosPoint(ii)

    def get_pos_swap_axes(self, ii):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetPosSwapAxes
                | o Func GetPosSwapAxes(        ii) As
                | 
                | Gets axes inversion from previous definition for both
                | profile plane and first sweep plane.
                |
                | Parameters:
                | iI
                |     Axis system index (1 for profile plane, 2 for first sweep plane).
                |  
                |  oElem
                |     Inversion value:
                |   Inversion values : 
                |    =  1 - CATGSMAxisInversionMode_None : no axis inverted.
                |     =  2 - CATGSMAxisInversionMode_X : only X axis inverted.
                |     =  3 - CATGSMAxisInversionMode_Y : only Y axis inverted.
                |     =  4 - CATGSMAxisInversionMode_Both : both axes inverted.
                |  
                | 
                |  See also:


        :param ii:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetPosSwapAxes(ii)

    def get_relimiters(self, op_ia_elem_1, op_orient_1, op_ia_elem_2, op_orient_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetRelimiters
                | o Sub GetRelimiters(        opIAElem1,
                |                             opOrient1,
                |                             opIAElem2,
                |                             opOrient2)
                | 
                | Retrieves the elements relimiting the spine (or the default
                | spine).
                |
                | Parameters:
                | opIAElem1
                |     The first relimiting feature (plane or point)
                |  
                |  opOrient1
                |    Split direction for the first relimitation
                |    0 means that the beginning of the spine (considering its orientation) is removed, 1 means that the end of the spine is removed
                |  
                |  opIAElem2
                |    The second relimiting feature (plane or point)
                |  
                |  opOrient2
                |    Split direction for the second relimitation


        :param op_ia_elem_1:
        :param op_orient_1:
        :param op_ia_elem_2:
        :param op_orient_2:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.GetRelimiters(op_ia_elem_1, op_orient_1, op_ia_elem_2, op_orient_2)

    def is_sketch_axis_used_as_default(self, o_boolean):
        """
        .. note::
            CAA V5 Visual Basic help

                | IsSketchAxisUsedAsDefault
                | o Sub IsSketchAxisUsedAsDefault(        oBoolean)
                | 
                | Queries status wherere Sketch axis used as default or not.
                | In case of a sketch profile, specify if the 2D sketch axis
                | must be used as default planar profile axis (for positioning
                | purpose) or not. param oBoolean TRUE if the 2D sketch axis
                | must be used, FALSE if not.
                |
                | Parameters:


        :param o_boolean:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.IsSketchAxisUsedAsDefault(o_boolean)

    def remove_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAngle
                | o Sub RemoveAngle(    )
                | 
                | Removes an Angle.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep_explicit.RemoveAngle()

    def remove_fitting_points(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveFittingPoints
                | o Sub RemoveFittingPoints(    )
                | 
                | Removes the fitting points.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep_explicit.RemoveFittingPoints()

    def remove_guide(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveGuide
                | o Sub RemoveGuide(    )
                | 
                | Removes a guide curve.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep_explicit.RemoveGuide()

    def set_angle_ref(self, ii, elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAngleRef
                | o Sub SetAngleRef(        ii,
                |                           Elem)
                | 
                | Sets the angle value associated to the reference surface.
                |
                | Parameters:
                | iI
                |     Angle value index (1: start value, 2: end value).
                |  
                |  iElem
                |     Angle value.
                |  
                | 
                |  See also:


        :param ii:
        :param elem:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.SetAngleRef(ii, elem)

    def set_fitting_points(self, ip_ia_elem_a, ip_ia_elem_b):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetFittingPoints
                | o Sub SetFittingPoints(        ipIAElemA,
                |                                ipIAElemB)
                | 
                | Sets the fitting points. Does not work with NULL_var values,
                | Use RemoveFittingPoints() method instead. param ipIAElem1
                | Fitting point associated to the first guide (must not be
                | equal to NULL_var) param ipIAElem2 Fitting point associated
                | to the second guide (can be equal to NULL_var)
                |
                | Parameters:


        :param ip_ia_elem_a:
        :param ip_ia_elem_b:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.SetFittingPoints(ip_ia_elem_a, ip_ia_elem_b)

    def set_guide_deviation(self, i_length):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetGuideDeviation
                | o Sub SetGuideDeviation(        iLength)
                | 
                | Sets deviation value (length) from guide curves allowed
                | during sweeping. operation in order to smooth it. param :
                | iLength Numerical value.
                |
                | Parameters:


        :param i_length:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.SetGuideDeviation(i_length)

    def set_longitudinal_relimiters(self, ip_ia_elem_a, ip_ia_elem_b):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLongitudinalRelimiters
                | o Sub SetLongitudinalRelimiters(        ipIAElemA,
                |                                         ipIAElemB)
                | 
                | Deprecated: V5R16 CATHybridShapeSweepExplicit#SetRelimiters
                | Sets the elements relimiting the spine (or the default
                | spine). param : ipIAElem1 First relimiting feature (plane or
                | point) param : ipIAElem2 Second relimiting feature (plane or
                | point)
                |
                | Parameters:


        :param ip_ia_elem_a:
        :param ip_ia_elem_b:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.SetLongitudinalRelimiters(ip_ia_elem_a, ip_ia_elem_b)

    def set_pos_angle(self, ii, elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPosAngle
                | o Sub SetPosAngle(        ii,
                |                           Elem)
                | 
                | Sets angles if both profile and first sweep plane axis
                | systems from default positions.
                |
                | Parameters:
                | iI
                |     Index of numerical positioning coordinates in profile
                |            (value 1) or first sweep plane (value 2) axis system.
                |  
                |  iElem
                |     Angle value.
                |  
                | 
                |  See also:


        :param ii:
        :param elem:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.SetPosAngle(ii, elem)

    def set_pos_coord(self, ii, elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPosCoord
                | o Sub SetPosCoord(        ii,
                |                           Elem)
                | 
                | Sets translations coordinates if both profile axis system
                | and first sweep plane axis system from default positions.
                |
                | Parameters:
                | iI
                |     Index of numerical positioning coordinates in profile
                |            (value 1 or 2) or first sweep plane (value 3 or 4) axis system.
                |  
                |  iElem
                |     Coordinate value.
                |  
                | 
                |  See also:


        :param ii:
        :param elem:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.SetPosCoord(ii, elem)

    def set_pos_direction(self, ii, elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPosDirection
                | o Sub SetPosDirection(        ii,
                |                               Elem)
                | 
                | Sets the positioning directions : profile plane or first
                | sweep plane X-axis direction.
                |
                | Parameters:
                | iI
                |     Plane index : 1 for profile plane, 2 for first sweep plane.
                |  
                |  iElem
                |     Direction element.
                |    
                | 
                |  See also:
                |  
                |  See also:


        :param ii:
        :param elem:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.SetPosDirection(ii, elem)

    def set_pos_point(self, ii, elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPosPoint
                | o Sub SetPosPoint(        ii,
                |                           Elem)
                | 
                | Sets the points designated as the origins of the profile
                | plane and first sweep plane.
                |
                | Parameters:
                | iI
                |     Plane index : 1 for profile plane, 2 for first sweep plane.
                |  
                |  iElem
                |     Origin point.
                |    
                | 
                |  See also:
                |  
                |  See also:


        :param ii:
        :param elem:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.SetPosPoint(ii, elem)

    def set_pos_swap_axes(self, ii, elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetPosSwapAxes
                | o Sub SetPosSwapAxes(        ii,
                |                              Elem)
                | 
                | Sets axes inversion from previous definition for both
                | profile plane and first sweep plane.
                |
                | Parameters:
                | iI
                |     Axis system index (1 for profile plane, 2 for first sweep plane).
                |  
                |  iElem
                |     Inversion value:
                |  Inversion values : 
                |    =  1 - CATGSMAxisInversionMode_None : no axis inverted.
                |     =  2 - CATGSMAxisInversionMode_X : only X axis inverted.
                |     =  3 - CATGSMAxisInversionMode_Y : only Y axis inverted.
                |     =  4 - CATGSMAxisInversionMode_Both : both axes inverted.
                |  
                | 
                |  See also:


        :param ii:
        :param elem:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.SetPosSwapAxes(ii, elem)

    def set_relimiters(self, ip_ia_elem_1, ip_orient_1, ip_ia_elem_2, ip_orient_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetRelimiters
                | o Sub SetRelimiters(        ipIAElem1,
                |                             ipOrient1,
                |                             ipIAElem2,
                |                             ipOrient2)
                | 
                | Sets the elements relimiting the spine (or the default
                | spine).
                |
                | Parameters:
                | ipIAElem1
                |  	  The first relimiting feature (plane or point)
                |   
                |  ipOrient1
                |    Split direction for the first relimitation
                |    0 means that the beginning of the spine (considering its orientation) is removed, 1 means that the end of the spine is removed
                |   
                |  ipIAElem2
                |    The second relimiting feature (plane or point)
                |   
                |  ipOrient2
                |    Split direction for the second relimitation


        :param ip_ia_elem_1:
        :param ip_orient_1:
        :param ip_ia_elem_2:
        :param ip_orient_2:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.SetRelimiters(ip_ia_elem_1, ip_orient_1, ip_ia_elem_2, ip_orient_2)

    def set_smooth_angle_threshold(self, i_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSmoothAngleThreshold
                | o Sub SetSmoothAngleThreshold(        iAngle)
                | 
                | Sets angular threshold. param : iAngle Numerical value.
                |
                | Parameters:


        :param i_angle:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.SetSmoothAngleThreshold(i_angle)

    def use_sketch_axis_as_default(self, i_boolean):
        """
        .. note::
            CAA V5 Visual Basic help

                | UseSketchAxisAsDefault
                | o Sub UseSketchAxisAsDefault(        iBoolean)
                | 
                | Uses Sketch Axis As Default. In case of a sketch profile,
                | specify if the 2D sketch axis must be used as default planar
                | profile axis (for positioning purpose) or not. param
                | iBoolean TRUE if the 2D sketch axis must be used, FALSE if
                | not.
                |
                | Parameters:


        :param i_boolean:
        :return:
        """
        return self.hybrid_shape_sweep_explicit.UseSketchAxisAsDefault(i_boolean)

    def __repr__(self):
        return f'HybridShapeSweepExplicit()'
