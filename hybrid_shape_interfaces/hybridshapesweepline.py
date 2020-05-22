#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSweepLine(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the sweep line object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep_line = com_object     

    @property
    def angle_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AngleLaw
                | o Property AngleLaw(    ) As
                | 
                | Returns or sets the angular law.

        :return:
        """
        return self.hybrid_shape_sweep_line.AngleLaw

    @angle_law.setter
    def angle_law(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.AngleLaw = value 

    @property
    def angle_law_inversion(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AngleLawInversion
                | o Property AngleLawInversion(    ) As
                | 
                | Returns or sets whether the angular law has to be inverted.
                | Legal angular law inversion values are: 0 The angular law
                | has NOT to be inverted 1 The angular law has to be inverted

        :return:
        """
        return self.hybrid_shape_sweep_line.AngleLawInversion

    @angle_law_inversion.setter
    def angle_law_inversion(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.AngleLawInversion = value 

    @property
    def angle_law_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | AngleLawType
                | o Property AngleLawType(    ) As
                | 
                | Returns or sets the angular law type. Legal angular law type
                | values are: 0 Undefined law type (CATGSMBasicLawType_None) 1
                | Constant law type (CATGSMBasicLawType_Constant) 2 Linear law
                | type (CATGSMBasicLawType_Linear) 3 S law type
                | (CATGSMBasicLawType_SType) 4 Law specified by a GSD law
                | feature (CATGSMBasicLawType_Advanced)

        :return:
        """
        return self.hybrid_shape_sweep_line.AngleLawType

    @angle_law_type.setter
    def angle_law_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.AngleLawType = value 

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
        return self.hybrid_shape_sweep_line.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.CanonicalDetection = value 

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
        return self.hybrid_shape_sweep_line.Context

    @context.setter
    def context(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.Context = value 

    @property
    def draft_computation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DraftComputationMode
                | o Property DraftComputationMode(    ) As
                | 
                | Returns or sets the draft computation mode.

        :return:
        """
        return self.hybrid_shape_sweep_line.DraftComputationMode

    @draft_computation_mode.setter
    def draft_computation_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.DraftComputationMode = value 

    @property
    def draft_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DraftDirection
                | o Property DraftDirection(    ) As
                | 
                | Returns or sets the draft direction. 
                |
                | Example:
                | This example
                | retrieves in oDirection the direction of the LinearSweep
                | feature. Dim oDirection As CATIAHybridShapeDirection Set
                | oDirection = LinearSweep.DraftDirection

        :return:
        """
        return self.hybrid_shape_sweep_line.DraftDirection

    @draft_direction.setter
    def draft_direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.DraftDirection = value 

    @property
    def first_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstGuideCrv
                | o Property FirstGuideCrv(    ) As
                | 
                | Returns or sets the sweep operation first guide curve.

        :return:
        """
        return self.hybrid_shape_sweep_line.FirstGuideCrv

    @first_guide_crv.setter
    def first_guide_crv(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.FirstGuideCrv = value 

    @property
    def first_guide_surf(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstGuideSurf
                | o Property FirstGuideSurf(    ) As
                | 
                | Returns or sets the sweep operation first guide surface.

        :return:
        """
        return self.hybrid_shape_sweep_line.FirstGuideSurf

    @first_guide_surf.setter
    def first_guide_surf(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.FirstGuideSurf = value 

    @property
    def first_length_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstLengthLaw
                | o Property FirstLengthLaw(    ) As
                | 
                | Returns or sets the first length law useful in some linear
                | sweep types.

        :return:
        """
        return self.hybrid_shape_sweep_line.FirstLengthLaw

    @first_length_law.setter
    def first_length_law(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.FirstLengthLaw = value 

    @property
    def first_length_law_inversion(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstLengthLawInversion
                | o Property FirstLengthLawInversion(    ) As
                | 
                | Returns or sets whether the first length law has to be
                | inverted. Legal length law inversion values are: 0 The
                | length law has NOT to be inverted 1 The length law has to be
                | inverted

        :return:
        """
        return self.hybrid_shape_sweep_line.FirstLengthLawInversion

    @first_length_law_inversion.setter
    def first_length_law_inversion(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.FirstLengthLawInversion = value 

    @property
    def guide_deviation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GuideDeviation
                | o Property GuideDeviation(    ) As   (Read Only)
                | 
                | Returns the deviation value (length) from guide curves
                | allowed during a sweeping operation in order to smooth it.

        :return:
        """
        return self.hybrid_shape_sweep_line.GuideDeviation

    @property
    def guide_deviation_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GuideDeviationActivity
                | o Property GuideDeviationActivity(    ) As
                | 
                | Returns or sets whether a deviation from guide curves is
                | allowed. This property gives the information on performing
                | smoothing during sweeping operation. TRUE if a deviation
                | from guide curves is allowed, or FALSE otherwise (FALSE if
                | not specified).

        :return:
        """
        return self.hybrid_shape_sweep_line.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.GuideDeviationActivity = value 

    @property
    def mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Mode
                | o Property Mode(    ) As
                | 
                | Returns or sets the linear sweep mode. Legal mode values
                | are: 0 Undefined linear profile swept surface
                | (CATGSMLinearSweep_None) 1 Linear profile swept surface
                | defined by two guide curves (CATGSMLinearSweep_TwoGuides) 2
                | Linear profile swept surface defined by a guide curve and an
                | angle (CATGSMLinearSweep_GuideAndAngleCurve) 3 Linear
                | profile swept surface defined by a guide curve and a middle
                | curve (CATGSMLinearSweep_GuideAndMiddle) 4 Linear profile
                | swept surface defined by a guide curve and an angle from a
                | reference surface
                | (CATGSMLinearSweep_GuideAndRefSurfaceAngle) 5 Linear profile
                | swept surface defined by a guide curve and a tangency
                | surface (CATGSMLinearSweep_GuideAndTangencySurface) 6 Linear
                | profile swept surface defined by a guide curve and a draft
                | directio (CATGSMLinearSweep_GuideAndDraftDirection) 7 Linear
                | profile swept surface defined by two tangency surfaces
                | (CATGSMLinearSweep_TwoTangencySurfaces)

        :return:
        """
        return self.hybrid_shape_sweep_line.Mode

    @mode.setter
    def mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.Mode = value 

    @property
    def second_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondGuideCrv
                | o Property SecondGuideCrv(    ) As
                | 
                | Returns or sets the sweep operation second guide curve.

        :return:
        """
        return self.hybrid_shape_sweep_line.SecondGuideCrv

    @second_guide_crv.setter
    def second_guide_crv(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.SecondGuideCrv = value 

    @property
    def second_guide_surf(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondGuideSurf
                | o Property SecondGuideSurf(    ) As
                | 
                | Returns or sets the sweep operation second guide surface.

        :return:
        """
        return self.hybrid_shape_sweep_line.SecondGuideSurf

    @second_guide_surf.setter
    def second_guide_surf(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.SecondGuideSurf = value 

    @property
    def second_length_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondLengthLaw
                | o Property SecondLengthLaw(    ) As
                | 
                | Returns or sets second length law useful in some linear
                | sweep types.

        :return:
        """
        return self.hybrid_shape_sweep_line.SecondLengthLaw

    @second_length_law.setter
    def second_length_law(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.SecondLengthLaw = value 

    @property
    def second_length_law_inversion(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondLengthLawInversion
                | o Property SecondLengthLawInversion(    ) As
                | 
                | Returns or sets whether the second length law has to be
                | inverted. Legal length law inversion values are: 0 The
                | length law has NOT to be inverted 1 The length law has to be
                | inverted

        :return:
        """
        return self.hybrid_shape_sweep_line.SecondLengthLawInversion

    @second_length_law_inversion.setter
    def second_length_law_inversion(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.SecondLengthLawInversion = value 

    @property
    def second_trim_option(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondTrimOption
                | o Property SecondTrimOption(    ) As
                | 
                | Returns or sets the trim option for the second tangency
                | surface. Legal trim option values are: 0 No trim computed or
                | trim undefined (CATGSMSweepTrimMode_None) 1 Trim computed
                | (CATGSMSweepTrimMode_On)

        :return:
        """
        return self.hybrid_shape_sweep_line.SecondTrimOption

    @second_trim_option.setter
    def second_trim_option(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.SecondTrimOption = value 

    @property
    def smooth_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothActivity
                | o Property SmoothActivity(    ) As
                | 
                | Returns whether the sweeping operation is smoothed. TRUE if
                | the sweeping operation is smoothed, or FALSE otherwise
                | (FALSE if not specified).

        :return:
        """
        return self.hybrid_shape_sweep_line.SmoothActivity

    @property
    def smooth_angle_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothAngleThreshold
                | o Property SmoothAngleThreshold(    ) As   (Read Only)
                | 
                | Returns the angular threshold.

        :return:
        """
        return self.hybrid_shape_sweep_line.SmoothAngleThreshold

    @property
    def solution_no(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SolutionNo
                | o Property SolutionNo(    ) As
                | 
                | Returns or sets the choice number, which corresponds to each
                | solution of a given linear sweep case. For example: a linear
                | sweep with reference surface leads to four possible
                | solutions.

        :return:
        """
        return self.hybrid_shape_sweep_line.SolutionNo

    @solution_no.setter
    def solution_no(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.SolutionNo = value 

    @property
    def spine(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Spine
                | o Property Spine(    ) As
                | 
                | Returns or sets the sweep operation spine (optional).

        :return:
        """
        return self.hybrid_shape_sweep_line.Spine

    @spine.setter
    def spine(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.Spine = value 

    @property
    def trim_option(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TrimOption
                | o Property TrimOption(    ) As
                | 
                | Returns or sets the trim option. Legal trim option values
                | are: 0 No trim computed or trim undefined
                | (CATGSMSweepTrimMode_None) 1 Trim computed
                | (CATGSMSweepTrimMode_On)

        :return:
        """
        return self.hybrid_shape_sweep_line.TrimOption

    @trim_option.setter
    def trim_option(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_line.TrimOption = value 

    def add_draft_angle_definition_location(self, ip_ia_loc_elem, i_ang):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddDraftAngleDefinitionLocation
                | o Sub AddDraftAngleDefinitionLocation(        ipIALocElem,
                |                                               iAng)
                | 
                | Adds a draft angle location.
                |
                | Parameters:
                | ipIALocElem
                |   The geometric element where the draft angle applies
                |  
                |  iAng
                |   The draft angle


        :param ip_ia_loc_elem:
        :param i_ang:
        :return:
        """
        return self.hybrid_shape_sweep_line.AddDraftAngleDefinitionLocation(ip_ia_loc_elem, i_ang)

    def get_angle(self, i_i):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAngle
                | o Func GetAngle(        iI) As
                | 
                | Returns the angle values useful in some linear sweep types.
                |
                | Parameters:
                | iI
                |     The angle value index
                |  
                | 
                |  Returns:
                |      The angle value


        :param i_i:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetAngle(i_i)

    def get_angular_law(self, op_start_ang, op_end_ang, o_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAngularLaw
                | o Sub GetAngularLaw(        opStartAng,
                |                             opEndAng,
                |                             oLawType)
                | 
                | Retrieves the angular law useful in some linear sweep types.
                |
                | Parameters:
                | opStartAng
                |    The angular law start value
                |  
                |  opEndAng
                |    The angular law end value
                |  
                |  oLawType
                |    The angular law type
                |  Legal angular law type values are: 
                |  
                | 
                | 0
                | Undefined law type (CATGSMBasicLawType_None)
                | 
                | 
                | 1
                | Constant law type (CATGSMBasicLawType_Constant)
                | 
                | 
                | 2
                | Linear law type (CATGSMBasicLawType_Linear)
                | 
                | 
                | 3
                | S law type (CATGSMBasicLawType_SType)
                | 
                | 
                | 4
                | Law specified by a GSD law feature (CATGSMBasicLawType_Advanced)


        :param op_start_ang:
        :param op_end_ang:
        :param o_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetAngularLaw(op_start_ang, op_end_ang, o_law_type)

    def get_choice_nb_surfaces(self, o_surf_ori_1, o_surf_ori_2, o_surf_coupl_ori_1, o_surf_coupl_ori_2, o_no):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetChoiceNbSurfaces
                | o Sub GetChoiceNbSurfaces(        oSurfOri1,
                |                                   oSurfOri2,
                |                                   oSurfCouplOri1,
                |                                   oSurfCouplOri2,
                |                                   oNo)
                | 
                | Gets a sequence which identifies a solution amongst all
                | possibilities of a line-profile swept surface, case
                | CATGSMLinearSweep_TwoTangencySurfaces.
                |
                | Parameters:
                | oSurfOri1
                |       This orientation determines the location of the results with regard to
                |       the first surface. Possible values are: 
                |       * +1 : the result is in the semi-space defined by the normal to the surface, 
                |       * -1 : the result is in the semi-space defined by the opposite to the normal to the surface, 
                |       * 0  : no orientation is specified, all the results are output, 
                |       * 2  : the result changes of semi-space along the spine. 
                | 
                |  oSurfOri2
                |       This orientation determines the location of the results with regard to
                |       the second surface.
                |       Possible values are as for oSurfOri1.
                |    
                |  oSurfCouplOri1
                |       This orientation determines the location of the results with regard to
                |       the trihedron defined by the the spine, the normal to the first surface and
                |       the tangent to the linear profile. Possible values are: 
                |       * +1 : the output results are such that the triedron is counter clockwise, 
                |       * -1 : the output results are such that the triedron is clockwise, 
                |       * 0  : no orientation is specified, all the results are output, 
                |       * 2  : the orientation of the trihedron changes along the spine.
                |    
                |  oSurfCouplOri2
                |       This orientation determines the location of the results with regard to
                |       the trihedron defined by the the spine, the normal to the second surface and
                |       the tangent to the linear profile.
                |       Possible values are as for oSurfCouplOri1.
                |    
                |  oNo
                |       Given the previous orientations, solution number in a distance ordered list.


        :param o_surf_ori_1:
        :param o_surf_ori_2:
        :param o_surf_coupl_ori_1:
        :param o_surf_coupl_ori_2:
        :param o_no:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetChoiceNbSurfaces(o_surf_ori_1, o_surf_ori_2, o_surf_coupl_ori_1, o_surf_coupl_ori_2, o_no)

    def get_choice_no(self, o_val_1, o_val_2, o_val_3):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetChoiceNo
                | o Sub GetChoiceNo(        oVal1,
                |                           oVal2,
                |                           oVal3)
                | 
                | Retrieves the choice number associated with each solution of
                | a given linear sweep case. 
                |
                | Example:
                | a linear sweep with one
                | guide curve and a tangency surface may lead to several
                | possible solutions.
                |
                | Parameters:
                | oVal1
                |    The solution number (from 1 to n)
                |  
                |  oVal2
                |    In the example, the shell orientation : -1, +1 or 0 (both +1 and -1)
                |  
                |  val3
                |    In the example, the wire orientation : -1, +1 or 0 (both +1 and -1)


        :param o_val_1:
        :param o_val_2:
        :param o_val_3:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetChoiceNo(o_val_1, o_val_2, o_val_3)

    def get_draft_angle_definition_location(self, i_loc, op_ia_element, o_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDraftAngleDefinitionLocation
                | o Sub GetDraftAngleDefinitionLocation(        iLoc,
                |                                               opIAElement,
                |                                               oAngle)
                | 
                | Retrieves the draft angle location element.
                |
                | Parameters:
                | iLoc
                |   The draft angle location position in the list
                |  
                |  opIAElement
                |   The geometric element at that location and where the draft angle applies
                |  
                |  oAngle
                |   The draft angle


        :param i_loc:
        :param op_ia_element:
        :param o_angle:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetDraftAngleDefinitionLocation(i_loc, op_ia_element, o_angle)

    def get_draft_angle_definition_locations_nb(self, o_count):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetDraftAngleDefinitionLocationsNb
                | o Sub GetDraftAngleDefinitionLocationsNb(        oCount)
                | 
                | Retrieves the draft angle location list size.
                |
                | Parameters:
                | oCount
                |    The draft angle location list size


        :param o_count:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetDraftAngleDefinitionLocationsNb(o_count)

    def get_first_length_definition_type(self, o_first_type, op_ia_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFirstLengthDefinitionType
                | o Sub GetFirstLengthDefinitionType(        oFirstType,
                |                                            opIAElem)
                | 
                | Retrieves the first length definition type.
                |
                | Parameters:
                | oFirstType
                |   The first length definition type
                |   Legal length definition types are:
                |  
                | 
                | 0
                | Undefined length type (CATGSMLinearSweepLengthType_None)
                | 
                | 
                | 1
                | Length of the swept line in
                |        the sweeping plane from the guide curve (CATGSMLinearSweepLengthType_Standard)
                | 
                | 
                | 2
                | No numerical value is required,
                |        equivalent to standard length at zero (CATGSMLinearSweepLengthType_FromCurve)
                | 
                | 
                | 3
                | Up to or from a geometrical
                |        reference (a surface) (CATGSMLinearSweepLengthType_Reference)
                | 
                | 
                | 4
                | Only for draft surfaces,
                |        the length is computed in the draft direction from an extremum point on
                |        the guide curve (CATGSMLinearSweepLengthType_FromExtremum)
                | 
                | 
                | 5
                | Only for draft surfaces,
                |        the length will be used in a way similar to euclidean parallel curve
                |        distance on the swept surface (CATGSMLinearSweepLengthType_AlongSurface)
                | 
                | 
                | 
                |  opIAElem
                |   The geometric element where the first length definition type applies


        :param o_first_type:
        :param op_ia_elem:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetFirstLengthDefinitionType(o_first_type, op_ia_elem)

    def get_first_length_law(self, o_length_1, o_length_2, o_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFirstLengthLaw
                | o Sub GetFirstLengthLaw(        oLength1,
                |                                 oLength2,
                |                                 oLawType)
                | 
                | Retrieves the first length law useful in some linear sweep
                | types.
                |
                | Parameters:
                | oLength1
                |    The length law start value
                |  
                |  oLength2
                |    The length law end value
                |  
                |  oLawType
                |    The length law type
                |  Legal length law type values are: 
                |  
                | 
                | 0
                | Undefined law type (CATGSMBasicLawType_None)
                | 
                | 
                | 1
                | Constant law type (CATGSMBasicLawType_Constant)
                | 
                | 
                | 2
                | Linear law type (CATGSMBasicLawType_Linear)
                | 
                | 
                | 3
                | S law type (CATGSMBasicLawType_SType)
                | 
                | 
                | 4
                | Law specified by a GSD law feature (CATGSMBasicLawType_Advanced)


        :param o_length_1:
        :param o_length_2:
        :param o_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetFirstLengthLaw(o_length_1, o_length_2, o_law_type)

    def get_length(self, i_i):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLength
                | o Func GetLength(        iI) As
                | 
                | Returns the length values useful in some linear sweep types.
                |
                | Parameters:
                | iI
                |     The length value index
                |  
                | 
                |  Returns:
                |      The length value


        :param i_i:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetLength(i_i)

    def get_length_law_types(self, o_first_type, o_second_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLengthLawTypes
                | o Sub GetLengthLawTypes(        oFirstType,
                |                                 oSecondType)
                | 
                | Gets length law types.
                |
                | Parameters:
                | oFirstType
                |       First type of law.
                |    
                |  oSecondType
                |       Second type of law.
                |    oFirstType and oSecondType = 0 : Undefined law type
                | 								 = 1 : Constant law type
                | 								 = 2 : Linear law type
                | 								 = 3 : S law type
                | 								 = 4 : Law specified by a GSD law feature
                | 								 = 5 : Law specified by a set of points and parameters


        :param o_first_type:
        :param o_second_type:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetLengthLawTypes(o_first_type, o_second_type)

    def get_longitudinal_relimiters(self, op_ia_elem_1, op_ia_elem_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLongitudinalRelimiters
                | o Sub GetLongitudinalRelimiters(        opIAElem1,
                |                                         opIAElem2)
                | 
                | Deprecated: V5R16 CATHybridShapeSweepLine#GetRelimiters
                | Retrieves the elements relimiting the spine (or the default
                | spine).
                |
                | Parameters:
                | opIAElem1
                |     The first relimiting feature (plane or point)
                |  
                |  opIAElem2
                |    The second relimiting feature (plane or point)


        :param op_ia_elem_1:
        :param op_ia_elem_2:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetLongitudinalRelimiters(op_ia_elem_1, op_ia_elem_2)

    def get_nb_angle(self, o_ang):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbAngle
                | o Sub GetNbAngle(        oAng)
                | 
                | Retrieves the number of angles.
                |
                | Parameters:
                | oAng
                |     The number of angles


        :param o_ang:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetNbAngle(o_ang)

    def get_nb_guide_crv(self, o_num):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbGuideCrv
                | o Sub GetNbGuideCrv(        oNum)
                | 
                | Retrieves the number of guides curves.
                |
                | Parameters:
                | oNum
                |     The number of guide curves


        :param o_num:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetNbGuideCrv(o_num)

    def get_nb_guide_sur(self, o_num):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbGuideSur
                | o Sub GetNbGuideSur(        oNum)
                | 
                | Retrieves the number of guide surfaces.
                |
                | Parameters:
                | oNum
                |     The number of guides surfaces


        :param o_num:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetNbGuideSur(o_num)

    def get_nb_length(self, o_len):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbLength
                | o Sub GetNbLength(        oLen)
                | 
                | Retrieves the number of lengths.
                |
                | Parameters:
                | oLen
                |     The number of lengths


        :param o_len:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetNbLength(o_len)

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
        return self.hybrid_shape_sweep_line.GetRelimiters(op_ia_elem_1, op_orient_1, op_ia_elem_2, op_orient_2)

    def get_second_length_definition_type(self, o_second_type, op_ia_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSecondLengthDefinitionType
                | o Sub GetSecondLengthDefinitionType(        oSecondType,
                |                                             opIAElem)
                | 
                | Retrieves the second length definition type.
                |
                | Parameters:
                | oSecondType
                |   The second length definition type
                |   Legal length definition types are:
                |  
                | 
                | 0
                | Undefined length type (CATGSMLinearSweepLengthType_None)
                | 
                | 
                | 1
                | Length of the swept line in
                |        the sweeping plane from the guide curve (CATGSMLinearSweepLengthType_Standard)
                | 
                | 
                | 2
                | No numerical value is required,
                |        equivalent to standard length at zero (CATGSMLinearSweepLengthType_FromCurve)
                | 
                | 
                | 3
                | Up to or from a geometrical
                |        reference (a surface) (CATGSMLinearSweepLengthType_Reference)
                | 
                | 
                | 4
                | Only for draft surfaces,
                |        the length is computed in the draft direction from an extremum point on
                |        the guide curve (CATGSMLinearSweepLengthType_FromExtremum)
                | 
                | 
                | 5
                | Only for draft surfaces,
                |        the length will be used in a way similar to euclidean parallel curve
                |        distance on the swept surface (CATGSMLinearSweepLengthType_AlongSurface)
                | 
                | 
                | 
                |  opIAElem
                |   The geometric element where the second length definition type applies


        :param o_second_type:
        :param op_ia_elem:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetSecondLengthDefinitionType(o_second_type, op_ia_elem)

    def get_second_length_law(self, o_length_1, o_length_2, o_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSecondLengthLaw
                | o Sub GetSecondLengthLaw(        oLength1,
                |                                  oLength2,
                |                                  oLawType)
                | 
                | Retrieves the second length law useful in some linear sweep
                | types.
                |
                | Parameters:
                | oLength1
                |    The length law start value
                |  
                |  oLength2
                |    The length law end value
                |  
                |  oLawType
                |    The length law type
                |  Legal length law type values are: 
                |  
                | 
                | 0
                | Undefined law type (CATGSMBasicLawType_None)
                | 
                | 
                | 1
                | Constant law type (CATGSMBasicLawType_Constant)
                | 
                | 
                | 2
                | Linear law type (CATGSMBasicLawType_Linear)
                | 
                | 
                | 3
                | S law type (CATGSMBasicLawType_SType)
                | 
                | 
                | 4
                | Law specified by a GSD law feature (CATGSMBasicLawType_Advanced)


        :param o_length_1:
        :param o_length_2:
        :param o_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_line.GetSecondLengthLaw(o_length_1, o_length_2, o_law_type)

    def insert_draft_angle_definition_location(self, i_elem, i_angle, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | InsertDraftAngleDefinitionLocation
                | o Sub InsertDraftAngleDefinitionLocation(        iElem,
                |                                                  iAngle,
                |                                                  iPos)
                | 
                | Inserts a geometrical element and a value necessary for
                | draft angle definition after a given position in the lists.
                |
                | Parameters:
                | iElem
                |       Geometrical element
                |    
                |  iAngle
                |       Angular parameter
                |    
                |  iPos
                |       Position in lists.
                |  To insert in the beginning of the list put iPos = 0.


        :param i_elem:
        :param i_angle:
        :param i_pos:
        :return:
        """
        return self.hybrid_shape_sweep_line.InsertDraftAngleDefinitionLocation(i_elem, i_angle, i_pos)

    def remove_all_draft_angle_definition_locations(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllDraftAngleDefinitionLocations
                | o Sub RemoveAllDraftAngleDefinitionLocations(    )
                | 
                | Removes all geometrical elements and values necessary for
                | draft angle definition.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep_line.RemoveAllDraftAngleDefinitionLocations()

    def remove_angle(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAngle
                | o Sub RemoveAngle(    )
                | 
                | Removes an angle.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep_line.RemoveAngle()

    def remove_draft_angle_definition_location_position(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveDraftAngleDefinitionLocationPosition
                | o Sub RemoveDraftAngleDefinitionLocationPosition(        iPos)
                | 
                | Removes a draft angle location.
                |
                | Parameters:
                | iPos
                |   The position in the list of the draft angle location to remove


        :param i_pos:
        :return:
        """
        return self.hybrid_shape_sweep_line.RemoveDraftAngleDefinitionLocationPosition(i_pos)

    def remove_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveGuideCrv
                | o Sub RemoveGuideCrv(    )
                | 
                | Removes a guide curve.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep_line.RemoveGuideCrv()

    def remove_guide_sur(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveGuideSur
                | o Sub RemoveGuideSur(    )
                | 
                | Removes a guide surface.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep_line.RemoveGuideSur()

    def remove_length(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveLength
                | o Sub RemoveLength(    )
                | 
                | Removes a length.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep_line.RemoveLength()

    def set_angle(self, i_i, i_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAngle
                | o Sub SetAngle(        iI,
                |                        iElem)
                | 
                | Sets the angle values useful in some linear sweep types.
                |
                | Parameters:
                | iI
                |     The angle value index
                |  
                |  iElem
                |     The angle value


        :param i_i:
        :param i_elem:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetAngle(i_i, i_elem)

    def set_angular_law(self, i_start_ang, i_end_ang, i_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAngularLaw
                | o Sub SetAngularLaw(        iStartAng,
                |                             iEndAng,
                |                             iLawType)
                | 
                | Sets the angular law useful in some linear sweep types.
                |
                | Parameters:
                | iStartAng
                |    The angular law start value
                |  
                |  iEndAng
                |    The angular law end value
                |  
                |  iLawType
                |    The angular law type
                |  Legal angular law type values are: 
                |  
                | 
                | 0
                | Undefined law type (CATGSMBasicLawType_None)
                | 
                | 
                | 1
                | Constant law type (CATGSMBasicLawType_Constant)
                | 
                | 
                | 2
                | Linear law type (CATGSMBasicLawType_Linear)
                | 
                | 
                | 3
                | S law type (CATGSMBasicLawType_SType)
                | 
                | 
                | 4
                | Law specified by a GSD law feature (CATGSMBasicLawType_Advanced)


        :param i_start_ang:
        :param i_end_ang:
        :param i_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetAngularLaw(i_start_ang, i_end_ang, i_law_type)

    def set_choice_nb_surfaces(self, i_surf_ori_1, i_surf_ori_2, i_surf_coupl_ori_1, i_surf_coupl_ori_2, i_no):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetChoiceNbSurfaces
                | o Sub SetChoiceNbSurfaces(        iSurfOri1,
                |                                   iSurfOri2,
                |                                   iSurfCouplOri1,
                |                                   iSurfCouplOri2,
                |                                   iNo)
                | 
                | Sets a sequence which identifies a solution amongst all
                | possibilities of a line-profile swept surface, case
                | CATGSMLinearSweep_TwoTangencySurfaces.
                |
                | Parameters:
                | iSurfOri1
                |       This orientation determines the location of the results with regard to
                |       the first surface. Possible values are: 
                |       * +1 : the result is in the semi-space defined by the normal to the surface, 
                |       * -1 : the result is in the semi-space defined by the opposite to the normal to the , 
                |       * 0  : no orientation is specified, all the results are output, 
                |       * 2  : the result changes of semi-space along the spine. 
                | 
                |  iSurfOri2
                |       This orientation determines the location of the results with regard to
                |       the second surface.
                |       Possible values are as for iSurfOri1.
                |    
                |  iSurfCouplOri1
                |       This orientation determines the location of the results with regard to
                |       the trihedron defined by the the spine, the normal to the first surface and
                |       the tangent to the linear profile. Possible values are: 
                |       * +1 : the output results are such that the triedron is counter clockwise, 
                |       * -1 : the output results are such that the triedron is clockwise, 
                |       * 0  : no orientation is specified, all the results are output, 
                |       * 2  : the orientation of the trihedron changes along the spine.
                |    
                |  iSurfCouplOri2
                |       This orientation determines the location of the results with regard to
                |       the trihedron defined by the the spine, the normal to the second surface and
                |       the tangent to the linear profile.
                |       Possible values are as for iSurfCouplOri2.
                |    
                |  iNo
                |       Given the previous orientations, solution number in a distance ordered list.


        :param i_surf_ori_1:
        :param i_surf_ori_2:
        :param i_surf_coupl_ori_1:
        :param i_surf_coupl_ori_2:
        :param i_no:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetChoiceNbSurfaces(i_surf_ori_1, i_surf_ori_2, i_surf_coupl_ori_1, i_surf_coupl_ori_2, i_no)

    def set_choice_no(self, i_val_1, i_val_2, i_val_3):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetChoiceNo
                | o Sub SetChoiceNo(        iVal1,
                |                           iVal2,
                |                           iVal3)
                | 
                | Sets the choice number associated with each solution of a
                | given linear sweep case. 
                |
                | Example:
                | a linear sweep with one
                | guide curve and a tangency surface may lead to several
                | possible solutions.
                |
                | Parameters:
                | iVal1
                |    The solution number (from 1 to n)
                |  
                |  iVal2
                |    In the example, the shell orientation : -1, +1 or 0 (both +1 and -1)
                |  
                |  iVal3
                |    In the example, the wire orientation : -1, +1 or 0 (both +1 and -1)


        :param i_val_1:
        :param i_val_2:
        :param i_val_3:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetChoiceNo(i_val_1, i_val_2, i_val_3)

    def set_first_length_definition_type(self, i_first_type, ip_ia_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetFirstLengthDefinitionType
                | o Sub SetFirstLengthDefinitionType(        iFirstType,
                |                                            ipIAElem)
                | 
                | Sets the first length definition type.
                |
                | Parameters:
                | iFirstType
                |   The first length definition type
                |   Legal length definition types are:
                |  
                | 
                | 0
                | Undefined length type (CATGSMLinearSweepLengthType_None)
                | 
                | 
                | 1
                | Length of the swept line in
                |        the sweeping plane from the guide curve (CATGSMLinearSweepLengthType_Standard)
                | 
                | 
                | 2
                | No numerical value is required,
                |        equivalent to standard length at zero (CATGSMLinearSweepLengthType_FromCurve)
                | 
                | 
                | 3
                | Up to or from a geometrical
                |        reference (a surface) (CATGSMLinearSweepLengthType_Reference)
                | 
                | 
                | 4
                | Only for draft surfaces,
                |        the length is computed in the draft direction from an extremum point on
                |        the guide curve (CATGSMLinearSweepLengthType_FromExtremum)
                | 
                | 
                | 5
                | Only for draft surfaces,
                |        the length will be used in a way similar to euclidean parallel curve
                |        distance on the swept surface (CATGSMLinearSweepLengthType_AlongSurface)
                | 
                | 
                | 
                |  ipIAElem
                |   The geometric element where the first length definition type applies


        :param i_first_type:
        :param ip_ia_elem:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetFirstLengthDefinitionType(i_first_type, ip_ia_elem)

    def set_first_length_law(self, i_length_1, i_length_2, i_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetFirstLengthLaw
                | o Sub SetFirstLengthLaw(        iLength1,
                |                                 iLength2,
                |                                 iLawType)
                | 
                | Sets the first length law useful in some linear sweep types.
                |
                | Parameters:
                | iLength1
                |    The length law start value
                |  
                |  iLength2
                |    The length law end value
                |  
                |  iLawType
                |    The length law type
                |  Legal length law type values are: 
                |  
                | 
                | 0
                | Undefined law type (CATGSMBasicLawType_None)
                | 
                | 
                | 1
                | Constant law type (CATGSMBasicLawType_Constant)
                | 
                | 
                | 2
                | Linear law type (CATGSMBasicLawType_Linear)
                | 
                | 
                | 3
                | S law type (CATGSMBasicLawType_SType)
                | 
                | 
                | 4
                | Law specified by a GSD law feature (CATGSMBasicLawType_Advanced)


        :param i_length_1:
        :param i_length_2:
        :param i_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetFirstLengthLaw(i_length_1, i_length_2, i_law_type)

    def set_guide_deviation(self, i_length):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetGuideDeviation
                | o Sub SetGuideDeviation(        iLength)
                | 
                | Sets the deviation value (length) from guide curves allowed
                | during sweeping operation in order to smooth it.
                |
                | Parameters:
                | iLength
                |     The deviation value


        :param i_length:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetGuideDeviation(i_length)

    def set_length(self, i_i, i_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLength
                | o Sub SetLength(        iI,
                |                         iElem)
                | 
                | Sets the linear values useful in some linear sweep types.
                |
                | Parameters:
                | iI
                |     The linear value index
                |  
                |  iElem
                |     The linear value


        :param i_i:
        :param i_elem:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetLength(i_i, i_elem)

    def set_length_law_types(self, i_first_type, i_second_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLengthLawTypes
                | o Sub SetLengthLawTypes(        iFirstType,
                |                                 iSecondType)
                | 
                | Sets length law types.
                |
                | Parameters:
                | iFirstType
                |       First type of law.
                |    
                |  iSecondType
                |       Second type of law.
                |    iFirstType and iSecondType = 0 : Undefined law type
                | 								 = 1 : Constant law type
                | 								 = 2 : Linear law type
                | 								 = 3 : S law type
                | 								 = 4 : Law specified by a GSD law feature
                | 								 = 5 : Law specified by a set of points and parameters


        :param i_first_type:
        :param i_second_type:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetLengthLawTypes(i_first_type, i_second_type)

    def set_longitudinal_relimiters(self, ip_ia_elem_1, ip_ia_elem_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLongitudinalRelimiters
                | o Sub SetLongitudinalRelimiters(        ipIAElem1,
                |                                         ipIAElem2)
                | 
                | Deprecated: V5R16 CATHybridShapeSweepLine#SetRelimiters Sets
                | the elements relimiting the spine (or the default spine).
                |
                | Parameters:
                | ipIAElem1
                |     The first relimiting feature (plane or point)
                |  
                |  ipIAElem2
                |    The second relimiting feature (plane or point)


        :param ip_ia_elem_1:
        :param ip_ia_elem_2:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetLongitudinalRelimiters(ip_ia_elem_1, ip_ia_elem_2)

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
        return self.hybrid_shape_sweep_line.SetRelimiters(ip_ia_elem_1, ip_orient_1, ip_ia_elem_2, ip_orient_2)

    def set_second_length_definition_type(self, i_second_type, ip_ia_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSecondLengthDefinitionType
                | o Sub SetSecondLengthDefinitionType(        iSecondType,
                |                                             ipIAElem)
                | 
                | Sets the second length definition type.
                |
                | Parameters:
                | iSecondType
                |   The second length definition type
                |   Legal length definition types are:
                |  
                | 
                | 0
                | Undefined length type (CATGSMLinearSweepLengthType_None)
                | 
                | 
                | 1
                | Length of the swept line in
                |        the sweeping plane from the guide curve (CATGSMLinearSweepLengthType_Standard)
                | 
                | 
                | 2
                | No numerical value is required,
                |        equivalent to standard length at zero (CATGSMLinearSweepLengthType_FromCurve)
                | 
                | 
                | 3
                | Up to or from a geometrical
                |        reference (a surface) (CATGSMLinearSweepLengthType_Reference)
                | 
                | 
                | 4
                | Only for draft surfaces,
                |        the length is computed in the draft direction from an extremum point on
                |        the guide curve (CATGSMLinearSweepLengthType_FromExtremum)
                | 
                | 
                | 5
                | Only for draft surfaces,
                |        the length will be used in a way similar to euclidean parallel curve
                |        distance on the swept surface (CATGSMLinearSweepLengthType_AlongSurface)
                | 
                | 
                | 
                |  ipIAElem
                |   The geometric element where the second length definition type applies


        :param i_second_type:
        :param ip_ia_elem:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetSecondLengthDefinitionType(i_second_type, ip_ia_elem)

    def set_second_length_law(self, i_length_1, i_length_2, i_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSecondLengthLaw
                | o Sub SetSecondLengthLaw(        iLength1,
                |                                  iLength2,
                |                                  iLawType)
                | 
                | Sets the second length law useful in some linear sweep
                | types.
                |
                | Parameters:
                | iLength1
                |    The length law start value
                |  
                |  iLength2
                |    The length law end value
                |  
                |  iLawType
                |    The length law type
                |  Legal length law type values are: 
                |  
                | 
                | 0
                | Undefined law type (CATGSMBasicLawType_None)
                | 
                | 
                | 1
                | Constant law type (CATGSMBasicLawType_Constant)
                | 
                | 
                | 2
                | Linear law type (CATGSMBasicLawType_Linear)
                | 
                | 
                | 3
                | S law type (CATGSMBasicLawType_SType)
                | 
                | 
                | 4
                | Law specified by a GSD law feature (CATGSMBasicLawType_Advanced)


        :param i_length_1:
        :param i_length_2:
        :param i_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetSecondLengthLaw(i_length_1, i_length_2, i_law_type)

    def set_smooth_angle_threshold(self, i_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSmoothAngleThreshold
                | o Sub SetSmoothAngleThreshold(        iAngle)
                | 
                | Sets the angular threshold.
                |
                | Parameters:
                | iAngle
                |     The angle numerical value


        :param i_angle:
        :return:
        """
        return self.hybrid_shape_sweep_line.SetSmoothAngleThreshold(i_angle)

    def __repr__(self):
        return f'HybridShapeSweepLine()'
