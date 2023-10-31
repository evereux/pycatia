#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeConic(HybridShape):
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
                |                         HybridShapeConic
                | 
                | Represents the hybrid shape conic object.
                | Role: To access the data of the hybrid shape conic object. This data
                | includes:
                | 
                |     The start point and its associated tangent contraint
                |     The end point and its associated tangent contraint
                |     The supporting plane
                |     The tangent intersection point
                |     The conic parameter: p = 0.5 (parabola), 0<=p<=0.5 (ellipse), 0.5<= p <=1.0 (hyperbola)
                | 
                | Use the HybridShapeFactory to create a HybridShapeConic
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_conic = com_object

    @property
    def conic_parameter(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ConicParameter() As double
                | 
                |     Returns or sets the conic parameter.
                | 
                |     Example:
                |         This example retrieves in conicParm the conic parameter of the conic
                |         hybConic.
                | 
                |          Dim conicParm As double 
                |          Set conicParm = hybConic.ConicParameter

        :rtype: float
        """

        return self.hybrid_shape_conic.ConicParameter

    @conic_parameter.setter
    def conic_parameter(self, value: float):
        """
        :param float value:
        """

        self.hybrid_shape_conic.ConicParameter = value

    @property
    def conic_user_tol(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ConicUserTol() As Length (Read Only)
                | 
                |     Gets or sets the conic User Tolerance.
                | 
                |     Example:
                |         This example retrieves in conicUserTol the conic user tolerance of the
                |         conic HybridShapeConic.
                | 
                |          Dim oConicUserTol As  CATIALength 
                |          Set oConicUserTol = HybridShapeConic.conicUserTol
                |          
                | 
                |     See also:
                |         Length

        :rtype: Length
        """

        return Length(self.hybrid_shape_conic.ConicUserTol)

    @property
    def end_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndPoint() As Reference
                | 
                |     Returns or sets the conic end point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in endPt the end point of the conic
                |         hybConic.
                | 
                |          Dim endPt As Reference 
                |          Set endPt = hybConic.EndPoint

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_conic.EndPoint)

    @end_point.setter
    def end_point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_conic.EndPoint = reference_point.com_object

    @property
    def end_tangent(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property EndTangent() As HybridShapeDirection
                | 
                |     Returns or sets the tangent direction at the conic end
                |     point.
                | 
                |     Example:
                |         This example retrieves in endTgt the tangent direction associated with
                |         the end point of the conic hybConic.
                | 
                |          Dim endTgt As Reference 
                |          Set endTgt = hybConic.EndTangent

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_conic.EndTangent)

    @end_tangent.setter
    def end_tangent(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_conic.EndTangent = direction.com_object

    @property
    def start_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StartPoint() As Reference
                | 
                |     Returns or sets the conic start point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example sets startPt as the start point of the conic
                |         hybConic.
                | 
                |          Dim startPt As Reference
                |          ... ' Value startPt
                |          hybConic.StartPoint startPt

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_conic.StartPoint)

    @start_point.setter
    def start_point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_conic.StartPoint = reference_point

    @property
    def start_tangent(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property StartTangent() As HybridShapeDirection
                | 
                |     Returns or sets the tangent direction at the conic start
                |     point.
                | 
                |     Example:
                |         This example sets startTgt as the tangent direction at the start point
                |         of the conic hybConic.
                | 
                |          Dim startTgt As Reference
                |          ... ' Value startTangent
                |          hybConic.StartTangent startTgt

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_conic.StartTangent)

    @start_tangent.setter
    def start_tangent(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_conic.StartTangent = direction

    @property
    def support_plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SupportPlane() As Reference
                | 
                |     Returns or sets the conic supporting plane.
                |     Sub-element(s) supported (see Boundary object):
                |     PlanarFace.
                | 
                |     Example:
                |         This example retrieves in supportPln the supporting plane of the conic
                |         hybConic.
                | 
                |          Dim supportPln As Reference 
                |          Set supportPln = hybConic.SupportPlane

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_conic.SupportPlane)

    @support_plane.setter
    def support_plane(self, reference_plane: Reference):
        """
        :param Reference reference_plane:
        """

        self.hybrid_shape_conic.SupportPlane = reference_plane.com_object

    @property
    def tangent_int_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TangentIntPoint() As Reference
                | 
                |     Returns or sets the conic tangent intersection point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in tgtIntPt the tangent intersection point of
                |         the conic hybConic.
                | 
                |          Dim tgtIntPt As Reference 
                |          Set tgtIntPt = hybConic.TangentIntPoint

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_conic.TangentIntPoint)

    @tangent_int_point.setter
    def tangent_int_point(self, reference_tangent_point: Reference):
        """
        :param Reference reference_tangent_point:
        """

        self.hybrid_shape_conic.TangentIntPoint = reference_tangent_point

    def get_end_tangent_direction_flag(self, o_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetEndTangentDirectionFlag(long oOrientation)
                | 
                |     Retrieves the tangent direction orientation at the conic end
                |     point.
                | 
                |     Parameters:
                | 
                |         oOrientation
                |             The direction orientation applied to the tangent direction at the
                |             conic end point
                |             Legal values: 1 if the tangent direction is used as is, and -1 if
                |             it is inverted 
                | 
                |     Example:
                | 
                |           This example retrieves the direction orientation of the tangent at
                |           the end point of
                |          the conic hybConic.
                |          
                | 
                |          Dim endPtTgtOrient As long
                |          hybConic.GetEndTangentDirectionFlag endPtTgtOrient

        :param int o_orientation:
        :rtype: None
        """
        return self.hybrid_shape_conic.GetEndTangentDirectionFlag(o_orientation)

    def get_intermed_tangent(self, i_index_point: int) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetIntermedTangent(long iIndexPoint) As
                | HybridShapeDirection
                | 
                |     Retrieves the tangent direction at one of the conic intermediate passing
                |     points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point to
                |             retrieve
                |             Legal values: 1 for the first passing point, and 2 for the second
                |             one 
                |         oTgtDir
                |             The retrieved tangent direction at the given passing point
                |             
                | 
                |     Example:
                | 
                |           This example retrieves in tgtDir the tangent direction at point
                |           passingPtIdx 
                |          through which the conic hybConic passes.
                |          
                | 
                |          Dim tgtDir As Reference
                |          passingPtIdx = 1
                |          Set tgtDir = hybConic.GetIntermedTangent (passingPtIdx)

        :param int i_index_point:
        :rtype: HybridShapeDirection
        """
        return HybridShapeDirection(self.hybrid_shape_conic.GetIntermedTangent(i_index_point))

    def get_intermediate_point(self, i_index_point: int, o_end_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetIntermediatePoint(long iIndexPoint,
                | Reference oEndPoint)
                | 
                |     Retrieves one of the conic intermediate passing points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point to
                |             retrieve
                |             Legal values: 1 for the first passing point, 2 for the second one,
                |             and 3 for the third one 
                |         oEndPoint
                |             The retrieved passing point 
                | 
                |     Example:
                | 
                |           This example retrieves in passingPt the second point through
                |           which
                |          the conic hybConic passes.
                |          
                | 
                |          Dim passingPt As Reference
                |          passingPtIdx = 2
                |          hybConic.GetIntermediatePoint passingPtIdx, passingPt

        :param int i_index_point:
        :param Reference o_end_point:
        :rtype: None
        """
        return self.hybrid_shape_conic.GetIntermediatePoint(i_index_point, o_end_point.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_intermediate_point'
        # # vba_code = """
        # # Public Function get_intermediate_point(hybrid_shape_conic)
        # #     Dim iIndexPoint (2)
        # #     hybrid_shape_conic.GetIntermediatePoint iIndexPoint
        # #     get_intermediate_point = iIndexPoint
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_intermediate_tangent_direction_flag(self, i_index_point: int, o_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetIntermediateTangentDirectionFlag(long iIndexPoint,
                | long oOrientation)
                | 
                |     Retrieves the tangent direction orientation of one of the conic
                |     intermediate points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point to
                |             retrieve
                |             Legal values: 1 for the first passing point, and 2 for the second
                |             one 
                |         oOrientation
                |             The direction orientation applied to the tangent direction at the
                |             intermediate passing point
                |             Legal values: 1 if the tangent direction is used as is, and -1 if
                |             it is inverted 
                | 
                |     Example:
                | 
                |           This example retrieves the direction orientation of the tangent at
                |           the first point through which
                |          the conic hybConic passes.
                |          
                | 
                |          passingPtIdx = 1
                |          Dim passingPtTgtOrient As long
                |          hybConic.GetIntermediateTangentDirectionFlag passingPtIdx,
                |          passingPtTgtOrient

        :param int i_index_point:
        :param int o_orientation:
        :rtype: None
        """
        return self.hybrid_shape_conic.GetIntermediateTangentDirectionFlag(i_index_point, o_orientation)

    def get_start_tangent_direction_flag(self, o_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetStartTangentDirectionFlag(long oOrientation)
                | 
                |     Retrieves the tangent direction orientation at the conic start
                |     point.
                | 
                |     Parameters:
                | 
                |         oOrientation
                |             The direction orientation applied to the tangent direction at the
                |             conic start point
                |             Legal values: 1 if the tangent direction is used as is, and -1 if
                |             it is inverted 
                | 
                |     Example:
                | 
                |           This example retrieves the direction orientation of the tangent at
                |           the start point of
                |          the conic hybConic.
                |          
                | 
                |          Dim startPtTgtOrient As long
                |          hybConic.GetStartTangentDirectionFlag
                |          startPtTgtOrient

        :param int o_orientation:
        :rtype: None
        """
        return self.hybrid_shape_conic.GetStartTangentDirectionFlag(o_orientation)

    def set_end_tangent_direction_flag(self, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetEndTangentDirectionFlag(long iOrientation)
                | 
                |     Sets the tangent direction orientation at the conic end
                |     point.
                | 
                |     Parameters:
                | 
                |         iOrientation
                |             The direction orientation to be applied to the tangent direction at
                |             the conic end point
                |             Legal values: 1 if the tangent direction is to be used as is, and
                |             -1 if it must be inverted 
                | 
                |     Example:
                | 
                |           This example sets the direction orientation of the tangent at the end
                |           point of
                |          the conic hybConic to the one of the direction used
                |          for
                |          the tangent.
                |          
                | 
                |          endPtTgtOrient = 1
                |          hybConic.SetEndTangentDirectionFlag endPtTgtOrient

        :param int i_orientation:
        :rtype: None
        """
        return self.hybrid_shape_conic.SetEndTangentDirectionFlag(i_orientation)

    def set_intermediate_point(self, i_index_point: int, i_end_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetIntermediatePoint(long iIndexPoint,
                | Reference iEndPoint)
                | 
                |     Sets one of the conic intermediate passing points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point to
                |             retrieve
                |             Legal values: 1 for the first passing point, 2 for the second one,
                |             and 3 for the third one 
                |         iEndPoint
                |             The passing point to set.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex. 
                |     Example:
                | 
                |           This example sets passingPt as the first point through
                |           which
                |          the conic hybConic must pass.
                |          
                | 
                |          Dim passingPt As Reference
                |          ... ' Value passingPt
                |          passingPtIdx = 1
                |          hybConic.SetIntermediatePoint passingPtIdx, passingPt

        :param int i_index_point:
        :param Reference i_end_point:
        :rtype: None
        """
        return self.hybrid_shape_conic.SetIntermediatePoint(i_index_point, i_end_point.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_intermediate_point'
        # # vba_code = """
        # # Public Function set_intermediate_point(hybrid_shape_conic)
        # #     Dim iIndexPoint (2)
        # #     hybrid_shape_conic.SetIntermediatePoint iIndexPoint
        # #     set_intermediate_point = iIndexPoint
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_intermediate_tangent(self, i_index_point: int, i_tgt_dir: HybridShapeDirection) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetIntermediateTangent(long iIndexPoint,
                | HybridShapeDirection iTgtDir)
                | 
                |     Sets the tangent direction at one of the conic intermediate passing
                |     points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point where the tangent
                |             direction is to be set
                |             Legal values: 1 for the first passing point, and 2 for the second
                |             one 
                |         iTgtDir
                |             The direction to set as the tangent direction at the given passing
                |             point 
                | 
                |     Example:
                | 
                |           This example sets tgtDir as the tangent direction at the first point
                |           through which
                |          the conic hybConic passes.
                |          
                | 
                |          Dim tgtDir As Reference
                |          ... ' Value tgtDir
                |          passingPtIdx = 1
                |          hybConic.SetIntermediateTangent passingPtIdx, tgtDir

        :param int i_index_point:
        :param HybridShapeDirection i_tgt_dir:
        :rtype: None
        """
        return self.hybrid_shape_conic.SetIntermediateTangent(i_index_point, i_tgt_dir.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_intermediate_tangent'
        # # vba_code = """
        # # Public Function set_intermediate_tangent(hybrid_shape_conic)
        # #     Dim iIndexPoint (2)
        # #     hybrid_shape_conic.SetIntermediateTangent iIndexPoint
        # #     set_intermediate_tangent = iIndexPoint
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_intermediate_tangent_direction_flag(self, i_index_point: int, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetIntermediateTangentDirectionFlag(long iIndexPoint,
                | long iOrientation)
                | 
                |     Sets the tangent direction orientation of one of the conic intermediate
                |     points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point to
                |             retrieve
                |             Legal values: 1 for the first passing point, and 2 for the second
                |             one 
                |         iOrientation
                |             The direction orientation to be applied to the tangent direction at
                |             the intermediate passing point
                |             Legal values: 1 if the tangent direction is to be used as is, and
                |             -1 if it must be inverted 
                | 
                |     Example:
                | 
                |           This example sets the direction orientation of the tangent at the
                |           first point through which
                |          the conic hybConic passes to the inverse of the one of the direction
                |          used for
                |          the tangent.
                |          
                | 
                |          passingPtIdx = 1
                |          passingPtTgtOrient = -1
                |          hybConic.SetIntermediateTangentDirectionFlag passingPtIdx,
                |          passingPtTgtOrient

        :param int i_index_point:
        :param int i_orientation:
        :rtype: None
        """
        return self.hybrid_shape_conic.SetIntermediateTangentDirectionFlag(i_index_point, i_orientation)

    def set_start_and_end_tangents_plus_conic_parameter(self, i_start_tgt: HybridShapeDirection,
                                                        i_end_tgt: HybridShapeDirection, i_conic_param: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetStartAndEndTangentsPlusConicParameter(HybridShapeDirection
                | iStartTgt,
                | HybridShapeDirection iEndTgt,
                | double iConicParam)
                | 
                |     Sets the tangent directions at conic start and end points, and the conic
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iStartTgt
                |             The tangent direction at the start point 
                |         iEndTgt
                |             The tangent direction at the end point 
                |         iConicParam
                |             The conic parameter
                |             Legal values: p = 0.5 (parabola), 0<=p<=0.5 (ellipse), 0.5<= p <=1.0 (hyperbola) 
                | 
                |     Example:
                | 
                |           This example sets firstDir and secondDir as the tangent directions at
                |           the start
                |          and end points of the conic hybConic, and conicParm as the conic
                |          parameter.
                |          
                | 
                |          hybConic.SetStartAndEndTangentsPlusConicParameter firstDir, secondDir,
                |          conicParm

        :param HybridShapeDirection i_start_tgt:
        :param HybridShapeDirection i_end_tgt:
        :param float i_conic_param:
        :rtype: None
        """
        return self.hybrid_shape_conic.SetStartAndEndTangentsPlusConicParameter(i_start_tgt.com_object,
                                                                                i_end_tgt.com_object, i_conic_param)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_start_and_end_tangents_plus_conic_parameter'
        # # vba_code = """
        # # Public Function set_start_and_end_tangents_plus_conic_parameter(hybrid_shape_conic)
        # #     Dim iStartTgt (2)
        # #     hybrid_shape_conic.SetStartAndEndTangentsPlusConicParameter iStartTgt
        # #     set_start_and_end_tangents_plus_conic_parameter = iStartTgt
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_start_and_end_tangents_plus_passing_point(self, i_start_tgt: HybridShapeDirection,
                                                      i_end_tgt: HybridShapeDirection, i_passing_pt: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetStartAndEndTangentsPlusPassingPoint(HybridShapeDirection
                | iStartTgt,
                | HybridShapeDirection iEndTgt,
                | Reference iPassingPt)
                | 
                |     Sets the tangent directions at conic start and end points, and a passing
                |     point.
                | 
                |     Parameters:
                | 
                |         iStartTgt
                |             The tangent direction at the start point.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex. 
                |     iEndTgt
                |         The tangent direction at the end point 
                |     iPassingPt
                |         A point through which the conic must pass.
                |         Legal values: This point must differ from the start and end points.
                |         
                |     Example:
                | 
                |           This example sets firstDir and secondDir as the tangent directions at
                |           the start
                |          and end points of the conic hybConic, and passingPoint as a point
                |          through
                |          which the conic must pass.
                |          
                | 
                |          hybConic.SetStartAndEndTangentsPlusPassingPoint firstDir, secondDir,
                |          passingPoint

        :param HybridShapeDirection i_start_tgt:
        :param HybridShapeDirection i_end_tgt:
        :param Reference i_passing_pt:
        :rtype: None
        """
        return self.hybrid_shape_conic.SetStartAndEndTangentsPlusPassingPoint(i_start_tgt.com_object,
                                                                              i_end_tgt.com_object,
                                                                              i_passing_pt.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_start_and_end_tangents_plus_passing_point'
        # # vba_code = """
        # # Public Function set_start_and_end_tangents_plus_passing_point(hybrid_shape_conic)
        # #     Dim iStartTgt (2)
        # #     hybrid_shape_conic.SetStartAndEndTangentsPlusPassingPoint iStartTgt
        # #     set_start_and_end_tangents_plus_passing_point = iStartTgt
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_start_tangent_direction_flag(self, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetStartTangentDirectionFlag(long iOrientation)
                | 
                |     Sets the tangent direction orientation at the conic start
                |     point.
                | 
                |     Parameters:
                | 
                |         iOrientation
                |             The direction orientation to be applied to the tangent direction at
                |             the conic start point
                |             Legal values: 1 if the tangent direction is to be used as is, and
                |             -1 if it must be inverted 
                | 
                |     Example:
                | 
                |           This example sets the direction orientation of the tangent at the
                |           start point of
                |          the conic hybConic to the inverse of the one of the direction used
                |          for
                |          the tangent.
                |          
                | 
                |          startPtTgtOrient = -1
                |          hybConic.SetStartTangentDirectionFlag
                |          startPtTgtOrient

        :param int i_orientation:
        :rtype: None
        """
        return self.hybrid_shape_conic.SetStartTangentDirectionFlag(i_orientation)

    def set_tangent_intersect_point_plus_conic_parm(self, i_tgt_int: Reference, i_conic_param: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTangentIntersectPointPlusConicParm(Reference
                | iTgtInt,
                | double iConicParam)
                | 
                |     Sets the intersection point of the conic tangents to the start and end
                |     points, and the conic parameter.
                | 
                |     Parameters:
                | 
                |         iTgtInt
                |             The point intersection of the conic tangents to the start and end
                |             point.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex. 
                |     iConicParam
                |         The conic parameter
                |         Legal values: p = 0.5 (parabola), 0<=p<=0.5 (ellipse), 0.5<= p <=1.0 (hyperbola) 
                |     Example:
                | 
                |           This example sets tgtIntPoint as the intersection point of the
                |           tangents
                |          to the start and end points of the conic hybConic, and conicParm as
                |          the conic parameter.
                |          
                | 
                |          hybConic.SetTangentIntersectPointPlusConicParm tgtIntPoint,
                |          conicParm

        :param Reference i_tgt_int:
        :param float i_conic_param:
        :rtype: None
        """
        return self.hybrid_shape_conic.SetTangentIntersectPointPlusConicParm(i_tgt_int.com_object, i_conic_param)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tangent_intersect_point_plus_conic_parm'
        # # vba_code = """
        # # Public Function set_tangent_intersect_point_plus_conic_parm(hybrid_shape_conic)
        # #     Dim iTgtInt (2)
        # #     hybrid_shape_conic.SetTangentIntersectPointPlusConicParm iTgtInt
        # #     set_tangent_intersect_point_plus_conic_parm = iTgtInt
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tangent_intersect_point_plus_passing_point(self, i_tgt_int: Reference, i_passing_pt: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTangentIntersectPointPlusPassingPoint(Reference
                | iTgtInt,
                | Reference iPassingPt)
                | 
                |     Sets the intersection point of the conic tangents to the start and end
                |     points, and a passing point.
                | 
                |     Parameters:
                | 
                |         iTgtInt
                |             The point intersection of the conic tangents to the start and end
                |             point.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex. 
                |     iPassingPt
                |         A point through which the conic must pass.
                |         Legal values: This point must differ from the start and end
                |         points.
                |         Sub-element(s) supported (see Boundary object):
                |         Vertex.
                |     Example:
                | 
                |           This example sets tgtIntPoint as the intersection point of the
                |           tangents
                |          to the start and end points of the conic hybConic, and passingPoint as
                |          a point through
                |          which the conic must pass.
                |          
                | 
                |          hybConic.SetTangentIntersectPointPlusPassingPoint tgtIntPoint,
                |          passingPoint

        :param Reference i_tgt_int:
        :param Reference i_passing_pt:
        :rtype: None
        """
        return self.hybrid_shape_conic.SetTangentIntersectPointPlusPassingPoint(i_tgt_int.com_object,
                                                                                i_passing_pt.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tangent_intersect_point_plus_passing_point'
        # # vba_code = """
        # # Public Function set_tangent_intersect_point_plus_passing_point(hybrid_shape_conic)
        # #     Dim iTgtInt (2)
        # #     hybrid_shape_conic.SetTangentIntersectPointPlusPassingPoint iTgtInt
        # #     set_tangent_intersect_point_plus_passing_point = iTgtInt
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_three_intermediate_passing_points(self, i_pass_pt1: Reference, i_pass_pt2: Reference,
                                              i_pass_pt3: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetThreeIntermediatePassingPoints(Reference iPassPt1,
                | Reference iPassPt2,
                | Reference iPassPt3)
                | 
                |     Sets three conic intermediate passing points.
                | 
                |     Parameters:
                | 
                |         iPassPt1
                |             The first intermediate passing point.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex. 
                |     iPassPt2
                |         The second intermediate passing point.
                |         Sub-element(s) supported (see Boundary object):
                |         Vertex.
                |     iPassPt3
                |         The third intermediate passing point.
                |         Sub-element(s) supported (see Boundary object):
                |         Vertex.
                |     Example:
                | 
                |           This example sets passingPoint1, passingPoint2, and passingPoint3 as
                |           the
                |          three intermediate points through which the conic hybConic must
                |          pass.
                |          
                | 
                |          hybConic.SetThreeIntermediatePassingPoints passingPoint1,
                |          passingPoint2, passingPoint3

        :param Reference i_pass_pt1:
        :param Reference i_pass_pt2:
        :param Reference i_pass_pt3:
        :rtype: None
        """
        return self.hybrid_shape_conic.SetThreeIntermediatePassingPoints(i_pass_pt1.com_object, i_pass_pt2.com_object,
                                                                         i_pass_pt3.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_three_intermediate_passing_points'
        # # vba_code = """
        # # Public Function set_three_intermediate_passing_points(hybrid_shape_conic)
        # #     Dim iPassPt1 (2)
        # #     hybrid_shape_conic.SetThreeIntermediatePassingPoints iPassPt1
        # #     set_three_intermediate_passing_points = iPassPt1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_two_intermediate_passing_points_plus_one_tangent(self, i_pass_pt1: Reference, i_pass_pt2: Reference,
                                                             i_tgt_dir: HybridShapeDirection,
                                                             i_index_point: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTwoIntermediatePassingPointsPlusOneTangent(Reference
                | iPassPt1,
                | Reference iPassPt2,
                | HybridShapeDirection iTgtDir,
                | long iIndexPoint)
                | 
                |     Sets two conic intermediate passing points and a tangent at one of the
                |     passing points.
                | 
                |     Parameters:
                | 
                |         iPassPt1
                |             The first intermediate passing point.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex. 
                |     iPassPt2
                |         The second intermediate passing point.
                |         Sub-element(s) supported (see Boundary object):
                |         Vertex.
                |     iTgtDir
                |         The tangent direction at one of the intermediate passing points
                |         
                |     iIndexPoint
                |         An index indicating the passing point to which the tangent direction
                |         applies
                |         Legal values: 1 for the first passing point, and 2 for the second one
                |         
                |     Example:
                | 
                |           This example sets passingPoint1 and passingPoint2 as
                |           two
                |          intermediate points through which the conic hybConic must
                |          pass,
                |          tgtDir as the tangent direction at the passing point designated by
                |          passingPointIdx.
                |          
                | 
                |          hybConic.SetTwoIntermediatePassingPointsPlusOneTangent passingPoint1,
                |          passingPoint2, tgtDir, passingPointIdx

        :param Reference i_pass_pt1:
        :param Reference i_pass_pt2:
        :param HybridShapeDirection i_tgt_dir:
        :param int i_index_point:
        :rtype: None
        """
        return self.hybrid_shape_conic.SetTwoIntermediatePassingPointsPlusOneTangent(i_pass_pt1.com_object,
                                                                                     i_pass_pt2.com_object,
                                                                                     i_tgt_dir.com_object,
                                                                                     i_index_point)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_two_intermediate_passing_points_plus_one_tangent'
        # # vba_code = """
        # # Public Function set_two_intermediate_passing_points_plus_one_tangent(hybrid_shape_conic)
        # #     Dim iPassPt1 (2)
        # #     hybrid_shape_conic.SetTwoIntermediatePassingPointsPlusOneTangent iPassPt1
        # #     set_two_intermediate_passing_points_plus_one_tangent = iPassPt1
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def switch_end_tangent_direction(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SwitchEndTangentDirection()
                | 
                |     Inverts the tangent direction orientation at the conic end
                |     point.
                | 
                |     Example:
                | 
                |           This example inverts the direction orientation of the tangent at the
                |           end point of
                |          the conic hybConic.
                |          
                | 
                |          hybConic.SwitchEndTangentDirection

        :rtype: None
        """
        return self.hybrid_shape_conic.SwitchEndTangentDirection()

    def switch_intermediate_tangent_direction(self, i_index_point: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SwitchIntermediateTangentDirection(long iIndexPoint)
                | 
                |     Inverts the tangent direction orientation of one of the conic intermediate
                |     points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point where the tangent
                |             direction is to be inverted
                |             Legal values: 1 for the first passing point, and 2 for the second
                |             one 
                | 
                |     Example:
                | 
                |           This example inverts the direction orientation of the tangent at the
                |           first point through which
                |          the conic hybConic passes.
                |          
                | 
                |          passingPtIdx = 1
                |          hybConic.SwitchIntermediateTangentDirection
                |          passingPtIdx

        :param int i_index_point:
        :rtype: None
        """
        return self.hybrid_shape_conic.SwitchIntermediateTangentDirection(i_index_point)

    def switch_start_tangent_direction(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SwitchStartTangentDirection()
                | 
                |     Inverts the tangent direction orientation at the conic start
                |     point.
                | 
                |     Example:
                | 
                |           This example inverts the direction orientation of the tangent at the
                |           start point of
                |          the conic hybConic.
                |          
                | 
                |          hybConic.SwitchStartTangentDirection

        :rtype: None
        """
        return self.hybrid_shape_conic.SwitchStartTangentDirection()

    def __repr__(self):
        return f'HybridShapeConic(name="{self.name}")'
