#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeCurveSmooth(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape curve smoothing operation feature.Role: To
                | access the data of the curve smoothing operation.of the hybrid shape
                | curve parameter object. This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_curve_smooth = com_object     

    @property
    def correction_mode(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CorrectionMode
                | o Property CorrectionMode(    ) As
                | 
                | Returns or sets the correction mode (threshold, point,
                | tangency or curvature) applied to the smoothed curve. Legal
                | values: 0 CATGSMCSCorrectionMode_Threshold. no continuity 1
                | CATGSMCSCorrectionMode_Point. continuity in point (C0). 2
                | CATGSMCSCorrectionMode_Tangency. continuity in tangency
                | (C1). 3 CATGSMCSCorrectionMode_Curvature. continuity in
                | curvature (C2).

        :return:
        """
        return self.hybrid_shape_curve_smooth.CorrectionMode

    @correction_mode.setter
    def correction_mode(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_smooth.CorrectionMode = value 

    @property
    def curvature_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CurvatureThreshold
                | o Property CurvatureThreshold(    ) As
                | 
                | Returns or sets the CurvatureThreshold. 
                |
                | Example:
                | This
                | example retrieves the CurvatureThreshold of the
                | hybShpCurveSmooth in CurvatureThH. Dim CurvatureThH as
                | double CurvatureThH = hybShpCurvePar.CurvatureThreshold o
                | Property CurvatureThresholdActivity() As Returns or sets the
                | CurvatureThresholdActivity. 
                |
                | Example:
                | This example retrieves
                | the CurvatureThresholdActivity of the hybShpCurveSmooth in
                | CurvatureActivity . Dim CurvatureActivity as boolean
                | CurvatureActivity =
                | hybShpCurvePar.CurvatureThresholdActivity o Property
                | CurveToSmooth() As Returns or sets the curve to smooth.
                | 
                |
                | Example:
                | This example retrieves the curve to smooth object
                | of the hybShpCurveSmooth in Curve. Dim Curve as
                | CATIAReference Curve = hybShpCurvePar.CurveToSmooth o
                | Property EndExtremityContinuity() As Returns or sets the
                | continuity condition (curvature, tangency or point) applied
                | to the smoothed curve with regard to the input curve at the
                | end extremity of the input curve. Legal values: 0
                | CATGSMContinuity_Point. continuity in point (C0). 1
                | CATGSMContinuity_Tangency. continuity in tangency (C1). 2
                | CATGSMContinuity_Curvature. continuity in curvature (C2).
                | 
                |
                | Example:
                | This example retrieves in oContinuity the
                | continuity at the end extremity for the hybShpCurveSmooth
                | hybrid shape feature. oContinuity =
                | hybShpCurveSmooth.EndExtremityContinuity o Property
                | MaximumDeviation() As (Read Only) Returns the
                | MaximumDeviation. 
                |
                | Example:
                | This example retrieves the
                | MaximumDeviation of the hybShpCurveSmooth in
                | MaximumDeviationVal. Dim MaximumDeviationVal as CATIALength
                | MaximumDeviationVal = hybShpCurvePar.MaximumDeviation o
                | Property MaximumDeviationActivity() As Returns or sets the
                | MaximumDeviationActivity. 
                |
                | Example:
                | This example retrieves
                | the MaximumDeviationActivity of the hybShpCurveSmooth in
                | MaxActivity . Dim MaxActivity as boolean MaxActivity =
                | hybShpCurvePar.MaximumDeviationActivity o Property
                | StartExtremityContinuity() As Returns or sets the continuity
                | condition (curvature, tangency or point) applied to the
                | smoothed curve with regard to the input curve at the start
                | extremity of the input curve. Legal values: 0
                | CATGSMContinuity_Point. continuity in point (C0). 1
                | CATGSMContinuity_Tangency. continuity in tangency (C1). 2
                | CATGSMContinuity_Curvature. continuity in curvature (C2).
                | 
                |
                | Example:
                | This example retrieves in oContinuity the
                | continuity at the start extremity for the hybShpCurveSmooth
                | hybrid shape feature. oContinuity =
                | hybShpCurveSmooth.StartExtremityContinuity o Property
                | Support() As Returns or sets the support of the curve. if
                | Suppport == nothing no support associated to the curve
                | 
                |
                | Example:
                | This example retrieves the support of curve to
                | smooth object of the hybShpCurveSmooth in Support. Dim
                | Support as CATIAReference Support = ybShpCurveSmooth.Support
                | o Property TangencyThreshold() As (Read Only) Returns the
                | TangencyThreshold. 
                |
                | Example:
                | This example retrieves the curve
                | to smooth object of the hybShpCurveSmooth in AngleThH. Dim
                | Curve as CATIAAngle AngleThH =
                | ybShpCurveSmooth.TangencyThreshold o Property
                | TopologySimplificationActivity() As Returns or sets the
                | TopologySimplificationActivity. 
                |
                | Example:
                | This example
                | retrieves the TopologySimplificationActivity of the
                | hybShpCurveSmooth in TopSimplifyAct. Dim TopSimplifyAct as
                | boolean TopSimplifyAct =
                | hybShpCurvePar.TogologySimplificationActivity Methods o Sub
                | AddFrozenCurveSegment( iCurve) Adds a frozen curve to the
                | hybrid shape curve smooth feature object.
                | Examples:
                | The following example adds the iCurve curve to the
                | hybShpCurveSmooth object.
                | hybShpCurveSmooth.AddFrozenCurveSegment iCurve o Sub
                | AddFrozenPoint( iPoint) Adds a frozen points to the hybrid
                | shape curve smooth feature object.

        :return:
        """
        return self.hybrid_shape_curve_smooth.CurvatureThreshold

    @curvature_threshold.setter
    def curvature_threshold(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_smooth.CurvatureThreshold = value 

    @property
    def curvature_threshold_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CurvatureThresholdActivity
                | o Property CurvatureThresholdActivity(    ) As
                | 
                | Returns or sets the CurvatureThresholdActivity. Example:
                | This example retrieves the CurvatureThresholdActivity of the
                | hybShpCurveSmooth in CurvatureActivity . Dim
                | CurvatureActivity as boolean CurvatureActivity =
                | hybShpCurvePar.CurvatureThresholdActivity o Property
                | CurveToSmooth() As Returns or sets the curve to smooth.
                | 
                |
                | Example:
                | This example retrieves the curve to smooth object
                | of the hybShpCurveSmooth in Curve. Dim Curve as
                | CATIAReference Curve = hybShpCurvePar.CurveToSmooth o
                | Property EndExtremityContinuity() As Returns or sets the
                | continuity condition (curvature, tangency or point) applied
                | to the smoothed curve with regard to the input curve at the
                | end extremity of the input curve. Legal values: 0
                | CATGSMContinuity_Point. continuity in point (C0). 1
                | CATGSMContinuity_Tangency. continuity in tangency (C1). 2
                | CATGSMContinuity_Curvature. continuity in curvature (C2).
                | 
                |
                | Example:
                | This example retrieves in oContinuity the
                | continuity at the end extremity for the hybShpCurveSmooth
                | hybrid shape feature. oContinuity =
                | hybShpCurveSmooth.EndExtremityContinuity

        :return:
        """
        return self.hybrid_shape_curve_smooth.CurvatureThresholdActivity

    @curvature_threshold_activity.setter
    def curvature_threshold_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_smooth.CurvatureThresholdActivity = value 

    @property
    def curve_to_smooth(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | CurveToSmooth
                | o Property CurveToSmooth(    ) As
                | 
                | Returns or sets the curve to smooth. 
                |
                | Example:
                | This example
                | retrieves the curve to smooth object of the
                | hybShpCurveSmooth in Curve. Dim Curve as CATIAReference
                | Curve = hybShpCurvePar.CurveToSmooth o Property
                | EndExtremityContinuity() As Returns or sets the continuity
                | condition (curvature, tangency or point) applied to the
                | smoothed curve with regard to the input curve at the end
                | extremity of the input curve. Legal values: 0
                | CATGSMContinuity_Point. continuity in point (C0). 1
                | CATGSMContinuity_Tangency. continuity in tangency (C1). 2
                | CATGSMContinuity_Curvature. continuity in curvature (C2).
                | 
                |
                | Example:
                | This example retrieves in oContinuity the
                | continuity at the end extremity for the hybShpCurveSmooth
                | hybrid shape feature. oContinuity =
                | hybShpCurveSmooth.EndExtremityContinuity

        :return:
        """
        return self.hybrid_shape_curve_smooth.CurveToSmooth

    @curve_to_smooth.setter
    def curve_to_smooth(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_smooth.CurveToSmooth = value 

    @property
    def end_extremity_continuity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndExtremityContinuity
                | o Property EndExtremityContinuity(    ) As
                | 
                | Returns or sets the continuity condition (curvature,
                | tangency or point) applied to the smoothed curve with regard
                | to the input curve at the end extremity of the input curve.
                | Legal values: 0 CATGSMContinuity_Point. continuity in point
                | (C0). 1 CATGSMContinuity_Tangency. continuity in tangency
                | (C1). 2 CATGSMContinuity_Curvature. continuity in curvature
                | (C2).

        :return:
        """
        return self.hybrid_shape_curve_smooth.EndExtremityContinuity

    @end_extremity_continuity.setter
    def end_extremity_continuity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_smooth.EndExtremityContinuity = value 

    @property
    def maximum_deviation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MaximumDeviation
                | o Property MaximumDeviation(    ) As   (Read Only)
                | 
                | Returns the MaximumDeviation. 
                |
                | Example:
                | This example
                | retrieves the MaximumDeviation of the hybShpCurveSmooth in
                | MaximumDeviationVal. Dim MaximumDeviationVal as CATIALength
                | MaximumDeviationVal = hybShpCurvePar.MaximumDeviation o
                | Property MaximumDeviationActivity() As Returns or sets the
                | MaximumDeviationActivity. 
                |
                | Example:
                | This example retrieves
                | the MaximumDeviationActivity of the hybShpCurveSmooth in
                | MaxActivity . Dim MaxActivity as boolean MaxActivity =
                | hybShpCurvePar.MaximumDeviationActivity o Property
                | StartExtremityContinuity() As Returns or sets the continuity
                | condition (curvature, tangency or point) applied to the
                | smoothed curve with regard to the input curve at the start
                | extremity of the input curve. Legal values: 0
                | CATGSMContinuity_Point. continuity in point (C0). 1
                | CATGSMContinuity_Tangency. continuity in tangency (C1). 2
                | CATGSMContinuity_Curvature. continuity in curvature (C2).
                | 
                |
                | Example:
                | This example retrieves in oContinuity the
                | continuity at the start extremity for the hybShpCurveSmooth
                | hybrid shape feature. oContinuity =
                | hybShpCurveSmooth.StartExtremityContinuity

        :return:
        """
        return self.hybrid_shape_curve_smooth.MaximumDeviation

    @maximum_deviation.setter
    def maximum_deviation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_smooth.MaximumDeviation = value 

    @property
    def maximum_deviation_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | MaximumDeviationActivity
                | o Property MaximumDeviationActivity(    ) As
                | 
                | Returns or sets the MaximumDeviationActivity. 
                |
                | Example:
                | This
                | example retrieves the MaximumDeviationActivity of the
                | hybShpCurveSmooth in MaxActivity . Dim MaxActivity as
                | boolean MaxActivity =
                | hybShpCurvePar.MaximumDeviationActivity o Property
                | StartExtremityContinuity() As Returns or sets the continuity
                | condition (curvature, tangency or point) applied to the
                | smoothed curve with regard to the input curve at the start
                | extremity of the input curve. Legal values: 0
                | CATGSMContinuity_Point. continuity in point (C0). 1
                | CATGSMContinuity_Tangency. continuity in tangency (C1). 2
                | CATGSMContinuity_Curvature. continuity in curvature (C2).
                | 
                |
                | Example:
                | This example retrieves in oContinuity the
                | continuity at the start extremity for the hybShpCurveSmooth
                | hybrid shape feature. oContinuity =
                | hybShpCurveSmooth.StartExtremityContinuity

        :return:
        """
        return self.hybrid_shape_curve_smooth.MaximumDeviationActivity

    @maximum_deviation_activity.setter
    def maximum_deviation_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_smooth.MaximumDeviationActivity = value 

    @property
    def start_extremity_continuity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartExtremityContinuity
                | o Property StartExtremityContinuity(    ) As
                | 
                | Returns or sets the continuity condition (curvature,
                | tangency or point) applied to the smoothed curve with regard
                | to the input curve at the start extremity of the input
                | curve. Legal values: 0 CATGSMContinuity_Point. continuity in
                | point (C0). 1 CATGSMContinuity_Tangency. continuity in
                | tangency (C1). 2 CATGSMContinuity_Curvature. continuity in
                | curvature (C2).

        :return:
        """
        return self.hybrid_shape_curve_smooth.StartExtremityContinuity

    @start_extremity_continuity.setter
    def start_extremity_continuity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_smooth.StartExtremityContinuity = value 

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Support
                | o Property Support(    ) As
                | 
                | Returns or sets the support of the curve. if Suppport ==
                | nothing no support associated to the curve 
                |
                | Example:
                | This
                | example retrieves the support of curve to smooth object of
                | the hybShpCurveSmooth in Support. Dim Support as
                | CATIAReference Support = ybShpCurveSmooth.Support o Property
                | TangencyThreshold() As (Read Only) Returns the
                | TangencyThreshold. 
                |
                | Example:
                | This example retrieves the curve
                | to smooth object of the hybShpCurveSmooth in AngleThH. Dim
                | Curve as CATIAAngle AngleThH =
                | ybShpCurveSmooth.TangencyThreshold o Property
                | TopologySimplificationActivity() As Returns or sets the
                | TopologySimplificationActivity. 
                |
                | Example:
                | This example
                | retrieves the TopologySimplificationActivity of the
                | hybShpCurveSmooth in TopSimplifyAct. Dim TopSimplifyAct as
                | boolean TopSimplifyAct =
                | hybShpCurvePar.TogologySimplificationActivity Methods o Sub
                | AddFrozenCurveSegment( iCurve) Adds a frozen curve to the
                | hybrid shape curve smooth feature object.
                | Examples:
                | The following example adds the iCurve curve to the
                | hybShpCurveSmooth object.
                | hybShpCurveSmooth.AddFrozenCurveSegment iCurve o Sub
                | AddFrozenPoint( iPoint) Adds a frozen points to the hybrid
                | shape curve smooth feature object.

        :return:
        """
        return self.hybrid_shape_curve_smooth.Support

    @support.setter
    def support(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_smooth.Support = value 

    @property
    def tangency_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TangencyThreshold
                | o Property TangencyThreshold(    ) As   (Read Only)
                | 
                | Returns the TangencyThreshold. 
                |
                | Example:
                | This example
                | retrieves the curve to smooth object of the
                | hybShpCurveSmooth in AngleThH. Dim Curve as CATIAAngle
                | AngleThH = ybShpCurveSmooth.TangencyThreshold o Property
                | TopologySimplificationActivity() As Returns or sets the
                | TopologySimplificationActivity. 
                |
                | Example:
                | This example
                | retrieves the TopologySimplificationActivity of the
                | hybShpCurveSmooth in TopSimplifyAct. Dim TopSimplifyAct as
                | boolean TopSimplifyAct =
                | hybShpCurvePar.TogologySimplificationActivity Methods o Sub
                | AddFrozenCurveSegment( iCurve) Adds a frozen curve to the
                | hybrid shape curve smooth feature object.
                | Examples:
                | The following example adds the iCurve curve to the
                | hybShpCurveSmooth object.
                | hybShpCurveSmooth.AddFrozenCurveSegment iCurve o Sub
                | AddFrozenPoint( iPoint) Adds a frozen points to the hybrid
                | shape curve smooth feature object.

        :return:
        """
        return self.hybrid_shape_curve_smooth.TangencyThreshold

    @tangency_threshold.setter
    def tangency_threshold(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_smooth.TangencyThreshold = value 

    @property
    def topology_simplification_activity(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TopologySimplificationActivity
                | o Property TopologySimplificationActivity(    ) As
                | 
                | Returns or sets the TopologySimplificationActivity. Example:
                | This example retrieves the TopologySimplificationActivity of
                | the hybShpCurveSmooth in TopSimplifyAct. Dim TopSimplifyAct
                | as boolean TopSimplifyAct =
                | hybShpCurvePar.TogologySimplificationActivity Methods o Sub
                | AddFrozenCurveSegment( iCurve) Adds a frozen curve to the
                | hybrid shape curve smooth feature object.
                | Examples:
                | The following example adds the iCurve curve to the
                | hybShpCurveSmooth object.
                | hybShpCurveSmooth.AddFrozenCurveSegment iCurve

        :return:
        """
        return self.hybrid_shape_curve_smooth.TopologySimplificationActivity

    @topology_simplification_activity.setter
    def topology_simplification_activity(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_curve_smooth.TopologySimplificationActivity = value 

    def add_frozen_curve_segment(self, i_curve):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddFrozenCurveSegment
                | o Sub AddFrozenCurveSegment(        iCurve)
                | 
                | Adds a frozen curve to the hybrid shape curve smooth feature
                | object.
                |
                | Parameters:
                | iCurve
                | 		The curve to be added to the hybrid shape curve smooth feature object.

                | Examples:
                | The following example adds the iCurve curve to the
                | hybShpCurveSmooth object.
                | hybShpCurveSmooth.AddFrozenCurveSegment iCurve

        :param i_curve:
        :return:
        """
        return self.hybrid_shape_curve_smooth.AddFrozenCurveSegment(i_curve)

    def add_frozen_point(self, i_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | AddFrozenPoint
                | o Sub AddFrozenPoint(        iPoint)
                | 
                | Adds a frozen points to the hybrid shape curve smooth
                | feature object.
                |
                | Parameters:
                | iPoint
                | 		The frozen point to be added to the hybrid shape curve smooth feature object.

                | Examples:
                | The following example adds the iPoint frozen point to the
                | hybShpCurveSmooth object. hybShpCurveSmooth.AddFrozenPoint
                | iPoint

        :param i_point:
        :return:
        """
        return self.hybrid_shape_curve_smooth.AddFrozenPoint(i_point)

    def get_frozen_curve_segment(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFrozenCurveSegment
                | o Func GetFrozenCurveSegment(        iPos) As
                | 
                | Retrieves the Frozen Curve Segment at specified position in
                | the hybrid shape curve smooth object.
                |
                | Parameters:
                | iPos
                | 		The position of the Frozen Curve Segment to retrieve.

                | Examples:
                | The following example gets the oCurve Frozen Curve Segment
                | of the hybShpCurveSmooth object at the position iPos. Dim
                | oCurve As Reference Set oCurve =
                | hybShpCurveSmooth.GetFrozenCurveSegment (iPos).

        :param i_pos:
        :return:
        """
        return self.hybrid_shape_curve_smooth.GetFrozenCurveSegment(i_pos)

    def get_frozen_curve_segments_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFrozenCurveSegmentsSize
                | o Func GetFrozenCurveSegmentsSize(    ) As
                | 
                | Returns the number of frozen curve segments in the curve
                | smooth object.
                |
                | Parameters:
                | oSize
                |      Number of frozen curve segments in the curve smooth.

                | Examples:
                | This example retrieves the number of frozen curve segments.
                | in the hybShpCurveSmooth hybrid shape curve smooth. Dim
                | oSize As long oSize =
                | hybShpCurveSmooth.GetFrozenCurveSegmentsSize

        :return:
        """
        return self.hybrid_shape_curve_smooth.GetFrozenCurveSegmentsSize()

    def get_frozen_point(self, i_pos):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFrozenPoint
                | o Func GetFrozenPoint(        iPos) As
                | 
                | Retrieves the Frozen Point at specified position in the
                | hybrid shape curve smooth object.
                |
                | Parameters:
                | iPos
                | 		The position of the Frozen Point to retrieve.

                | Examples:
                | The following example gets the oPoint Frozen Point of the
                | hybShpCurveSmooth object at the position iPos. Dim oPoint As
                | Reference Set oPoint = hybShpCurveSmooth.GetFrozenPoint
                | (iPos).

        :param i_pos:
        :return:
        """
        return self.hybrid_shape_curve_smooth.GetFrozenPoint(i_pos)

    def get_frozen_points_size(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetFrozenPointsSize
                | o Func GetFrozenPointsSize(    ) As
                | 
                | Returns the number of Frozen Points in the curve smooth
                | object.
                |
                | Parameters:
                | oSize
                |      Number of Frozen Points in the curve smooth.

                | Examples:
                | This example retrieves the number of Frozen Points. in the
                | hybShpCurveSmooth hybrid shape curve smooth. Dim oSize As
                | long oSize = hybShpCurveSmooth.GetFrozenPointsSize

        :return:
        """
        return self.hybrid_shape_curve_smooth.GetFrozenPointsSize()

    def remove_all_frozen_curve_segments(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllFrozenCurveSegments
                | o Sub RemoveAllFrozenCurveSegments(    )
                | 
                | Removes all Frozen Curve Segment of the hybrid shape curve
                | smooth object.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_curve_smooth.RemoveAllFrozenCurveSegments()

    def remove_all_frozen_points(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveAllFrozenPoints
                | o Sub RemoveAllFrozenPoints(    )
                | 
                | Removes all Frozen Points of the hybrid shape curve smooth
                | object.
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_curve_smooth.RemoveAllFrozenPoints()

    def remove_frozen_curve_segment(self, i_curve):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveFrozenCurveSegment
                | o Sub RemoveFrozenCurveSegment(        iCurve)
                | 
                | Removes Frozen Curve Segment from the list of Forzen curves
                | in hybrid shape curve smooth object.
                |
                | Parameters:
                | iCurve
                | 		The Frozen Curve Segment to remove.

                | Examples:
                | The following example removes the Frozen Curve Segment from
                | the hybShpCurveSmooth object.
                | hybShpCurveSmooth.RemoveFrozenCurveSegment iCurve.

        :param i_curve:
        :return:
        """
        return self.hybrid_shape_curve_smooth.RemoveFrozenCurveSegment(i_curve)

    def remove_frozen_point(self, i_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | RemoveFrozenPoint
                | o Sub RemoveFrozenPoint(        iPoint)
                | 
                | Removes Frozen Point from the list of frozen points in
                | hybrid shape curve smooth object.
                |
                | Parameters:
                | iPoint
                | 		The Frozen Point to remove.

                | Examples:
                | The following example removes the Frozen Point from the
                | hybShpCurveSmooth object.
                | hybShpCurveSmooth.RemoveFrozenPoint iPoint.

        :param i_point:
        :return:
        """
        return self.hybrid_shape_curve_smooth.RemoveFrozenPoint(i_point)

    def set_maximum_deviation(self, i_max_deviation):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetMaximumDeviation
                | o Sub SetMaximumDeviation(        iMaxDeviation)
                | 
                | Sets the maximum deviation.
                |
                | Parameters:
                | iMaxDeviation
                |    The maximium deviation


        :param i_max_deviation:
        :return:
        """
        return self.hybrid_shape_curve_smooth.SetMaximumDeviation(i_max_deviation)

    def set_tangency_threshold(self, i_tangency_threshold):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTangencyThreshold
                | o Sub SetTangencyThreshold(        iTangencyThreshold)
                | 
                | Sets the tangency threshold.
                |
                | Parameters:
                | iTangencyThreshold
                |    The tangency threshold


        :param i_tangency_threshold:
        :return:
        """
        return self.hybrid_shape_curve_smooth.SetTangencyThreshold(i_tangency_threshold)

    def __repr__(self):
        return f'HybridShapeCurveSmooth()'
