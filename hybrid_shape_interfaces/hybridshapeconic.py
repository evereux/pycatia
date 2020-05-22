#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapeConic(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape conic object.Role: To access the data of
                | the hybrid shape conic object. This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_conic = com_object     

    @property
    def conic_parameter(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConicParameter
                | o Property ConicParameter(    ) As
                | 
                | Returns or sets the conic parameter. 
                |
                | Example:
                | This example
                | retrieves in conicParm the conic parameter of the conic
                | hybConic. Dim conicParm As double Set conicParm =
                | hybConic.ConicParameter

        :return:
        """
        return self.hybrid_shape_conic.ConicParameter

    @conic_parameter.setter
    def conic_parameter(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_conic.ConicParameter = value 

    @property
    def conic_user_tol(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | ConicUserTol
                | o Property ConicUserTol(    ) As   (Read Only)
                | 
                | Gets or sets the conic User Tolerance. 
                |
                | Example:
                | This example
                | retrieves in conicUserTol the conic user tolerance of the
                | conic HybridShapeConic. Dim oConicUserTol As CATIALength Set
                | oConicUserTol = HybridShapeConic.conicUserTol See also:

        :return:
        """
        return self.hybrid_shape_conic.ConicUserTol

    @property
    def end_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndPoint
                | o Property EndPoint(    ) As
                | 
                | Returns or sets the conic end point. Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example retrieves in
                | endPt the end point of the conic hybConic. Dim endPt As
                | Reference Set endPt = hybConic.EndPoint

        :return:
        """
        return self.hybrid_shape_conic.EndPoint

    @end_point.setter
    def end_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_conic.EndPoint = value 

    @property
    def end_tangent(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | EndTangent
                | o Property EndTangent(    ) As
                | 
                | Returns or sets the tangent direction at the conic end
                | point. 
                |
                | Example:
                | This example retrieves in endTgt the tangent
                | direction associated with the end point of the conic
                | hybConic. Dim endTgt As Reference Set endTgt =
                | hybConic.EndTangent

        :return:
        """
        return self.hybrid_shape_conic.EndTangent

    @end_tangent.setter
    def end_tangent(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_conic.EndTangent = value 

    @property
    def start_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartPoint
                | o Property StartPoint(    ) As
                | 
                | Returns or sets the conic start point. Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example sets startPt
                | as the start point of the conic hybConic. Dim startPt As
                | Reference ... ' Value startPt hybConic.StartPoint startPt

        :return:
        """
        return self.hybrid_shape_conic.StartPoint

    @start_point.setter
    def start_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_conic.StartPoint = value 

    @property
    def start_tangent(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | StartTangent
                | o Property StartTangent(    ) As
                | 
                | Returns or sets the tangent direction at the conic start
                | point. 
                |
                | Example:
                | This example sets startTgt as the tangent
                | direction at the start point of the conic hybConic. Dim
                | startTgt As Reference ... ' Value startTangent
                | hybConic.StartTangent startTgt

        :return:
        """
        return self.hybrid_shape_conic.StartTangent

    @start_tangent.setter
    def start_tangent(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_conic.StartTangent = value 

    @property
    def support_plane(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SupportPlane
                | o Property SupportPlane(    ) As
                | 
                | Returns or sets the conic supporting plane. Sub-element(s)
                | supported (see object): . 
                |
                | Example:
                | This example retrieves in
                | supportPln the supporting plane of the conic hybConic. Dim
                | supportPln As Reference Set supportPln =
                | hybConic.SupportPlane

        :return:
        """
        return self.hybrid_shape_conic.SupportPlane

    @support_plane.setter
    def support_plane(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_conic.SupportPlane = value 

    @property
    def tangent_int_point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | TangentIntPoint
                | o Property TangentIntPoint(    ) As
                | 
                | Returns or sets the conic tangent intersection point. Sub-
                | element(s) supported (see object): . 
                |
                | Example:
                | This example
                | retrieves in tgtIntPt the tangent intersection point of the
                | conic hybConic. Dim tgtIntPt As Reference Set tgtIntPt =
                | hybConic.TangentIntPoint

        :return:
        """
        return self.hybrid_shape_conic.TangentIntPoint

    @tangent_int_point.setter
    def tangent_int_point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_conic.TangentIntPoint = value 

    def get_end_tangent_direction_flag(self, o_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetEndTangentDirectionFlag
                | o Sub GetEndTangentDirectionFlag(        oOrientation)
                | 
                | Retrieves the tangent direction orientation at the conic end
                | point.
                |
                | Parameters:
                | oOrientation
                |    The direction orientation applied to the tangent direction at the conic end point
                |    Legal values: 1 if the tangent direction is used as is, and -1 if it
                |    is inverted

                | Examples:
                | This example retrieves the direction orientation of the
                | tangent at the end point of the conic hybConic. Dim
                | endPtTgtOrient As long hybConic.GetEndTangentDirectionFlag
                | endPtTgtOrient

        :param o_orientation:
        :return:
        """
        return self.hybrid_shape_conic.GetEndTangentDirectionFlag(o_orientation)

    def get_intermed_tangent(self, i_index_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetIntermedTangent
                | o Func GetIntermedTangent(        iIndexPoint) As
                | 
                | Retrieves the tangent direction at one of the conic
                | intermediate passing points.
                |
                | Parameters:
                | iIndexPoint
                |    An index that designates the passing point to retrieve
                |    Legal values: 1 for the first passing point, and 2 for the second one
                |  
                |  oTgtDir
                |    The retrieved tangent direction at the given passing point

                | Examples:
                | This example retrieves in tgtDir the tangent direction at
                | point passingPtIdx through which the conic hybConic passes.
                | Dim tgtDir As Reference passingPtIdx = 1 Set tgtDir =
                | hybConic.GetIntermedTangent (passingPtIdx)

        :param i_index_point:
        :return:
        """
        return self.hybrid_shape_conic.GetIntermedTangent(i_index_point)

    def get_intermediate_point(self, i_index_point, o_end_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetIntermediatePoint
                | o Sub GetIntermediatePoint(        iIndexPoint,
                |                                    oEndPoint)
                | 
                | Retrieves one of the conic intermediate passing points.
                |
                | Parameters:
                | iIndexPoint
                |    An index that designates the passing point to retrieve
                |    Legal values: 1 for the first passing point, 2 for the second one, and 3 for the third one 
                |  
                |  oEndPoint
                |    The retrieved passing point

                | Examples:
                | This example retrieves in passingPt the second point through
                | which the conic hybConic passes. Dim passingPt As Reference
                | passingPtIdx = 2 hybConic.GetIntermediatePoint passingPtIdx,
                | passingPt

        :param i_index_point:
        :param o_end_point:
        :return:
        """
        return self.hybrid_shape_conic.GetIntermediatePoint(i_index_point, o_end_point)

    def get_intermediate_tangent_direction_flag(self, i_index_point, o_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetIntermediateTangentDirectionFlag
                | o Sub GetIntermediateTangentDirectionFlag(        iIndexPoint,
                |                                                   oOrientation)
                | 
                | Retrieves the tangent direction orientation of one of the
                | conic intermediate points.
                |
                | Parameters:
                | iIndexPoint
                |    An index that designates the passing point to retrieve
                |    Legal values: 1 for the first passing point, and 2 for the second one
                |  
                |  oOrientation
                |    The direction orientation applied to the tangent direction at the intermediate passing point
                |    Legal values: 1 if the tangent direction is used as is, and -1 if it
                |    is inverted

                | Examples:
                | This example retrieves the direction orientation of the
                | tangent at the first point through which the conic hybConic
                | passes. passingPtIdx = 1 Dim passingPtTgtOrient As long
                | hybConic.GetIntermediateTangentDirectionFlag passingPtIdx,
                | passingPtTgtOrient

        :param i_index_point:
        :param o_orientation:
        :return:
        """
        return self.hybrid_shape_conic.GetIntermediateTangentDirectionFlag(i_index_point, o_orientation)

    def get_start_tangent_direction_flag(self, o_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | GetStartTangentDirectionFlag
                | o Sub GetStartTangentDirectionFlag(        oOrientation)
                | 
                | Retrieves the tangent direction orientation at the conic
                | start point.
                |
                | Parameters:
                | oOrientation
                |    The direction orientation applied to the tangent direction at the conic start point
                |    Legal values: 1 if the tangent direction is used as is, and -1 if it
                |    is inverted

                | Examples:
                | This example retrieves the direction orientation of the
                | tangent at the start point of the conic hybConic. Dim
                | startPtTgtOrient As long
                | hybConic.GetStartTangentDirectionFlag startPtTgtOrient

        :param o_orientation:
        :return:
        """
        return self.hybrid_shape_conic.GetStartTangentDirectionFlag(o_orientation)

    def set_end_tangent_direction_flag(self, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetEndTangentDirectionFlag
                | o Sub SetEndTangentDirectionFlag(        iOrientation)
                | 
                | Sets the tangent direction orientation at the conic end
                | point.
                |
                | Parameters:
                | iOrientation
                |    The direction orientation to be applied to the tangent direction at the conic end point
                |    Legal values: 1 if the tangent direction is to be used as is, and -1 if it
                |    must be inverted

                | Examples:
                | This example sets the direction orientation of the tangent
                | at the end point of the conic hybConic to the one of the
                | direction used for the tangent. endPtTgtOrient = 1
                | hybConic.SetEndTangentDirectionFlag endPtTgtOrient

        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_conic.SetEndTangentDirectionFlag(i_orientation)

    def set_intermediate_point(self, i_index_point, i_end_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetIntermediatePoint
                | o Sub SetIntermediatePoint(        iIndexPoint,
                |                                    iEndPoint)
                | 
                | Sets one of the conic intermediate passing points.
                |
                | Parameters:
                | iIndexPoint
                |    An index that designates the passing point to retrieve
                |    Legal values: 1 for the first passing point, 2 for the second one, and 3 for the third one 
                |  
                |  iEndPoint
                |    The passing point to set.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | .

                | Examples:
                | This example sets passingPt as the first point through which
                | the conic hybConic must pass. Dim passingPt As Reference ...
                | ' Value passingPt passingPtIdx = 1
                | hybConic.SetIntermediatePoint passingPtIdx, passingPt

        :param i_index_point:
        :param i_end_point:
        :return:
        """
        return self.hybrid_shape_conic.SetIntermediatePoint(i_index_point, i_end_point)

    def set_intermediate_tangent(self, i_index_point, i_tgt_dir):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetIntermediateTangent
                | o Sub SetIntermediateTangent(        iIndexPoint,
                |                                      iTgtDir)
                | 
                | Sets the tangent direction at one of the conic intermediate
                | passing points.
                |
                | Parameters:
                | iIndexPoint
                |    An index that designates the passing point where the tangent direction is to be set
                |    Legal values: 1 for the first passing point, and 2 for the second one
                |  
                |  iTgtDir
                |    The direction to set as the tangent direction at the given passing point

                | Examples:
                | This example sets tgtDir as the tangent direction at the
                | first point through which the conic hybConic passes. Dim
                | tgtDir As Reference ... ' Value tgtDir passingPtIdx = 1
                | hybConic.SetIntermediateTangent passingPtIdx, tgtDir

        :param i_index_point:
        :param i_tgt_dir:
        :return:
        """
        return self.hybrid_shape_conic.SetIntermediateTangent(i_index_point, i_tgt_dir)

    def set_intermediate_tangent_direction_flag(self, i_index_point, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetIntermediateTangentDirectionFlag
                | o Sub SetIntermediateTangentDirectionFlag(        iIndexPoint,
                |                                                   iOrientation)
                | 
                | Sets the tangent direction orientation of one of the conic
                | intermediate points.
                |
                | Parameters:
                | iIndexPoint
                |    An index that designates the passing point to retrieve
                |    Legal values: 1 for the first passing point, and 2 for the second one
                |  
                |  iOrientation
                |    The direction orientation to be applied to the tangent direction at the intermediate passing point
                |    Legal values: 1 if the tangent direction is to be used as is, and -1 if it
                |    must be inverted

                | Examples:
                | This example sets the direction orientation of the tangent
                | at the first point through which the conic hybConic passes
                | to the inverse of the one of the direction used for the
                | tangent. passingPtIdx = 1 passingPtTgtOrient = -1
                | hybConic.SetIntermediateTangentDirectionFlag passingPtIdx,
                | passingPtTgtOrient

        :param i_index_point:
        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_conic.SetIntermediateTangentDirectionFlag(i_index_point, i_orientation)

    def set_start_and_end_tangents_plus_conic_parameter(self, i_start_tgt, i_end_tgt, i_conic_param):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetStartAndEndTangentsPlusConicParameter
                | o Sub SetStartAndEndTangentsPlusConicParameter(        iStartTgt,
                |                                                        iEndTgt,
                |                                                        iConicParam)
                | 
                | Sets the tangent directions at conic start and end points,
                | and the conic parameter.
                |
                | Parameters:
                | iStartTgt
                |    The tangent direction at the start point
                |  
                |  iEndTgt
                |    The tangent direction at the end point
                |  
                |  iConicParam
                |    The conic parameter
                |    Legal values: p = 0.5 (parabola), 0<=p<=0.5 (ellipse), 0.5<= p <=1.0 (hyperbola)

                | Examples:
                | This example sets firstDir and secondDir as the tangent
                | directions at the start and end points of the conic
                | hybConic, and conicParm as the conic parameter.
                | hybConic.SetStartAndEndTangentsPlusConicParameter firstDir,
                | secondDir, conicParm

        :param i_start_tgt:
        :param i_end_tgt:
        :param i_conic_param:
        :return:
        """
        return self.hybrid_shape_conic.SetStartAndEndTangentsPlusConicParameter(i_start_tgt, i_end_tgt, i_conic_param)

    def set_start_and_end_tangents_plus_passing_point(self, i_start_tgt, i_end_tgt, i_passing_pt):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetStartAndEndTangentsPlusPassingPoint
                | o Sub SetStartAndEndTangentsPlusPassingPoint(        iStartTgt,
                |                                                      iEndTgt,
                |                                                      iPassingPt)
                | 
                | Sets the tangent directions at conic start and end points,
                | and a passing point.
                |
                | Parameters:
                | iStartTgt
                |    The tangent direction at the start point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | . 
                |      iEndTgt
                |    The tangent direction at the end point
                |  
                |  iPassingPt
                |    A point through which the conic must pass.
                |    Legal values: This point must differ from the start and end points.

                | Examples:
                | This example sets firstDir and secondDir as the tangent
                | directions at the start and end points of the conic
                | hybConic, and passingPoint as a point through which the
                | conic must pass.
                | hybConic.SetStartAndEndTangentsPlusPassingPoint firstDir,
                | secondDir, passingPoint

        :param i_start_tgt:
        :param i_end_tgt:
        :param i_passing_pt:
        :return:
        """
        return self.hybrid_shape_conic.SetStartAndEndTangentsPlusPassingPoint(i_start_tgt, i_end_tgt, i_passing_pt)

    def set_start_tangent_direction_flag(self, i_orientation):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetStartTangentDirectionFlag
                | o Sub SetStartTangentDirectionFlag(        iOrientation)
                | 
                | Sets the tangent direction orientation at the conic start
                | point.
                |
                | Parameters:
                | iOrientation
                |    The direction orientation to be applied to the tangent direction at the conic start point
                |    Legal values: 1 if the tangent direction is to be used as is, and -1 if it
                |    must be inverted

                | Examples:
                | This example sets the direction orientation of the tangent
                | at the start point of the conic hybConic to the inverse of
                | the one of the direction used for the tangent.
                | startPtTgtOrient = -1 hybConic.SetStartTangentDirectionFlag
                | startPtTgtOrient

        :param i_orientation:
        :return:
        """
        return self.hybrid_shape_conic.SetStartTangentDirectionFlag(i_orientation)

    def set_tangent_intersect_point_plus_conic_parm(self, i_tgt_int, i_conic_param):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTangentIntersectPointPlusConicParm
                | o Sub SetTangentIntersectPointPlusConicParm(        iTgtInt,
                |                                                     iConicParam)
                | 
                | Sets the intersection point of the conic tangents to the
                | start and end points, and the conic parameter.
                |
                | Parameters:
                | iTgtInt
                |    The point intersection of the conic tangents to the start and end point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | .  
                |      iConicParam
                |    The conic parameter
                |    Legal values: p = 0.5 (parabola), 0<=p<=0.5 (ellipse), 0.5<= p <=1.0 (hyperbola)

                | Examples:
                | This example sets tgtIntPoint as the intersection point of
                | the tangents to the start and end points of the conic
                | hybConic, and conicParm as the conic parameter.
                | hybConic.SetTangentIntersectPointPlusConicParm tgtIntPoint,
                | conicParm

        :param i_tgt_int:
        :param i_conic_param:
        :return:
        """
        return self.hybrid_shape_conic.SetTangentIntersectPointPlusConicParm(i_tgt_int, i_conic_param)

    def set_tangent_intersect_point_plus_passing_point(self, i_tgt_int, i_passing_pt):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTangentIntersectPointPlusPassingPoint
                | o Sub SetTangentIntersectPointPlusPassingPoint(        iTgtInt,
                |                                                        iPassingPt)
                | 
                | Sets the intersection point of the conic tangents to the
                | start and end points, and a passing point.
                |
                | Parameters:
                | iTgtInt
                |    The point intersection of the conic tangents to the start and end point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | . 
                |      iPassingPt
                |    A point through which the conic must pass.
                |    Legal values: This point must differ from the start and end points.
                |  Sub-element(s) supported (see 
                |  object):  
                | .

                | Examples:
                | This example sets tgtIntPoint as the intersection point of
                | the tangents to the start and end points of the conic
                | hybConic, and passingPoint as a point through which the
                | conic must pass.
                | hybConic.SetTangentIntersectPointPlusPassingPoint
                | tgtIntPoint, passingPoint

        :param i_tgt_int:
        :param i_passing_pt:
        :return:
        """
        return self.hybrid_shape_conic.SetTangentIntersectPointPlusPassingPoint(i_tgt_int, i_passing_pt)

    def set_three_intermediate_passing_points(self, i_pass_pt_1, i_pass_pt_2, i_pass_pt_3):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetThreeIntermediatePassingPoints
                | o Sub SetThreeIntermediatePassingPoints(        iPassPt1,
                |                                                 iPassPt2,
                |                                                 iPassPt3)
                | 
                | Sets three conic intermediate passing points.
                |
                | Parameters:
                | iPassPt1
                |    The first intermediate passing point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | . 
                |      iPassPt2
                |    The second intermediate passing point.
                |  Sub-element(s) supported (see 
                |  object):  
                | . 
                |      iPassPt3
                |    The third intermediate passing point.
                |  Sub-element(s) supported (see 
                |  object):  
                | .

                | Examples:
                | This example sets passingPoint1, passingPoint2, and
                | passingPoint3 as the three intermediate points through which
                | the conic hybConic must pass.
                | hybConic.SetThreeIntermediatePassingPoints passingPoint1,
                | passingPoint2, passingPoint3

        :param i_pass_pt_1:
        :param i_pass_pt_2:
        :param i_pass_pt_3:
        :return:
        """
        return self.hybrid_shape_conic.SetThreeIntermediatePassingPoints(i_pass_pt_1, i_pass_pt_2, i_pass_pt_3)

    def set_two_intermediate_passing_points_plus_one_tangent(self, i_pass_pt_1, i_pass_pt_2, i_tgt_dir, i_index_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | SetTwoIntermediatePassingPointsPlusOneTangent
                | o Sub SetTwoIntermediatePassingPointsPlusOneTangent(        iPassPt1,
                |                                                             iPassPt2,
                |                                                             iTgtDir,
                |                                                             iIndexPoint)
                | 
                | Sets two conic intermediate passing points and a tangent at
                | one of the passing points.
                |
                | Parameters:
                | iPassPt1
                |    The first intermediate passing point.
                |  Sub-element(s) supported (see 
                | 
                |  object):  
                | .  
                |      iPassPt2
                |    The second intermediate passing point.
                |  Sub-element(s) supported (see 
                |  object):  
                | . 
                |      iTgtDir
                |    The tangent direction at one of the intermediate passing points
                |  
                |  iIndexPoint
                |    An index indicating the passing point to which the tangent direction applies
                |    Legal values: 1 for the first passing point, and 2 for the second one

                | Examples:
                | This example sets passingPoint1 and passingPoint2 as two
                | intermediate points through which the conic hybConic must
                | pass, tgtDir as the tangent direction at the passing point
                | designated by passingPointIdx.
                | hybConic.SetTwoIntermediatePassingPointsPlusOneTangent
                | passingPoint1, passingPoint2, tgtDir, passingPointIdx

        :param i_pass_pt_1:
        :param i_pass_pt_2:
        :param i_tgt_dir:
        :param i_index_point:
        :return:
        """
        return self.hybrid_shape_conic.SetTwoIntermediatePassingPointsPlusOneTangent(i_pass_pt_1, i_pass_pt_2, i_tgt_dir, i_index_point)

    def switch_end_tangent_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SwitchEndTangentDirection
                | o Sub SwitchEndTangentDirection(    )
                | 
                | Inverts the tangent direction orientation at the conic end
                | point. 
                |
                | Example:
                | This example inverts the direction
                | orientation of the tangent at the end point of the conic
                | hybConic. hybConic.SwitchEndTangentDirection
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_conic.SwitchEndTangentDirection()

    def switch_intermediate_tangent_direction(self, i_index_point):
        """
        .. note::
            CAA V5 Visual Basic help

                | SwitchIntermediateTangentDirection
                | o Sub SwitchIntermediateTangentDirection(        iIndexPoint)
                | 
                | Inverts the tangent direction orientation of one of the
                | conic intermediate points.
                |
                | Parameters:
                | iIndexPoint
                |    An index that designates the passing point where the tangent direction is to be inverted
                |    Legal values: 1 for the first passing point, and 2 for the second one

                | Examples:
                | This example inverts the direction orientation of the
                | tangent at the first point through which the conic hybConic
                | passes. passingPtIdx = 1
                | hybConic.SwitchIntermediateTangentDirection passingPtIdx

        :param i_index_point:
        :return:
        """
        return self.hybrid_shape_conic.SwitchIntermediateTangentDirection(i_index_point)

    def switch_start_tangent_direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | SwitchStartTangentDirection
                | o Sub SwitchStartTangentDirection(    )
                | 
                | Inverts the tangent direction orientation at the conic start
                | point. 
                |
                | Example:
                | This example inverts the direction
                | orientation of the tangent at the start point of the conic
                | hybConic. hybConic.SwitchStartTangentDirection
                |
                | Parameters:


        :return:
        """
        return self.hybrid_shape_conic.SwitchStartTangentDirection()

    def __repr__(self):
        return f'HybridShapeConic()'
