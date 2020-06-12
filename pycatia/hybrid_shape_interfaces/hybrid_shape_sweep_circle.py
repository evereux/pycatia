#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_sweep import HybridShapeSweep
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length


class HybridShapeSweepCircle(HybridShapeSweep):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeSweep
                |                             HybridShapeSweepCircle
                | 
                | Represents the hybrid shape sweep circle feature object.
                | Role: To access the data of the hybrid shape sweep circle feature
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
        self.hybrid_shape_sweep_circle = com_object

    @property
    def canonical_detection(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property CanonicalDetection() As long
                | 
                |     Returns or sets whether canonical surfaces of the swept surface are
                |     detected.
                |     Legal values:
                |     0 No detection of canonical surface is performed.
                |     2 Detection of canonical surfaces is performed.

        :return: int
        """

        return self.hybrid_shape_sweep_circle.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_circle.CanonicalDetection = value

    @property
    def choice_no(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ChoiceNo() As long
                | 
                |     Returns or sets the choice number, which corresponds to each solution of a
                |     given circular sweep case.
                |     For example: a circular sweep with two guide curves and a radius leads to
                |     four possible solutions.

        :return: int
        """

        return self.hybrid_shape_sweep_circle.ChoiceNo

    @choice_no.setter
    def choice_no(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_circle.ChoiceNo = value

    @property
    def context(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
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

        :return: int
        """

        return self.hybrid_shape_sweep_circle.Context

    @context.setter
    def context(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_circle.Context = value

    @property
    def first_angle_law(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FirstAngleLaw() As Reference
                | 
                |     Returns or sets the first angle law useful in some circular sweep types.

        :return: Reference
        """

        return Reference(self.hybrid_shape_sweep_circle.FirstAngleLaw)

    @first_angle_law.setter
    def first_angle_law(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_sweep_circle.FirstAngleLaw = value

    @property
    def first_angle_law_inversion(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FirstAngleLawInversion() As long
                | 
                |     Returns or sets the first angle law inversion information.

        :return: int
        """

        return self.hybrid_shape_sweep_circle.FirstAngleLawInversion

    @first_angle_law_inversion.setter
    def first_angle_law_inversion(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_circle.FirstAngleLawInversion = value

    @property
    def first_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property FirstGuideCrv() As Reference
                | 
                |     Returns or sets the sweep operation first guide curve.

        :return: Reference
        """

        return Reference(self.hybrid_shape_sweep_circle.FirstGuideCrv)

    @first_guide_crv.setter
    def first_guide_crv(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_sweep_circle.FirstGuideCrv = value

    @property
    def guide_deviation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GuideDeviation() As Length (Read Only)
                | 
                |     Returns the deviation value (length) from guide curves allowed during a
                |     sweeping operation in order to smooth it.

        :return: Length
        """

        return Length(self.hybrid_shape_sweep_circle.GuideDeviation)

    @property
    def guide_deviation_activity(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property GuideDeviationActivity() As boolean
                | 
                |     Returns or sets information whether a deviation from guide curves is
                |     allowed or not.
                |     Gives the information on performing smoothing during sweeping
                |     operation.
                |     TRUE if a deviation from guide curves is allowed, or FALSE otherwise (FALSE
                |     if not specified).

        :return: bool
        """

        return self.hybrid_shape_sweep_circle.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_sweep_circle.GuideDeviationActivity = value

    @property
    def mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Mode() As long
                | 
                |     Returns or sets the circular sweep mode.
                |     Legal mode values are:
                |     0 Undefined circular profile swept surface
                |     (CATGSMCircularSweep_None)
                |     2 Circular profile swept surface defined by three guide curves (4
                |     solutions) (CATGSMCircularSweep_ThreeGuides)
                |     3 Circular profile swept surface defined by a center curve and a reference
                |     curve (for angles and radius)
                |     (CATGSMCircularSweep_TwoGuidesAndRadius)
                |     5 Circular profile swept surface defined by a center curve and a reference
                |     curve (for angles and radius)
                |     (CATGSMCircularSweep_CenterAndAngleCurve)
                |     6 Circular profile swept surface defined by a center curve and a radius
                |     (CATGSMCircularSweep_CenterAndRadius)
                |     7 Circular profile swept surface defined by two guide curves with a
                |     tangency condition on the second one (with reference surface)
                |     (CATGSMCircularSweep_TwoGuidesAndTangency)
                |     8 Circular profile swept surface defined by a guide curve, a radius and a
                |     tangency surface
                |     (CATGSMCircularSweep_GuideAndTangencyAndRadius)

        :return: int
        """

        return self.hybrid_shape_sweep_circle.Mode

    @mode.setter
    def mode(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_circle.Mode = value

    @property
    def radius_law(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RadiusLaw() As Reference
                | 
                |     Returns or sets the radius law feature.

        :return: Reference
        """

        return Reference(self.hybrid_shape_sweep_circle.RadiusLaw)

    @radius_law.setter
    def radius_law(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_sweep_circle.RadiusLaw = value

    @property
    def radius_law_inversion(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RadiusLawInversion() As long
                | 
                |     Returns or sets the radius law inversion information.

        :return: int
        """

        return self.hybrid_shape_sweep_circle.RadiusLawInversion

    @radius_law_inversion.setter
    def radius_law_inversion(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_circle.RadiusLawInversion = value

    @property
    def radius_law_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property RadiusLawType() As long
                | 
                |     Returns or sets the radius law type.

        :return: int
        """

        return self.hybrid_shape_sweep_circle.RadiusLawType

    @radius_law_type.setter
    def radius_law_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_circle.RadiusLawType = value

    @property
    def reference(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Reference() As Reference
                | 
                |     Returns or sets the reference (functional curve or guide surface).

        :return: Reference
        """

        return Reference(self.hybrid_shape_sweep_circle.Reference)

    @reference.setter
    def reference(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_sweep_circle.Reference = value

    @property
    def second_angle_law(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SecondAngleLaw() As Reference
                | 
                |     Returns or sets the second angle law useful in some circular sweep types.

        :return: Reference
        """

        return Reference(self.hybrid_shape_sweep_circle.SecondAngleLaw)

    @second_angle_law.setter
    def second_angle_law(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_sweep_circle.SecondAngleLaw = value

    @property
    def second_angle_law_inversion(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SecondAngleLawInversion() As long
                | 
                |     Returns or sets the second angle law inversion information.

        :return: int
        """

        return self.hybrid_shape_sweep_circle.SecondAngleLawInversion

    @second_angle_law_inversion.setter
    def second_angle_law_inversion(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_circle.SecondAngleLawInversion = value

    @property
    def second_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SecondGuideCrv() As Reference
                | 
                |     Returns or sets the sweep operation second guide curve.

        :return: Reference
        """

        return Reference(self.hybrid_shape_sweep_circle.SecondGuideCrv)

    @second_guide_crv.setter
    def second_guide_crv(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_sweep_circle.SecondGuideCrv = value

    @property
    def smooth_activity(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SmoothActivity() As boolean
                | 
                |     Returns or sets information whether a sweeping operation is smoothed or
                |     not.
                |     TRUE if the sweeping operation is smoothed, or FALSE otherwise (FALSE if
                |     not specified).

        :return: bool
        """

        return self.hybrid_shape_sweep_circle.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_sweep_circle.SmoothActivity = value

    @property
    def smooth_angle_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property SmoothAngleThreshold() As Angle (Read Only)
                | 
                |     Returns the angular threshold.

        :return: Angle
        """

        return Angle(self.hybrid_shape_sweep_circle.SmoothAngleThreshold)

    @property
    def spine(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Spine() As Reference
                | 
                |     Returns or sets the sweep operation spine (optional).

        :return: Reference
        """

        return Reference(self.hybrid_shape_sweep_circle.Spine)

    @spine.setter
    def spine(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_sweep_circle.Spine = value

    @property
    def third_guide_crv(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property ThirdGuideCrv() As Reference
                | 
                |     Returns or sets the sweep operation third guide curve.

        :return: Reference
        """

        return Reference(self.hybrid_shape_sweep_circle.ThirdGuideCrv)

    @third_guide_crv.setter
    def third_guide_crv(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_sweep_circle.ThirdGuideCrv = value

    @property
    def trim_option(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property TrimOption() As long
                | 
                |     Returns or sets the trim option status.
                |     The trim option status legal values are:
                |     0 No trim computed or undefined
                |     (CATGSMSweepTrimMode_None)
                |     1 Trim computed (CATGSMSweepTrimMode_On)

        :return: int
        """

        return self.hybrid_shape_sweep_circle.TrimOption

    @trim_option.setter
    def trim_option(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_sweep_circle.TrimOption = value

    def get_angle(self, i_i):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetAngle(long iI) As Angle
                | 
                |     Returns the angle values useful in some circular sweep
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
        :return: Angle
        """
        return Angle(self.hybrid_shape_sweep_circle.GetAngle(i_i))

    def get_angle_law_types(self, o_first_type, o_second_type):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetAngleLawTypes(long oFirstType,
                | long oSecondType)
                | 
                |     Retrieves angle law types.
                | 
                |     Parameters:
                | 
                |         oFirstType
                |             The first type of law (from CATGSMBasicLawType
                |             enumeration).
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)
                |         oSecondType
                |             The second type of law (from CATGSMBasicLawType
                |             enumeration).
                |             Same legal values as oFirstType

        :param int o_first_type:
        :param int o_second_type:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.GetAngleLawTypes(o_first_type, o_second_type)

    def get_first_angle_law(self, o_elem1, o_elem2, ol_law_type):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetFirstAngleLaw(Angle oElem1,
                | Angle oElem2,
                | long olLawType)
                | 
                |     Retrieves the first angle law useful in some circular sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         oElem1
                |             The angle law start value 
                |         oElem2
                |             The angle law end value 
                |         olLawType
                |             The angle law type

        :param Angle o_elem1:
        :param Angle o_elem2:
        :param int ol_law_type:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.GetFirstAngleLaw(o_elem1.com_object, o_elem2.com_object, ol_law_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_first_angle_law'
        # # vba_code = """
        # # Public Function get_first_angle_law(hybrid_shape_sweep_circle)
        # #     Dim oElem1 (2)
        # #     hybrid_shape_sweep_circle.GetFirstAngleLaw oElem1
        # #     get_first_angle_law = oElem1
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_longitudinal_relimiters(self, op_ia_elem1, op_ia_elem2):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetLongitudinalRelimiters(Reference opIAElem1,
                | Reference opIAElem2)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepCircle#GetRelimiters Retrieves the elements
                |         relimiting the spine (or the default spine). 
                |     Parameters:
                | 
                |         opIAElem1
                |             The first relimiting feature (plane or point) 
                |         opIAElem2
                |             The second relimiting feature (plane or point)

        :param Reference op_ia_elem1:
        :param Reference op_ia_elem2:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.GetLongitudinalRelimiters(op_ia_elem1.com_object, op_ia_elem2.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_longitudinal_relimiters'
        # # vba_code = """
        # # Public Function get_longitudinal_relimiters(hybrid_shape_sweep_circle)
        # #     Dim opIAElem1 (2)
        # #     hybrid_shape_sweep_circle.GetLongitudinalRelimiters opIAElem1
        # #     get_longitudinal_relimiters = opIAElem1
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_nb_angle(self, o_ang):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetNbAngle(long oAng)
                | 
                |     Retrieves the number of angles.
                | 
                |     Parameters:
                | 
                |         oAng
                |             The number of angles

        :param int o_ang:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.GetNbAngle(o_ang)

    def get_nb_guide(self, o_num):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetNbGuide(long oNum)
                | 
                |     Retrieves the number of guide curves.
                | 
                |     Parameters:
                | 
                |         oNum
                |             The number of guide curves

        :param int o_num:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.GetNbGuide(o_num)

    def get_nb_radius(self, o_rad):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetNbRadius(long oRad)
                | 
                |     Retrieves the number of radii.
                | 
                |     Parameters:
                | 
                |         oRad
                |             The number of radii

        :param int o_rad:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.GetNbRadius(o_rad)

    def get_radius(self, i_i):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetRadius(long iI) As Length
                | 
                |     Returns the radius value useful in some circular sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The radius value index (1: start value, 2: end value)
                |             
                | 
                |     Returns:
                |         The radius value

        :param int i_i:
        :return: Length
        """
        return Length(self.hybrid_shape_sweep_circle.GetRadius(i_i))

    def get_relimiters(self, op_ia_elem1, op_orient1, op_ia_elem2, op_orient2):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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
        :return: None
        """
        return self.hybrid_shape_sweep_circle.GetRelimiters(op_ia_elem1.com_object,
                                                            op_orient1,
                                                            op_ia_elem2.com_object,
                                                            op_orient2)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_relimiters'
        # # vba_code = """
        # # Public Function get_relimiters(hybrid_shape_sweep_circle)
        # #     Dim opIAElem1 (2)
        # #     hybrid_shape_sweep_circle.GetRelimiters opIAElem1
        # #     get_relimiters = opIAElem1
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_second_angle_law(self, o_elem1, o_elem2, ol_law_type):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetSecondAngleLaw(Angle oElem1,
                | Angle oElem2,
                | long olLawType)
                | 
                |     Retrieves the second angle law useful in some circular sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         oElem1
                |             The angle law start value 
                |         oElem2
                |             The angle law end value 
                |         olLawType
                |             The angle law type

        :param Angle o_elem1:
        :param Angle o_elem2:
        :param int ol_law_type:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.GetSecondAngleLaw(o_elem1.com_object, o_elem2.com_object, ol_law_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_second_angle_law'
        # # vba_code = """
        # # Public Function get_second_angle_law(hybrid_shape_sweep_circle)
        # #     Dim oElem1 (2)
        # #     hybrid_shape_sweep_circle.GetSecondAngleLaw oElem1
        # #     get_second_angle_law = oElem1
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_tangency_choice_no(self, o_no, o_shell_ori, o_guide_ori):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetTangencyChoiceNo(long oNo,
                | long oShellOri,
                | long oGuideOri)
                | 
                |     Retrieves a sequence which identifies a solution among all possibilities of
                |     a circular profile sweep tangent to a surface. (case
                |     CATGSMCircularSweep_GuideAndTangencyAndRadius).
                | 
                |     Parameters:
                | 
                |         oNo
                |             Given the orientations, solution number in a distance ordered list.
                |             
                |         oShellOri
                |             This orientation allows to compute just the results that are
                |             tangent to a specific side of the shell. It can take three
                |             values:
                |             +1 The result is on the normal side of the shell
                |             -1 The result is on the side of the shell opposite to the
                |             normal
                |             0 No orientation is specified
                |         oGuideOri
                |             This orientation allows to compute just the results that are on the
                |             "left" or the "right" side of the shell, when looking in the guide direction.
                |             It can take three values:
                |             +1 The result is on the "left" side
                |             -1 The result is on the "right" side
                |             0 No orientation is specified

        :param int o_no:
        :param int o_shell_ori:
        :param int o_guide_ori:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.GetTangencyChoiceNo(o_no, o_shell_ori, o_guide_ori)

    def remove_angle(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveAngle()
                | 
                |     Removes an angle.

        :return: None
        """
        return self.hybrid_shape_sweep_circle.RemoveAngle()

    def remove_guide(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveGuide()
                | 
                |     Removes a guide curve.

        :return: None
        """
        return self.hybrid_shape_sweep_circle.RemoveGuide()

    def remove_radius(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveRadius()
                | 
                |     Removes a radius.

        :return: None
        """
        return self.hybrid_shape_sweep_circle.RemoveRadius()

    def set_angle(self, i_i, i_elem):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetAngle(long iI,
                | double iElem)
                | 
                |     Sets the angle values useful in some circular sweep types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The angle value index 
                |         iElem
                |             The angle value

        :param int i_i:
        :param float i_elem:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.SetAngle(i_i, i_elem)

    def set_angle_law_types(self, i_first_type, i_second_type):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetAngleLawTypes(long iFirstType,
                | long iSecondType)
                | 
                |     Sets angle law types.
                | 
                |     Parameters:
                | 
                |         iFirstType
                |             The first type of law (from CATGSMBasicLawType
                |             enumeration).
                |             Legal values:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)
                |         iSecondType
                |             The second type of law (from CATGSMBasicLawType
                |             enumeration).
                |             Same legal values as iFirstType

        :param int i_first_type:
        :param int i_second_type:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.SetAngleLawTypes(i_first_type, i_second_type)

    def set_first_angle_law(self, i_elem1, i_elem2, il_law_type):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFirstAngleLaw(double iElem1,
                | double iElem2,
                | long ilLawType)
                | 
                |     Sets the first angle law useful in some circular sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iElem1
                |             The angle law start value 
                |         iElem2
                |             The angle law end value 
                |         ilLawType
                |             The angle law type

        :param float i_elem1:
        :param float i_elem2:
        :param int il_law_type:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.SetFirstAngleLaw(i_elem1, i_elem2, il_law_type)

    def set_guide_deviation(self, i_length):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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
        :return: None
        """
        return self.hybrid_shape_sweep_circle.SetGuideDeviation(i_length)

    def set_longitudinal_relimiters(self, ip_ia_elem1, ip_ia_elem2):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetLongitudinalRelimiters(Reference ipIAElem1,
                | Reference ipIAElem2)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepCircle#SetRelimiters Sets the elements
                |         relimiting the spine (or the default spine). 
                |     Parameters:
                | 
                |         ipIAElem1
                |             The first relimiting feature (plane or point) 
                |         ipIAElem2
                |             The second relimiting feature (plane or point)

        :param Reference ip_ia_elem1:
        :param Reference ip_ia_elem2:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.SetLongitudinalRelimiters(ip_ia_elem1.com_object, ip_ia_elem2.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_longitudinal_relimiters'
        # # vba_code = """
        # # Public Function set_longitudinal_relimiters(hybrid_shape_sweep_circle)
        # #     Dim ipIAElem1 (2)
        # #     hybrid_shape_sweep_circle.SetLongitudinalRelimiters ipIAElem1
        # #     set_longitudinal_relimiters = ipIAElem1
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_radius(self, i_i, i_radius):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetRadius(long iI,
                | double iRadius)
                | 
                |     Sets the radius value useful in some circular sweep types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The radius value index (1: start value, 2: end value)
                |             
                |         iRadius
                |             The radius value

        :param int i_i:
        :param float i_radius:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.SetRadius(i_i, i_radius)

    def set_relimiters(self, ip_ia_elem1, ip_orient1, ip_ia_elem2, ip_orient2):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
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
        :return: None
        """
        return self.hybrid_shape_sweep_circle.SetRelimiters(ip_ia_elem1.com_object,
                                                            ip_orient1,
                                                            ip_ia_elem2.com_object,
                                                            ip_orient2
                                                            )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_relimiters'
        # # vba_code = """
        # # Public Function set_relimiters(hybrid_shape_sweep_circle)
        # #     Dim ipIAElem1 (2)
        # #     hybrid_shape_sweep_circle.SetRelimiters ipIAElem1
        # #     set_relimiters = ipIAElem1
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_second_angle_law(self, i_elem1, i_elem2, il_law_type):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSecondAngleLaw(double iElem1,
                | double iElem2,
                | long ilLawType)
                | 
                |     Sets the second angle law useful in some circular sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iElem1
                |             The angle law start value 
                |         iElem2
                |             The angle law end value 
                |         ilLawType
                |             Tha angle law type

        :param float i_elem1:
        :param float i_elem2:
        :param int il_law_type:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.SetSecondAngleLaw(i_elem1, i_elem2, il_law_type)

    def set_smooth_angle_threshold(self, i_angle):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSmoothAngleThreshold(double iAngle)
                | 
                |     Sets the angular threshold.
                | 
                |     Parameters:
                | 
                |         iAngle
                |             The angular threshold

        :param float i_angle:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.SetSmoothAngleThreshold(i_angle)

    def set_tangency_choice_no(self, i_shell_ori, i_guide_ori, i_no):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetTangencyChoiceNo(long iShellOri,
                | long iGuideOri,
                | long iNo)
                | 
                |     Sets a sequence which identifies a solution among all possibilities of a
                |     circular profile sweep tangent to a surface.
                | 
                |     Parameters:
                | 
                |         iNo
                |             Given the orientations, solution number in a distance ordered list.
                |             
                |         iShellOri
                |             This orientation allows to compute just the results that are
                |             tangent to a specific side of the shell. It can take three
                |             values:
                |             +1 The result is on the normal side of the shell
                |             -1 The result is on the side of the shell opposite to the
                |             normal
                |             0 No orientation is specified
                |         iGuideOri
                |             This orientation allows to compute just the results that are on the
                |             "left" or the "right" side of the shell, when looking in the guide direction.
                |             It can take three values:
                |             +1 The result is on the "left" side
                |             -1 The result is on the "right" side
                |             0 No orientation is specified

        :param int i_shell_ori:
        :param int i_guide_ori:
        :param int i_no:
        :return: None
        """
        return self.hybrid_shape_sweep_circle.SetTangencyChoiceNo(i_shell_ori, i_guide_ori, i_no)

    def __repr__(self):
        return f'HybridShapeSweepCircle(name="{self.name}")'
