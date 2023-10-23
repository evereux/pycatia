#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_direction import HybridShapeDirection
from pycatia.hybrid_shape_interfaces.point import Point
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.knowledge_interfaces.real_param import RealParam


class HybridShapePointOnCurve(Point):
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
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointOnCurve
                | 
                | Represents the hybrid shape point on a curve.
                | Role: To access the data of the point object created on a curve. This data
                | includes:
                | 
                |     The curve onto which the point is created
                |     The reference point from which the point is created
                |     The curvilinear distance from the reference point
                |     The ratio of distance with respect to the curve length
                |     The distance stored value type, either distance or ratio
                |     The curve orientation
                |     The distance type, either geodesic or euclidean.
                |     The direction along which point is created with specified
                |     distance.
                | 
                | Use the HybridShapeFactory to create a HybridShapePointOnCurve
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_on_curve = com_object

    @property
    def curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Curve() As Reference
                | 
                |     Returns or sets the curve onto which the point is or should be
                |     created.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                | 
                |           This example retrieves in oCurve the supporting curve 
                |           for
                |          the pointOnCurve hybrid shape point.
                |          
                | 
                |          Dim oCurve As CATIAReference
                |          Set oCurve = pointOnCurve.Curve

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_on_curve.Curve)

    @curve.setter
    def curve(self, reference_curve: Reference):
        """
        :param Reference reference_curve:
        """

        self.hybrid_shape_point_on_curve.Curve = reference_curve.com_object

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Returns or sets the direction along which the point is or should be
                |     created.
                | 
                |     Example
                |         This example retrieves in Dir the direction for the PointOnCurve hybrid
                |         shape feature.
                | 
                |          Dim Dir As CATIAHybridShapeDirection
                |          Set Dir=pointOnCurve.Direction

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_point_on_curve.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_point_on_curve.Direction = direction.com_object

    @property
    def distance_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property DistanceType() As long
                | 
                |     Returns or sets the distance type.
                |     Legal values: 1 for geodesic, -1 for euclidean.
                |     Default is geodesic.
                | 
                |         Geodesic means that the distance is measured with a curvilinear
                |         abscissa
                |         Euclidean means that the point is created as the intersection between
                |         the reference curve and a circle whose radius is the length defined
                |         above.
                | 
                |     Example:
                | 
                |           This example retrieves in oDistanceType the distance computation type
                |           used 
                |          for the pointOnCurve hybrid shape object.
                |          
                | 
                |          Dim oDistanceType As  long
                |          Set oDistanceType = pointOnCurve.DistanceType

        :rtype: int
        """

        return self.hybrid_shape_point_on_curve.DistanceType

    @distance_type.setter
    def distance_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_point_on_curve.DistanceType = value

    @property
    def offset(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Offset() As Length (Read Only)
                | 
                |     Returns the distance to the reference point.
                |     This distance is a distance in a length unit, The distance can be null.In
                |     this case, the reference point is the curve end point defined using the
                |     Orientation parameter.
                | 
                |     Example:
                | 
                |           This example retrieves in oOffset the distance from the reference
                |           point
                |          on the supporting curve for the pointOnCurve hybrid shape
                |          object.
                |          
                | 
                |          Dim oOffset As  CATIALength  
                |          Set oOffset = pointOnCurve.Offset

        :rtype: Length
        """

        return Length(self.hybrid_shape_point_on_curve.Offset)

    @property
    def on_curve_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OnCurveType() As long
                | 
                |     Returns or sets the OnCurve type for created point on
                |     curve.
                |     Legal values: 0 = Distance on curve 1 = Distance along direction 2 = Ratio of Curve length

        :rtype: int
        """

        return self.hybrid_shape_point_on_curve.OnCurveType

    @on_curve_type.setter
    def on_curve_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_point_on_curve.OnCurveType = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation() As long
                | 
                |     Returns or sets the curve orientation.
                |     Legal values: -1 means that the distance (length or ratio) is
                |     measured:
                | 
                |         in the other orientation of the curve, when a reference point has been
                |         set
                |         in the other orientation of the curve and from the other extremity,
                |         when no reference point has been set.
                | 
                |     Example:
                | 
                |           This example retrieves in oOrientation curve Orientation use
                |           
                |          for the pointOnCurve hybrid shape feature.
                |          
                | 
                |          Dim oOrientation As  long
                |          Set oOrientation = pointOnCurve.Orientation

        :rtype: int
        """

        return self.hybrid_shape_point_on_curve.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_point_on_curve.Orientation = value

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Point() As Reference
                | 
                |     Returns or sets the reference point.
                | 
                |     If the point does not lie on the curve, the point on the curve with the
                |     smallest distance to this point is taken.
                | 
                |     The reference point may not exist. In this case, the extremity of the curve
                |     is taken as reference point.
                | 
                | 
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                | 
                |           This example retrieves in oRefPoint the reference
                |           point
                |          on the supporting curve for the pointOnCurve hybrid shape
                |          object.
                |          
                | 
                |          Dim oRefPoint As  CATIAReference
                |          Set oRefPoint = pointOnCurve.Point

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_on_curve.Point)

    @point.setter
    def point(self, reference_point: Reference):
        """
        :param Reference reference_point:
        """

        self.hybrid_shape_point_on_curve.Point = reference_point.com_object

    @property
    def ratio(self) -> RealParam:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Ratio() As RealParam (Read Only)
                | 
                |     Returns the distance ratio to the reference point.
                |     This is a real parameter which corresponds to the ratio of the distance
                |     from the reference point with respect to the length of the supporting curve.
                |     The ratio can be null. In this case, the reference point is the curve end point
                |     defined using the Orientation parameter.
                | 
                |     Example:
                | 
                |           This example retrieves in oRatio the distance ratio from the
                |           reference point
                |          on the supporting curve for the pointOnCurve hybrid shape
                |          object.
                |          
                | 
                |          Dim oRatio As  CATIALength  
                |          Set oRatio = PointOnCurve.Ratio

        :rtype: RealParam
        """

        return RealParam(self.hybrid_shape_point_on_curve.Ratio)

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Type() As long (Read Only)
                | 
                |     Returns the distance stored value type.
                |     Legal values:
                | 
                |         1 when the type of measure is the length
                |         -1 when the type of measure is the distance ratio
                | 
                |     Example:
                | 
                |           This example retrieves in oType the distance type computation
                |           
                |          for the pointOnCurve hybrid shape object.
                |          
                | 
                |          Dim oType As long
                |          Set oType = pointOnCurve.Type

        :rtype: int
        """

        return self.hybrid_shape_point_on_curve.Type

    def __repr__(self):
        return f'HybridShapePointOnCurve(name="{self.name}")'
