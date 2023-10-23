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
from pycatia.knowledge_interfaces.real_param import RealParam
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeBlend(HybridShape):
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
                |                         HybridShapeBlend
                | 
                | Represents the hybrid shape blended surface object.
                | Role: To access the data of the hybrid shape blended surface
                | object.
                | 
                | This data includes:
                | 
                |     Two support surfaces, one at each limit of the blended
                |     surface
                |     Two curves, one for each support surface
                |     The curve closing points
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeBlend
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_blend = com_object

    @property
    def coupling(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Coupling() As long
                | 
                |     Returns or sets the type of coupling between the limits of the
                |     blend.
                |     Legal values: The values representing the type of coupling can
                |     be:
                | 
                |     1
                |         Ratio: the curves are coupled according to the curvilinear abscissa
                |         ratio 
                |     2
                |         Tangency: the curves are coupled according to their tangency
                |         discontinuity points. If they do not have the same number of tangency
                |         discontinuity points, they cannot be coupled and an error message is displayed
                |         
                |     3
                |         Tangency then curvature: the curves are coupled according to their
                |         tangency discontinuity points first, then according to their curvature
                |         discontinuity points. If they do not have the same number of tangency and
                |         curvature discontinuity points, they cannot be coupled and an error message is
                |         displayed 
                |     4
                |         Vertices: the curves are coupled according to their vertices. If they
                |         do not have the same number of vertices, they cannot be coupled and an error
                |         message is displayed 
                |     5
                |         Spine: coupling is completely driven by a curve (called spine)
                |         
                | 
                |     Example:
                |         This example retrieves in CouplingVal the coupling value of the
                |         ShpBlend hybrid shape blended feature.
                | 
                |          CouplingVal = ShpBlend.Coupling

        :rtype: int
        """

        return self.hybrid_shape_blend.Coupling

    @coupling.setter
    def coupling(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_blend.Coupling = value

    @property
    def ruled_developable_surface(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property RuledDevelopableSurface() As boolean
                | 
                |     Returns or sets the ruled developable surface mode.
                |     TRUE means that the mode is enabled and FALSE means that it is disabled.

        :rtype: bool
        """

        return self.hybrid_shape_blend.RuledDevelopableSurface

    @ruled_developable_surface.setter
    def ruled_developable_surface(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_blend.RuledDevelopableSurface = value

    @property
    def smooth_angle_threshold(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothAngleThreshold() As Angle (Read Only)
                | 
                |     Returns the angular threshold.

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_blend.SmoothAngleThreshold)

    @property
    def smooth_angle_threshold_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothAngleThresholdActivity() As boolean
                | 
                |     Returns or sets information whether a blending operation is smoothed or
                |     not.
                |     TRUE if the blending operation is smoothed, or FALSE otherwise (FALSE if
                |     not specified).

        :rtype: bool
        """

        return self.hybrid_shape_blend.SmoothAngleThresholdActivity

    @smooth_angle_threshold_activity.setter
    def smooth_angle_threshold_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_blend.SmoothAngleThresholdActivity = value

    @property
    def smooth_deviation(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothDeviation() As Length (Read Only)
                | 
                |     Returns the deviation value (length) from guide curves allowed during a
                |     sweeping operation in order to smooth it.

        :rtype: Length
        """

        return Length(self.hybrid_shape_blend.SmoothDeviation)

    @property
    def smooth_deviation_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SmoothDeviationActivity() As boolean
                | 
                |     Returns or sets information whether a deviation from guide curves is
                |     allowed or not.
                |     Gives the information on performing smoothing during blending
                |     operation.
                |     TRUE if a deviation from guide curves is allowed, or FALSE otherwise (FALSE
                |     if not specified).

        :rtype: bool
        """

        return self.hybrid_shape_blend.SmoothDeviationActivity

    @smooth_deviation_activity.setter
    def smooth_deviation_activity(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_blend.SmoothDeviationActivity = value

    @property
    def spine(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Spine() As Reference
                | 
                |     Returns or sets a curve used as spine for coupling in Blend computation.
                |     Setting the spine curve also changes coupling mode to CATGSMSpineCoupling. In
                |     order to remove the spine, set another coupling mode.
                | 
                |     Parameters:
                | 
                |         iSpine
                |             spine curve

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_blend.Spine)

    @spine.setter
    def spine(self, reference_spine: Reference):
        """
        :param Reference reference_spine:
        """

        self.hybrid_shape_blend.Spine = reference_spine.com_object

    def get_border_mode(self, i_blend_limit: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetBorderMode(long iBlendLimit) As long
                | 
                |     Returns the type of border to a limit of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose type of border is to be
                |             retrieved.
                |             Legal values: 1 for the first limit, and 2 for the second one
                |             
                | 
                |     Returns:
                |         The type of border
                |         Legal values:
                | 
                |         1
                |             The border of the blend will be tangent to the border of the
                |             support surface, or if the curve ends on the border of a face of the support
                |             surface, then the border of the blend will be tangent to the border face.
                |             
                |         2
                |             The border of the blend is not constrained. 
                | 
                | Example:
                |     This example retrieves in BorderType the type of border of the first limit
                |     of the ShpBlend hybrid shape blended feature.
                | 
                |      BorderType = ShpBlend.GetBorderMode(1)

        :param int i_blend_limit:
        :rtype: int
        """
        return self.hybrid_shape_blend.GetBorderMode(i_blend_limit)

    def get_closing_point(self, i_blend_limit: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetClosingPoint(long iBlendLimit) As Reference
                | 
                |     Returns the closing point of a closed curve of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose curve closing point is
                |             returned.
                |             Legal values: 1 for the first curve, and 2 for the second one
                |             
                | 
                |     Returns:
                |         The retrieved closing point 
                | 
                | Example:
                |     This example retrieves in ClosingPoint the closing point of the curve of
                |     the second limit of the ShpBlend hybrid shape blended
                |     feature.
                | 
                |      Dim ClosingPoint As Reference
                |      ClosingPoint = ShpBlend.GetClosingPoint(2)

        :param int i_blend_limit:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_blend.GetClosingPoint(i_blend_limit))

    def get_continuity(self, i_blend_limit: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetContinuity(long iBlendLimit) As long
                | 
                |     Retrieves the continuity of a limit of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose continuity is to be
                |             retrieved.
                |             Legal values: 1 for the first limit, and 2 for the second one
                |             
                | 
                |     Returns:
                |         The retrieved continuity.
                |         Legal values:
                | 
                |         0
                |             Point continuity 
                |         1
                |             Tangency continuity 
                |         2
                |             Curvature continuity 
                | 
                | Example:
                |     This example retrieves in Continuity the continuity of the second limit of
                |     the ShpBlend hybrid shape blended feature.
                | 
                |      Continuity = ShpBlend.GetContinuity(2)

        :param int i_blend_limit:
        :rtype: int
        """
        return self.hybrid_shape_blend.GetContinuity(i_blend_limit)

    def get_curve(self, i_blend_limit: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetCurve(long iBlendLimit) As Reference
                | 
                |     Returns a curve from the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend from which the curve will be
                |             retrieved.
                |             Legal values: 1 for the first curve, and 2 for the second one
                |             
                | 
                |     Returns:
                |         The retrieved curve 
                | 
                | Example:
                |     This example retrieves in BlendCurve the curve of the second limit of the
                |     ShpBlend hybrid shape blended feature.
                | 
                |      Dim BlendCurve As Reference
                |      BlendCurve = ShpBlend.GetCurve(2)

        :param int i_blend_limit:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_blend.GetCurve(i_blend_limit))

    def get_orientation(self, i_blend_limit: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetOrientation(long iBlendLimit) As long
                | 
                |     Returns the orientation of a curve of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose curve orientation is to be
                |             retrieved.
                |             Legal values: 1 for the first curve, and 2 for the second one
                |             
                | 
                |     Returns:
                |         The orientation to set to the curve.
                |         Legal values: 1 for direct and -1 for reverse 
                | 
                | Example:
                |     This example retrieves in Orientation the orientation of the second limit
                |     of the ShpBlend hybrid shape blended feature.
                | 
                |      Orientation = ShpBlend.GetOrientation(2)

        :param int i_blend_limit:
        :rtype: int
        """
        return self.hybrid_shape_blend.GetOrientation(i_blend_limit)

    def get_ruled_developable_surface_connection(self, i_blend_limit: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetRuledDevelopableSurfaceConnection(long iBlendLimit) As
                | long
                | 
                |     Returns or sets the ruled developable surface connection
                |     type.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend for which the connection type is to be
                |             set.
                |             Legal values: 1 for the start limit, and 2 for the end one
                |             
                |         oBlendConnection
                |             The value of connection type
                |             Legal values:
                | 
                |             1
                |                 Connect to both extremities 
                |             2
                |                 Free first curve 
                |             3
                |                 Free second curve

        :param int i_blend_limit:
        :rtype: int
        """
        return self.hybrid_shape_blend.GetRuledDevelopableSurfaceConnection(i_blend_limit)

    def get_support(self, i_blend_limit: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetSupport(long iBlendLimit) As Reference
                | 
                |     Returns a support from the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose support is to be
                |             retrieved.
                |             Legal values: 1 for the first support, and 2 for the second one
                |             
                | 
                |     Returns:
                |         The retrieved support surface 
                | 
                | Example:
                |     This example retrieves in SupportSurf the support surface of the second
                |     limit of the ShpBlend hybrid shape blended feature.
                | 
                |      Dim SupportSurf As Reference 
                |      SupportSurf = ShpBlend.GetSupport(2)

        :param int i_blend_limit:
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_blend.GetSupport(i_blend_limit))

    def get_tension_in_double(self, i_blend_limit: int, i_rank: int) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTensionInDouble(long iBlendLimit,
                | long iRank) As RealParam
                | 
                |     Returns the tension values of a limit of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend from which the tension type and values are
                |             to be retrieved.
                |             Legal values: 1 for the first limit, and 2 for the second one
                |             
                |         iRank
                |             The rank of the value to retrieve among those available, depending
                |             on the tension type.
                |             Legal values: iRank can take the following values:
                | 
                |             1
                |                 With default tension and constant tension, for the unique
                |                 available value, and with linear tension for the first value
                |                 
                |             2
                |                 With linear tension for the second value 
                | 
                |     Returns:
                |         The retrieved tension value 
                | 
                | Example:
                |     This example retrieves in TensionVal the tension value of the tension,
                |     supposed to be a constant tension, of the first limit of the ShpBlend hybrid
                |     shape blended feature.
                | 
                |      Dim ConstTensionVal As RealParam
                |      Set ConstTensionVal = ShpBlend.GetTensionInDouble(1, 1)

        :param int i_blend_limit:
        :param int i_rank:
        :rtype: RealParam
        """
        return RealParam(self.hybrid_shape_blend.GetTensionInDouble(i_blend_limit, i_rank))

    def get_tension_type(self, i_blend_limit: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTensionType(long iBlendLimit) As long
                | 
                |     Returns the tension type of a limit of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend from which the tension type is to be
                |             retrieved.
                |             Legal values: 1 for the first limit, and 2 for the second one
                |             
                | 
                |     Returns:
                |         The value of tension type
                |         Legal values:
                | 
                |         1
                |             Default tension 
                |         2
                |             Constant tension 
                |         3
                |             Linear tension 
                | 
                | Example:
                |     This example retrieves in TensionType the tension type of the first limit
                |     of the ShpBlend hybrid shape blended feature.
                | 
                |      TensionType.GetTensionType(1)

        :param int i_blend_limit:
        :rtype: int
        """
        return self.hybrid_shape_blend.GetTensionType(i_blend_limit)

    def get_transition(self, i_blend_limit: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTransition(long iBlendLimit) As long
                | 
                |     Returns the transition orientation from a limit of the
                |     blend.
                |     Let T be the tangent to the wire, and N be the normal to the skin body. The
                |     transition orientation defines how the blend goes from the initial wires: it
                |     takes the direction of iTransition*(T^N), where ^ is the cross
                |     product.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose transition orientation is to be
                |             retrieved.
                |             Legal values: 1 for the first support, and 2 for the second one
                |             
                | 
                |     Returns:
                |         The retrieved value of transition orientation.
                |         Legal values: 1 for direct and -1 for reverse 
                | 
                | Example:
                |     This example retrieves in TransOrientation the transition orientation of
                |     the second limit of the ShpBlend hybrid shape blended
                |     feature.
                | 
                |      TransOrientation = ShpBlend.GetTransition(2)

        :param int i_blend_limit:
        :rtype: int
        """
        return self.hybrid_shape_blend.GetTransition(i_blend_limit)

    def get_trim_support(self, i_blend_limit: int) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTrimSupport(long iBlendLimit) As long
                | 
                |     Returns whether a support of the blend will be trimmed
                |     off.
                |     If the support is set to be trimmed, it will be trimmed using the curve
                |     then joined to the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose support is to be
                |             trimmed.
                |             Legal values: 1 for the first limit, and 2 for the second one
                |             
                | 
                |     Returns:
                |         The trim support mode
                |         Legal values:
                | 
                |         1
                |             No trim 
                |         2
                |             The support will be trimmed 
                | 
                | Example:
                |     This example retrieves whether the second limit of the ShpBlend hybrid
                |     shape blended feature should be trimmed off.
                | 
                |      IsTrimmed = ShpBlend.GetTrimSupport(2)

        :param int i_blend_limit:
        :rtype: int
        """
        return self.hybrid_shape_blend.GetTrimSupport(i_blend_limit)

    def insert_coupling(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertCoupling(long iPosition)
                | 
                |     Inserts a coupling into the blend.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position of the coupling in the list of couplings. Setting
                |             iPosition to 0 inserts the coupling at the end of the list.
                |             
                | 
                |     Example:
                |         This example inserts a coupling at the end of the coupling list of the
                |         ShpBlend hybrid shape blended feature.
                | 
                |          ShpBlend.InsertCouplingt 0

        :param int i_position:
        :rtype: None
        """
        return self.hybrid_shape_blend.InsertCoupling(i_position)

    def insert_coupling_point(self, i_coupling_index: int, i_position: int, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InsertCouplingPoint(long iCouplingIndex,
                | long iPosition,
                | Reference iPoint)
                | 
                |     Inserts a coupling point to a coupling of the blend.
                | 
                |     Parameters:
                | 
                |         iCouplingIndex
                |             The index of the coupling in the list of couplings into which the
                |             coupling point will be inserted. 
                |         iPosition
                |             The position of the coupling point in the list of coupling points.
                |             Setting iPosition to 0 inserts the coupling point at the end of the list.
                |             
                |         iPoint
                |             The coupling point to be inserted. This point must lay on the
                |             section with the same position.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex. 
                | 
                | Example:
                |     This example inserts the Point23 point into the third coupling at the end
                |     of the list of coupling points of the ShpBlend hybrid shape blended
                |     feature.
                | 
                |      ShpBlend.InsertCouplingPoint 3, 0, Point23

        :param int i_coupling_index:
        :param int i_position:
        :param Reference i_point:
        :rtype: None
        """
        return self.hybrid_shape_blend.InsertCouplingPoint(i_coupling_index, i_position, i_point.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'insert_coupling_point'
        # # vba_code = """
        # # Public Function insert_coupling_point(hybrid_shape_blend)
        # #     Dim iCouplingIndex (2)
        # #     hybrid_shape_blend.InsertCouplingPoint iCouplingIndex
        # #     insert_coupling_point = iCouplingIndex
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_border_mode(self, i_blend_limit: int, i_border: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetBorderMode(long iBlendLimit,
                | long iBorder)
                | 
                |     Sets the type of border to a limit of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose type of border is to be
                |             set.
                |             Legal values: 1 for the first limit, and 2 for the second one
                |             
                |         iBorder
                |             The type of border
                |             Legal values:
                | 
                |             1
                |                 The border of the blend will be tangent to the border of the
                |                 support surface, or if the curve ends on the border of a face of the support
                |                 surface, then the border of the blend will be tangent to the border face.
                |                 
                |             2
                |                 The border of the blend is not constrained. 
                |             3
                |                 The border of the blend will be tangent to the border of the
                |                 support surface at the start extremity of the curve, or if the curve ends on
                |                 the border of a face of the support surface, then the border of the blend will
                |                 be tangent to the border face at the start extremity of the curve.
                |                 
                |             4
                |                 The border of the blend will be tangent to the border of the
                |                 support surface at the end extremity of the curve, or if the curve ends on the
                |                 border of a face of the support surface, then the border of the blend will be
                |                 tangent to the border face at the end extremity of the curve.
                |                 
                | 
                |     Example:
                |         This example sets the type of border of the second limit of the
                |         ShpBlend hybrid shape blended feature to "no
                |         constraint".
                | 
                |          ShpBlend.SetBorderMode 2, 2

        :param int i_blend_limit:
        :param int i_border:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetBorderMode(i_blend_limit, i_border)

    def set_closing_point(self, i_blend_limit: int, i_closing_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetClosingPoint(long iBlendLimit,
                | Reference iClosingPoint)
                | 
                |     Sets a new closing point to a closed curve of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose curve will be set a new closing
                |             point.
                |             Legal values: 1 for the first curve, and 2 for the second one
                |             
                |         iClosingPoint
                |             The closing point to be set. This point must lay on the curve of
                |             the blend limit.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Vertex. 
                | 
                | Example:
                |     This example sets the Point10 point as the closing point to the second
                |     limit of the ShpBlend hybrid shape blended feature.
                | 
                |      ShpBlend.SetClosingPoint 2, Point10

        :param int i_blend_limit:
        :param Reference i_closing_point:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetClosingPoint(i_blend_limit, i_closing_point.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_closing_point'
        # # vba_code = """
        # # Public Function set_closing_point(hybrid_shape_blend)
        # #     Dim iBlendLimit (2)
        # #     hybrid_shape_blend.SetClosingPoint iBlendLimit
        # #     set_closing_point = iBlendLimit
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_continuity(self, i_blend_limit: int, i_continuity: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetContinuity(long iBlendLimit,
                | long iContinuity)
                | 
                |     Sets the continuity to a limit of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose continuity is to be
                |             set.
                |             Legal values: 1 for the first limit, and 2 for the second one
                |             
                |         iContinuity
                |             The continuity to set
                |             Legal values:
                | 
                |             0
                |                 Point continuity 
                |             1
                |                 Tangency continuity 
                |             2
                |                 Curvature continuity 
                | 
                |     Example:
                |         This example sets the continuity of the second limit of the ShpBlend
                |         hybrid shape blended feature to tangency continuity.
                | 
                |          ShpBlend.SetContinuity 2, 1

        :param int i_blend_limit:
        :param int i_continuity:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetContinuity(i_blend_limit, i_continuity)

    def set_curve(self, i_blend_limit: int, i_curve: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetCurve(long iBlendLimit,
                | Reference iCurve)
                | 
                |     Sets a curve to the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend to which the curve will be
                |             set.
                |             Legal values: 1 for the first curve, and 2 for the second one
                |             
                |         iCurve
                |             The curve to be set.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): TriDimFeatEdge and BiDimFeatEdge. 
                | 
                | Example:
                |     This example sets the CurveForBlend curve to the second limit of the
                |     ShpBlend hybrid shape blended feature.
                | 
                |      ShpBlend.SetCurve 2, CurveForBlend

        :param int i_blend_limit:
        :param Reference i_curve:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetCurve(i_blend_limit, i_curve.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_curve'
        # # vba_code = """
        # # Public Function set_curve(hybrid_shape_blend)
        # #     Dim iBlendLimit (2)
        # #     hybrid_shape_blend.SetCurve iBlendLimit
        # #     set_curve = iBlendLimit
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_orientation(self, i_blend_limit: int, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetOrientation(long iBlendLimit,
                | long iOrientation)
                | 
                |     Sets the orientation of a curve of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose curve orientation is to be
                |             set.
                |             Legal values: 1 for the first curve, and 2 for the second one
                |             
                |         iOrientation
                |             The orientation to set to the curve.
                |             Legal values: 1 for direct and -1 for reverse 
                | 
                |     Example:
                |         This example sets the orientation of the second limit of the ShpBlend
                |         hybrid shape blended feature to direct.
                | 
                |          ShpBlend.SetOrientation 2, 1

        :param int i_blend_limit:
        :param int i_orientation:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetOrientation(i_blend_limit, i_orientation)

    def set_ruled_developable_surface_connection(self, i_blend_limit: int, i_blend_connection: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetRuledDevelopableSurfaceConnection(long iBlendLimit,
                | long iBlendConnection)

        :param int i_blend_limit:
        :param int i_blend_connection:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetRuledDevelopableSurfaceConnection(i_blend_limit, i_blend_connection)

    def set_smooth_angle_threshold(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSmoothAngleThreshold(double iAngle)
                | 
                |     Sets the angular threshold.
                | 
                |     Parameters:
                | 
                |         iAngle
                |             The angular threshold

        :param float i_angle:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetSmoothAngleThreshold(i_angle)

    def set_smooth_deviation(self, i_length: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSmoothDeviation(double iLength)
                | 
                |     Sets the deviation value (length) from guide curves allowed during sweeping
                |     operation in order to smooth it.
                | 
                |     Parameters:
                | 
                |         iLength
                |             The deviation value

        :param float i_length:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetSmoothDeviation(i_length)

    def set_support(self, i_blend_limit: int, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetSupport(long iBlendLimit,
                | Reference iSupport)
                | 
                |     Sets a support to the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose support is to be set.
                |             Legal values: 1 for the first support, and 2 for the second one
                |             
                |         iSupport
                |             The support surface to be set. The curve of the blend limit must
                |             lay on the surface.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Face. 
                | 
                | Example:
                |     This example sets the SupportSurf surface as the support of the second
                |     limit of the ShpBlend hybrid shape blended feature.
                | 
                |      ShpBlend.SetSupport 2, SupportSurf

        :param int i_blend_limit:
        :param Reference i_support:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetSupport(i_blend_limit, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_support'
        # # vba_code = """
        # # Public Function set_support(hybrid_shape_blend)
        # #     Dim iBlendLimit (2)
        # #     hybrid_shape_blend.SetSupport iBlendLimit
        # #     set_support = iBlendLimit
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tension_in_double(self, i_blend_limit: int, i_tension_type: int, i_first_tension: float,
                              i_second_tension: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTensionInDouble(long iBlendLimit,
                | long iTensionType,
                | double iFirstTension,
                | double iSecondTension)
                | 
                |     Sets the tension values to a limit of the blend. The values must be
                |     expressed as doubles and must be positive.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend to which the tension values are to be
                |             set.
                |             Legal values: 1 for the first limit, and 2 for the second one
                |             
                |         iTensionType
                |             The tension type
                |             Legal values:
                | 
                |             1
                |                 Default tension 
                |             2
                |                 Constant tension 
                |             3
                |                 Linear tension 
                | 
                |         iFirstTension
                |             The value for the first tension. It must be used with any tension
                |             type
                |             Legal values: it must be a double and positive. 
                |         iSecondTension
                |             The value for the second tension. It can be used with linear
                |             tension only
                |             Legal values: it must be a double and positive. 
                | 
                |     Example:
                |         This example sets the tension values of the tension, supposed to be a
                |         linear tension, of the first limit of the ShpBlend hybrid shape blended feature
                |         to respectively 1.5 and 0.5.
                | 
                |          ShpBlend.SetTensionInDouble 1, 3, 1.5, 0.5

        :param int i_blend_limit:
        :param int i_tension_type:
        :param float i_first_tension:
        :param float i_second_tension:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetTensionInDouble(i_blend_limit, i_tension_type, i_first_tension,
                                                          i_second_tension)

    def set_tension_type(self, i_blend_limit: int, i_tension_type: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTensionType(long iBlendLimit,
                | long iTensionType)
                | 
                |     Sets the tension type of a limit of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend for which the tension type is to be
                |             set.
                |             Legal values: 1 for the first limit, and 2 for the second one
                |             
                |         iBlendLimit
                |             The value of tension type
                |             Legal values:
                | 
                |             1
                |                 Default tension 
                |             2
                |                 Constant tension 
                |             3
                |                 Linear tension 
                |             4
                |                 SType tension 
                | 
                |     Example:
                |         This example sets the tension type as Default Tension for the first
                |         limit of the ShpBlend hybrid shape blended feature.
                | 
                |          ShpBlend.SetTensionType 1, 1

        :param int i_blend_limit:
        :param int i_tension_type:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetTensionType(i_blend_limit, i_tension_type)

    def set_transition(self, i_blend_limit: int, i_transition: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTransition(long iBlendLimit,
                | long iTransition)
                | 
                |     Sets the transition orientation to a limit of the blend.
                |     Role: Let T be the tangent to the wire, and N be the normal to the skin
                |     body. The transition orientation defines how the blend goes from the initial
                |     wires: it takes the direction of iTransition*(T^N), where ^ is the cross
                |     product.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose transition orientation is to be
                |             set.
                |             Legal values: 1 for the first support, and 2 for the second one
                |             
                |         iTransition
                |             The value of transition orientation.
                |             Legal values: 1 for direct and -1 for reverse 
                | 
                |     Example:
                |         This example sets the transition orientation of the second limit of the
                |         ShpBlend hybrid shape blended feature to reverse.
                | 
                |          ShpBlend.SetTransition 2, -1

        :param int i_blend_limit:
        :param int i_transition:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetTransition(i_blend_limit, i_transition)

    def set_trim_support(self, i_blend_limit: int, i_trim_support: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTrimSupport(long iBlendLimit,
                | long iTrimSupport)
                | 
                |     Sets whether a support of the blend is to be trimmed off.
                |     If the support is set to be trimmed, it will be trimmed using the curve
                |     then joined to the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose support is to be
                |             trimmed.
                |             Legal values: 1 for the first limit, and 2 for the second one
                |             
                |         iTrimSupport
                |             The trim support mode
                |             Legal values:
                | 
                |             1
                |                 No trim 
                |             2
                |                 The support will be trimmed 
                | 
                |     Example:
                |         This example sets that the second limit of the ShpBlend hybrid shape
                |         blended feature should be trimmed off.
                | 
                |          ShpBlend.SetTrimSupport 2, 2

        :param int i_blend_limit:
        :param int i_trim_support:
        :rtype: None
        """
        return self.hybrid_shape_blend.SetTrimSupport(i_blend_limit, i_trim_support)

    def unset_closing_point(self, i_blend_limit: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub UnsetClosingPoint(long iBlendLimit)
                | 
                |     Unsets the closing point of a closed curve of the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose curve closing point is
                |             unset.
                |             Legal values: 1 for the first curve, and 2 for the second one
                |             
                | 
                |     Example:
                |         This example unsets the closing point of the second limit of the
                |         ShpBlend hybrid shape blended feature.
                | 
                |          ShpBlend.UnsetClosingPoint 2

        :param int i_blend_limit:
        :rtype: None
        """
        return self.hybrid_shape_blend.UnsetClosingPoint(i_blend_limit)

    def unset_support(self, i_blend_limit: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub UnsetSupport(long iBlendLimit)
                | 
                |     Unsets a support from the blend.
                | 
                |     Parameters:
                | 
                |         iBlendLimit
                |             The limit of the blend whose support is to be
                |             unset.
                |             Legal values: 1 for the first support, and 2 for the second one
                |             
                | 
                |     Example:
                |         This example unsets the support surface of the second limit of the
                |         ShpBlend hybrid shape blended feature.
                | 
                |          ShpBlend.UnsetSupport 2

        :param int i_blend_limit:
        :rtype: None
        """
        return self.hybrid_shape_blend.UnsetSupport(i_blend_limit)

    def __repr__(self):
        return f'HybridShapeBlend(name="{self.name}")'
