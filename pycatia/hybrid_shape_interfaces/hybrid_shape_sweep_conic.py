#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_sweep import HybridShapeSweep
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length


class HybridShapeSweepConic(HybridShapeSweep):
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
                |                             HybridShapeSweepConic
                | 
                | Represents the hybrid shape conic sweep feature.
                | Role: To access the data of the conic sweep feature .
                | 
                | Use the HybridShapeFactory.AddNewSweepConic to create a HybridShapeConicSweep
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_sweep_conic = com_object

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

        return self.hybrid_shape_sweep_conic.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_conic.CanonicalDetection = value

    @property
    def fifth_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FifthGuideCrv() As Reference
                | 
                |     Returns or sets the fifth guide curve.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_conic.FifthGuideCrv)

    @fifth_guide_crv.setter
    def fifth_guide_crv(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_sweep_conic.FifthGuideCrv = reference_curve.com_object

    @property
    def first_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstGuideCrv() As Reference
                | 
                |     Returns or sets the first guide curve.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_conic.FirstGuideCrv)

    @first_guide_crv.setter
    def first_guide_crv(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_sweep_conic.FirstGuideCrv = reference_curve.com_object

    @property
    def fourth_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FourthGuideCrv() As Reference
                | 
                |     Returns or sets the fourth guide curve.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_conic.FourthGuideCrv)

    @fourth_guide_crv.setter
    def fourth_guide_crv(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_sweep_conic.FourthGuideCrv = reference_curve.com_object

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

        return Length(self.hybrid_shape_sweep_conic.GuideDeviation)

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
                |     Gives the information on performing smoothinh during sweeping
                |     operation.
                |     TRUE or FALSE (FALSE if not specified).

        :rtype: bool
        """

        return self.hybrid_shape_sweep_conic.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_sweep_conic.GuideDeviationActivity = value

    @property
    def parameter(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Parameter() As double
                | 
                |     Returns or sets the parameter for conic sweep operation.
                |     if the parameter is a law, the method returns FALSE see
                |     HybridShapeLawDistProj

        :rtype: float
        """

        return self.hybrid_shape_sweep_conic.Parameter

    @parameter.setter
    def parameter(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_sweep_conic.Parameter = value

    @property
    def parameter_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ParameterLaw() As Reference
                | 
                |     Returns or sets the parameter law useful in conic sweep operation.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_conic.ParameterLaw)

    @parameter_law.setter
    def parameter_law(self, reference_law: Reference):
        """
        :param Reference reference_law:
        """

        self.hybrid_shape_sweep_conic.ParameterLaw = reference_law.com_object

    @property
    def parameter_law_inversion(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ParameterLawInversion() As boolean
                | 
                |     Returns or sets the parameter law inversion flag of conic sweep
                |     operation.
                |     TRUE if parameter law is inverted. Else it is FALSE. see
                |     HybridShapeLawDistProj

        :rtype: bool
        """

        return self.hybrid_shape_sweep_conic.ParameterLawInversion

    @parameter_law_inversion.setter
    def parameter_law_inversion(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_sweep_conic.ParameterLawInversion = value

    @property
    def parameter_law_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ParameterLawType() As long
                | 
                |     Returns or sets the parameter law type in conic sweep operation.

        :rtype: int
        """

        return self.hybrid_shape_sweep_conic.ParameterLawType

    @parameter_law_type.setter
    def parameter_law_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_conic.ParameterLawType = value

    @property
    def second_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondGuideCrv() As Reference
                | 
                |     Returns or sets the second guide curve.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_conic.SecondGuideCrv)

    @second_guide_crv.setter
    def second_guide_crv(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_sweep_conic.SecondGuideCrv = reference_curve.com_object

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

        return self.hybrid_shape_sweep_conic.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_sweep_conic.SmoothActivity = value

    @property
    def smooth_angle_threshold(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothAngleThreshold() As Angle (Read Only)
                | 
                |     Returns angular threshold under which discontinuities .
                |     moving frame,tangency net on reference surface will be smoothed when
                |     sweeping.

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_sweep_conic.SmoothAngleThreshold)

    @property
    def spine(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Spine() As Reference
                | 
                |     Returns or sets the spine (optional) for sweep operation.
                |     param : oElem Spine curve.
                | 
                |     See also:
                |         Reference

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_conic.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        """
        :param Reference reference_spine:
        """

        self.hybrid_shape_sweep_conic.Spine = reference_spine.com_object

    @property
    def third_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ThirdGuideCrv() As Reference
                | 
                |     Returns or sets the third guide curve.

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_sweep_conic.ThirdGuideCrv)

    @third_guide_crv.setter
    def third_guide_crv(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_sweep_conic.ThirdGuideCrv = reference_curve.com_object

    def get_longitudinal_relimiters(self, op_ia_elem1: Reference, op_ia_elem2: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetLongitudinalRelimiters(Reference opIAElem1,
                | Reference opIAElem2)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepConic#GetRelimiters Gets the elements
                |         relimiting the spine (or the default spine).
                |         param : opIAElem1 First relimiting feature (plane or point)
                |         param : opIAElem2 Second relimiting feature (plane or point)

        :param Reference op_ia_elem1:
        :param Reference op_ia_elem2:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.GetLongitudinalRelimiters(op_ia_elem1.com_object, op_ia_elem2.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_longitudinal_relimiters'
        # # vba_code = """
        # # Public Function get_longitudinal_relimiters(hybrid_shape_sweep_conic)
        # #     Dim opIAElem1 (2)
        # #     hybrid_shape_sweep_conic.GetLongitudinalRelimiters opIAElem1
        # #     get_longitudinal_relimiters = opIAElem1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_nb_guides(self, o_num: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetNbGuides(long oNum)
                | 
                |     Gets the number of guides.
                |     param : oNum Number of guides curve.

        :param int o_num:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.GetNbGuides(o_num)

    def get_parameter_law(self, o_param_start: float, o_param_end: float, o_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetParameterLaw(double oParamStart,
                | double oParamEnd,
                | long oLawType)
                | 
                |     Gets the parameter law used in conic sweep operation.
                |     param : oParamStart Parameter law start value.
                |     param : oParamEnd Parameter law end value.
                |     param : oLawType Parameter law type.

        :param float o_param_start:
        :param float o_param_end:
        :param int o_law_type:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.GetParameterLaw(o_param_start, o_param_end, o_law_type)

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
        return self.hybrid_shape_sweep_conic.GetRelimiters(op_ia_elem1.com_object, op_orient1, op_ia_elem2.com_object,
                                                           op_orient2)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_relimiters'
        # # vba_code = """
        # # Public Function get_relimiters(hybrid_shape_sweep_conic)
        # #     Dim opIAElem1 (2)
        # #     hybrid_shape_sweep_conic.GetRelimiters opIAElem1
        # #     get_relimiters = opIAElem1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_tangency(self, op_ia_elem: Reference, op_ia_angle_start: Angle, op_ia_angle_end: Angle, o_law_type: int,
                     i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetTangency(Reference opIAElem,
                | Angle opIAAngleStart,
                | Angle opIAAngleEnd,
                | long oLawType,
                | long iIndex)
                | 
                |     Gets tangency surface or curve and its angle given the guide curve
                |     index.
                |     param : opIAElem
                |     param : opIAAngleStart Start tangency angle from surface or curve reference.
                |     param : opIAAngleEnd End tangency angle from surface or curve reference.
                |     param : oLawType Type of law used for tangency angle from surface or curve reference.
                |     param : iIndex Guide curve index : 1 to 5.

        :param Reference op_ia_elem:
        :param Angle op_ia_angle_start:
        :param Angle op_ia_angle_end:
        :param int o_law_type:
        :param int i_index:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.GetTangency(op_ia_elem.com_object, op_ia_angle_start.com_object,
                                                         op_ia_angle_end.com_object, o_law_type, i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_tangency'
        # # vba_code = """
        # # Public Function get_tangency(hybrid_shape_sweep_conic)
        # #     Dim opIAElem (2)
        # #     hybrid_shape_sweep_conic.GetTangency opIAElem
        # #     get_tangency = opIAElem
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_tangency_angle_law_inversion(self, i_index: int, o_inversion: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetTangencyAngleLawInversion(long iIndex,
                | long oInversion)
                | 
                |     Gets information whether tangency angle law has to be inverted or not for a
                |     specified guide curve.
                |     param : iIndex Guide curve index : 1 to 5
                |     param : oInversion Non-Zero for TRUE and 0 for FALSE.

        :param int i_index:
        :param int o_inversion:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.GetTangencyAngleLawInversion(i_index, o_inversion)

    def get_tangency_law(self, op_ia_elem: Reference, op_ia_law: Reference, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetTangencyLaw(Reference opIAElem,
                | Reference opIALaw,
                | long iIndex)
                | 
                |     Gets tangency surface or curve and its angle given the guide curve
                |     index.
                |     param : opIAElem Tangency surface or curve feature.
                |     param : opIALaw Start tangency angle from surface or curve reference.
                |     param : iIndex Guide curve index : 1 to 5.

        :param Reference op_ia_elem:
        :param Reference op_ia_law:
        :param int i_index:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.GetTangencyLaw(op_ia_elem.com_object, op_ia_law.com_object, i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_tangency_law'
        # # vba_code = """
        # # Public Function get_tangency_law(hybrid_shape_sweep_conic)
        # #     Dim opIAElem (2)
        # #     hybrid_shape_sweep_conic.GetTangencyLaw opIAElem
        # #     get_tangency_law = opIAElem
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_guide(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveGuide(long iIndex)
                | 
                |     Removes a guide curve given its index.
                |     it removes also tangency element if specified.
                |     param : iIndex Guide curve index : 1 to 5. If 0, all guides are removed.

        :param int i_index:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.RemoveGuide(i_index)

    def remove_parameter(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveParameter()
                | 
                |     Removes conical sweep parameter, whether it is a single value or a law.

        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.RemoveParameter()

    def remove_tangency(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveTangency(long iIndex)
                | 
                |     removes tangency surface or curve and its angle given the guide curve
                |     index.
                |     param : iIndex Guide curve index : 1 to 5.

        :param int i_index:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.RemoveTangency(i_index)

    def set_guide_deviation(self, i_length: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetGuideDeviation(double iLength)
                | 
                |     Sets deviation value (length) from guide curves allowed during sweeping
                |     operation in order to smooth it.
                |     param : iLength Numerical value.

        :param float i_length:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.SetGuideDeviation(i_length)

    def set_longitudinal_relimiters(self, ip_ia_elem1: Reference, ip_ia_elem2: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetLongitudinalRelimiters(Reference ipIAElem1,
                | Reference ipIAElem2)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepConic#SetRelimiters Sets the elements
                |         relimiting the spine (or the default spine).
                |         param : ipIAElem1 First relimiting feature (plane or point)
                |         param : ipIAElem2 Second relimiting feature (plane or point)

        :param Reference ip_ia_elem1:
        :param Reference ip_ia_elem2:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.SetLongitudinalRelimiters(ip_ia_elem1.com_object, ip_ia_elem2.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_longitudinal_relimiters'
        # # vba_code = """
        # # Public Function set_longitudinal_relimiters(hybrid_shape_sweep_conic)
        # #     Dim ipIAElem1 (2)
        # #     hybrid_shape_sweep_conic.SetLongitudinalRelimiters ipIAElem1
        # #     set_longitudinal_relimiters = ipIAElem1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_parameter_law(self, i_param_start: float, i_param_end: float, i_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetParameterLaw(double iParamStart,
                | double iParamEnd,
                | long iLawType)
                | 
                |     Sets the parameter law that will be used in conic sweep
                |     operation.
                |     param : iParamStart Parameter law start value.
                |     param : iParamEnd Parameter law end value.
                |     param : iLawType Parameter law type.

        :param float i_param_start:
        :param float i_param_end:
        :param int i_law_type:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.SetParameterLaw(i_param_start, i_param_end, i_law_type)

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
        return self.hybrid_shape_sweep_conic.SetRelimiters(ip_ia_elem1.com_object, ip_orient1, ip_ia_elem2.com_object,
                                                           ip_orient2)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_relimiters'
        # # vba_code = """
        # # Public Function set_relimiters(hybrid_shape_sweep_conic)
        # #     Dim ipIAElem1 (2)
        # #     hybrid_shape_sweep_conic.SetRelimiters ipIAElem1
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
                |     Sets angular threshold under which discontinuities.
                |     note: moving frame,tangency net on reference surface will be smoothed when
                |     sweeping.
                |     param : iAngle Numerical value.

        :param float i_angle:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.SetSmoothAngleThreshold(i_angle)

    def set_tangency(self, ip_ia_elem: Reference, i_angle_start: float, i_angle_end: float, ilaw_type: int,
                     i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTangency(Reference ipIAElem,
                | double iAngleStart,
                | double iAngleEnd,
                | long ilawType,
                | long iIndex)
                | 
                |     Sets tangency surface or curve and its angle given the guide curve
                |     index.
                |     param : ipIAElem Tangency surface or curve feature.
                |     param : iAngleStart Start tangency angle from surface or curve reference.
                |     param : iAngleEnd End tangency angle from surface or curve reference.
                |     param : iAngleLawType Type of law used for tangency angle from surface or curve reference.
                |     param : iIndex Guide curve index : 1 to 5.

        :param Reference ip_ia_elem:
        :param float i_angle_start:
        :param float i_angle_end:
        :param int ilaw_type:
        :param int i_index:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.SetTangency(ip_ia_elem.com_object, i_angle_start, i_angle_end, ilaw_type,
                                                         i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tangency'
        # # vba_code = """
        # # Public Function set_tangency(hybrid_shape_sweep_conic)
        # #     Dim ipIAElem (2)
        # #     hybrid_shape_sweep_conic.SetTangency ipIAElem
        # #     set_tangency = ipIAElem
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tangency_angle_law_inversion(self, i_index: int, i_inversion: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTangencyAngleLawInversion(long iIndex,
                | long iInversion)
                | 
                |     Sets information whether tangency angle law has to be inverted or not for a
                |     specified guide curve.
                |     param : iIndex Guide curve index : 1 to 5
                |     param : iInversion 1 for TRUE and 0 for FALSE.

        :param int i_index:
        :param int i_inversion:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.SetTangencyAngleLawInversion(i_index, i_inversion)

    def set_tangency_law(self, ip_ia_elem: Reference, ip_ia_law: Reference, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTangencyLaw(Reference ipIAElem,
                | Reference ipIALaw,
                | long iIndex)
                | 
                |     Sets tangency surface or curve and its angle given the guide curve
                |     index.
                |     param : ipIAElem Tangency surface or curve feature.
                |     param : ipIALaw Start tangency angle from surface or curve reference.
                |     param : iIndex Guide curve index : 1 to 5.

        :param Reference ip_ia_elem:
        :param Reference ip_ia_law:
        :param int i_index:
        :rtype: None
        """
        return self.hybrid_shape_sweep_conic.SetTangencyLaw(ip_ia_elem.com_object, ip_ia_law.com_object, i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tangency_law'
        # # vba_code = """
        # # Public Function set_tangency_law(hybrid_shape_sweep_conic)
        # #     Dim ipIAElem (2)
        # #     hybrid_shape_sweep_conic.SetTangencyLaw ipIAElem
        # #     set_tangency_law = ipIAElem
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeSweepConic(name="{self.name}")'
