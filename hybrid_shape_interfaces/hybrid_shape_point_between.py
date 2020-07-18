#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.point import Point
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.real_param import RealParam


class HybridShapePointBetween(Point):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointBetween
                | 
                | Represents the hybrid shape PointBetween feature object.
                | Role: To access the data of the hybrid shape PointBetween feature
                | object.
                | This data includes:
                | 
                |     The first reference point
                |     The second reference point 
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_point_between = com_object

    @property
    def first_point(self) -> Reference:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FirstPoint() As Reference
                | 
                |     Returns or sets the first reference point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in RefPoint1 the first reference point for the
                |         PointBetween hybrid shape feature.
                | 
                |          Dim RefPoint1 As Reference
                |          Set RefPoint1 = PointBetween.FirstPoint

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_between.FirstPoint)

    @first_point.setter
    def first_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_point_between.FirstPoint = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Orientation() As long
                | 
                |     Returns or sets the orientation. Role:
                |     Orientation = 1 means that distance is measured from the second point
                | 
                |     Example:
                |         This example retrieves in Orient the orientation for the PointBetween
                |         hybrid shape feature.
                | 
                |          Dim Orient As long
                |          Set Orient = PointBetween.Orientation

        :return: int
        :rtype: int
        """

        return self.hybrid_shape_point_between.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_point_between.Orientation = value

    @property
    def ratio(self) -> RealParam:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Ratio() As RealParam (Read Only)
                | 
                |     Get the ratio. Role:
                |     if d1 is the distance between the first point and the created point, and d2 is the distance
                |     between the first point and the second point, then ratio = d1/d2.
                | 
                |     Example:
                |         This example retrieves in ratio the orientation for the PointBetween
                |         hybrid shape feature.
                | 
                |          Dim ratio  As CATIARealParam
                |          Get ratio = PointBetween.Ratio

        :return: RealParam
        :rtype: RealParam
        """

        return RealParam(self.hybrid_shape_point_between.Ratio)

    @property
    def second_point(self) -> Reference:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SecondPoint() As Reference
                | 
                |     Returns or sets the second reference point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in RefPoint2 the second reference point for the
                |         PointBetween hybrid shape feature.
                | 
                |          Dim RefPoint2 As Reference
                |          Set RefPoint2 = PointBetween.SecondPoint

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_between.SecondPoint)

    @second_point.setter
    def second_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_point_between.SecondPoint = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or Sets the support.
                |     Note: the support can be surface or curve. It is not
                |     mandatory
                | 
                |     Sub-element(s) supported (see Boundary object): Face and TriDimFeatEdge and
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in oSupport the support(if it exist) for the
                |         PointBetween hybrid shape feature.
                | 
                |          Dim oSupport As Reference 
                |          Set oSupport = PointBetween.Support

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_point_between.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_point_between.Support = value

    def __repr__(self):
        return f'HybridShapePointBetween(name="{self.name}")'
