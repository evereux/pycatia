#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeCurveSmooth(HybridShape):
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
                |                         HybridShapeCurveSmooth
                | 
                | Represents the hybrid shape curve smoothing operation feature.
                | Role: To access the data of the curve smoothing operation.of the hybrid shape
                | curve parameter object. This data includes:
                | 
                |     The curve to smooth
                |     The support (if exist )
                |     The tangent tolerance value (threshold)
                |     The curvature tolerance value (threshold)
                |     The info if curvature threshold is activated
                |     The maximum deviation accepted
                |     The info if maxcimum deviation is activated
                |     The fixed points
                |     The fixed segments
                |     The info if topology simplification is activated
                | 
                | Use the HybridShapeFactory.AddNewCurveSmooth to create a HybridShapeCurveSmooth
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_curve_smooth = com_object

    @property
    def correction_mode(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CorrectionMode() As long
                | 
                |     Returns or sets the correction mode (threshold, point, tangency or
                |     curvature) applied to the smoothed curve.
                |     Legal values:
                | 
                |     0
                |         CATGSMCSCorrectionMode_Threshold. no continuity 
                |     1
                |         CATGSMCSCorrectionMode_Point. continuity in point
                |         (C0).
                |     2
                |         CATGSMCSCorrectionMode_Tangency. continuity in tangency
                |         (C1).
                |     3
                |         CATGSMCSCorrectionMode_Curvature. continuity in curvature
                |         (C2).
                | 
                | Example:
                |     This example retrieves in oMode the correction mode for the
                |     hybShpCurveSmooth hybrid shape feature.
                | 
                |      oMode = hybShpCurveSmooth.CorrectionMode

        :rtype: int
        """

        return self.hybrid_shape_curve_smooth.CorrectionMode

    @correction_mode.setter
    def correction_mode(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_curve_smooth.CorrectionMode = value

    @property
    def curvature_threshold(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CurvatureThreshold() As double
                | 
                |     Returns or sets the CurvatureThreshold.
                | 
                |     Example: This example retrieves the CurvatureThreshold of the
                |     hybShpCurveSmooth in CurvatureThH.
                | 
                |      Dim CurvatureThH as double
                |      CurvatureThH = hybShpCurvePar.CurvatureThreshold

        :rtype: float
        """

        return self.hybrid_shape_curve_smooth.CurvatureThreshold

    @curvature_threshold.setter
    def curvature_threshold(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_curve_smooth.CurvatureThreshold = value

    @property
    def curvature_threshold_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CurvatureThresholdActivity() As boolean
                | 
                |     Returns or sets the CurvatureThresholdActivity.
                | 
                |     Example: This example retrieves the CurvatureThresholdActivity of the
                |     hybShpCurveSmooth in CurvatureActivity .
                | 
                |      Dim CurvatureActivity as boolean 
                |      CurvatureActivity = hybShpCurvePar.CurvatureThresholdActivity

        :rtype: bool
        """

        return self.hybrid_shape_curve_smooth.CurvatureThresholdActivity

    @curvature_threshold_activity.setter
    def curvature_threshold_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_curve_smooth.CurvatureThresholdActivity = value

    @property
    def curve_to_smooth(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property CurveToSmooth() As Reference
                | 
                |     Returns or sets the curve to smooth.
                | 
                |     Example: This example retrieves the curve to smooth object of the
                |     hybShpCurveSmooth in Curve.
                | 
                |      Dim Curve as CATIAReference 
                |      Curve  = hybShpCurvePar.CurveToSmooth

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_curve_smooth.CurveToSmooth)

    @curve_to_smooth.setter
    def curve_to_smooth(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_curve_smooth.CurveToSmooth = reference_curve.com_object

    @property
    def end_extremity_continuity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndExtremityContinuity() As long
                | 
                |     Returns or sets the continuity condition (curvature, tangency or point)
                |     applied to the smoothed curve with regard to the input curve at the end
                |     extremity of the input curve.
                |     Legal values:
                | 
                |     0
                |         CATGSMContinuity_Point. continuity in point (C0). 
                |     1
                |         CATGSMContinuity_Tangency. continuity in tangency
                |         (C1).
                |     2
                |         CATGSMContinuity_Curvature. continuity in curvature
                |         (C2).
                | 
                | Example:
                |     This example retrieves in oContinuity the continuity at the end extremity
                |     for the hybShpCurveSmooth hybrid shape feature.
                | 
                |      oContinuity = hybShpCurveSmooth.EndExtremityContinuity

        :rtype: int
        """

        return self.hybrid_shape_curve_smooth.EndExtremityContinuity

    @end_extremity_continuity.setter
    def end_extremity_continuity(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_curve_smooth.EndExtremityContinuity = value

    @property
    def maximum_deviation(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MaximumDeviation() As Length (Read Only)
                | 
                |     Returns the MaximumDeviation.
                | 
                |     Example: This example retrieves the MaximumDeviation of the
                |     hybShpCurveSmooth in MaximumDeviationVal.
                | 
                |      Dim MaximumDeviationVal as CATIALength
                |      MaximumDeviationVal  = hybShpCurvePar.MaximumDeviation

        :rtype: Length
        """

        return Length(self.hybrid_shape_curve_smooth.MaximumDeviation)

    @property
    def maximum_deviation_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property MaximumDeviationActivity() As boolean
                | 
                |     Returns or sets the MaximumDeviationActivity.
                | 
                |     Example: This example retrieves the MaximumDeviationActivity of the
                |     hybShpCurveSmooth in MaxActivity .
                | 
                |      Dim MaxActivity as boolean
                |      MaxActivity  = hybShpCurvePar.MaximumDeviationActivity

        :rtype: bool
        """

        return self.hybrid_shape_curve_smooth.MaximumDeviationActivity

    @maximum_deviation_activity.setter
    def maximum_deviation_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_curve_smooth.MaximumDeviationActivity = value

    @property
    def start_extremity_continuity(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StartExtremityContinuity() As long
                | 
                |     Returns or sets the continuity condition (curvature, tangency or point)
                |     applied to the smoothed curve with regard to the input curve at the start
                |     extremity of the input curve.
                |     Legal values:
                | 
                |     0
                |         CATGSMContinuity_Point. continuity in point (C0). 
                |     1
                |         CATGSMContinuity_Tangency. continuity in tangency
                |         (C1).
                |     2
                |         CATGSMContinuity_Curvature. continuity in curvature
                |         (C2).
                | 
                | Example:
                |     This example retrieves in oContinuity the continuity at the start extremity
                |     for the hybShpCurveSmooth hybrid shape feature.
                | 
                |      oContinuity = hybShpCurveSmooth.StartExtremityContinuity

        :rtype: int
        """

        return self.hybrid_shape_curve_smooth.StartExtremityContinuity

    @start_extremity_continuity.setter
    def start_extremity_continuity(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_curve_smooth.StartExtremityContinuity = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support of the curve.
                |     if Suppport == nothing no support associated to the curve
                | 
                |     Example: This example retrieves the support of curve to smooth object of
                |     the hybShpCurveSmooth in Support.
                | 
                |      Dim Support  as CATIAReference 
                |      Support   = ybShpCurveSmooth.Support

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_curve_smooth.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_curve_smooth.Support = reference_support.com_object

    @property
    def tangency_threshold(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TangencyThreshold() As Angle (Read Only)
                | 
                |     Returns the TangencyThreshold.
                | 
                |     Example: This example retrieves the curve to smooth object of the
                |     hybShpCurveSmooth in AngleThH.
                | 
                |      Dim Curve as CATIAAngle  
                |      AngleThH  = ybShpCurveSmooth.TangencyThreshold

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_curve_smooth.TangencyThreshold)

    @property
    def topology_simplification_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TopologySimplificationActivity() As boolean
                | 
                |     Returns or sets the TopologySimplificationActivity.
                | 
                |     Example: This example retrieves the TopologySimplificationActivity of the
                |     hybShpCurveSmooth in TopSimplifyAct.
                | 
                |      Dim TopSimplifyAct as boolean 
                |      TopSimplifyAct  = hybShpCurvePar.TogologySimplificationActivity 
                |      
                | 
                |     Methods
                | 
                | o Sub AddFrozenCurveSegment(Reference iCurve)
                | 
                |     Adds a frozen curve to the hybrid shape curve smooth feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iCurve
                |             The curve to be added to the hybrid shape curve smooth feature
                |             object. 
                | 
                |     Example:
                |         The following example adds the iCurve curve to the hybShpCurveSmooth
                |         object.
                | 
                |          hybShpCurveSmooth.AddFrozenCurveSegment iCurve
                |          
                | 
                | o Sub AddFrozenPoint(Reference iPoint)
                | 
                |     Adds a frozen points to the hybrid shape curve smooth feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             The frozen point to be added to the hybrid shape curve smooth
                |             feature object. 
                | 
                |     Example:
                |         The following example adds the iPoint frozen point to the
                |         hybShpCurveSmooth object.
                | 
                |          hybShpCurveSmooth.AddFrozenPoint iPoint
                |          
                | 
                | o Func GetFrozenCurveSegment(long iPos) As Reference
                | 
                |     Retrieves the Frozen Curve Segment at specified position in the hybrid
                |     shape curve smooth object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the Frozen Curve Segment to retrieve.
                |             
                | 
                |     Example:
                |         The following example gets the oCurve Frozen Curve Segment of the
                |         hybShpCurveSmooth object at the position iPos.
                | 
                |          Dim oCurve As Reference
                |          Set oCurve = hybShpCurveSmooth.GetFrozenCurveSegment (iPos).
                |          
                | 
                | o Func GetFrozenCurveSegmentsSize() As long
                | 
                |     Returns the number of frozen curve segments in the curve smooth
                |     object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of frozen curve segments in the curve
                |             smooth.
                | 
                |             Example:
                |                 This example retrieves the number of frozen curve segments. in
                |                 the hybShpCurveSmooth hybrid shape curve
                |                 smooth.
                | 
                |                  Dim oSize As  long
                |                  oSize = hybShpCurveSmooth.GetFrozenCurveSegmentsSize
                |                  
                | 
                | o Func GetFrozenPoint(long iPos) As Reference
                | 
                |     Retrieves the Frozen Point at specified position in the hybrid shape curve
                |     smooth object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the Frozen Point to retrieve. 
                | 
                |     Example:
                |         The following example gets the oPoint Frozen Point of the
                |         hybShpCurveSmooth object at the position iPos.
                | 
                |          Dim oPoint As Reference
                |          Set oPoint = hybShpCurveSmooth.GetFrozenPoint (iPos).
                |          
                | 
                | o Func GetFrozenPointsSize() As long
                | 
                |     Returns the number of Frozen Points in the curve smooth
                |     object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of Frozen Points in the curve smooth.
                | 
                |             Example:
                |                 This example retrieves the number of Frozen Points. in the
                |                 hybShpCurveSmooth hybrid shape curve smooth.
                | 
                |                  Dim oSize As  long
                |                  oSize = hybShpCurveSmooth.GetFrozenPointsSize
                |                  
                | 
                | o Sub RemoveAllFrozenCurveSegments()
                | 
                |     Removes all Frozen Curve Segment of the hybrid shape curve smooth object.
                |     
                | 
                | Example:
                |     The following example removes all Frozen Curve Segments of the
                |     hybShpCurveSmooth object.
                | 
                |      hybShpCurveSmooth.RemoveAllFrozenCurveSegments
                |      
                | 
                | o Sub RemoveAllFrozenPoints()
                | 
                |     Removes all Frozen Points of the hybrid shape curve smooth object.
                |     
                | 
                | Example:
                |     The following example removes all Frozen Points of the hybShpCurveSmooth
                |     object.
                | 
                |      hybShpCurveSmooth.RemoveAllFrozenPoints
                |      
                | 
                | o Sub RemoveFrozenCurveSegment(Reference iCurve)
                | 
                |     Removes Frozen Curve Segment from the list of Forzen curves in hybrid shape
                |     curve smooth object.
                | 
                |     Parameters:
                | 
                |         iCurve
                |             The Frozen Curve Segment to remove. 
                | 
                |     Example:
                |         The following example removes the Frozen Curve Segment from the
                |         hybShpCurveSmooth object.
                | 
                |          hybShpCurveSmooth.RemoveFrozenCurveSegment iCurve.
                |          
                | 
                | o Sub RemoveFrozenPoint(Reference iPoint)
                | 
                |     Removes Frozen Point from the list of frozen points in hybrid shape curve
                |     smooth object.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             The Frozen Point to remove. 
                | 
                |     Example:
                |         The following example removes the Frozen Point from the
                |         hybShpCurveSmooth object.
                | 
                |          hybShpCurveSmooth.RemoveFrozenPoint iPoint.
                |          
                | 
                | o Sub SetMaximumDeviation(double iMaxDeviation)
                | 
                |     Sets the maximum deviation.
                | 
                |     Parameters:
                | 
                |         iMaxDeviation
                |             The maximium deviation
                | 
                | o Sub SetTangencyThreshold(double iTangencyThreshold)
                | 
                |     Sets the tangency threshold.
                | 
                |     Parameters:
                | 
                |         iTangencyThreshold
                |             The tangency threshold

        :rtype: bool
        """

        return self.hybrid_shape_curve_smooth.TopologySimplificationActivity

    @topology_simplification_activity.setter
    def topology_simplification_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_curve_smooth.TopologySimplificationActivity = value

    def add_frozen_curve_segment(self, i_curve: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddFrozenCurveSegment(Reference iCurve)
                |
                |     Adds a frozen curve to the hybrid shape curve smooth feature
                |     object.
                |
                |     Parameters:
                |
                |         iCurve
                |             The curve to be added to the hybrid shape curve smooth feature
                |             object.
                |
                |     Example:
                |         The following example adds the iCurve curve to the hybShpCurveSmooth
                |         object.
                |
                |          hybShpCurveSmooth.AddFrozenCurveSegment iCurve

        :param Reference i_curve:
        :rtype: None
        """
        return self.hybrid_shape_curve_smooth.AddFrozenCurveSegment(i_curve.com_object)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_frozen_curve_segment'
        # # vba_code = """
        # # Public Function add_frozen_curve_segment(hybrid_shape_curve_smooth)
        # #     Dim iCurve (2)
        # #     hybrid_shape_curve_smooth.AddFrozenCurveSegment iCurve
        # #     add_frozen_curve_segment = iCurve
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_frozen_point(self, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddFrozenPoint(Reference iPoint)
                |
                |     Adds a frozen points to the hybrid shape curve smooth feature
                |     object.
                |
                |     Parameters:
                |
                |         iPoint
                |             The frozen point to be added to the hybrid shape curve smooth
                |             feature object.
                |
                |     Example:
                |         The following example adds the iPoint frozen point to the
                |         hybShpCurveSmooth object.
                |
                |          hybShpCurveSmooth.AddFrozenPoint iPoint

        :param Reference i_point:
        :rtype: None
        """
        return self.hybrid_shape_curve_smooth.AddFrozenPoint(i_point.com_object)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_frozen_point'
        # # vba_code = """
        # # Public Function add_frozen_point(hybrid_shape_curve_smooth)
        # #     Dim iPoint (2)
        # #     hybrid_shape_curve_smooth.AddFrozenPoint iPoint
        # #     add_frozen_point = iPoint
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_frozen_curve_segment(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFrozenCurveSegment(long iPos) As Reference
                |
                |     Retrieves the Frozen Curve Segment at specified position in the hybrid
                |     shape curve smooth object.
                |
                |     Parameters:
                |
                |         iPos
                |             The position of the Frozen Curve Segment to retrieve.
                |
                |
                |     Example:
                |         The following example gets the oCurve Frozen Curve Segment of the
                |         hybShpCurveSmooth object at the position iPos.
                |
                |          Dim oCurve As Reference
                |          Set oCurve = hybShpCurveSmooth.GetFrozenCurveSegment (iPos).

        :param int i_pos:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_curve_smooth.GetFrozenCurveSegment(i_pos))

    def get_frozen_curve_segments_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFrozenCurveSegmentsSize() As long
                |
                |     Returns the number of frozen curve segments in the curve smooth
                |     object.
                |
                |     Parameters:
                |
                |         oSize
                |             Number of frozen curve segments in the curve
                |             smooth.
                |
                |             Example:
                |                 This example retrieves the number of frozen curve segments. in
                |                 the hybShpCurveSmooth hybrid shape curve
                |                 smooth.
                |
                |                  Dim oSize As  long
                |                  oSize = hybShpCurveSmooth.GetFrozenCurveSegmentsSize

        :rtype: int
        """
        return self.hybrid_shape_curve_smooth.GetFrozenCurveSegmentsSize()

    def get_frozen_point(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFrozenPoint(long iPos) As Reference
                |
                |     Retrieves the Frozen Point at specified position in the hybrid shape curve
                |     smooth object.
                |
                |     Parameters:
                |
                |         iPos
                |             The position of the Frozen Point to retrieve.
                |
                |     Example:
                |         The following example gets the oPoint Frozen Point of the
                |         hybShpCurveSmooth object at the position iPos.
                |
                |          Dim oPoint As Reference
                |          Set oPoint = hybShpCurveSmooth.GetFrozenPoint (iPos).

        :param int i_pos:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_curve_smooth.GetFrozenPoint(i_pos))

    def get_frozen_points_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetFrozenPointsSize() As long
                |
                |     Returns the number of Frozen Points in the curve smooth
                |     object.
                |
                |     Parameters:
                |
                |         oSize
                |             Number of Frozen Points in the curve smooth.
                |
                |             Example:
                |                 This example retrieves the number of Frozen Points. in the
                |                 hybShpCurveSmooth hybrid shape curve smooth.
                |
                |                  Dim oSize As  long
                |                  oSize = hybShpCurveSmooth.GetFrozenPointsSize

        :rtype: int
        """
        return self.hybrid_shape_curve_smooth.GetFrozenPointsSize()

    def remove_all_frozen_curve_segments(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveAllFrozenCurveSegments()
                |
                |     Removes all Frozen Curve Segment of the hybrid shape curve smooth object.
                |
                |
                | Example:
                |     The following example removes all Frozen Curve Segments of the
                |     hybShpCurveSmooth object.
                |
                |      hybShpCurveSmooth.RemoveAllFrozenCurveSegments

        :rtype: None
        """
        return self.hybrid_shape_curve_smooth.RemoveAllFrozenCurveSegments()

    def remove_all_frozen_points(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveAllFrozenPoints()
                |
                |     Removes all Frozen Points of the hybrid shape curve smooth object.
                |
                |
                | Example:
                |     The following example removes all Frozen Points of the hybShpCurveSmooth
                |     object.
                |
                |      hybShpCurveSmooth.RemoveAllFrozenPoints

        :rtype: None
        """
        return self.hybrid_shape_curve_smooth.RemoveAllFrozenPoints()

    def remove_frozen_curve_segment(self, i_curve: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveFrozenCurveSegment(Reference iCurve)
                |
                |     Removes Frozen Curve Segment from the list of Forzen curves in hybrid shape
                |     curve smooth object.
                |
                |     Parameters:
                |
                |         iCurve
                |             The Frozen Curve Segment to remove.
                |
                |     Example:
                |         The following example removes the Frozen Curve Segment from the
                |         hybShpCurveSmooth object.
                |
                |          hybShpCurveSmooth.RemoveFrozenCurveSegment iCurve.

        :param Reference i_curve:
        :rtype: None
        """
        return self.hybrid_shape_curve_smooth.RemoveFrozenCurveSegment(i_curve.com_object)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_frozen_curve_segment'
        # # vba_code = """
        # # Public Function remove_frozen_curve_segment(hybrid_shape_curve_smooth)
        # #     Dim iCurve (2)
        # #     hybrid_shape_curve_smooth.RemoveFrozenCurveSegment iCurve
        # #     remove_frozen_curve_segment = iCurve
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_frozen_point(self, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveFrozenPoint(Reference iPoint)
                |
                |     Removes Frozen Point from the list of frozen points in hybrid shape curve
                |     smooth object.
                |
                |     Parameters:
                |
                |         iPoint
                |             The Frozen Point to remove.
                |
                |     Example:
                |         The following example removes the Frozen Point from the
                |         hybShpCurveSmooth object.
                |
                |          hybShpCurveSmooth.RemoveFrozenPoint iPoint.

        :param Reference i_point:
        :rtype: None
        """
        return self.hybrid_shape_curve_smooth.RemoveFrozenPoint(i_point.com_object)
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_frozen_point'
        # # vba_code = """
        # # Public Function remove_frozen_point(hybrid_shape_curve_smooth)
        # #     Dim iPoint (2)
        # #     hybrid_shape_curve_smooth.RemoveFrozenPoint iPoint
        # #     remove_frozen_point = iPoint
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_maximum_deviation(self, i_max_deviation: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetMaximumDeviation(double iMaxDeviation)
                |
                |     Sets the maximum deviation.
                |
                |     Parameters:
                |
                |         iMaxDeviation
                |             The maximium deviation

        :param float i_max_deviation:
        :rtype: None
        """
        return self.hybrid_shape_curve_smooth.SetMaximumDeviation(i_max_deviation)

    def set_tangency_threshold(self, i_tangency_threshold: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTangencyThreshold(double iTangencyThreshold)
                |
                |     Sets the tangency threshold.
                |
                |     Parameters:
                |
                |         iTangencyThreshold
                |             The tangency threshold

        :param float i_tangency_threshold:
        :rtype: None
        """
        return self.hybrid_shape_curve_smooth.SetTangencyThreshold(i_tangency_threshold)

    def __repr__(self):
        return f'HybridShapeCurveSmooth(name="{self.name}")'
