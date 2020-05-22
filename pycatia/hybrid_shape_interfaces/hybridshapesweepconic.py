#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeSweepConic(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape conic sweep  feature.Role: To access the
                | data of the conic sweep feature .

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep_conic = com_object     

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
        return self.hybrid_shape_sweep_conic.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.CanonicalDetection = value 

    @property
    def fifth_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FifthGuideCrv
                | o Property FifthGuideCrv(    ) As
                | 
                | Returns or sets the fifth guide curve.

        :return:
        """
        return self.hybrid_shape_sweep_conic.FifthGuideCrv

    @fifth_guide_crv.setter
    def fifth_guide_crv(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.FifthGuideCrv = value 

    @property
    def first_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FirstGuideCrv
                | o Property FirstGuideCrv(    ) As
                | 
                | Returns or sets the first guide curve.

        :return:
        """
        return self.hybrid_shape_sweep_conic.FirstGuideCrv

    @first_guide_crv.setter
    def first_guide_crv(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.FirstGuideCrv = value 

    @property
    def fourth_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | FourthGuideCrv
                | o Property FourthGuideCrv(    ) As
                | 
                | Returns or sets the fourth guide curve.

        :return:
        """
        return self.hybrid_shape_sweep_conic.FourthGuideCrv

    @fourth_guide_crv.setter
    def fourth_guide_crv(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.FourthGuideCrv = value 

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
        return self.hybrid_shape_sweep_conic.GuideDeviation

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
                | performing smoothinh during sweeping operation. TRUE or
                | FALSE (FALSE if not specified).

        :return:
        """
        return self.hybrid_shape_sweep_conic.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.GuideDeviationActivity = value 

    @property
    def parameter(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Parameter
                | o Property Parameter(    ) As
                | 
                | Returns or sets the parameter for conic sweep operation. if
                | the parameter is a law, the method returns FALSE see

        :return:
        """
        return self.hybrid_shape_sweep_conic.Parameter

    @parameter.setter
    def parameter(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.Parameter = value 

    @property
    def parameter_law(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ParameterLaw
                | o Property ParameterLaw(    ) As
                | 
                | Returns or sets the parameter law useful in conic sweep
                | operation.

        :return:
        """
        return self.hybrid_shape_sweep_conic.ParameterLaw

    @parameter_law.setter
    def parameter_law(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.ParameterLaw = value 

    @property
    def parameter_law_inversion(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ParameterLawInversion
                | o Property ParameterLawInversion(    ) As
                | 
                | Returns or sets the parameter law inversion flag of conic
                | sweep operation. TRUE if parameter law is inverted. Else it
                | is FALSE. see

        :return:
        """
        return self.hybrid_shape_sweep_conic.ParameterLawInversion

    @parameter_law_inversion.setter
    def parameter_law_inversion(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.ParameterLawInversion = value 

    @property
    def parameter_law_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ParameterLawType
                | o Property ParameterLawType(    ) As
                | 
                | Returns or sets the parameter law type in conic sweep
                | operation.

        :return:
        """
        return self.hybrid_shape_sweep_conic.ParameterLawType

    @parameter_law_type.setter
    def parameter_law_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.ParameterLawType = value 

    @property
    def second_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SecondGuideCrv
                | o Property SecondGuideCrv(    ) As
                | 
                | Returns or sets the second guide curve.

        :return:
        """
        return self.hybrid_shape_sweep_conic.SecondGuideCrv

    @second_guide_crv.setter
    def second_guide_crv(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.SecondGuideCrv = value 

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
        return self.hybrid_shape_sweep_conic.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.SmoothActivity = value 

    @property
    def smooth_angle_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SmoothAngleThreshold
                | o Property SmoothAngleThreshold(    ) As   (Read Only)
                | 
                | Returns angular threshold under which discontinuities .
                | moving frame,tangency net on reference surface will be
                | smoothed when sweeping.

        :return:
        """
        return self.hybrid_shape_sweep_conic.SmoothAngleThreshold

    @property
    def spine(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Spine
                | o Property Spine(    ) As
                | 
                | Returns or sets the spine (optional) for sweep operation.
                | param : oElem Spine curve. See also:

        :return:
        """
        return self.hybrid_shape_sweep_conic.Spine

    @spine.setter
    def spine(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.Spine = value 

    @property
    def third_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ThirdGuideCrv
                | o Property ThirdGuideCrv(    ) As
                | 
                | Returns or sets the third guide curve.

        :return:
        """
        return self.hybrid_shape_sweep_conic.ThirdGuideCrv

    @third_guide_crv.setter
    def third_guide_crv(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_sweep_conic.ThirdGuideCrv = value 

    def get_longitudinal_relimiters(self, op_ia_elem_1, op_ia_elem_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetLongitudinalRelimiters
                | o Sub GetLongitudinalRelimiters(        opIAElem1,
                |                                         opIAElem2)
                | 
                | Deprecated: V5R16 CATHybridShapeSweepConic#GetRelimiters
                | Gets the elements relimiting the spine (or the default
                | spine). param : opIAElem1 First relimiting feature (plane or
                | point) param : opIAElem2 Second relimiting feature (plane or
                | point)
                |
                | Parameters:


        :param op_ia_elem_1:
        :param op_ia_elem_2:
        :return:
        """
        return self.hybrid_shape_sweep_conic.GetLongitudinalRelimiters(op_ia_elem_1, op_ia_elem_2)

    def get_nb_guides(self, o_num):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetNbGuides
                | o Sub GetNbGuides(        oNum)
                | 
                | Gets the number of guides. param : oNum Number of guides
                | curve.
                |
                | Parameters:


        :param o_num:
        :return:
        """
        return self.hybrid_shape_sweep_conic.GetNbGuides(o_num)

    def get_parameter_law(self, o_param_start, o_param_end, o_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetParameterLaw
                | o Sub GetParameterLaw(        oParamStart,
                |                               oParamEnd,
                |                               oLawType)
                | 
                | Gets the parameter law used in conic sweep operation. param
                | : oParamStart Parameter law start value. param : oParamEnd
                | Parameter law end value. param : oLawType Parameter law
                | type.
                |
                | Parameters:


        :param o_param_start:
        :param o_param_end:
        :param o_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_conic.GetParameterLaw(o_param_start, o_param_end, o_law_type)

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
        return self.hybrid_shape_sweep_conic.GetRelimiters(op_ia_elem_1, op_orient_1, op_ia_elem_2, op_orient_2)

    def get_tangency(self, op_ia_elem, op_ia_angle_start, op_ia_angle_end, o_law_type, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetTangency
                | o Sub GetTangency(        opIAElem,
                |                           opIAAngleStart,
                |                           opIAAngleEnd,
                |                           oLawType,
                |                           iIndex)
                | 
                | Gets tangency surface or curve and its angle given the guide
                | curve index. param : opIAElem param : opIAAngleStart Start
                | tangency angle from surface or curve reference. param :
                | opIAAngleEnd End tangency angle from surface or curve
                | reference. param : oLawType Type of law used for tangency
                | angle from surface or curve reference. param : iIndex Guide
                | curve index : 1 to 5.
                |
                | Parameters:


        :param op_ia_elem:
        :param op_ia_angle_start:
        :param op_ia_angle_end:
        :param o_law_type:
        :param i_index:
        :return:
        """
        return self.hybrid_shape_sweep_conic.GetTangency(op_ia_elem, op_ia_angle_start, op_ia_angle_end, o_law_type, i_index)

    def get_tangency_angle_law_inversion(self, i_index, o_inversion):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetTangencyAngleLawInversion
                | o Sub GetTangencyAngleLawInversion(        iIndex,
                |                                            oInversion)
                | 
                | Gets information whether tangency angle law has to be
                | inverted or not for a specified guide curve. param : iIndex
                | Guide curve index : 1 to 5 param : oInversion Non-Zero for
                | TRUE and 0 for FALSE.
                |
                | Parameters:


        :param i_index:
        :param o_inversion:
        :return:
        """
        return self.hybrid_shape_sweep_conic.GetTangencyAngleLawInversion(i_index, o_inversion)

    def get_tangency_law(self, op_ia_elem, op_ia_law, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetTangencyLaw
                | o Sub GetTangencyLaw(        opIAElem,
                |                              opIALaw,
                |                              iIndex)
                | 
                | Gets tangency surface or curve and its angle given the guide
                | curve index. param : opIAElem Tangency surface or curve
                | feature. param : opIALaw Start tangency angle from surface
                | or curve reference. param : iIndex Guide curve index : 1 to
                | 5.
                |
                | Parameters:


        :param op_ia_elem:
        :param op_ia_law:
        :param i_index:
        :return:
        """
        return self.hybrid_shape_sweep_conic.GetTangencyLaw(op_ia_elem, op_ia_law, i_index)

    def remove_guide(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveGuide
                | o Sub RemoveGuide(        iIndex)
                | 
                | Removes a guide curve given its index. it removes also
                | tangency element if specified. param : iIndex Guide curve
                | index : 1 to 5. If 0, all guides are removed.
                |
                | Parameters:


        :param i_index:
        :return:
        """
        return self.hybrid_shape_sweep_conic.RemoveGuide(i_index)

    def remove_parameter(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveParameter
                | o Sub RemoveParameter(    )
                | 
                | Removes conical sweep parameter, whether it is a single
                | value or a law.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_sweep_conic.RemoveParameter()

    def remove_tangency(self, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveTangency
                | o Sub RemoveTangency(        iIndex)
                | 
                | removes tangency surface or curve and its angle given the
                | guide curve index. param : iIndex Guide curve index : 1 to
                | 5.
                |
                | Parameters:


        :param i_index:
        :return:
        """
        return self.hybrid_shape_sweep_conic.RemoveTangency(i_index)

    def set_guide_deviation(self, i_length):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetGuideDeviation
                | o Sub SetGuideDeviation(        iLength)
                | 
                | Sets deviation value (length) from guide curves allowed
                | during sweeping operation in order to smooth it. param :
                | iLength Numerical value.
                |
                | Parameters:


        :param i_length:
        :return:
        """
        return self.hybrid_shape_sweep_conic.SetGuideDeviation(i_length)

    def set_longitudinal_relimiters(self, ip_ia_elem_1, ip_ia_elem_2):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetLongitudinalRelimiters
                | o Sub SetLongitudinalRelimiters(        ipIAElem1,
                |                                         ipIAElem2)
                | 
                | Deprecated: V5R16 CATHybridShapeSweepConic#SetRelimiters
                | Sets the elements relimiting the spine (or the default
                | spine). param : ipIAElem1 First relimiting feature (plane or
                | point) param : ipIAElem2 Second relimiting feature (plane or
                | point)
                |
                | Parameters:


        :param ip_ia_elem_1:
        :param ip_ia_elem_2:
        :return:
        """
        return self.hybrid_shape_sweep_conic.SetLongitudinalRelimiters(ip_ia_elem_1, ip_ia_elem_2)

    def set_parameter_law(self, i_param_start, i_param_end, i_law_type):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetParameterLaw
                | o Sub SetParameterLaw(        iParamStart,
                |                               iParamEnd,
                |                               iLawType)
                | 
                | Sets the parameter law that will be used in conic sweep
                | operation. param : iParamStart Parameter law start value.
                | param : iParamEnd Parameter law end value. param : iLawType
                | Parameter law type.
                |
                | Parameters:


        :param i_param_start:
        :param i_param_end:
        :param i_law_type:
        :return:
        """
        return self.hybrid_shape_sweep_conic.SetParameterLaw(i_param_start, i_param_end, i_law_type)

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
        return self.hybrid_shape_sweep_conic.SetRelimiters(ip_ia_elem_1, ip_orient_1, ip_ia_elem_2, ip_orient_2)

    def set_smooth_angle_threshold(self, i_angle):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetSmoothAngleThreshold
                | o Sub SetSmoothAngleThreshold(        iAngle)
                | 
                | Sets angular threshold under which discontinuities. note:
                | moving frame,tangency net on reference surface will be
                | smoothed when sweeping. param : iAngle Numerical value.
                |
                | Parameters:


        :param i_angle:
        :return:
        """
        return self.hybrid_shape_sweep_conic.SetSmoothAngleThreshold(i_angle)

    def set_tangency(self, ip_ia_elem, i_angle_start, i_angle_end, ilaw_type, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTangency
                | o Sub SetTangency(        ipIAElem,
                |                           iAngleStart,
                |                           iAngleEnd,
                |                           ilawType,
                |                           iIndex)
                | 
                | Sets tangency surface or curve and its angle given the guide
                | curve index. param : ipIAElem Tangency surface or curve
                | feature. param : iAngleStart Start tangency angle from
                | surface or curve reference. param : iAngleEnd End tangency
                | angle from surface or curve reference. param : iAngleLawType
                | Type of law used for tangency angle from surface or curve
                | reference. param : iIndex Guide curve index : 1 to 5.
                |
                | Parameters:


        :param ip_ia_elem:
        :param i_angle_start:
        :param i_angle_end:
        :param ilaw_type:
        :param i_index:
        :return:
        """
        return self.hybrid_shape_sweep_conic.SetTangency(ip_ia_elem, i_angle_start, i_angle_end, ilaw_type, i_index)

    def set_tangency_angle_law_inversion(self, i_index, i_inversion):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTangencyAngleLawInversion
                | o Sub SetTangencyAngleLawInversion(        iIndex,
                |                                            iInversion)
                | 
                | Sets information whether tangency angle law has to be
                | inverted or not for a specified guide curve. param : iIndex
                | Guide curve index : 1 to 5 param : iInversion 1 for TRUE and
                | 0 for FALSE.
                |
                | Parameters:


        :param i_index:
        :param i_inversion:
        :return:
        """
        return self.hybrid_shape_sweep_conic.SetTangencyAngleLawInversion(i_index, i_inversion)

    def set_tangency_law(self, ip_ia_elem, ip_ia_law, i_index):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTangencyLaw
                | o Sub SetTangencyLaw(        ipIAElem,
                |                              ipIALaw,
                |                              iIndex)
                | 
                | Sets tangency surface or curve and its angle given the guide
                | curve index. param : ipIAElem Tangency surface or curve
                | feature. param : ipIALaw Start tangency angle from surface
                | or curve reference. param : iIndex Guide curve index : 1 to
                | 5.
                |
                | Parameters:


        :param ip_ia_elem:
        :param ip_ia_law:
        :param i_index:
        :return:
        """
        return self.hybrid_shape_sweep_conic.SetTangencyLaw(ip_ia_elem, ip_ia_law, i_index)

    def __repr__(self):
        return f'HybridShapeSweepConic()'
