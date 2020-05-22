#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA R25 on 2020-05-22 12:54:36.956119

from pycatia.mec_mod_interfaces.hybridshape import HybridShape


class HybridShapePointOnCurve(HybridShape):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents the hybrid shape point on a curve.Role: To access the data
                | of the point object created on a curve. This data includes:

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_on_curve = com_object     

    @property
    def curve(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Curve
                | o Property Curve(    ) As
                | 
                | Returns or sets the curve onto which the point is or should
                | be created. Sub-element(s) supported (see object): or .
                | 
                |
                | Example:
                | This example retrieves in oCurve the supporting
                | curve for the pointOnCurve hybrid shape point. Dim oCurve As
                | CATIAReference Set oCurve = pointOnCurve.Curve

        :return:
        """
        return self.hybrid_shape_point_on_curve.Curve

    @curve.setter
    def curve(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_on_curve.Curve = value 

    @property
    def direction(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Direction
                | o Property Direction(    ) As
                | 
                | Returns or sets the direction along which the point is or
                | should be created. Example This example retrieves in Dir the
                | direction for the PointOnCurve hybrid shape feature. Dim Dir
                | As CATIAHybridShapeDirection Set Dir=pointOnCurve.Direction

        :return:
        """
        return self.hybrid_shape_point_on_curve.Direction

    @direction.setter
    def direction(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_on_curve.Direction = value 

    @property
    def distance_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | DistanceType
                | o Property DistanceType(    ) As
                | 
                | Returns or sets the distance type. Legal values: 1 for
                | geodesic, -1 for euclidean. Default is geodesic. Geodesic
                | means that the distance is measured with a curvilinear
                | abscissa Euclidean means that the point is created as the
                | intersection between the reference curve and a circle whose
                | radius is the length defined above. 
                |
                | Example:
                | This example
                | retrieves in oDistanceType the distance computation type
                | used for the pointOnCurve hybrid shape object. Dim
                | oDistanceType As long Set oDistanceType =
                | pointOnCurve.DistanceType

        :return:
        """
        return self.hybrid_shape_point_on_curve.DistanceType

    @distance_type.setter
    def distance_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_on_curve.DistanceType = value 

    @property
    def offset(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Offset
                | o Property Offset(    ) As   (Read Only)
                | 
                | Returns the distance to the reference point. This distance
                | is a distance in a length unit, The distance can be null.In
                | this case, the reference point is the curve end point
                | defined using the Orientation parameter. 
                |
                | Example:
                | This
                | example retrieves in oOffset the distance from the reference
                | point on the supporting curve for the pointOnCurve hybrid
                | shape object. Dim oOffset As CATIALength Set oOffset =
                | pointOnCurve.Offset

        :return:
        """
        return self.hybrid_shape_point_on_curve.Offset

    @property
    def on_curve_type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | OnCurveType
                | o Property OnCurveType(    ) As
                | 
                | Returns or sets the OnCurve type for created point on curve.
                | Legal values: 0 = Distance on curve 1 = Distance along
                | direction 2 = Ratio of Curve length

        :return:
        """
        return self.hybrid_shape_point_on_curve.OnCurveType

    @on_curve_type.setter
    def on_curve_type(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_on_curve.OnCurveType = value 

    @property
    def orientation(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Orientation
                | o Property Orientation(    ) As
                | 
                | Returns or sets the curve orientation. Legal values: -1
                | means that the distance (length or ratio) is measured: in
                | the other orientation of the curve, when a reference point
                | has been set in the other orientation of the curve and from
                | the other extremity, when no reference point has been set.
                | 
                |
                | Example:
                | This example retrieves in oOrientation curve
                | Orientation use for the pointOnCurve hybrid shape feature.
                | Dim oOrientation As long Set oOrientation =
                | pointOnCurve.Orientation

        :return:
        """
        return self.hybrid_shape_point_on_curve.Orientation

    @orientation.setter
    def orientation(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_on_curve.Orientation = value 

    @property
    def point(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Point
                | o Property Point(    ) As
                | 
                | Returns or sets the reference point. If the point does not
                | lie on the curve, the point on the curve with the smallest
                | distance to this point is taken. The reference point may not
                | exist. In this case, the extremity of the curve is taken as
                | reference point. Sub-element(s) supported (see object): .
                | 
                |
                | Example:
                | This example retrieves in oRefPoint the reference
                | point on the supporting curve for the pointOnCurve hybrid
                | shape object. Dim oRefPoint As CATIAReference Set oRefPoint
                | = pointOnCurve.Point

        :return:
        """
        return self.hybrid_shape_point_on_curve.Point

    @point.setter
    def point(self, value):
        """
            :param type value:
        """
        self.hybrid_shape_point_on_curve.Point = value 

    @property
    def ratio(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Ratio
                | o Property Ratio(    ) As   (Read Only)
                | 
                | Returns the distance ratio to the reference point. This is a
                | real parameter which corresponds to the ratio of the
                | distance from the reference point with respect to the length
                | of the supporting curve. The ratio can be null. In this
                | case, the reference point is the curve end point defined
                | using the Orientation parameter. 
                |
                | Example:
                | This example
                | retrieves in oRatio the distance ratio from the reference
                | point on the supporting curve for the pointOnCurve hybrid
                | shape object. Dim oRatio As CATIALength Set oRatio =
                | PointOnCurve.Ratio

        :return:
        """
        return self.hybrid_shape_point_on_curve.Ratio

    @property
    def type(self):
        """
        .. note::
            CAA V5 Visual Basic help

                | Type
                | o Property Type(    ) As   (Read Only)
                | 
                | Returns the distance stored value type. Legal values: 1 when
                | the type of measure is the length -1 when the type of
                | measure is the distance ratio 
                |
                | Example:
                | This example
                | retrieves in oType the distance type computation for the
                | pointOnCurve hybrid shape object. Dim oType As long Set
                | oType = pointOnCurve.Type

        :return:
        """
        return self.hybrid_shape_point_on_curve.Type

    def __repr__(self):
        return f'HybridShapePointOnCurve()'
