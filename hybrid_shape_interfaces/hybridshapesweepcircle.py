#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSweepCircle(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape sweep circle feature object.Role: To
                | access the data of the hybrid shape sweep circle feature object.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep_circle = com_object     

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
        return self.hybrid_shape_sweep_circle.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.CanonicalDetection = value 

    @property
    def choice_no(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ChoiceNo
                | o Property ChoiceNo(    ) As
                | 
                | Returns or sets the choice number, which corresponds to each
                | solution of a given circular sweep case. For example: a
                | circular sweep with two guide curves and a radius leads to
                | four possible solutions.

        :return:
        """
        return self.hybrid_shape_sweep_circle.ChoiceNo

    @choice_no.setter
    def choice_no(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.ChoiceNo = value 

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
        return self.hybrid_shape_sweep_circle.Context

    @context.setter
    def context(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.Context = value 

    @property
    def first_angle_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstAngleLaw
                | o Property FirstAngleLaw(    ) As
                | 
                | Returns or sets the first angle law useful in some circular
                | sweep types.

        :return:
        """
        return self.hybrid_shape_sweep_circle.FirstAngleLaw

    @first_angle_law.setter
    def first_angle_law(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.FirstAngleLaw = value 

    @property
    def first_angle_law_inversion(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstAngleLawInversion
                | o Property FirstAngleLawInversion(    ) As
                | 
                | Returns or sets the first angle law inversion information.

        :return:
        """
        return self.hybrid_shape_sweep_circle.FirstAngleLawInversion

    @first_angle_law_inversion.setter
    def first_angle_law_inversion(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.FirstAngleLawInversion = value 

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
        return self.hybrid_shape_sweep_circle.FirstGuideCrv

    @first_guide_crv.setter
    def first_guide_crv(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.FirstGuideCrv = value 

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
        return self.hybrid_shape_sweep_circle.GuideDeviation

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
                | performing smoothing during sweeping operation. TRUE if a
                | deviation from guide curves is allowed, or FALSE otherwise
                | (FALSE if not specified).

        :return:
        """
        return self.hybrid_shape_sweep_circle.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.GuideDeviationActivity = value 

    @property
    def mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Mode
                | o Property Mode(    ) As
                | 
                | Returns or sets the circular sweep mode. Legal mode values
                | are: 0 Undefined circular profile swept surface
                | (CATGSMCircularSweep_None) 2 Circular profile swept surface
                | defined by three guide curves (4 solutions)
                | (CATGSMCircularSweep_ThreeGuides) 3 Circular profile swept
                | surface defined by a center curve and a reference curve (for
                | angles and radius) (CATGSMCircularSweep_TwoGuidesAndRadius)
                | 5 Circular profile swept surface defined by a center curve
                | and a reference curve (for angles and radius)
                | (CATGSMCircularSweep_CenterAndAngleCurve) 6 Circular profile
                | swept surface defined by a center curve and a radius
                | (CATGSMCircularSweep_CenterAndRadius) 7 Circular profile
                | swept surface defined by two guide curves with a tangency
                | condition on the second one (with reference surface)
                | (CATGSMCircularSweep_TwoGuidesAndTangency) 8 Circular
                | profile swept surface defined by a guide curve, a radius and
                | a tangency surface
                | (CATGSMCircularSweep_GuideAndTangencyAndRadius)

        :return:
        """
        return self.hybrid_shape_sweep_circle.Mode

    @mode.setter
    def mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.Mode = value 

    @property
    def radius_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RadiusLaw
                | o Property RadiusLaw(    ) As
                | 
                | Returns or sets the radius law feature.

        :return:
        """
        return self.hybrid_shape_sweep_circle.RadiusLaw

    @radius_law.setter
    def radius_law(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.RadiusLaw = value 

    @property
    def radius_law_inversion(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RadiusLawInversion
                | o Property RadiusLawInversion(    ) As
                | 
                | Returns or sets the radius law inversion information.

        :return:
        """
        return self.hybrid_shape_sweep_circle.RadiusLawInversion

    @radius_law_inversion.setter
    def radius_law_inversion(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.RadiusLawInversion = value 

    @property
    def radius_law_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RadiusLawType
                | o Property RadiusLawType(    ) As
                | 
                | Returns or sets the radius law type.

        :return:
        """
        return self.hybrid_shape_sweep_circle.RadiusLawType

    @radius_law_type.setter
    def radius_law_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.RadiusLawType = value 

    @property
    def reference(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Reference
                | o Property Reference(    ) As
                | 
                | Returns or sets the reference (functional curve or guide
                | surface).

        :return:
        """
        return self.hybrid_shape_sweep_circle.Reference

    @reference.setter
    def reference(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.Reference = value 

    @property
    def second_angle_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondAngleLaw
                | o Property SecondAngleLaw(    ) As
                | 
                | Returns or sets the second angle law useful in some circular
                | sweep types.

        :return:
        """
        return self.hybrid_shape_sweep_circle.SecondAngleLaw

    @second_angle_law.setter
    def second_angle_law(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.SecondAngleLaw = value 

    @property
    def second_angle_law_inversion(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondAngleLawInversion
                | o Property SecondAngleLawInversion(    ) As
                | 
                | Returns or sets the second angle law inversion information.

        :return:
        """
        return self.hybrid_shape_sweep_circle.SecondAngleLawInversion

    @second_angle_law_inversion.setter
    def second_angle_law_inversion(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.SecondAngleLawInversion = value 

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
        return self.hybrid_shape_sweep_circle.SecondGuideCrv

    @second_guide_crv.setter
    def second_guide_crv(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.SecondGuideCrv = value 

    @property
    def smooth_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothActivity
                | o Property SmoothActivity(    ) As
                | 
                | Returns or sets information whether a sweeping operation is
                | smoothed or not. TRUE if the sweeping operation is smoothed,
                | or FALSE otherwise (FALSE if not specified).

        :return:
        """
        return self.hybrid_shape_sweep_circle.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.SmoothActivity = value 

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
        return self.hybrid_shape_sweep_circle.SmoothAngleThreshold

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
        return self.hybrid_shape_sweep_circle.Spine

    @spine.setter
    def spine(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.Spine = value 

    @property
    def third_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ThirdGuideCrv
                | o Property ThirdGuideCrv(    ) As
                | 
                | Returns or sets the sweep operation third guide curve.

        :return:
        """
        return self.hybrid_shape_sweep_circle.ThirdGuideCrv

    @third_guide_crv.setter
    def third_guide_crv(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.ThirdGuideCrv = value 

    @property
    def trim_option(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TrimOption
                | o Property TrimOption(    ) As
                | 
                | Returns or sets the trim option status. The trim option
                | status legal values are: 0 No trim computed or undefined
                | (CATGSMSweepTrimMode_None) 1 Trim computed
                | (CATGSMSweepTrimMode_On)

        :return:
        """
        return self.hybrid_shape_sweep_circle.TrimOption

    @trim_option.setter
    def trim_option(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_circle.TrimOption = value 

    def get_angle(self, i_i):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAngle
                | o Func GetAngle(        iI) As
                | 
                | Returns the angle values useful in some circular sweep
                | types.
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
        return self.hybrid_shape_sweep_circle.GetAngle(i_i)

    def get_angle_law_types(self, o_first_type, o_second_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetAngleLawTypes
                | o Sub GetAngleLawTypes(        oFirstType,
                |                                oSecondType)
                | 
                | Retrieves angle law types.
                |
                | Parameters:
                | oFirstType
                |    The first type of law (from CATGSMBasicLawType enumeration).
                |    
                |  0 Undefined law type (CATGSMBasicLawType_None) 
                |  1 Constant law type (CATGSMBasicLawType_Constant) 
                |  2 Linear law type (CATGSMBasicLawType_Linear) 
                |  3 S law type (CATGSMBasicLawType_SType) 
                |  4 Law specified by a GSD law feature (CATGSMBasicLawType_Advanced) 
                | 
                | 
                |  oSecondType
                |    The second type of law (from CATGSMBasicLawType enumeration).
                |    Same legal values as oFirstType


        :param o_first_type:
        :param o_second_type:
        :return:
        """
        return self.hybrid_shape_sweep_circle.GetAngleLawTypes(o_first_type, o_second_type)

    def get_first_angle_law(self, o_elem_1, o_elem_2, ol_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFirstAngleLaw
                | o Sub GetFirstAngleLaw(        oElem1,
                |                                oElem2,
                |                                olLawType)
                | 
                | Retrieves the first angle law useful in some circular sweep
                | types.
                |
                | Parameters:
                | oElem1
                |    The angle law start value
                |  
                |  oElem2
                |    The angle law end value
                |  
                |  olLawType
                |    The angle law type


        :param o_elem_1:
        :param o_elem_2:
        :param ol_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_circle.GetFirstAngleLaw(o_elem_1, o_elem_2, ol_law_type)

    def get_longitudinal_relimiters(self, op_ia_elem_1, op_ia_elem_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLongitudinalRelimiters
                | o Sub GetLongitudinalRelimiters(        opIAElem1,
                |                                         opIAElem2)
                | 
                | Deprecated: V5R16 CATHybridShapeSweepCircle#GetRelimiters
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
        return self.hybrid_shape_sweep_circle.GetLongitudinalRelimiters(op_ia_elem_1, op_ia_elem_2)

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
        return self.hybrid_shape_sweep_circle.GetNbAngle(o_ang)

    def get_nb_guide(self, o_num):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbGuide
                | o Sub GetNbGuide(        oNum)
                | 
                | Retrieves the number of guide curves.
                |
                | Parameters:
                | oNum
                |     The number of guide curves


        :param o_num:
        :return:
        """
        return self.hybrid_shape_sweep_circle.GetNbGuide(o_num)

    def get_nb_radius(self, o_rad):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbRadius
                | o Sub GetNbRadius(        oRad)
                | 
                | Retrieves the number of radii.
                |
                | Parameters:
                | oRad
                |     The number of radii


        :param o_rad:
        :return:
        """
        return self.hybrid_shape_sweep_circle.GetNbRadius(o_rad)

    def get_radius(self, i_i):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetRadius
                | o Func GetRadius(        iI) As
                | 
                | Returns the radius value useful in some circular sweep
                | types.
                |
                | Parameters:
                | iI
                |     The radius value index (1: start value, 2: end value)
                |  
                | 
                |  Returns:
                |     The radius value


        :param i_i:
        :return:
        """
        return self.hybrid_shape_sweep_circle.GetRadius(i_i)

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
        return self.hybrid_shape_sweep_circle.GetRelimiters(op_ia_elem_1, op_orient_1, op_ia_elem_2, op_orient_2)

    def get_second_angle_law(self, o_elem_1, o_elem_2, ol_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetSecondAngleLaw
                | o Sub GetSecondAngleLaw(        oElem1,
                |                                 oElem2,
                |                                 olLawType)
                | 
                | Retrieves the second angle law useful in some circular sweep
                | types.
                |
                | Parameters:
                | oElem1
                |    The angle law start value
                |  
                |  oElem2
                |    The angle law end value
                |  
                |  olLawType
                |    The angle law type


        :param o_elem_1:
        :param o_elem_2:
        :param ol_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_circle.GetSecondAngleLaw(o_elem_1, o_elem_2, ol_law_type)

    def get_tangency_choice_no(self, o_no, o_shell_ori, o_guide_ori):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetTangencyChoiceNo
                | o Sub GetTangencyChoiceNo(        oNo,
                |                                   oShellOri,
                |                                   oGuideOri)
                | 
                | Retrieves a sequence which identifies a solution among all
                | possibilities of a circular profile sweep tangent to a
                | surface. (case
                | CATGSMCircularSweep_GuideAndTangencyAndRadius).
                |
                | Parameters:
                | oNo
                |       Given the orientations, solution number in a distance ordered list.
                |    
                |  oShellOri
                |       This orientation allows to compute just the results that are tangent
                |       to a specific side of the shell. It can take three values:
                |       
                |  +1 The result is on the normal side of the shell 
                |  -1 The result is on the side of the shell opposite to the normal 
                |  0 No orientation is specified 
                | 
                | 
                |  oGuideOri
                |       This orientation allows to compute just the results that are on the
                |       "left" or the "right" side of the shell, when looking in
                |       the guide direction. It can take three values:
                |       
                |  +1 The result is on the "left" side 
                |  -1 The result is on the "right" side 
                |  0 No orientation is specified


        :param o_no:
        :param o_shell_ori:
        :param o_guide_ori:
        :return:
        """
        return self.hybrid_shape_sweep_circle.GetTangencyChoiceNo(o_no, o_shell_ori, o_guide_ori)

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
        return self.hybrid_shape_sweep_circle.RemoveAngle()

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
        return self.hybrid_shape_sweep_circle.RemoveGuide()

    def remove_radius(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveRadius
                | o Sub RemoveRadius(    )
                | 
                | Removes a radius.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep_circle.RemoveRadius()

    def set_angle(self, i_i, i_elem):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAngle
                | o Sub SetAngle(        iI,
                |                        iElem)
                | 
                | Sets the angle values useful in some circular sweep types.
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
        return self.hybrid_shape_sweep_circle.SetAngle(i_i, i_elem)

    def set_angle_law_types(self, i_first_type, i_second_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetAngleLawTypes
                | o Sub SetAngleLawTypes(        iFirstType,
                |                                iSecondType)
                | 
                | Sets angle law types.
                |
                | Parameters:
                | iFirstType
                |    The first type of law (from CATGSMBasicLawType enumeration).
                |    Legal values:
                |    
                |  0 Undefined law type (CATGSMBasicLawType_None) 
                |  1 Constant law type (CATGSMBasicLawType_Constant) 
                |  2 Linear law type (CATGSMBasicLawType_Linear) 
                |  3 S law type (CATGSMBasicLawType_SType) 
                |  4 Law specified by a GSD law feature (CATGSMBasicLawType_Advanced) 
                | 
                | 
                |  iSecondType
                |    The second type of law (from CATGSMBasicLawType enumeration).
                |    Same legal values as iFirstType


        :param i_first_type:
        :param i_second_type:
        :return:
        """
        return self.hybrid_shape_sweep_circle.SetAngleLawTypes(i_first_type, i_second_type)

    def set_first_angle_law(self, i_elem_1, i_elem_2, il_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetFirstAngleLaw
                | o Sub SetFirstAngleLaw(        iElem1,
                |                                iElem2,
                |                                ilLawType)
                | 
                | Sets the first angle law useful in some circular sweep
                | types.
                |
                | Parameters:
                | iElem1
                |    The angle law start value
                |  
                |  iElem2
                |    The angle law end value
                |  
                |  ilLawType
                |    The angle law type


        :param i_elem_1:
        :param i_elem_2:
        :param il_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_circle.SetFirstAngleLaw(i_elem_1, i_elem_2, il_law_type)

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
        return self.hybrid_shape_sweep_circle.SetGuideDeviation(i_length)

    def set_longitudinal_relimiters(self, ip_ia_elem_1, ip_ia_elem_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLongitudinalRelimiters
                | o Sub SetLongitudinalRelimiters(        ipIAElem1,
                |                                         ipIAElem2)
                | 
                | Deprecated: V5R16 CATHybridShapeSweepCircle#SetRelimiters
                | Sets the elements relimiting the spine (or the default
                | spine).
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
        return self.hybrid_shape_sweep_circle.SetLongitudinalRelimiters(ip_ia_elem_1, ip_ia_elem_2)

    def set_radius(self, i_i, i_radius):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetRadius
                | o Sub SetRadius(        iI,
                |                         iRadius)
                | 
                | Sets the radius value useful in some circular sweep types.
                |
                | Parameters:
                | iI
                |     The radius value index (1: start value, 2: end value)
                |  
                |  iRadius
                |    The radius value


        :param i_i:
        :param i_radius:
        :return:
        """
        return self.hybrid_shape_sweep_circle.SetRadius(i_i, i_radius)

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
        return self.hybrid_shape_sweep_circle.SetRelimiters(ip_ia_elem_1, ip_orient_1, ip_ia_elem_2, ip_orient_2)

    def set_second_angle_law(self, i_elem_1, i_elem_2, il_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSecondAngleLaw
                | o Sub SetSecondAngleLaw(        iElem1,
                |                                 iElem2,
                |                                 ilLawType)
                | 
                | Sets the second angle law useful in some circular sweep
                | types.
                |
                | Parameters:
                | iElem1
                |    The angle law start value
                |  
                |  iElem2
                |    The angle law end value
                |  
                |  ilLawType
                |    Tha angle law type


        :param i_elem_1:
        :param i_elem_2:
        :param il_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_circle.SetSecondAngleLaw(i_elem_1, i_elem_2, il_law_type)

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
                |     The angular threshold


        :param i_angle:
        :return:
        """
        return self.hybrid_shape_sweep_circle.SetSmoothAngleThreshold(i_angle)

    def set_tangency_choice_no(self, i_shell_ori, i_guide_ori, i_no):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTangencyChoiceNo
                | o Sub SetTangencyChoiceNo(        iShellOri,
                |                                   iGuideOri,
                |                                   iNo)
                | 
                | Sets a sequence which identifies a solutionamong all
                | possibilities of a circular profile sweep tangent to a
                | surface.
                |
                | Parameters:
                | iNo
                |       Given the orientations, solution number in a distance ordered list.
                |    
                |  iShellOri
                |       This orientation allows to compute just the results that are tangent
                |       to a specific side of the shell. It can take three values:
                |       
                |  +1 The result is on the normal side of the shell 
                |  -1 The result is on the side of the shell opposite to the normal 
                |  0 No orientation is specified 
                | 
                | 
                |  iGuideOri
                |       This orientation allows to compute just the results that are on the
                |       "left" or the "right" side of the shell, when looking in
                |       the guide direction. It can take three values:
                |       
                |  +1 The result is on the "left" side 
                |  -1 The result is on the "right" side 
                |  0 No orientation is specified


        :param i_shell_ori:
        :param i_guide_ori:
        :param i_no:
        :return:
        """
        return self.hybrid_shape_sweep_circle.SetTangencyChoiceNo(i_shell_ori, i_guide_ori, i_no)

    def __repr__(self):
        return f'HybridShapeSweepCircle()'
