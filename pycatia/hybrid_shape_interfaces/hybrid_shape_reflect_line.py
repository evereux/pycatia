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
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeReflectLine(HybridShape):
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
                |                         HybridShapeReflectLine
                | 
                | Represents the hybrid shape reflect line feature object.
                | Role: To access the data of the hybrid shape reflect line feature object. This
                | data includes:
                | 
                |     The surface used to create the reflect line
                |     The direction (cylindrical)
                |     The origin (conical)
                |     The angle value
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeReflectLine
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_reflect_line = com_object

    @property
    def angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Angle() As Angle
                | 
                |     Returns or sets the angle used to create the reflectline.
                | 
                |     Example:
                |         This example retrieves in Ang the angle for the RelectLine hybrid shape
                |         feature.
                | 
                |          Dim Ang As CATIAAngle
                |          Set Ang = ReflectLine.Angle

        :rtype: Angle
        """

        return Angle(self.hybrid_shape_reflect_line.Angle)

    @angle.setter
    def angle(self, angle: Angle):
        """
        :param Angle angle:
        """

        self.hybrid_shape_reflect_line.Angle = angle.com_object

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Direction() As HybridShapeDirection
                | 
                |     Returns or sets the direction used to create the cylindrical
                |     reflectline.
                | 
                |     Example:
                |         This example retrieves in Dir the direction for the cylindrical
                |         RelectLine hybrid shape feature.
                | 
                |          Dim Dir As CATIAHybridShapeDirection
                |          Set Dir = ReflectLine.Direction

        :rtype: HybridShapeDirection
        """

        return HybridShapeDirection(self.hybrid_shape_reflect_line.Direction)

    @direction.setter
    def direction(self, direction: HybridShapeDirection):
        """
        :param HybridShapeDirection direction:
        """

        self.hybrid_shape_reflect_line.Direction = direction.com_object

    @property
    def orientation_direction(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OrientationDirection() As long
                | 
                |     Returns or sets the direction orientation used to compute the reflect
                |     line.
                |     Role: The orientation is used to define the angle between the direction and
                |     the normal to the support of the points on the result curve. The orientation is
                |     the same than or the inverse of the result of the cross product:
                |     Normal(support) ^ Tangent(FirstReferenceCurve).
                |     Legal values: 1 for same orientation, and -1 for inverse

        :rtype: int
        """

        return self.hybrid_shape_reflect_line.OrientationDirection

    @orientation_direction.setter
    def orientation_direction(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_reflect_line.OrientationDirection = value

    @property
    def orientation_support(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OrientationSupport() As long
                | 
                |     Returns or sets the support orientation used to compute the reflect
                |     line.
                |     Role: The orientation is used to define the angle between the direction and
                |     the normal to the support of the points on the result curve. The orientation is
                |     the same than or the inverse of the result of the cross product:
                |     Normal(support) ^ Tangent(FirstReferenceCurve).
                |     Legal values: 1 for same orientation, and -1 for inverse

        :rtype: int
        """

        return self.hybrid_shape_reflect_line.OrientationSupport

    @orientation_support.setter
    def orientation_support(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_reflect_line.OrientationSupport = value

    @property
    def origin(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Origin() As Reference
                | 
                |     Returns or sets the origin point used to create the conical
                |     reflectline.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in Point the origin point for the conical
                |         ReflectLine hybrid shape feature.
                | 
                |          Dim Point As Reference
                |          Set Point = ReflectLine.Origin

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_reflect_line.Origin)

    @origin.setter
    def origin(self, reference_origin: Reference):
        """
        :param Reference reference_origin:
        """

        self.hybrid_shape_reflect_line.Origin = reference_origin.com_object

    @property
    def source_type(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SourceType() As long
                | 
                |     Returns or sets whether the reflectline curve is or should be created with
                |     infinite light source (cylindrical) or with finite point light source
                |     (conical).
                |     Role: The SourceType indicates whether the created reflectline curve is
                |     compute with infinite light source for cylindrical type or with finite point
                |     light source for conical type.
                |     Legal values: 0 for cylindrical and 1 for conical.

        :rtype: int
        """

        return self.hybrid_shape_reflect_line.SourceType

    @source_type.setter
    def source_type(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_reflect_line.SourceType = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support surface used to create the
                |     reflectline.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in Surface the support surface for the
                |         RelectLine hybrid shape feature.
                | 
                |          Dim Surface As Reference
                |          Set Surface = ReflectLine.Support

        :rtype: Reference
        """

        return Reference(self.hybrid_shape_reflect_line.Support)

    @support.setter
    def support(self, reference_support: Reference):
        """
        :param Reference reference_support:
        """

        self.hybrid_shape_reflect_line.Support = reference_support.com_object

    @property
    def type_solution(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property TypeSolution() As long
                | 
                |     Returns or sets whether the reflectline curve is or should be created with
                |     the normal to the support or the tangent plane to the
                |     support.
                |     Role: The TypeSolution indicates whether the created reflectline curve is
                |     compute with the angle between the normale to the support and the direction or
                |     with the angle between the tangent plane to the support and the
                |     direction.
                |     Legal values: 0 for the normal and 1 for the tangent plane.

        :rtype: int
        """

        return self.hybrid_shape_reflect_line.TypeSolution

    @type_solution.setter
    def type_solution(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_reflect_line.TypeSolution = value

    def invert_orientation_direction(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InvertOrientationDirection()
                | 
                |     Inverts the orientation of direction. This example inverts the direction
                |     orientation of hybRefLine hybrid shape reflect line
                |     object.
                | 
                |      hybRefLine.InvertOrientationDirection

        :rtype: None
        """
        return self.hybrid_shape_reflect_line.InvertOrientationDirection()

    def invert_orientation_support(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub InvertOrientationSupport()
                | 
                |     Inverts the orientation of support. This example inverts the support
                |     orientation of hybRefLine hybrid shape reflect line
                |     object.
                | 
                |      hybRefLine.InvertOrientationSupport

        :rtype: None
        """
        return self.hybrid_shape_reflect_line.InvertOrientationSupport()

    def __repr__(self):
        return f'HybridShapeReflectLine(name="{self.name}")'
